"""Presentation transformations preserve formula bodies and source artifacts."""
import errno
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from build_reading_edition import (
    check, current_document_page, expected_files, math_delimiters, render,
    repair_source,
)


class ReadingEditionTests(unittest.TestCase):
    def test_current_guide_edits_need_no_mirror_or_manifest_update(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            guides = ("AGENTS.md", "autoresearch.md", "CONTRIBUTING.md",
                      "docs/launch/READINESS.md", "tasks/example.md",
                      "docs/research/agent-procedure.md", "docs/research/current-priorities.md",
                      "docs/research/pr-intake.md", "docs/research/research-archive-intake.md",
                      "docs/research/research-package-guide.md")
            for source in (*guides, "docs/theory/example.md"):
                path = root / source
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Original\n")
            before = expected_files(root)
            for source in guides:
                (root / source).write_text("# Edited guide\n\nCurrent instructions.\n")
            self.assertEqual(expected_files(root), before)
            manifest = json.loads(before["reading/manifest.json"])
            self.assertEqual([row["source"] for row in manifest["documents"]],
                             ["docs/theory/example.md"])
            self.assertEqual({row["source"] for row in manifest["current_document_links"]},
                             set(guides))
            for source in guides:
                page = before["reading/" + source]
                self.assertNotIn("Original", page)
                self.assertNotIn("SHA-256", page)
                self.assertIn(source, page)

    def test_math_source_edits_still_require_a_current_reading_view(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "docs/theory/example.md"
            source.parent.mkdir(parents=True)
            source.write_text("\\[x=1\\]\n")
            for name, text in expected_files(root).items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(text.encode("utf-8"))
            source.write_text("\\[x=2\\]\n")
            errors = check(root)
            self.assertIn("stale or missing reading page: reading/docs/theory/example.md", errors)
            self.assertIn("stale or missing reading page: reading/manifest.json", errors)

    def test_old_reading_urls_link_to_current_sources(self):
        self.assertIn("[AGENTS.md](../AGENTS.md)", current_document_page("AGENTS.md"))
        self.assertIn("[docs/launch/READINESS.md](../../../docs/launch/READINESS.md)",
                      current_document_page("docs/launch/READINESS.md"))
        with tempfile.TemporaryDirectory() as tmp:
            page, _ = render("docs/proof.md", "[instructions](../AGENTS.md)",
                             {"docs/proof.md", "AGENTS.md"}, Path(tmp))
        self.assertIn("[instructions](../AGENTS.md)", page)

    def test_current_guide_classification_cannot_discard_a_pinned_math_repair(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENTS.md").write_text("Current guidance.\n")
            registry = root / "docs/publication/reading-tex-repairs.json"
            registry.parent.mkdir(parents=True)
            registry.write_text(json.dumps({"documents": {"AGENTS.md": {}}}))
            with self.assertRaisesRegex(ValueError, "repair refers to a current guidance document"):
                expected_files(root)

    def test_root_guides_reject_symlinks_even_without_reading_their_contents(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target.md").write_text("Guidance.\n")
            try:
                (root / "AGENTS.md").symlink_to("target.md")
            except NotImplementedError as exc:
                self.skipTest(f"native symlink fixture unavailable: {exc}")
            except OSError as exc:
                if (exc.errno in {errno.EACCES, errno.EPERM, errno.ENOSYS, errno.ENOTSUP}
                        or getattr(exc, 'winerror', None) in {1, 50, 1314}):
                    self.skipTest(f"native symlink fixture unavailable: {exc}")
                raise
            with self.assertRaisesRegex(ValueError, "symlinked source document: AGENTS.md"):
                expected_files(root)

    def test_quote_markers_stay_outside_the_equation(self):
        output, _ = math_delimiters("> Claim.\n> \\[\n> F_D^{uniq}\n> \\]\n\nNext.\n")
        self.assertIn("> ```math\n> F_D^{uniq}\n> ```", output)
        self.assertNotIn("\n```math\n>", output)

    def test_underindented_source_math_retains_the_list_and_following_proof(self):
        output, _ = math_delimiters("1. Claim.\n   \\[\n   L-1\\le5e\n|a|\\le50e\n   \\]\n\n## Proof\nText.\n")
        self.assertIn("   ```math\n   L-1\\le5e\n   |a|\\le50e\n   ```", output)
        self.assertIn("\n\n## Proof\nText.", output)

    def test_real_greater_than_is_not_a_quote_marker(self):
        output, _ = math_delimiters("\\[\nx\n> y\n\\]\n")
        self.assertIn("```math\nx\n> y\n```", output)

    def test_table_pipes_are_escaped_without_changing_formula(self):
        with tempfile.TemporaryDirectory() as tmp:
            output, _ = render("docs/a.md", "| Term | Scope |\n| --- | --- |\n| $|A|$ | every label |\n", set(), Path(tmp))
        self.assertIn("$`\\|A\\|`$", output)

    def test_repairs_fail_on_changed_source_or_occurrence_count(self):
        registry = {"a.md": {"source_sha256": "pinned", "replacements": [{"old": "bad", "new": "good", "count": 1}]}}
        self.assertEqual(repair_source("a.md", "bad", "pinned", registry)[0], "good")
        with self.assertRaisesRegex(ValueError, "stale reading repair source"):
            repair_source("a.md", "bad", "changed", registry)
        with self.assertRaisesRegex(ValueError, "stale reading replacement"):
            repair_source("a.md", "bad bad", "pinned", registry)

    def test_truncated_formula_is_a_literal_excerpt(self):
        output, _ = math_delimiters("\\[\\boxed{ x=…\\]", literal_displays=("\\boxed{ x=…",))
        self.assertIn("```text", output)
        self.assertNotIn("```math", output)

    def test_formula_bytes_are_preserved_and_code_examples_are_untouched(self):
        source = "Text \\(a+b\\).\n\n\\[\nx^2 + \\sqrt{3}\n\\]\n\n`\\(literal\\)`\n```python\n'\\[fixture\\]'\n```\n"
        output, pairs = math_delimiters(source)
        self.assertEqual(pairs, 2)
        self.assertIn("$`a+b`$", output)
        self.assertIn("```math\nx^2 + \\sqrt{3}\n```", output)
        self.assertIn("`\\(literal\\)`", output)
        self.assertIn("'\\[fixture\\]'", output)

    def test_display_inside_prose_gets_its_own_block(self):
        output, pairs = math_delimiters("Before \\[a=b\\] after.")
        self.assertEqual(pairs, 1)
        self.assertIn("\n\n```math\na=b\n```\n\n", output)

    def test_links_route_to_reading_pages_but_code_uses_real_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "research").mkdir()
            (root / "research/check.py").write_text("pass\n")
            raw = "[proof](b.md#lemma) [code](../research/check.py)"
            output, _ = render("docs/a.md", raw, {"docs/a.md", "docs/b.md"}, root)
            self.assertIn("[proof](b.md#lemma)", output)
            self.assertIn("[code](../../research/check.py)", output)
            self.assertIn(hashlib.sha256(raw.encode()).hexdigest(), output)

    def test_source_wording_fix_does_not_mutate_source_bytes(self):
        raw = "minimum pairwise distance (1)"
        with tempfile.TemporaryDirectory() as tmp:
            output, _ = render("docs/problem/statement.md", raw, set(), Path(tmp))
        self.assertIn("minimum pairwise distance exactly $`1`$", output)
        self.assertEqual(raw, "minimum pairwise distance (1)")

    def test_existing_dollar_math_preserves_escaped_braces(self):
        source = "$$\n\\{x\\}\n$$ and $\\{y\\}$."
        output, _ = math_delimiters(source)
        self.assertIn("```math\n\\{x\\}\n```", output)
        self.assertIn("$`\\{y\\}`$", output)

    def test_missing_source_closure_does_not_swallow_the_next_paragraph(self):
        diagnostics = {}
        source = "\\[\nx=y\n\nProse.\n\n\\[\na=b\n\\]\n"
        output, count = math_delimiters(source, diagnostics)
        self.assertEqual(count, 2)
        self.assertEqual(diagnostics["repaired_source_delimiters"], 1)
        self.assertIn("```math\nx=y\n```\n\nProse.", output)

    def test_malformed_inline_source_is_preserved_without_guessing_a_formula(self):
        diagnostics = {}
        source = "This has an incomplete \\(x+y) marker.\n\nNext paragraph.\n"
        output, _ = math_delimiters(source, diagnostics)
        self.assertIn("```text\nThis has an incomplete \\(x+y) marker.", output)
        self.assertIn("Next paragraph.", output)
        self.assertEqual(diagnostics["source_excerpts"], 1)

    def test_source_excerpt_does_not_consume_a_preceding_math_fence(self):
        source = "\\[\nx=y\n\\]\nThis proves it. \\(square)\n"
        output, _ = math_delimiters(source)
        self.assertIn("```math\nx=y\n```\n", output)
        self.assertIn("```text\nThis proves it. \\(square)\n```", output)
        self.assertNotIn("````text\n```", output)

    def test_source_hash_binds_raw_crlf_bytes_while_the_view_uses_lf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            original = b"# Test\r\n\r\n\\[\r\nx=y\r\n\\]\r\n"
            (root / "docs/example.md").write_bytes(original)
            outputs = expected_files(root)
            record = json.loads(outputs["reading/manifest.json"])["documents"][0]
            self.assertEqual(record["source_sha256"], hashlib.sha256(original).hexdigest())
            self.assertIn(record["source_sha256"], outputs["reading/docs/example.md"])
            self.assertNotIn("\r", outputs["reading/docs/example.md"])
            self.assertIn("```math\nx=y\n```", outputs["reading/docs/example.md"])
            self.assertEqual((root / "docs/example.md").read_bytes(), original)

