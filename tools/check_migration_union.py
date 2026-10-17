#!/usr/bin/env python3
"""Audit the combined migration by source identity, not independent ownership.

Read-only by default. No research code is executed. An optional replay directory
contains historical source bytes, not a replacement for the accepted theorem state.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

SOURCE = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
SOURCE_TREE = "e061f039eac44c286a00eacdcaa9a4cbbb877891"
BASE = "c6e0394b3152d21075328bf4f26e6c070229bf13"
ROOT = "docs/research/migration/2026-10-16/"
ASSIGNMENTS = (
    ROOT + "agent-1/evidence/source-main-three-way-assignment.jsonl",
    ROOT + "agent-2/corpus-assignment.jsonl",
    ROOT + "agent-3/source-main-allocation.jsonl",
)
DISPOSITIONS = (
    ROOT + "agent-1/source-main-reconciliation.jsonl",
    ROOT + "agent-2/corpus/corpus-dispositions.jsonl",
    ROOT + "agent-3/source-main-dispositions.jsonl",
)
FROZEN = ROOT + "frozen-target-c-813-dispositions.jsonl"
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
FROZEN_SCHEMA = "erdos-99-frozen-target-c-813-disposition/v1"


class AuditError(ValueError):
    """Invalid or incomplete evidence."""


def safe_path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value:
        raise AuditError(f"Invalid repository path: {value!r}")
    parts = value.split("/")
    if any(p in ("", ".", "..") or p.lower() == ".git" for p in parts):
        raise AuditError(f"Unsafe repository path: {value!r}")
    return value


def digest(kind: str, data: bytes) -> str:
    return hashlib.sha1(kind.encode() + b" " + str(len(data)).encode() + b"\0" + data).hexdigest()


def source_record(row: dict[str, Any]) -> tuple[str, tuple[str, str, str]]:
    path = safe_path(row["source_path"])
    blob = row.get("source_git_blob_sha1", row.get("source_blob"))
    if ("source_git_blob_sha1" in row and "source_blob" in row
            and row["source_git_blob_sha1"] != row["source_blob"]):
        raise AuditError(f"Conflicting source blob identities: {path}")
    mode, sha256 = row.get("source_mode"), row.get("source_sha256")
    if not isinstance(blob, str) or not HEX40.fullmatch(blob):
        raise AuditError(f"Invalid source blob: {path}")
    if mode not in ("100644", "100755", "120000"):
        raise AuditError(f"Unsupported source mode: {path}")
    if not isinstance(sha256, str) or not HEX64.fullmatch(sha256):
        raise AuditError(f"Invalid source SHA-256: {path}")
    return path, (mode, blob, sha256)


def frozen_record(row: dict[str, Any], records: dict[str, tuple[str, str, str]],
                  source_tree: str = SOURCE_TREE) -> tuple[str, dict[str, Any]]:
    """Read the committed nested v1 schema and bind it to the source inventory.

    A destination hash alone must never discharge an unrelated source identity.
    Source modes come from the reconstructed pinned Git tree; the frozen schema
    records the destination mode rather than duplicating the source mode.
    """
    if row.get("schema_version") != FROZEN_SCHEMA:
        raise AuditError("Unsupported frozen disposition schema")
    source, destination = row.get("source"), row.get("destination")
    if not isinstance(source, dict) or not isinstance(destination, dict):
        raise AuditError("Frozen disposition requires source and destination objects")
    path, target = safe_path(source.get("path")), safe_path(destination.get("path"))
    identity = records.get(path)
    if identity is None:
        raise AuditError(f"Frozen source path is absent from the pinned inventory: {path}")
    mode, blob, sha256 = identity
    if (mode not in ("100644", "100755")
            or source.get("git_blob_sha1") != blob or source.get("sha256") != sha256
            or ("mode" in source and source["mode"] != mode)):
        raise AuditError(f"Frozen source identity mismatch: {path}")
    if (source.get("repository") != "1337isnot1337/e-99"
            or source.get("commit") != SOURCE or source.get("tree") != source_tree):
        raise AuditError(f"Frozen source snapshot mismatch: {path}")
    if destination.get("repository") != "1337isnot1337/erdos-99":
        raise AuditError(f"Frozen destination repository mismatch: {target}")
    for obj, field in ((source, "bytes"), (destination, "final_bytes")):
        size = obj.get(field)
        if type(size) is not int or size < 0:
            raise AuditError(f"Invalid frozen byte count {field}: {path}")
    for field, pattern in (("final_git_blob_sha1", HEX40), ("final_sha256", HEX64)):
        value = destination.get(field)
        if not isinstance(value, str) or not pattern.fullmatch(value):
            raise AuditError(f"Invalid frozen destination {field}: {target}")
    if destination.get("final_mode") not in ("100644", "100755"):
        raise AuditError(f"Unsupported frozen destination mode: {target}")
    return path, dict(destination, path=target, source_bytes=source["bytes"])


def tree_hash(records: dict[str, tuple[str, str, str]]) -> str:
    root: dict[str, Any] = {}
    for path, (mode, blob, _) in records.items():
        parts = safe_path(path).split("/")
        node = root
        for part in parts[:-1]:
            node = node.setdefault(part, {})
            if not isinstance(node, dict):
                raise AuditError(f"File/directory conflict: {path}")
        if parts[-1] in node:
            raise AuditError(f"Duplicate or conflicting path: {path}")
        node[parts[-1]] = (mode, blob)

    def visit(node: dict[str, Any]) -> str:
        entries = []
        for name, value in node.items():
            directory = isinstance(value, dict)
            mode, blob = ("40000", visit(value)) if directory else value
            encoded = name.encode("utf-8")
            entries.append((encoded + (b"/" if directory else b""),
                            mode.encode() + b" " + encoded + b"\0" + bytes.fromhex(blob)))
        return digest("tree", b"".join(value for _, value in sorted(entries)))

    return visit(root)


def inventories(all_rows: list[list[dict[str, Any]]], expected_tree: str = SOURCE_TREE):
    maps, owners = [], []
    for rows in all_rows:
        mapping, owner = {}, {}
        for row in rows:
            path, identity = source_record(row)
            if path in mapping:
                raise AuditError(f"Duplicate inventory row: {path}")
            mapping[path] = identity
            owner[path] = row.get("agent", row.get("assigned_agent", row.get("owner")))
        if tree_hash(mapping) != expected_tree:
            raise AuditError("An inventory does not reconstruct the pinned source Git tree")
        maps.append(mapping)
        owners.append(owner)
    if not maps or any(m != maps[0] for m in maps[1:]):
        raise AuditError("Source identities disagree between inventories")
    disagreements = [p for p in sorted(maps[0]) if len({o[p] for o in owners}) != 1]
    return maps[0], disagreements


class Git:
    def __init__(self, path: Path):
        self.path = path.resolve()
        self.cache: dict[str, bytes] = {}

    def run(self, *args: str) -> bytes:
        result = subprocess.run(["git", "--no-replace-objects", "-C", str(self.path), *args],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if result.returncode:
            raise AuditError(result.stderr.decode("utf-8", "replace").strip())
        return result.stdout

    def resolve(self, ref: str) -> str:
        return self.run("rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()

    def tree(self, commit: str) -> dict[str, tuple[str, str]]:
        result = {}
        for entry in self.run("ls-tree", "-rz", "--full-tree", commit).split(b"\0"):
            if not entry:
                continue
            header, raw_path = entry.split(b"\t", 1)
            mode, kind, oid = header.decode().split()
            path = safe_path(raw_path.decode("utf-8"))
            if kind != "blob":
                raise AuditError(f"Unexpected Git entry {kind}: {path}")
            result[path] = (mode, oid)
        return result

    def blob(self, oid: str) -> bytes:
        if not HEX40.fullmatch(oid):
            raise AuditError("Invalid blob object name")
        if oid not in self.cache:
            data = self.run("cat-file", "blob", oid)
            if digest("blob", data) != oid:
                raise AuditError(f"Git blob hash mismatch: {oid}")
            self.cache[oid] = data
        return self.cache[oid]

    def rows(self, tree: dict[str, tuple[str, str]], path: str):
        if path not in tree or tree[path][0] not in ("100644", "100755"):
            raise AuditError(f"Missing regular-file manifest: {path}")
        data = self.blob(tree[path][1]).decode("utf-8")
        rows = [json.loads(line) for line in data.splitlines() if line.strip()]
        if any(not isinstance(r, dict) for r in rows):
            raise AuditError(f"Non-object manifest row: {path}")
        return rows


def publication_exclusion(path: str) -> bool:
    # Reference files stay excluded. Bibliographic Markdown is not excluded.
    return path.startswith("extracted/") or (
        path.startswith("papers/") and not path.endswith((".md", ".bib", ".json")))


def choose_copy(paths: list[str], source_path: str) -> str:
    return min(paths, key=lambda p: (p != source_path, len(p), p))


def write_replay(output: Path, files: dict[str, tuple[str, bytes]]) -> None:
    """Write a new historical source view. Refuse all existing output paths."""
    output = output.absolute()
    if output.exists() or output.is_symlink():
        raise AuditError("Replay destination must not exist")
    for parent in output.parents:
        if parent.is_symlink():
            raise AuditError("Replay destination has a symlink ancestor")
    for path, (mode, data) in files.items():
        safe_path(path)
        if mode not in ("100644", "100755") or not isinstance(data, bytes):
            raise AuditError(f"Replay only supports regular files: {path}")
    output.mkdir(parents=True, exist_ok=False)
    for path, (mode, data) in files.items():
        target = output / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(data)
        # Do not automatically make unreviewed historical scripts executable.
        target.chmod(0o644)


def audit(repo: Git, candidate: str, baseline: str = BASE,
          source_tree: str = SOURCE_TREE, expected_count: int = 4717,
          frozen_count: int = 813) -> tuple[dict[str, Any], dict[str, tuple[str, bytes]]]:
    tree, base = repo.tree(candidate), repo.tree(baseline)
    records, disagreements = inventories([repo.rows(tree, p) for p in ASSIGNMENTS], source_tree)
    if len(records) != expected_count:
        raise AuditError("Unexpected source inventory size")
    errors = []
    changed = [p for p, entry in base.items() if tree.get(p) != entry]
    if changed:
        errors.append({"baseline_files_changed": changed})
    by_blob: dict[str, list[str]] = defaultdict(list)
    for p, (mode, oid) in tree.items():
        if mode in ("100644", "100755"):
            by_blob[oid].append(p)
    frozen, frozen_seen = {}, set()
    frozen_rows = repo.rows(base, FROZEN)
    if len(frozen_rows) != frozen_count:
        errors.append({"frozen_manifest_count": len(frozen_rows), "expected": frozen_count})
    for row in frozen_rows:
        p, destination = frozen_record(row, records, source_tree)
        target = destination["path"]
        if p in frozen_seen:
            raise AuditError("Invalid or repeated frozen source path")
        frozen_seen.add(p)
        source_oid = records[p][1]
        if source_oid in by_blob:
            source_data = repo.blob(source_oid)
            if (len(source_data) != destination["source_bytes"]
                    or hashlib.sha256(source_data).hexdigest() != records[p][2]):
                raise AuditError(f"Frozen source byte identity mismatch: {p}")
        expected_entry = (destination["final_mode"], destination["final_git_blob_sha1"])
        if tree.get(target) != expected_entry or base.get(target) != expected_entry:
            errors.append({"frozen_identity_mismatch": target})
        elif (len(repo.blob(tree[target][1])) != destination["final_bytes"]
              or hashlib.sha256(repo.blob(tree[target][1])).hexdigest() != destination["final_sha256"]):
            errors.append({"frozen_hash_mismatch": target})
        else:
            frozen[p] = target
    if len(frozen) != frozen_count:
        errors.append({"frozen_verified_count": len(frozen), "expected": frozen_count})
    assigned: dict[str, list[int]] = defaultdict(list)
    for agent, manifest in enumerate(DISPOSITIONS, 1):
        for row in repo.rows(tree, manifest):
            p, identity = source_record(row)
            if records.get(p) != identity:
                raise AuditError(f"Disposition source identity mismatch: {p}")
            assigned[p].append(agent)
            target = row.get("destination_path") or row.get("destination_artifact_path")
            expected = row.get("payload_sha256") or row.get("destination_sha256")
            if row.get("preserved_destination_path"):
                target = ROOT + "agent-2/corpus/" + safe_path(row["preserved_destination_path"])
                expected = row["source_sha256"]
            if target:
                safe_path(target)
                if target not in tree or tree[target][0] not in ("100644", "100755"):
                    errors.append({"missing_disposition_target": target, "source": p})
                elif not expected or hashlib.sha256(repo.blob(tree[target][1])).hexdigest() != expected:
                    errors.append({"disposition_target_hash_mismatch": target, "source": p})
    coverage, missing, replay, duplicates = [], [], {}, []
    for p, (mode, oid, sha256) in sorted(records.items()):
        row: dict[str, Any] = {"source_path": p, "source_blob": oid,
                               "source_sha256": sha256, "source_mode": mode}
        paths = by_blob.get(oid, []) if mode != "120000" else []
        if paths:
            target = choose_copy(paths, p)
            data = repo.blob(oid)
            if hashlib.sha256(data).hexdigest() != sha256:
                raise AuditError(f"Byte SHA-256 mismatch: {p}")
            row.update(status="exact_preserved", destination=target)
            if not publication_exclusion(p):
                replay[p] = (mode, data)
            if len(paths) > 1:
                duplicates.append({"source_path": p, "destinations": sorted(paths)})
        elif p in frozen:
            row.update(status="verified_frozen_transformation", destination=frozen[p])
        elif publication_exclusion(p):
            row.update(status="reference_not_redistributed", destination=None)
        else:
            row.update(status="unresolved", destination=None)
            missing.append(row.copy())
        coverage.append(row)
    diagnostic_backlog = [p for p, (_, oid, _) in records.items()
                          if p not in frozen and not any(e[1] == oid for e in base.values())]
    unassigned = sorted(p for p in diagnostic_backlog if not assigned[p])
    report = {
        "schema_version": 1, "candidate_commit": candidate, "baseline_commit": baseline,
        "source_commit": SOURCE, "reconstructed_source_tree": tree_hash(records),
        "source_files": len(records), "coverage_counts": dict(Counter(r["status"] for r in coverage)),
        "frozen_manifest_count": len(frozen_rows), "frozen_verified_count": len(frozen),
        "ownership_disagreements": disagreements,
        "duplicate_disposition_sources": sorted(p for p, agents in assigned.items() if len(agents) > 1),
        "backlog_without_worker_disposition": unassigned, "duplicate_payloads": duplicates,
        "coverage": coverage, "missing": missing, "errors": errors,
        "source_main_preservation_passed": not missing and not errors,
        "status": "PASS_SOURCE_MAIN_ONLY" if not missing and not errors else "BLOCKED",
        "deprecation_ready": False, "release_verified": False, "mathematical_proof": False,
        "limits": ["This check does not clear branch-only or unavailable worktree obligations.",
                   "It does not grant rights, replay research certificates, or replace Gate 2.",
                   "Source-main preservation is not full-project migration completion."],
    }
    return report, replay


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay-directory", type=Path)
    args = parser.parse_args()
    try:
        repo = Git(args.repo)
        candidate = repo.resolve(args.ref)
        report, replay = audit(repo, candidate)
        output = args.output.absolute()
        if output.exists() or output.is_symlink():
            raise AuditError("Output report must not already exist")
        if output.is_relative_to(repo.path):
            raise AuditError("Write audit evidence outside the repository")
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8") as stream:
            json.dump(report, stream, indent=2, sort_keys=True)
            stream.write("\n")
        if args.replay_directory:
            if args.replay_directory.resolve().is_relative_to(repo.path):
                raise AuditError("Replay directory must be outside the repository")
            if report["missing"] or report["errors"]:
                raise AuditError("Cannot construct a replay while preservation is incomplete")
            # Modified frozen proofs must not be presented as exact old source bytes.
            if len(replay) != sum(not publication_exclusion(p) for p in
                                 (r["source_path"] for r in report["coverage"])):
                raise AuditError("Exact historical replay requires source bytes for transformed files")
            write_replay(args.replay_directory, replay)
        print(json.dumps({k: report[k] for k in ("status", "candidate_commit", "coverage_counts",
                                                "deprecation_ready", "release_verified")}, sort_keys=True))
        return 0 if report["source_main_preservation_passed"] else 1
    except (AuditError, OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"migration-union: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

