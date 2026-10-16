"""Rights evidence must fail hash mismatches and never infer contributor consent."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from tools import audit_public_rights as rights


class RightsAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)
        self.source, self.public = (self.directory / p for p in ('source', 'public'))
        for repo in (self.source, self.public):
            repo.mkdir()
            self.git(repo, 'init', '-qb', 'main')
            self.git(repo, 'config', 'user.name', 'Fixture contributor')
            self.git(repo, 'config', 'user.email', 'fixture@private.invalid')
        (self.source / 'proof.md').write_text('Original mathematical argument\n')
        self.commit(self.source)
        self.pin = self.git(self.source, 'rev-parse', 'HEAD').decode().strip()
        self.blob = self.git(self.source, 'rev-parse', 'HEAD:proof.md').decode().strip()
        data = (self.source / 'proof.md').read_bytes()
        self.checksum = hashlib.sha256(data).hexdigest()
        (self.public / 'proof.md').write_bytes(data)
        (self.public / 'docs/publication').mkdir(parents=True)
        self.manifest = {'source_commit':self.pin, 'entries':[{
            'public_path':'proof.md', 'source_path':'proof.md',
            'source_commit':self.pin, 'source_blob':self.blob,
            'source_sha256':self.checksum,'public_sha256':self.checksum,
            'publication_clearance':'pending provenance/content review'}]}
        self.write_manifest()
        self.commit(self.public)

    def tearDown(self):
        self.temporary.cleanup()

    def git(self, repo, *args):
        return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)

    def commit(self, repo):
        self.git(repo, 'add', '-A')
        self.git(repo, 'commit', '-qm', 'fixture')

    def write_manifest(self):
        (self.public / 'docs/publication/inclusion.json').write_text(json.dumps(self.manifest))

    def audit(self):
        with patch.object(rights, 'ADAPTATION_SOURCE', self.pin), patch.object(rights, 'ADAPTATION_PATHS', set()):
            return rights.audit(self.public, self.source)

    def test_hashes_and_author_names_do_not_grant_rights(self):
        result = self.audit()
        self.assertEqual(result['failures'], [])
        self.assertEqual(result['status'], 'OWNER DECISION REQUIRED')
        self.assertEqual(result['counts']['verified_source_hashes'], 1)
        record = next(x for x in result['files'] if x['public_path'] == 'proof.md')
        self.assertEqual(len(record['observed_author_ids']), 1)
        self.assertNotIn('Fixture contributor', json.dumps(result))
        self.assertNotIn('private.invalid', json.dumps(result))
        self.assertTrue(all(x['disposition'] == 'OWNER DECISION REQUIRED' for x in result['groups']))

    def test_external_identity_map_is_stable_and_never_in_public_report(self):
        identities = {}
        with patch.object(rights, 'ADAPTATION_SOURCE', self.pin), patch.object(rights, 'ADAPTATION_PATHS', set()):
            first = rights.audit(self.public, self.source, identities=identities)
            second = rights.audit(self.public, self.source, identities=identities)
        self.assertEqual(first, second)
        self.assertIn('Fixture contributor', identities)
        self.assertNotIn('Fixture contributor', json.dumps(first))

    def test_exact_source_blob_mismatch_blocks(self):
        self.manifest['entries'][0]['source_blob'] = '0' * 40
        self.write_manifest()
        self.commit(self.public)
        result = self.audit()
        self.assertEqual(result['status'], 'BLOCKED')
        self.assertEqual(result['counts']['verified_source_hashes'], 0)
        self.assertEqual(result['failures'][0]['kind'], 'pinned-hash-mismatch')

    def test_merge_created_content_has_attribution_history(self):
        first = self.pin
        (self.source / 'branch.md').write_text('branch')
        self.commit(self.source)
        second = self.git(self.source, 'rev-parse', 'HEAD').decode().strip()
        (self.source / 'merge-only.md').write_text('merge-created source')
        self.git(self.source, 'add', '-A')
        tree = self.git(self.source, 'write-tree').decode().strip()
        merge = self.git(self.source, 'commit-tree', tree, '-p', first, '-p', second, '-m', 'merge-only source').decode().strip()
        result = rights.history(self.source, merge, {'merge-only.md'})
        self.assertEqual(result['merge-only.md']['authors'], {'Fixture contributor'})
        self.assertEqual(result['merge-only.md']['commits'], [merge])


if __name__ == '__main__':
    unittest.main()
