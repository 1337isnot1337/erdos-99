"""Check that the measured wheel set and both version/hash locks agree."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VerificationWheelTests(unittest.TestCase):
    def test_lock_matches_measured_wheel_manifest_and_version_lock(self):
        manifest = json.loads((ROOT / 'tools/verification-wheels.json').read_text())
        normalize = lambda name: re.sub(r'[-_.]+', '-', name).lower()
        versions = {}
        for line in (ROOT / 'tools/requirements-verification.lock').read_text().splitlines():
            if line.strip() and not line.startswith('#'):
                name, version = line.split('=='); versions[normalize(name)] = version
        measured = {}
        for wheel in manifest['wheels']:
            key = normalize(wheel['distribution'])
            self.assertNotIn(key, measured)
            self.assertRegex(wheel['sha256'], r'^[a-f0-9]{64}$')
            self.assertGreater(wheel['size_bytes'], 0)
            self.assertTrue(wheel['filename'].endswith('.whl'))
            measured[key] = (wheel['version'], wheel['sha256'])
        locked = {}
        for line in (ROOT / 'tools/requirements-verification-linux-x86_64.lock').read_text().splitlines():
            if not line.strip() or line.startswith('#'): continue
            match = re.fullmatch(r'([\w.-]+)==([^ ]+) --hash=sha256:([a-f0-9]{64})', line)
            self.assertIsNotNone(match, line)
            key = normalize(match[1]); self.assertNotIn(key, locked)
            locked[key] = (match[2], match[3])
        self.assertEqual(locked, measured)
        self.assertEqual({name: value[0] for name, value in locked.items()}, versions)
        self.assertEqual(manifest['python'], '3.14.7')
        self.assertEqual((manifest['platform'], manifest['machine']), ('linux', 'x86_64'))


    def test_integrity_lock_is_the_measured_lightweight_subset(self):
        manifest = json.loads((ROOT / 'tools/verification-wheels.json').read_text())
        normalize = lambda name: re.sub(r'[-_.]+', '-', name).lower()
        measured = {normalize(w['distribution']): (w['version'], w['sha256']) for w in manifest['wheels']}
        locked = {}
        for line in (ROOT / 'tools/requirements-integrity-linux-x86_64.lock').read_text().splitlines():
            if not line.strip() or line.startswith('#'): continue
            match = re.fullmatch(r'([\w.-]+)==([^ ]+) --hash=sha256:([a-f0-9]{64})', line)
            self.assertIsNotNone(match, line)
            key = normalize(match[1]); self.assertNotIn(key, locked)
            locked[key] = (match[2], match[3])
        self.assertEqual(set(locked), {'attrs', 'jsonschema', 'jsonschema-specifications',
                                      'pyyaml', 'referencing', 'rpds-py'})
        self.assertEqual(locked, {key: measured[key] for key in locked})
        for line in (ROOT / 'tools/requirements-integrity.txt').read_text().splitlines():
            if line.strip() and not line.startswith('#'):
                name, version = line.split('==')
                self.assertEqual(locked[normalize(name)][0], version)

    def test_localized_ci_installs_only_trusted_integrity_locks(self):
        import shlex
        import yaml
        workflow = yaml.safe_load((ROOT / '.github/workflows/theorem-state.yml').read_text())
        self.assertEqual(workflow['permissions'], {'contents': 'read'})
        steps = [s for j in workflow['jobs'].values() for s in j['steps']]
        installs = [s for s in steps if 'pip install' in s.get('run', '')]
        self.assertEqual(len(installs), 2)
        wanted = ['control/tools/requirements-integrity-linux-x86_64.lock'] * 2
        for step, lock in zip(installs, wanted):
            tokens = shlex.split(step['run'])
            self.assertIn('--require-hashes', tokens)
            self.assertIn('--only-binary=:all:', tokens)
            self.assertEqual(tokens[tokens.index('-r') + 1], lock)
        self.assertNotIn('requirements-verification-linux-x86_64.lock', str(installs))
        checkout = next(s for s in steps if s.get('uses', '').startswith('actions/checkout@'))
        self.assertFalse(checkout['with']['persist-credentials'])


if __name__ == '__main__':
    unittest.main()
