"""Regression tests for combined, source-identity migration coverage."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import check_migration_union as audit
import repair_migration_union as repair


def identity(path, data):
    return {"source_path": path, "source_mode": "100644",
            "source_git_blob_sha1": audit.digest("blob", data),
            "source_sha256": hashlib.sha256(data).hexdigest()}


def frozen_disposition(path, source_data, destination_data, source_tree, target=None):
    """Use the committed nested ledger format, including its identity fields."""
    return {
        "schema_version": audit.FROZEN_SCHEMA,
        "source": {"path": path, "repository": "1337isnot1337/e-99",
                   "commit": audit.SOURCE, "tree": source_tree,
                   "git_blob_sha1": audit.digest("blob", source_data),
                   "sha256": hashlib.sha256(source_data).hexdigest(), "bytes": len(source_data)},
        "destination": {"path": target or path, "repository": "1337isnot1337/erdos-99",
                        "final_mode": "100644", "final_bytes": len(destination_data),
                        "final_git_blob_sha1": audit.digest("blob", destination_data),
                        "final_sha256": hashlib.sha256(destination_data).hexdigest()},
    }


class Fixture:
    def __init__(self, directory, source, frozen=(), frozen_files=None):
        self.root = Path(directory)
        self.root.mkdir(parents=True, exist_ok=True)
        self.source = source
        self.rows = [identity(p, b) for p, b in source.items()]
        self.source_tree = audit.tree_hash(dict(audit.source_record(r) for r in self.rows))
        self.git = audit.Git(self.root)
        self.git.run("init", "-q")
        self.git.run("config", "user.name", "Migration test")
        self.git.run("config", "user.email", "migration-test@example.invalid")
        self.write("sentinel.txt", b"accepted destination must stay unchanged\n")
        self.write(audit.FROZEN, self.jsonl(list(frozen)))
        for path, data in (frozen_files or {}).items():
            self.write(path, data)
        self.base = self.commit("baseline")
        for agent, path in enumerate(audit.ASSIGNMENTS, 1):
            field = ("agent", "assigned_agent", "owner")[agent - 1]
            rows = [dict(r, **{field: (i + agent) % 3 + 1}) for i, r in enumerate(self.rows)]
            self.write(path, self.jsonl(rows))
        for path in audit.DISPOSITIONS:
            self.write(path, b"")
        self.frozen_count = len(frozen)

    @staticmethod
    def jsonl(rows):
        return b"".join(json.dumps(r, sort_keys=True).encode() + b"\n" for r in rows)

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def commit(self, message):
        self.git.run("add", "--all")
        self.git.run("commit", "-qm", message)
        return self.git.resolve("HEAD")

    def check(self):
        head = self.commit("candidate")
        return audit.audit(self.git, head, self.base, self.source_tree,
                           len(self.source), self.frozen_count)


class MigrationTests(unittest.TestCase):
    def test_git_tree_hash_matches_git_with_directory_sorting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = {"a.py": b"a", "a/file": b"b", "a0": b"c", "z/file": b"d"}
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            for p, b in source.items():
                (root / p).parent.mkdir(parents=True, exist_ok=True)
                (root / p).write_bytes(b)
            subprocess.run(["git", "-C", str(root), "add", "--all"], check=True)
            expected = subprocess.check_output(["git", "-C", str(root), "write-tree"]).decode().strip()
            actual = audit.tree_hash(dict(audit.source_record(identity(p, b)) for p, b in source.items()))
            self.assertEqual(expected, actual)

    def test_different_owners_cannot_hide_missing_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a", "research/b.py": b"b"})
            fx.write("archive/a.py", b"a")
            # All workers claiming completion for A must not discharge B.
            for agent, path in enumerate(audit.DISPOSITIONS, 1):
                row = dict(fx.rows[0], destination_path="archive/a.py",
                           destination_sha256=hashlib.sha256(b"a").hexdigest())
                fx.write(path, fx.jsonl([row]))
            report, _ = fx.check()
            self.assertFalse(report["source_main_preservation_passed"])
            self.assertEqual([r["source_path"] for r in report["missing"]], ["research/b.py"])
            self.assertEqual(len(report["duplicate_disposition_sources"]), 1)
            self.assertGreater(len(report["ownership_disagreements"]), 0)

    def test_archive_bytes_discharge_coverage_without_original_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"safe data"})
            fx.write("archive/a.py", b"safe data")
            report, replay = fx.check()
            self.assertTrue(report["source_main_preservation_passed"])
            self.assertFalse(report["deprecation_ready"])
            self.assertFalse(report["release_verified"])
            self.assertEqual(replay["research/a.py"][1], b"safe data")

    def test_agent_two_relative_prefix_is_resolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a"})
            relative = "source-main/research/a.py"
            fx.write(audit.ROOT + "agent-2/corpus/" + relative, b"a")
            fx.write(audit.DISPOSITIONS[1], fx.jsonl([
                dict(fx.rows[0], preserved_destination_path=relative)]))
            report, _ = fx.check()
            self.assertTrue(report["source_main_preservation_passed"])

    def test_changed_baseline_file_blocks_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a"})
            fx.write("research/a.py", b"a")
            fx.write("sentinel.txt", b"stale source overwrote current text")
            report, _ = fx.check()
            self.assertFalse(report["source_main_preservation_passed"])
            self.assertIn("baseline_files_changed", report["errors"][0])

    def test_replace_refs_cannot_hide_a_changed_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a"})
            fx.write("research/a.py", b"a")
            good = fx.commit("complete candidate")
            fx.write("sentinel.txt", b"changed accepted baseline")
            bad = fx.commit("corrupt candidate")
            fx.git.run("replace", bad, good)
            report, _ = audit.audit(fx.git, bad, fx.base, fx.source_tree, 1, 0)
            self.assertEqual(report["candidate_commit"], bad)
            self.assertFalse(report["source_main_preservation_passed"])
            self.assertIn("baseline_files_changed", report["errors"][0])

    def test_missing_target_is_not_resolved_by_sibling_owner_label(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a"})
            row = dict(fx.rows[0], destination_path="missing/a.py",
                       destination_sha256=hashlib.sha256(b"a").hexdigest(),
                       disposition="assigned_to_sibling")
            fx.write(audit.DISPOSITIONS[0], fx.jsonl([row]))
            report, _ = fx.check()
            self.assertTrue(report["errors"])
            self.assertTrue(report["missing"])

    def test_false_sha256_is_rejected_even_with_correct_git_blob(self):
        row = identity("research/a.py", b"a")
        tree = audit.tree_hash(dict([audit.source_record(row)]))
        bad = dict(row, source_sha256="0" * 64)
        with self.assertRaises(audit.AuditError):
            audit.inventories([[row], [bad], [row]], tree)

    def test_wrong_source_tree_rejected(self):
        with self.assertRaises(audit.AuditError):
            audit.inventories([[identity("research/a.py", b"a")]], "0" * 40)

    def test_duplicate_inventory_row_rejected(self):
        row = identity("research/a.py", b"a")
        with self.assertRaises(audit.AuditError):
            audit.inventories([[row, row]])

    def test_frozen_transformation_never_replaced_by_source_text(self):
        old, new = b"old unsupported rate", b"corrected scoped bound"
        source = {"docs/report.md": old}
        tree = audit.tree_hash(dict(audit.source_record(identity(p, b)) for p, b in source.items()))
        frozen = [frozen_disposition("docs/report.md", old, new, tree)]
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, source, frozen, {"docs/report.md": new})
            report, replay = fx.check()
            self.assertTrue(report["source_main_preservation_passed"])
            self.assertNotIn("docs/report.md", replay)
            self.assertEqual(report["coverage_counts"], {"verified_frozen_transformation": 1})

    def test_invalid_frozen_hash_is_a_failure(self):
        row = identity("docs/report.md", b"old")
        tree = audit.tree_hash(dict([audit.source_record(row)]))
        frozen = [frozen_disposition("docs/report.md", b"old", b"new", tree)]
        frozen[0]["destination"]["final_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"docs/report.md": b"old"}, frozen, {"docs/report.md": b"new"})
            report, _ = fx.check()
            self.assertFalse(report["source_main_preservation_passed"])

    def test_real_committed_frozen_record_schema(self):
        # Exact first JSONL record from the pinned 813-report ledger at
        # f282d53169df4d507117893bfdcc99f663855923; do not flatten this fixture.
        fixture = Path(__file__).parent / "fixtures/migration-union-frozen-record.json"
        row = json.loads(fixture.read_text(encoding="utf-8"))
        source = row["source"]
        records = {source["path"]: ("100644", source["git_blob_sha1"], source["sha256"])}
        path, destination = audit.frozen_record(row, records)
        self.assertEqual(path, source["path"])
        self.assertEqual(destination["path"], row["destination"]["path"])
        self.assertEqual(destination["final_bytes"], 11237)
        self.assertEqual(destination["final_git_blob_sha1"], source["git_blob_sha1"])

    def test_malformed_or_unbound_frozen_identity_rejected(self):
        source = identity("docs/report.md", b"old")
        records = dict([audit.source_record(source)])
        tree = audit.tree_hash(records)
        row = frozen_disposition("docs/report.md", b"old", b"new", tree)
        cases = (
            (None, "schema_version", "unknown/v2"),
            (None, "source", []),
            ("source", "path", "docs/unrelated.md"),
            ("source", "path", "../unsafe.md"),
            ("source", "git_blob_sha1", "0" * 40),
            ("source", "sha256", "0" * 64),
            ("source", "mode", "100755"),
            ("source", "commit", "0" * 40),
            ("source", "tree", "0" * 40),
            ("source", "repository", "other/repo"),
            ("source", "bytes", -1),
            ("source", "bytes", True),
            ("destination", "repository", "other/repo"),
            ("destination", "path", "../unsafe.md"),
            ("destination", "final_git_blob_sha1", "bad"),
            ("destination", "final_sha256", "bad"),
            ("destination", "final_mode", "120000"),
            ("destination", "final_bytes", "3"),
        )
        for section, field, value in cases:
            bad = copy.deepcopy(row)
            (bad[section] if section else bad)[field] = value
            with self.subTest(section=section, field=field), self.assertRaises(audit.AuditError):
                audit.frozen_record(bad, records, tree)

    def test_frozen_destination_mode_blob_and_size_are_checked(self):
        source = {"docs/report.md": b"old"}
        tree = audit.tree_hash(dict([audit.source_record(identity("docs/report.md", b"old"))]))
        for field, value in (("final_mode", "100755"),
                             ("final_git_blob_sha1", "0" * 40), ("final_bytes", 100)):
            row = frozen_disposition("docs/report.md", b"old", b"new", tree)
            row["destination"][field] = value
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                fx = Fixture(tmp, source, [row], {"docs/report.md": b"new"})
                report, _ = fx.check()
                self.assertFalse(report["source_main_preservation_passed"])
                self.assertEqual(report["frozen_verified_count"], 0)

    def test_frozen_source_byte_size_is_bound_when_source_is_preserved(self):
        tree = audit.tree_hash(dict([audit.source_record(identity("docs/report.md", b"old"))]))
        row = frozen_disposition("docs/report.md", b"old", b"new", tree)
        row["source"]["bytes"] = 100
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"docs/report.md": b"old"}, [row], {"docs/report.md": b"new"})
            fx.write("archive/old.md", b"old")
            with self.assertRaisesRegex(audit.AuditError, "source byte identity"):
                fx.check()

    def test_duplicate_frozen_source_rejected_even_if_first_target_is_bad(self):
        tree = audit.tree_hash(dict([audit.source_record(identity("docs/report.md", b"old"))]))
        row = frozen_disposition("docs/report.md", b"old", b"new", tree)
        row["destination"]["final_sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"docs/report.md": b"old"}, [row, row], {"docs/report.md": b"new"})
            with self.assertRaisesRegex(audit.AuditError, "repeated frozen source"):
                fx.check()

    def test_conflicting_inventory_blob_aliases_rejected(self):
        row = identity("research/a.py", b"a")
        row["source_blob"] = "0" * 40
        with self.assertRaisesRegex(audit.AuditError, "Conflicting source blob"):
            audit.source_record(row)

    def test_recovery_round_trip_uses_frozen_schema_without_overwriting_it(self):
        source = {"docs/report.md": b"old unsupported rate", "research/check.py": b"exact checker\n"}
        records = dict(audit.source_record(identity(p, b)) for p, b in source.items())
        tree = audit.tree_hash(records)
        row = frozen_disposition("docs/report.md", source["docs/report.md"], b"accepted correction", tree)
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(Path(tmp) / "destination", source, [row],
                         {"docs/report.md": b"accepted correction"})
            report, _ = fx.check()
            source_root = Path(tmp) / "source"
            source_git = audit.Git(source_root)
            source_root.mkdir()
            source_git.run("init", "-q")
            source_git.run("config", "user.name", "Migration test")
            source_git.run("config", "user.email", "migration-test@example.invalid")
            for path, data in source.items():
                target = source_root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            source_git.run("add", "--all")
            source_git.run("commit", "-qm", "pinned source")
            plan = repair.prepare(source_git, report, source_git.resolve("HEAD"), tree)
            self.assertEqual([r["source_path"] for r in plan], ["research/check.py"])
            written = repair.apply_plan(fx.root, plan)
            self.assertEqual(written, [repair.ARCHIVE + "research/check.py.source"])
            self.assertEqual(repair.apply_plan(fx.root, plan), [])
            final, _ = fx.check()
            self.assertTrue(final["source_main_preservation_passed"])
            self.assertEqual(final["frozen_verified_count"], 1)
            self.assertEqual((fx.root / "docs/report.md").read_bytes(), b"accepted correction")
            self.assertEqual((fx.root / written[0]).stat().st_mode & 0o777, 0o644)

    def test_repair_preflight_rejects_corrupt_payload_before_any_write(self):
        def item(path, data):
            return dict(identity(path, data), destination=repair.ARCHIVE + path + ".source", data=data)
        with tempfile.TemporaryDirectory() as tmp:
            good = item("research/a.py", b"a")
            bad = item("research/b.py", b"b")
            bad["data"] = b"corrupt"
            with self.assertRaisesRegex(audit.AuditError, "payload identity mismatch"):
                repair.apply_plan(Path(tmp), [good, bad])
            self.assertFalse((Path(tmp) / good["destination"]).exists())

    def test_reference_exclusion_does_not_execute_or_copy_paper(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"papers/other.pdf": b"reference", "papers/README.md": b"citation"})
            fx.write("archive/citation.md", b"citation")
            report, replay = fx.check()
            self.assertTrue(report["source_main_preservation_passed"])
            self.assertNotIn("papers/other.pdf", replay)
            self.assertIn("papers/README.md", replay)

    def test_unsafe_paths_rejected(self):
        for p in ("../a", "/tmp/a", "x/../a", ".git/config", "x//a", "x\\a", "x/./a"):
            with self.subTest(p=p), self.assertRaises(audit.AuditError):
                audit.safe_path(p)

    def test_replay_is_non_overwriting_and_regular_file_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "new"
            audit.write_replay(target, {"research/a.py": ("100755", b"raise RuntimeError('not executed')")})
            self.assertEqual((target / "research/a.py").stat().st_mode & 0o777, 0o644)
            with self.assertRaises(audit.AuditError):
                audit.write_replay(target, {})
            with self.assertRaises(audit.AuditError):
                audit.write_replay(Path(tmp) / "other", {"x": ("120000", b"/etc/passwd")})

    def test_replay_rejects_symlink_ancestor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "real").mkdir()
            (root / "link").symlink_to(root / "real", target_is_directory=True)
            with self.assertRaises(audit.AuditError):
                audit.write_replay(root / "link/new", {"a": ("100644", b"x")})

    def test_same_blob_with_multiple_destinations_uses_stable_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            fx = Fixture(tmp, {"research/a.py": b"a"})
            for path in ("long/archive/a.py", "z.py", "research/a.py"):
                fx.write(path, b"a")
            report, _ = fx.check()
            self.assertEqual(report["coverage"][0]["destination"], "research/a.py")
            self.assertEqual(len(report["duplicate_payloads"][0]["destinations"]), 3)


if __name__ == "__main__":
    unittest.main()

