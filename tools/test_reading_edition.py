"""Presentation transformations preserve formula bodies and source artifacts."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from build_reading_edition import math_delimiters, render


class ReadingEditionTests(unittest.TestCase):
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
