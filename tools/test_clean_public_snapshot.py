"""Meaningful privacy isolation and source-object preservation regressions."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from tools.prepare_clean_public_snapshot import prepare


class CleanSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'Fixture author')
        # Synthetic private-looking identity must remain absent from exported bytes.
        self.git('config', 'user.email', 'fixture@privacy.invalid')

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.source), *args], stderr=subprocess.PIPE)

    def commit(self, message='fixture'):
        self.git('add', '-A')
        self.git('commit', '-qm', message)

    def test_exact_tree_one_root_no_hidden_objects_no_filters(self):
        (self.source / 'secret-history.txt').write_text('synthetic historical marker')
        self.commit('historical marker')
        old = self.git('rev-parse', 'HEAD').strip()
        (self.source / 'secret-history.txt').unlink()
        (self.source / '.gitattributes').write_text('*.txt -text\n')
        (self.source / 'data.txt').write_bytes(b'crlf\r\nbytes\r\n')
        exe = self.source / 'run'
        exe.write_text('#!/bin/sh\nexit 0\n')
        exe.chmod(0o755)
        self.commit('retained candidate')
        self.git('tag', '-a', 'old-tag', '-m', 'old metadata', old.decode())
        original_refs = self.git('show-ref')
        destination = self.root / 'clean'
        result = prepare(self.source, destination)
        call = lambda *args: subprocess.check_output(['git', '-C', str(destination), *args], stderr=subprocess.PIPE)
        self.assertEqual(call('rev-parse', 'HEAD^{tree}'), self.git('rev-parse', 'HEAD^{tree}'))
        self.assertEqual(call('rev-list', '--all', '--count').strip(), b'1')
        self.assertEqual(call('rev-list', '--parents', 'HEAD').decode().split(), [result['clean_candidate']])
        self.assertEqual(call('remote'), b'')
        self.assertFalse((destination / '.git/objects/info/alternates').exists())
        self.assertEqual((destination / 'data.txt').read_bytes(), b'crlf\r\nbytes\r\n')
        self.assertTrue(os.access(destination / 'run', os.X_OK))
        self.assertEqual(call('cat-file', '--batch-all-objects', '--batch-check=%(objecttype)').splitlines().count(b'commit'), 1)
        self.assertNotIn(b'privacy.invalid', call('log', '--all', '--format=raw'))
        self.assertEqual(original_refs, self.git('show-ref'))
        with self.assertRaises(subprocess.CalledProcessError):
            call('cat-file', '-t', old.decode())

    def test_existing_destination_preserved(self):
        (self.source / 'file').write_text('candidate')
        self.commit()
        destination = self.root / 'existing'
        destination.mkdir()
        (destination / 'keep').write_text('keep')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            prepare(self.source, destination)
        self.assertEqual((destination / 'keep').read_text(), 'keep')

    def test_symlink_rejected_before_export(self):
        (self.source / 'link').symlink_to('/etc/passwd')
        self.commit()
        destination = self.root / 'clean'
        with self.assertRaisesRegex(ValueError, 'unsafe path'):
            prepare(self.source, destination)
        self.assertFalse(destination.exists())

    def test_immutable_ref_ignores_dirty_worktree(self):
        (self.source / 'file').write_text('committed')
        self.commit()
        (self.source / 'file').write_text('uncommitted')
        destination = self.root / 'clean'
        prepare(self.source, destination)
        self.assertEqual((destination / 'file').read_text(), 'committed')
        self.assertEqual((self.source / 'file').read_text(), 'uncommitted')


if __name__ == '__main__':
    unittest.main()
