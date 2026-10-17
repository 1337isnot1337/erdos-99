"""Real Git controls for exact mathematical false-positive dispositions."""
import hashlib
import json
from pathlib import Path
import secrets
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.review_scanner_findings import review_combined_history_gitleaks, review_tree_gitleaks
from tools.verify_publication_candidate import review_history_gitleaks


class MathematicalFindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        self.git('init', '-q')
        self.path = 'assignment.jsonl'
        self.stem = ''.join(['global_', 'convexity_', 'exit_barrier_', '2026_10_12'])
        field = 'unit_' + 'key'
        self.file = self.root / self.path
        self.file.write_text(json.dumps({field: self.stem}, separators=(',', ':')) + '\n')
        self.git('add', self.path)
        self.commit('reviewed mathematical assignment')
        self.candidate = self.git('rev-parse', 'HEAD').strip()
        data = self.file.read_bytes()
        self.record = {
            'git_blob_sha': self.git('rev-parse', 'HEAD:' + self.path).strip(),
            'sha256': hashlib.sha256(data).hexdigest(),
            'findings': {1: (3, 51, self.stem)},
        }
        context = patch('tools.review_scanner_findings.REVIEWED_MATH_GROUPS',
                        {self.path: self.record})
        context.start()
        self.addCleanup(context.stop)
        self.report = Path(self.temp.name) / 'scanner.json'
        self.tree_match = {
            'Commit': '', 'File': self.path, 'RuleID': 'generic-api-key',
            'StartLine': 1, 'EndLine': 1, 'StartColumn': 3, 'EndColumn': 51,
            'Fingerprint': self.path + ':generic-api-key:1',
            'Match': field + '":"REDACTED"', 'Secret': 'REDACTED',
            'SymlinkFile': '',
        }
        self.report.write_text(json.dumps([self.tree_match]))

    def git(self, *argv):
        return subprocess.check_output(['git', '--no-replace-objects', '-C', str(self.root),
                                        *argv], text=True, stderr=subprocess.PIPE)

    def commit(self, message):
        self.git('-c', 'user.name=Scanner review fixture',
                 '-c', 'user.email=fixture@example.invalid', '-c', 'commit.gpgsign=false',
                 'commit', '--allow-empty', '-qm', message)

    def history_match(self, commit):
        return {**self.tree_match, 'Commit': commit,
                'Fingerprint': commit + ':' + self.path + ':generic-api-key:1'}

    def test_exact_tree_finding_preserves_raw_report(self):
        raw = self.report.read_bytes()
        review = review_tree_gitleaks(self.root, self.report, self.candidate)
        self.assertEqual(review['finding_count'], 1)
        self.assertTrue(review['raw_scanner_result_preserved'])
        self.assertEqual(self.report.read_bytes(), raw)

    def test_same_reviewed_blob_on_two_commits_is_bound_independently(self):
        self.commit('identical reviewed assignment on another commit')
        alias = self.git('rev-parse', 'HEAD').strip()
        self.report.write_text(json.dumps([self.history_match(self.candidate),
                                          self.history_match(alias)]))
        review = review_combined_history_gitleaks(self.root, self.report,
                                                 review_history_gitleaks)
        self.assertEqual(review['finding_count'], 2)
        self.assertEqual({finding['Commit'] for finding in review['mathematical_findings']},
                         {self.candidate, alias})

    def test_added_or_duplicate_findings_are_rejected(self):
        for additional in (self.tree_match, {**self.tree_match, 'File': 'other.jsonl',
                                             'Fingerprint': 'other.jsonl:generic-api-key:1'}):
            self.report.write_text(json.dumps([self.tree_match, additional]))
            self.assertIsNone(review_tree_gitleaks(self.root, self.report, self.candidate))

    def test_every_changed_identity_field_is_rejected(self):
        for key, value in self.tree_match.items():
            with self.subTest(field=key):
                changed = 'different' if not isinstance(value, int) else value + 1
                self.report.write_text(json.dumps([{**self.tree_match, key: changed}]))
                self.assertIsNone(review_tree_gitleaks(self.root, self.report, self.candidate))

    def test_missing_malformed_reports_are_rejected(self):
        for raw in ('', 'null', '{}', '[]', '[null]', '[{"Fingerprint": []}]'):
            self.report.write_text(raw)
            self.assertIsNone(review_tree_gitleaks(self.root, self.report, self.candidate))
        self.report.unlink()
        self.assertIsNone(review_tree_gitleaks(self.root, self.report, self.candidate))

    def test_credential_shaped_replacement_is_not_borrowed_from_reviewed_blob(self):
        self.file.write_text(json.dumps({'unit_' + 'key': secrets.token_hex(24)},
                                       separators=(',', ':')) + '\n')
        self.git('add', self.path)
        self.commit('synthetic token negative control')
        changed = self.git('rev-parse', 'HEAD').strip()
        self.assertIsNone(review_tree_gitleaks(self.root, self.report, changed))
        self.report.write_text(json.dumps([self.history_match(changed)]))
        self.assertIsNone(review_combined_history_gitleaks(self.root, self.report,
                                                         review_history_gitleaks))

    def test_uncommitted_substitution_never_changes_reviewed_git_bytes(self):
        self.file.write_text('Uncommitted replacement\n')
        self.assertIsNotNone(review_tree_gitleaks(self.root, self.report, self.candidate))

    def test_a_changed_pin_or_unavailable_git_object_fails_closed(self):
        for key in ('git_blob_sha', 'sha256'):
            record = {**self.record, key: '0' * len(self.record[key])}
            with patch('tools.review_scanner_findings.REVIEWED_MATH_GROUPS',
                       {self.path: record}):
                self.assertIsNone(review_tree_gitleaks(self.root, self.report, self.candidate))
        self.report.write_text(json.dumps([self.history_match('0' * 40)]))
        self.assertIsNone(review_combined_history_gitleaks(self.root, self.report,
                                                         review_history_gitleaks))

    def test_an_unreviewed_history_finding_is_not_filtered_out(self):
        additional = {**self.history_match(self.candidate),
                      'File': 'unexpected.py',
                      'Fingerprint': self.candidate + ':unexpected.py:generic-api-key:1'}
        self.report.write_text(json.dumps([self.history_match(self.candidate), additional]))
        raw = self.report.read_bytes()
        self.assertIsNone(review_combined_history_gitleaks(self.root, self.report,
                                                         review_history_gitleaks))
        self.assertEqual(self.report.read_bytes(), raw)

    def test_octopus_merge_multiplicity_is_derived_from_exact_parent_diffs(self):
        original_tree = self.git('rev-parse', self.candidate + '^{tree}').strip()
        self.git('rm', self.path)
        empty_tree = self.git('write-tree').strip()

        def commit_tree(tree, parents, message):
            argv = ['-c', 'user.name=Scanner review fixture',
                    '-c', 'user.email=fixture@example.invalid',
                    'commit-tree', tree]
            for parent in parents:
                argv += ['-p', parent]
            return self.git(*argv, '-m', message).strip()

        absent = [commit_tree(empty_tree, [self.candidate], 'absent parent ' + str(index))
                  for index in range(3)]
        merge = commit_tree(original_tree, [self.candidate, *absent], 'four-parent merge')
        for count in (2, 3, 4):
            with self.subTest(reported_occurrences=count):
                self.report.write_text(json.dumps([self.history_match(merge)] * count))
                result = review_combined_history_gitleaks(self.root, self.report,
                                                         review_history_gitleaks)
                if count == 3:
                    self.assertEqual(result['finding_count'], 3)
                else:
                    self.assertIsNone(result)

    def test_exact_source_fixture_is_reviewed_but_changed_payload_is_not(self):
        opening = '-----BEGIN ' + 'PRIVATE KEY-----'
        self.file.write_text('first = ' + repr(opening) + '\nsecond = ' + repr(opening) + '\n')
        self.git('add', self.path)
        self.commit('payload-free negative-test delimiters')
        candidate = self.git('rev-parse', 'HEAD').strip()
        record = {
            'path': self.path,
            'git_blob_sha': self.git('rev-parse', 'HEAD:' + self.path).strip(),
            'sha256': hashlib.sha256(self.file.read_bytes()).hexdigest(),
            'StartLine': 1, 'EndLine': 2, 'StartColumn': 1, 'EndColumn': 1,
        }
        match = {**self.tree_match, 'RuleID': 'private-key', 'Match': 'REDACTED',
                 'StartLine': 1, 'EndLine': 2, 'StartColumn': 1, 'EndColumn': 1,
                 'Fingerprint': self.path + ':private-key:1'}
        self.report.write_text(json.dumps([match]))
        with patch('tools.review_scanner_findings.REVIEWED_SOURCE_FIXTURE', record):
            self.assertIsNotNone(review_tree_gitleaks(self.root, self.report, candidate))
            self.file.write_text(self.file.read_text() + 'payload = ' + repr(secrets.token_hex(32)) + '\n')
            self.git('add', self.path)
            self.commit('synthetic encoded-payload negative control')
            changed = self.git('rev-parse', 'HEAD').strip()
            self.assertIsNone(review_tree_gitleaks(self.root, self.report, changed))


if __name__ == '__main__':
    unittest.main()

