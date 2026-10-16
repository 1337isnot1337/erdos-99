"""Real Git controls for index-hidden changes in final-candidate receipts."""
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.verify_publication_candidate import verify_committed_worktree


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


if __name__ == '__main__':
    unittest.main()
