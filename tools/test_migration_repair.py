"""Safe, source-pinned repair planning and archive writes."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from check_migration_union import AuditError, Git, digest
from repair_migration_union import ARCHIVE, apply_plan, prepare


def plan_item(path, payload, **overrides):
    """Match the source identity and archive fields returned by prepare()."""
    return dict({"source_path": path, "source_mode": "100644",
                 "source_blob": digest("blob", payload),
                 "source_sha256": hashlib.sha256(payload).hexdigest(),
                 "destination": ARCHIVE + path + ".source", "data": payload}, **overrides)


class RepairTests(unittest.TestCase):
    def test_preserves_bytes_and_never_overwrites_existing_current_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "research").mkdir()
            (root / "research/a.py").write_bytes(b"corrected destination")
            plan = [plan_item("research/a.py", b"historical source")]
            self.assertEqual(len(apply_plan(root, plan)), 1)
            self.assertEqual((root / "research/a.py").read_bytes(), b"corrected destination")
            self.assertEqual(apply_plan(root, plan), [])

    def test_preflight_rejects_conflicts_before_any_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / ARCHIVE / "b.source"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"keep")
            plan = [plan_item("a", b"new"), plan_item("b", b"different")]
            with self.assertRaises(AuditError):
                apply_plan(root, plan)
            self.assertFalse((root / ARCHIVE / "a.source").exists())

    def test_rejects_nonarchive_target(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(AuditError):
            apply_plan(Path(tmp), [plan_item("a", b"wrong", destination="docs/STATE.md")])

    def test_rejects_duplicate_plan_targets(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaises(AuditError):
            item = plan_item("a", b"x")
            apply_plan(Path(tmp), [item, item])

    def test_rejects_symlink_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "elsewhere").mkdir()
            (root / "docs").symlink_to(root / "elsewhere", target_is_directory=True)
            with self.assertRaises(AuditError):
                apply_plan(root, [plan_item("a", b"x")])

    def test_malformed_plan_raises_audit_error_before_any_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = plan_item("a", b"a")
            for field in ("source_path", "source_mode", "source_blob", "source_sha256",
                          "destination", "data"):
                bad = plan_item("b", b"b")
                del bad[field]
                with self.subTest(missing_field=field), self.assertRaises(AuditError):
                    apply_plan(root, [good, bad])
                self.assertFalse((root / good["destination"]).exists())
            for value in (None, 1, "invalid", []):
                with self.subTest(item=value), self.assertRaises(AuditError):
                    apply_plan(root, [good, value])
                self.assertFalse((root / good["destination"]).exists())
            for value in (None, 1, "invalid", {}):
                with self.subTest(plan=value), self.assertRaises(AuditError):
                    apply_plan(root, value)

    def test_corrupt_identity_cannot_bypass_payload_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for field, value in (("source_mode", "120000"), ("source_blob", "0" * 40),
                                 ("source_sha256", "0" * 64), ("data", b"other")):
                bad = plan_item("a", b"original", **{field: value})
                with self.subTest(field=field), self.assertRaises(AuditError):
                    apply_plan(root, [bad])
                self.assertFalse((root / bad["destination"]).exists())

    def test_malformed_report_raises_audit_error_before_git_reads(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Git(Path(tmp))
            for report in (None, {}, {"errors": []}, {"errors": [], "missing": {}},
                           {"errors": "", "missing": []}):
                with self.subTest(report=report), self.assertRaises(AuditError):
                    prepare(repo, report)

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
            for field in ("source_path", "source_mode", "source_blob", "source_sha256"):
                bad = dict(row)
                del bad[field]
                with self.subTest(missing_field=field), self.assertRaises(AuditError):
                    prepare(repo, {"errors": [], "missing": [bad]}, commit, tree)
            with self.assertRaises(AuditError):
                prepare(repo, {"errors": [{"bad": True}], "missing": [row]}, commit, tree)
            with self.assertRaises(AuditError):
                prepare(repo, {"errors": [], "missing": [row]}, commit, "0" * 40)


if __name__ == "__main__":
    unittest.main()
