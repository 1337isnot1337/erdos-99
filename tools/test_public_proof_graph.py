"""Reject stale lifecycle/statement and dependency views in the public JSON graph."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools import generate_theorem_state_views as views


class PublicProofGraphTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        source = Path(__file__).resolve().parents[1]
        self.state = views.load(source)
        for rel in (views.STATE_DOC, views.TARGET_C_DOC, "docs/publication/inclusion.json", views.MANIFEST):
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((source / rel).read_bytes())
        for rel, content in views.expected_files(self.root, self.state).items():
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content)

    def check(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            code = views.main(["--root", str(self.root)])
        return code, output.getvalue()

    def test_withdrawn_claim_cannot_remain_canonical_in_json(self):
        path = self.root / views.PUBLIC_PROOF_GRAPH
        graph = json.loads(path.read_text())
        claim = next(c for c in graph["claims"] if c["id"] == "C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION")
        self.assertEqual(claim["status"], "audited-working")
        claim["status"] = "canonical"
        claim["statement"] = "Withdrawn global Lipschitz chart and O(D^(4/5)) rate"
        path.write_text(json.dumps(graph, indent=2) + "\n")
        code, output = self.check()
        self.assertEqual(code, 1)
        self.assertIn(views.PUBLIC_PROOF_GRAPH, output)

    def test_new_manifest_dependency_requires_graph_refresh(self):
        path = self.root / "docs/publication/inclusion.json"
        inclusion = json.loads(path.read_text())
        inclusion["entries"][0].setdefault("dependencies", []).append("docs/new-proof-premise.md")
        path.write_text(json.dumps(inclusion))
        code, output = self.check()
        self.assertEqual(code, 1)
        self.assertIn(views.PUBLIC_PROOF_GRAPH, output)

    def test_current_graph_and_other_views_pass(self):
        self.assertEqual(self.check()[0], 0)


if __name__ == "__main__":
    unittest.main()
