#!/usr/bin/env python3
"""Preserve the Agent 3 owned frozen dirty-worktree snapshot with provenance."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def normalized_markdown(data: bytes) -> bytes:
    lines = data.splitlines(keepends=True)
    while lines and lines[0].startswith((b"<!-- theorem-state:", b"<!-- migration-provenance:")):
        lines.pop(0)
    return b"".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--allocation", type=Path, required=True)
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--destination-main", required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--materialize", action="store_true")
    args = ap.parse_args()
    args.destination = args.destination.resolve()
    args.allocation = args.allocation.resolve()
    args.output = args.output.resolve()

    dest_tree = {}
    for entry in git(args.destination, "ls-tree", "-rz", "--full-tree", args.destination_main).split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        _mode, kind, oid = meta.decode("ascii").split()
        if kind == "blob":
            dest_tree[path.decode("utf-8", "surrogateescape")] = oid
    rows = [json.loads(line) for line in args.allocation.read_text().splitlines() if line.strip()]
    out = []
    copied = []
    readme_patch_rows = []
    for row in rows:
        record = {**row, "destination_baseline": args.destination_main,
                  "destination_path": None, "destination_sha256": None,
                  "destination_git_blob_sha1": None, "source_body_sha256": None,
                  "destination_body_sha256": None, "transformations": []}
        if row.get("owner") != 3:
            record["migration_disposition"] = row.get("disposition")
            record["migration_reason"] = "Outside Agent 3 dirty-worktree allocation; retained in the complete allocation ledger for the owning shard."
            out.append(record)
            continue
        if not row.get("currently_accessible") or not row.get("current_matches_frozen_snapshot"):
            record["migration_disposition"] = "unresolved_agent3_dirty_snapshot"
            record["migration_reason"] = "Agent 3 owns this frozen dirty-worktree path, but the worktree is inaccessible or current bytes cannot be matched to the frozen snapshot. Source worktree remains untouched."
            out.append(record)
            continue

        source = Path(row["worktree"]) / row["path"]
        data = source.read_bytes()
        actual_sha = sha(data)
        if actual_sha != row.get("local_sha256") or actual_sha != row.get("current_observed_sha256"):
            raise RuntimeError(f"frozen snapshot hash mismatch: {source}")
        record["source_sha256"] = actual_sha
        record["source_bytes"] = len(data)
        record["source_path"] = row["path"]
        record["source_worktree_head"] = row.get("head")
        record["source_repository"] = "https://github.com/1337isnot1337/e-99"

        if row["path"] == "research/README.md":
            diff = git(Path(row["worktree"]), "diff", "--no-ext-diff", "--unified=3", "HEAD", "--", row["path"])
            patch_path = args.output.parent / "dirty-shared-readme.patch"
            if args.materialize:
                patch_path.write_bytes(diff)
            record["migration_disposition"] = "exclude_shared_navigation_save_diff"
            record["reason"] = "Shared navigation edits are not applied; the exact worktree diff and its SHA-256 are retained as evidence."
            record["source_change_diff_sha256"] = sha(diff)
            record["source_change_diff_bytes"] = len(diff)
            record["destination_path"] = str(patch_path.relative_to(args.destination))
            record["destination_sha256"] = sha(diff)
            record["destination_bytes"] = len(diff)
            record["destination_git_blob_sha1"] = hashlib.sha1(b"blob " + str(len(diff)).encode() + b"\0" + diff).hexdigest()
            readme_patch_rows.append(record)
            out.append(record)
            continue

        source_path = row["path"]
        relation = row.get("relation_to_destination_main")
        if source_path.endswith("hybrid_clique_matching.json") and relation == "absent":
            target = source_path
            record["migration_disposition"] = "preserve_new_first_party_certificate_fixture"
            record["reason"] = "New exact finite matching certificate used by the assigned global palette research; copied byte-for-byte."
            content = data
            record["source_body_sha256"] = actual_sha
            record["destination_body_sha256"] = actual_sha
        else:
            commit_tag = actual_sha[:12]
            owner_ref = row.get("ownership_refname", "unmapped").removeprefix("refs/heads/").replace("/", "_")
            target = f"docs/archive/source-e99-dirty-worktrees/{owner_ref}/{commit_tag}/{source_path}.source"
            content_body = normalized_markdown(data) if source_path.lower().endswith(".md") else data
            record["source_body_sha256"] = sha(content_body)
            if source_path.lower().endswith(".md") and data.startswith(b"<!-- theorem-state:"):
                record["source_theorem_state_header"] = data.splitlines(keepends=True)[0].decode("utf-8", "replace").rstrip("\r\n")
            record["migration_disposition"] = "preserve_historical_dirty_snapshot"
            record["reason"] = "The dirty source worktree version conflicts with destination main; the current destination remains authoritative and the full source content is retained as a historical unreviewed snapshot."
            marker = {"source_repository": "https://github.com/1337isnot1337/e-99",
                      "source_worktree_head": row.get("head"), "source_path": source_path,
                      "source_sha256": actual_sha, "source_lifecycle": "dirty uncommitted worktree snapshot",
                      "destination_status": "historical_unreviewed_noncanonical"}
            notice = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n"
                      "> **Historical dirty-worktree snapshot; destination version retained.** " + record["reason"] + "\n\n")
            content = notice.encode() + content_body if source_path.lower().endswith(".md") else data
            record["transformations"].append("added_historical_dirty_snapshot_provenance_notice" if source_path.lower().endswith(".md") else "archived_source_bytes_without_modification")

        record["destination_path"] = target
        record["destination_sha256"] = sha(content)
        record["destination_bytes"] = len(content)
        record["destination_body_sha256"] = record.get("destination_body_sha256") or record["source_body_sha256"]
        record["destination_git_blob_sha1"] = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        if args.materialize:
            target_path = args.destination / target
            target_path.parent.mkdir(parents=True, exist_ok=True)
            if target_path.exists():
                if target_path.read_bytes() != content:
                    raise RuntimeError(f"refusing to overwrite nonidentical existing path {target}")
            else:
                target_path.write_bytes(content)
        copied.append(record)
        out.append(record)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(record, sort_keys=True) + "\n" for record in out))
    summary = {"frozen_dirty_path_count": len(rows),
               "agent3_owned_dirty_path_count": sum(r.get("owner") == 3 for r in rows),
               "materialized_file_count": len(copied),
               "materialized_bytes": sum(r.get("destination_bytes", 0) for r in copied),
               "disposition_counts": dict(Counter(r.get("migration_disposition") for r in out))}
    (args.output.parent / "dirty-disposition-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
