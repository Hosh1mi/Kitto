#!/usr/bin/env python3
"""从 data/songs/*.json 生成 README.md 中的歌曲难度表。
README 里仅记录歌曲名、P 主、歌姬、总体难度与总体评分。
export.csv 里还会记录详细评分与评价。

运行：python scripts/generate.py

可选 option:
    --csv   同时在根目录生成 export.csv
    --check 仅检查是否存在不合理的数据，不修改输出文件
    --list  同时在根目录生成 list.txt，记录所有有效歌曲名

不合理的歌曲整首跳过；配置中的无效项跳过并禁用依赖它们的计算。
校验问题集中记录在根目录的 generate.log（每次运行覆盖）。
空值指字段缺失、null 或空字符串；空评分不参与计算，七项齐全才计算总分。
阈值按 JSON 中的顺序不递减，低于最低阈值的歌曲不自动评级。
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import math
import re
import string
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- SONG_TABLE_START -->"
END = "<!-- SONG_TABLE_END -->"
SCORE_FIELDS = (
    "range", "melody", "rhythm", "breath",
    "pronunciation", "technique", "stability",
)
HEADERS = ("歌曲", "制作人", "歌姬", "难度等级", "综合难度")
DETAIL_HEADERS = ("音高范围", "BPM", "音域", "旋律", "节奏", "气息", "咬字", "技巧", "稳定性", "评价")
BPM_PATTERN = re.compile(r"\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?", re.ASCII)
MD_TEXT_ESCAPES = str.maketrans({char: f"&#{ord(char)};" for char in string.punctuation})
LOG = logging.getLogger(__name__)


class SongDataError(ValueError):
    """输入数据不符合要求。"""


def is_blank(value: object) -> bool:
    return value is None or value == ""


def is_number(value: object) -> bool:
    # bool 是 int 的子类，但不是评分；JSON 的 NaN/Infinity 也不能用于计算。
    return type(value) is int or (type(value) is float and math.isfinite(value))


def read_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise SongDataError("顶层数据必须是 JSON 对象")
    return value


DATA_ERRORS = (OSError, UnicodeError, ValueError, OverflowError, RecursionError)


def validate(song: dict) -> dict:
    """集中校验并标准化生成所用字段；不检查 sources 和额外维度。"""
    errors = []
    for field in ("id", "title"):
        if not isinstance(song.get(field), str):
            errors.append(f"{field} 必须是字符串")
    for field in ("producers", "vocalists"):
        if not isinstance(song.get(field), list):
            errors.append(f"{field} 必须是列表")

    bpm = song.get("bpm")
    if not is_blank(bpm) and not (
        is_number(bpm) or (isinstance(bpm, str) and BPM_PATTERN.fullmatch(bpm))
    ):
        errors.append('bpm 必须是数字、数字字符串、区间（如 "200-203"）或空值')

    vocal_range = song.get("vocal_range")
    if is_blank(vocal_range) or vocal_range == {}:
        vocal_range = {"min": "", "max": ""}
    if not isinstance(vocal_range, dict) or any(
        not isinstance(vocal_range.get(key), str) for key in ("min", "max")
    ):
        errors.append("vocal_range 必须是 min、max 均为字符串的字典，或空值")

    scores = song.get("scores")
    if is_blank(scores):
        scores = {}
    if not isinstance(scores, dict):
        errors.append("scores 必须是对象或空值")
    else:
        for field in SCORE_FIELDS:
            value = scores.get(field)
            if not is_blank(value) and not is_number(value):
                errors.append(f"scores.{field} 必须是浮点数、整数或空值")

    for field in ("difficulty", "comments"):
        value = song.get(field)
        if not is_blank(value) and not isinstance(value, str):
            errors.append(f"{field} 必须是字符串或空值")
    if errors:
        raise SongDataError("；".join(errors))
    return {
        **song,
        "bpm": "" if is_blank(bpm) else bpm,
        "vocal_range": vocal_range,
        "scores": {field: scores.get(field) for field in SCORE_FIELDS},
        "difficulty": song.get("difficulty") or "",
        "comments": song.get("comments") or "",
    }


def load_config(path: Path) -> tuple[dict[str, float], dict[str, int | float]]:
    try:
        config = read_object(path)
    except DATA_ERRORS as exc:
        LOG.warning("跳过配置 %s：%s", path, exc)
        return {}, {}

    weights = {}
    raw_weights = config.get("score_weights")
    if not isinstance(raw_weights, dict):
        LOG.warning("%s：跳过 score_weights，必须是包含七项评分维度的对象", path)
    else:
        for field in SCORE_FIELDS:
            value = raw_weights.get(field)
            if not is_number(value):
                LOG.warning("%s：跳过 score_weights.%s，缺失或不是浮点数/整数", path, field)
            else:
                weights[field] = value
        if len(weights) == len(SCORE_FIELDS) and sum(map(Fraction, weights.values())) == 0:
            LOG.warning("%s：跳过 score_weights，权重之和为零，无法计算加权平均值", path)
            weights = {}

    thresholds = {}
    raw_thresholds = config.get("difficulty_thresholds")
    if not isinstance(raw_thresholds, dict) or not raw_thresholds:
        LOG.warning("%s：跳过 difficulty_thresholds，必须是非空对象", path)
    else:
        previous = 0.0
        for level, cutoff in raw_thresholds.items():
            if type(cutoff) is not float or not math.isfinite(cutoff) or cutoff <= 0:
                LOG.warning("%s：跳过 difficulty_thresholds.%s，必须是正浮点数", path, level)
            elif cutoff < previous:
                LOG.warning("%s：跳过 difficulty_thresholds.%s，阈值不能小于前一项", path, level)
            else:
                thresholds[level] = cutoff
                previous = cutoff
    return thresholds, weights


def load_songs(data_dir: Path) -> list[dict]:
    if not data_dir.is_dir():
        LOG.warning("跳过歌曲目录 %s：目录不存在", data_dir)
        return []
    songs = []
    for path in sorted(data_dir.glob("*.json")):
        try:
            songs.append(validate(read_object(path)))
        except DATA_ERRORS as exc:
            LOG.warning("跳过歌曲 %s：%s", path, exc)
    return songs


def overall_score(song: dict, weights: dict) -> float | None:
    if any(field not in weights or is_blank(song["scores"][field]) for field in SCORE_FIELDS):
        return None
    # 精确累加避免有限输入在中间乘法、求和时溢出或丢失有效位。
    total = sum(Fraction(weights[field]) for field in SCORE_FIELDS)
    return float(sum(Fraction(song["scores"][field]) * Fraction(weights[field])
                     for field in SCORE_FIELDS) / total)


def calculate_difficulty(overall: float | None, thresholds: dict) -> str:
    if overall is not None:
        for level, cutoff in reversed(list(thresholds.items())):
            if overall >= cutoff:
                return level
    return ""


def build_rows(songs: list[dict], thresholds: dict, weights: dict) -> list[list]:
    rows = []
    ranks = {level: index for index, level in enumerate(thresholds)}
    prepared = []
    for song in songs:
        try:
            overall = overall_score(song, weights)
            difficulty = song["difficulty"] or calculate_difficulty(overall, thresholds)
            prepared.append((song, overall, difficulty))
        except DATA_ERRORS as exc:
            LOG.warning("跳过歌曲 id=%r title=%r：无法计算总分：%s", song["id"], song["title"], exc)
    prepared.sort(key=lambda item: (
        ranks.get(item[2], len(ranks)), item[1] is None,
        item[1] if item[1] is not None else 0, item[0]["title"], item[0]["id"],
    ))
    for song, overall, difficulty in prepared:
        vocal_range = song["vocal_range"]
        range_text = "～".join(vocal_range[key] for key in ("min", "max")) if any(
            vocal_range[key] for key in ("min", "max")
        ) else ""
        rows.append([
            song["title"], "、".join(map(str, song["producers"])),
            "、".join(map(str, song["vocalists"])), difficulty,
            f"{overall:.2f}" if overall is not None else "", range_text, song["bpm"],
            *("" if is_blank(song["scores"][field]) else song["scores"][field]
              for field in SCORE_FIELDS), song["comments"],
        ])
    return rows


def md_cell(value: object) -> str:
    """单次编码标点为 HTML 实体，显示原文而不触发 Markdown/HTML 语法。

    同时处理表格分隔符、强调、代码、链接、自动链接和原文本中的实体。
    只用于 Markdown 展示；CSV 与歌曲名列表保留原始文本。
    """
    text = str(value).replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    return text.translate(MD_TEXT_ESCAPES)


def render_content(rows: list[list]) -> str:
    lines = ["| " + " | ".join(HEADERS) + " |", "| " + " | ".join("---" for _ in HEADERS) + " |"]
    lines.extend("| " + " | ".join(map(md_cell, row[:len(HEADERS)])) + " |" for row in rows)
    return "\n".join(lines)


def update_readme(current: str, content: str) -> str:
    block = f"{START}\n\n{content}\n\n{END}"
    if current.count(START) == current.count(END) == 0:
        return current.rstrip() + ("\n\n" if current.strip() else "") + block + "\n"
    if current.count(START) != 1 or current.count(END) != 1 or current.index(START) > current.index(END):
        raise SongDataError("README 中的生成标记必须各出现一次，且 START 位于 END 之前")
    start, end = current.index(START), current.index(END) + len(END)
    return current[:start] + block + current[end:]


def write_readme(path: Path, rows: list[list]) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else "# VOCALOID 翻唱难度表\n"
    result = update_readme(current, render_content(rows))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(result, encoding="utf-8")


def write_csv(path: Path, rows: list[list]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS + DETAIL_HEADERS)
        writer.writerows(rows)


def write_list(path: Path, rows: list[list]) -> None:
    path.write_text("".join(row[0] + "\n" for row in rows), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="检查歌曲数据并生成歌曲难度表")
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data" / "songs", help="歌曲 JSON 目录")
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md", help="目标 Markdown 文件")
    parser.add_argument("--config", type=Path, default=ROOT / "config.json", help="评分配置")
    parser.add_argument("--csv", action="store_true", help="同时生成根目录下的 export.csv")
    parser.add_argument("--check", action="store_true", help="仅检查数据，不修改 README、CSV 或歌曲名列表")
    parser.add_argument("--list", action="store_true", help="同时生成根目录下的 list.txt")
    args = parser.parse_args()

    handler = logging.FileHandler(ROOT / "generate.log", mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    LOG.addHandler(handler)
    LOG.setLevel(logging.INFO)
    try:
        thresholds, weights = load_config(args.config)
        rows = build_rows(load_songs(args.data_dir), thresholds, weights)
        LOG.info("检查完成：%d 首有效歌曲", len(rows))
        output_failed = False
        if not args.check:
            outputs = [(args.readme, write_readme)]
            if args.csv:
                outputs.append((ROOT / "export.csv", write_csv))
            if args.list:
                outputs.append((ROOT / "list.txt", write_list))
            for path, writer in outputs:
                try:
                    writer(path, rows)
                except DATA_ERRORS as exc:
                    LOG.error("跳过输出 %s：%s", path, exc)
                    output_failed = True
        print(f"{'检查' if args.check else '生成'}完成：{len(rows)} 首有效歌曲，日志：{ROOT / 'generate.log'}")
        return 1 if output_failed else 0
    finally:
        LOG.removeHandler(handler)
        handler.close()


if __name__ == "__main__":
    raise SystemExit(main())
