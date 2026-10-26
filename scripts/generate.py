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


def is_blank(value: object) -> bool:
    return value is None or value == ""


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
        if not isinstance(items, list):
            raise SongDataError(f"{field} 必须是字符串数组（未知时使用 []）")
        for index, item in enumerate(items):
            check_nonempty_string(item, f"{field}[{index}]")

    bpm = song.get("bpm")
    if not is_blank(bpm):
        if type(bpm) in (int, float):
            valid_bpm = math.isfinite(bpm) and bpm > 0
        elif isinstance(bpm, str):
            valid_bpm = bool(re.fullmatch(r"\d+(?:\.\d+)?(?:~~\d+(?:\.\d+)?)?", bpm))
            if valid_bpm:
                bounds = [float(part) for part in bpm.split("~~")]
                valid_bpm = all(math.isfinite(n) and n > 0 for n in bounds) and bounds == sorted(bounds)
        else:
            valid_bpm = False
        if not valid_bpm:
            raise SongDataError('bpm 必须是正数、数字字符串或递增区间（如 "200~~205"），也可留空')

    vocal_range = song.get("vocal_range")
    if is_blank(vocal_range):
        vocal_range = {"min": "", "max": ""}
        song["vocal_range"] = vocal_range
    if not isinstance(vocal_range, dict) or set(vocal_range) != {"min", "max"}:
        raise SongDataError("vocal_range 必须包含且仅包含 min、max")
    for name in ("min", "max"):
        if not is_blank(vocal_range[name]):
            check_nonempty_string(vocal_range[name], f"vocal_range.{name}")
            pitch_number(vocal_range[name])
    if all(not is_blank(vocal_range[n]) for n in ("min", "max")) and pitch_number(vocal_range["min"]) > pitch_number(vocal_range["max"]):
        raise SongDataError("vocal_range.min 不能高于 vocal_range.max")

    scores = song.get("scores")
    if is_blank(scores):
        scores = {}
        song["scores"] = scores
    if not isinstance(scores, dict):
        raise SongDataError("scores 必须是对象")
    extra = set(scores) - set(SCORE_FIELDS)
    if extra:
        raise SongDataError(f"scores 字段错误：多余 {sorted(extra)}")
    for field in SCORE_FIELDS:
        value = scores.get(field)
        if not is_blank(value) and (type(value) is not int or not 1 <= value <= 5):
            raise SongDataError(f"scores.{field} 必须是 1～5 的整数或留空")

    if not is_blank(song.get("difficulty")) and song["difficulty"] not in DIFFICULTY_LEVELS:
        raise SongDataError("difficulty 必须是 B、A、S、SS、SSS 或留空")

    if "comments" in song and not isinstance(song["comments"], str):
        raise SongDataError("comments 必须是字符串")
    return song


def load_config(config_path: Path) -> tuple[dict[str, float], dict[str, float]]:
    """读取评分权重和等级最低综合分，要求 B < A < S < SS < SSS。"""
    try:
        config = json.loads(config_path.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, UnicodeError, OSError) as exc:
        raise SongDataError(f"无法读取配置文件 {config_path}：{exc}") from exc

    if not isinstance(config, dict) or set(config) != {"difficulty_thresholds", "score_weights"}:
        raise SongDataError("配置必须包含且仅包含 difficulty_thresholds、score_weights 对象")

    weights = config["score_weights"]
    if not isinstance(weights, dict) or set(weights) != set(SCORE_FIELDS):
        raise SongDataError("score_weights 必须包含且仅包含七项评分维度")
    for field, weight in weights.items():
        if type(weight) not in (int, float) or not math.isfinite(weight) or weight < 0:
            raise SongDataError(f"score_weights.{field} 必须是非负有限数字")
    if not math.isfinite(sum(weights.values())) or sum(weights.values()) <= 0:
        raise SongDataError("score_weights 权重之和必须是大于 0 的有限数字")

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
    return ({level: float(thresholds[level]) for level in DIFFICULTY_LEVELS},
            {field: float(weights[field]) for field in SCORE_FIELDS})


def overall_score(song: dict, weights: dict[str, float]) -> float | None:
    """七项全部填写后才计算加权平均值，不提前舍入。"""
    scores = song.get("scores") or {}
    if any(is_blank(scores.get(key)) for key in SCORE_FIELDS):
        return None
    scale = max(weights.values())
    scaled_weights = {key: weights[key] / scale for key in SCORE_FIELDS}
    return (math.fsum(scores[key] * scaled_weights[key] for key in SCORE_FIELDS)
            / math.fsum(scaled_weights.values()))


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

    return songs


def md_cell(value: object) -> str:
    """将普通文本安全放入 Markdown 单元格。"""
    value = html.escape(str(value), quote=False)
    # 避免 BPM 中的 ~~ 被 Markdown 渲染为删除线。
    value = value.replace("~", "&#126;")
    value = value.replace("\\", "\\\\").replace("|", "\\|")
    return value.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")


def render_content(songs: list[dict], thresholds: dict[str, float], weights: dict[str, float]) -> str:
    headers = (
        "歌曲", "制作人", "歌姬", "BPM", "音高范围",
        "音域", "旋律", "节奏", "气息", "咬字", "技巧", "稳定性", "综合难度", "难度等级",
    )
    lines = [
        "> 综合难度为七项评分的加权平均值（满分 5 分），权重见 `config.json`；七项全部填写后才计算。按综合难度升序排列，未评分歌曲按 id 排在最后。",
        f"> 等级可由歌曲的 `difficulty` 手动指定，否则根据配置阈值自动计算（左闭右开）：{difficulty_ranges(thresholds)}。",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    def sort_key(song: dict) -> tuple:
        overall = overall_score(song, weights)
        return (overall is None, overall if overall is not None else 0, song["id"])

    songs = sorted(songs, key=sort_key)
    for song in songs:
        score = song["scores"]
        overall = overall_score(song, weights)
        vocal_range = song["vocal_range"]
        range_text = "～".join(vocal_range.get(n) or "" for n in ("min", "max")) if any(vocal_range.values()) else ""
        values = [
            song["title"],
            "、".join(song["producers"]),
            "、".join(song["vocalists"]),
            song.get("difficulty") or (calculate_difficulty(overall, thresholds) if overall is not None else ""),
            song.get("bpm") or "",
            range_text,
            *(score.get(k) or "" for k in SCORE_FIELDS),
            f"{overall:.2f}" if overall is not None else "",
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
    parser.add_argument("--config", type=Path, default=ROOT / "config.json", help="难度等级阈值和评分权重配置")
    parser.add_argument("--check", action="store_true", help="仅检查 README 是否已与 JSON 同步")
    args = parser.parse_args()

    try:
        songs = load_songs(args.data_dir)
        thresholds, weights = load_config(args.config)
        current = args.readme.read_text(encoding="utf-8") if args.readme.exists() else ""
        if not current and not args.readme.exists():
            current = "# VOCALOID 翻唱难度表\n"
        result = update_readme(current, render_content(songs, thresholds, weights))
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
