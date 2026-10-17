"""Exercise the published entry command and reject misidentified prerequisites."""
import copy
import datetime as dt
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.choose_research_task import CatalogError, validate_catalog
from scripts import choose_research_task as selector
from scripts import research_coordination as coordination


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


class InvestigationSelectionTests(unittest.TestCase):
    seed = "0123456789abcdef0123456789abcdef"
    instant = dt.datetime(2026, 10, 17, tzinfo=dt.timezone.utc)

    def catalog(self):
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        for task in catalog["tasks"]:
            task["investigation"] = dict(id=task["id"], source_commit="a" * 40,
                                         domain="fixed domain " + task["id"],
                                         question=task["question"], status="open")
        return catalog

    def snapshot(self, task, status="CLAIM", role=None, **markers):
        investigation = task["investigation"]
        marked = {"TASK-ID": task["id"], "INVESTIGATION-ID": investigation["id"],
                  "SCOPE-ID": coordination.investigation_key(investigation),
                  "SOURCE-SHA": investigation["source_commit"], "DOMAIN": investigation["domain"],
                  "QUESTION": investigation["question"], "ROLE": role or coordination.default_role(task),
                  "STATUS": status, "CLAIM-EXPIRES": (self.instant + dt.timedelta(hours=1)).isoformat(),
                  **markers}
        return dict(pulls=[], discussions=[], issues=[dict(number=1, title="investigation", markers=marked,
                    url="https://example.invalid/issue/1", updated_at=self.instant.isoformat())])

    def test_active_exact_claim_is_excluded_before_random_draw(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target)
        with patch.object(coordination, "now", return_value=self.instant):
            selected = selector.select_tasks(catalog, self.seed, len(catalog["tasks"]) - 1, snapshot=snapshot)
        self.assertNotIn(target["id"], {task["id"] for task in selected})

    def test_open_exact_submission_is_occupied_without_an_unexpired_claim(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target)
        row = snapshot["issues"].pop()
        del row["markers"]["STATUS"]
        del row["markers"]["CLAIM-EXPIRES"]
        snapshot["pulls"].append(row)
        state = selector.task_candidates(catalog, snapshot)[0]["selection_state"]
        self.assertEqual(state["reasons"], ["open-exact-submission"])

    def assert_open_submission_survives_later_status(self, status, **markers):
        target = self.catalog()["tasks"][0]
        snapshot = self.snapshot(target)
        pull = snapshot["issues"].pop()
        pull.update(kind="pull", url="https://example.invalid/pull/1")
        pull["markers"].pop("STATUS")
        pull["markers"].pop("CLAIM-EXPIRES")
        snapshot["pulls"].append(pull)
        later = copy.deepcopy(pull)
        later.update(kind="discussion-comment", thread_id="later-claim",
                     url="https://example.invalid/discussion/2#comment-1", number=2,
                     updated_at=(self.instant + dt.timedelta(hours=1)).isoformat())
        later["markers"].update({"STATUS": status, **markers})
        snapshot["discussions"].append(later)
        with patch.object(coordination, "now", return_value=self.instant + dt.timedelta(hours=2)):
            state = coordination.investigation_availability(target, snapshot)
            self.assertFalse(state["eligible"])
            self.assertEqual(state["reasons"], ["open-exact-submission"])
            self.assertEqual([match["url"] for match in state["matches"]], [pull["url"]])
            # Only removal from the open-PR surface releases this submission.
            snapshot["pulls"].clear()
            self.assertTrue(coordination.investigation_availability(target, snapshot)["eligible"])

    def test_released_claim_does_not_release_an_open_submission(self):
        self.assert_open_submission_survives_later_status("RELEASED")

    def test_expired_claim_does_not_release_an_open_submission(self):
        self.assert_open_submission_survives_later_status(
            "CLAIM", **{"CLAIM-EXPIRES": (self.instant + dt.timedelta(hours=1)).isoformat()})

    def test_handoff_does_not_release_an_open_submission(self):
        self.assert_open_submission_survives_later_status("HANDOFF")

    def test_completed_scoped_job_is_excluded_while_global_problem_stays_open(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        target["investigation"]["status"] = "completed"
        selected = selector.select_tasks(catalog, self.seed, len(catalog["tasks"]) - 1)
        self.assertEqual(catalog["problem_status"], "open")
        self.assertNotIn(target["id"], {task["id"] for task in selected})

    def test_completed_investigation_cannot_reappear_through_an_alias_card(self):
        catalog = self.catalog()
        first, second = catalog["tasks"][:2]
        second["investigation"] = copy.deepcopy(first["investigation"])
        first["investigation"]["status"] = "completed"
        candidates = selector.task_candidates(catalog, {})
        self.assertFalse(candidates[0]["selection_state"]["eligible"])
        self.assertFalse(candidates[1]["selection_state"]["eligible"])

    def test_remote_done_excludes_only_the_exact_source_and_domain(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target, "DONE")
        prepared = selector.task_candidates(catalog, snapshot)[0]
        self.assertFalse(prepared["selection_state"]["eligible"])
        for key, changed in (("source_commit", "b" * 40), ("domain", "different domain"),
                             ("question", "a different question")):
            revised = copy.deepcopy(catalog)
            revised["tasks"][0]["investigation"][key] = changed
            self.assertTrue(selector.task_candidates(revised, snapshot)[0]["selection_state"]["eligible"])

    def test_copied_scope_marker_cannot_hide_a_changed_source(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target, "DONE", **{"SOURCE-SHA": "b" * 40})
        self.assertTrue(selector.task_candidates(catalog, snapshot)[0]["selection_state"]["eligible"])

    def assert_changed_identity_preserves_original(self, changes, full_identity=False, separate_root=False,
                                                   reverse_order=False):
        target = self.catalog()["tasks"][0]
        scope = coordination.investigation_key(target["investigation"])
        for status in ("HANDOFF", "CLAIM"):
            with self.subTest(status=status):
                snapshot = self.snapshot(target, status)
                root = snapshot["issues"].pop()
                root.update(kind="discussion-comment", thread_id="original-root")
                changed = copy.deepcopy(root)
                changed.update(kind="discussion-comment" if separate_root else "discussion-reply",
                               thread_id="other-root" if separate_root else "original-root",
                               updated_at=(self.instant + dt.timedelta(minutes=1)).isoformat())
                changed["markers"] = {**(root["markers"] if full_identity else {}),
                                      **changes, "ROLE": root["markers"]["ROLE"], "STATUS": "DONE"}
                snapshot["discussions"] = [changed, root] if reverse_order else [root, changed]
                lifecycles = coordination.investigation_lifecycles(snapshot)
                original = [current for current in lifecycles if current["scope_key"] == scope]
                self.assertEqual([current["status"] for current in original], [status])
                if status == "HANDOFF":
                    self.assertEqual([lead["scope_key"] for lead in coordination.handoff_leads(snapshot)], [scope])
                else:
                    with patch.object(coordination, "now", return_value=self.instant):
                        state = coordination.investigation_availability(target, snapshot)
                    self.assertFalse(state["eligible"])
                    self.assertEqual(state["reasons"], ["active-exact-claim"])

    def test_domain_only_reply_does_not_close_the_original_scope(self):
        self.assert_changed_identity_preserves_original({"DOMAIN": "a different domain"})

    def test_question_only_reply_does_not_close_the_original_scope(self):
        self.assert_changed_identity_preserves_original({"QUESTION": "a different question"})

    def test_complete_identity_overrides_a_copied_scope_id_before_grouping(self):
        for field, value in (("SOURCE-SHA", "b" * 40), ("DOMAIN", "a different domain"),
                             ("QUESTION", "a different question")):
            for separate_root in (False, True):
                with self.subTest(field=field, separate_root=separate_root):
                    self.assert_changed_identity_preserves_original({field: value}, full_identity=True,
                                                                   separate_root=separate_root)

    def test_partial_conflicting_identity_cannot_replace_another_root(self):
        scope = coordination.investigation_key(self.catalog()["tasks"][0]["investigation"])
        for field, value in (("INVESTIGATION-ID", "another investigation"), ("SOURCE-SHA", "b" * 40),
                             ("DOMAIN", "a different domain"), ("QUESTION", "a different question")):
            for reverse_order in (False, True):
                with self.subTest(field=field, reverse_order=reverse_order):
                    self.assert_changed_identity_preserves_original(
                        {"SCOPE-ID": scope, field: value}, separate_root=True, reverse_order=reverse_order)

    def test_matching_partial_identity_can_finish_another_root(self):
        target = self.catalog()["tasks"][0]
        scope = coordination.investigation_key(target["investigation"])
        for status in ("CLAIM", "HANDOFF"):
            for field in (None, "INVESTIGATION-ID", "SOURCE-SHA", "DOMAIN", "QUESTION"):
                for reverse_order in (False, True):
                    with self.subTest(status=status, field=field, reverse_order=reverse_order):
                        snapshot = self.snapshot(target, status)
                        root = snapshot["issues"].pop()
                        root.update(kind="discussion-comment", thread_id="original-root")
                        changed = copy.deepcopy(root)
                        changed.update(thread_id="other-root",
                                       updated_at=(self.instant + dt.timedelta(minutes=1)).isoformat())
                        changed["markers"] = {"SCOPE-ID": scope, "ROLE": root["markers"]["ROLE"], "STATUS": "DONE"}
                        if field:
                            changed["markers"][field] = root["markers"][field]
                        snapshot["discussions"] = [changed, root] if reverse_order else [root, changed]
                        self.assertEqual([current["status"] for current in coordination.investigation_lifecycles(snapshot)],
                                         ["DONE"])
                        self.assertEqual(coordination.handoff_leads(snapshot), [])
                        state = coordination.investigation_availability(target, snapshot)
                        self.assertFalse(state["eligible"])
                        self.assertEqual(state["reasons"], ["completed-exact-scope"])

    def test_method_and_seed_do_not_create_distinct_investigations(self):
        investigation = self.catalog()["tasks"][0]["investigation"]
        self.assertEqual(selector.scope_key("a", "first method", investigation),
                         selector.scope_key("a", "second method", investigation))

    def test_legacy_broad_task_marker_does_not_reserve_entire_family(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target)
        marked = snapshot["issues"][0]["markers"]
        for key in ("INVESTIGATION-ID", "SCOPE-ID", "DOMAIN", "QUESTION"):
            del marked[key]
        with patch.object(coordination, "now", return_value=self.instant):
            self.assertTrue(selector.task_candidates(catalog, snapshot)[0]["selection_state"]["eligible"])

    def test_expired_or_released_claim_does_not_block_a_new_attempt(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        expired = self.snapshot(target, **{"CLAIM-EXPIRES": (self.instant - dt.timedelta(hours=1)).isoformat()})
        with patch.object(coordination, "now", return_value=self.instant):
            for snapshot in (expired, self.snapshot(target, "RELEASED")):
                self.assertTrue(selector.task_candidates(catalog, snapshot)[0]["selection_state"]["eligible"])

    def test_named_awaiting_review_scope_preserves_status_and_reviewer_role(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        target["investigation"]["status"] = "awaiting-review"
        selected = selector.select_tasks(catalog, self.seed, task_id=target["id"], role="reviewer")
        self.assertEqual(selected[0]["role"], "reviewer")
        self.assertEqual(selected[0]["assignment_source"], "explicit")
        self.assertEqual(selected[0]["investigation"]["status"], "awaiting-review")
        self.assertFalse(selected[0]["selection_state"]["eligible"])

    def test_explicit_review_can_share_a_producer_investigation(self):
        catalog = self.catalog()
        identity = catalog["tasks"][0]["id"]
        selected = selector.select_tasks(catalog, self.seed, 4,
                                        assignments=[identity + ":producer", identity + ":reviewer"])
        self.assertEqual([task["role"] for task in selected[:2]], ["producer", "reviewer"])
        self.assertEqual(selected[0]["scope_key"], selected[1]["scope_key"])
        self.assertEqual(len({task["scope_key"] for task in selected}), 3)
        self.assertEqual([task["slot"] for task in selected], [1, 2, 3, 4])

    def test_duplicate_producer_slots_are_rejected_even_through_different_cards(self):
        catalog = self.catalog()
        first, second = catalog["tasks"][:2]
        second["investigation"] = copy.deepcopy(first["investigation"])
        with self.assertRaisesRegex(CatalogError, "duplicate producer"):
            selector.select_tasks(catalog, self.seed, 2,
                                  assignments=[first["id"] + ":producer", second["id"] + ":producer"])
        selected = selector.select_tasks(catalog, self.seed, len(catalog["tasks"]) - 1)
        self.assertEqual(len(selected), len({task["scope_key"] for task in selected}))

    def test_explicit_reviewer_is_not_blocked_by_producer_claim(self):
        catalog = self.catalog()
        target = catalog["tasks"][0]
        snapshot = self.snapshot(target, role="producer")
        with patch.object(coordination, "now", return_value=self.instant):
            selected = selector.select_tasks(catalog, self.seed, task_id=target["id"],
                                             role="reviewer", snapshot=snapshot)
        self.assertTrue(selected[0]["selection_state"]["eligible"])

    def test_cli_loads_snapshot_before_selection(self):
        events = []
        snapshot = dict(source="live-read-only", queried_at=self.instant.isoformat(),
                        pulls=[], issues=[], discussions=[])
        select = selector.select_tasks

        def read(**kwargs):
            events.append("snapshot")
            return snapshot

        def draw(*args, **kwargs):
            events.append("draw")
            self.assertIs(kwargs["snapshot"], snapshot)
            return select(*args, **kwargs)

        with patch.object(selector, "query_open_work", side_effect=read), \
             patch.object(selector, "select_tasks", side_effect=draw), redirect_stdout(io.StringIO()):
            status = selector.main(["--live-overlap", "--count", "1", "--seed", self.seed, "--json"])
        self.assertEqual(status, 0)
        self.assertEqual(events, ["snapshot", "draw"])

    def test_unknown_investigation_status_is_rejected(self):
        catalog = self.catalog()
        catalog["tasks"][0]["investigation"]["status"] = "theorem-solved"
        with self.assertRaisesRegex(CatalogError, "unknown status"):
            validate_catalog(catalog, ROOT)

    def test_claim_template_does_not_parse_its_handoff_example_as_current_status(self):
        catalog = self.catalog()
        selected = selector.select_tasks(catalog, self.seed, task_id=catalog["tasks"][0]["id"])[0]
        result = dict(checkout_commit="b" * 40, checkout_state_version="example", priority_revision="example")
        marked = coordination.markers(coordination.claim_text(result, selected, now=self.instant))
        self.assertEqual(marked["STATUS"], "CLAIM")
        self.assertEqual(marked["SOURCE-SHA"], "a" * 40)
        self.assertEqual(marked["SCOPE-ID"], selected["scope_key"])
        self.assertEqual(marked["ROLE"], selected["role"])

    def test_unknown_claim_is_rejected_even_in_the_manifest_path(self):
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        broken = copy.deepcopy(catalog)
        broken["tasks"][0]["canonical_dependencies"][0]["claim_id"] = "NONEXISTENT-CLAIM"
        with self.assertRaisesRegex(CatalogError, "does not map"):
            validate_catalog(broken, ROOT)
