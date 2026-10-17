"""Documentation edits stay structural; declared mathematical inputs remain protected."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

from tools.localized_ci.plan import make_plan
from tools.run_theorem_certificates import main, select_certificates


class DocumentationDiffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='e99-document-scope-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'CI Test')
        self.git('config', 'user.email', 'ci-test@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        self.state = {'targets': {'target-c': {'current_canonical_entries': [{
            'id': 'CLAIM', 'status': 'canonical',
            'report': 'docs/reports/result.md', 'audit': 'docs/audits/result.md',
            'certificates': ['research/check.py'],
        }]}}}
        self.write('docs/state/theorem-state.yaml', yaml.safe_dump(self.state))
        self.write('README.md', '# Fixture\n')
        self.write('docs/reports/result.md', '# Proof\n')
        self.write('docs/audits/result.md', '# Audit\n')
        self.write('docs/theory/lemma.md', '# Lemma\n')
        self.write('research/check.py', 'assert 1 + 1 == 2\n')
        self.json('research/certificates.json', {'certificates': [{
            'path': 'research/check.py', 'proof_sources': ['docs/reports/result.md'],
            'executable_dependencies': ['research/check.py'],
        }]})
        self.json('docs/research/onboarding-prerequisites.json', {'file_dependencies': {
            'docs/reports/result.md': ['docs/theory/lemma.md'],
        }})
        self.base = self.commit()

    def git(self, *args):
        return subprocess.check_output(
            ['git', '-C', str(self.root), *args], stderr=subprocess.PIPE,
        ).decode().strip()

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8', newline='\n')

    def json(self, path, obj):
        self.write(path, json.dumps(obj) + '\n')

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def assert_scope(self, changed, *, full):
        plan = make_plan(self.root, self.base)
        selection = select_certificates(self.state, changed, root=self.root)
        self.assertEqual(plan['level'], 'full-verification-required' if full else 'fast-only', plan)
        self.assertEqual(selection.paths is None, full, selection)
        self.assertFalse(plan['full_verified'])
        self.assertFalse(plan['replay_allowed'])

    def test_navigation_markdown_has_the_same_fast_scope_in_both_selectors(self):
        changed = set()
        for path in (
            'README.md', 'autoresearch.md', 'docs/COORDINATION.md',
            'tasks/new-question.md', 'docs/ci/README.md', 'docs/launch/READINESS.md',
            'docs/prompts/session.md', 'docs/research/research-priority-log.md',
            'docs/research/tracks/route.md', 'docs/targets/target-c/README.md',
            'research/README.md', 'reading/docs/reports/result.md',
        ):
            with self.subTest(path=path):
                self.write(path, '# Navigation clarification\n')
                self.commit()
                changed.add(path)
                self.assert_scope(changed, full=False)

    def test_certificate_proof_source_overrides_the_task_directory(self):
        self.write('tasks/proof-input.md', '# Registered proof input\n')
        registry = json.loads((self.root / 'research/certificates.json').read_text(encoding='utf-8'))
        registry['certificates'][0]['proof_sources'].append('tasks/proof-input.md')
        self.json('research/certificates.json', registry)
        self.base = self.commit()
        self.write('tasks/proof-input.md', '# Changed mathematical input\n')
        self.commit()
        self.assert_scope({'tasks/proof-input.md'}, full=True)

    def test_reading_manifest_is_structural_but_cannot_hide_changed_proof(self):
        self.json('reading/manifest.json', {'documents': []})
        self.commit()
        self.assert_scope({'reading/manifest.json'}, full=False)
        self.write('docs/reports/result.md', '# Changed mathematical argument\n')
        self.commit()
        self.assert_scope({'reading/manifest.json', 'docs/reports/result.md'}, full=True)

    def test_transitive_proof_dependencies_override_workflow_directories(self):
        self.json('docs/research/onboarding-prerequisites.json', {'file_dependencies': {
            'docs/reports/result.md': ['tasks/bridge.md'],
            'tasks/bridge.md': ['docs/ci/proof-input.md'],
            'docs/ci/proof-input.md': ['tasks/bridge.md'],
        }})
        self.write('tasks/bridge.md', '# Intermediate premise\n')
        self.write('docs/ci/proof-input.md', '# Proof input\n')
        self.base = self.commit()
        self.write('docs/ci/proof-input.md', '# Changed proof input\n')
        self.commit()
        self.assert_scope({'docs/ci/proof-input.md'}, full=True)

    def test_unknown_proof_markdown_is_not_assumed_to_be_navigation(self):
        self.write('docs/reports/new-result.md', '# New proof\n')
        self.commit()
        self.assert_scope({'docs/reports/new-result.md'}, full=True)

    def test_documentation_does_not_hide_a_verifier_change(self):
        self.write('README.md', '# Clarified setup\n')
        self.write('research/check.py', 'assert 2 + 2 == 4\n')
        self.commit()
        self.assert_scope({'README.md', 'research/check.py'}, full=True)

    def test_malformed_dependency_metadata_cannot_make_prose_safe(self):
        self.write('research/certificates.json', '{broken\n')
        self.write('README.md', '# Clarification\n')
        self.commit()
        plan = make_plan(self.root, self.base)
        self.assertTrue(plan['errors'])
        selection = select_certificates(self.state, {'README.md'}, root=self.root)
        self.assertIsNone(selection.paths)
        self.assertIn('dependency metadata', selection.reason)

    def test_explicit_certificate_command_still_selects_the_full_registry(self):
        # Assert command selection without executing any mathematical verifier.
        with patch('tools.run_theorem_certificates.subprocess.run') as run:
            run.return_value.returncode = 0
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['--root', str(self.root)]), 0)
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.args[0][-1], 'check.py')


if __name__ == '__main__':
    unittest.main()
