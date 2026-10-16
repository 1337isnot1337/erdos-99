"""Real Git controls for index-hidden changes in final-candidate receipts."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.verify_publication_candidate import GITLEAKS_HISTORY_LOG_OPTIONS, review_history_gitleaks, verify_committed_worktree


class CommittedCandidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.file = self.root / 'certificate.py'
        self.file.write_text('raise SystemExit(1)\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Receipt fixture', '-c', 'user.email=fixture@example.invalid',
                 '-c', 'commit.gpgSign=false', 'commit', '-qm', 'failing committed certificate')
        self.candidate = self.git('rev-parse', 'HEAD').strip()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], text=True)

    def test_clean_committed_tree_passes(self):
        self.assertEqual(verify_committed_worktree(self.root, self.candidate), 1)

    def test_assume_unchanged_cannot_hide_a_passing_replacement(self):
        self.git('update-index', '--assume-unchanged', 'certificate.py')
        self.file.write_text('raise SystemExit(0)\n')
        self.assertEqual(self.git('status', '--porcelain'), '')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_skip_worktree_cannot_hide_a_passing_replacement(self):
        self.git('update-index', '--skip-worktree', 'certificate.py')
        self.file.write_text('raise SystemExit(0)\n')
        self.assertEqual(self.git('status', '--porcelain'), '')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_raw_bytes_and_execute_mode_do_not_trust_git_configuration(self):
        self.git('config', 'core.filemode', 'false')
        self.file.chmod(0o755)
        self.assertEqual(self.git('status', '--porcelain'), '')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)
        self.file.chmod(0o644)
        self.file.write_text('raise SystemExit(0)\n')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_group_execute_bit_cannot_hide_behind_nonexecutable_owner(self):
        self.git('config', 'core.filemode', 'false')
        self.file.chmod(0o654)
        self.assertEqual(self.git('status', '--porcelain'), '')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_symlink_substitution_is_rejected(self):
        self.file.unlink()
        self.file.symlink_to('/dev/null')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)


class HistoricalScannerReviewTests(unittest.TestCase):
    # Reuse real Git setup without rerunning the inherited immutability tests.
    git = CommittedCandidateTests.git

    def setUp(self):
        CommittedCandidateTests.setUp(self)
        self.report = Path(self.tmp.name) / 'scanner.json'
        self.match = {'Commit': self.candidate, 'File': 'certificate.py',
                      'RuleID': 'private-key', 'StartLine': 1, 'EndLine': 1,
                      'Fingerprint': self.candidate + ':certificate.py:private-key:1'}
        digest = hashlib.sha256(self.file.read_bytes()).hexdigest()
        for name, value in [('REVIEWED_HISTORY_FIXTURE', self.match),
                            ('REVIEWED_HISTORY_BLOB_SHA256', digest)]:
            context = patch('tools.verify_publication_candidate.' + name, value)
            context.start()
            self.addCleanup(context.stop)
        self.report.write_text(json.dumps([self.match]))

    def test_exact_review_retains_raw_finding_identity(self):
        result = review_history_gitleaks(self.root, self.report)
        self.assertEqual(result['disposition'], 'reviewed-false-positive')
        self.assertEqual(result['finding'], self.match)
        self.assertTrue(result['raw_scanner_result_preserved'])

    def test_added_finding_is_not_covered(self):
        self.report.write_text(json.dumps([self.match, self.match]))
        self.assertIsNone(review_history_gitleaks(self.root, self.report))

    def test_changed_finding_identity_is_not_covered(self):
        for key in self.match:
            with self.subTest(key=key):
                changed = {**self.match, key: 'different'}
                self.report.write_text(json.dumps([changed]))
                self.assertIsNone(review_history_gitleaks(self.root, self.report))

    def test_missing_malformed_or_empty_report_is_not_covered(self):
        for contents in ['', 'null', '{}', '[]', '[null]', '[{"Commit":[]}]']:
            with self.subTest(contents=contents):
                self.report.write_text(contents)
                self.assertIsNone(review_history_gitleaks(self.root, self.report))
        self.report.unlink()
        self.assertIsNone(review_history_gitleaks(self.root, self.report))

    def test_committed_blob_digest_must_match(self):
        with patch('tools.verify_publication_candidate.REVIEWED_HISTORY_BLOB_SHA256', '0' * 64):
            self.assertIsNone(review_history_gitleaks(self.root, self.report))

    def test_worktree_substitution_does_not_change_reviewed_git_object(self):
        self.file.write_text('A different uncommitted fixture\n')
        self.assertIsNotNone(review_history_gitleaks(self.root, self.report))

    def test_missing_git_object_is_not_covered(self):
        self.git('init', '-q', str(self.root / 'empty'))
        self.assertIsNone(review_history_gitleaks(self.root / 'empty', self.report))

    def commit_alias(self, *, changed=False):
        if changed:
            self.file.write_text('Different committed bytes\n')
            self.git('add', 'certificate.py')
        self.git('-c', 'user.name=Receipt fixture', '-c', 'user.email=fixture@example.invalid',
                 '-c', 'commit.gpgSign=false', 'commit', '--allow-empty', '-qm', 'fixture alias')
        alias = self.git('rev-parse', 'HEAD').strip()
        second = {**self.match, 'Commit': alias,
                  'Fingerprint': alias + ':certificate.py:private-key:1'}
        self.report.write_text(json.dumps([self.match, second]))
        return alias

    def test_two_exact_pinned_occurrences_of_same_blob_are_reviewed(self):
        alias = self.commit_alias()
        with patch('tools.verify_publication_candidate.REVIEWED_HISTORY_ALIASES', (alias,)):
            result = review_history_gitleaks(self.root, self.report)
        self.assertEqual(result['finding_count'], 2)
        self.assertEqual({m['Commit'] for m in result['findings']}, {self.candidate, alias})

    def test_pinned_alias_must_also_have_exact_reviewed_blob(self):
        alias = self.commit_alias(changed=True)
        with patch('tools.verify_publication_candidate.REVIEWED_HISTORY_ALIASES', (alias,)):
            self.assertIsNone(review_history_gitleaks(self.root, self.report))

    def test_history_options_include_deleted_merge_resolution_content(self):
        self.git('config', 'user.name', 'Receipt fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('config', 'commit.gpgSign', 'false')
        self.git('switch', '-c', 'side')
        (self.root / 'side.txt').write_text('Side change\n')
        self.git('add', 'side.txt'); self.git('commit', '-qm', 'side')
        self.git('switch', '--detach', self.candidate)
        self.git('switch', '-c', 'primary')
        (self.root / 'primary.txt').write_text('Primary change\n')
        self.git('add', 'primary.txt'); self.git('commit', '-qm', 'primary')
        self.git('merge', '--no-commit', 'side')
        marker = 'unique merge resolution sentinel'
        (self.root / 'merge.txt').write_text(marker + '\n')
        self.git('add', 'merge.txt'); self.git('commit', '-qm', 'merge resolution')
        self.git('rm', 'merge.txt'); self.git('commit', '-qm', 'remove merge resolution')
        # Ordinary log patches can show the later deletion, but never the added
        # merge-only content. The scanner needs the positive diff to see it.
        self.assertNotIn('+' + marker, self.git('log', '-p', '--all'))
        self.assertIn('+' + marker, self.git('log', '-p', *GITLEAKS_HISTORY_LOG_OPTIONS.split()))


if __name__ == '__main__':
    unittest.main()
