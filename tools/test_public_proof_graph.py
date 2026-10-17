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
        for rel in (views.STATE_DOC, views.TARGET_C_DOC, views.CERTIFICATE_REGISTRY,
                    views.ONBOARDING_PREREQUISITES, views.MANIFEST):
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((source / rel).read_bytes())
        for rel, content in views.expected_files(self.root, self.state).items():
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8", newline="\n")

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

    def test_current_onboarding_dependency_requires_graph_refresh(self):
        path = self.root / views.ONBOARDING_PREREQUISITES
        supplement = json.loads(path.read_text())
        supplement["file_dependencies"]["docs/current-proof.md"] = ["docs/new-proof-premise.md"]
        path.write_text(json.dumps(supplement))
        code, output = self.check()
        self.assertEqual(code, 1)
        self.assertIn(views.PUBLIC_PROOF_GRAPH, output)
        graph = json.loads(views.publication_proof_graph(self.root, self.state))
        self.assertIn(["docs/current-proof.md", "docs/new-proof-premise.md"], graph["file_edges"])

    def test_current_certificate_dependencies_require_graph_refresh(self):
        path = self.root / views.CERTIFICATE_REGISTRY
        registry = json.loads(path.read_text())
        certificate = registry["certificates"][0]
        certificate.setdefault("proof_sources", []).append("docs/new-certificate-proof.md")
        certificate.setdefault("executable_dependencies", []).append("research/new-helper.py")
        path.write_text(json.dumps(registry))
        code, output = self.check()
        self.assertEqual(code, 1)
        self.assertIn(views.PUBLIC_PROOF_GRAPH, output)
        graph = json.loads(views.publication_proof_graph(self.root, self.state))
        self.assertIn([certificate["path"], "docs/new-certificate-proof.md"], graph["file_edges"])
        self.assertIn(["docs/new-certificate-proof.md", certificate["path"]], graph["file_edges"])
        self.assertIn([certificate["path"], "research/new-helper.py"], graph["file_edges"])

    def test_migration_inventory_is_neither_required_nor_read(self):
        path = self.root / "docs/publication/inclusion.json"
        self.assertFalse(path.exists())
        self.assertEqual(self.check()[0], 0)
        path.write_text("Historical data need not be valid input to this generator.\n")
        self.assertEqual(self.check()[0], 0)

    def test_claim_sources_and_prerequisites_supply_file_edges_without_mutation(self):
        state = {"targets": {"target-c": {"current_canonical_entries": [
            {"id": "CLAIM", "status": "canonical", "report": "docs/proof.md",
             "audit": "docs/audit.md", "certificates": ["research/check.py"], "depends_on": ["PREMISE"]},
            {"id": "PREMISE", "status": "canonical", "report": "docs/premise.md"},
        ]}}}
        before = json.dumps(state, sort_keys=True)
        graph = views.current_file_dependencies(self.root, state, certificates=[], supplement={})
        self.assertEqual(graph["docs/proof.md"], {"docs/audit.md", "research/check.py", "docs/premise.md"})
        self.assertEqual(graph["docs/audit.md"], {"docs/proof.md", "research/check.py", "docs/premise.md"})
        self.assertEqual(json.dumps(state, sort_keys=True), before)

    def test_current_graph_and_other_views_pass(self):
        self.assertEqual(self.check()[0], 0)


if __name__ == "__main__":
    unittest.main()
