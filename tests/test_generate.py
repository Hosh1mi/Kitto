"""Regression checks for optional metadata and configurable scoring."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("generate", Path(__file__).resolve().parents[1] / "scripts/generate.py")
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.song = {
            "id": "example", "title": "Example", "producers": [], "vocalists": [],
            "bpm": "", "vocal_range": {"min": "", "max": ""},
            "scores": {}, "comments": "",
        }
        self.thresholds, self.weights = generate.load_config(generate.ROOT / "config.json")

    def validate(self, song=None):
        return generate.validate(self.song if song is None else song, Path("example.json"))

    def test_bpm_values_preserve_display(self):
        for bpm in (186, "186", "200~~205", 120.5, "120.5~~125", "", None):
            with self.subTest(bpm=bpm):
                self.song["bpm"] = bpm
                self.validate()
                rendered = generate.render_content([self.song], self.thresholds, self.weights)
                if bpm:
                    self.assertIn(str(bpm).replace("~", "&#126;"), rendered)
                self.assertNotIn("None", rendered)
        for bpm in (True, 0, -1, "205~~200", "0~~200", "186 bpm", float("nan")):
            self.song["bpm"] = bpm
            with self.subTest(invalid=bpm), self.assertRaises(generate.SongDataError):
                self.validate()

    def test_missing_blank_and_partial_scores_do_not_calculate(self):
        variants = ({}, {"range": 3}, {key: "" for key in generate.SCORE_FIELDS}, None, "")
        for scores in variants:
            with self.subTest(scores=scores):
                song = copy.deepcopy(self.song)
                song["scores"] = scores
                self.validate(song)
                self.assertIsNone(generate.overall_score(song, self.weights))
                self.assertNotIn("| B |", generate.render_content([song], self.thresholds, self.weights))
        del self.song["scores"]
        self.validate()
        self.assertIsNone(generate.overall_score(self.song, self.weights))

    def test_manual_difficulty_with_and_without_scores(self):
        self.song["difficulty"] = "SSS"
        self.validate()
        self.assertIn("| SSS |", generate.render_content([self.song], self.thresholds, self.weights))
        self.song["scores"] = {key: 1 for key in generate.SCORE_FIELDS}
        self.assertIn("| 1.00 | SSS |", generate.render_content([self.song], self.thresholds, self.weights))
        self.song["difficulty"] = ""
        self.assertIn("| 1.00 | B |", generate.render_content([self.song], self.thresholds, self.weights))

    def test_weighted_score_and_weighted_sort(self):
        self.song["scores"] = {key: 1 for key in generate.SCORE_FIELDS}
        self.song["scores"]["range"] = 5
        weights = {key: 1 for key in generate.SCORE_FIELDS}
        weights["range"] = 6
        self.assertEqual(generate.overall_score(self.song, weights), 3)
        other = copy.deepcopy(self.song)
        other.update(id="other", title="Other", scores={key: 2 for key in generate.SCORE_FIELDS})
        blank = copy.deepcopy(self.song)
        blank.update(id="blank", title="Blank", scores={})
        table = generate.render_content([blank, self.song, other], self.thresholds, weights)
        self.assertLess(table.index("| Other |"), table.index("| Example |"))
        self.assertLess(table.index("| Example |"), table.index("| Blank |"))

    def test_bad_scores_and_difficulties_are_rejected(self):
        for scores in ({"range": 0}, {"range": True}, {"range": 6}, {"typo": 3}):
            self.song["scores"] = scores
            with self.assertRaises(generate.SongDataError):
                self.validate()
        self.song["scores"] = {}
        self.song["difficulty"] = "Impossible"
        with self.assertRaises(generate.SongDataError):
            self.validate()

    def test_unknown_or_partial_pitch_ranges(self):
        for pitch_range in (None, "", {"min": "", "max": "C5"}, {"min": "A3", "max": None}):
            song = copy.deepcopy(self.song)
            song["vocal_range"] = pitch_range
            self.validate(song)
            self.assertNotIn("None", generate.render_content([song], self.thresholds, self.weights))
        self.song["vocal_range"] = {"min": "C5", "max": "C4"}
        with self.assertRaises(generate.SongDataError):
            self.validate()

    def test_invalid_weight_config(self):
        config = json.loads((generate.ROOT / "config.json").read_text())
        for invalid in (-1, True, "1", float("inf")):
            config["score_weights"]["range"] = invalid
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "config.json"
                path.write_text(json.dumps(config))
                with self.subTest(weight=invalid), self.assertRaises(generate.SongDataError):
                    generate.load_config(path)
        config["score_weights"] = {key: 0 for key in generate.SCORE_FIELDS}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "config.json"
            path.write_text(json.dumps(config))
            with self.assertRaises(generate.SongDataError):
                generate.load_config(path)

    def test_weight_scaling_preserves_grade_boundaries(self):
        for value in (1, 3, 4, 5):
            self.song["scores"] = {key: value for key in generate.SCORE_FIELDS}
            self.assertEqual(generate.overall_score(self.song, self.weights), value)
        weights = {key: 0 for key in generate.SCORE_FIELDS}
        weights["range"] = 1e308
        self.assertEqual(generate.overall_score(self.song, weights), 5)


if __name__ == "__main__":
    unittest.main()
