#!/usr/bin/env python3
"""Preserve Agent 2's selected source-main evidence without overwriting main.

All bytes are extracted from the pinned source Git object database. Markdown is
stored with a `.source` suffix so historical links do not join active docs.
Third-party and coordinator-owned material is explicitly excluded in the
append-only disposition manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess


SOURCE_MAIN = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
DESTINATION_MAIN = "c6e0394b3152d21075328bf4f26e6c070229bf13"


def git(repo: str, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", repo, *args])


def read_git_blob(repo: str, oid: str) -> bytes:
    return git(repo, "cat-file", "blob", oid)


def exclusion(path: str, work_type: str) -> tuple[str | None, str | None]:
    if work_type == "third_party_exclusion_review":
        return "excluded_third_party_source", "scans, extracted paper text, and PDFs are not copied without redistribution rights"
    if path.startswith("docs/state/") or path == "docs/STATE.md":
        return "excluded_coordinator_owned_state", "source status and registries remain in the provenance manifest; active destination state is coordinator-owned"
    if path.startswith((".github/", "tools/", "scripts/", "tests/", "docs/ci/", "docs/launch/", "docs/maintenance/", "research-packages/")):
        return "excluded_repository_or_operations_material", "source-repository workflow, release, test, and operations infrastructure is not mathematical research payload"
    if path in {
        ".editorconfig", ".gitignore", "AGENTS.md", "CONTRIBUTING.md", "README.md", "autoresearch.md",
        "docs/README.md", "docs/COORDINATION.md", "docs/MAINTENANCE.md", "docs/RESEARCH_WORKFLOW.md",
        "docs/START_HERE.md", "docs/KNOWLEDGE_MAP.md", "docs/archive/README.md",
    }:
        return "excluded_superseded_navigation_or_policy", "destination repository has its own current instructions, navigation, and maintenance contract"
    if path == "docs/archive/homelab_audit_history_v1.7.0.md":
        return "excluded_unrelated_private_operational_history", "unrelated homelab history is outside Erdős #99 research preservation"
    if path == "research/cleanup/slot2-8f-ref-artifact-map-2026-10-05.tsv":
        return "excluded_migration_operations_metadata", "cleanup/artifact-map bookkeeping is not mathematical evidence"
    return None, None


def archive_path(root: pathlib.Path, original: str) -> pathlib.Path:
    target = root / "source-main" / pathlib.PurePosixPath(original)
    if target.suffix.lower() == ".md":
        target = target.with_name(target.name + ".source")
    return target


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--destination", required=True)
    p.add_argument("--assignment", type=pathlib.Path, required=True)
    p.add_argument("--output-root", type=pathlib.Path, required=True)
    args = p.parse_args()

    source_head = git(args.source, "rev-parse", SOURCE_MAIN + "^{commit}").decode().strip()
    destination_head = git(args.destination, "rev-parse", DESTINATION_MAIN + "^{commit}").decode().strip()
    if source_head != SOURCE_MAIN or destination_head != DESTINATION_MAIN:
        raise SystemExit(f"pinned ref mismatch: source={source_head}, destination={destination_head}")

    tree_rows = git(args.source, "ls-tree", "-r", "-z", SOURCE_MAIN).split(b"\0")
    blobs = {}
    modes = {}
    for item in tree_rows:
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        if kind == "blob":
            path = raw_path.decode("utf-8", "surrogateescape")
            blobs[path] = oid
            modes[path] = mode

    rows = [json.loads(line) for line in args.assignment.read_text().splitlines() if line]
    owned = [r for r in rows if r["assigned_agent"] == 2]
    dispositions = []
    for row in owned:
        original = row["source_path"]
        oid = blobs.get(original)
        if oid != row["source_git_blob_sha1"]:
            raise SystemExit(f"pinned source blob mismatch at {original}")
        data = read_git_blob(args.source, oid)
        digest = hashlib.sha256(data).hexdigest()
        if digest != row["source_sha256"] or len(data) != row["source_bytes"]:
            raise SystemExit(f"pinned source hash/length mismatch at {original}")

        reason, rationale = exclusion(original, row["file_work_type"])
        disp = dict(row)
        if reason:
            disp.update(action=reason, rationale=rationale, preserved_destination_path=None)
        else:
            target = archive_path(args.output_root, original)
            if target.exists():
                existing = hashlib.sha256(target.read_bytes()).hexdigest()
                if existing != digest:
                    raise SystemExit(f"refusing to overwrite nonmatching path {target}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                target.chmod(0o755 if modes[original] == "100755" else 0o644)
            disp.update(
                action="preserved_exact_source_bytes_noncanonical",
                rationale=("source snapshot kept outside active research paths; source lifecycle is provenance only"
                           if row.get("source_lifecycle") else "first-party mathematical/research source preserved as unreviewed archival evidence"),
                preserved_destination_path=target.relative_to(args.output_root).as_posix(),
            )
        dispositions.append(disp)

    out = args.output_root / "corpus-dispositions.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n" for r in dispositions))
    print(json.dumps({
        "agent_2_assigned_files": len(owned),
        "preserved": sum(r["action"] == "preserved_exact_source_bytes_noncanonical" for r in dispositions),
        "excluded": sum(r["action"] != "preserved_exact_source_bytes_noncanonical" for r in dispositions),
        "conflicts_preserved_separately": sum(r["destination_relation"] == "same_path_different_content" and r["action"] == "preserved_exact_source_bytes_noncanonical" for r in dispositions),
        "third_party_exclusions": sum(r["action"] == "excluded_third_party_source" for r in dispositions),
        "manifest": str(out),
        "manifest_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
