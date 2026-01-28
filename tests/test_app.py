import json
import os
import tempfile
import unittest
from pathlib import Path

import streak_cli.app as app


class TestStreakCli(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.data_path = Path(self._tmpdir.name) / "data.json"
        os.environ["STREAK_CLI_DATA"] = str(self.data_path)

    def tearDown(self):
        os.environ.pop("STREAK_CLI_DATA", None)
        self._tmpdir.cleanup()

    def test_add_note_creates_file(self):
        app.add_note("hello")
        self.assertTrue(self.data_path.exists())

        raw = json.loads(self.data_path.read_text(encoding="utf-8"))
        self.assertEqual(len(raw), 1)
        self.assertEqual(raw[0]["text"], "hello")
        self.assertIn("ts", raw[0])

    def test_list_notes_limit(self):
        for i in range(30):
            app.add_note(f"n{i}")
        notes = app.list_notes(limit=5)
        self.assertEqual(len(notes), 5)
        self.assertEqual(notes[0].text, "n25")
        self.assertEqual(notes[-1].text, "n29")

    def test_add_note_rejects_empty(self):
        with self.assertRaises(ValueError):
            app.add_note("   ")


if __name__ == "__main__":
    unittest.main()
