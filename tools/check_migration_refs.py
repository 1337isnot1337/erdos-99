#!/usr/bin/env python3
"""Verify known historical branch and dirty-file identities without executing them.

Exit 1 means a known captured byte identity is missing or evidence is invalid.
Unavailable worktrees without a captured path/hash are reported as separate
epistemic limits; this program cannot establish their uncommitted contents.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess


ROOT = "docs/research/migration/2026-10-16/"
EVIDENCE = ROOT + "ref-reconciliation/"
BRANCH_MANIFESTS = (
    ROOT + "agent-1/evidence/source-branches/source-branch-artifacts.jsonl",
    ROOT + "agent-2/branches/branch-file-dispositions.jsonl",
    ROOT + "agent-3/branch-dispositions.jsonl",
)
DIRTY_MANIFEST = ROOT + "agent-1/evidence/source-dirty-worktrees/source-dirty-worktree-assignments.jsonl"
CAPTURE = "f282d53169df4d507117893bfdcc99f663855923"
CAPTURE_BLOBS = {
    BRANCH_MANIFESTS[0]: "e25a79743f4f75713872540d146318015d827a69",
    BRANCH_MANIFESTS[1]: "e8b7ce8a76fd38867c09ad0ad4908f84b79e629c",
    BRANCH_MANIFESTS[2]: "e8f835ed12b4c59d2129d5fbd3c793d3e03735e9",
    DIRTY_MANIFEST: "4854bc7ba57cea323cb37f17d3441fa349b472ce",
    ROOT + "agent-1/evidence/source-remote-refs.txt": "9cb8389fd5c32762eff40811f6abbc2e7a3455f6",
    ROOT + "baseline/source-open-prs.json": "64cc656fb358754203648ffff827e0a898c29a46",
}
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")


def safe_path(path):
    if not isinstance(path, str) or not path or "\\" in path:
        raise ValueError("invalid evidence path")
    p = PurePosixPath(path)
    if p.is_absolute() or any(x in ("", ".", "..", ".git") for x in path.split("/")):
        raise ValueError("unsafe evidence path: " + path)
    return path


class Snapshot:
    def __init__(self, repo, candidate):
        self.repo = Path(repo).resolve()
        self.commit = self.git("rev-parse", "--verify", "--end-of-options", candidate + "^{commit}").decode().strip()
        self.files = {}
        self.by_blob = defaultdict(list)
        self.cache = {}
        for entry in self.git("ls-tree", "-rz", "--full-tree", self.commit).split(b"\0"):
            if not entry:
                continue
            meta, path = entry.split(b"\t", 1)
            mode, kind, oid = meta.decode().split()
            path = safe_path(path.decode())
            if kind != "blob":
                raise ValueError("unsupported snapshot entry: " + path)
            self.files[path] = (mode, oid)
            self.by_blob[oid].append(path)

    def git(self, *args):
        result = subprocess.run(["git", "--no-replace-objects", "-C", str(self.repo), *args], capture_output=True)
        if result.returncode:
            raise ValueError(result.stderr.decode("utf-8", "replace").strip())
        return result.stdout

    def blob(self, oid):
        if not HEX40.fullmatch(oid):
            raise ValueError("invalid Git blob identity")
        if oid not in self.cache:
            data = self.git("cat-file", "blob", oid)
            header = b"blob " + str(len(data)).encode() + b"\0"
            if hashlib.sha1(header + data).hexdigest() != oid:
                raise ValueError("Git blob identity mismatch: " + oid)
            self.cache[oid] = data
        return self.cache[oid]

    def read(self, path):
        path = safe_path(path)
        mode, oid = self.files[path]
        if mode not in ("100644", "100755"):
            raise ValueError("evidence must be a regular file: " + path)
        return self.blob(oid)

    def rows(self, path):
        return [json.loads(s) for s in self.read(path).decode().splitlines() if s.strip()]


def verify(snapshot):
    errors = []
    for path, blob in CAPTURE_BLOBS.items():
        if snapshot.files.get(path) != ("100644", blob):
            raise ValueError("captured migration obligations changed: " + path)
    branch_rows = []
    counts = Counter()
    for agent, manifest in enumerate(BRANCH_MANIFESTS, 1):
        for row_number, row in enumerate(snapshot.rows(manifest), 1):
            source_blob = row.get("source_git_blob_sha1") or row.get("source_blob")
            source_sha256 = row.get("source_sha256")
            source_path = safe_path(row.get("source_path") or row.get("path"))
            if not isinstance(source_blob, str) or not HEX40.fullmatch(source_blob):
                raise ValueError("invalid source blob in branch manifest")
            if not isinstance(source_sha256, str) or not HEX64.fullmatch(source_sha256):
                raise ValueError("invalid source SHA-256 in branch manifest")
            targets = sorted(snapshot.by_blob.get(source_blob, []), key=lambda p: (p != source_path, len(p), p))
            target = targets[0] if targets else None
            status = "preserved_exact_blob" if target else "missing_exact_captured_branch_blob"
            if target and hashlib.sha256(snapshot.read(target)).hexdigest() != source_sha256:
                status = "captured_source_hash_disagrees_with_blob"
            result = {
                "agent": agent, "source_manifest": manifest, "source_row": row_number,
                "source_path": source_path, "source_blob": source_blob,
                "source_sha256": source_sha256, "destination_path": target,
                "status": status, "original_disposition": row.get("disposition"),
            }
            branch_rows.append(result)
            counts[status] += 1
            if status != "preserved_exact_blob":
                errors.append(result)
    if len(branch_rows) != 1643:
        errors.append({"unexpected_branch_manifest_row_count": len(branch_rows)})

    support_rows = snapshot.rows(EVIDENCE + "branch-support-blobs.jsonl")
    for row in support_rows:
        path = safe_path(row["destination_path"])
        data = snapshot.read(path)
        if snapshot.files[path] != ("100644", row["sha"]):
            errors.append({"inert_archive_mode_or_blob_mismatch": path})
        if hashlib.sha256(data).hexdigest() != row["sha256"] or len(data) != row["bytes"]:
            errors.append({"inert_archive_sha256_or_size_mismatch": path})
    if len(support_rows) != 249 or len({r["sha"] for r in support_rows}) != 249:
        errors.append({"unexpected_historical_archive_blob_count": len(support_rows)})

    index_recipes = json.loads(snapshot.read(EVIDENCE + "dirty-index-reconstruction.json"))
    for recipe in index_recipes:
        base_path = safe_path(recipe["base_path"])
        base = snapshot.read(base_path)
        rows = [json.loads(line) for line in base.decode().splitlines()]
        common = [row for row in rows if row["path"] != recipe["remove_row_path"]]
        if snapshot.files[base_path][1] != recipe["base_blob"] or hashlib.sha256(base).hexdigest() != recipe["base_sha256"]:
            errors.append({"dirty_index_reconstruction_base_mismatch": base_path})
        if len(rows) != 1048 or len(common) != 1047:
            errors.append({"dirty_index_reconstruction_row_count_mismatch": base_path})
        added = recipe["add_row"]
        if added["artifact_id"] != "ART-" + hashlib.sha256(added["path"].encode()).hexdigest()[:12].upper():
            errors.append({"dirty_index_reconstruction_artifact_identity_mismatch": added["path"]})
        rebuilt = "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
                          for row in sorted([*common, added], key=lambda row: row["path"])).encode()
        path = safe_path(recipe["destination_path"])
        if snapshot.read(path) != rebuilt or hashlib.sha256(rebuilt).hexdigest() != recipe["source_sha256"] or len(rebuilt) != recipe["source_bytes"]:
            errors.append({"dirty_index_reconstruction_bytes_mismatch": path})
    if len(index_recipes) != 2:
        errors.append({"unexpected_dirty_index_reconstruction_count": len(index_recipes)})

    by_sha256 = defaultdict(list)
    for oid, paths in snapshot.by_blob.items():
        data = snapshot.blob(oid)
        by_sha256[hashlib.sha256(data).hexdigest()].extend(paths)
    dirty_rows, unavailable = [], []
    for row_number, row in enumerate(snapshot.rows(DIRTY_MANIFEST), 1):
        if row.get("snapshot_type") == "registered_unavailable_worktree":
            unavailable.append({
                "source_ref": row["source_ref"], "recorded_head_sha": row["recorded_head_sha"],
                "source_manifest": DIRTY_MANIFEST, "source_row": row_number,
                "captured_file_identity": None,
                "uncommitted_contents_status": "unknown_no_captured_path_or_hash",
                "recovery_claimed": False,
            })
            continue
        digest = row.get("frozen_snapshot_sha256")
        if not isinstance(digest, str) or not HEX64.fullmatch(digest):
            raise ValueError("invalid frozen dirty-file SHA-256")
        paths = sorted(by_sha256.get(digest, []), key=lambda p: (len(p), p))
        target = paths[0] if paths else None
        status = "preserved_exact_frozen_dirty_bytes" if target else "missing_known_frozen_dirty_bytes"
        if target and len(snapshot.read(target)) != row["bytes"]:
            status = "frozen_dirty_size_mismatch"
        result = {
            "source_manifest": DIRTY_MANIFEST, "source_row": row_number,
            "source_ref": row.get("source_ref"), "recorded_head_sha": row.get("recorded_head_sha"),
            "source_path": row["source_path"], "source_sha256": digest,
            "source_bytes": row["bytes"], "destination_path": target, "status": status,
            "original_capture": {"status": row.get("status"), "status_code": row.get("status_code")},
            "current_original_worktree_access": "not_established_by_frozen_capture",
        }
        dirty_rows.append(result)
        if status != "preserved_exact_frozen_dirty_bytes":
            errors.append(result)
    if len(dirty_rows) != 30 or len(unavailable) != 2:
        errors.append({"unexpected_dirty_inventory_counts": [len(dirty_rows), len(unavailable)]})

    refs = json.loads(snapshot.read(EVIDENCE + "live-ref-reconciliation.json"))
    frozen_branches = {}
    for line in snapshot.read(ROOT + "agent-1/evidence/source-remote-refs.txt").decode().splitlines():
        ref, sha = line.split()
        prefix = "refs/remotes/origin/"
        if ref.startswith(prefix) and not ref.startswith(prefix + "pr/") and ref != prefix + "HEAD":
            frozen_branches[ref.removeprefix(prefix)] = sha
    frozen_prs = {r["number"]: r["headRefOid"] for r in json.loads(snapshot.read(ROOT + "baseline/source-open-prs.json"))}
    captured_branches = {r["name"]: r["live_sha"] for r in refs["branches"]}
    captured_prs = {r["number"]: r["head_sha"] for r in refs["open_prs"]}
    if any(not HEX40.fullmatch(sha) for sha in (*captured_branches.values(), *captured_prs.values())):
        raise ValueError("invalid captured live-ref identity")
    ref_errors = [r for r in refs["branches"] if r.get("status") != "unchanged" or r["live_sha"] != r["frozen_sha"]]
    ref_errors += [r for r in refs["open_prs"] if r.get("status") != "unchanged" or r["head_sha"] != r["frozen_sha"]]
    if len(refs["branches"]) != 45 or len(refs["open_prs"]) != 21 or len(captured_branches) != 45 or len(captured_prs) != 21 or ref_errors or captured_branches != frozen_branches or captured_prs != frozen_prs:
        errors.append({"live_vs_frozen_ref_reconciliation_invalid": ref_errors})
    return {
        "schema_version": 1, "candidate_sha": snapshot.commit,
        "capture_sha": CAPTURE,
        "status": "pass" if not errors else "incomplete",
        "scope": "captured_branch_artifacts_and_frozen_dirty_file_identities",
        "branch_rows": len(branch_rows), "branch_counts": dict(counts),
        "inert_exact_historical_blobs": len(support_rows),
        "exact_dirty_indexes_reconstructed": len(index_recipes),
        "frozen_dirty_rows": len(dirty_rows),
        "frozen_dirty_counts": dict(Counter(r["status"] for r in dirty_rows)),
        "live_ref_capture": {"captured_at": refs["captured_at"], "unchanged_branches": 45, "unchanged_open_pr_heads": 21},
        "errors": errors, "branch_coverage": branch_rows, "dirty_coverage": dirty_rows,
        "unavailable_worktree_limits": unavailable,
        "known_captured_bytes_complete": not errors,
        "exhaustive_original_uncommitted_state_proven": False,
        "deprecation_ready": False,
        "deprecation_note": "This audit cannot authorize source retirement or establish unknown contents of inaccessible historical worktrees.",
        "mathematical_promotion": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--candidate", default="HEAD")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.output:
            output = Path(os.path.abspath(args.output))
            if output.is_relative_to(args.repo.resolve()):
                raise ValueError("output must be outside the audited checkout")
            if output.exists() or output.is_symlink() or any(p.is_symlink() for p in output.parents):
                raise ValueError("output must be new and have no symlink ancestors")
        report = verify(Snapshot(args.repo, args.candidate))
    except (ValueError, KeyError, UnicodeError, OSError) as error:
        report = {"status": "invalid_evidence", "error": str(error), "deprecation_ready": False}
    if args.output and report["status"] != "invalid_evidence":
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x") as stream:
            stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("branch_coverage", "dirty_coverage")}, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
