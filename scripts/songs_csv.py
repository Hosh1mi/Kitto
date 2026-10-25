#!/usr/bin/env python3
"""在歌曲 JSON 与 Excel 可编辑的 UTF-8 CSV 之间导入、导出。

python scripts/songs_csv.py export [data/songs.csv]
python scripts/songs_csv.py import [data/songs.csv] [--dry-run]
"""

from __future__ import annotations

import argparse
import copy
import csv
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import sys
import tempfile

try:
    from .generate import ROOT, SCORE_FIELDS, SongDataError, load_songs, validate
except ImportError:
    from generate import ROOT, SCORE_FIELDS, SongDataError, load_songs, validate


COLUMNS = (
    "id", "title", "producers", "vocalists", "bpm",
    "vocal_range.min", "vocal_range.max",
    *(f"scores.{key}" for key in SCORE_FIELDS), "difficulty", "comments",
)
LIST_SEPARATOR = "、"
ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def list_cell(items: list[str]) -> str:
    # JSON 数组用于含分隔符的名字，避免导出后无法无损导入。
    if any(LIST_SEPARATOR in item for item in items) or (items and items[0].startswith("[")):
        return json.dumps(items, ensure_ascii=False)
    return LIST_SEPARATOR.join(items)


def song_row(song: dict) -> dict[str, str]:
    row = {}
    for column in COLUMNS:
        if column in ("producers", "vocalists"):
            value = list_cell(song.get(column, []))
        elif "." in column:
            parent, child = column.split(".")
            value = (song.get(parent) or {}).get(child)
        else:
            value = song.get(column)
        row[column] = "" if value is None else str(value)
    return row


def parse_list(value: str, column: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("["):
        try:
            items = json.loads(value)
        except json.JSONDecodeError as exc:
            raise SongDataError(f"{column} 的 JSON 数组无效：{exc}") from exc
        if not isinstance(items, list) or any(not isinstance(x, str) or not x.strip() for x in items):
            raise SongDataError(f"{column} 必须是非空名字组成的 JSON 数组")
        return items
    items = [item.strip() for item in value.split(LIST_SEPARATOR)]
    if any(not item for item in items):
        raise SongDataError(f"{column} 包含空名字，请使用 {LIST_SEPARATOR} 分隔名字")
    return items


def parse_score(value: str, column: str) -> int | str:
    value = value.strip()
    if not value:
        return ""
    try:
        number = Decimal(value)
    except InvalidOperation as exc:
        raise SongDataError(f"{column} 必须是 1～5 的整数或留空") from exc
    if not number.is_finite() or not 1 <= number <= 5 or number != number.to_integral_value():
        raise SongDataError(f"{column} 必须是 1～5 的整数或留空")
    return int(number)


def parse_bpm(value: str) -> int | float | str:
    value = value.strip()
    if not value or "~~" in value:
        return value
    # 留给统一的歌曲校验器检查格式、正数和区间顺序。
    if re.fullmatch(r"\d+(?:\.\d+)?", value):
        number = Decimal(value)
        if not number.is_finite() or number > sys.float_info.max:
            raise SongDataError("bpm 超出有限数字范围")
        return int(number) if number == number.to_integral_value() else float(number)
    return value


def merge_row(row: dict[str, str], existing: dict | None, path: Path) -> dict:
    song = copy.deepcopy(existing) if existing is not None else {
        "id": row["id"], "title": "", "producers": [], "vocalists": [], "bpm": "",
        "vocal_range": {"min": "", "max": ""},
        "scores": {key: "" for key in SCORE_FIELDS}, "difficulty": "", "comments": "",
    }
    previous = song_row(song)
    for column in COLUMNS:
        value = row[column]
        if value == previous[column]:
            continue  # 保留未编辑字段的原始类型、null 及可选字段的缺省状态。
        if column in ("producers", "vocalists"):
            song[column] = parse_list(value, column)
        elif column.startswith("scores."):
            key = column.split(".")[1]
            if not isinstance(song.get("scores"), dict):
                song["scores"] = {}
            song["scores"][key] = parse_score(value, column)
        elif column.startswith("vocal_range."):
            key = column.split(".")[1]
            if not isinstance(song.get("vocal_range"), dict):
                song["vocal_range"] = {"min": "", "max": ""}
            song["vocal_range"][key] = value.strip()
        elif column == "bpm":
            song[column] = parse_bpm(value)
        else:
            song[column] = value if column in ("title", "comments") else value.strip()
    validate(copy.deepcopy(song), path)
    return song


def atomic_write(path: Path, content: str, *, encoding: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding=encoding, newline="", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
        if path.exists():
            temporary.chmod(path.stat().st_mode & 0o777)
        else:
            temporary.chmod(0o644)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def export_csv(data_dir: Path, output: Path) -> int:
    import io

    songs = load_songs(data_dir)
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(song_row(song) for song in songs)
    atomic_write(output, stream.getvalue(), encoding="utf-8-sig")
    return len(songs)


def import_csv(source: Path, data_dir: Path, *, dry_run: bool = False) -> dict[str, int]:
    pending = []
    counts = {"created": 0, "updated": 0, "unchanged": 0}
    seen = set()
    # 先校验所有行；无效 CSV 不会导致前面的歌曲被部分修改。
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        headers = reader.fieldnames or []
        if len(headers) != len(set(headers)) or set(headers) != set(COLUMNS):
            raise SongDataError(f"CSV 列错误：必须包含且仅包含 {', '.join(COLUMNS)}，不能有重复列")
        for row in reader:
            try:
                if None in row or any(value is None for value in row.values()):
                    raise SongDataError("单元格数量与表头不一致")
                if all(not value.strip() for value in row.values()):
                    continue
                song_id = row["id"]
                if not ID_PATTERN.fullmatch(song_id):
                    raise SongDataError("id 必须使用小写英文、数字和连字符，且不能有首尾空格")
                if song_id in seen:
                    raise SongDataError(f"歌曲 ID 重复：{song_id}")
                seen.add(song_id)
                path = data_dir / f"{song_id}.json"
                before = path.read_bytes() if path.exists() else None
                existing = json.loads(before.decode("utf-8-sig")) if before is not None else None
                if existing is not None:
                    validate(copy.deepcopy(existing), path)
                song = merge_row(row, existing, path)
                if song == existing:
                    counts["unchanged"] += 1
                    continue
                counts["created" if existing is None else "updated"] += 1
                pending.append((path, before, song))
            except (SongDataError, json.JSONDecodeError, UnicodeError) as exc:
                raise SongDataError(f"CSV 第 {reader.line_num} 行：{exc}") from exc
    if not seen:
        raise SongDataError("CSV 没有歌曲数据")
    if not dry_run:
        # 检查在校验期间被其他编辑器改动的文件，避免覆盖并发修改。
        for path, before, _ in pending:
            now = path.read_bytes() if path.exists() else None
            if now != before:
                raise SongDataError(f"校验期间文件发生变化，请重试：{path}")
        for path, _, song in pending:
            atomic_write(path, json.dumps(song, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="导出歌曲 CSV，或将 Excel 编辑的 CSV 合并回歌曲 JSON（保留 sources）")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("export", "import"):
        command = commands.add_parser(name)
        command.add_argument("csv_file", nargs="?", type=Path, default=ROOT / "data/songs.csv")
        command.add_argument("--data-dir", type=Path, default=ROOT / "data/songs")
        if name == "import":
            command.add_argument("--dry-run", action="store_true", help="仅校验并预览，不修改 JSON")
    args = parser.parse_args()
    try:
        if args.command == "export":
            count = export_csv(args.data_dir, args.csv_file)
            print(f"已导出 {count} 首歌曲：{args.csv_file}")
        else:
            counts = import_csv(args.csv_file, args.data_dir, dry_run=args.dry_run)
            prefix = "校验通过（未写入）" if args.dry_run else "已导入"
            print(f"{prefix}：新增 {counts['created']}，更新 {counts['updated']}，未变更 {counts['unchanged']}")
        return 0
    except (SongDataError, OSError, UnicodeError, csv.Error) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
