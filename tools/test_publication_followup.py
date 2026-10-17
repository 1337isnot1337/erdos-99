"""Operational follow-ups cannot substitute proofs or lose baseline bytes."""
import copy
import json
import unittest
from unittest.mock import patch

import publication_followup as m


class FollowupTests(unittest.TestCase):
    def fixture(self):
        old, new = b"old source\n", b"repaired source\n"
        before, after = m.identity(old, "100644"), m.identity(new, "100644")
        blobs = {before["git_blob_sha1"]: old, after["git_blob_sha1"]: new}
        path = "README.md"
        archive = m.ARCHIVE + path + ".source"
        row = {"path": path, "before": before, "after": after,
               "preserved_original": archive, "reason": "Fixture repair."}
        ledger = {"schema": "erdos-99-publication-polish/v1",
                  "baseline_commit": m.BASELINE, "edits": [row]}
        tree = {path: ("100644", after["git_blob_sha1"]),
                archive: ("100644", before["git_blob_sha1"])}
        return path, before, blobs, tree, ledger

    def verify(self, before, blobs, tree, ledger):
        tree = dict(tree)
        data = json.dumps(ledger).encode()
        obj = m.identity(data, "100644")["git_blob_sha1"]
        blobs = dict(blobs, **{obj: data})
        tree[m.LEDGER] = ("100644", obj)
        with patch.object(m, "BASELINE_ENTRIES", {"README.md": ["100644", before["git_blob_sha1"]]}):
            return m.original_tree(blobs.__getitem__, tree)

    def test_exact_operational_edit_retains_old_identity(self):
        path, before, blobs, tree, ledger = self.fixture()
        original, edited = self.verify(before, blobs, tree, ledger)
        self.assertEqual(original[path], ("100644", before["git_blob_sha1"]))
        self.assertEqual(edited, {path})

    def test_missing_or_changed_archive_fails(self):
        for mode in ("missing", "changed"):
            with self.subTest(mode=mode):
                path, before, blobs, tree, ledger = self.fixture()
                archive = m.ARCHIVE + path + ".source"
                if mode == "missing":
                    del tree[archive]
                else:
                    tree[archive] = tree[path]
                with self.assertRaises(ValueError):
                    self.verify(before, blobs, tree, ledger)

    def test_mathematical_path_cannot_be_authorized_by_the_ledger(self):
        _, before, blobs, tree, ledger = self.fixture()
        ledger["edits"][0]["path"] = "docs/targets/target-c/CURRENT.md"
        with self.assertRaisesRegex(ValueError, "unapproved"):
            self.verify(before, blobs, tree, ledger)

    def test_omitted_or_duplicate_edit_is_rejected(self):
        for mode in ("omitted", "duplicate"):
            with self.subTest(mode=mode):
                _, before, blobs, tree, ledger = self.fixture()
                if mode == "omitted":
                    ledger["edits"] = []
                else:
                    ledger["edits"] *= 2
                with self.assertRaises(ValueError):
                    self.verify(before, blobs, tree, ledger)

    def test_symlink_mode_and_changed_after_bytes_are_rejected(self):
        for mode in ("symlink", "bytes"):
            with self.subTest(mode=mode):
                path, before, blobs, tree, ledger = self.fixture()
                if mode == "symlink":
                    tree[path] = ("120000", tree[path][1])
                    ledger["edits"][0]["after"]["mode"] = "120000"
                else:
                    ledger["edits"][0]["after"]["sha256"] = "0" * 64
                with self.assertRaises(ValueError):
                    self.verify(before, blobs, tree, ledger)
