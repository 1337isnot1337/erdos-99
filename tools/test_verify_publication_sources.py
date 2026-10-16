#!/usr/bin/env python3
"""Real-object failure controls for the optional publication source auditor."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import verify_publication_sources as audit


class SourceAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='e99-source-audit-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'public'
        self.source = Path(self.tmp.name) / 'source'
        self.root.mkdir(); self.source.mkdir()
        (self.root / 'docs/publication').mkdir(parents=True)
        subprocess.run(['git', 'init', '-q', str(self.source)], check=True)
        (self.source / 'proof.md').write_text('Exact source proof\n')
        (self.source / 'other.md').write_text('Different source object\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Audit fixture', '-c', 'user.email=audit@users.noreply.github.com',
                 '-c', 'commit.gpgsign=false', 'commit', '-qm', 'fixture')
        commit = self.git('rev-parse', 'HEAD').strip()
        blob = self.git('rev-parse', 'HEAD:proof.md').strip()
        body = (self.source / 'proof.md').read_bytes()
        (self.root / 'proof.md').write_bytes(body)
        self.entry = dict(source_path='proof.md', public_path='proof.md',
                          source_commit=commit, source_blob=blob, source_mode='100644',
                          source_sha256=hashlib.sha256(body).hexdigest(),
                          public_sha256=hashlib.sha256(body).hexdigest())
        self.write_manifest()
        (self.root / 'docs/publication/exclusion.json').write_text('[]')

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.source), *args], text=True)

    def write_manifest(self):
        (self.root / 'docs/publication/inclusion.json').write_text(json.dumps(
            {'source_commit': self.entry['source_commit'], 'entries': [self.entry]}))

    def test_real_source_and_standalone_public_bytes(self):
        self.assertEqual(audit.verify(self.root)['errors'], [])
        result = audit.verify(self.root, self.source)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['source_records_verified'], 1)

    def test_other_valid_blob_cannot_impersonate_path(self):
        self.entry['source_blob'] = self.git('rev-parse', 'HEAD:other.md').strip()
        self.write_manifest()
        self.assertTrue(audit.verify(self.root, self.source)['errors'])

    def test_wrong_source_mode_is_rejected(self):
        self.entry['source_mode'] = '100755'
        self.write_manifest()
        self.assertTrue(audit.verify(self.root, self.source)['errors'])

    def test_mutated_public_body_is_rejected_without_source(self):
        (self.root / 'proof.md').write_text('Unexpected replacement')
        self.assertTrue(audit.verify(self.root)['errors'])

    def test_traversal_and_revision_syntax_are_rejected(self):
        for path in ('../bad', '/absolute', 'a/../bad', 'a//bad', 'a:bad', 'a\\bad'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                audit.safe_path(path)


if __name__ == '__main__':
    unittest.main()
