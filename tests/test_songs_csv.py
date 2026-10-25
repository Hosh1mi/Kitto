"""CSV editing must round-trip data and preserve unexported metadata."""

import copy
import csv
import json
from pathlib import Path
import tempfile
import unittest

from scripts import songs_csv


class SongsCsvTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = self.root / "songs"
        self.data.mkdir()
        self.csv = self.root / "songs.csv"
        self.song = {
            "id": "example", "title": '日本語, "Title"',
            "producers": ["Producer A", "Producer B"], "vocalists": ["初音ミク"],
            "bpm": "200~~205", "vocal_range": {"min": "A3", "max": "C5"},
            "scores": {"range": 3, "melody": ""},
            "comments": '第一行,"引用"\n第二行',
            "sources": {"metadata": ["https://example.com/song"]},
            "custom": {"keep": True},
        }
        self.path = self.data / "example.json"
        self.path.write_text(json.dumps(self.song, ensure_ascii=False), encoding="utf-8")

    def export(self):
        songs_csv.export_csv(self.data, self.csv)
        with self.csv.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return list(reader)

    def write_rows(self, rows, headers=songs_csv.COLUMNS):
        with self.csv.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def test_unedited_round_trip_preserves_bytes_and_optional_fields(self):
        before = self.path.read_bytes()
        rows = self.export()
        self.assertTrue(self.csv.read_bytes().startswith(b"\xef\xbb\xbf"))
        self.assertNotIn("sources", rows[0])
        self.assertEqual(rows[0]["comments"], self.song["comments"])
        self.assertEqual(rows[0]["scores.melody"], "")
        result = songs_csv.import_csv(self.csv, self.data)
        self.assertEqual(result, {"created": 0, "updated": 0, "unchanged": 1})
        self.assertEqual(self.path.read_bytes(), before)

    def test_edits_preserve_sources_and_parse_scores(self):
        rows = self.export()
        rows[0].update({"scores.rhythm": "4.0", "scores.range": "", "difficulty": "SS",
                        "bpm": "123.5", "producers": "New A、New B"})
        self.write_rows(rows)
        songs_csv.import_csv(self.csv, self.data)
        result = json.loads(self.path.read_text())
        self.assertEqual(result["scores"]["rhythm"], 4)
        self.assertEqual(result["scores"]["range"], "")
        self.assertEqual(result["bpm"], 123.5)
        self.assertEqual(result["difficulty"], "SS")
        self.assertEqual(result["producers"], ["New A", "New B"])
        self.assertEqual(result["sources"], self.song["sources"])
        self.assertEqual(result["custom"], self.song["custom"])

    def test_null_and_omitted_fields_survive_no_op_import(self):
        for scores in (None, "", {}):
            song = dict(self.song, scores=scores, vocal_range=None, bpm=None)
            self.path.write_text(json.dumps(song))
            before = self.path.read_bytes()
            self.export()
            result = songs_csv.import_csv(self.csv, self.data)
            self.assertEqual(result["unchanged"], 1)
            self.assertEqual(self.path.read_bytes(), before)

    def test_dry_run_and_missing_csv_rows_do_not_modify_or_delete(self):
        rows = self.export()
        rows[0]["title"] = "Changed"
        self.write_rows(rows)
        before = self.path.read_bytes()
        result = songs_csv.import_csv(self.csv, self.data, dry_run=True)
        self.assertEqual(result["updated"], 1)
        self.assertEqual(self.path.read_bytes(), before)
        other = copy.deepcopy(self.song)
        other["id"] = "other"
        other_path = self.data / "other.json"
        other_path.write_text(json.dumps(other))
        songs_csv.import_csv(self.csv, self.data)
        self.assertTrue(other_path.exists())

    def test_invalid_later_row_prevents_all_writes(self):
        rows = self.export()
        rows[0]["title"] = "Changed"
        bad = dict(rows[0], id="bad")
        bad["scores.range"] = "6"
        self.write_rows([*rows, bad])
        before = self.path.read_bytes()
        with self.assertRaises(songs_csv.SongDataError):
            songs_csv.import_csv(self.csv, self.data)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse((self.data / "bad.json").exists())

    def test_duplicate_id_and_traversal_and_bad_headers_rejected(self):
        row = self.export()[0]
        for rows in ([row, row], [dict(row, id="../bad")]):
            self.write_rows(rows)
            with self.assertRaises(songs_csv.SongDataError):
                songs_csv.import_csv(self.csv, self.data)
        self.write_rows([row], [*songs_csv.COLUMNS, "sources"])
        with self.assertRaises(songs_csv.SongDataError):
            songs_csv.import_csv(self.csv, self.data)

    def test_new_song_and_json_array_names(self):
        row = self.export()[0]
        row.update(id="new-song", producers='["A、B", "[C]"]', difficulty="A")
        self.write_rows([row])
        counts = songs_csv.import_csv(self.csv, self.data)
        self.assertEqual(counts["created"], 1)
        result = json.loads((self.data / "new-song.json").read_text())
        self.assertEqual(result["producers"], ["A、B", "[C]"])
        self.assertNotIn("sources", result)
        exported = self.export()
        new_row = next(row for row in exported if row["id"] == "new-song")
        self.assertEqual(json.loads(new_row["producers"]), result["producers"])


if __name__ == "__main__":
    unittest.main()
