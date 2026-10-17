"""Regressions for outsider prerequisite/evidence discovery and scope labels."""
from pathlib import Path
import json
import tempfile
import unittest

import yaml

from tools.task_context import ROOT, context


class TaskContextFixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.write("docs/start.md", "Start.\n")
        self.write("docs/implicit.md", "Implicit section prerequisite.\n")
        self.write("docs/dependency.md", "Dependent claim proof.\n")
        for name in ("registered", "supporting"):
            self.write(f"research/{name}.py", 'if __name__ == "__main__":\n    raise RuntimeError("never execute discovery")\n')
        self.write("research/helper.py", "def helper():\n    return 1\n")
        self.dump("docs/research/agent-task-catalog.json", {"tasks": [{
            "id": "example", "question": "Fixture?",
            "canonical_dependencies": [{"path": "docs/start.md"}],
            "previous_obstructions": [],
        }]})
        self.dump("docs/research/onboarding-prerequisites.json", {
            "file_dependencies": {"docs/start.md": ["docs/implicit.md", "research/supporting.py", "research/helper.py"]},
            "tasks": {},
        })
        self.write("docs/state/theorem-state.yaml", yaml.safe_dump({"targets": {"target-c": {
            "current_canonical_entries": [{"id": "ROOT", "status": "canonical", "report": "docs/implicit.md", "depends_on": ["DEP"]}],
            "regressions": [{"id": "DEP", "status": "regression", "report": "docs/dependency.md", "certificates": ["research/registered.py"]}],
        }}}))
        self.dump("research/certificates.json", {"certificates": [{
            "path": "research/registered.py", "command": "python research/registered.py",
            "claims": ["DEP"], "proof_sources": ["docs/dependency.md"], "scope": ["finite fixture"],
        }]})

    def write(self, path, text):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text)

    def dump(self, path, data):
        self.write(path, json.dumps(data))

    def test_implicit_and_claim_dependencies_reach_evidence_without_execution(self):
        before = (self.root / "docs/state/theorem-state.yaml").read_bytes()
        result = context("example", self.root)
        self.assertIn("docs/implicit.md", result["transitive_file_prerequisites"])
        self.assertIn("docs/dependency.md", result["transitive_file_prerequisites"])
        self.assertEqual(result["certificate_commands"], ["python research/registered.py"])
        self.assertEqual(result["supporting_evidence_commands"], ["python research/supporting.py"])
        self.assertEqual(result["supporting_helpers"], ["research/helper.py"])
        self.assertEqual({r["id"]: r["status"] for r in result["reachable_claims"]},
                         {"ROOT": "canonical", "DEP": "regression"})
        self.assertEqual(before, (self.root / "docs/state/theorem-state.yaml").read_bytes())

    def test_registry_proof_source_is_discovered_without_attached_certificate(self):
        self.write("docs/state/theorem-state.yaml", "targets: {}\n")
        self.dump("research/certificates.json", {"certificates": [{
            "path": "research/registered.py", "command": "python research/registered.py",
            "proof_sources": ["docs/implicit.md"],
        }]})
        self.assertEqual(context("example", self.root)["certificate_commands"], ["python research/registered.py"])

    def test_current_registry_proof_and_executable_dependencies_are_followed(self):
        path = self.root / "research/certificates.json"
        registry = json.loads(path.read_text())
        record = registry["certificates"][0]
        record["proof_sources"].append("docs/extra-proof.md")
        record["executable_dependencies"] = [record["path"], "research/certificate_helper.py"]
        self.dump("research/certificates.json", registry)
        self.write("docs/extra-proof.md", "Current certificate proof input.\n")
        self.write("research/certificate_helper.py", "def helper():\n    return 2\n")
        result = context("example", self.root)
        self.assertIn("docs/extra-proof.md", result["transitive_file_prerequisites"])
        self.assertIn("research/certificate_helper.py", result["supporting_helpers"])
        self.assertEqual(result["certificate_commands"], ["python research/registered.py"])

    def test_migration_inventory_is_neither_required_nor_read(self):
        path = self.root / "docs/publication/inclusion.json"
        self.assertFalse(path.exists())
        expected = context("example", self.root)
        self.write("docs/publication/inclusion.json", "Historical data; no active parser.\n")
        self.assertEqual(context("example", self.root), expected)

    def test_current_prerequisites_do_not_depend_on_a_generated_graph_refresh(self):
        self.dump("docs/publication/proof-graph.json", {"claims": [], "file_edges": []})
        self.write("docs/new-prerequisite.md", "Newly declared reading prerequisite.\n")
        path = self.root / "docs/research/onboarding-prerequisites.json"
        supplement = json.loads(path.read_text())
        supplement["file_dependencies"]["docs/start.md"].append("docs/new-prerequisite.md")
        self.dump("docs/research/onboarding-prerequisites.json", supplement)
        self.assertIn("docs/new-prerequisite.md", context("example", self.root)["transitive_file_prerequisites"])

    def test_unknown_task_is_an_explicit_error(self):
        with self.assertRaisesRegex(ValueError, "unknown task"):
            context("missing", self.root)

    def test_audited_working_premise_is_reachable_without_promotion(self):
        catalogue = json.loads((self.root / 'docs/research/agent-task-catalog.json').read_text())
        catalogue['tasks'][0]['audited_working_premises'] = [{'path': 'docs/working.md'}]
        self.dump('docs/research/agent-task-catalog.json', catalogue)
        self.write('docs/working.md', 'Scoped working premise, not canonical.\n')
        self.assertIn('docs/working.md', context('example', self.root)['transitive_file_prerequisites'])

    def test_missing_and_outside_prerequisites_fail(self):
        for path in ("docs/missing.md", "../private.md", "/tmp/private.md"):
            with self.subTest(path=path):
                self.dump("docs/research/onboarding-prerequisites.json", {
                    "file_dependencies": {"docs/start.md": [path]},
                })
                with self.assertRaises(ValueError):
                    context("example", self.root)


class PublicRouteRegressions(unittest.TestCase):
    def test_three_audited_routes_have_scoped_evidence(self):
        expected = {
            "target-a-locked-sector-surplus": "python research/tube_shield_cut_audit.py",
            "target-b-multigrain-transfer": "python research/phase_cut_certificate.py",
            "target-c-face-coupled-move": "python research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py",
        }
        for task, command in expected.items():
            with self.subTest(task=task):
                result = context(task, ROOT)
                self.assertIn(command, result["supporting_evidence_commands"])
                self.assertNotIn(command, result["certificate_commands"])
        a = context("target-a-locked-sector-surplus", ROOT)
        self.assertIn("docs/theory/03-oler-shell.md", a["transitive_file_prerequisites"])
        self.assertIn("docs/targets/target-a/03-source-response.md", a["transitive_file_prerequisites"])
        self.assertIn("docs/targets/target-a/26-tube-shield-sector-balance.md", a["transitive_file_prerequisites"])
        b = context('target-b-multigrain-transfer', ROOT)
        self.assertIn('docs/theory/03-oler-shell.md', b['transitive_file_prerequisites'])
        for report in (
            "target_b_dual_tree_dense_grid_extraction_correction_2026-09-05.md",
            "target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md",
            "target_b_positive_density_dual_tree_grid_2026-09-05.md",
            "target_b_penetration_charged_grid_cancellation_2026-09-05.md",
            "target_b_multicomponent_penetration_budget_2026-09-05.md",
            "target_b_balanced_phase_stability_exclusion_2026-09-05.md",
            "target_b_explicit_general_phase_interpolation_2026-09-05.md",
        ):
            self.assertIn("docs/reports/" + report, b["transitive_file_prerequisites"])
        c = context("target-c-face-coupled-move", ROOT)
        for prerequisite in (
            "docs/reports/target_c_full_source_circumradius_response_2026-09-10.md",
            "docs/reports/target_c_fs_symmetry_difference_body_2026-09-10.md",
            "docs/audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md",
            "docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md",
            "docs/targets/target-c/01-force-hull-and-shear.md",
            "research/campaign_2026_09_09_exact.py",
            "research/verify_target_c_face_coupled_quarter_folds_2026_10_07.py",
        ):
            self.assertIn(prerequisite, c["transitive_file_prerequisites"])


if __name__ == "__main__":
    unittest.main()
