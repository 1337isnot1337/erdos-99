#!/usr/bin/env python3
"""Build and verify the exhaustive theorem-state artifact registry.

Every Markdown research artifact under the roots declared by theorem-state.yaml gets a
small first-line JSON metadata header. The generated JSONL index is exhaustive and is
computed from the manifest plus conservative defaults; filenames and merge status never
promote an artifact. A single file may carry claims with different lifecycle states; in
that case its artifact-level status is ``mixed`` and claim_statuses records the exact
claim-level classifications.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml

MANIFEST = Path("docs/state/theorem-state.yaml")
HEADER_PREFIX = "<!-- theorem-state: "
HEADER_SUFFIX = " -->"
ENTRY_BUCKETS = (
    "current_canonical_entries",
    "audited_working",
    "regressions",
    "rejected_or_overridden",
)


def load_manifest(root: Path) -> dict[str, Any]:
    data = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("theorem-state manifest must be a mapping")
    return data


def iter_entries(state: dict[str, Any]) -> Iterable[tuple[str, str, dict[str, Any]]]:
    targets = state.get("targets", {})
    if not isinstance(targets, dict):
        return
    for target_name, target in targets.items():
        if not isinstance(target, dict):
            continue
        for bucket in ENTRY_BUCKETS:
            rows = target.get(bucket, []) or []
            if not isinstance(rows, list):
                continue
            for row in rows:
                if isinstance(row, dict):
                    yield target_name, bucket, row


def artifact_paths(root: Path, state: dict[str, Any]) -> list[str]:
    policy = state["artifact_policy"]
    excluded = set(policy.get("exclude", []))
    out: set[str] = set()
    for raw_root in policy["roots"]:
        base = root / raw_root
        if not base.is_dir():
            raise ValueError(f"artifact root does not exist: {raw_root}")
        for path in base.rglob("*.md"):
            rel = path.relative_to(root).as_posix()
            if rel not in excluded:
                out.add(rel)
    return sorted(out)


def entry_references(state: dict[str, Any]) -> dict[str, list[tuple[str, str, dict[str, Any]]]]:
    refs: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}
    for target_name, bucket, entry in iter_entries(state):
        for key in ("report", "audit"):
            path = entry.get(key)
            if isinstance(path, str):
                refs.setdefault(path, []).append((target_name, bucket, entry))
    return refs


def infer_target(path: str, refs: list[tuple[str, str, dict[str, Any]]]) -> str:
    targets = sorted({target for target, _, _ in refs})
    if len(targets) == 1:
        return targets[0]
    name = Path(path).name.lower()
    for token, target in (("target_a", "target-a"), ("target_b", "target-b"), ("target_c", "target-c")):
        if token in name:
            return target
    return "shared"


def build_record(path: str, state: dict[str, Any], refs: list[tuple[str, str, dict[str, Any]]]) -> dict[str, Any]:
    policy = state["artifact_policy"]
    claim_statuses = {
        str(entry["id"]): str(entry["status"])
        for _, _, entry in refs
        if isinstance(entry.get("id"), str) and isinstance(entry.get("status"), str)
    }
    statuses = set(claim_statuses.values())
    if len(statuses) > 1:
        status = "mixed"
    elif statuses:
        status = next(iter(statuses))
    elif path == "docs/archive" or path.startswith("docs/archive/"):
        status = policy["archive_status"]
    else:
        status = policy["default_status"]

    ids = sorted(claim_statuses)
    depends = sorted({x for _, _, entry in refs for x in (entry.get("depends_on") or []) if isinstance(x, str)})
    invalidates = sorted({x for _, _, entry in refs for x in (entry.get("invalidates") or []) if isinstance(x, str)})
    supersedes = sorted({x for _, _, entry in refs for x in (entry.get("supersedes") or []) if isinstance(x, str)})

    return {
        "artifact_id": "ART-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:12].upper(),
        "path": path,
        "target": infer_target(path, refs),
        "status": status,
        "canonical": "canonical" in statuses,
        "claim_ids": ids,
        "claim_statuses": {key: claim_statuses[key] for key in sorted(claim_statuses)},
        "depends_on": depends,
        "invalidates": invalidates,
        "supersedes": supersedes,
    }


def build_records(root: Path, state: dict[str, Any]) -> list[dict[str, Any]]:
    refs = entry_references(state)
    paths = artifact_paths(root, state)
    path_set = set(paths)
    dangling = sorted(
        path for path in refs
        if path.startswith(("docs/reports/", "docs/audits/", "docs/archive/")) and path not in path_set
    )
    if dangling:
        raise ValueError("manifest references artifacts outside the registry: " + ", ".join(dangling))
    return [build_record(path, state, refs.get(path, [])) for path in paths]


def header_for(record: dict[str, Any]) -> str:
    compact = {
        "artifact_id": record["artifact_id"],
        "status": record["status"],
        "canonical": record["canonical"],
        "target": record["target"],
        "claim_ids": record["claim_ids"],
        "claim_statuses": record["claim_statuses"],
        "index": "docs/state/artifact-index.jsonl",
    }
    return HEADER_PREFIX + json.dumps(compact, sort_keys=True, separators=(",", ":")) + HEADER_SUFFIX


def replace_header(text: str, header: str) -> str:
    lines = text.splitlines(keepends=True)
    if lines and lines[0].startswith(HEADER_PREFIX) and lines[0].rstrip("\r\n").endswith(HEADER_SUFFIX):
        ending = "\r\n" if lines[0].endswith("\r\n") else "\n"
        lines[0] = header + ending
        return "".join(lines)
    return header + "\n" + text


def index_text(records: list[dict[str, Any]]) -> str:
    return "".join(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n" for record in records)


def legacy_unreviewed_header(first: str, record: dict[str, Any]) -> bool:
    """Read an older header format without treating it as theorem authority.

    This is format compatibility only. It reads no migration ledger, source
    hashes, archived payloads, or Git history and places no constraint on the
    report body. The current manifest alone determines the record's lifecycle.
    """
    prefix, suffix = "<!-- migration-provenance: ", " -->"
    if (record["status"] != "unreviewed" or record["canonical"]
            or record["claim_ids"] or record["claim_statuses"]
            or not first.startswith(prefix) or not first.endswith(suffix)):
        return False
    try:
        header = json.loads(first[len(prefix):-len(suffix)])
    except (ValueError, TypeError):
        return False
    return (isinstance(header, dict)
            and header.get("source_canonical", False) is False
            and header.get("source_lifecycle") == "unreviewed"
            and header.get("destination_status") in
            {"historical_unreviewed_noncanonical", "unreviewed_noncanonical"})


def write_state(root: Path, state: dict[str, Any], records: list[dict[str, Any]], write_headers: bool) -> int:
    index_path = root / state["artifact_policy"]["index"]
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(index_text(records), encoding="utf-8", newline="\n")
    changed_headers = 0
    if write_headers:
        for record in records:
            path = root / record["path"]
            old = path.read_text(encoding="utf-8")
            new = replace_header(old, header_for(record))
            if new != old:
                path.write_text(new, encoding="utf-8", newline="\n")
                changed_headers += 1
    return changed_headers


def check_state(root: Path, state: dict[str, Any], records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    expected_index = index_text(records)
    index_path = root / state["artifact_policy"]["index"]
    if not index_path.is_file():
        errors.append(f"missing generated artifact index: {index_path.relative_to(root)}")
    elif index_path.read_text(encoding="utf-8") != expected_index:
        errors.append("artifact-index.jsonl is stale; run tools/build_artifact_index.py --write --write-headers")

    seen_ids: dict[str, str] = {}
    for record in records:
        ident = record["artifact_id"]
        if ident in seen_ids:
            errors.append(f"duplicate artifact id {ident}: {seen_ids[ident]} and {record['path']}")
        seen_ids[ident] = record["path"]
        path = root / record["path"]
        with path.open("r", encoding="utf-8") as source:
            first = source.readline().rstrip("\r\n")
        if first != header_for(record) and not legacy_unreviewed_header(first, record):
            errors.append(f"missing/stale theorem-state metadata header: {record['path']}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write the generated JSONL index")
    parser.add_argument("--write-headers", action="store_true", help="also insert/update metadata headers")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        state = load_manifest(root)
        records = build_records(root, state)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as exc:
        print(f"artifact-index: {exc}", file=sys.stderr)
        return 1

    if args.write or args.write_headers:
        changed = write_state(root, state, records, args.write_headers)
        print(f"artifact-index: wrote {len(records)} records; updated {changed} metadata headers")
        return 0

    errors = check_state(root, state, records)
    if errors:
        for error in errors:
            print(f"artifact-index: {error}", file=sys.stderr)
        return 1
    print(f"artifact-index: OK ({len(records)} artifacts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

