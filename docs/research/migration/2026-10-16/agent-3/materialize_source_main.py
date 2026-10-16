#!/usr/bin/env python3
"""Materialize only Agent 3's pinned source-main research and provenance."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ARCHIVE = "docs/archive/source-e99-main-42f0296d"
PRIVATE_HOME = re.compile(rb"(?<![A-Za-z0-9_.-])/home/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*")
INVERSE_PATH = "docs/audits/target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md"
RATE_OR_INVERSE = re.compile(rb"K(?:'|\xe2\x80\xb2)?/D.{0,80}Lipschitz|q\s*=\s*O\s*\(\s*D\s*\^\s*\(\s*4\s*/\s*5", re.I)


def git(repo: Path, *args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], input=data, check=True,
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


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def archive_path(path: str) -> str:
    if path.lower().endswith(".md"):
        return f"{ARCHIVE}/{path}.source"
    return f"{ARCHIVE}/{path}"


def disposition_class(path: str) -> tuple[str, str]:
    if path.startswith(("papers/", "extracted/")):
        return "exclude_third_party", "Third-party papers and OCR derivatives are not imported; source path, blob, SHA-256, and citation context remain in this ledger."
    if path in ("docs/state/artifact-index.jsonl", "docs/state/theorem-state.yaml"):
        return "exclude_shared_state_registry", "Shared claim registry/state file is not copied or edited; per-artifact source lifecycle and claim metadata are retained in this migration ledger."
    if path in ("docs/README.md", "docs/KNOWLEDGE_MAP.md", "docs/START_HERE.md",
                "docs/reports/README.md", "docs/targets/README.md", "docs/archive/README.md",
                "research/README.md", "README.md", ".gitignore", ".github/PULL_REQUEST_TEMPLATE.md"):
        return "exclude_shared_navigation", "Shared navigation or repository instructions; destination guidance remains authoritative."
    if path == "docs/state/THEOREM_GRAPH.generated.md" or path == "docs/STATE.md":
        return "archive_source_state_snapshot", "Historical source state view is preserved as a .source archive snapshot; no destination theorem state or generated view is changed."
    if path.startswith("research/"):
        return "preserve_research", "First-party research text, computational verifier, or supporting evidence under the source research tree."
    if path.startswith(("docs/reports/", "docs/audits/", "docs/theory/", "docs/research/")):
        return "preserve_research", "First-party proof, audit, research, or mathematical negative-result artifact."
    if path.startswith(("docs/targets/", "docs/prompts/")):
        return "archive_historical_research_context", "Historical target route or research prompt is preserved outside active destination state."
    if path == "docs/literature_review.md":
        return "archive_first_party_literature_review", "First-party literature analysis is preserved; referenced external papers remain citations and are not copied."
    if path.startswith("docs/archive/") and "homelab" not in path.lower() and "erdos" in path.lower():
        return "preserve_historical_report", "First-party historical Erdős #99 report already marked as archival source material."
    if path.startswith("docs/archive/") and "homelab" in path.lower():
        return "exclude_unrelated_nonresearch", "Unrelated local-service audit history is outside the mathematical corpus."
    return "exclude_nonmathematical_infrastructure", "Repository, CI, publication, maintenance, benchmark, or task-selection infrastructure is outside the assigned mathematical corpus; source hash remains recorded."


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--source-commit", required=True)
    ap.add_argument("--destination-commit", required=True)
    ap.add_argument("--allocation", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--materialize", action="store_true")
    args = ap.parse_args()

    dest_tree = tree(args.destination, args.destination_commit)
    dest_blobs: dict[str, list[str]] = {}
    for path, oid in dest_tree.items():
        dest_blobs.setdefault(oid, []).append(path)
    index_bytes = git(args.source, "show", f"{args.source_commit}:docs/state/artifact-index.jsonl")
    idx = {r["path"]: r for r in
           (json.loads(line) for line in index_bytes.decode().splitlines() if line.strip())}
    rows = [json.loads(line) for line in args.allocation.read_text().splitlines() if line.strip()]
    rows = [r for r in rows if r.get("owner") == 3]
    output_rows = []
    materialized = []
    for row in rows:
        path = row["source_path"]
        classification, reason = disposition_class(path)
        out = {**row,
               "source_commit": args.source_commit,
               "source_artifact_index_entry": idx.get(path),
               "destination_artifact_path": None,
               "destination_sha256": None,
               "destination_git_blob_sha1": None,
               "source_body_sha256": None,
               "destination_body_sha256": None,
               "destination_bytes": None,
               "transformations": [],
               "mathematical_disposition": classification,
               "disposition_reason": reason,
               "authority_note": "Source lifecycle and source theorem-state labels are provenance only. Destination theorem-state remains authoritative; this import promotes no claim.",
               "migration_status": None}

        if classification.startswith("exclude_") or classification == "exclude_unrelated_nonresearch":
            out["migration_status"] = classification
            output_rows.append(out)
            continue

        content = git(args.source, "cat-file", "blob", row["source_blob"])
        original_body = content
        markdown = path.lower().endswith(".md")
        removed_header = b""
        if markdown:
            lines = content.splitlines(keepends=True)
            if lines and lines[0].startswith(b"<!-- theorem-state:"):
                removed_header = lines.pop(0)
                content = b"".join(lines)
                out["source_theorem_state_header"] = removed_header.decode("utf-8", "replace").rstrip("\r\n")
                out["transformations"].append("removed_source_theorem_state_header_and_retained_its_fields_in_ledger")
        out["source_body_sha256"] = sha(content)

        # Code remains byte-exact; local path redactions are applied only to
        # prose/data, never to executable source text.
        if not path.lower().endswith((".py", ".cpp", ".hpp")):
            safe = PRIVATE_HOME.sub(b"[local filesystem path omitted]", content)
            if safe != content:
                out["transformations"].append("redacted_absolute_owner_local_paths_in_prose_or_data")
            content = safe
        out["destination_body_sha256"] = sha(content)

        should_archive = classification in ("archive_source_state_snapshot",
                                               "archive_historical_research_context",
                                               "archive_first_party_literature_review") or row["source_relation"] == "same_path_content_conflict"
        if classification == "preserve_historical_report":
            target = path
        elif should_archive:
            target = archive_path(path)
        elif row["source_relation"] == "same_path_content_conflict":
            target = archive_path(path)
        else:
            target = path

        # Target maps/frontiers and prompts stay outside active paths.
        if path.startswith(("docs/targets/", "docs/prompts/")):
            target = archive_path(path)
        if row["source_relation"] == "same_path_content_conflict":
            target = archive_path(path)

        warning = "Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical."
        source_status = (idx.get(path) or {}).get("status")
        if source_status:
            warning = f"Source lifecycle was `{source_status}`; it is retained as provenance only. Destination status remains unreviewed/noncanonical."
        if path == INVERSE_PATH or RATE_OR_INVERSE.search(original_body):
            warning = ("Withdrawn inverse-phase/rate inference preserved only as historical source text. "
                       "Do not use a global K'/D-Lipschitz conclusion or q=O(D^(4/5)) rate as a premise; "
                       "destination corrections remain authoritative.")
            if not should_archive:
                target = archive_path(path)
                out["transformations"].append("forced_historical_archive_for_withdrawn_inverse_phase_or_rate_claim")

        if markdown:
            marker = {
                "source_repository": "https://github.com/1337isnot1337/e-99",
                "source_commit": args.source_commit,
                "source_path": path,
                "source_blob": row["source_blob"],
                "source_sha256": row["source_sha256"],
                "source_lifecycle": source_status or "not_indexed_first_party_source_material",
                "source_canonical": (idx.get(path) or {}).get("canonical"),
                "destination_status": "historical_unreviewed_noncanonical",
            }
            if target.startswith(ARCHIVE + "/"):
                warning_text = (f"> **Historical source snapshot; destination authority remains current.** {warning} "
                                f"Source path: `{path}`. Source commit: `{args.source_commit}`.\n\n")
                if path == INVERSE_PATH or RATE_OR_INVERSE.search(original_body):
                    warning_text += ("> **Withdrawn inference warning:** this source version must not restore the global `K'/D`-Lipschitz "
                                     "inverse-phase conclusion or the `q=O(D^(4/5))` rate.\n\n")
                content = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n").encode() + warning_text.encode() + content
            else:
                content = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n" +
                           f"> **Imported source research; no destination claim is promoted.** {warning}\n\n").encode() + content
            out["transformations"].append("added_source_provenance_and_nonpromotion_notice")
            out["destination_body_sha256"] = sha(content)
        else:
            out["destination_body_sha256"] = sha(content)

        # A preexisting archive object with the same name is never overwritten.
        existing_oid = dest_tree.get(target)
        if existing_oid:
            existing = git(args.destination, "cat-file", "blob", existing_oid)
            if existing == content:
                out["migration_status"] = "exact_destination_duplicate"
                out["destination_artifact_path"] = target
                out["destination_sha256"] = sha(existing)
                out["destination_git_blob_sha1"] = existing_oid
                output_rows.append(out)
                continue
            target = target + ".agent3-" + row["source_sha256"][:12]
            out["transformations"].append("collision_avoided_with_sha256_suffix")

        out["destination_artifact_path"] = target
        out["destination_sha256"] = sha(content)
        out["destination_bytes"] = len(content)
        out["destination_git_blob_sha1"] = hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()
        out["migration_status"] = "preserved_historical_snapshot" if target.startswith(ARCHIVE + "/") else "preserved_at_source_path"
        if args.materialize:
            target_path = args.destination / target
            target_path.parent.mkdir(parents=True, exist_ok=True)
            if target_path.exists():
                raise RuntimeError(f"refusing to overwrite existing path: {target}")
            target_path.write_bytes(content)
        materialized.append(out)
        output_rows.append(out)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in output_rows))
    summary = {
        "source_commit": args.source_commit,
        "destination_baseline": args.destination_commit,
        "agent_3_allocated_file_count": len(rows),
        "disposition_counts": dict(Counter(r["mathematical_disposition"] for r in output_rows)),
        "migration_status_counts": dict(Counter(r["migration_status"] for r in output_rows)),
        "materialized_file_count": len(materialized),
        "materialized_bytes": sum(r.get("bytes", 0) for r in materialized),
        "excluded_third_party_file_count": sum(r["mathematical_disposition"] == "exclude_third_party" for r in output_rows),
    }
    (args.output.parent / "source-main-disposition-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
