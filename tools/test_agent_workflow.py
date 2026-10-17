"""Behavioral regressions for coordination, review reuse and non-executing package checks."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import research_coordination as coordination
from scripts.choose_research_task import CatalogError, validate_catalog
from scripts.new_research_package import create
from scripts import pr_intake as intake
from scripts.research_package import check
from scripts.workflow_common import REPOSITORY, atomic_json, git, timestamp


def snapshot(**extra):
    return dict(schema_version=2, repository=REPOSITORY, queried_at=timestamp(),
                source="live-read-only", pulls=[], issues=[], discussions=[], coverage={}, **extra)


def row(number=1, body="", kind="pulls", updated="2026-10-17T00:00:00Z"):
    return dict(number=number, title="A different title", body=body, kind=kind,
                url="https://example.invalid/work", updated_at=updated,
                markers=coordination.markers(body))


class OverlapTests(unittest.TestCase):
    def test_body_only_match_and_bounded_excerpt(self):
        result = coordination.search([row(body="x" * 900 + "PAID seam" + "y" * 900)], ["paid seam"])
        self.assertEqual(len(result), 1)
        self.assertIn("PAID seam", result[0]["excerpt"])
        self.assertLessEqual(len(result[0]["excerpt"]), 500)
        self.assertNotIn("body", result[0])

    def test_blank_marker_cannot_consume_the_following_line(self):
        self.assertNotEqual(coordination.markers("E99-STATUS:\nE99-NEXT-ACTION: inspect")
                            .get("STATUS"), "E99-NEXT-ACTION: inspect")

    def test_claim_cannot_reserve_an_arbitrarily_distant_expiry(self):
        self.assertIn("seven-day-limit", coordination.claim_status(
            row(body="E99-CLAIM-EXPIRES: 2099-01-01T00:00:00Z")))

    def test_latest_done_releases_a_discussion_handoff(self):
        data = snapshot()
        data["discussions"] = [row(body="E99-STATUS: HANDOFF\nE99-REMAINING: bridge"),
                               row(body="E99-STATUS: DONE", kind="discussion-comment",
                                   updated="2026-10-17T01:00:00Z")]
        self.assertEqual(coordination.handoff_leads(data), [])

    def test_handoff_reports_the_exact_remaining_action(self):
        data = snapshot()
        data["issues"] = [row(body="E99-STATUS: HANDOFF\nE99-TASK-ID: abc\nE99-NEXT-ACTION: check the bridge")]
        lead = coordination.handoff_leads(data)[0]
        self.assertEqual(lead["task_id"], "abc")
        self.assertEqual(lead["next_action"], "check the bridge")

    def test_cache_is_repository_bound_and_offline_status_explicit(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / "cache.json"
            atomic_json(cache, snapshot())
            with patch.object(coordination, "pages", side_effect=AssertionError("network")):
                self.assertEqual(coordination.query_open_work(cache=cache)["source"], "cached-read-only")
                self.assertEqual(coordination.query_open_work(cache=cache, offline=True)["source"], "offline-saved-query")
            data = snapshot(); data["repository"] = "another/project"; atomic_json(cache, data)
            with self.assertRaisesRegex(ValueError, "another repository"):
                coordination.query_open_work(cache=cache)

    def test_stale_offline_cache_is_never_labelled_live(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / "cache.json"
            data = snapshot(); data["queried_at"] = "2001-01-01T00:00:00Z"
            data["issues"] = [row(body="E99-CLAIM-EXPIRES: 2001-01-02T00:00:00Z")]
            atomic_json(cache, data)
            result = coordination.query_open_work(cache=cache, offline=True)
            self.assertEqual(result["source"], "offline-saved-query")
            self.assertEqual(result["issues"][0]["claim_status"], "expired")

    def test_missing_offline_cache_has_unknown_remote_coverage(self):
        result = coordination.query_open_work(offline=True)
        self.assertEqual(result["source"], "offline-no-remote-data")
        self.assertEqual(result["discussions_availability"], "unknown")

    def test_offline_closed_scope_is_explicitly_unavailable(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / "cache.json"; atomic_json(cache, snapshot())
            result = coordination.query_open_work(cache=cache, offline=True, include_closed=True)
            self.assertIn("closed-PR coverage", result["warnings"][0])

    def test_malformed_timestamp_fails_as_an_input_error(self):
        data = snapshot(); data["queried_at"] = None
        with self.assertRaisesRegex(ValueError, "timestamp"):
            coordination.validate_snapshot(data)

    def test_failed_refresh_preserves_the_old_cache(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / "cache.json"; atomic_json(cache, snapshot())
            before = cache.read_bytes()
            with patch.object(coordination, "pages", side_effect=ValueError("network failed")):
                with self.assertRaisesRegex(ValueError, "network failed"):
                    coordination.query_open_work(cache=cache, refresh=True)
            self.assertEqual(before, cache.read_bytes())

    def test_disabled_discussions_and_issue_pr_filter_are_visible(self):
        item = dict(number=3, title="draft", body="bridge", html_url="https://example.invalid", head={"sha":"a"*40})
        with patch.object(coordination, "pages", side_effect=[[item], [item | {"pull_request": {}}]]), \
             patch.object(coordination, "gh", return_value={"has_discussions":False}):
            data = coordination.query_open_work()
        self.assertEqual(len(data["pulls"]), 1)
        self.assertEqual(data["issues"], [])
        matched = coordination.overlap_for_task(dict(id="bridge", overlap_terms=[]), data)
        self.assertEqual(matched["discussions_availability"], "disabled")
        self.assertTrue(matched["coverage"]["pulls"]["complete_pagination"])

    def test_unknown_discussion_availability_is_not_labelled_disabled(self):
        with patch.object(coordination, "pages", return_value=[]), patch.object(coordination, "gh", return_value={}):
            with self.assertRaisesRegex(ValueError, "availability is unknown"):
                coordination.query_open_work()

    def test_graphql_discussion_comment_and_reply_pagination(self):
        calls = []
        def response(query, **variables):
            calls.append(variables)
            if "repository(" in query:
                nodes = [] if variables.get("cursor") else [dict(id="d", number=8, title="Topic", body="start", url="u", updatedAt="t")]
                return {"repository":{"discussions":{"nodes":nodes,"pageInfo":{"hasNextPage":bool(nodes),"endCursor":"discussion-next"}}}}
            if variables["id"] == "d":
                nodes = [] if variables.get("cursor") else [dict(id="c",body="comment",url="c",updatedAt="t")]
                field, cursor = "comments", "comment-next"
            else:
                nodes = [dict(id="r2",body="last reply",url="r2",updatedAt="t")] if variables.get("cursor") else [dict(id="r",body="first reply",url="r",updatedAt="t")]
                field, cursor = "replies", "reply-next"
            return {"node":{field:{"nodes":nodes,"pageInfo":{"hasNextPage":bool(nodes) and not variables.get("cursor"),"endCursor":cursor}}}}
        with patch.object(coordination, "graphql", side_effect=response):
            records = coordination._discussions(REPOSITORY)
        self.assertEqual([r["body"] for r in records], ["start","comment","first reply","last reply"])
        self.assertTrue(any(c.get("cursor") == "discussion-next" for c in calls))
        self.assertTrue(any(c.get("cursor") == "comment-next" for c in calls))
        self.assertTrue(any(c.get("cursor") == "reply-next" for c in calls))

    def test_selector_accepts_saved_current_repository_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / "overlap.json"; atomic_json(cache, snapshot())
            process = subprocess.run([sys.executable, "scripts/choose_research_task.py", "--count", "1", "--overlap-snapshot", str(cache), "--json"],
                                     cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["overlap_status"], "offline-saved-query")

    def test_prior_coverage_rejects_unpinned_external_evidence(self):
        catalog = json.loads((ROOT / "docs/research/agent-task-catalog.json").read_text())
        checked = next(task for task in catalog["tasks"] if task["existing_checks"])
        checked["existing_checks"][0]["evidence"] = "https://github.com/another/project/blob/main/report.md"
        with self.assertRaisesRegex(CatalogError, "exact source SHA"):
            validate_catalog(catalog)


class RepositoryFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        git(self.root, "init", "-q")
        git(self.root, "config", "user.name", "Workflow tests")
        git(self.root, "config", "user.email", "workflow-tests@example.invalid")
        git(self.root, "config", "commit.gpgsign", "false")
        git(self.root, "config", "core.hooksPath", str(self.root / "no-hooks"))
        self.write("source.md", "Pinned evidence\n")
        for path in (intake.STATE, intake.LEDGER):
            atomic_json(self.root / path, dict(schema_version=1,repository=REPOSITORY,entries={}))
        atomic_json(self.root / "docs/research/agent-task-catalog.json", dict(tasks=[dict(id="example")]))
        self.base = self.commit()
        self.live = [dict(number=1, head_sha="a"*40, title="one", url="u")]

    def write(self, path, text):
        target = self.root / path; target.parent.mkdir(parents=True, exist_ok=True); target.write_text(text)

    def commit(self):
        git(self.root, "add", "."); git(self.root, "commit", "-qm", "fixture")
        return git(self.root, "rev-parse", "HEAD")

    def args(self, **changes):
        values = dict(number=1,head="a"*40,base_ref="HEAD",status="waiting_revision",lane="archive",
                      review_status="partially_reviewed",reason="missing bridge",coverage="source intake only",
                      remaining="prove the bridge",evidence=["source.md"],watch_path=[],watch_pr=[])
        return argparse.Namespace(**(values | changes))

    def held(self, **changes):
        decision = dict(head_sha="a"*40, status="waiting_revision",policy_version=intake.POLICY_VERSION,
                        watch_paths={},watch_prs={}) | changes
        return dict(entries={"1":decision})


class IntakeTests(RepositoryFixture):
    def test_unchanged_hold_stays_dormant_after_unrelated_main_commit(self):
        self.write("unrelated.txt", "new"); base = self.commit()
        plan = intake.make_plan(self.root, base, self.live, self.held())
        self.assertEqual(plan["actionable_count"], 0)
        self.assertEqual(len(plan["dormant"]), 1)

    def test_changed_head_invalidates_ready_status(self):
        live = [self.live[0] | dict(head_sha="b"*40)]
        plan = intake.make_plan(self.root, self.base, live, self.held(status="ready_to_integrate"))
        self.assertIn("changed-head", plan["selected"][0]["reasons"])
        self.assertEqual(plan["selected"][0]["scheduling_status"], "pending_review")

    def test_watched_source_change_wakes_hold(self):
        state = self.held(watch_paths={"source.md":intake.identity(self.root, self.base, "source.md")})
        self.write("source.md", "changed"); base = self.commit()
        plan = intake.make_plan(self.root, base, self.live, state)
        self.assertIn("changed-path:source.md", plan["selected"][0]["reasons"])

    def test_file_mode_change_is_part_of_watched_identity(self):
        state = self.held(watch_paths={"source.md":intake.identity(self.root, self.base, "source.md")})
        git(self.root, "update-index", "--chmod=+x", "source.md")
        git(self.root, "commit", "-qm", "mode change")
        base = git(self.root, "rev-parse", "HEAD")
        self.assertIn("changed-path:source.md", intake.make_plan(self.root, base, self.live, state)["selected"][0]["reasons"])

    def test_watched_pr_departure_wakes_hold_without_claiming_merge(self):
        plan = intake.make_plan(self.root, self.base, self.live, self.held(watch_prs={"2":"b"*40}))
        self.assertIn("changed-pr:2", plan["selected"][0]["reasons"])
        self.assertIn("does not establish merging", plan["limits"])

    def test_pending_review_remains_actionable_and_deferred_replay_dormant(self):
        for status, count in [("pending_review",1),("deferred_replay",0)]:
            plan = intake.make_plan(self.root, self.base, self.live, self.held(status=status))
            self.assertEqual(plan["actionable_count"], count)
        plan = intake.make_plan(self.root, self.base, self.live, self.held(), wake=[1])
        self.assertIn("explicit-wake", plan["selected"][0]["reasons"])

    def test_changed_policy_wakes_a_hold(self):
        plan = intake.make_plan(self.root, self.base, self.live, self.held(policy_version=-1))
        self.assertIn("changed-policy", plan["selected"][0]["reasons"])

    def test_new_heads_precede_continuing_reviews_and_limit_is_honest(self):
        live = self.live + [dict(number=2,head_sha="b"*40,title="two",url="v")]
        plan = intake.make_plan(self.root, self.base, live, self.held(status="pending_review"), limit=1)
        self.assertEqual(plan["selected"][0]["number"], 2)
        self.assertEqual(plan["remaining_actionable"], 1)

    def test_changed_live_head_cannot_be_recorded(self):
        before = (self.root / intake.LEDGER).read_bytes()
        with self.assertRaisesRegex(ValueError, "reviewed head"):
            intake.record(self.root, self.args(head="b"*40), self.live)
        self.assertEqual(before, (self.root / intake.LEDGER).read_bytes())

    def test_uncommitted_review_evidence_cannot_be_recorded(self):
        self.write("source.md", "uncommitted")
        with self.assertRaisesRegex(ValueError, "commit the exact"):
            intake.record(self.root, self.args(), self.live)

    def test_archive_receipt_does_not_become_scientifically_verified(self):
        with self.assertRaisesRegex(ValueError, "partially_reviewed"):
            intake.record(self.root, self.args(review_status="scope_verified"), self.live)
        intake.record(self.root, self.args(), self.live)
        ledger = intake.document(self.root, intake.LEDGER)
        self.assertEqual(ledger["entries"]["1"][0]["review_status"], "partially_reviewed")
        self.assertEqual(ledger["entries"]["1"][0]["evidence"][0]["commit"], self.base)

    def test_repeated_identical_decision_does_not_duplicate_ledger(self):
        intake.record(self.root, self.args(), self.live)
        intake.record(self.root, self.args(), self.live)
        self.assertEqual(len(intake.document(self.root, intake.LEDGER)["entries"]["1"]), 1)

    def test_lock_refuses_an_overlapping_record_without_losing_state(self):
        with intake.recording_lock(self.root):
            with self.assertRaises(FileExistsError):
                intake.record(self.root, self.args(), self.live)
        self.assertEqual(intake.document(self.root, intake.LEDGER)["entries"], {})

    def test_offline_fixture_is_labelled_and_cannot_modify_cache(self):
        fixture = self.root / "live.json"
        atomic_json(fixture, dict(repository=REPOSITORY,pulls=self.live))
        before = (self.root / intake.STATE).read_bytes()
        process = subprocess.run([sys.executable,str(ROOT / "scripts/pr_intake.py"),"--root",str(self.root),"plan","--live-json",str(fixture),"--base-ref","HEAD"],capture_output=True,text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["source"], "offline-fixture")
        self.assertEqual(before, (self.root / intake.STATE).read_bytes())

    def test_plan_output_cannot_overwrite_scheduling_state(self):
        fixture = self.root / "live.json"; atomic_json(fixture, dict(repository=REPOSITORY,pulls=self.live))
        before = (self.root / intake.STATE).read_bytes()
        process = subprocess.run([sys.executable,str(ROOT / "scripts/pr_intake.py"),"--root",str(self.root),"plan","--live-json",str(fixture),"--base-ref","HEAD","--output",str(self.root / intake.STATE)],capture_output=True,text=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("cannot overwrite", process.stderr)
        self.assertEqual(before, (self.root / intake.STATE).read_bytes())


class LocalNoteTests(RepositoryFixture):
    def test_local_search_does_not_follow_symlinked_parent_directories(self):
        self.write("docs/reports/note.md", "original"); self.commit()
        directory = self.root / "docs/reports"
        (directory / "note.md").unlink(); directory.rmdir()
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "note.md").write_text("outside source")
            try:
                directory.symlink_to(temp, target_is_directory=True)
            except OSError as exc:
                self.skipTest(str(exc))
            self.assertFalse(any(row["body"] == "outside source" for row in coordination.local_records(self.root)))


class PackageTests(RepositoryFixture):
    def package(self):
        return create(self.root,"example-package","example","Workflow tests",["source.md"])

    def test_draft_metadata_is_valid_but_replay_is_unresolved_and_checker_fails(self):
        directory = self.package()
        result = check(self.root,"research-packages/example-package")
        self.assertFalse(result["executed_commands"])
        self.assertFalse(result["replay_authorized"])
        process = subprocess.run([sys.executable,"-O",str(directory / "verify.py")],capture_output=True,text=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("Draft package", process.stderr)

    def test_pinned_source_change_is_detected(self):
        self.package(); self.write("source.md","different")
        with self.assertRaisesRegex(ValueError,"hash mismatch"):
            check(self.root,"research-packages/example-package")

    def test_resolved_metadata_still_cannot_authorize_replay_or_verify_a_theorem(self):
        directory = self.package()
        code = "assert 2 + 2 == 4\n"
        self.write("research-packages/example-package/verify.py", code)
        source = json.loads((directory / "SOURCES.json").read_text())
        source["inputs"][-1]["sha256"] = hashlib.sha256(code.encode()).hexdigest()
        source["unresolved"] = []
        atomic_json(directory / "SOURCES.json", source)
        result = check(self.root,"research-packages/example-package")
        self.assertEqual(result["unresolved"], [])
        self.assertFalse(result["full_verified"])
        self.assertFalse(result["replay_authorized"])

    def test_generator_rejects_dirty_sources_and_existing_packages(self):
        directory = self.package(); before = (directory / "README.md").read_bytes()
        with self.assertRaises(FileExistsError):
            self.package()
        self.assertEqual(before,(directory / "README.md").read_bytes())
        self.write("source.md","dirty")
        with self.assertRaisesRegex(ValueError,"differs from HEAD"):
            create(self.root,"another-package","example","Workflow tests",["source.md"])
        self.assertFalse((self.root / "research-packages/another-package").exists())

    def test_generator_rejects_path_escape_and_symlink_sources(self):
        with self.assertRaises(ValueError):
            create(self.root,"../escape","example","Workflow tests",["source.md"])
        link = self.root / "link.md"
        try:
            link.symlink_to("source.md")
        except OSError as exc:
            self.skipTest(str(exc))
        with self.assertRaisesRegex(ValueError,"symlink"):
            create(self.root,"symlink-package","example","Workflow tests",["link.md"])

    def test_metadata_check_never_executes_declared_code(self):
        directory = self.package()
        code = 'open("sentinel", "w").write("executed")\n'
        self.write("research-packages/example-package/verify.py", code)
        path = directory / "SOURCES.json"; source = json.loads(path.read_text())
        source["inputs"][-1]["sha256"] = hashlib.sha256(code.encode()).hexdigest()
        atomic_json(path,source)
        result = check(self.root,"research-packages/example-package")
        self.assertFalse(result["executed_commands"])
        self.assertFalse((self.root / "sentinel").exists())


if __name__ == "__main__":
    unittest.main()
