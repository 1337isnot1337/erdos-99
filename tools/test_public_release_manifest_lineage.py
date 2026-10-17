"""Real-Git controls for retaining the approved source grant after one tool edit."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import audit_public_release as release


class ManifestLineageTests(unittest.TestCase):
    manifest_path = "docs/publication/inclusion.json"
    generator_path = "tools/build_artifact_index.py"
    old_generator = b"# approved artifact generator\n"
    new_generator = b"# generator with exact migration metadata validation\n"

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Manifest lineage fixture")
        self.git("config", "user.email", "manifest-fixture@example.invalid")
        self.write(self.generator_path, self.old_generator)
        self.write("reports/current.md", b"Unchanged scoped research.\n")
        entries = []
        for path in (self.generator_path, "reports/current.md"):
            data = (self.root / path).read_bytes()
            entries.append(dict(source_path=path, public_path=path, source_commit="1" * 40,
                                source_blob="2" * 40, source_sha256=hashlib.sha256(data).hexdigest(),
                                public_sha256=hashlib.sha256(data).hexdigest(),
                                publication_clearance="pending provenance review",
                                editorial_change="byte-identical"))
        self.approved = dict(source_commit="1" * 40, entries=entries,
                             unresolved_dependencies=[], rights_scope="original project source")
        self.write_json(self.manifest_path, self.approved)
        self.approved_blob = self.git("hash-object", self.manifest_path).decode().strip()
        self.owner_record = {
            "schema_version": 1, "repository": "1337isnot1337/erdos-99",
            "source_manifest": dict(path=self.manifest_path, git_blob_sha=self.approved_blob,
                                    retained_source_records=2, source_pins=1),
            "owner_declaration": dict(evidence_url=release.OWNER_RIGHTS_EVIDENCE,
                                      disposition="OWNER AUTHORIZED FOR PROJECT-CONTROLLED SOURCE EXPRESSION",
                                      license_terms="Apache-2.0 for project source"),
            "external_expression_review": dict(confirmed_uncleared_redistributed_third_party_exceptions=[]),
            "release_boundaries": dict(repository_visibility_change_authorized=False),
            "current_manifest_reconciliation": {
                "prior_owner_attested_manifest_git_blob_sha": self.approved_blob,
                "current_manifest_git_blob_sha": self.approved_blob,
                "same_810_included_public_paths_as_prior_attestation": True,
                "same_source_commit_and_12_source_pins": True,
                "changed_manifest_paths": [],
            },
        }
        self.write_json(release.OWNER_RIGHTS_RECORD, self.owner_record)
        self.commit("record approved source scope")
        self.owner_record_bytes = (self.root / release.OWNER_RIGHTS_RECORD).read_bytes()

    def git(self, *args):
        return subprocess.check_output(["git", "--no-replace-objects", "-C", str(self.root), *args],
                                       stderr=subprocess.PIPE)

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def write_json(self, path, data):
        self.write(path, (json.dumps(data, indent=2) + "\n").encode())

    def commit(self, message):
        self.git("add", "--all")
        self.git("commit", "-qm", message)

    def changed_manifest(self):
        changed = copy.deepcopy(self.approved)
        changed["entries"][0].update(public_sha256=hashlib.sha256(self.new_generator).hexdigest(),
                                     editorial_change="Validate exact migration metadata; original retained.")
        return changed

    def install(self, manifest):
        self.write(self.generator_path, self.new_generator)
        self.write_json(self.manifest_path, manifest)
        self.commit("apply editorial source-manifest transition")

    def permissions(self, manifest=None):
        if manifest is None:
            manifest = json.loads(self.git("show", "HEAD:" + self.manifest_path))
        with patch.object(release, "OWNER_APPROVED_MANIFEST_BLOB", self.approved_blob), \
                patch.object(release, "OWNER_APPROVED_MANIFEST_ENTRIES", 2), \
                patch.object(release, "OWNER_APPROVED_CHANGED_MANIFEST_ENTRIES", 0):
            return release.attested_owner_permissions(self.root, manifest)

    def test_original_approved_manifest_remains_accepted(self):
        result = self.permissions()
        self.assertEqual(result["imported_entries"], 2)
        self.assertIs(result["manifest_lineage"]["editorial_update"], False)

    def test_exact_tool_editorial_update_retains_original_grant(self):
        self.install(self.changed_manifest())
        result = self.permissions()
        lineage = result["manifest_lineage"]
        self.assertIs(lineage["source_scope_unchanged"], True)
        self.assertIs(lineage["owner_grant_extended"], False)
        self.assertEqual(lineage["owner_attested_manifest_git_blob_sha"], self.approved_blob)
        self.assertEqual(lineage["current_manifest_git_blob_sha"],
                         self.git("rev-parse", "HEAD:" + self.manifest_path).decode().strip())
        self.assertEqual((self.root / release.OWNER_RIGHTS_RECORD).read_bytes(), self.owner_record_bytes)

    def test_source_or_rights_fields_cannot_change(self):
        for field, value in (("source_path", "new/source.py"), ("source_commit", "3" * 40),
                             ("source_blob", "4" * 40), ("source_sha256", "5" * 64),
                             ("public_path", "tools/another.py"),
                             ("publication_clearance", "cleared"), ("new_rights_grant", True)):
            with self.subTest(field=field):
                changed = self.changed_manifest()
                changed["entries"][0][field] = value
                self.install(changed)
                self.assertIsNone(self.permissions())

    def test_new_or_removed_source_records_cannot_change_scope(self):
        for extra in (True, False):
            with self.subTest(extra=extra):
                changed = self.changed_manifest()
                if extra:
                    changed["entries"].append(copy.deepcopy(changed["entries"][1]))
                else:
                    changed["entries"].pop()
                self.install(changed)
                self.assertIsNone(self.permissions())

    def test_top_level_scope_and_another_file_hash_cannot_change(self):
        changed = self.changed_manifest()
        changed["rights_scope"] = "expanded grant"
        self.install(changed)
        self.assertIsNone(self.permissions())
        changed = self.changed_manifest()
        changed["entries"][1]["public_sha256"] = "0" * 64
        self.install(changed)
        self.assertIsNone(self.permissions())

    def test_wrong_public_hash_or_empty_editorial_description_is_rejected(self):
        for field, value in (("public_sha256", "0" * 64), ("editorial_change", " ")):
            with self.subTest(field=field):
                changed = self.changed_manifest()
                changed["entries"][0][field] = value
                self.install(changed)
                self.assertIsNone(self.permissions())

    def test_worktree_generator_cannot_substitute_for_committed_bytes(self):
        self.write_json(self.manifest_path, self.changed_manifest())
        self.commit("manifest claims bytes absent from committed generator")
        self.write(self.generator_path, self.new_generator)
        self.assertIsNone(self.permissions())

    def test_retargeting_owner_record_or_uncommitted_manifest_cannot_extend_grant(self):
        self.install(self.changed_manifest())
        changed = self.changed_manifest()
        changed["new_uncommitted_scope"] = True
        self.assertIsNone(self.permissions(changed))
        record = copy.deepcopy(self.owner_record)
        record["source_manifest"]["git_blob_sha"] = self.git(
            "rev-parse", "HEAD:" + self.manifest_path).decode().strip()
        self.write_json(release.OWNER_RIGHTS_RECORD, record)
        self.commit("retarget attestation to editorial manifest")
        self.assertIsNone(self.permissions())


if __name__ == "__main__":
    unittest.main()
