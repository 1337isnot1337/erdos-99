#!/usr/bin/env python3
"""Plan changed PR reviews and persist exact-head decisions; never execute or merge submissions.

Design informed by CrocSwap/integer-mult-bounds, Apache-2.0,
463113d675af7410ac91d53a4fed51ec6494eb9a. This implementation is repository-specific.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
from pathlib import Path
import re
import subprocess

try:
    from scripts.workflow_common import REPOSITORY, ROOT, SHA, atomic_json, git, pages, regular_file, repo_path, timestamp
except ModuleNotFoundError:
    from workflow_common import REPOSITORY, ROOT, SHA, atomic_json, git, pages, regular_file, repo_path, timestamp

POLICY_VERSION = 1
STATE = "docs/research/pr-intake-state.json"
LEDGER = "docs/research/pr-ledger.json"
STATUSES = ("ready_to_integrate", "pending_review", "waiting_revision", "deferred_replay")
LANES = ("archive", "validated-research", "shared-tooling", "canonical-promotion")


def document(root, path):
    data = json.loads(regular_file(root, path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("repository") != REPOSITORY:
        raise ValueError("intake document belongs to another repository or schema")
    if not isinstance(data.get("entries"), dict):
        raise ValueError("invalid intake entries")
    return data


def metadata(fixture=None):
    if fixture:
        result = json.loads(Path(fixture).read_text(encoding="utf-8"))
        if result.get("repository") != REPOSITORY or not isinstance(result.get("pulls"), list):
            raise ValueError("invalid offline queue fixture")
        rows = result["pulls"]
    else:
        rows = pages(f"repos/{REPOSITORY}/pulls?state=open&per_page=100")
    clean = []
    for row in rows:
        head = row.get("head_sha") or row.get("head", {}).get("sha")
        if type(row.get("number")) is not int or row["number"] < 1 or not SHA.fullmatch(head or ""):
            raise ValueError("invalid PR number/head in queue")
        clean.append(dict(number=row["number"], head_sha=head, title=row["title"],
                          url=row.get("html_url", row.get("url"))))
    if len({row["number"] for row in clean}) != len(clean):
        raise ValueError("duplicate PR metadata")
    return clean


def identity(root, base, path):
    path = repo_path(path)
    # Includes mode/type as well as blob/tree ID; a missing input is a distinct identity.
    return git(root, "--literal-pathspecs", "ls-tree", base, "--", path) or "missing"


def make_plan(root, base, live, state, *, wake=(), limit=100, source="live-read-only"):
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    heads = {str(row["number"]): row["head_sha"] for row in live}
    actionable, dormant = [], []
    for row in live:
        key = str(row["number"])
        previous = state["entries"].get(key)
        reasons = []
        if previous is None:
            reasons.append("new-head")
        else:
            if previous["head_sha"] != row["head_sha"]:
                reasons.append("changed-head")
            if previous.get("policy_version") != POLICY_VERSION:
                reasons.append("changed-policy")
            for path, expected in previous.get("watch_paths", {}).items():
                if identity(root, base, path) != expected:
                    reasons.append("changed-path:" + path)
            for number, expected in previous.get("watch_prs", {}).items():
                if heads.get(number, "not-open") != expected:
                    reasons.append("changed-pr:" + number)
        if row["number"] in wake:
            reasons.append("explicit-wake")
        status = previous["status"] if previous else "pending_review"
        if status not in STATUSES:
            raise ValueError("unknown persisted scheduling status")
        if not reasons and status in ("ready_to_integrate", "pending_review"):
            reasons.append("unfinished-action")
        if reasons and reasons != ["unfinished-action"]:
            status = "pending_review"
        entry = dict(**row, scheduling_status=status, reasons=reasons,
                     prior_decision=previous)
        (actionable if reasons else dormant).append(entry)
    actionable.sort(key=lambda row: (row["reasons"] == ["unfinished-action"], row["number"]))
    return dict(schema_version=1, repository=REPOSITORY, policy_version=POLICY_VERSION,
                checked_at=timestamp(), source=source, base_commit=base,
                open_count=len(live), actionable_count=len(actionable),
                selected=actionable[:limit], remaining_actionable=len(actionable[limit:]),
                dormant=dormant, no_longer_open=sorted(set(state["entries"]) - set(heads)),
                limits="Scheduling only. Departure from the open queue does not establish merging or acceptance. Comment-only evidence requires --wake. No research code was executed.")


@contextlib.contextmanager
def recording_lock(root):
    # A shared repository lock also protects record operations from other worktrees.
    lock = Path(git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")) / "erdos99-pr-intake.lock"
    lock.mkdir()  # Fail visibly instead of overwriting another reviewer's decisions.
    try:
        yield
    finally:
        lock.rmdir()


def record(root, args, live):
    if not SHA.fullmatch(args.head):
        raise ValueError("--head must be a full lowercase SHA")
    row = next((row for row in live if row["number"] == args.number), None)
    if row is None or row["head_sha"] != args.head:
        raise ValueError("PR is no longer open at the reviewed head; refresh and review the delta")
    if not args.reason.strip() or not args.coverage.strip() or not args.remaining.strip():
        raise ValueError("reason, coverage and remaining obligation must be explicit")
    base = git(root, "rev-parse", "--verify", args.base_ref + "^{commit}")
    evidence = []
    for path in args.evidence:
        source = regular_file(root, path)
        committed = subprocess.check_output(["git", "-C", str(root), "show", "HEAD:" + repo_path(path)],
                                            stderr=subprocess.PIPE, timeout=60)
        if source.read_bytes() != committed:
            raise ValueError("commit the exact review evidence before recording its receipt")
        evidence.append(dict(path=path, commit=git(root, "rev-parse", "HEAD"),
                             sha256=hashlib.sha256(committed).hexdigest()))
    if args.lane == "archive" and args.review_status != "partially_reviewed":
        raise ValueError("archive intake leaves scientific review partially_reviewed")
    heads = {str(row["number"]): row["head_sha"] for row in live}
    decision = dict(head_sha=args.head, status=args.status, policy_version=POLICY_VERSION,
                    checked_at=timestamp(), base_commit=base, reason=args.reason,
                    lane=args.lane, review_status=args.review_status, coverage=args.coverage,
                    remaining=args.remaining, evidence=evidence,
                    watch_paths={p: identity(root, base, p) for p in set(args.watch_path) | set(args.evidence)},
                    watch_prs={str(n): heads.get(str(n), "not-open") for n in args.watch_pr})
    with recording_lock(root):
        state, ledger = document(root, STATE), document(root, LEDGER)
        key = str(args.number)
        def reusable(value):
            if value is None:
                return None
            comparable = {k: v for k, v in value.items() if k not in ("checked_at", "base_commit", "evidence")}
            comparable["evidence"] = [{k: v for k, v in row.items() if k != "commit"}
                                      for row in value.get("evidence", [])]
            return comparable
        if reusable(state["entries"].get(key)) == reusable(decision):
            return decision
        # Ledger first: a crash before the cache update leaves extra actionable review,
        # never a scheduling-only receipt masquerading as scientific acceptance.
        ledger["entries"].setdefault(key, []).append(decision)
        atomic_json(Path(root) / LEDGER, ledger)
        state["entries"][key] = decision
        atomic_json(Path(root) / STATE, state)
    return decision


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    plan = commands.add_parser("plan")
    inputs = plan.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--refresh", action="store_true")
    inputs.add_argument("--live-json", type=Path, help="offline diagnostic fixture; never fresh GitHub evidence")
    plan.add_argument("--base-ref")
    plan.add_argument("--remote", default="origin", help="canonical remote; forks may use upstream")
    plan.add_argument("--output", type=Path)
    plan.add_argument("--wake", type=int, action="append", default=[])
    plan.add_argument("--limit", type=int, default=100)
    save = commands.add_parser("record")
    save.add_argument("--number", type=int, required=True)
    save.add_argument("--head", required=True)
    save.add_argument("--base-ref", default="origin/main")
    save.add_argument("--status", choices=STATUSES, required=True)
    save.add_argument("--lane", choices=LANES, required=True)
    save.add_argument("--review-status", choices=("partially_reviewed", "scope_verified"), required=True)
    for flag in ("reason", "coverage", "remaining"):
        save.add_argument("--" + flag, required=True)
    save.add_argument("--evidence", action="append", required=True)
    save.add_argument("--watch-path", action="append", default=[])
    save.add_argument("--watch-pr", type=int, action="append", default=[])
    args = parser.parse_args(argv)
    try:
        if args.command == "plan":
            if args.refresh:
                if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*", args.remote):
                    raise ValueError("invalid canonical remote name")
                remote = git(args.root, "remote", "get-url", args.remote)
                if remote.removesuffix(".git") not in ("https://github.com/" + REPOSITORY, "git@github.com:" + REPOSITORY):
                    raise ValueError("selected remote is not canonical erdos-99; use --remote with the canonical remote")
                git(args.root, "fetch", "--no-tags", args.remote,
                    f"+refs/heads/main:refs/remotes/{args.remote}/main")
            reference = args.base_ref or args.remote + "/main"
            base = git(args.root, "rev-parse", "--verify", reference + "^{commit}")
            result = make_plan(args.root, base, metadata(args.live_json), document(args.root, STATE),
                               wake=args.wake, limit=args.limit,
                               source="offline-fixture" if args.live_json else "live-read-only")
            if args.output:
                atomic_json(args.output, result)
        else:
            result = record(args.root, args, metadata())
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
