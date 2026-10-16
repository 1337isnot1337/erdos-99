#!/usr/bin/env python3
"""Rebuild source branch and frozen dirty-worktree ownership for Agent 3."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def remainder(refname: str) -> int:
    return int(hashlib.sha256(refname.encode("utf-8")).hexdigest(), 16) % 3


def refs(repo: Path, prefix: str) -> list[tuple[str, str]]:
    raw = git(repo, "for-each-ref", "--format=%(refname)%09%(objectname)", prefix)
    return [tuple(line.decode().split("\t", 1)) for line in raw.splitlines()]


def revs(repo: Path, *heads: str, exclude: str) -> set[str]:
    if not heads:
        return set()
    raw = git(repo, "rev-list", *heads, "^" + exclude)
    return set(raw.decode().splitlines())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True, help="local source repository with preserved worktrees")
    ap.add_argument("--remote-source", type=Path, required=True, help="fresh mirror of live source refs")
    ap.add_argument("--source-main", required=True)
    ap.add_argument("--open-prs", type=Path, required=True)
    ap.add_argument("--closed-prs", type=Path, required=True)
    ap.add_argument("--dirty-snapshot", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    local_refs = refs(args.source, "refs/heads")
    remote_refs = refs(args.remote_source, "refs/heads")
    pr_refs = [(r, h) for r, h in refs(args.remote_source, "refs/pull") if r.endswith("/head")]
    open_prs = json.loads(args.open_prs.read_text())
    closed_prs = [json.loads(line) for line in args.closed_prs.read_text().splitlines() if line.strip()]
    all_prs = closed_prs + open_prs
    pr_names: dict[str, list[int]] = defaultdict(list)
    pr_heads: set[str] = set()
    for pr in all_prs:
        name = pr.get("headRefName") or pr.get("head_ref_name")
        number = pr.get("number")
        head = pr.get("headRefOid") or pr.get("head_sha")
        if name:
            pr_names[name].append(number)
        if head:
            pr_heads.add(head)
    pr_commit_set = revs(args.remote_source, *(r for r, _ in pr_refs), exclude=args.source_main)

    branch_versions: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for ref, head in local_refs:
        branch_versions[ref].append(("local", head))
    for ref, head in remote_refs:
        branch_versions[ref].append(("live_remote", head))
    branch_commit_sets: dict[str, set[str]] = {}
    heads_out = []
    branch_pr_status: dict[str, bool] = {}
    for ref, versions in sorted(branch_versions.items()):
        short_name = ref.removeprefix("refs/heads/")
        related_prs = sorted(set(pr_names.get(short_name, [])))
        by_head_prs = {head: sorted(pr.get("number") for pr in all_prs
                                    if (pr.get("headRefOid") or pr.get("head_sha")) == head)
                       for _, head in versions}
        is_pr = bool(related_prs or any(by_head_prs.values()) or
                     any(head in pr_heads for _, head in versions))
        branch_pr_status[ref] = is_pr
        union_commits: set[str] = set()
        for origin, head in versions:
            commits = revs(args.source if origin == "local" else args.remote_source,
                           head, exclude=args.source_main)
            union_commits.update(commits)
            if not commits:
                continue
            unaccounted_commits = commits - pr_commit_set
            heads_out.append({
                "refname": ref,
                "origin": origin,
                "head": head,
                "ahead_commit_count": len(commits),
                "sha256_integer_mod_3": remainder(ref),
                "owner": remainder(ref) + 1,
                "pr_associated": is_pr,
                "pr_numbers_by_refname": related_prs,
                "pr_numbers_by_head_sha": by_head_prs.get(head, []),
                "unaccounted_commit_count": len(unaccounted_commits),
                "disposition": "exclude_pr_branch_accounted_separately" if not unaccounted_commits else
                               "assigned_nonpr_branch_residual" if is_pr and remainder(ref) == 2 else
                               "assigned_nonpr_branch" if remainder(ref) == 2 else "assigned_to_other_agent",
            })
        if union_commits:
            branch_commit_sets[ref] = union_commits

    all_branch_commits: dict[str, list[str]] = defaultdict(list)
    for ref, commits in branch_commit_sets.items():
        for commit in commits:
            all_branch_commits[commit].append(ref)
    commit_rows = []
    for commit, reachers in all_branch_commits.items():
        if commit in pr_commit_set:
            status = "accounted_by_source_pr"
            primary = None
            owner = None
        else:
            primary = sorted(reachers)[0]
            owner = remainder(primary) + 1
            status = "unique_unaccounted_branch_commit_assigned"
        try:
            meta_raw = git(args.source, "show", "-s", "--format=%H%x09%an%x09%ae%x09%ad%x09%s",
                           "--date=iso-strict", commit)
        except subprocess.CalledProcessError:
            meta_raw = git(args.remote_source, "show", "-s", "--format=%H%x09%an%x09%ae%x09%ad%x09%s",
                           "--date=iso-strict", commit)
        meta = meta_raw.decode("utf-8", "replace").strip().split("\t", 4)
        commit_rows.append({
            "commit": commit,
            "author": meta[1] if len(meta) > 1 else None,
            "author_email": meta[2] if len(meta) > 2 else None,
            "author_date": meta[3] if len(meta) > 3 else None,
            "subject": meta[4] if len(meta) > 4 else None,
            "reachable_branch_refs": sorted(reachers),
            "reachable_pr_head_commit": commit in pr_commit_set,
            "reachable_pr_head_count": 1 if commit in pr_commit_set else 0,
            "primary_refname": primary,
            "owner": owner,
            "disposition": status if owner is None else
                           "assigned_to_agent_3" if owner == 3 else f"deduplicated_to_agent_{owner}",
        })

    dirty_rows = [json.loads(line) for line in args.dirty_snapshot.read_text().splitlines() if line.strip()]
    dirty_out = []
    for row in dirty_rows:
        branch = row.get("branch")
        refname = branch if isinstance(branch, str) and branch.startswith("refs/heads/") else None
        mapping = "snapshot_branch_ref"
        candidates = []
        if not refname and branch == "detached":
            containing_raw = git(args.source, "for-each-ref", "--contains=" + row.get("head", ""),
                                 "--format=%(refname)", "refs/heads")
            candidates = sorted(containing_raw.decode().splitlines())
            exact = [ref for ref, head in local_refs if head == row.get("head")]
            if exact:
                refname = sorted(exact)[0]
                mapping = "detached_head_exactly_matches_source_branch_head"
            elif candidates:
                refname = candidates[0]
                mapping = "detached_head_mapped_to_lexicographically_first_containing_source_branch"
            else:
                mapping = "detached_head_has_no_current_source_branch_ref"
        rem = remainder(refname) if refname else None
        worktree = row.get("worktree")
        path = row.get("path")
        local_path = Path(worktree) / path if worktree and path else None
        accessible = bool(local_path and local_path.is_file())
        observed = None
        matches = None
        if accessible:
            observed = hashlib.sha256(local_path.read_bytes()).hexdigest()
            matches = observed == row.get("local_sha256")
        dirty_out.append({
            **row,
            "ownership_refname": refname,
            "ownership_mapping": mapping,
            "ownership_ref_candidates": candidates,
            "sha256_integer_mod_3": rem,
            "owner": rem + 1 if rem is not None else None,
            "currently_accessible": accessible,
            "current_observed_sha256": observed,
            "current_matches_frozen_snapshot": matches,
            "disposition": "assigned_dirty_snapshot_agent_3" if rem == 2 and accessible and matches else
                           "assigned_to_other_agent" if rem is not None and rem != 2 else
                           "unresolved_inaccessible_or_ref_unmapped",
        })

    args.output.mkdir(parents=True, exist_ok=True)
    def dump(name: str, rows: list[dict]) -> None:
        (args.output / name).write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in rows))
    dump("source-branch-heads.jsonl", sorted(heads_out, key=lambda r: r["refname"]))
    dump("source-branch-commits.jsonl", sorted(commit_rows, key=lambda r: r["commit"]))
    dump("source-dirty-worktree-allocation.jsonl", sorted(dirty_out, key=lambda r: (r.get("branch", ""), r.get("path", ""))))
    summary = {
        "source_main": args.source_main,
        "local_source_branch_head_count": len(local_refs),
        "live_remote_source_branch_head_count": len(remote_refs),
        "union_source_branch_refname_count": len(branch_versions),
        "ahead_branch_head_version_count": len(heads_out),
        "ahead_branch_head_versions_by_origin": dict(Counter(r["origin"] for r in heads_out)),
        "ahead_branch_head_dispositions": dict(Counter(r["disposition"] for r in heads_out)),
        "branch_owner_counts_including_pr_refs": dict(Counter(str(r["owner"]) for r in heads_out)),
        "agent_3_nonpr_branch_refs": [ref for ref in sorted(branch_versions)
                                      if remainder(ref) == 2 and not branch_pr_status[ref]
                                      and ref in branch_commit_sets],
        "agent_3_residual_pr_named_branch_refs": [r["refname"] for r in heads_out
                                                  if r["owner"] == 3 and r["pr_associated"]
                                                  and r["unaccounted_commit_count"] > 0],
        "all_unique_commit_count_across_source_heads": len(all_branch_commits),
        "unique_commit_count_after_deduplicating_source_prs": sum(1 for r in commit_rows if r["primary_refname"] is not None),
        "commit_rows_including_pr_accounting": len(commit_rows),
        "commit_dispositions": dict(Counter(r["disposition"] for r in commit_rows)),
        "agent_3_commit_count": sum(r["owner"] == 3 for r in commit_rows),
        "frozen_dirty_worktree_path_count": len(dirty_out),
        "dirty_path_dispositions": dict(Counter(r["disposition"] for r in dirty_out)),
        "agent_3_dirty_path_count": sum(r["owner"] == 3 for r in dirty_out),
    }
    (args.output / "source-branch-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
