#!/usr/bin/env python3
"""Preserve the four Agent 3 source PRs with exact per-file dispositions."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


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


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--prs-dir", type=Path, required=True)
    ap.add_argument("--destination-main", required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--materialize", action="store_true")
    args = ap.parse_args()

    dest_tree = tree(args.destination, args.destination_main)
    dest_by_blob: dict[str, list[str]] = {}
    for path, oid in dest_tree.items():
        dest_by_blob.setdefault(oid, []).append(path)
    output_rows = []
    copied = []
    shared_metadata_diffs = []
    for number in (953, 966, 967, 969):
        info = json.loads((args.prs_dir / f"pr-{number}.json").read_text())
        refs = json.loads((args.prs_dir / f"pr-{number}-refs.json").read_text())
        head, base = refs["head_sha"], refs["base_sha"]
        head_tree = tree(args.source, head)
        index = {}
        index_path = "docs/state/artifact-index.jsonl"
        if index_path in head_tree:
            idx_bytes = git(args.source, "cat-file", "blob", head_tree[index_path])
            index = {r["path"]: r for r in
                     (json.loads(line) for line in idx_bytes.decode().splitlines() if line.strip())}
        for file in info["files"]:
            path = file["path"]
            oid = head_tree.get(path)
            data = git(args.source, "cat-file", "blob", oid) if oid else b""
            dest_oid = dest_tree.get(path)
            identical_paths = sorted(dest_by_blob.get(oid, [])) if oid else []
            row = {
                "source_pr": number,
                "pr_title": info["title"],
                "pr_url": info["url"],
                "source_ref": info["headRefName"],
                "source_head": head,
                "source_base": base,
                "source_path": path,
                "source_blob": oid,
                "source_sha256": sha(data) if oid else None,
                "source_bytes": len(data) if oid else 0,
                "source_artifact_index_entry": index.get(path),
                "destination_baseline": args.destination_main,
                "destination_same_path_blob": dest_oid,
                "destination_identical_blob_paths": identical_paths,
                "destination_same_path_relation": "absent" if not dest_oid else
                    "identical" if oid and dest_oid == oid else "different",
                "additions": file.get("additions"),
                "deletions": file.get("deletions"),
                "destination_path": None,
                "destination_sha256": None,
                "destination_git_blob_sha1": None,
                "source_body_sha256": None,
                "destination_body_sha256": None,
                "transformations": [],
            }
            if path == index_path:
                row["disposition"] = "exclude_source_claim_registry_change"
                row["reason"] = "The source PR adds lifecycle metadata only; the exact row is embedded in this ledger and the shared destination registry remains unchanged."
            elif path.endswith("README.md"):
                row["disposition"] = "exclude_shared_research_navigation_change"
                row["reason"] = "The PR changes a shared navigation file; destination navigation is preserved and relevant reproduction links are recorded in the Agent 3 migration index."
                base_blob = git(args.source, "rev-parse", f"{base}:{path}")
                patch = git(args.source, "diff", "--no-ext-diff", "--unified=3", base, head, "--", path)
                shared_metadata_diffs.append((number, path, patch))
                row["source_base_blob"] = base_blob.decode().strip()
                row["source_change_diff_sha256"] = sha(patch)
            elif oid and dest_oid == oid:
                row["disposition"] = "exact_destination_duplicate"
                row["reason"] = "The exact source PR blob already exists at the same path on destination main."
                row["destination_path"] = path
                row["destination_sha256"] = row["source_sha256"]
                row["destination_git_blob_sha1"] = dest_oid
            elif oid and oid in dest_by_blob:
                row["disposition"] = "exact_destination_duplicate_at_other_path"
                row["reason"] = "The exact source PR blob already exists at a different destination path."
                row["destination_path"] = identical_paths[0]
                row["destination_sha256"] = row["source_sha256"]
                row["destination_git_blob_sha1"] = oid
            elif oid and path in dest_tree:
                row["disposition"] = "preserve_historical_conflict_snapshot"
                row["reason"] = "Destination main has different bytes at this path; its current correction is retained, and this PR version is preserved under a source-specific archive path."
                target = f"docs/archive/source-e99-pr-{number}-{head[:8]}/{path}"
                if path.lower().endswith(".md"):
                    target += ".source"
                if data.startswith(b"<!-- theorem-state:"):
                    lines = data.splitlines(keepends=True)
                    row["source_theorem_state_header"] = lines[0].decode("utf-8", "replace").rstrip("\r\n")
                    body = b"".join(lines[1:])
                    row["source_body_sha256"] = sha(body)
                    data = body
                    row["transformations"].append("removed_source_theorem_state_header")
                else:
                    row["source_body_sha256"] = sha(data)
                row["destination_body_sha256"] = sha(data)
                marker = {"source_repository": "https://github.com/1337isnot1337/e-99",
                          "source_pr": number, "source_head": head, "source_path": path,
                          "source_blob": oid, "source_sha256": row["source_sha256"],
                          "destination_status": "historical_unreviewed_noncanonical"}
                if path.lower().endswith(".md"):
                    data = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n" +
                            f"> **Historical PR snapshot; destination version retained.** PR #{number} remains an unreviewed source candidate.\n\n").encode() + data
                    row["transformations"].append("added_historical_nonpromotion_notice")
                row["destination_path"] = target
                row["destination_sha256"] = sha(data)
                row["destination_git_blob_sha1"] = git_blob(data)
                row["destination_bytes"] = len(data)
                if args.materialize:
                    target_path = args.destination / target
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    if target_path.exists():
                        raise RuntimeError(f"refusing to overwrite {target}")
                    target_path.write_bytes(data)
                copied.append((row, data))
            elif oid:
                row["disposition"] = "preserve_new_first_party_mathematical_artifact"
                row["reason"] = "No exact destination copy exists; the report, verifier, certificate, or run record is copied while remaining unreviewed and noncanonical."
                target = path
                if data.startswith(b"<!-- theorem-state:"):
                    lines = data.splitlines(keepends=True)
                    row["source_theorem_state_header"] = lines[0].decode("utf-8", "replace").rstrip("\r\n")
                    body = b"".join(lines[1:])
                    row["source_body_sha256"] = sha(body)
                    data = body
                    row["transformations"].append("removed_source_theorem_state_header")
                else:
                    row["source_body_sha256"] = sha(data)
                marker = {"source_repository": "https://github.com/1337isnot1337/e-99",
                          "source_pr": number, "source_head": head, "source_path": path,
                          "source_blob": oid, "source_sha256": row["source_sha256"],
                          "source_lifecycle": (index.get(path) or {}).get("status", "not indexed"),
                          "destination_status": "unreviewed_noncanonical"}
                if path.lower().endswith(".md"):
                    body = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n" +
                            f"> **Imported unreviewed source research.** PR #{number} is not a theorem promotion; current destination theorem state remains authoritative.\n\n").encode() + data
                    row["transformations"].append("added_source_provenance_and_nonpromotion_notice")
                    row["destination_body_sha256"] = sha(data)
                    data = body
                else:
                    row["destination_body_sha256"] = sha(data)
                row["destination_path"] = target
                row["destination_sha256"] = sha(data)
                row["destination_git_blob_sha1"] = git_blob(data)
                row["destination_bytes"] = len(data)
                if args.materialize:
                    target_path = args.destination / target
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    if target_path.exists():
                        raise RuntimeError(f"refusing to overwrite {target}")
                    target_path.write_bytes(data)
                copied.append((row, data))
            else:
                row["disposition"] = "deleted_at_pr_head"
                row["reason"] = "No file blob exists at the exact PR head; deletion is recorded without copying."
            row["authority_note"] = "Source PR status is provenance only. Level I remains open; no canonical theorem state or source lifecycle is promoted."
            output_rows.append(row)

        # Save the source artifact-index additions as narrow provenance evidence,
        # without changing the destination's shared registry.
        additions = [r for r in index.values() if r.get("path") in {f["path"] for f in info["files"]}]
        (args.output.parent / f"pr-{number}-source-index-entries.jsonl").write_text(
            "".join(json.dumps(r, sort_keys=True) + "\n" for r in additions))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in output_rows))
    patch_out = args.output.parent / "pr-shared-metadata-diffs.patch"
    patch_out.write_bytes(b"".join(b"\n" + f"# PR {n} {p}\n".encode() + patch for n, p, patch in shared_metadata_diffs))
    summary = {
        "pr_numbers": [953, 966, 967, 969],
        "changed_artifact_count": len(output_rows),
        "dispositions": dict(Counter(r["disposition"] for r in output_rows)),
        "materialized_file_count": len(copied),
        "materialized_bytes": sum(len(data) for _, data in copied),
        "shared_metadata_diff_sha256": sha(patch_out.read_bytes()),
    }
    (args.output.parent / "pr-disposition-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
