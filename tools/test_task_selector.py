"""Exercise the published entry command and reject misidentified prerequisites."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.choose_research_task import CatalogError, validate_catalog


class PublishedSelectorTests(unittest.TestCase):
    def test_documented_command_selects_from_the_complete_catalogue(self):
        result = subprocess.run(
            [sys.executable, "scripts/choose_research_task.py", "--count", "1",
             "--seed", "0123456789abcdef0123456789abcdef", "--json"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        data = json.loads(result.stdout)
        self.assertEqual(data["status"], "SUGGESTIONS_ONLY_NOT_RESERVED")
        self.assertEqual(len(data["suggestions"]), 1)
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        self.assertIn(data["suggestions"][0]["id"], {task["id"] for task in catalog["tasks"]})
        self.assertTrue(data["state_matches_reviewed_snapshot"])

    def test_known_claim_cannot_be_assigned_to_an_unrelated_existing_proof(self):
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        broken = copy.deepcopy(catalog)
        task = next(t for t in broken["tasks"] if t["id"] == "target-c-branch-aware-atomic-gap")
        ref = next(r for r in task["canonical_dependencies"] if r.get("claim_id") == "C-HOLE-GRID-DIAMETER")
        ref["path"] = "docs/problem/statement.md"
        with self.assertRaisesRegex(CatalogError, "does not map"):
            validate_catalog(broken, ROOT)

    def test_unknown_claim_is_rejected_even_in_the_manifest_path(self):
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        broken = copy.deepcopy(catalog)
        broken["tasks"][0]["canonical_dependencies"][0]["claim_id"] = "NONEXISTENT-CLAIM"
        with self.assertRaisesRegex(CatalogError, "does not map"):
            validate_catalog(broken, ROOT)
