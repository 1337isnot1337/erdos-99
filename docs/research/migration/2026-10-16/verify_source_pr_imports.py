#!/usr/bin/env python3
"""Verify a frozen source open or merged-PR file ledger against Git and destination bytes."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


LEDGER = Path(__file__).with_name("ledger") / "source-pr-files.jsonl"


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--pr", type=int, required=True)
    args = parser.parse_args()
    source = args.source_repo.resolve()
    destination = args.destination.resolve()

    records = [
        json.loads(line)
        for line in LEDGER.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    selected = [r for r in records if r.get("record_type") in {"source_open_pr_file", "source_merged_pr_file"} and r.get("source_pr") == args.pr]
    if not selected:
        print(f"ERROR: no source open-PR ledger rows for PR #{args.pr}", file=sys.stderr)
        return 1

    heads = {r.get("source_head_sha") for r in selected}
    trees = {r.get("source_head_tree") for r in selected}
    if len(heads) != 1 or len(trees) != 1:
        print("ERROR: selected rows do not share one frozen PR head and tree", file=sys.stderr)
        return 1
    head, expected_tree = next(iter(heads)), next(iter(trees))
    actual_tree = git(source, "rev-parse", f"{head}^{{tree}}").decode().strip()
    if actual_tree != expected_tree:
        print(f"ERROR: frozen PR tree mismatch: expected {expected_tree}, got {actual_tree}", file=sys.stderr)
        return 1

    exact = transformed = blocked = 0
    errors: list[str] = []
    seen: set[str] = set()
    for row in selected:
        path = row.get("original_path")
        if not path or path in seen:
            errors.append(f"missing or duplicate source path: {path!r}")
            continue
        seen.add(path)
        commit = row.get("source_commit") or head
        try:
            source_bytes = git(source, "cat-file", "blob", f"{commit}:{path}")
        except subprocess.CalledProcessError:
            errors.append(f"source blob is unavailable: {commit}:{path}")
            continue
        source_blob = git(source, "rev-parse", f"{commit}:{path}").decode().strip()
        source_sha = hashlib.sha256(source_bytes).hexdigest()
        if source_blob != row.get("source_git_blob_sha"):
            errors.append(f"source Git blob mismatch: {path}")
        if source_sha != row.get("source_sha256") or len(source_bytes) != row.get("source_bytes"):
            errors.append(f"source SHA-256 or byte-count mismatch: {path}")

        disposition = str(row.get("disposition", ""))
        relation = str(row.get("destination_relation", ""))
        destination_path = row.get("destination_path")
        if "blocked" in disposition or not destination_path:
            blocked += 1
            continue
        target = destination / destination_path
        if not target.is_file():
            errors.append(f"destination file is missing: {destination_path}")
            continue
        dest_bytes = target.read_bytes()
        dest_sha = hashlib.sha256(dest_bytes).hexdigest()
        dest_blob = git(destination, "hash-object", "--", str(target)).decode().strip()
        if dest_sha != row.get("destination_sha256"):
            errors.append(f"destination SHA-256 mismatch: {destination_path}")
        recorded_blob = row.get("destination_git_blob_sha")
        if recorded_blob and dest_blob != recorded_blob:
            errors.append(f"destination Git blob mismatch: {destination_path}")
        if relation in {"exact_copy", "exact_duplicate"}:
            if source_bytes != dest_bytes:
                errors.append(f"exact-copy bytes differ: {path}")
            exact += 1
        else:
            if not row.get("transformation"):
                errors.append(f"transformed mapping has no transformation record: {path}")
            transformed += 1

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps({
        "status": "PASS",
        "source_pr": args.pr,
        "source_head": head,
        "source_tree": actual_tree,
        "source_paths_checked": len(selected),
        "record_types": sorted({r.get("record_type") for r in selected}),
        "exact_copies": exact,
        "transformed_or_regenerated": transformed,
        "rights_or_scope_blocked": blocked,
        "claim": "source identity and recorded destination-byte integrity only; no mathematical correctness inferred"
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
