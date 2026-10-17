"""Current artifact metadata does not depend on historical migration checks."""
import json
from pathlib import Path
import tempfile
import unittest

import build_artifact_index as index


class ArtifactHeaderTests(unittest.TestCase):
    def record(self, **changes):
        return dict(artifact_id="ART-TEST", path="docs/reports/working.md", target="shared",
                    status="unreviewed", canonical=False, claim_ids=[], claim_statuses={},
                    depends_on=[], invalidates=[], supersedes=[], **changes)

    def legacy(self, **changes):
        header = dict(destination_status="historical_unreviewed_noncanonical",
                      source_canonical=False, source_lifecycle="unreviewed")
        header.update(changes)
        return "<!-- migration-provenance: " + json.dumps(header) + " -->"

    def check(self, record, text):
        # Deliberately no Git repository, archive, migration policy, or ledger.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = root / record["path"]
            report.parent.mkdir(parents=True)
            report.write_text(text)
            (root / "index.jsonl").write_text(index.index_text([record]))
            return index.check_state(root, {"artifact_policy": {"index": "index.jsonl"}}, [record])

    def test_generated_current_header_is_accepted(self):
        record = self.record()
        self.assertEqual(self.check(record, index.header_for(record) + "\nWorking analysis.\n"), [])

    def test_legacy_unreviewed_body_can_change_without_migration_state(self):
        record = self.record()
        header = self.legacy()
        for body in ("Original analysis.\n", "Edited and expanded analysis.\n"):
            with self.subTest(body=body):
                self.assertEqual(self.check(record, header + "\n" + body), [])

    def test_legacy_header_may_omit_source_canonical_for_unreviewed_record(self):
        header = {"destination_status": "unreviewed_noncanonical",
                  "source_lifecycle": "unreviewed"}
        text = "<!-- migration-provenance: " + json.dumps(header) + " -->\nEdited analysis.\n"
        self.assertEqual(self.check(self.record(), text), [])

    def test_legacy_header_cannot_replace_canonical_claim_metadata(self):
        record = self.record()
        record.update(status="canonical", canonical=True, claim_ids=["Claim.1"],
                      claim_statuses={"Claim.1": "canonical"})
        errors = self.check(record, self.legacy() + "\nAnalysis.\n")
        self.assertTrue(any("metadata header" in error for error in errors))

    def test_unreviewed_claim_references_still_require_generated_metadata(self):
        record = self.record()
        record.update(claim_ids=["Claim.1"], claim_statuses={"Claim.1": "unreviewed"})
        self.assertFalse(index.legacy_unreviewed_header(self.legacy(), record))

    def test_invalid_or_promoted_legacy_header_is_not_an_alternative(self):
        headers = ("<!-- migration-provenance: invalid -->",
                   "<!-- migration-provenance: [] -->",
                   self.legacy(source_canonical=True),
                   self.legacy(source_canonical=None),
                   self.legacy(source_canonical=0),
                   self.legacy(source_canonical="false"),
                   self.legacy(source_lifecycle="canonical"),
                   self.legacy(destination_status="canonical"))
        for header in headers:
            with self.subTest(header=header):
                self.assertFalse(index.legacy_unreviewed_header(header, self.record()))

    def test_current_header_can_replace_the_legacy_format(self):
        record = self.record()
        text = self.legacy() + "\nEdited body.\n"
        rewritten = index.replace_header(text, index.header_for(record))
        self.assertEqual(self.check(record, rewritten), [])


if __name__ == "__main__":
    unittest.main()
