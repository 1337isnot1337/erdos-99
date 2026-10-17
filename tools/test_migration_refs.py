#!/usr/bin/env python3
"""Identity and output-boundary regressions for the historical migration audit."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import check_migration_refs as audit


class HistoricalIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        self.git("config", "user.name", "Migration fixture")
        self.git("config", "user.email", "fixture@example.invalid")

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args]).decode().strip()

    def commit(self, text):
        (self.repo / "captured.txt").write_text(text)
        self.git("add", "captured.txt")
        self.git("commit", "-qm", text)
        return self.git("rev-parse", "HEAD")

    def test_commit_replacement_cannot_change_exact_candidate(self):
        original = self.commit("captured bytes\n")
        replacement = self.commit("different bytes\n")
        self.git("replace", original, replacement)
        # Git's ordinary lookup sees the replacement, which reproduced a false
        # exact-SHA audit before --no-replace-objects was required.
        self.assertEqual(self.git("show", original + ":captured.txt"), "different bytes")
        snapshot = audit.Snapshot(self.repo, original)
        self.assertEqual(snapshot.commit, original)
        self.assertEqual(snapshot.read("captured.txt"), b"captured bytes\n")

    def test_captured_obligation_rewrite_refuses_audit(self):
        class RewrittenCapture:
            files = {path: ("100644", blob) for path, blob in audit.CAPTURE_BLOBS.items()}

        rewritten = RewrittenCapture()
        rewritten.files = dict(rewritten.files)
        rewritten.files[audit.DIRTY_MANIFEST] = ("100644", "0" * 40)
        with self.assertRaisesRegex(ValueError, "captured migration obligations changed"):
            audit.verify(rewritten)

    def test_output_inside_checkout_is_refused_without_writing(self):
        self.commit("captured bytes\n")
        target = self.repo / "audit.json"
        output = io.StringIO()
        with patch.object(sys, "argv", ["check_migration_refs.py", "--repo", str(self.repo), "--output", str(target)]):
            with contextlib.redirect_stdout(output):
                self.assertEqual(audit.main(), 1)
        self.assertFalse(target.exists())
        self.assertEqual(json.loads(output.getvalue())["status"], "invalid_evidence")


if __name__ == "__main__":
    unittest.main()
