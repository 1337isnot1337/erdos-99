"""Executable fixtures for the independent public release audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.audit_public_release import PRIVATE_REFERENCE_PATTERNS, audit


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

    def set_owner_attestation(self, *, email="cinnajdavis@gmail.com", exceptions=None):
        """Write the real owner-record schema for a one-file synthetic manifest."""
        manifest_path = "docs/publication/inclusion.json"
        blob = self.git("hash-object", manifest_path).stdout.decode("ascii").strip()
        self.approved_manifest_blob = blob
        manifest = json.loads((self.root / manifest_path).read_text())
        entries = manifest["entries"]
        attestation = {
            "schema_version": 1,
            "repository": "1337isnot1337/erdos-99",
            "source_manifest": {
                "path": manifest_path,
                "git_blob_sha": blob,
                "retained_source_records": len(entries),
                "source_pins": len({e["source_commit"] for e in entries}),
            },
            "owner_declaration": {
                "evidence_url": "https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207244081",
                "disposition": "OWNER AUTHORIZED FOR PROJECT-CONTROLLED SOURCE EXPRESSION",
                "license_terms": "Apache-2.0 for owner-controlled source expression",
            },
            "external_expression_review": {
                "confirmed_uncleared_redistributed_third_party_exceptions": exceptions or []
            },
            "history_email_consent": {
                "comment_url": "https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207434631",
                "personal_domain_emails_found": [email],
            },
            "release_boundaries": {
                "repository_visibility_change_authorized": False
            },
            "current_manifest_reconciliation": {
                "prior_owner_attested_manifest_git_blob_sha": blob,
                "current_manifest_git_blob_sha": blob,
                "same_810_included_public_paths_as_prior_attestation": True,
                "same_source_commit_and_12_source_pins": True,
                "changed_manifest_entry_count": 0,
                "changed_manifest_paths": [],
            },
        }
        self.write("docs/publication/owner-rights-authorization.json",
                   json.dumps(attestation, indent=2) + "\n")

    def audit_authorized(self):
        # Fixtures are intentionally tiny; simulate the fixed manifest SHA in this
        # test only. Production keeps the immutable 810-entry Git blob hard-pinned.
        with patch("tools.audit_public_release.OWNER_APPROVED_MANIFEST_BLOB",
                   self.approved_manifest_blob), \
                patch("tools.audit_public_release.OWNER_APPROVED_MANIFEST_ENTRIES", 1), \
                patch("tools.audit_public_release.OWNER_APPROVED_CHANGED_MANIFEST_ENTRIES", 0):
            return audit(self.root)

    def test_private_reference_signatures_still_detect_exact_examples(self):
        source_url = b"https://github.com/1337isnot1337/" + b"e-99/tree/main"
        worktree_path = b"/tmp/e99-" + b"private/checkout"
        self.assertTrue(PRIVATE_REFERENCE_PATTERNS["private-source-url"].search(source_url))
        self.assertTrue(PRIVATE_REFERENCE_PATTERNS["private-worktree-path"].search(worktree_path))

    def test_published_theorem_schema_has_no_private_source_identifier(self):
        schema_path = Path(__file__).resolve().parents[1] / "docs/state/theorem-state.schema.json"
        schema_bytes = schema_path.read_bytes()
        schema = json.loads(schema_bytes)
        self.assertEqual(schema["$id"], "urn:erdos-99:theorem-state.schema")
        self.assertIsNone(PRIVATE_REFERENCE_PATTERNS["private-source-url"].search(schema_bytes))

    def test_manifest_pinned_owner_authorization_clears_pending_source_rights(self):
        self.set_owner_attestation()
        self.git("add", "-A")
        self.git("commit", "-qm", "record original-source owner grant")
        result = self.audit_authorized()
        self.assertEqual(result["status"], "STRUCTURAL_PRECHECK_PASSED", result["blockers"])
        self.assertEqual(result["counts"].get("owner_attested_pending_source_records"), 1)
        self.assertEqual(result["counts"].get("pending_rights_reviews", 0), 0)

    def test_owner_authorization_fails_closed_if_manifest_changes(self):
        self.set_owner_attestation()
        self.git("add", "-A")
        self.git("commit", "-qm", "record scoped grant")
        path = "docs/publication/inclusion.json"
        changed = json.loads((self.root / path).read_text())
        changed["post_authorization_change"] = True
        self.write(path, json.dumps(changed))
        self.git("add", "-A")
        self.git("commit", "-qm", "mutate manifest after authorization")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("unverified-owner-rights-record", kinds)
        self.assertIn("rights-clearance-pending", kinds)

    def test_owner_grant_does_not_cover_independent_exception(self):
        self.set_owner_attestation(exceptions=["reports/current.md"])
        self.git("add", "-A")
        self.git("commit", "-qm", "declare unlicensed external exception")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("unverified-owner-rights-record", kinds)
        self.assertIn("rights-clearance-pending", kinds)

    def test_owner_grant_licenses_only_the_named_personal_git_email(self):
        self.set_owner_attestation()
        self.git("config", "user.email", "cinnajdavis@gmail.com")
        self.git("add", "-A")
        self.git("commit", "-qm", "owner-provided rights and email permission")
        result = self.audit_authorized()
        self.assertEqual(result["status"], "STRUCTURAL_PRECHECK_PASSED", result["blockers"])
        self.assertGreater(result["counts"].get("owner_authorized_git_email_occurrences", 0), 0)

        self.git("config", "user.email", "independent-person@example.org")
        self.git("commit", "--allow-empty", "-qm", "other contributor is not covered")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("personal-git-email", kinds)

    def test_auth_record_cannot_expand_email_consent_unilaterally(self):
        self.set_owner_attestation(email="independent-person@example.org")
        self.git("config", "user.email", "independent-person@example.org")
        self.git("add", "-A")
        self.git("commit", "-qm", "unsupported author email")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("personal-git-email", kinds)

    def test_owner_rights_attestation_never_waives_secrets(self):
        self.set_owner_attestation()
        self.write("reports/token.txt", "ghp_" + "A" * 36)
        self.git("add", "-A")
        self.git("commit", "-qm", "unsafe synthetic credential")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("historical-credential-indicator", kinds)

    def test_retargeting_both_manifest_and_record_cannot_expand_scope(self):
        self.set_owner_attestation()
        self.git("add", "-A")
        self.git("commit", "-qm", "record narrowly scoped grant")
        path = "docs/publication/inclusion.json"
        changed = json.loads((self.root / path).read_text())
        changed["post_authorization_change"] = "new contents"
        self.write(path, json.dumps(changed))
        record_path = "docs/publication/owner-rights-authorization.json"
        record = json.loads((self.root / record_path).read_text())
        record["source_manifest"]["git_blob_sha"] = self.git(
            "hash-object", path).stdout.decode("ascii").strip()
        self.write(record_path, json.dumps(record))
        self.git("add", "-A")
        self.git("commit", "-qm", "try to broaden grant to a different manifest")
        kinds = {v["kind"] for v in self.audit_authorized()["blockers"]}
        self.assertIn("unverified-owner-rights-record", kinds)
        self.assertIn("rights-clearance-pending", kinds)

    def test_pending_rights_are_blockers(self):
        result = audit(self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertIn("rights-clearance-pending", {v["kind"] for v in result["blockers"]})

    def test_frozen_target_c_source_requires_additive_rights_record(self):
        manifest = json.loads((self.root / "docs/publication/inclusion.json").read_text())
        manifest["latest_observed_source_main"] = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
        self.write("docs/publication/inclusion.json", json.dumps(manifest))
        self.git("add", "-A")
        self.git("commit", "-qm", "declare frozen source migration")
        kinds = {item["kind"] for item in audit(self.root)["blockers"]}
        self.assertIn("missing-additive-first-party-rights-record", kinds)

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

    def test_github_web_merge_noreply_email_is_safe_but_other_github_emails_are_not(self):
        self.set_inventory("approved")
        self.git("add", "-A")
        self.git("commit", "-qm", "approved fixture")
        self.git("-c", "user.email=noreply@github.com", "commit", "--allow-empty", "-qm", "GitHub web merge")
        self.git("-c", "user.email=noreply@github.com", "tag", "-a", "v-github-web-merge", "-m", "GitHub tag")
        safe = audit(self.root)
        self.assertEqual(safe["status"], "STRUCTURAL_PRECHECK_PASSED", safe["blockers"])
        self.assertEqual(safe["counts"].get("personal_domain_git_emails", 0), 0)

        self.git("-c", "user.email=person@github.com", "commit", "--allow-empty", "-qm", "unapproved GitHub-domain author")
        blocked = audit(self.root)
        self.assertIn("personal-git-email", {v["kind"] for v in blocked["blockers"]})

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

