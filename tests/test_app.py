import json
import tempfile
import unittest
from pathlib import Path

import streak_cli.app as app


class TestStreakCli(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.data_path = Path(self._tmpdir.name) / "data.json"
        # Patch the module-level path so tests don't touch repo files
        app.DATA_PATH = self.data_path

    def tearDown(self):
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


if __name__ == "__main__":
    unittest.main()
