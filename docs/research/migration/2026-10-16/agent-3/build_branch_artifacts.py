#!/usr/bin/env python3
"""Inventory mathematical file versions introduced by Agent 3 branch commits."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def tree(repo: Path, revision: str) -> dict[str, str]:
    raw = git(repo, "ls-tree", "-rz", "--full-tree", revision)
    out = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        _mode, kind, oid = meta.decode("ascii").split()
        if kind == "blob":
            out[path.decode("utf-8", "surrogateescape")] = oid
    return out


def is_math_evidence(path: str) -> bool:
    if path in ("docs/state/artifact-index.jsonl", "research/README.md"):
        return False
    return path.startswith(("research/", "docs/reports/", "docs/audits/",
                           "docs/targets/", "docs/theory/", "docs/prompts/"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--source-main", required=True)
    ap.add_argument("--destination-main", required=True)
    ap.add_argument("--commit-ledger", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    main_tree = tree(args.source, args.source_main)
    dest_tree = tree(args.destination, args.destination_main)
    main_blobs = set(main_tree.values())
    dest_blobs = set(dest_tree.values())
    dest_by_blob: dict[str, list[str]] = defaultdict(list)
    for path, oid in dest_tree.items():
        dest_by_blob[oid].append(path)
    commits = [json.loads(line) for line in args.commit_ledger.read_text().splitlines() if line.strip()]
    commits = [r for r in commits if r.get("owner") == 3]

    versions: dict[tuple[str, str], dict] = {}
    commit_changed_paths = 0
    for row in commits:
        commit = row["commit"]
        parents = git(args.source, "show", "-s", "--format=%P", commit).decode().strip().split()
        if parents:
            parent = parents[0]
            # `diff-tree`'s default merge view is combined and can omit a file
            # introduced only by the second parent. Compare the merge tree with
            # its first parent explicitly so merge-resolution/branch additions
            # are part of the branch artifact ledger.
            paths = git(args.source, "diff-tree", "--no-commit-id", "--name-only", "-r",
                         "--no-renames", parent, commit).decode("utf-8", "surrogateescape").splitlines()
            parent_tree = None
        else:
            paths = git(args.source, "diff-tree", "--root", "--no-commit-id", "--name-only", "-r",
                         commit).decode("utf-8", "surrogateescape").splitlines()
            parent = None
            parent_tree = {}
        commit_changed_paths += len(paths)
        commit_tree = None
        for path in sorted(set(paths)):
            if not is_math_evidence(path):
                continue
            if commit_tree is None:
                commit_tree = tree(args.source, commit)
            if parent is not None and parent_tree is None:
                parent_tree = tree(args.source, parent)
            oid = commit_tree.get(path)
            side = "commit_state"
            if oid is None:
                oid = parent_tree.get(path)
                side = "pre_deletion_snapshot"
            if oid is None:
                continue
            data = git(args.source, "cat-file", "blob", oid)
            key = (path, oid)
            entry = versions.setdefault(key, {
                "source_path": path,
                "source_blob": oid,
                "source_sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "source_relation": None,
                "destination_same_path_blob": dest_tree.get(path),
                "destination_identical_blob_paths": sorted(dest_by_blob.get(oid, [])),
                "source_main_same_path_blob": main_tree.get(path),
                "introduced_or_deleted_by": [],
                "primary_branch_refs": [],
                "file_state": side,
            })
            entry["introduced_or_deleted_by"].append(commit)
            entry["primary_branch_refs"].append(row["primary_refname"])
            if oid in dest_blobs:
                relation = "exact_destination_content_copy"
            elif oid in main_blobs:
                relation = "exact_source_main_content_copy"
            elif path in dest_tree:
                relation = "same_path_destination_conflict"
            elif path in main_tree:
                relation = "same_path_source_main_conflict"
            else:
                relation = "branch_only_content"
            entry["source_relation"] = relation

    out_rows = []
    for row in versions.values():
        row["introduced_or_deleted_by"] = sorted(set(row["introduced_or_deleted_by"]))
        row["primary_branch_refs"] = sorted(set(row["primary_branch_refs"]))
        if row["source_relation"] == "branch_only_content":
            row["disposition"] = "preserve_branch_only_mathematical_artifact"
        elif row["source_relation"] in ("same_path_destination_conflict", "same_path_source_main_conflict"):
            row["disposition"] = "preserve_as_historical_snapshot; retain_current_main_version"
        elif row["source_relation"] == "exact_destination_content_copy":
            row["disposition"] = "exact_destination_duplicate_verified_by_git_blob"
        else:
            row["disposition"] = "source_main_duplicate_verified_by_git_blob"
        out_rows.append(row)
    out_rows.sort(key=lambda r: (r["source_path"], r["source_blob"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in out_rows))
    summary = {
        "agent_3_unique_commit_count": len(commits),
        "changed_path_events_across_owned_commits": commit_changed_paths,
        "unique_mathematical_file_versions": len(out_rows),
        "source_relation_counts": {},
        "candidate_branch_only_versions": sum(r["source_relation"] == "branch_only_content" for r in out_rows),
        "destination_conflict_versions": sum(r["source_relation"] == "same_path_destination_conflict" for r in out_rows),
        "source_main_conflict_versions": sum(r["source_relation"] == "same_path_source_main_conflict" for r in out_rows),
        "exact_destination_versions": sum(r["source_relation"] == "exact_destination_content_copy" for r in out_rows),
        "exact_source_main_versions": sum(r["source_relation"] == "exact_source_main_content_copy" for r in out_rows),
    }
    from collections import Counter
    summary["source_relation_counts"] = dict(Counter(r["source_relation"] for r in out_rows))
    (args.output.parent / "source-branch-artifacts-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
