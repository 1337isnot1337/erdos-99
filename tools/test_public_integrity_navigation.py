"""Current navigation and helper checks do not depend on migration inventories."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from check_public import check_declared_files, check_files


class CurrentNavigationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='e99-current-navigation-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def write(self, path, text):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text)

    @staticmethod
    def record(path, **changes):
        return {'path': path, 'status': 'unreviewed', 'canonical': False,
                'claim_ids': [], 'claim_statuses': {}, **changes}

    @staticmethod
    def old_header(**changes):
        metadata = {'source_canonical': False, 'source_lifecycle': 'unreviewed',
                    'destination_status': 'historical_unreviewed_noncanonical', **changes}
        return '<!-- migration-provenance: ' + json.dumps(metadata) + ' -->\n'

    def test_current_readme_and_code_can_change_without_historical_metadata(self):
        self.write('README.md', '# Research\n[Check](research/check.py)\n')
        self.write('research/check.py', 'from fractions import Fraction\nvalue = Fraction(1, 2)\n')
        self.assertEqual(check_files(self.root, []), ([], 0))
        self.write('README.md', '# Updated instructions\nRun the [check](research/check.py).\n')
        self.write('research/check.py', 'from fractions import Fraction\nvalue = Fraction(2, 3)\n')
        self.assertEqual(check_files(self.root, []), ([], 0))
        self.assertFalse((self.root / '.git').exists())
        self.assertFalse((self.root / 'docs/publication/inclusion.json').exists())
        self.assertFalse((self.root / 'docs/research/migration').exists())

    def test_archived_source_relative_text_and_code_are_data(self):
        self.write('README.md', '# Current entrypoint\n')
        self.write('docs/archive/old/report.md', '[Source-only](../../../../old-source/file.md)\n')
        self.write('docs/archive/old/helper.py', 'def incomplete_source(\n')
        self.write('docs/research/migration/snapshot/report.md', '[Old source](missing-source.md)\n')
        self.write('docs/research/migration/snapshot/check.py', 'import verify_missing_old_helper\n')
        self.assertEqual(check_files(self.root, []), ([], 0))

    def test_current_declared_premise_is_required_without_an_import_inventory(self):
        self.write('docs/proof.md', '# Current proof\n')
        dependencies = {'docs/proof.md': {'docs/premise.md'}}
        self.assertEqual(check_declared_files(self.root, dependencies),
                         ['missing current dependency: docs/premise.md'])
        self.write('docs/premise.md', '# Current premise\n')
        self.assertEqual(check_declared_files(self.root, dependencies), [])
        self.write('docs/premise.md', '# Revised premise\n')
        self.assertEqual(check_declared_files(self.root, dependencies), [])

    def test_current_declared_dependencies_cannot_escape_the_repository(self):
        self.write('docs/proof.md', '# Current proof\n')
        errors = check_declared_files(self.root, {'docs/proof.md': {'../private.md'}})
        self.assertEqual(errors, ['unsafe current dependency: ../private.md'])

    def test_missing_current_proof_link_is_still_an_error(self):
        self.write('README.md', '[Proof](docs/reports/result.md)\n')
        errors, references = check_files(self.root, [])
        self.assertIn('README.md: missing link docs/reports/result.md', errors)
        self.assertEqual(references, 0)
        self.write('docs/reports/result.md', '# Present proof\n')
        self.assertEqual(check_files(self.root, []), ([], 0))

    def test_missing_current_import_helpers_are_still_errors(self):
        self.write('research/check.py', 'import verify_helper\nfrom target_geometry import value\n')
        errors, _ = check_files(self.root, [])
        self.assertEqual(set(errors), {
            'research/check.py: omitted helper verify_helper',
            'research/check.py: omitted helper target_geometry',
        })
        self.write('research/verify_helper.py', 'value = 1\n')
        self.write('research/target_geometry.py', 'value = 2\n')
        self.assertEqual(check_files(self.root, []), ([], 0))

    def test_current_python_syntax_is_checked(self):
        self.write('research/check.py', 'def broken(\n')
        errors, _ = check_files(self.root, [])
        self.assertTrue(any(error.startswith('research/check.py: syntax ') for error in errors))

    def test_legacy_unreviewed_literature_references_do_not_pin_report_bytes(self):
        path = 'docs/reports/old-report.md'
        text = (self.old_header() + '# Unreviewed source note\n'
                '[Paper](../../papers/external.pdf)\n'
                '[Extract](../../extracted/external.txt)\n')
        self.write(path, text)
        records = [self.record(path)]
        self.assertEqual(check_files(self.root, records), ([], 2))
        self.write(path, text + '\nCurrent correction and additional explanation.\n')
        self.assertEqual(check_files(self.root, records), ([], 2))

    def test_legacy_header_does_not_excuse_a_missing_current_proof(self):
        path = 'docs/reports/old-report.md'
        self.write(path, self.old_header() + '[Proof](current-result.md)\n'
                   '[Current bibliography](../../papers/current.bib)\n')
        errors, references = check_files(self.root, [self.record(path)])
        self.assertEqual(references, 0)
        self.assertEqual(set(errors), {
            path + ': missing link docs/reports/current-result.md',
            path + ': missing link papers/current.bib',
        })

    def test_canonical_or_claim_bearing_metadata_never_gets_the_literature_exception(self):
        path = 'docs/reports/old-report.md'
        self.write(path, self.old_header() + '[Paper](../../papers/external.pdf)\n')
        for changes in (
            {'status': 'canonical', 'canonical': True,
             'claim_ids': ['CLAIM'], 'claim_statuses': {'CLAIM': 'canonical'}},
            {'claim_ids': ['CLAIM'], 'claim_statuses': {'CLAIM': 'unreviewed'}},
            {'status': 'audited-working'},
        ):
            with self.subTest(changes=changes):
                errors, references = check_files(self.root, [self.record(path, **changes)])
                self.assertEqual(references, 0)
                self.assertIn(path + ': missing link papers/external.pdf', errors)
        self.write(path, self.old_header(source_canonical=True) + '[Paper](../../papers/external.pdf)\n')
        errors, references = check_files(self.root, [self.record(path)])
        self.assertEqual(references, 0)
        self.assertIn(path + ': missing link papers/external.pdf', errors)


if __name__ == '__main__':
    unittest.main()
