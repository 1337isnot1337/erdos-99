#!/usr/bin/env python3
"""Verify the frozen Target C shard selection and imported byte provenance."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

SOURCE_COMMIT = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
DESTINATION_BASELINE = "358af8253f85ab7b9cdbf976ce186ee8426718e4"
FIRST_PATH = "docs/reports/target_c_nearzero_diameter_geodesic_strip_2026-09-09.md"
LAST_PATH = "docs/reports/target_c_singleton_star_response_stress_2026-09-09.md"
SHARD_START = 489
SHARD_END = 650
EXPECTED_MISSING = 813
ROOT = Path(__file__).resolve().parent


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    source = args.source_repo.resolve()
    destination = args.destination.resolve()
    errors: list[str] = []

    try:
        source_index = jsonl_from_bytes(
            git(source, "show", f"{SOURCE_COMMIT}:docs/state/artifact-index.jsonl")
        )
        base_paths = set(
            git(destination, "ls-tree", "-r", "--name-only", DESTINATION_BASELINE)
            .decode()
            .splitlines()
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"FAIL: unable to read frozen source/destination inputs: {exc}")
        return 1

    missing = sorted(
        (
            row
            for row in source_index
            if row.get("target") == "target-c" and row.get("path") not in base_paths
        ),
        key=lambda row: row["path"],
    )
    if len(missing) != EXPECTED_MISSING:
        errors.append(f"expected {EXPECTED_MISSING} missing Target C entries, found {len(missing)}")
    if len(missing) <= SHARD_END:
        errors.append("frozen missing list does not contain the assigned final index")
        assigned = []
    else:
        assigned = missing[SHARD_START : SHARD_END + 1]
    if len(assigned) != SHARD_END - SHARD_START + 1:
        errors.append(f"expected 162 assigned entries, found {len(assigned)}")
    if assigned and assigned[0]["path"] != FIRST_PATH:
        errors.append(f"wrong first assigned path: {assigned[0]['path']}")
    if assigned and assigned[-1]["path"] != LAST_PATH:
        errors.append(f"wrong last assigned path: {assigned[-1]['path']}")

    rows = jsonl(ROOT / "dispositions.jsonl")
    by_index: dict[int, dict] = {}
    for row in rows:
        index = row.get("frozen_missing_index_zero_based")
        if index in by_index:
            errors.append(f"duplicate disposition index {index}")
        by_index[index] = row
    if len(rows) > len(assigned):
        errors.append(f"disposition ledger has {len(rows)} rows, over assigned count {len(assigned)}")
    if args.require_complete and len(rows) != len(assigned):
        errors.append(f"complete ledger required: found {len(rows)} of {len(assigned)} rows")

    for position, row in enumerate(assigned, SHARD_START):
        ledger = by_index.get(position)
        if ledger is None:
            if args.require_complete:
                errors.append(f"missing disposition for frozen index {position}")
            continue
        path = row["path"]
        if ledger.get("source_path") != path:
            errors.append(f"index {position} path mismatch: {ledger.get('source_path')} != {path}")
        if ledger.get("source_commit") != SOURCE_COMMIT:
            errors.append(f"index {position} has wrong source commit")
        if ledger.get("destination_baseline") != DESTINATION_BASELINE:
            errors.append(f"index {position} has wrong destination baseline")
        if path in base_paths:
            errors.append(f"assigned path was already tracked at frozen destination baseline: {path}")
        try:
            blob = git(source, "rev-parse", f"{SOURCE_COMMIT}:{path}").decode().strip()
            source_bytes = git(source, "cat-file", "blob", blob)
        except subprocess.CalledProcessError:
            errors.append(f"missing source blob for {path}")
            continue
        if blob != ledger.get("source_git_blob_sha"):
            errors.append(f"source Git blob mismatch for {path}")
        if sha(source_bytes) != ledger.get("source_sha256"):
            errors.append(f"source SHA-256 mismatch for {path}")
        imported = destination / ledger.get("destination_path", "")
        if not imported.is_file():
            errors.append(f"destination import missing: {ledger.get('destination_path')}")
        elif sha(imported.read_bytes()) != ledger.get("destination_sha256"):
            errors.append(f"destination SHA-256 mismatch for {path}")
        if ledger.get("destination_canonical") is not False:
            errors.append(f"noncanonical flag absent for {path}")
        if ledger.get("destination_lifecycle") != "unreviewed_noncanonical":
            errors.append(f"unexpected destination lifecycle for {path}")
        if not ledger.get("disposition") or not ledger.get("mathematical_summary"):
            errors.append(f"missing justified disposition/summary for {path}")

    for row in jsonl(ROOT / "evidence.jsonl"):
        path = row["source_path"]
        try:
            blob = git(source, "rev-parse", f"{SOURCE_COMMIT}:{path}").decode().strip()
            data = git(source, "cat-file", "blob", blob)
        except subprocess.CalledProcessError:
            errors.append(f"missing supporting evidence source blob: {path}")
            continue
        if blob != row.get("source_git_blob_sha") or sha(data) != row.get("source_sha256"):
            errors.append(f"supporting evidence source pin mismatch: {path}")
        imported = destination / row.get("destination_path", "")
        if not imported.is_file() or sha(imported.read_bytes()) != row.get("destination_sha256"):
            errors.append(f"supporting evidence destination pin mismatch: {path}")

    topics = json.loads((ROOT / "topic-map.json").read_text())
    covered = {i for topic in topics.get("topics", []) for i in topic.get("indices", [])}
    if covered != set(by_index):
        errors.append("topic map indexes do not match disposition ledger indexes")
    if topics.get("source_commit") != SOURCE_COMMIT:
        errors.append("topic map has wrong source commit")
    if topics.get("destination_baseline") != DESTINATION_BASELINE:
        errors.append("topic map has wrong destination baseline")

    result = {
        "status": "PASS" if not errors else "FAIL",
        "source_commit": SOURCE_COMMIT,
        "destination_baseline": DESTINATION_BASELINE,
        "frozen_missing_target_c_count": len(missing),
        "assigned_count": len(assigned),
        "disposition_count": len(rows),
        "supporting_evidence_count": len(jsonl(ROOT / "evidence.jsonl")),
        "complete": len(rows) == len(assigned),
        "claim": "selection and source/destination hash provenance only; no mathematical correctness inferred",
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


def jsonl_from_bytes(data: bytes) -> list[dict]:
    return [json.loads(line) for line in data.decode().splitlines() if line.strip()]


if __name__ == "__main__":
    raise SystemExit(main())
