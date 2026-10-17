"""Real Git controls for index-hidden changes in final-candidate receipts."""
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.verify_publication_candidate import GITLEAKS_HISTORY_LOG_OPTIONS, find_executable, main, review_history_gitleaks, verify_committed_worktree


class CommittedCandidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'core.autocrlf', 'false')
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

    @unittest.skipIf(os.name == 'nt', 'POSIX execute bits are not represented on Windows')
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

    @unittest.skipIf(os.name == 'nt', 'POSIX execute bits are not represented on Windows')
    def test_group_execute_bit_cannot_hide_behind_nonexecutable_owner(self):
        self.git('config', 'core.filemode', 'false')
        self.file.chmod(0o654)
        self.assertEqual(self.git('status', '--porcelain'), '')
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_symlink_substitution_is_rejected(self):
        target = self.root / 'target.txt'
        target.write_text('Target fixture\n')
        self.file.unlink()
        try:
            self.file.symlink_to(target)
        except (OSError, NotImplementedError) as error:
            self.skipTest('Host does not allow symlink creation: ' + str(error))
        with self.assertRaises(ValueError):
            verify_committed_worktree(self.root, self.candidate)

    def test_host_without_execute_bits_still_checks_committed_bytes(self):
        self.git('config', 'core.filemode', 'false')
        self.git('update-index', '--chmod=+x', 'certificate.py')
        self.git('-c', 'user.name=Receipt fixture', '-c', 'user.email=fixture@example.invalid',
                 '-c', 'commit.gpgSign=false', 'commit', '-qm', 'record executable Git mode')
        candidate = self.git('rev-parse', 'HEAD').strip()
        with patch('tools.verify_publication_candidate.CHECK_POSIX_EXECUTE_BITS', False):
            self.assertEqual(verify_committed_worktree(self.root, candidate), 1)
            self.file.write_text('raise SystemExit(0)\n')
            with self.assertRaises(ValueError):
                verify_committed_worktree(self.root, candidate)


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


class CurrentReleaseCommandTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='e99-release-command-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'repo'
        self.root.mkdir()
        self.output = Path(self.tmp.name) / 'receipt'
        subprocess.check_call(['git', '-C', str(self.root), 'init', '-q'])
        subprocess.check_call(['git', '-C', str(self.root), 'config', 'core.autocrlf', 'false'])
        (self.root / 'README.md').write_text('# Current release fixture\n')
        subprocess.check_call(['git', '-C', str(self.root), 'add', 'README.md'])
        subprocess.check_call(['git', '-C', str(self.root), '-c', 'user.name=CI Test',
                               '-c', 'user.email=ci-test@example.invalid',
                               '-c', 'commit.gpgSign=false', 'commit', '-qm', 'fixture'])

    def run_candidate(self, *, scanner_findings=False, release_audit_fails=False,
                      available_tools=('gitleaks', 'actionlint'), require_release_tools=False,
                      invocation_failure=None, skipped_tests=False):
        real_run = subprocess.run
        self.lookups = []

        def lookup(name):
            self.lookups.append(name)
            return str(Path(self.tmp.name) / 'native tools' / name) if name in available_tools else None

        def execute(argv, **kwargs):
            # Keep real Git snapshot checks; do not execute verifier suites or scanners.
            if argv[0] == 'git':
                return real_run(argv, **kwargs)
            if invocation_failure is not None and Path(argv[0]).name == invocation_failure:
                raise OSError('Native executable cannot run on this host')
            code = int(scanner_findings and Path(argv[0]).name == 'gitleaks'
                       and argv[1] in ('dir', 'git'))
            if release_audit_fails and 'tools/audit_public_release.py' in argv:
                code = 1
            if skipped_tests and 'unittest' in argv and 'tools' in argv:
                kwargs['stdout'].write(
                    b"Ran 1 test in 0.01s\nOK\n"
                    b"test_optional ... skipped 'isolated backend unavailable'\n"
                    b"Ran 20 tests in 0.01s\nOK (skipped=2)\n")
            return subprocess.CompletedProcess(argv, code)

        stdout = io.StringIO()
        with patch('tools.verify_publication_candidate.subprocess.run', side_effect=execute), \
             patch('tools.verify_publication_candidate.shutil.which', side_effect=lookup), \
             patch('tools.verify_publication_candidate.sandbox_unavailable_reason',
                   return_value='Optional isolated backend unavailable in this fixture'), \
             patch('tools.verify_publication_candidate.importlib.metadata.distributions', return_value=[]), \
             contextlib.redirect_stdout(stdout):
            argv = ['--root', str(self.root), '--output', str(self.output)]
            if require_release_tools:
                argv.append('--require-release-tools')
            status = main(argv)
        self.summary = json.loads(stdout.getvalue().splitlines()[-1])
        return status, json.loads((self.output / 'receipt.json').read_text())

    def test_current_checks_run_without_a_source_repository_or_migration_receipt(self):
        status, receipt = self.run_candidate(require_release_tools=True)
        self.assertEqual(status, 0)
        self.assertTrue(receipt['require_release_tools'])
        self.assertTrue(receipt['candidate_unchanged'])
        self.assertTrue(receipt['executable_checks_passed'])
        self.assertTrue(self.summary['automated_release_precheck_passed'])
        self.assertNotIn('release_cleared', receipt)
        self.assertNotIn('release_cleared', self.summary)
        self.assertTrue(all('clearance_gate' not in row for row in receipt['commands']))
        names = {row['name'] for row in receipt['commands']}
        self.assertTrue({'reading-edition', 'public-integrity', 'theorem-state',
                         'tool-tests', 'corpus-tests', 'certificates', 'release-audit',
                         'gitleaks-tree', 'gitleaks-history', 'actionlint'} <= names)
        self.assertEqual(self.lookups, ['gitleaks', 'actionlint'])
        self.assertIn('system', receipt['platform'])
        self.assertEqual(receipt['skipped_checks'], [])
        self.assertNotIn('source-provenance', names)
        arguments = [arg for row in receipt['commands'] for arg in row['argv']]
        self.assertNotIn('tools/verify_publication_sources.py', arguments)
        self.assertNotIn('--source-repo', arguments)
        self.assertFalse((self.output / 'source-provenance.json').exists())

    def test_missing_optional_tools_do_not_fail_standard_checks(self):
        status, receipt = self.run_candidate(available_tools=())
        self.assertEqual(status, 0)
        self.assertTrue(receipt['executable_checks_passed'])
        self.assertTrue(receipt['required_scope_passed'])
        self.assertFalse(receipt['automated_release_precheck_passed'])
        skipped = {name for row in receipt['skipped_checks'] for name in row['names']}
        self.assertEqual(skipped, {'gitleaks-version', 'gitleaks-tree', 'gitleaks-history', 'actionlint'})
        self.assertFalse(receipt['capabilities']['gitleaks']['available'])
        self.assertFalse(receipt['capabilities']['isolated_package_replay']['available'])

    def test_strict_release_scope_requires_missing_tools(self):
        status, receipt = self.run_candidate(available_tools=(), require_release_tools=True)
        self.assertEqual(status, 1)
        self.assertTrue(receipt['executable_checks_passed'])
        self.assertFalse(receipt['required_scope_passed'])
        self.assertFalse(receipt['automated_release_precheck_passed'])

    def test_gitleaks_alone_does_not_establish_full_release_scope(self):
        status, receipt = self.run_candidate(available_tools=('gitleaks',))
        self.assertEqual(status, 0)
        self.assertTrue(receipt['executable_checks_passed'])
        self.assertFalse(receipt['automated_release_precheck_passed'])
        self.assertEqual(receipt['skipped_checks'][0]['names'], ['actionlint'])

    def test_native_tool_invocation_error_is_recorded_as_failure(self):
        status, receipt = self.run_candidate(invocation_failure='actionlint')
        self.assertEqual(status, 1)
        command = next(row for row in receipt['commands'] if row['name'] == 'actionlint')
        self.assertIsNone(command['exit_code'])
        self.assertIn('OSError', command['invocation_error'])
        self.assertFalse(command['verification_passed'])
        self.assertFalse(receipt['automated_release_precheck_passed'])

    def test_optional_test_skips_remain_visible_in_receipt(self):
        status, receipt = self.run_candidate(skipped_tests=True)
        self.assertEqual(status, 0)
        command = next(row for row in receipt['commands'] if row['name'] == 'tool-tests')
        self.assertEqual(command['test_summary'], {
            'tests_run': 20, 'tests_skipped': 2,
            'skip_reasons': ['isolated backend unavailable'],
        })

    def test_explicit_missing_tool_is_an_invocation_error(self):
        with patch('tools.verify_publication_candidate.shutil.which', return_value=None), \
             contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            main(['--root', str(self.root), '--output', str(self.output), '--gitleaks', 'missing-native-tool'])
        self.assertEqual(error.exception.code, 2)
        self.assertFalse(self.output.exists())

    def test_explicit_tool_name_uses_path_discovery(self):
        executable = str(Path(self.tmp.name) / 'native tools' / 'scanner')
        with patch('tools.verify_publication_candidate.shutil.which', return_value=executable) as lookup:
            self.assertEqual(find_executable('gitleaks', 'custom-scanner'), str(Path(executable).resolve()))
        lookup.assert_called_once_with('custom-scanner')

    def test_release_audit_failure_fails_all_current_checks(self):
        status, receipt = self.run_candidate(release_audit_fails=True)
        self.assertEqual(status, 1)
        self.assertTrue(receipt['candidate_unchanged'])
        self.assertFalse(receipt['executable_checks_passed'])
        self.assertFalse(receipt['automated_release_precheck_passed'])
        self.assertFalse(self.summary['executable_checks_passed'])
        audit = next(row for row in receipt['commands'] if row['name'] == 'release-audit')
        self.assertEqual(audit['exit_code'], 1)
        self.assertFalse(audit['verification_passed'])

    def test_removed_source_repository_option_is_not_accepted(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            main(['--root', str(self.root), '--output', str(self.output),
                  '--source-repo', str(self.root)])
        self.assertEqual(error.exception.code, 2)

    def test_scanner_reviews_keep_the_raw_detected_finding_exits(self):
        reviewed = {'disposition': 'reviewed-false-positive', 'finding_count': 1,
                    'raw_scanner_result_preserved': True}
        with patch('tools.verify_publication_candidate.review_tree_gitleaks', return_value=reviewed) as tree, \
             patch('tools.verify_publication_candidate.review_combined_history_gitleaks', return_value=reviewed) as history:
            status, receipt = self.run_candidate(scanner_findings=True)
        self.assertEqual(status, 0)
        tree.assert_called_once()
        history.assert_called_once()
        scans = [row for row in receipt['commands'] if row['name'] in ('gitleaks-tree', 'gitleaks-history')]
        self.assertEqual(len(scans), 2)
        self.assertTrue(all(row['exit_code'] == 1 and row['verification_passed'] for row in scans))


if __name__ == '__main__':
    unittest.main()
