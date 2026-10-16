#!/usr/bin/env python3
"""Verify the frozen source-only branch ledger against Git objects and files."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def blob(repo: Path, ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", f"{ref}:{path}"],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def verify_active_baseline(source: Path, destination: Path, errors: list[str]) -> None:
    base = Path(__file__).resolve().parent / "baseline"
    pin_path = base / "active-run-baseline-2026-10-16.json"
    try:
        pin = json.loads(pin_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read active run baseline: {exc}")
        return
    for label, repo, manifest_base in (
        ("source", source, base),
        ("destination", destination, base),
    ):
        record = pin.get("repositories", {}).get(label, {})
        sha = record.get("main_sha", "")
        try:
            if git(repo, "rev-parse", f"{sha}^{{tree}}") != record.get("main_tree"):
                errors.append(f"active {label} main tree does not match run baseline")
            actual = git(repo, "ls-tree", "-r", "--name-only", sha) + "\n"
        except subprocess.CalledProcessError:
            errors.append(f"active {label} main commit is unavailable")
            continue
        manifest_path = manifest_base / record.get("main_manifest_path", "")
        try:
            manifest = manifest_path.read_text()
        except OSError:
            errors.append(f"active {label} tracked-file manifest is missing")
            continue
        if hashlib.sha256(manifest.encode()).hexdigest() != record.get("main_manifest_sha256"):
            errors.append(f"active {label} tracked-file manifest hash differs from baseline")
        if len(manifest.splitlines()) != record.get("main_tracked_paths"):
            errors.append(f"active {label} tracked-file manifest count differs from baseline")
        if manifest != actual:
            errors.append(f"active {label} tracked-file manifest differs from the frozen main tree")
        prs = record.get("open_prs", {})
        pr_path = manifest_base / prs.get("inventory_path", "")
        try:
            pr_data = pr_path.read_bytes()
            pr_document = json.loads(pr_data)
        except (OSError, json.JSONDecodeError):
            errors.append(f"active {label} open-PR snapshot is unreadable")
            continue
        if hashlib.sha256(pr_data).hexdigest() != prs.get("inventory_sha256"):
            errors.append(f"active {label} open-PR snapshot hash differs from baseline")
        pr_rows = pr_document.get("open_prs", []) if isinstance(pr_document, dict) else pr_document
        if len(pr_rows) != prs.get("count"):
            errors.append(f"active {label} open-PR count differs from baseline")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path(__file__).resolve().parents[4],
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path(__file__).resolve().parent / "ledger/source-branch-files.jsonl",
    )
    args = parser.parse_args(argv)
    source = args.source_repo.resolve()
    destination = args.destination.resolve()
    ledger = args.ledger.resolve()
    errors: list[str] = []
    verify_active_baseline(source, destination, errors)
    try:
        rows = [json.loads(line) for line in ledger.read_text().splitlines() if line]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"source-branch-import: cannot read ledger: {exc}", file=sys.stderr)
        return 2
    snapshots = [row for row in rows if row.get("record_type") == "source_branch_snapshot"]
    files = [row for row in rows if row.get("record_type") == "source_branch_file"]
    comparisons = [
        row for row in rows if row.get("record_type") == "source_branch_main_comparison"
    ]
    if len(snapshots) != 1:
        errors.append(f"expected one branch snapshot row; found {len(snapshots)}")
        snapshot = snapshots[0] if snapshots else {}
    else:
        snapshot = snapshots[0]
    head = snapshot.get("source_head_sha", "")
    merge_base = snapshot.get("source_merge_base_sha", "")
    main = snapshot.get("frozen_source_main_sha", "")
    try:
        if git(source, "rev-parse", f"{head}^{{tree}}") != snapshot.get("source_head_tree"):
            errors.append("source branch head tree does not match the ledger")
        if git(source, "rev-parse", f"{merge_base}^{{tree}}") != snapshot.get("source_merge_base_tree"):
            errors.append("source merge-base tree does not match the ledger")
        if git(source, "rev-parse", f"{main}^{{tree}}") != snapshot.get("frozen_source_main_tree"):
            errors.append("frozen source-main tree does not match the ledger")
        manifest_path = snapshot.get("branch_manifest_path")
        if manifest_path:
            manifest = Path(manifest_path)
            lines = git(source, "ls-tree", "-r", "--name-only", head).splitlines()
            manifest_bytes = ("\n".join(lines) + "\n").encode()
            if len(lines) != snapshot.get("branch_tracked_paths"):
                errors.append("source branch tracked-path count does not match its manifest")
            if hashlib.sha256(manifest_bytes).hexdigest() != snapshot.get("branch_manifest_sha256"):
                errors.append("source branch tracked-path manifest hash does not match")
        status_counts: dict[str, int] = {}
        status_by_path: dict[str, str] = {}
        for line in git(source, "diff", "--name-status", f"{main}..{head}").splitlines():
            fields = line.split("\t", 1)
            code = fields[0]
            status_counts[code[0]] = status_counts.get(code[0], 0) + 1
            if len(fields) == 2:
                status_by_path[fields[1]] = code
        if status_counts != snapshot.get("source_main_comparison_status_counts"):
            errors.append("source branch/source-main path comparison counts do not match")
        expected = set(
            git(source, "diff", "--name-only", f"{merge_base}..{head}").splitlines()
        )
    except subprocess.CalledProcessError as exc:
        print(f"source-branch-import: Git identity lookup failed: {exc}", file=sys.stderr)
        return 2
    observed = {row.get("original_path") for row in files}
    if observed != expected:
        errors.append(
            f"branch delta/ledger paths differ: source={len(expected)} ledger={len(observed)}"
        )
    counts: dict[str, int] = {}
    for row in files:
        path = row.get("original_path", "")
        disposition = row.get("disposition", "")
        counts[disposition] = counts.get(disposition, 0) + 1
        try:
            source_data = subprocess.check_output(["git", "show", f"{head}:{path}"], cwd=source)
        except subprocess.CalledProcessError:
            errors.append(f"source file missing at frozen head: {path}")
            continue
        source_hash = hashlib.sha256(source_data).hexdigest()
        source_blob = blob(source, head, path)
        if source_hash != row.get("source_sha256"):
            errors.append(f"source SHA-256 mismatch: {path}")
        if source_blob != row.get("source_git_blob_sha"):
            errors.append(f"source Git blob mismatch: {path}")
        if len(source_data) != row.get("source_bytes"):
            errors.append(f"source byte-count mismatch: {path}")
        if row.get("source_equals_frozen_main"):
            if blob(source, main, path) != source_blob:
                errors.append(f"frozen-main identity mismatch: {path}")
        destination_path = destination / row.get("destination_path", "")
        if not destination_path.is_file():
            errors.append(f"destination file missing: {row.get('destination_path')}")
            continue
        dest_data = destination_path.read_bytes()
        dest_sha = hashlib.sha256(dest_data).hexdigest()
        dest_blob = git(destination, "hash-object", str(destination_path))
        if dest_sha != row.get("destination_sha256"):
            errors.append(f"destination SHA-256 mismatch: {row.get('destination_path')}")
        if dest_blob != row.get("destination_git_blob_sha"):
            errors.append(f"destination Git blob mismatch: {row.get('destination_path')}")
        byte_identity = source_data == dest_data
        if byte_identity != bool(row.get("byte_identity_verified")):
            errors.append(f"byte-identity flag mismatch: {path}")
        if disposition in {"exact_duplicate", "integrated_as_active_noncanonical_research"} and not byte_identity:
            errors.append(f"byte-preservation disposition failed: {path}")
        nav_paths = row.get("destination_navigation_path", [])
        if isinstance(nav_paths, str):
            nav_paths = [nav_paths]
        for nav_path in nav_paths:
            if not (destination / nav_path).is_file():
                errors.append(f"secondary navigation target missing: {nav_path}")
    source_main_queue_path = destination / "docs/research/migration/2026-10-16/ledger/source-main-files.jsonl"
    try:
        source_main_queue = {
            row.get("original_path"): row
            for row in (
                json.loads(line)
                for line in source_main_queue_path.read_text().splitlines()
                if line
            )
        }
    except (OSError, json.JSONDecodeError):
        source_main_queue = {}
        errors.append("cannot read source-main file ledger for comparison records")
    for row in comparisons:
        path = row.get("original_path", "")
        if not status_by_path.get(path, "").startswith("M"):
            errors.append(f"comparison record is not a modified source-main path: {path}")
        try:
            branch_data = subprocess.check_output(["git", "show", f"{head}:{path}"], cwd=source)
            main_data = subprocess.check_output(["git", "show", f"{main}:{path}"], cwd=source)
        except subprocess.CalledProcessError:
            errors.append(f"branch/main comparison object missing: {path}")
            continue
        if hashlib.sha256(branch_data).hexdigest() != row.get("source_sha256"):
            errors.append(f"branch comparison SHA-256 mismatch: {path}")
        if blob(source, head, path) != row.get("source_git_blob_sha"):
            errors.append(f"branch comparison Git blob mismatch: {path}")
        if hashlib.sha256(main_data).hexdigest() != row.get("source_main_sha256"):
            errors.append(f"frozen source-main SHA-256 mismatch: {path}")
        if blob(source, main, path) != row.get("source_main_git_blob_sha"):
            errors.append(f"frozen source-main Git blob mismatch: {path}")
        if len(main_data) != row.get("source_main_bytes"):
            errors.append(f"frozen source-main byte-count mismatch: {path}")
        disposition = row.get("disposition")
        if disposition == "already_fully_represented_by_exact_source_main_copy":
            target = destination / row.get("destination_path", "")
            if not target.is_file() or target.read_bytes() != main_data:
                errors.append(f"destination is not the exact frozen source-main successor: {path}")
            if branch_data == main_data:
                errors.append(f"comparison was marked modified but source bytes are identical: {path}")
        elif disposition == "superseded_by_destination_current_frontier":
            target = destination / row.get("destination_path", "")
            if not target.is_file() or not row.get("destination_sha256"):
                errors.append(f"destination frontier mapping missing: {path}")
            elif hashlib.sha256(target.read_bytes()).hexdigest() != row.get("destination_sha256"):
                errors.append(f"destination frontier hash mismatch: {path}")
        elif disposition == "queued_as_source_main_research":
            queued = source_main_queue.get(path)
            if not queued or not str(queued.get("disposition", "")).startswith("queued"):
                errors.append(f"source-main queue does not account for branch version: {path}")
            if queued and queued.get("source_sha256") != row.get("source_main_sha256"):
                errors.append(f"source-main queue identity differs for {path}")
        else:
            errors.append(f"unknown branch/main comparison disposition {disposition}: {path}")
    relevant_modified = {
        path
        for path, status in status_by_path.items()
        if status.startswith("M")
        and (path.startswith("docs/reports/") or path.startswith("docs/targets/target-c/") or path.startswith("research/"))
    }
    delta_target_paths = {
        row.get("original_path")
        for row in files
        if row.get("source_main_git_blob_sha")
        and row.get("source_equals_frozen_main") is False
        and (
            str(row.get("original_path", "")).startswith("docs/reports/")
            or str(row.get("original_path", "")).startswith("docs/targets/target-c/")
            or str(row.get("original_path", "")).startswith("research/")
        )
    }
    if len(relevant_modified) != snapshot.get("source_main_comparison_target_c_paths"):
        errors.append("Target C branch/source-main modified-path count does not match snapshot")
    if relevant_modified != {row.get("original_path") for row in comparisons} | delta_target_paths:
        errors.append("Target C branch/source-main comparison ledger is incomplete")
    expected_roles = {"mathematical_report": 8, "finite_verifier": 8}
    for role, count in expected_roles.items():
        observed_count = sum(row.get("file_role") == role for row in files)
        if observed_count != count:
            errors.append(f"expected {count} {role} rows; found {observed_count}")
    if errors:
        for error in errors:
            print(f"source-branch-import: ERROR {error}", file=sys.stderr)
        print(f"source-branch-import: FAIL ({len(errors)} errors)", file=sys.stderr)
        return 1
    print(
        "source-branch-import: PASS; "
        f"{len(files)} branch paths, "
        f"{len(comparisons)} older branch/source-main comparison paths, "
        f"{snapshot.get('branch_tracked_paths')} branch tracked paths, "
        f"{counts.get('exact_duplicate', 0)} exact duplicates, "
        f"{counts.get('integrated_as_active_noncanonical_research', 0)} byte-exact imports, "
        f"{len(files) - counts.get('exact_duplicate', 0) - counts.get('integrated_as_active_noncanonical_research', 0)} metadata/navigation treatments; "
        "source and destination blob/SHA-256 identities verified; active main manifests and open-PR snapshots match the frozen baseline"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
