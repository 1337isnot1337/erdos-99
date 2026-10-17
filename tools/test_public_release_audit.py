"""Current-tree and reachable-history controls for the public release audit."""
from __future__ import annotations

import errno
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.audit_public_release import allowed_relative, audit, git as audit_git


class ReleaseAuditFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.git("init", "-q")
        self.git("config", "user.name", "E99 fixture")
        self.git("config", "user.email", "fixture@users.noreply.github.com")
        self.write("README.md", "Current project introduction.\n")
        self.write("reports/current.md", "Current scoped mathematical evidence.\n")
        self.write("tools/example.py", "print('example')\n")
        self.commit("fixture")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args],
                              check=True, capture_output=True)

    def write(self, path, contents):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(contents)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)

    def assert_clean(self):
        result = audit(self.root)
        self.assertEqual(result["status"], "STRUCTURAL_PRECHECK_PASSED", result["blockers"])
        self.assertTrue(result["full_content_scan"])
        return result

    def test_clean_repository_needs_no_import_manifests(self):
        self.assertFalse((self.root / "docs/publication").exists())
        result = self.assert_clean()
        self.assertEqual(result["candidate_commit"],
                         self.git("rev-parse", "HEAD").stdout.decode().strip())
        self.assertEqual(result["counts"]["committed_files"], 3)

    def test_readme_code_and_report_paths_can_change_freely(self):
        self.write("README.md", "Revised introduction and credits.\n")
        self.write("tools/example.py", "print('revised example')\n")
        (self.root / "reports/current.md").rename(self.root / "reports/revised.md")
        self.commit("edit documentation and code; rename report")
        self.assert_clean()

    def test_ordinary_git_emails_are_allowed(self):
        self.git("config", "user.email", "fixture@personaldomain.example")
        self.git("commit", "--allow-empty", "-qm", "attributed author")
        self.git("-c", "user.email=noreply@github.com", "commit", "--allow-empty", "-qm", "web merge")
        self.git("-c", "user.email=person@github.com", "commit", "--allow-empty", "-qm", "attribution")
        result = self.assert_clean()
        self.assertGreater(result["counts"].get("git_author_email_metadata_records", 0), 0)
        self.assertGreater(result["counts"].get("git_committer_email_metadata_records", 0), 0)

    def test_tag_and_contributor_attribution_are_allowed(self):
        self.git("-c", "user.email=tag-fixture@personaldomain.example", "tag", "-a", "v-fixture", "-m", "tag")
        self.git("commit", "--allow-empty", "-qm",
                 "preserve attribution\n\nCo-authored-by: Contributor <contributor@example.org>")
        result = self.assert_clean()
        self.assertGreaterEqual(result["counts"].get("git_tag_and_contributor_email_metadata_records", 0), 2)

    def test_secret_indicator_is_redacted(self):
        token = "ghp_" + "A" * 36
        self.write("reports/accidental-token.txt", token)
        self.commit("synthetic credential")
        result = audit(self.root)
        self.assertIn("credential-indicator", {v["kind"] for v in result["blockers"]})
        self.assertNotIn(token, json.dumps(result))

    def test_credential_in_git_author_metadata_is_blocked(self):
        token = "ghp_" + "A" * 36
        self.git("-c", "user.email=" + token + "@example.org",
                 "commit", "--allow-empty", "-qm", "synthetic credential in metadata")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator", {v["kind"] for v in result["blockers"]})
        self.assertNotIn(token, json.dumps(result))

    def test_restricted_pdf_is_a_blocker(self):
        self.write("papers/unlicensed.pdf", "fixture")
        self.commit("restricted fixture")
        result = audit(self.root)
        self.assertIn("restricted-redistribution", {v["kind"] for v in result["blockers"]})

    def test_dirty_tracked_file_is_not_a_final_candidate(self):
        self.write("README.md", "An uncommitted edit.\n")
        result = audit(self.root)
        self.assertIn("dirty-candidate", {v["kind"] for v in result["blockers"]})

    def test_untracked_file_is_not_a_final_candidate(self):
        self.write("untracked.txt", "An untracked file.\n")
        result = audit(self.root)
        self.assertIn("dirty-candidate", {v["kind"] for v in result["blockers"]})

    def test_uncommitted_substitution_cannot_hide_committed_secret(self):
        token = "ghp_" + "C" * 36
        self.write("committed.txt", token)
        self.commit("synthetic credential")
        self.write("committed.txt", "apparently clean replacement")
        result = audit(self.root)
        kinds = {v["kind"] for v in result["blockers"]}
        self.assertIn("credential-indicator", kinds)
        self.assertIn("dirty-candidate", kinds)
        self.assertNotIn(token, json.dumps(result))

    def test_deleted_historical_token_is_still_a_blocker(self):
        token = "ghp_" + "A" * 36
        self.write("reports/temporary.txt", token)
        self.commit("temporary synthetic credential")
        (self.root / "reports/temporary.txt").unlink()
        self.commit("delete synthetic credential")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator", {v["kind"] for v in result["blockers"]})
        self.assertNotIn(token, json.dumps(result))

    def test_deleted_historical_pdf_is_still_a_blocker(self):
        self.write("papers/temp.pdf", "a third-party PDF placeholder")
        self.commit("temporarily import paper")
        (self.root / "papers/temp.pdf").unlink()
        self.commit("delete paper")
        result = audit(self.root)
        self.assertIn("historical-restricted-redistribution", {v["kind"] for v in result["blockers"]})

    def test_secret_on_other_branch_is_still_a_blocker(self):
        self.git("checkout", "-qb", "unsafe-branch")
        self.write("reports/side-branch.txt", "ghp_" + "A" * 36)
        self.commit("side branch synthetic credential")
        self.git("checkout", "-q", "-")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator", {v["kind"] for v in result["blockers"]})

    def test_commit_and_tag_message_secrets_are_blocked(self):
        token = "ghp_" + "A" * 36
        self.git("commit", "--allow-empty", "-qm", "temporary " + token)
        self.git("tag", "-a", "unsafe-tag", "-m", "synthetic " + token)
        self.git("commit", "--allow-empty", "-qm", "safe current commit")
        result = audit(self.root)
        self.assertIn("historical-credential-indicator", {v["kind"] for v in result["blockers"]})
        self.assertGreater(result["counts"].get("reachable_tag_objects_scanned", 0), 0)
        self.assertNotIn(token, json.dumps(result))

    def test_symlink_is_a_blocker_in_current_tree_and_history(self):
        link = self.root / "report-link"
        try:
            link.symlink_to("reports/current.md")
        except NotImplementedError as exc:
            self.skipTest(f"native symlink fixture unavailable: {exc}")
        except OSError as exc:
            if (exc.errno in {errno.EACCES, errno.EPERM, errno.ENOSYS, errno.ENOTSUP}
                    or getattr(exc, 'winerror', None) in {1, 50, 1314}):
                self.skipTest(f"native symlink fixture unavailable: {exc}")
            raise
        self.git("config", "core.symlinks", "true")
        self.commit("symlink fixture")
        result = audit(self.root)
        kinds = {v["kind"] for v in result["blockers"]}
        self.assertIn("special-object", kinds)
        self.assertIn("symlink-or-missing", kinds)
        link.unlink()
        self.commit("delete symlink")
        result = audit(self.root)
        self.assertIn("historical-special-object", {v["kind"] for v in result["blockers"]})

    def test_paths_must_be_canonical_and_relative(self):
        for path in ("/outside", "../outside", "docs/../outside", "docs//file", "./file", "-option", "docs\\file", ""):
            with self.subTest(path=path):
                self.assertFalse(allowed_relative(path))
        self.assertTrue(allowed_relative("docs/research/current.md"))

    def test_incomplete_history_scan_is_a_blocker(self):
        def fail_history(root, *args):
            if args == ("rev-list", "--all"):
                raise subprocess.CalledProcessError(1, "git")
            return audit_git(root, *args)

        with patch("tools.audit_public_release.git", side_effect=fail_history):
            result = audit(self.root)
        self.assertIn("history-blob-audit-incomplete", {v["kind"] for v in result["blockers"]})

    def test_skipped_content_scan_is_not_reported_as_pass(self):
        result = audit(self.root, scan_content=False)
        self.assertEqual(result["status"], "CONTENT_SCAN_SKIPPED")
        self.assertFalse(result["full_content_scan"])


if __name__ == "__main__":
    unittest.main()
