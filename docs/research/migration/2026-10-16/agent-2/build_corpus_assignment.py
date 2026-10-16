#!/usr/bin/env python3
"""Rebuild Agent 2's deterministic source-main corpus allocation.

The read-only audit directory is an input. This script verifies its pinned
source/destination identities, the source tree/hash rows, and all 813 frozen
Target C destinations before emitting the complete 4,717-row allocation.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import pathlib
import re
import subprocess
import sys


SOURCE_MAIN = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
DESTINATION_MAIN = "c6e0394b3152d21075328bf4f26e6c070229bf13"
FROZEN_COUNT = 813
START_TOTALS = [90, 75, 60]


def git(repo: str, *args: str, input_bytes: bytes | None = None) -> bytes:
    return subprocess.check_output(["git", "-C", repo, *args], input=input_bytes)


def tree(repo: str, rev: str) -> dict[str, str]:
    raw = git(repo, "ls-tree", "-r", "-z", rev)
    result: dict[str, str] = {}
    for row in raw.split(b"\0"):
        if not row:
            continue
        metadata, raw_path = row.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        if kind == "blob":
            result[raw_path.decode("utf-8", "surrogateescape")] = oid
    return result


def hashes_for_blobs(repo: str, oids: list[str]) -> dict[str, tuple[int, str]]:
    """Return (byte length, SHA256) for unique Git blob IDs using one process."""
    unique = list(dict.fromkeys(oids))
    proc = subprocess.Popen(
        ["git", "-C", repo, "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    assert proc.stdin is not None and proc.stdout is not None
    result: dict[str, tuple[int, str]] = {}
    try:
        for oid in unique:
            proc.stdin.write((oid + "\n").encode("ascii"))
            proc.stdin.flush()
            header = proc.stdout.readline().decode("ascii").strip().split()
            if len(header) != 3 or header[1] != "blob":
                raise RuntimeError(f"unexpected cat-file response for {oid}: {header}")
            size = int(header[2])
            data = proc.stdout.read(size)
            if len(data) != size or proc.stdout.read(1) != b"\n":
                raise RuntimeError(f"truncated cat-file response for {oid}")
            result[oid] = (size, hashlib.sha256(data).hexdigest())
    finally:
        proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("git cat-file --batch failed")
    return result


def read_jsonl(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def unit_key(path: str) -> tuple[str, str]:
    basename = pathlib.PurePosixPath(path).name
    suffix = pathlib.PurePosixPath(basename).suffix
    stem = basename[: -len(suffix)] if suffix else basename
    if stem.startswith("verify_"):
        stem = stem[len("verify_") :]
    if re.match(r"^(target_a|target_b|target_c|global)_", stem):
        stem = re.sub(r"(?<!\d)(20\d{2})[-_](\d{2})[-_](\d{2})(?!\d)", r"\1_\2_\3", stem)
        return stem, "normalized_family_basename"
    return path, "full_path"


def third_party_exclusion(path: str) -> bool:
    return path.startswith("extracted/") or (
        path.startswith("papers/") and path.lower().endswith(".pdf")
    )


def work_type(row: dict) -> str:
    path = row["source_path"]
    suffix = pathlib.PurePosixPath(path).suffix.lower()
    if third_party_exclusion(path):
        return "third_party_exclusion_review"
    if suffix in (".py", ".cpp") and pathlib.PurePosixPath(path).name.lower().startswith("verify_"):
        return "verifier"
    if suffix == ".md" and (
        path.startswith(("research/", "docs/reports/", "docs/audits/", "docs/targets/", "docs/canonical/"))
        or row.get("source_target")
        or re.match(r"^(target_a|target_b|target_c|global)_", pathlib.PurePosixPath(path).name)
    ):
        return "proof_or_research_markdown"
    return "other"


def file_cost(row: dict) -> int:
    path = row["source_path"]
    size = int(row["source_bytes"])
    kind = work_type(row)
    if kind == "third_party_exclusion_review":
        return 1
    if kind == "verifier":
        base = 3 + min(12, math.ceil(size / 8000))
    elif kind == "proof_or_research_markdown":
        base = 3 + min(12, math.ceil(size / 10000))
    else:
        base = 1 + min(12, math.ceil(size / 20000))
    if row["destination_relation"] == "same_path_different_content":
        base += 3
    return base


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-dir", type=pathlib.Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--frozen-ledger", type=pathlib.Path, required=True)
    args = parser.parse_args()

    source_head = git(args.source, "rev-parse", SOURCE_MAIN + "^{commit}").decode().strip()
    destination_head = git(args.destination, "rev-parse", DESTINATION_MAIN + "^{commit}").decode().strip()
    if source_head != SOURCE_MAIN or destination_head != DESTINATION_MAIN:
        raise SystemExit(f"pinned ref mismatch: source={source_head}, destination={destination_head}")

    coverage_path = args.audit_dir / "source-main-4717-coverage.jsonl"
    input_rows = read_jsonl(coverage_path)
    if len(input_rows) != 4717:
        raise SystemExit(f"expected 4717 audit rows, got {len(input_rows)}")
    source_tree = tree(args.source, SOURCE_MAIN)
    destination_tree = tree(args.destination, DESTINATION_MAIN)
    if len(source_tree) != 4717:
        raise SystemExit(f"expected 4717 source blobs, got {len(source_tree)}")

    frozen = read_jsonl(args.frozen_ledger)
    if len(frozen) != FROZEN_COUNT:
        raise SystemExit(f"expected {FROZEN_COUNT} frozen dispositions, got {len(frozen)}")
    frozen_by_path = {r["source"]["path"]: r for r in frozen}
    if len(frozen_by_path) != FROZEN_COUNT:
        raise SystemExit("frozen source paths are not unique")

    source_oids = [source_tree[row["source_path"]] for row in input_rows]
    source_hashes = hashes_for_blobs(args.source, source_oids)
    dest_oids = list(destination_tree.values())
    dest_hashes = hashes_for_blobs(args.destination, dest_oids)
    dest_blob_paths: dict[str, list[str]] = collections.defaultdict(list)
    for path, oid in destination_tree.items():
        dest_blob_paths[oid].append(path)

    source_exact = 0
    same_path_exact = 0
    alternate_exact = 0
    frozen_overlap = 0
    records: list[dict] = []
    candidates: list[dict] = []
    for row in input_rows:
        path = row["source_path"]
        source_oid = source_tree.get(path)
        if not source_oid or source_oid != row["source_git_blob_sha1"]:
            raise SystemExit(f"source blob mismatch at {path}")
        size, digest = source_hashes[source_oid]
        if digest != row["source_sha256"] or size != int(row["source_bytes"]):
            raise SystemExit(f"source bytes mismatch at {path}")

        actual_dest_oid = destination_tree.get(path)
        actual_alt = [p for p in dest_blob_paths.get(source_oid, []) if p != path]
        if actual_dest_oid == source_oid:
            relation = "same_path_identical"
        elif actual_dest_oid is not None:
            relation = "same_path_different_content"
        elif actual_alt:
            relation = "path_absent_identical_blob_elsewhere"
        else:
            relation = "path_absent_no_exact_blob"
        if relation != row["destination_relation"]:
            raise SystemExit(f"destination relation mismatch for {path}: {relation} != {row['destination_relation']}")
        if relation == "same_path_identical":
            same_path_exact += 1
        elif relation == "path_absent_identical_blob_elsewhere":
            alternate_exact += 1

        frozen_row = frozen_by_path.get(path)
        is_frozen = frozen_row is not None and frozen_row["source"]["sha256"] == digest
        if is_frozen:
            frozen_overlap += relation == "same_path_identical"
            d = frozen_row["destination"]
            dpath = d["path"]
            doid = destination_tree.get(dpath)
            if doid != d["final_git_blob_sha1"]:
                raise SystemExit(f"frozen destination blob mismatch at {dpath}")
            if dest_hashes[doid][1] != d["final_sha256"]:
                raise SystemExit(f"frozen destination SHA256 mismatch at {dpath}")

        if relation == "same_path_identical" or relation == "path_absent_identical_blob_elsewhere":
            exclusion = "exact_content_match"
        elif is_frozen:
            exclusion = "verified_frozen_target_c_disposition"
        else:
            exclusion = None
            candidates.append(row)

        key, key_type = unit_key(path)
        rec = {
            "source_path": path,
            "source_mode": row["source_mode"],
            "source_git_blob_sha1": source_oid,
            "source_sha256": digest,
            "source_bytes": size,
            "source_target": row.get("source_target"),
            "source_lifecycle": row.get("source_lifecycle"),
            "source_canonical_flag": row.get("canonical_flag"),
            "source_claim_ids": row.get("claim_ids", []),
            "source_depends_on": row.get("depends_on", []),
            "destination_relation": relation,
            "destination_same_path_sha256": row.get("destination_same_path_sha256"),
            "destination_identical_blob_paths_elsewhere": actual_alt,
            "verified_frozen_target_c": bool(is_frozen),
            "exclusion_reason": exclusion,
            "unit_key": key,
            "unit_key_type": key_type,
            "file_work_type": work_type(row),
            "file_cost": None if exclusion else file_cost(row),
            "assigned_agent": None,
            "unit_cost": None,
            "unit_order": None,
        }
        records.append(rec)

    units: dict[tuple[str, str], list[dict]] = collections.defaultdict(list)
    record_by_path = {r["source_path"]: r for r in records}
    for row in candidates:
        key = unit_key(row["source_path"])
        units[key].append(row)
    ordered_units = []
    for (key, key_type), rows in units.items():
        cost = sum(file_cost(row) for row in rows)
        ordered_units.append((key, key_type, cost, rows))
    ordered_units.sort(key=lambda u: (-u[2], u[0], u[1]))

    totals = START_TOTALS.copy()
    assigned_units = collections.Counter()
    assigned_files = collections.Counter()
    assigned_cost = collections.Counter()
    for order, (key, key_type, cost, rows) in enumerate(ordered_units, start=1):
        agent = min(range(3), key=lambda i: (totals[i], i)) + 1
        before = totals[agent - 1]
        totals[agent - 1] += cost
        assigned_units[agent] += 1
        assigned_files[agent] += len(rows)
        assigned_cost[agent] += cost
        for row in rows:
            rec = record_by_path[row["source_path"]]
            rec.update(
                assigned_agent=agent,
                unit_cost=cost,
                unit_order=order,
                unit_total_before=before,
                unit_total_after=totals[agent - 1],
            )

    # The candidate count is the outstanding source-main obligation set.
    exact_count = same_path_exact + alternate_exact
    frozen_only = FROZEN_COUNT - frozen_overlap
    if len(candidates) != 3049 or exact_count != 1465 or frozen_only != 203:
        raise SystemExit(
            f"unexpected partition: candidates={len(candidates)}, exact={exact_count}, frozen_only={frozen_only}"
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    assignment_path = args.output_dir / "corpus-assignment.jsonl"
    with assignment_path.open("w") as stream:
        for rec in records:
            stream.write(json.dumps(rec, sort_keys=True, separators=(",", ":")) + "\n")

    input_sha = hashlib.sha256(coverage_path.read_bytes()).hexdigest()
    frozen_sha = hashlib.sha256(args.frozen_ledger.read_bytes()).hexdigest()
    totals_sum = sum(totals)
    spread_percent = 100 * (max(totals) - min(totals)) / (totals_sum / 3)
    summary = {
        "schema_version": 1,
        "source_main": SOURCE_MAIN,
        "destination_main": DESTINATION_MAIN,
        "source_main_tracked_files": len(source_tree),
        "source_main_coverage_input": str(coverage_path),
        "source_main_coverage_input_sha256": input_sha,
        "frozen_target_c_dispositions": FROZEN_COUNT,
        "frozen_disposition_input_sha256": frozen_sha,
        "same_path_exact_matches": same_path_exact,
        "exact_content_matches_elsewhere": alternate_exact,
        "frozen_dispositions_overlapping_same_path_exact": frozen_overlap,
        "frozen_dispositions_remaining_after_exact_matches": frozen_only,
        "outstanding_source_main_files": len(candidates),
        "outstanding_units": len(ordered_units),
        "starting_agent_totals": START_TOTALS,
        "assigned_files": {str(k): assigned_files[k] for k in (1, 2, 3)},
        "assigned_units": {str(k): assigned_units[k] for k in (1, 2, 3)},
        "assigned_cost": {str(k): assigned_cost[k] for k in (1, 2, 3)},
        "final_agent_totals": totals,
        "workload_spread_score": max(totals) - min(totals),
        "workload_spread_percent_of_mean": spread_percent,
        "agent_2_owned_files": assigned_files[2],
        "agent_2_owned_units": assigned_units[2],
        "agent_2_workload_score": assigned_cost[2],
        "corpus_assignment_sha256": hashlib.sha256(assignment_path.read_bytes()).hexdigest(),
    }
    (args.output_dir / "corpus-assignment-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
