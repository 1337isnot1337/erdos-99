"""Safe, source-pinned repair planning and archive writes."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from check_migration_union import AuditError, Git, digest
from repair_migration_union import ARCHIVE, apply_plan, prepare


class RepairTests(unittest.TestCase):
    def test_preserves_bytes_and_never_overwrites_existing_current_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "research").mkdir()
            (root / "research/a.py").write_bytes(b"corrected destination")
            plan = [{"destination": ARCHIVE + "research/a.py.source", "data": b"historical source"}]
            self.assertEqual(len(apply_plan(root, plan)), 1)
            self.assertEqual((root / "research/a.py").read_bytes(), b"corrected destination")
            self.assertEqual(apply_plan(root, plan), [])

    def test_preflight_rejects_conflicts_before_any_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / ARCHIVE / "b.source"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"keep")
            plan = [{"destination": ARCHIVE + "a.source", "data": b"new"},
                    {"destination": ARCHIVE + "b.source", "data": b"different"}]
            with self.assertRaises(AuditError):
                apply_plan(root, plan)
            self.assertFalse((root / ARCHIVE / "a.source").exists())

    def test_rejects_nonarchive_target(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(AuditError):
            apply_plan(Path(tmp), [{"destination": "docs/STATE.md", "data": b"wrong"}])

    def test_rejects_duplicate_plan_targets(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(AuditError):
            item = {"destination": ARCHIVE + "a.source", "data": b"x"}
            apply_plan(Path(tmp), [item, item])

    def test_rejects_symlink_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "elsewhere").mkdir()
            (root / "docs").symlink_to(root / "elsewhere", target_is_directory=True)
            with self.assertRaises(AuditError):
                apply_plan(root, [{"destination": ARCHIVE + "a.source", "data": b"x"}])

    def test_prepare_reads_pinned_commit_not_dirty_working_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = Git(root)
            repo.run("init", "-q")
            repo.run("config", "user.name", "test")
            repo.run("config", "user.email", "test@example.invalid")
            (root / "research").mkdir()
            (root / "research/a.py").write_bytes(b"pinned")
            repo.run("add", "research/a.py")
            repo.run("commit", "-qm", "source")
            commit = repo.resolve("HEAD")
            tree = repo.run("rev-parse", "HEAD^{tree}").decode().strip()
            (root / "research/a.py").write_bytes(b"dirty uncommitted")
            row = {"source_path": "research/a.py", "source_mode": "100644",
                   "source_blob": digest("blob", b"pinned"),
                   "source_sha256": hashlib.sha256(b"pinned").hexdigest()}
            result = prepare(repo, {"errors": [], "missing": [row]}, commit, tree)
            self.assertEqual(result[0]["data"], b"pinned")
            with self.assertRaises(AuditError):
                prepare(repo, {"errors": [{"bad": True}], "missing": [row]}, commit, tree)
            with self.assertRaises(AuditError):
                prepare(repo, {"errors": [], "missing": [row]}, commit, "0" * 40)


if __name__ == "__main__":
    unittest.main()
