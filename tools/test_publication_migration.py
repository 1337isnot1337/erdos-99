"""Negative controls for exact historical payload and baseline support policy."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import publication_migration as m


def identity(data, mode="100644", **extra):
    return dict(mode=mode, git_blob_sha1=m.blob_hash(data),
                sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), **extra)


class PolicyFixture:
    def __init__(self, root):
        self.root = Path(root)
        self.capture, self.base = {}, {}
        self.policy = dict(schema="migration-integrity-policy-v1", captured_commit=m.CAPTURE,
                           baseline_commit=m.BASE, historical_payloads=[],
                           noncanonical_metadata=[], baseline_transformations=[])
        source = dict(source_path="docs/reports/source.md", source_git_blob_sha1="a" * 40,
                      source_sha256="b" * 64)
        for name in ("agent-1/evidence/source-main-three-way-assignment.jsonl",
                     "agent-1/evidence/source-branches/source-branch-artifacts.jsonl",
                     "agent-3/branch-dispositions.jsonl", "agent-3/pr-dispositions.jsonl"):
            self.write(m.ROOT + name, (json.dumps(source) + "\n").encode())
        self.write(m.FROZEN, b"")
        self.base[m.FROZEN] = self.capture[m.FROZEN]
        self.archive = m.ROOT + "agent-1/payload/source-main/docs/reports/old.md"
        data = b"Historical source [link](not-here.md).\n"
        self.write(self.archive, data)
        self.policy["historical_payloads"].append(identity(data, path=self.archive))
        self.report = "docs/reports/imported.md"
        provenance = dict(destination_status="historical_unreviewed_noncanonical",
                          source_canonical=False, source_commit=m.SOURCE,
                          source_lifecycle="unreviewed", source_path=source["source_path"],
                          source_blob=source["source_git_blob_sha1"], source_sha256=source["source_sha256"])
        data = ("<!-- migration-provenance: " + json.dumps(provenance) + " -->\n\n"
                "> Imported source research; no destination claim is promoted.\n").encode()
        self.write(self.report, data)
        self.policy["noncanonical_metadata"].append(identity(data, path=self.report))
        self.save()

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        self.capture[path] = ("100644", m.blob_hash(data))

    def save(self):
        target = self.root / m.POLICY
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(self.policy))

    def load(self):
        def tree(_, ref):
            return self.capture if ref == m.CAPTURE else self.base
        with patch.object(m, "git_tree", tree):
            return m.load_policy(self.root)


class HistoricalPolicyTests(unittest.TestCase):
    def test_exact_historical_snapshot_and_noncanonical_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            self.assertEqual(f.load(), ({f.archive}, {f.report}))

    def test_changed_archive_bytes_and_mode_fail(self):
        for change in ("bytes", "mode"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                f = PolicyFixture(tmp)
                path = f.root / f.archive
                if change == "bytes":
                    path.write_bytes(path.read_bytes() + b"changed\n")
                else:
                    path.chmod(0o755)
                with self.assertRaises(ValueError):
                    f.load()

    def test_inventory_cannot_omit_captured_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            f.policy["historical_payloads"] = []
            f.save()
            with self.assertRaises(ValueError):
                f.load()

    def test_active_document_cannot_be_labeled_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            f.policy["historical_payloads"].append(identity((f.root / f.report).read_bytes(), path=f.report))
            f.save()
            with self.assertRaises(ValueError):
                f.load()

    def test_metadata_must_match_captured_bytes_and_source_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            f.capture[f.report] = ("100644", "c" * 40)
            with self.assertRaises(ValueError):
                f.load()

    def test_pinned_source_manifest_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            path = f.root / (m.ROOT + "agent-3/pr-dispositions.jsonl")
            path.write_bytes(b"{}\n")
            with self.assertRaises(ValueError):
                f.load()

    def test_imported_banner_cannot_exempt_canonical_metadata(self):
        import build_artifact_index as index
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            record = dict(path=f.report, artifact_id="ART-TEST", target="shared",
                          status="canonical", canonical=True, claim_ids=["claim"],
                          claim_statuses={"claim": "canonical"})
            (f.root / "index.jsonl").write_text(index.index_text([record]))
            with patch.object(m, "load_policy", return_value=(set(), {f.report})):
                errors = index.check_state(f.root, {"artifact_policy": {"index": "index.jsonl"}}, [record])
            self.assertTrue(any("metadata header" in error for error in errors))

    def test_symlink_and_nonobject_policy_rows_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            path = f.root / f.archive
            original = path.with_suffix(".saved")
            path.rename(original)
            path.symlink_to(original)
            with self.assertRaises(ValueError):
                f.load()
        with tempfile.TemporaryDirectory() as tmp:
            f = PolicyFixture(tmp)
            f.policy["historical_payloads"] = [None]
            f.save()
            with self.assertRaises(ValueError):
                f.load()


class BaselinePolicyTests(unittest.TestCase):
    def fixture(self, path="tools/check_public.py", old=b"old\n", new=b"new\n"):
        objects = {}
        def put(data):
            oid = m.blob_hash(data)
            objects[oid] = data
            return "100644", oid
        base = {path: put(old)}
        preserved = m.ROOT + "integration/baseline-originals/" + path + ".source"
        tree = {path: put(new), preserved: base[path]}
        policy = dict(schema="migration-integrity-policy-v1", captured_commit=m.CAPTURE,
                      baseline_commit=m.BASE, historical_payloads=[], noncanonical_metadata=[],
                      baseline_transformations=[dict(path=path, preserved_original=preserved,
                          before=identity(old), after=identity(new), reason="bounded support correction")])
        def save():
            tree[m.POLICY] = put(json.dumps(policy).encode())
        save()
        return objects, base, tree, policy, save

    def test_support_change_requires_exact_original_and_new_bytes(self):
        objects, base, tree, policy, save = self.fixture()
        self.assertEqual(m.permitted_baseline_changes(objects.__getitem__, tree, base), {"tools/check_public.py"})
        policy["baseline_transformations"][0]["after"]["sha256"] = "0" * 64
        save()
        with self.assertRaises(ValueError):
            m.permitted_baseline_changes(objects.__getitem__, tree, base)

    def test_proof_changes_cannot_be_authorized(self):
        objects, base, tree, _, _ = self.fixture("docs/reports/proof.md")
        with self.assertRaises(ValueError):
            m.permitted_baseline_changes(objects.__getitem__, tree, base)

    def test_original_copy_cannot_be_removed(self):
        objects, base, tree, policy, _ = self.fixture()
        del tree[policy["baseline_transformations"][0]["preserved_original"]]
        with self.assertRaises(ValueError):
            m.permitted_baseline_changes(objects.__getitem__, tree, base)

    def test_index_can_add_unreviewed_rows_but_cannot_change_old_rows(self):
        old_row = dict(path="old.md", status="canonical", canonical=True, claim_ids=["accepted"])
        new_row = dict(path="new.md", status="unreviewed", canonical=False, claim_ids=[], claim_statuses={},
                       depends_on=[], invalidates=[], supersedes=[])
        old = (json.dumps(old_row) + "\n").encode()
        new = (json.dumps(old_row) + "\n" + json.dumps(new_row) + "\n").encode()
        objects, base, tree, policy, save = self.fixture("docs/state/artifact-index.jsonl", old, new)
        self.assertEqual(m.permitted_baseline_changes(objects.__getitem__, tree, base), {"docs/state/artifact-index.jsonl"})
        bad = copy.deepcopy(old_row)
        bad["status"] = "unreviewed"
        data = (json.dumps(bad) + "\n" + json.dumps(new_row) + "\n").encode()
        oid = m.blob_hash(data)
        objects[oid] = data
        tree["docs/state/artifact-index.jsonl"] = ("100644", oid)
        policy["baseline_transformations"][0]["after"] = identity(data)
        save()
        with self.assertRaises(ValueError):
            m.permitted_baseline_changes(objects.__getitem__, tree, base)


if __name__ == "__main__":
    unittest.main()
