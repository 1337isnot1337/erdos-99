"""Reject stale or incomplete underlying release receipts."""
import unittest

from tools.verify_migration_release_candidate import accepted_gate2


class ExactMigrationReceiptTests(unittest.TestCase):
    def setUp(self):
        self.candidate, self.tree = 'a' * 40, 'b' * 40
        self.receipt = {
            'candidate_commit': self.candidate, 'candidate_tree': self.tree,
            'candidate_unchanged': True, 'executable_checks_passed': True,
            'automated_release_precheck_passed': True,
        }

    def test_exact_passing_receipt_is_accepted(self):
        self.assertTrue(accepted_gate2(self.receipt, self.candidate, self.tree))

    def test_another_commit_or_tree_is_rejected(self):
        for key in ('candidate_commit', 'candidate_tree'):
            changed = {**self.receipt, key: 'c' * 40}
            self.assertFalse(accepted_gate2(changed, self.candidate, self.tree))

    def test_a_failed_missing_or_nonboolean_check_is_rejected(self):
        for key in ('candidate_unchanged', 'executable_checks_passed',
                    'automated_release_precheck_passed'):
            for value in (False, None, 'true', 1):
                with self.subTest(key=key, value=value):
                    self.assertFalse(accepted_gate2({**self.receipt, key: value},
                                                    self.candidate, self.tree))
            changed = dict(self.receipt)
            del changed[key]
            self.assertFalse(accepted_gate2(changed, self.candidate, self.tree))

    def test_missing_or_malformed_receipt_is_rejected(self):
        for receipt in (None, [], 'receipt', {}, True):
            self.assertFalse(accepted_gate2(receipt, self.candidate, self.tree))


if __name__ == '__main__':
    unittest.main()
