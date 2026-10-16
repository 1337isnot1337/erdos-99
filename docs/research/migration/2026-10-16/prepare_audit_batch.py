#!/usr/bin/env python3
"""Reconcile the source-main audit batch and queue all unrelated corpus rows."""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
MIGRATION = ROOT / "docs/research/migration/2026-10-16"
BATCH = "source-main-target-c-audit-batch-1"
ARCHIVE_PREFIX = "docs/archive/source-e99-main-42f0296d/"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows))


def expected_path(row: dict) -> str | None:
    return row.get("public_path") or row.get("proposed_destination") or row.get("destination_path") or row.get("proposed_destination_path")


def expected_sha(row: dict) -> str | None:
    return row.get("public_sha256") or row.get("planned_public_sha256") or row.get("planned_public_sha256_before_generated_artifact_header")


def matches_public(path: str | None, expected: str | None) -> bool:
    if not path or not expected:
        return False
    target = ROOT / path
    return target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == expected


def matches_row(row: dict, path_override: str | None = None) -> bool:
    path = path_override or expected_path(row)
    return matches_public(path, expected_sha(row))


def queue_publication(row: dict) -> None:
    path = expected_path(row)
    digest = expected_sha(row)
    if path:
        row["proposed_destination"] = path
    if digest:
        row["planned_public_sha256"] = digest
    row["public_path"] = None
    row["public_sha256"] = None
    row.pop("integration_batch", None)


def main() -> None:
    ledger = MIGRATION / "ledger"
    artifacts = read_jsonl(ledger / "source-main-artifacts.jsonl")
    edges = read_jsonl(ledger / "source-main-dependency-edges.jsonl")

    # The first batch contains the missing Target C audits, two shared audit
    # dependencies, all 38 source conflict snapshots, and their direct link
    # closure. Re-pin already copied shared audit files to this batch identity.
    for row in artifacts:
        if row.get("source_target") != "target-c" and row.get("integration_batch"):
            if matches_row(row):
                row["integration_batch"] = BATCH
            else:
                queue_publication(row)
                row["disposition"] = "queue_for_linked_source_batch"

    roots = {
        row["original_path"]
        for row in artifacts
        if row["original_path"].startswith("docs/audits/")
        and row.get("integration_batch") == BATCH
        and row.get("public_path") == row["original_path"]
        and matches_row(row)
    }

    # Expand through the frozen Markdown graph only where the exact destination
    # target is present. Missing report targets copied from the full checkpoint
    # qualify through their pre-recorded public hash.
    artifact_by_path = {row["original_path"]: row for row in artifacts}
    dependency_edges: dict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        dependency_edges[edge["from_source_path"]].append(edge)
    reachable = set(roots)
    queue = deque(roots)
    while queue:
        source_path = queue.popleft()
        for edge in dependency_edges.get(source_path, []):
            target_source = edge["to_source_path"]
            target_public = edge.get("to_destination_path")
            candidate = artifact_by_path.get(target_source)
            present = bool(target_public and (ROOT / target_public).is_file())
            if candidate and target_public and not matches_row(candidate, target_public):
                present = False
            if present and target_source not in reachable:
                reachable.add(target_source)
                queue.append(target_source)

    linked_reports = {
        path for path in reachable
        if path.startswith("docs/reports/")
        and path in artifact_by_path
        and matches_row(artifact_by_path[path])
    }

    integrated_audits = linked_reports_count = archived_versions = queued_reports = 0
    for row in artifacts:
        if row.get("source_target") != "target-c":
            continue
        path = row["original_path"]
        disposition = row.get("disposition", "")
        if disposition.startswith("exact_duplicate"):
            continue
        if disposition.startswith("preserve"):
            if matches_row(row):
                row["integration_batch"] = BATCH
                archived_versions += 1
            else:
                queue_publication(row)
                row["disposition"] = "queue_historical_conflict_for_source_report_batch"
            continue
        if disposition.startswith("integrate") or disposition.startswith("queue_for_source_main_report_batch"):
            is_audit = path.startswith("docs/audits/")
            is_linked_report = path in linked_reports
            if (is_audit or is_linked_report) and matches_row(row):
                row["public_path"] = expected_path(row)
                row["public_sha256"] = expected_sha(row)
                row["integration_batch"] = BATCH
                if is_audit:
                    integrated_audits += 1
                else:
                    row["disposition"] = "integrated_as_linked_noncanonical_dependency"
                    linked_reports_count += 1
            else:
                queue_publication(row)
                row["disposition"] = "queue_for_source_main_report_batch"
                queued_reports += 1

    # Keep non-C source artifact records only when their actual copied bytes are
    # present. This includes the two linked shared audits; other dependencies
    # stay queued with their parent report or later corpus batch.
    for row in artifacts:
        if row.get("source_target") == "target-c" or not row.get("integration_batch"):
            continue
        if matches_row(row):
            row["integration_batch"] = BATCH
        else:
            queue_publication(row)
            row["disposition"] = "queue_for_linked_source_batch"
    write_jsonl(ledger / "source-main-artifacts.jsonl", artifacts)

    dependencies = read_jsonl(ledger / "source-main-dependencies.jsonl")
    integrated_dependency_sources: set[str] = set()
    for row in dependencies:
        source_path = row["original_path"]
        linked_from = set(row.get("linked_from", []))
        audit_linked = bool(linked_from & reachable)
        artifact = artifact_by_path.get(source_path)
        if artifact and artifact.get("integration_batch") == BATCH and matches_row(artifact):
            row["destination_path"] = expected_path(artifact)
            row["public_sha256"] = expected_sha(artifact)
            row["integration_batch"] = BATCH
            row["disposition"] = "integrated from linked artifact ledger"
            integrated_dependency_sources.add(source_path)
            continue
        public_path = row.get("destination_path") or row.get("proposed_destination_path")
        public_matches = matches_public(public_path, row.get("public_sha256"))
        exact_existing = row.get("destination_relation") == "identical_same_path"
        historical = bool(public_path and public_path.startswith(ARCHIVE_PREFIX))
        if public_matches and (audit_linked or exact_existing or historical):
            row["destination_path"] = public_path
            row["integration_batch"] = BATCH if audit_linked or historical else None
            row["disposition"] = "integrated as linked noncanonical dependency" if audit_linked else ("preserved as linked historical source version" if historical else "exact destination dependency")
            integrated_dependency_sources.add(source_path)
        else:
            row["proposed_destination_path"] = public_path
            row["destination_path"] = None
            row["public_sha256"] = None
            row.pop("integration_batch", None)
            row["disposition"] = "queued with its source research batch"
    write_jsonl(ledger / "source-main-dependencies.jsonl", dependencies)

    files = read_jsonl(ledger / "source-main-files.jsonl")
    for row in files:
        if not row.get("integration_batch"):
            continue
        if matches_row(row) and (row.get("original_path") in integrated_dependency_sources or expected_path(row).startswith(ARCHIVE_PREFIX)):
            row["integration_batch"] = BATCH
            row["disposition"] = "integrated_as_linked_dependency"
        else:
            queue_publication(row)
            row["disposition"] = "queued_for_source_research_batch"
    write_jsonl(ledger / "source-main-files.jsonl", files)

    integrated_edges = 0
    for row in edges:
        if row.get("from_source_path") in reachable and row.get("to_destination_path") and (ROOT / row["to_destination_path"]).exists():
            row["integration_status"] = "integrated_with_audit_batch"
            integrated_edges += 1
        else:
            row["integration_status"] = "queued_with_source_research_batch"
    write_jsonl(ledger / "source-main-dependency-edges.jsonl", edges)

    rewrites = read_jsonl(ledger / "source-main-link-rewrites.jsonl")
    applied_rewrites = 0
    for row in rewrites:
        parent = row.get("parent_destination")
        if row.get("parent_source") in reachable and parent and (ROOT / parent).is_file():
            body = (ROOT / parent).read_text(errors="replace")
            if row.get("new_link") in body:
                row["application"] = "verified_in_reconstructed_copy"
                applied_rewrites += 1
                continue
        row["application"] = "queued_until_parent_report_batch"
    write_jsonl(ledger / "source-main-link-rewrites.jsonl", rewrites)

    print(json.dumps({
        "source_target_c_artifact_rows": sum(row.get("source_target") == "target-c" for row in artifacts),
        "integrated_missing_audits": integrated_audits,
        "integrated_linked_reports": linked_reports_count,
        "archived_source_conflicts": archived_versions,
        "queued_missing_reports": queued_reports,
        "reachable_source_markdown_paths": len(reachable),
        "integrated_dependency_records": len(integrated_dependency_sources),
        "integrated_dependency_edges": integrated_edges,
        "verified_link_rewrites": applied_rewrites,
        "queued_link_rewrites": len(rewrites) - applied_rewrites,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
