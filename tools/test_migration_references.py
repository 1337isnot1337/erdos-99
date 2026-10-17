"""Regression tests for literal migration link checks."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from check_migration_references import (GitReader, ReferenceError, analyze, local_target,
                                        safe_path, write_receipt, require_recorded_blobs, PINNED_EVIDENCE)

DOC = 'docs/reports/a.md'
TARGET = 'research/example.py'
BLOB = 'a' * 40


def receipt(document=DOC, original=DOC, link='../../research/example.py', target=TARGET, **extra):
    row = dict(markdown_destination=document, markdown_source_path=original,
               link_target=link, normalized_source_target=target)
    row.update(extra)
    return {'unresolved_relative_links': [row]}


class ReferenceTests(unittest.TestCase):
    def run_case(self, more=None, document=DOC, text='[check](../../research/example.py)', rec=None):
        tree = {document: ('100644', 'b' * 40)}
        tree.update(more or {})
        return analyze(rec or receipt(), tree, {document: text}, {TARGET: BLOB})

    def test_original_path_resolves(self):
        report = self.run_case({TARGET: ('100644', BLOB)})
        self.assertEqual(report['blocking_references'], [])
        self.assertEqual(report['counts'], {'resolved_file': 1})

    def test_archived_copy_does_not_resolve_literal_link(self):
        report = self.run_case({'archive/example.py': ('100644', BLOB)})
        row = report['blocking_references'][0]
        self.assertEqual(row['status'], 'missing_link_preserved_elsewhere')
        self.assertEqual(row['exact_archive_candidates'], ['archive/example.py'])

    def test_owner_label_cannot_clear_missing_reference(self):
        report = self.run_case(rec=receipt(category='assigned_to_agent_2', owner_or_scope=2))
        self.assertEqual(report['status'], 'BLOCKED')

    def test_empty_source_evidence_does_not_clear_link(self):
        report = analyze(receipt(), {DOC: ('100644', BLOB)},
                         {DOC: '[x](../../research/example.py)'}, {})
        self.assertEqual(report['counts'], {'missing_link_and_content': 1})

    def test_archived_document_uses_actual_location(self):
        archive = 'archive/agent/docs/reports/a.md'
        report = self.run_case({TARGET: ('100644', BLOB)}, document=archive,
                               rec=receipt(document=archive))
        self.assertEqual(report['blocking_references'][0]['target'], 'archive/agent/research/example.py')

    def test_missing_document_blocks(self):
        report = analyze(receipt(), {}, {}, {})
        self.assertEqual(report['errors'][0]['status'], 'missing_document')

    def test_external_reference_is_separate(self):
        rec = receipt(link='../../papers/a.pdf', target='papers/a.pdf')
        report = self.run_case(text='[paper](../../papers/a.pdf)', rec=rec)
        self.assertEqual(report['counts'], {'reference_not_redistributed': 1})
        self.assertFalse(report['release_verified'])

    def test_forged_reference_exclusion_is_rejected(self):
        with self.assertRaises(ReferenceError):
            self.run_case(rec=receipt(target='papers/a.pdf'))

    def test_symlink_target_is_not_followed(self):
        report = self.run_case({TARGET: ('120000', BLOB)})
        self.assertEqual(report['counts'], {'unsupported_target_mode': 1})

    def test_new_relative_link_is_also_checked(self):
        report = self.run_case({TARGET: ('100644', BLOB)},
                               text='[x](../../research/example.py) [y](missing.md)')
        self.assertEqual(report['counts']['missing_link_and_content'], 1)

    def test_reference_removed_without_reconciliation_blocks(self):
        report = self.run_case(text='Reference removed.')
        self.assertEqual(report['counts'], {'historical_receipt_link_changed_or_not_inline': 1})

    def test_external_links_and_fragments_not_claimed_verified(self):
        report = self.run_case({TARGET: ('100644', BLOB)},
                               text='[x](../../research/example.py) [web](https://example.org/x) [a](#section)')
        self.assertEqual(report['counts']['external'], 1)
        self.assertEqual(report['counts']['anchor'], 1)
        self.assertFalse(report['deprecation_ready'])

    def test_unsafe_links_block(self):
        for link in ('../../../../escape', 'file:///etc/passwd', '/root/file', '../../.git/config'):
            with self.subTest(link=link):
                report = self.run_case(text='[x](../../research/example.py) [bad](' + link + ')')
                self.assertIn('unsafe_reference', report['counts'])

    def test_encoded_escape_rejected(self):
        with self.assertRaises(ReferenceError):
            local_target('a.md', '%2e%2e/out')

    def test_duplicate_receipt_entries_do_not_inflate_counts(self):
        rec = receipt()
        rec['unresolved_relative_links'] *= 2
        report = self.run_case({TARGET: ('100644', BLOB)}, rec=rec)
        self.assertEqual(report['counts'], {'resolved_file': 1})

    def test_parent_directory_link(self):
        report = self.run_case({TARGET: ('100644', BLOB)},
                               text='[x](../../research/example.py) [dir](../../research/)')
        self.assertEqual(report['counts']['resolved_directory'], 1)

    def test_receipt_is_non_overwriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / 'repo'
            repo.mkdir()
            output = root / 'receipt.json'
            write_receipt(output, repo, {'ok': True})
            with self.assertRaises(ReferenceError):
                write_receipt(output, repo, {'ok': False})
            self.assertEqual(json.loads(output.read_text()), {'ok': True})

    def test_receipt_symlink_ancestor_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'repo').mkdir()
            (root / 'real').mkdir()
            (root / 'link').symlink_to(root / 'real', target_is_directory=True)
            with self.assertRaises(ReferenceError):
                write_receipt(root / 'link' / 'out.json', root / 'repo', {})

    def test_git_reader_reads_committed_not_dirty_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True).stdout
            git('init', '-q')
            git('config', 'user.name', 'Migration Test')
            git('config', 'user.email', 'migration-test@example.invalid')
            (root / 'a.md').write_text('committed\n')
            git('add', 'a.md')
            git('commit', '-qm', 'fixture')
            (root / 'a.md').write_text('dirty\n')
            reader = GitReader(root)
            commit, tree = reader.tree('HEAD')
            self.assertEqual(len(commit), 40)
            self.assertEqual(reader.text(tree, 'a.md'), 'committed\n')

    def test_evidence_pin_is_enforced(self):
        tree = {p: ("100644", oid) for p, oid in PINNED_EVIDENCE.items()}
        require_recorded_blobs(tree)
        tree[next(iter(tree))] = ("100644", "c" * 40)
        with self.assertRaises(ReferenceError):
            require_recorded_blobs(tree)

    def test_git_replacement_cannot_change_reported_commit_contents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True).stdout
            git('init', '-q')
            git('config', 'user.name', 'Migration Test')
            git('config', 'user.email', 'migration-test@example.invalid')
            (root / 'a.md').write_text('original\n')
            git('add', 'a.md')
            git('commit', '-qm', 'original')
            original = git('rev-parse', 'HEAD').decode().strip()
            (root / 'a.md').write_text('replacement\n')
            git('add', 'a.md')
            git('commit', '-qm', 'replacement')
            replacement = git('rev-parse', 'HEAD').decode().strip()
            git('replace', original, replacement)
            self.assertEqual(git('show', original + ':a.md').decode(), 'replacement\n')
            reader = GitReader(root)
            commit, tree = reader.tree(original)
            self.assertEqual(commit, original)
            self.assertEqual(reader.text(tree, 'a.md'), 'original\n')

    def test_missing_evidence_blocks(self):
        with self.assertRaises(ReferenceError):
            require_recorded_blobs({})

    def test_unsafe_repository_path_rejected(self):
        for path in ('a/../b', '/a', 'a\\b', 'a/.GiT/config', 'a\x00b'):
            with self.subTest(path=path), self.assertRaises(ReferenceError):
                safe_path(path)


if __name__ == '__main__':
    unittest.main()
