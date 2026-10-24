#!/usr/bin/env python3
"""从 data/songs/*.json 生成 README.md 中的歌曲难度表。

运行：python scripts/generate.py
检查是否同步（适合 CI）：python scripts/generate.py --check
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- SONG_TABLE_START -->"
END = "<!-- SONG_TABLE_END -->"
SCORE_FIELDS = (
    "range", "melody", "rhythm", "breath",
    "pronunciation", "technique", "stability",
)
NOTE_PATTERN = re.compile(r"^([A-G])([#b]?)(-?\d+)$")
NOTE_VALUES = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
DIFFICULTY_LEVELS = ("B", "A", "S", "SS", "SSS")


class SongDataError(ValueError):
    """JSON 数据不符合歌曲格式。"""


def check_nonempty_string(value: object, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise SongDataError(f"{name} 必须是非空字符串")


def pitch_number(note: str) -> int:
    match = NOTE_PATTERN.fullmatch(note)
    if not match:
        raise SongDataError(f"无效音高 {note!r}，请使用 A3、C#5、Bb4 等格式")
    letter, accidental, octave = match.groups()
    accidental_delta = 1 if accidental == "#" else -1 if accidental == "b" else 0
    return (int(octave) + 1) * 12 + NOTE_VALUES[letter] + accidental_delta


def validate(song: object, path: Path) -> dict:
    if not isinstance(song, dict):
        raise SongDataError("顶层数据必须是 JSON 对象")

    for field in ("id", "title"):
        check_nonempty_string(song.get(field), field)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", song["id"]):
        raise SongDataError("id 必须使用小写英文、数字和连字符")
    if song["id"] != path.stem:
        raise SongDataError(f"id={song['id']!r} 与文件名 {path.name!r} 不一致")

    for field in ("producers", "vocalists"):
        items = song.get(field)
        if not isinstance(items, list) or not items:
            raise SongDataError(f"{field} 必须是非空字符串数组")
        for index, item in enumerate(items):
            check_nonempty_string(item, f"{field}[{index}]")

    bpm = song.get("bpm")
    if type(bpm) is not int or bpm <= 0:
        raise SongDataError("bpm 必须是正整数")

    vocal_range = song.get("vocal_range")
    if not isinstance(vocal_range, dict) or set(vocal_range) != {"min", "max"}:
        raise SongDataError("vocal_range 必须包含且仅包含 min、max")
    for name in ("min", "max"):
        check_nonempty_string(vocal_range[name], f"vocal_range.{name}")
    if pitch_number(vocal_range["min"]) > pitch_number(vocal_range["max"]):
        raise SongDataError("vocal_range.min 不能高于 vocal_range.max")

    scores = song.get("scores")
    if not isinstance(scores, dict):
        raise SongDataError("scores 必须是对象")
    missing = set(SCORE_FIELDS) - set(scores)
    extra = set(scores) - set(SCORE_FIELDS)
    if missing or extra:
        raise SongDataError(f"scores 字段错误：缺少 {sorted(missing)}；多余 {sorted(extra)}")
    for field in SCORE_FIELDS:
        value = scores[field]
        if type(value) is not int or not 1 <= value <= 5:
            raise SongDataError(f"scores.{field} 必须是 1～5 的整数")

    if "difficulty" in song:
        raise SongDataError("difficulty 是自动计算字段，请从歌曲 JSON 中删除")

    if "comments" in song and not isinstance(song["comments"], str):
        raise SongDataError("comments 必须是字符串")
    return song


def load_difficulty_thresholds(config_path: Path) -> dict[str, float]:
    """读取等级的最低综合分，严格要求 B < A < S < SS < SSS。"""
    try:
        config = json.loads(config_path.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, UnicodeError, OSError) as exc:
        raise SongDataError(f"无法读取配置文件 {config_path}：{exc}") from exc

    if not isinstance(config, dict) or set(config) != {"difficulty_thresholds"}:
        raise SongDataError("config.json 只能包含 difficulty_thresholds 对象")

    thresholds = config["difficulty_thresholds"]
    if not isinstance(thresholds, dict) or set(thresholds) != set(DIFFICULTY_LEVELS):
        raise SongDataError("difficulty_thresholds 必须包含且仅包含 B、A、S、SS、SSS")

    previous = None
    for level in DIFFICULTY_LEVELS:
        cutoff = thresholds[level]
        if type(cutoff) not in (int, float) or not math.isfinite(cutoff) or not 1 <= cutoff <= 5:
            raise SongDataError(f"difficulty_thresholds.{level} 必须是 1～5 的有限数字")
        if previous is not None and cutoff <= previous:
            raise SongDataError("难度阈值必须严格递增：B < A < S < SS < SSS")
        previous = cutoff
    if thresholds["B"] != 1:
        raise SongDataError("difficulty_thresholds.B 必须为 1，才能覆盖所有评分")
    return {level: float(thresholds[level]) for level in DIFFICULTY_LEVELS}


def overall_score(song: dict) -> float:
    """七项评分的算术平均值，不提前舍入。"""
    return sum(song["scores"][key] for key in SCORE_FIELDS) / len(SCORE_FIELDS)


def calculate_difficulty(overall: float, thresholds: dict[str, float]) -> str:
    for level in reversed(DIFFICULTY_LEVELS):
        if overall >= thresholds[level]:
            return level
    raise SongDataError(f"无法给平均分 {overall} 分级")


def difficulty_ranges(thresholds: dict[str, float]) -> str:
    """根据配置文件实时生成可读的等级边界说明。"""
    descriptions = []
    for index, level in enumerate(DIFFICULTY_LEVELS):
        low = thresholds[level]
        if index + 1 == len(DIFFICULTY_LEVELS):
            descriptions.append(f"{level}：{low:.2f}～5.00")
        else:
            high = thresholds[DIFFICULTY_LEVELS[index + 1]]
            descriptions.append(f"{level}：[{low:.2f}, {high:.2f})")
    return "；".join(descriptions)


def load_songs(data_dir: Path) -> list[dict]:
    if not data_dir.is_dir():
        raise SongDataError(f"歌曲目录不存在：{data_dir}")
    paths = sorted(data_dir.glob("*.json"))
    if not paths:
        raise SongDataError(f"歌曲目录中没有 JSON 文件：{data_dir}")

    songs: list[dict] = []
    ids: set[str] = set()
    for path in paths:
        try:
            song = validate(json.loads(path.read_text(encoding="utf-8-sig")), path)
        except (json.JSONDecodeError, UnicodeError, SongDataError) as exc:
            raise SongDataError(f"{path}: {exc}") from exc
        if song["id"] in ids:
            raise SongDataError(f"歌曲 ID 重复：{song['id']}")
        ids.add(song["id"])
        songs.append(song)

    # 按七项综合难度从易到难；同分时按 id 排序，确保输出稳定。
    songs.sort(key=lambda s: (sum(s["scores"][k] for k in SCORE_FIELDS), s["id"]))
    return songs


def md_cell(value: object) -> str:
    """将普通文本安全放入 Markdown 单元格。"""
    value = html.escape(str(value), quote=False)
    value = value.replace("\\", "\\\\").replace("|", "\\|")
    return value.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")


def render_content(songs: list[dict], thresholds: dict[str, float]) -> str:
    headers = (
        "歌曲", "制作人", "歌姬", "BPM", "音高范围",
        "音域", "旋律", "节奏", "气息", "咬字", "技巧", "稳定性", "综合难度", "难度等级",
    )
    lines = [
        "> 综合难度为七项评分的算术平均值（满分 5 分，包含稳定性）；按综合难度升序排列。",
        f"> 等级根据 `config.json` 中的阈值自动计算（左闭右开）：{difficulty_ranges(thresholds)}。",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for song in songs:
        score = song["scores"]
        overall = overall_score(song)
        values = [
            song["title"],
            "、".join(song["producers"]),
            "、".join(song["vocalists"]),
            song["bpm"],
            f"{song['vocal_range']['min']}～{song['vocal_range']['max']}",
            *(score[k] for k in SCORE_FIELDS),
            f"{overall:.2f}",
            calculate_difficulty(overall, thresholds),
        ]
        lines.append("| " + " | ".join(map(md_cell, values)) + " |")

    commented = [song for song in songs if song.get("comments", "").strip()]
    if commented:
        lines += ["", "### 演唱建议", ""]
        for song in commented:
            title = html.escape(song["title"], quote=False)
            comment = html.escape(song["comments"].strip(), quote=False)
            comment = comment.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")
            lines += [
                f"<details><summary>{title}</summary>",
                f"<p>{comment}</p>",
                "</details>",
                "",
            ]
    return "\n".join(lines).rstrip()


def update_readme(current: str, content: str) -> str:
    block = f"{START}\n\n{content}\n\n{END}"
    start_count = current.count(START)
    end_count = current.count(END)
    if start_count == end_count == 0:
        return current.rstrip() + ("\n\n" if current.strip() else "") + block + "\n"
    if start_count != 1 or end_count != 1:
        raise SongDataError("README 中的生成标记必须各出现一次，且顺序正确")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(current):
        raise SongDataError("README 中 SONG_TABLE_START 必须位于 SONG_TABLE_END 之前")
    return pattern.sub(lambda _: block, current, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description="生成 VOCALOID 歌曲翻唱难度 Markdown 表格")
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data" / "songs", help="歌曲 JSON 目录")
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md", help="目标 Markdown 文件")
    parser.add_argument("--config", type=Path, default=ROOT / "config.json", help="难度等级阈值配置")
    parser.add_argument("--check", action="store_true", help="仅检查 README 是否已与 JSON 同步")
    args = parser.parse_args()

    try:
        songs = load_songs(args.data_dir)
        thresholds = load_difficulty_thresholds(args.config)
        current = args.readme.read_text(encoding="utf-8") if args.readme.exists() else ""
        if not current and not args.readme.exists():
            current = "# VOCALOID 翻唱难度表\n"
        result = update_readme(current, render_content(songs, thresholds))
        if args.check:
            if result != current:
                print(f"README 需要更新：{args.readme}", file=sys.stderr)
                return 1
            print(f"校验通过：{len(songs)} 首歌曲，README 已同步。")
            return 0
        if result == current:
            print(f"没有变化：{len(songs)} 首歌曲，README 已同步。")
            return 0
        args.readme.parent.mkdir(parents=True, exist_ok=True)
        args.readme.write_text(result, encoding="utf-8")
        print(f"已生成：{args.readme}（共 {len(songs)} 首歌曲）")
        return 0
    except (SongDataError, OSError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
