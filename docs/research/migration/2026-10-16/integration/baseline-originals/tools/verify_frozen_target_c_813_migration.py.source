#!/usr/bin/env python3
"""Verify exact identities and dispositions for the frozen 813-report Target C corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import re
from collections import Counter
from pathlib import Path

SOURCE_COMMIT = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
SOURCE_TREE = "e061f039eac44c286a00eacdcaa9a4cbbb877891"
DESTINATION_BASELINE = "358af8253f85ab7b9cdbf976ce186ee8426718e4"
PRE_COORDINATOR_TREE = "0ac22c4709f00afdbc5a84d0eb30810e953d2305"
MIGRATION = Path("docs/research/migration/2026-10-16")
SUPPORT_PATHS = (
    "research/diameter_endpoint_gap_audit.py",
    "research/target_c_dominant_pentagon_through_splicing_2026-09-15.md",
    "research/target_c_efaq_uniform_cap.py",
    "research/target_c_open_cell_phase_flux_2026-10-03.md",
    "research/target_c_s1_q13_shell_regression.py",
    "research/target_c_two_halfdisk_scalar_regression_2026-09-12.md",
    "research/verify_aligned_swap_horn_obstructions.py",
    "research/verify_antipode_transition.py",
    "research/verify_convex_shared_witness_outer_occurrences.py",
    "research/verify_diameter_first_joint_depth_2026_10_02.py",
    "research/verify_diameter_star_contiguity.py",
    "research/verify_s1_q13_kkt_endpoints.py",
    "research/verify_target_c_annular_atlas_2026_09_26.py",
    "research/verify_target_c_antitone_interval_scc_2026_10_03.py",
    "research/verify_target_c_ball_hull_lattice_2026_10_02.py",
    "research/verify_target_c_central_face_two_geodesic_corridor.py",
    "research/verify_target_c_collinear_punctures_2026_10_02.py",
    "research/verify_target_c_deep_isolate_octagon_flip_2026_10_02.py",
    "research/verify_target_c_dominant_pentagon_through_splicing.py",
    "research/verify_target_c_star_ray_staircase_2026_10_01.py",
    "research/verify_target_c_two_halfdisk_scalar_regression.py",
)


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def source_blob_exists(repo: Path, commit: str, path: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(repo), "cat-file", "-e", f"{commit}:{path}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, help="Optional frozen source clone for raw source-byte replay")
    parser.add_argument("--destination", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    source = args.source_repo.resolve() if args.source_repo else None
    destination = args.destination.resolve()
    errors: list[str] = []
    counts: Counter[str] = Counter()

    source_tree = SOURCE_TREE
    if source is not None:
        source_tree = git(source, "rev-parse", f"{SOURCE_COMMIT}^{{tree}}").decode().strip()
        if source_tree != SOURCE_TREE:
            errors.append(f"frozen source tree mismatch: {source_tree}")
    frozen = read_jsonl(destination / MIGRATION / "shards/frozen-813-index.jsonl")
    ledger = read_jsonl(destination / MIGRATION / "frozen-target-c-813-dispositions.jsonl")
    if len(frozen) != 813:
        errors.append(f"frozen index has {len(frozen)} rows, expected 813")
    if len(ledger) != 813:
        errors.append(f"disposition ledger has {len(ledger)} rows, expected 813")

    frozen_by_index = {row.get("frozen_index"): row for row in frozen}
    ledger_by_index = {row.get("frozen_index"): row for row in ledger}
    if set(frozen_by_index) != set(range(813)):
        errors.append("frozen indexes are not the exact range 0–812")
    if set(ledger_by_index) != set(range(813)):
        errors.append("disposition indexes are not the exact range 0–812")
    if len({row.get("path") for row in frozen}) != 813:
        errors.append("duplicate source path in frozen 813 index")
    rights = read_jsonl(destination / MIGRATION / "ledger/coordinator-first-party-rights-addendum.jsonl")
    rights_by_path: dict[str, dict] = {}
    for row in rights:
        path = row.get("original_path")
        if path in rights_by_path:
            errors.append(f"duplicate rights record: {path}")
        rights_by_path[path] = row
    expected_rights_paths = {row.get("path") for row in frozen} | set(SUPPORT_PATHS)
    if len(rights) != 834:
        errors.append(f"additive rights ledger has {len(rights)} rows, expected 834")
    if set(rights_by_path) != expected_rights_paths:
        errors.append(
            "additive rights ledger paths differ from the frozen 813 reports plus 21 supporting files: "
            f"missing={len(expected_rights_paths - set(rights_by_path))}, "
            f"extra={len(set(rights_by_path) - expected_rights_paths)}"
        )

    base_state = git(destination, "show", f"{DESTINATION_BASELINE}:docs/state/theorem-state.yaml")
    current_state = (destination / "docs/state/theorem-state.yaml").read_bytes()
    if sha256(base_state) != sha256(current_state):
        errors.append("destination theorem-state differs from frozen baseline")
    base_inclusion = git(destination, "show", f"{DESTINATION_BASELINE}:docs/publication/inclusion.json")
    current_inclusion = (destination / "docs/publication/inclusion.json").read_bytes()
    if sha256(base_inclusion) != sha256(current_inclusion):
        errors.append("owner-attested inclusion manifest differs from frozen baseline")
    current_page = (destination / "docs/targets/target-c/CURRENT.md").read_text(encoding="utf-8")
    if "q=O(D^(4/5))" not in current_page or "withdrawn" not in current_page.lower():
        errors.append("withdrawn inverse-phase rate/chart warning is missing from current Target C page")

    for index in range(813):
        frozen_row = frozen_by_index.get(index)
        row = ledger_by_index.get(index)
        if frozen_row is None or row is None:
            continue
        source_record = row.get("source", {})
        dest_record = row.get("destination", {})
        path = frozen_row.get("path")
        if source_record.get("path") != path:
            errors.append(f"source path differs from frozen row {index}: {path}")
        if source_record.get("commit") != SOURCE_COMMIT or source_record.get("tree") != SOURCE_TREE:
            errors.append(f"source pin differs at index {index}: {path}")
        if source_record.get("git_blob_sha1") != frozen_row.get("source_git_blob_sha"):
            errors.append(f"source blob identity differs at index {index}: {path}")
        if source_record.get("sha256") != frozen_row.get("source_sha256"):
            errors.append(f"source SHA-256 pin differs from frozen index at index {index}: {path}")
        source_bytes = None
        if source is not None:
            try:
                source_bytes = git(source, "cat-file", "blob", f"{SOURCE_COMMIT}:{path}")
                source_mode_line = git(source, "ls-tree", SOURCE_COMMIT, "--", path).decode("ascii").split()
                source_mode = source_mode_line[0]
            except subprocess.CalledProcessError:
                errors.append(f"source path missing from frozen commit: {path}")
                continue
            if sha256(source_bytes) != frozen_row.get("source_sha256") or sha256(source_bytes) != source_record.get("sha256"):
                errors.append(f"source SHA-256 mismatch at index {index}: {path}")
            if git_blob_sha(source_bytes) != frozen_row.get("source_git_blob_sha"):
                errors.append(f"source Git blob mismatch at index {index}: {path}")
            counts["source_blobs_checked"] += 1
        else:
            recorded_right = rights_by_path.get(path, {})
            source_mode = recorded_right.get("source_mode")
            if source_mode not in ("100644", "100755"):
                errors.append(f"recorded source mode is absent or invalid at index {index}: {path}")
        if source_record.get("canonical") is not False or source_record.get("lifecycle") != "unreviewed":
            errors.append(f"source lifecycle/canonical guard is wrong at index {index}: {path}")

        destination_path = dest_record.get("path")
        relation = dest_record.get("relation_to_source", "")
        relocated_archive = (
            destination_path != path
            and destination_path.startswith("docs/archive/source-e99-main-42f0296d/")
            and "archiv" in relation.lower()
            and dest_record.get("final_sha256") == source_record.get("sha256")
        )
        if destination_path != path and not relocated_archive:
            errors.append(f"undocumented destination relocation at index {index}: {path} -> {destination_path}")
        if not relation.strip():
            errors.append(f"missing source-to-destination relation at index {index}: {path}")
        if source_blob_exists(destination, DESTINATION_BASELINE, path):
            errors.append(f"path was already present at frozen destination baseline: {path}")
        target = destination / destination_path
        if not target.is_file():
            errors.append(f"destination file missing at index {index}: {destination_path}")
            continue
        data = target.read_bytes()
        actual_sha = sha256(data)
        actual_blob = git_blob_sha(data)
        if actual_sha != dest_record.get("final_sha256"):
            errors.append(f"final destination SHA-256 mismatch at index {index}: {destination_path}")
        if actual_sha != source_record.get("sha256") and not (
            dest_record.get("worker_transformations")
            or dest_record.get("coordinator_transformations")
            or dest_record.get("generated_header_updated")
        ):
            errors.append(f"source/destination content difference has no recorded transformation at index {index}: {path}")
        for transform in dest_record.get("worker_transformations", []) + dest_record.get("coordinator_transformations", []):
            details = transform if isinstance(transform, str) else transform.get("details", "")
            match = re.search(r"Replaced exactly (\d+) source byte sequence\(s\) 0x0c followed by \"rac\" with the LaTeX command bytes \\frac; all remaining source bytes are unchanged\.", details)
            if match:
                count = int(match.group(1))
                if source_bytes is not None:
                    replaced = source_bytes.count(b"\x0crac")
                    if replaced != count or source_bytes.replace(b"\x0crac", b"\\frac") != data:
                        errors.append(f"recorded LaTeX form-feed repair does not reproduce destination bytes at index {index}: {path}")
        if actual_blob != dest_record.get("final_git_blob_sha1"):
            errors.append(f"final destination Git blob mismatch at index {index}: {destination_path}")
        counts[dest_record.get("disposition", "missing-disposition")] += 1
        allowed_dispositions = {
            "integrated_as_noncanonical_research",
            "integrated_as_historical_superseded_research",
        }
        if dest_record.get("disposition") not in allowed_dispositions:
            errors.append(f"non-explicit or unexpected disposition at index {index}: {path}")

        permission = target.stat().st_mode
        destination_mode = "100755" if permission & 0o111 else "100644"
        if destination_mode != dest_record.get("final_mode"):
            errors.append(f"destination mode mismatch at index {index}: {destination_path}")
        right = rights_by_path.get(path)
        if right is None:
            errors.append(f"missing additive rights record at index {index}: {path}")
        else:
            if right.get("source_sha256") != source_record.get("sha256"):
                errors.append(f"rights/source hash mismatch at index {index}: {path}")
            if right.get("destination_sha256") != actual_sha or right.get("destination_path") != destination_path:
                errors.append(f"rights/destination hash mismatch at index {index}: {path}")
            transformation = right.get("transformation")
            if actual_sha != source_record.get("sha256") and transformation in (None, "none", "none; source and destination bytes are identical", []):
                errors.append(f"rights row omits a source-to-destination transformation at index {index}: {path}")
            if destination_path != path and not (
                isinstance(transformation, list) and any("archive" in item.lower() or "archived" in item.lower() for item in transformation if isinstance(item, str))
            ):
                errors.append(f"rights row omits the documented archive relocation at index {index}: {path}")
            if right.get("source_mode") != source_mode:
                errors.append(f"rights/source mode mismatch at index {index}: {path}")
            if right.get("destination_mode") != destination_mode:
                errors.append(f"rights/destination mode mismatch at index {index}: {path}")
            counts["rights_rows_checked"] += 1

        # Verify the independently recorded pre-coordinator tree hash. Worker rows
        # or the pre-coordinator central artifact index supplied the comparison.
        pre_path = dest_record.get("path")
        try:
            pre_bytes = git(destination, "show", f"{PRE_COORDINATOR_TREE}:{pre_path}")
            if sha256(pre_bytes) != dest_record.get("pre_coordinator_sha256"):
                errors.append(f"pre-coordinator destination hash mismatch at index {index}: {path}")
        except subprocess.CalledProcessError:
            errors.append(f"pre-coordinator destination path absent at index {index}: {path}")
        refs = dest_record.get("pre_coordinator_hash_matched_records", [])
        if not refs:
            errors.append(f"no worker/central comparison evidence at index {index}: {path}")
        else:
            matched_record = False
            worker_refs = row.get("provenance", {}).get("worker_records", [])
            for match in refs:
                record_kind = match.get("record")
                field = match.get("field")
                if record_kind == "worker":
                    for worker_ref in worker_refs:
                        worker_lines = (destination / worker_ref["path"]).read_text(encoding="utf-8").splitlines()
                        worker_row = json.loads(worker_lines[worker_ref["line"] - 1])
                        if worker_row.get(field) == dest_record.get("pre_coordinator_sha256"):
                            matched_record = True
                            break
                elif record_kind in ("central-artifact", "central-file"):
                    ledger_rel = (
                        MIGRATION / "ledger/source-main-artifacts.jsonl"
                        if record_kind == "central-artifact"
                        else MIGRATION / "ledger/source-main-files.jsonl"
                    ).as_posix()
                    pre_ledger = git(destination, "show", f"{PRE_COORDINATOR_TREE}:{ledger_rel}").decode("utf-8")
                    for line in pre_ledger.splitlines():
                        if not line.strip():
                            continue
                        pre_row = json.loads(line)
                        if pre_row.get("original_path") == path and pre_row.get(field) == dest_record.get("pre_coordinator_sha256"):
                            matched_record = True
                            break
                if matched_record:
                    break
            if not matched_record:
                errors.append(f"pre-coordinator hash has no matching worker/central row at index {index}: {path}")
        counts["pre_coordinator_tree_checks"] += 1

        for ref in row.get("provenance", {}).get("worker_records", []):
            worker_path = destination / ref["path"]
            lines = worker_path.read_text(encoding="utf-8").splitlines()
            line_no = ref["line"]
            if line_no < 1 or line_no > len(lines):
                errors.append(f"worker evidence row absent at index {index}: {ref}")
            else:
                try:
                    json.loads(lines[line_no - 1])
                except json.JSONDecodeError:
                    errors.append(f"worker evidence row is invalid JSON at index {index}: {ref}")
        counts["worker_records_checked"] += len(row.get("provenance", {}).get("worker_records", []))

    # The owner-authorized additive rows must not mutate the pinned 810-entry
    # inclusion manifest or imply that it includes these 813 paths.
    inclusion = json.loads((destination / "docs/publication/inclusion.json").read_text(encoding="utf-8"))
    inclusion_paths = {entry.get("source_path") for entry in inclusion.get("entries", []) if isinstance(entry, dict)}
    overlap = inclusion_paths & {row.get("path") for row in frozen}
    if overlap:
        errors.append(f"unexpected overlap between frozen 813 corpus and exact 810 inclusion manifest: {len(overlap)}")

    for path in SUPPORT_PATHS:
        right = rights_by_path.get(path)
        if right is None:
            errors.append(f"missing additive rights row for cross-shard support import: {path}")
            continue
        source_bytes = None
        if source is not None:
            try:
                source_bytes = git(source, "show", f"{SOURCE_COMMIT}:{path}")
            except subprocess.CalledProcessError:
                errors.append(f"support dependency absent from frozen source commit: {path}")
                continue
        destination_path = right.get("destination_path")
        target = destination / destination_path
        if not target.is_file():
            errors.append(f"support dependency absent from destination tree: {destination_path}")
            continue
        dest_bytes = target.read_bytes()
        source_mode = right.get("source_mode")
        if source is not None:
            source_mode = git(source, "ls-tree", SOURCE_COMMIT, "--", path).decode("ascii").split()[0]
        if source_bytes is not None and sha256(source_bytes) != right.get("source_sha256"):
            errors.append(f"support dependency source SHA-256 mismatch: {path}")
        if source_bytes is not None and git_blob_sha(source_bytes) != right.get("source_git_blob_sha"):
            errors.append(f"support dependency source Git blob mismatch: {path}")
        if sha256(dest_bytes) != right.get("destination_sha256"):
            errors.append(f"support dependency source/destination hash mismatch: {path}")
        if right.get("transformation") in ("none", "none; exact source bytes preserved") and git_blob_sha(dest_bytes) != right.get("source_git_blob_sha"):
            errors.append(f"untransformed support dependency differs from pinned source Git blob: {path}")
        if source_mode != right.get("source_mode"):
            errors.append(f"support dependency source mode mismatch: {path}")
        permission = target.stat().st_mode
        destination_mode = "100755" if permission & 0o111 else "100644"
        if destination_mode != right.get("destination_mode"):
            errors.append(f"support dependency destination mode mismatch: {path}")
        if source_bytes is not None:
            counts["support_source_blobs_checked"] += 1
        counts["support_files_checked"] += 1

    destination_head = git(destination, "rev-parse", "HEAD").decode().strip()
    destination_tree = git(destination, "rev-parse", "HEAD^{tree}").decode().strip()
    result = {
        "status": "PASS" if not errors else "FAIL",
        "destination_git_head": destination_head,
        "destination_head_tree": destination_tree,
        "source_main": SOURCE_COMMIT,
        "source_tree": source_tree,
        "source_clone_replay": source is not None,
        "destination_assignment_baseline": DESTINATION_BASELINE,
        "pre_coordinator_destination_tree": PRE_COORDINATOR_TREE,
        "counts": {"frozen_paths": len(frozen), "disposition_rows": len(ledger), **dict(counts)},
        "dispositions": dict(counts),
        "errors": errors,
        "scope_note": "Always verifies frozen source pins as recorded, destination hashes/modes, worker evidence pointers, additive rights rows, unchanged theorem-state and inverse-phase warning. When --source-repo is supplied, also verifies each raw frozen source blob/mode and replays recorded byte repairs. This is not a mathematical proof audit or complete Gate 2 release verification.",
    }
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
