"""Executable fixtures for the independent public release audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.audit_public_release import audit


class ReleaseAuditFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.git("init", "-q")
        self.git("config", "user.name", "E99 fixture")
        self.git("config", "user.email", "fixture@users.noreply.github.com")
        (self.root / "docs/publication").mkdir(parents=True)
        (self.root / "reports").mkdir()
        self.write("reports/current.md", "Current scoped mathematical evidence.\n")
        self.source_digest = hashlib.sha256(b"Current scoped mathematical evidence.\n").hexdigest()
        self.set_inventory("pending provenance review")
        self.git("add", "-A")
        self.git("commit", "-qm", "fixture")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def write(self, path, contents):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(contents)

    def set_inventory(self, clearance):
        inc = {"source_commit": "1" * 40, "entries": [{
            "source_path": "reports/current.md",
            "public_path": "reports/current.md",
            "source_commit": "1" * 40,
            "source_blob": "2" * 40,
            "source_sha256": self.source_digest,
            "public_sha256": self.source_digest,
            "dependencies": [],
            "publication_clearance": clearance,
        }], "unresolved_dependencies": []}
        self.write("docs/publication/inclusion.json", json.dumps(inc))
        self.write("docs/publication/exclusion.json", "[]")

    def test_pending_rights_are_blockers(self):
        result = audit(self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertIn("rights-clearance-pending", {v["kind"] for v in result["blockers"]})

    def test_approved_records_only_are_structurally_clean(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approve synthetic fixture")
        result = audit(self.root)
        self.assertEqual(result["status"], "STRUCTURAL_PRECHECK_PASSED", result["blockers"])

    def test_changed_contents_must_match_hash(self):
        self.set_inventory("approved")
        self.write("reports/current.md", "Changed proof bytes\n")
        self.git("add", "-A")
        self.git("commit", "-qm", "change fixture")
        result = audit(self.root)
        self.assertIn("hash-mismatch", {v["kind"] for v in result["blockers"]})

    def test_non_noreply_git_email_requires_owner_signoff(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        self.git("config", "user.email", "fixture@personaldomain.example")
        self.write("reports/current.md", "Current scoped mathematical evidence.\n")
        self.git("commit", "--allow-empty", "-qm", "individual author email")
        result = audit(self.root)
        self.assertIn("personal-git-email", {v["kind"] for v in result["blockers"]})

    def test_secret_indicator_is_redacted(self):
        self.set_inventory("approved")
        content = "ghp_" + "A" * 36
        self.write("reports/accidental-token.txt", content)
        self.git("add", "-A")
        self.git("commit", "-qm", "synthetic token")
        result = audit(self.root)
        summary = json.dumps(result)
        self.assertIn("credential-indicator", summary)
        self.assertNotIn(content, summary)

    def test_restricted_pdf_is_a_blocker(self):
        self.set_inventory("approved")
        self.write("papers/unlicensed.pdf", "fixture")
        self.git("add", "-A")
        self.git("commit", "-qm", "unlicensed fixture")
        result = audit(self.root)
        self.assertIn("restricted-redistribution", {v["kind"] for v in result["blockers"]})

    def test_uncommitted_approval_cannot_clear_candidate(self):
        self.set_inventory("approved")
        result = audit(self.root)
        kinds = {v["kind"] for v in result["blockers"]}
        self.assertIn("dirty-candidate", kinds)
        self.assertIn("rights-clearance-pending", kinds)

    def test_annotated_tag_metadata_is_scanned_without_printing_email(self):
        email = "tag-fixture@personaldomain.example"
        self.git("-c", "user.email=" + email, "tag", "-a", "v-fixture", "-m", "tag")
        result = audit(self.root)
        self.assertIn("personal-git-trailer-or-tag-email", {v["kind"] for v in result["blockers"]})
        self.assertNotIn(email, json.dumps(result))

    def test_uncommitted_substitution_cannot_hide_committed_secret(self):
        secret = "ghp_" + "C" * 36
        self.write("committed.txt", secret)
        self.git("add", "-A")
        self.git("commit", "-qm", "token")
        self.write("committed.txt", "apparently clean replacement")
        result = audit(self.root)
        kinds = {v["kind"] for v in result["blockers"]}
        self.assertIn("credential-indicator", kinds)
        self.assertIn("dirty-candidate", kinds)
        self.assertNotIn(secret, json.dumps(result))



    def test_deleted_historical_token_is_still_a_blocker(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        token = "ghp_" + "A" * 36
        self.write("reports/temporary.txt", token)
        self.git("add", "-A")
        self.git("commit", "-qm", "temporary synthetic credential")
        (self.root / "reports/temporary.txt").unlink()
        self.git("add", "-A")
        self.git("commit", "-qm", "delete synthetic credential")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator",
                      {x["kind"] for x in result["blockers"]})
        self.assertNotIn(token, json.dumps(result))

    def test_deleted_historical_pdf_is_still_a_blocker(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        self.write("papers/temp.pdf", "a third-party PDF placeholder")
        self.git("add", "-A")
        self.git("commit", "-qm", "temporarily import paper")
        (self.root / "papers/temp.pdf").unlink()
        self.git("add", "-A")
        self.git("commit", "-qm", "delete paper")
        result = audit(self.root)
        self.assertIn("historical-restricted-redistribution",
                      {x["kind"] for x in result["blockers"]})

    def test_secret_on_other_branch_is_still_a_blocker(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        self.git("checkout", "-qb", "unsafe-branch")
        self.write("reports/side-branch.txt", "ghp_" + "A" * 36)
        self.git("add", "-A")
        self.git("commit", "-qm", "side branch synthetic credential")
        self.git("checkout", "-q", "-")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator",
                      {x["kind"] for x in result["blockers"]})

    def test_commit_message_secret_is_still_a_blocker(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        token = "ghp_" + "A" * 36
        self.git("commit", "--allow-empty", "-qm", "temporary " + token)
        self.git("commit", "--allow-empty", "-qm", "safe current commit")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator",
                      {x["kind"] for x in result["blockers"]})
        self.assertNotIn(token, json.dumps(result))


if __name__ == "__main__":
    unittest.main()

