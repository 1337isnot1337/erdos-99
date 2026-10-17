"""Regression tests for full-corpus navigation and immutable-source mappings."""
import json
from pathlib import Path
import tempfile
import unittest

from audit_migration_navigation import (ReferenceError, audit, markdown_links, navigation_markdown,
                                        original_context, resolve, write_navigation)

DOC = "docs/reports/report.md"
TARGET = "research/check.py"
ARCHIVE = "docs/archive/source-e99-main-42f0296d/docs/reports/report.md.source"
CHECK = "docs/research/migration/2026-10-16/integration/source-main/research/check.py.source"
BLOB = "a" * 40


class NavigationTests(unittest.TestCase):
    def test_active_missing_link_stays_blocked_with_archive_copy(self):
        tree = {DOC: ("100644", "b" * 40), CHECK: ("100644", BLOB)}
        result = audit(tree, {DOC: "[check](../../research/check.py)"}, {TARGET: BLOB})
        self.assertEqual(result["status"], "BLOCKED_ACTIVE_DOCUMENT_PATHS")
        self.assertEqual(result["active_blocking_references"][0]["navigation_target"], CHECK)

    def test_historical_mapping_is_distinct_from_literal_resolution(self):
        tree = {ARCHIVE: ("100644", "b" * 40), CHECK: ("100644", BLOB)}
        result = audit(tree, {ARCHIVE: "[check](../../research/check.py)"}, {TARGET: BLOB})
        row = result["references"][0]
        self.assertEqual(row["status"], "broken_literal_link")
        self.assertEqual(row["mapping_status"], "exact_source_target_preserved")
        self.assertEqual(row["source_target"], TARGET)
        self.assertEqual(result["active_blocking_references"], [])
        self.assertEqual(result["historical_unresolved_references"], [])

    def test_resolved_active_target_does_not_require_archive_map(self):
        result = audit({DOC: ("100644", BLOB), TARGET: ("100644", BLOB)},
                       {DOC: "[x](../../research/check.py)"}, {})
        self.assertEqual(result["reference_counts"], {"resolved_file": 1})

    def test_unsupported_file_mode_blocks(self):
        result = audit({DOC: ("100644", BLOB), TARGET: ("120000", BLOB)},
                       {DOC: "[x](../../research/check.py)"}, {})
        self.assertEqual(result["active_blocking_references"][0]["status"], "unsupported_target_mode")

    def test_unresolved_historical_reference_stays_explicit(self):
        result = audit({ARCHIVE: ("100644", BLOB)}, {ARCHIVE: "[x](missing.md)"}, {})
        self.assertEqual(len(result["historical_unresolved_references"]), 1)
        self.assertEqual(result["historical_unresolved_references"][0]["mapping_status"], "unresolved")

    def test_unsafe_historical_reference_has_serializable_counts(self):
        result = audit({ARCHIVE: ("100644", BLOB)}, {ARCHIVE: "[x](file:///etc/passwd) [missing](missing.md)"}, {})
        self.assertEqual(result["historical_mapping_counts"], {"unsafe_reference": 1, "unresolved": 1})
        json.dumps(result, sort_keys=True)

    def test_branch_snapshot_mapping_does_not_claim_exact_old_dependency_version(self):
        branch = "docs/archive/source-e99-branches/branch/commits/fb895e5c738a/docs/reports/report.md.source"
        result = audit({branch: ("100644", "b" * 40), CHECK: ("100644", BLOB)},
                       {branch: "[check](../../research/check.py)"}, {TARGET: BLOB})
        self.assertEqual(result["references"][0]["mapping_status"], "pinned_source_main_target_preserved")
        self.assertIn("not established", result["references"][0]["mapping_limit"])

    def test_same_snapshot_suffix_target_precedes_pinned_main_fallback(self):
        root = "docs/research/migration/2026-10-16/agent-1/payload/source-branches/branch/fb895e5c738a/"
        document = root + "docs/reports/report.md.source"
        target = root + "research/check.py.source"
        tree = {document: ("100644", "b" * 40), target: ("100644", "c" * 40), CHECK: ("100644", BLOB)}
        result = audit(tree, {document: "[check](../../research/check.py)"}, {TARGET: BLOB})
        row = result["references"][0]
        self.assertEqual(row["mapping_status"], "same_snapshot_preserved_target")
        self.assertEqual(row["navigation_target"], target)

    def test_other_snapshot_fallback_discloses_unknown_dependency_version(self):
        first = "docs/research/migration/2026-10-16/agent-1/payload/source-branches/branch/fb895e5c738a/"
        second = "docs/research/migration/2026-10-16/agent-1/payload/source-branches/other/075d6d99fdc7/"
        document = first + "docs/reports/report.md.source"
        target = second + "research/old-check.py.source"
        result = audit({document: ("100644", "b" * 40), target: ("100644", "c" * 40)},
                       {document: "[check](../../research/old-check.py)"}, {})
        self.assertEqual(result["references"][0]["mapping_status"], "other_historical_target_version_unverified")
        self.assertIn("not established", result["references"][0]["mapping_limit"])

    def test_external_reference_bytes_are_not_imported(self):
        result = audit({DOC: ("100644", BLOB)}, {DOC: "[paper](../../papers/a.pdf)"}, {})
        self.assertEqual(result["active_blocking_references"], [])
        self.assertEqual(result["references"][0]["mapping_status"], "external_reference_not_redistributed")
        self.assertFalse(result["deprecation_ready"])

    def test_fenced_and_inline_code_do_not_produce_links(self):
        text = "[real](a.md)\n```markdown\n[example](missing.md)\n```\n`[example](missing2.md)`"
        self.assertEqual(markdown_links(text), [("a.md", 1)])

    def test_math_products_are_not_markdown_links(self):
        text = "[real](a.md)\n\\[\nN(C):=[J(C)-0.072](3C-W_0).\n\\]\n$[a](b)$\n$$[c](d)$$\n\\([e](f)\\)"
        self.assertEqual(markdown_links(text), [("a.md", 1)])

    def test_balanced_and_escaped_parentheses(self):
        text = r"[a](a_(b).md) [b](a_\(c\).md) [c](<file with spaces.md>)"
        self.assertEqual([x[0] for x in markdown_links(text)], ["a_(b).md", "a_(c).md", "file with spaces.md"])

    def test_explicit_reference_links_are_checked(self):
        text = "[one][target]\n[Two][]\n[target]: a.md\n[two]: <b b.md>\n"
        self.assertEqual(markdown_links(text), [("a.md", 1), ("b b.md", 2)])

    def test_unsafe_paths_remain_blocking(self):
        for link in ("../../../../outside", "%2e%2e/%2e%2e/%2e%2e/out", "/etc/passwd", "file:///x", "../../.git/config"):
            with self.subTest(link=link):
                self.assertEqual(resolve(DOC, link)[0], "unsafe_reference")

    def test_original_context_from_each_archive_layout(self):
        examples = {
            ARCHIVE: DOC,
            "docs/research/migration/2026-10-16/agent-1/payload/source-main/docs/reports/report.md": DOC,
            "docs/research/migration/2026-10-16/integration/source-main/docs/reports/report.md.source": DOC,
            "docs/research/migration/2026-10-16/agent-2/corpus/source-main/docs/reports/report.md.source": DOC,
            "docs/archive/source-e99-branches/research/branch/commits/fb895e5c738a/docs/reports/report.md.source": DOC,
            "docs/research/migration/2026-10-16/agent-1/payload/source-branches/research/branch/075d6d99fdc7b9ebd972e335b1f6c040e0bf5dad/docs/reports/report.md.source": DOC,
            "docs/research/migration/2026-10-16/agent-2/branches/agent-2/research/branch/fb895e5c738a/docs/reports/report.md.source": DOC,
            "docs/research/migration/2026-10-16/agent-1/payload/source-pr-737/docs/reports/report.md": DOC,
            "docs/research/migration/2026-10-16/agent-2/source-pr/pr-0949/docs/reports/report.md.source": DOC,
            "docs/research/migration/2026-10-16/agent-2/branches/agent-2/worktrees/e99-gap-cycle/docs/reports/report.md.source": DOC,
        }
        for path, expected in examples.items():
            with self.subTest(path=path):
                self.assertEqual(original_context(path, {}, {}, BLOB), expected)

    def test_corrected_filename_mapping_does_not_assert_byte_identity(self):
        target = "research/target_c_allregime_fan_train_floor_hostile_audit_2026-09-12.md"
        document = "docs/archive/source-e99-main-42f0296d/research/README.md.source"
        result = audit({document: ("100644", BLOB), target: ("100644", "c" * 40)},
                       {document: "[audit](target_c_allregime_fan_train_floor_reaudit_2026-09-12.md)"}, {})
        self.assertEqual(result["references"][0]["mapping_status"], "corrected_historical_filename")
        self.assertIn("no old dependency version", result["references"][0]["mapping_limit"])

    def test_dirty_archive_context_uses_known_source_path(self):
        path = "docs/research/migration/2026-10-16/agent-1/payload/source-dirty-worktrees/research/global-repacking-20261012/research/README.md"
        self.assertEqual(original_context(path, {"research/README.md": BLOB}, {}, "b" * 40), "research/README.md")

    def test_pinned_dirty_context_maps_file_absent_from_source_main(self):
        document = "docs/research/migration/2026-10-16/agent-2/branches/agent-2/worktrees/e99-fan/docs/reports/report.md.source"
        program = "docs/research/migration/2026-10-16/agent-1/payload/source-dirty-worktrees/swarm/sol/fan/research/old-check.py"
        result = audit({document: ("100644", "b" * 40), program: ("100644", BLOB)},
                       {document: "[check](../../research/old-check.py)"}, {}, {program: "research/old-check.py"})
        self.assertEqual(result["references"][0]["navigation_target"], program)
        self.assertEqual(result["references"][0]["mapping_status"], "other_historical_target_version_unverified")

    def test_navigation_contains_exact_target_without_modifying_raw_document(self):
        text = "[check](../../research/check.py)"
        result = audit({ARCHIVE: ("100644", "b" * 40), CHECK: ("100644", BLOB)},
                       {ARCHIVE: text}, {TARGET: BLOB})
        output = navigation_markdown(result, "docs/map.md")
        self.assertIn("[Immutable source](archive/source-e99-main-42f0296d/docs/reports/report.md.source)", output)
        self.assertIn("[exact_source_target_preserved](research/migration/2026-10-16/integration/source-main/research/check.py.source)", output)
        self.assertEqual(text, "[check](../../research/check.py)")

    def test_navigation_output_refuses_symlink_ancestor_and_existing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / "repo"
            repo.mkdir()
            (root / "actual").mkdir()
            (root / "linked").symlink_to(root / "actual", target_is_directory=True)
            with self.assertRaises(ReferenceError):
                write_navigation(root / "linked" / "map.md", repo, "bad")
            output = root / "map.md"
            write_navigation(output, repo, "original")
            with self.assertRaises(ReferenceError):
                write_navigation(output, repo, "overwrite")
            self.assertEqual(output.read_text(), "original")


if __name__ == "__main__":
    unittest.main()
