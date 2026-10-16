#!/usr/bin/env python3
"""Prepare missing source-main archives from an existing authorized local clone.

No network requests, Git writes, theorem promotions, or overwrites are performed.
The default is a plan. --apply writes exact source files to a historical archive.
Commit the explicit additions, then rerun the union audit against that commit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

from check_migration_union import (AuditError, BASE, Git, ROOT, SOURCE,
                                   SOURCE_TREE, audit, publication_exclusion, safe_path)

ARCHIVE = ROOT + "integration/source-main/"


def prepare(source: Git, report: dict, expected_source: str = SOURCE,
            expected_tree: str = SOURCE_TREE) -> list[dict]:
    if report["errors"]:
        raise AuditError("Resolve integrity errors before copying missing source files")
    commit = source.resolve(expected_source)
    actual_tree = source.run("rev-parse", commit + "^{tree}").decode().strip()
    if actual_tree != expected_tree:
        raise AuditError("Source checkout does not contain the pinned source tree")
    entries = source.tree(commit)
    plan = []
    for row in report["missing"]:
        path = safe_path(row["source_path"])
        mode, oid = entries.get(path, (None, None))
        if publication_exclusion(path):
            raise AuditError(f"Reference material cannot enter a repair plan: {path}")
        if mode not in ("100644", "100755") or (mode, oid) != (row["source_mode"], row["source_blob"]):
            raise AuditError(f"Source identity mismatch: {path}")
        data = source.blob(oid)
        if hashlib.sha256(data).hexdigest() != row["source_sha256"]:
            raise AuditError(f"Source byte hash mismatch: {path}")
        plan.append(dict(row, destination=ARCHIVE + path + ".source", data=data))
    return plan


def apply_plan(root: Path, plan: list[dict]) -> list[str]:
    root = root.resolve()
    pending = []
    seen = set()
    # Preflight every target before writing any file.
    for item in plan:
        relative = safe_path(item["destination"])
        if not relative.startswith(ARCHIVE) or relative in seen:
            raise AuditError("Repair targets must be unique historical archive paths")
        seen.add(relative)
        target = root / relative
        for parent in (target, *target.parents):
            if parent == root:
                break
            if parent.is_symlink():
                raise AuditError(f"Symlink in repair target: {relative}")
        if target.exists():
            if not target.is_file() or target.read_bytes() != item["data"]:
                raise AuditError(f"Refusing to overwrite a different file: {relative}")
        else:
            pending.append((target, item["data"]))
    for target, data in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(data)
        target.chmod(0o644)
    return [str(p.relative_to(root)) for p, _ in pending]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        destination, source = Git(args.repo), Git(args.source_repo)
        if destination.path == source.path:
            raise AuditError("Source and destination must be different checkouts")
        head = destination.resolve("HEAD")
        report, _ = audit(destination, head)
        plan = prepare(source, report)
        output = args.output.absolute()
        if output.is_relative_to(destination.path) or output.is_relative_to(source.path):
            raise AuditError("Write the repair receipt outside both repositories")
        if output.exists() or output.is_symlink():
            raise AuditError("Output receipt must not already exist")
        output.parent.mkdir(parents=True, exist_ok=True)
        if destination.resolve("HEAD") != head:
            raise AuditError("Destination HEAD changed during preparation")
        written = apply_plan(destination.path, plan) if args.apply else []
        receipt = {"candidate_before": head, "source_commit": SOURCE,
                   "baseline_commit": BASE, "applied": args.apply, "written": written,
                   "planned": [{k: v for k, v in item.items() if k != "data"} for item in plan],
                   "git_committed": False, "source_main_preservation_passed": False,
                   "deprecation_ready": False, "release_verified": False,
                   "next_check": "Commit reviewed explicit additions, then run check_migration_union.py again."}
        with output.open("x", encoding="utf-8") as stream:
            json.dump(receipt, stream, indent=2, sort_keys=True)
            stream.write("\n")
        print(json.dumps({"planned": len(plan), "written": len(written),
                          "git_committed": False, "deprecation_ready": False}))
        return 0
    except (AuditError, OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"migration-repair: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
