#!/usr/bin/env python3
"""Preserve Agent 3 branch-only research versions without replacing destination content."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ARCHIVE = "docs/archive/source-e99-branches"
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


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def normalized_body(data: bytes) -> bytes:
    lines = data.splitlines(keepends=True)
    while lines:
        first = lines[0]
        if first.startswith((b"<!-- theorem-state:", b"<!-- migration-provenance:")):
            lines.pop(0)
            continue
        if not first.strip() or first.startswith((b"> **Historical source snapshot", b"> **Historical branch snapshot",
                                                   b"> **Withdrawn inference", b"> **Imported source research",
                                                   b"> **Imported unreviewed source research")):
            lines.pop(0)
            continue
        break
    return b"".join(lines)


def source_index_for_commit(repo: Path, commit: str, cache: dict[str, dict[str, dict]]) -> dict[str, dict]:
    if commit not in cache:
        try:
            raw = git(repo, "show", f"{commit}:docs/state/artifact-index.jsonl")
            cache[commit] = {r["path"]: r for r in
                             (json.loads(line) for line in raw.decode().splitlines() if line.strip())}
        except subprocess.CalledProcessError:
            cache[commit] = {}
    return cache[commit]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True, help="local source repository")
    ap.add_argument("--remote-source", type=Path, required=True, help="live source mirror")
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--source-main", required=True)
    ap.add_argument("--destination-main", required=True)
    ap.add_argument("--artifacts", type=Path, required=True)
    ap.add_argument("--commit-ledger", type=Path, required=True)
    ap.add_argument("--branch-heads", type=Path, required=True)
    ap.add_argument("--main-dispositions", type=Path, required=True)
    ap.add_argument("--main-allocation", type=Path, required=True)
    ap.add_argument("--existing-main-ledger", type=Path, required=True)
    ap.add_argument("--frozen-index", type=Path, required=True)
    ap.add_argument("--frozen-dispositions", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--materialize", action="store_true")
    args = ap.parse_args()

    source_main_tree = tree(args.source, args.source_main)
    dest_tree = tree(args.destination, args.destination_main)
    dest_blob_paths: dict[str, list[str]] = defaultdict(list)
    for path, oid in dest_tree.items():
        dest_blob_paths[oid].append(path)
    commit_rows = {r["commit"]: r for r in
                   (json.loads(line) for line in args.commit_ledger.read_text().splitlines() if line.strip())}
    main_dispositions = {r["source_path"]: r for r in
                         (json.loads(line) for line in args.main_dispositions.read_text().splitlines() if line.strip())}
    main_allocation = {r["source_path"]: r for r in
                       (json.loads(line) for line in args.main_allocation.read_text().splitlines() if line.strip())}
    existing_main = {}
    for record in (json.loads(line) for line in args.existing_main_ledger.read_text().splitlines() if line.strip()):
        if record.get("original_path") and record.get("source_git_blob_sha"):
            existing_main[(record["original_path"], record["source_git_blob_sha"])] = record
    frozen_index = {r["path"]: r for r in
                    (json.loads(line) for line in args.frozen_index.read_text().splitlines() if line.strip())}
    frozen_dispositions = {r.get("source", {}).get("path"): r for r in
                           (json.loads(line) for line in args.frozen_dispositions.read_text().splitlines() if line.strip())}
    artifacts = [json.loads(line) for line in args.artifacts.read_text().splitlines() if line.strip()]
    agent3_heads = [json.loads(line) for line in args.branch_heads.read_text().splitlines()
                    if line.strip() and json.loads(line).get("owner") == 3
                    and json.loads(line).get("unaccounted_commit_count", 0) > 0]
    head_paths: dict[tuple[str, str], list[str]] = defaultdict(list)
    tree_cache: dict[tuple[str, str], dict[str, str]] = {}
    for head in agent3_heads:
        repo = args.source if head["origin"] == "local" else args.remote_source
        key = (str(repo), head["head"])
        if key not in tree_cache:
            tree_cache[key] = tree(repo, head["head"])
        for path, oid in tree_cache[key].items():
            head_paths[(path, oid)].append(head["refname"])

    # An active path receives only a branch version that still exists at an
    # Agent 3 non-PR branch head. Earlier versions remain in a commit-specific archive.
    active_candidates: dict[str, list[dict]] = defaultdict(list)
    for row in artifacts:
        if row["source_relation"] != "branch_only_content":
            continue
        live_refs = sorted(set(head_paths.get((row["source_path"], row["source_blob"]), [])))
        existing_path = args.destination / row["source_path"]
        previously_materialized = False
        if existing_path.is_file():
            existing = existing_path.read_bytes()
            previously_materialized = (sha(existing) == row["source_sha256"] or
                                       (b'"source_blob": "' + row["source_blob"].encode() + b'"') in existing[:4096])
        if live_refs and row["source_path"] not in dest_tree and (not existing_path.exists() or previously_materialized):
            row["live_agent3_head_refs"] = live_refs
            active_candidates[row["source_path"]].append(row)
    selected_active: dict[tuple[str, str], str] = {}
    for path, choices in active_candidates.items():
        def sort_key(row: dict) -> tuple[str, str, str]:
            commit = row["introduced_or_deleted_by"][-1]
            meta = commit_rows.get(commit, {})
            return (meta.get("author_date") or "", meta.get("primary_refname") or "", row["source_blob"])
        chosen = max(choices, key=sort_key)
        selected_active[(chosen["source_path"], chosen["source_blob"])] = sort_key(chosen)[1]

    idx_cache: dict[str, dict[str, dict]] = {}
    out_rows = []
    copied = []
    for row in artifacts:
        p, oid = row["source_path"], row["source_blob"]
        commits = row["introduced_or_deleted_by"]
        newest = max(commits, key=lambda c: commit_rows.get(c, {}).get("author_date") or "") if commits else None
        meta = commit_rows.get(newest, {}) if newest else {}
        source_repo = args.source
        content = git(source_repo, "cat-file", "blob", oid)
        out = {**row,
               "source_repository": "https://github.com/1337isnot1337/e-99",
               "source_commit": newest,
               "source_commit_author": meta.get("author"),
               "source_commit_author_date": meta.get("author_date"),
               "source_commit_subject": meta.get("subject"),
               "source_artifact_index_entry": source_index_for_commit(args.source, newest, idx_cache).get(p) if newest else None,
               "destination_path": None,
               "destination_sha256": None,
               "destination_git_blob_sha1": None,
               "source_body_sha256": None,
               "destination_body_sha256": None,
               "destination_bytes": None,
               "transformations": [],
               "authority_note": "Branch lifecycle is provenance only. Destination theorem state remains authoritative; no canonical theorem or status is promoted."}
        if row["source_relation"] in ("exact_destination_content_copy", "exact_source_main_content_copy"):
            if row["source_relation"] == "exact_source_main_content_copy" and p in main_allocation:
                alloc = main_allocation[p]
                if alloc.get("owner") in (1, 2):
                    out["disposition"] = f"deduplicated_source_main_allocated_to_agent_{alloc['owner']}"
                    out["source_main_owner"] = alloc["owner"]
                    out["source_main_unit_key"] = alloc.get("unit_key")
                    out["reason"] = "This branch blob is an exact source-main copy, and the source-main content is independently assigned to the recorded sibling shard; no branch duplicate is imported."
                elif alloc.get("owner") == 3 and p in main_dispositions:
                    main_row = main_dispositions[p]
                    dest_path = main_row.get("destination_artifact_path")
                    dest_file = args.destination / dest_path if dest_path else None
                    if dest_file and dest_file.is_file():
                        dest_data = dest_file.read_bytes()
                    elif dest_path in dest_tree:
                        dest_data = git(args.destination, "show", f"{args.destination_main}:{dest_path}")
                    else:
                        dest_data = None
                    source_text = normalized_body(content) if p.lower().endswith(".md") else content
                    dest_text = normalized_body(dest_data) if dest_data is not None and p.lower().endswith(".md") else dest_data
                    if (main_row.get("source_blob") == oid and dest_data is not None
                            and source_text == dest_text):
                        out["disposition"] = "exact_source_main_body_migrated_by_source_main"
                        out["destination_path"] = dest_path
                        out["destination_sha256"] = main_row.get("destination_sha256")
                        out["destination_git_blob_sha1"] = main_row.get("destination_git_blob_sha1")
                        out["destination_bytes"] = main_row.get("destination_bytes")
                        out["source_body_sha256"] = sha(source_text)
                        out["destination_body_sha256"] = sha(dest_text)
                        out["reason"] = "Exact source-main Git blob is already preserved by Agent 3's source-main migration; its transformed destination body is checked and no branch duplicate is imported."
                    else:
                        out["disposition"] = "unresolved_source_main_duplicate_mapping"
                        out["reason"] = "Branch blob matches an Agent 3 source-main allocation, but its destination body did not match the recorded source-main receipt."
                elif alloc.get("frozen_set_member"):
                    frozen = frozen_index.get(p)
                    frozen_receipt = frozen_dispositions.get(p)
                    dest = frozen_receipt.get("destination", {}) if frozen_receipt else {}
                    dest_path = dest.get("path") or (frozen.get("proposed_destination") if frozen else None)
                    dest_sha = dest.get("final_sha256")
                    dest_blob = dest.get("final_git_blob_sha1")
                    if (dest_path and dest_sha and (args.destination / dest_path).is_file()
                            and sha((args.destination / dest_path).read_bytes()) == dest_sha):
                        out["disposition"] = "deduplicated_existing_frozen_report_migration"
                        out["destination_path"] = dest_path
                        out["destination_sha256"] = dest_sha
                        out["destination_git_blob_sha1"] = dest_blob
                        out["reason"] = "This exact source-main report is already covered by the verified frozen Target C migration set; its existing receipt is reused and no duplicate is imported."
                    else:
                        out["disposition"] = "unresolved_frozen_report_mapping"
                        out["reason"] = "Frozen report receipt exists, but its recorded destination artifact is not present with the recorded hash at this baseline."
                elif (p, oid) in existing_main:
                    prior = existing_main[(p, oid)]
                    dest_path = prior.get("public_path") or prior.get("proposed_destination")
                    dest_blob = dest_tree.get(dest_path) if dest_path else None
                    if dest_path and dest_blob and prior.get("public_sha256"):
                        out["disposition"] = "deduplicated_existing_migration_record"
                        out["destination_path"] = dest_path
                        out["destination_sha256"] = prior["public_sha256"]
                        out["destination_git_blob_sha1"] = dest_blob
                        out["source_body_sha256"] = sha(normalized_body(content)) if p.lower().endswith(".md") else sha(content)
                        out["destination_bytes"] = int(prior.get("public_bytes") or 0) or None
                        out["reason"] = "This exact source-main Git blob has an integrity-recorded destination transformation in the frozen migration ledger, present at this baseline; no branch duplicate is imported."
                    else:
                        out["disposition"] = "unresolved_existing_migration_record_mapping"
                        out["reason"] = "A source-main ledger record matches this blob, but its recorded destination path/blob is absent at the pinned destination baseline."
                else:
                    out["disposition"] = "unresolved_source_main_duplicate_mapping"
                    out["reason"] = "The branch blob matches pinned source main, but no source-main allocation or destination mapping was found."
            elif row["source_relation"] == "exact_source_main_content_copy" and p in main_dispositions:
                main_row = main_dispositions[p]
                dest_path = main_row.get("destination_artifact_path")
                dest_file = args.destination / dest_path if dest_path else None
                if dest_file and dest_file.is_file():
                    dest_data = dest_file.read_bytes()
                elif dest_path in dest_tree:
                    dest_data = git(args.destination, "show", f"{args.destination_main}:{dest_path}")
                else:
                    dest_data = None
                source_text = normalized_body(content) if p.lower().endswith(".md") else content
                dest_text = normalized_body(dest_data) if dest_data is not None and p.lower().endswith(".md") else dest_data
                if dest_data is not None and source_text == dest_text:
                    out["disposition"] = "exact_source_main_body_migrated_by_source_main"
                    out["destination_path"] = dest_path
                    out["destination_sha256"] = main_row.get("destination_sha256")
                    out["destination_git_blob_sha1"] = main_row.get("destination_git_blob_sha1")
                    out["destination_bytes"] = main_row.get("destination_bytes")
                    out["source_body_sha256"] = sha(source_text)
                    out["destination_body_sha256"] = sha(dest_text)
                    out["reason"] = "Exact source-main Git blob is already preserved by Agent 3's source-main migration; its transformed destination body is checked and no branch duplicate is imported."
                else:
                    out["disposition"] = "unresolved_source_main_duplicate_mapping"
                    out["reason"] = "Branch blob is identical to pinned source main, but the Agent 3 source-main destination body could not be matched."
            elif row["source_relation"] == "exact_source_main_content_copy" and (p, oid) in existing_main:
                prior = existing_main[(p, oid)]
                dest_path = prior.get("public_path") or prior.get("proposed_destination")
                dest_blob = dest_tree.get(dest_path) if dest_path else None
                if dest_path and dest_blob and prior.get("public_sha256"):
                    out["disposition"] = "deduplicated_existing_migration_record"
                    out["destination_path"] = dest_path
                    out["destination_sha256"] = prior["public_sha256"]
                    out["destination_git_blob_sha1"] = dest_blob
                    out["source_body_sha256"] = sha(normalized_body(content)) if p.lower().endswith(".md") else sha(content)
                    out["destination_bytes"] = int(prior.get("public_bytes") or 0) or None
                    out["reason"] = ("This exact source-main Git blob already has an integrity-recorded destination transformation in the frozen migration ledger; "
                                     "that disposition is reused and no branch duplicate is imported.")
                else:
                    out["disposition"] = "unresolved_existing_migration_record_mapping"
                    out["reason"] = "A source-main ledger record matches the source blob, but its recorded destination path/blob is absent at the pinned destination baseline."
            elif row["source_relation"] == "exact_source_main_content_copy" and p in main_allocation:
                alloc = main_allocation[p]
                frozen = frozen_index.get(p)
                frozen_receipt = frozen_dispositions.get(p)
                if alloc.get("frozen_set_member") and frozen and frozen_receipt:
                    dest = frozen_receipt.get("destination", {})
                    dest_path = dest.get("path") or frozen.get("proposed_destination")
                    dest_sha = dest.get("final_sha256")
                    dest_blob = dest.get("final_git_blob_sha1")
                    if dest_path and dest_sha and (args.destination / dest_path).is_file():
                        out["disposition"] = "deduplicated_existing_frozen_report_migration"
                        out["destination_path"] = dest_path
                        out["destination_sha256"] = dest_sha
                        out["destination_git_blob_sha1"] = dest_blob
                        out["reason"] = "This exact source-main report is already covered by the verified frozen Target C migration set; its existing receipt is reused and no duplicate is imported."
                    else:
                        out["disposition"] = "unresolved_frozen_report_mapping"
                        out["reason"] = "Frozen report index entry exists but its recorded destination artifact is absent."
                elif alloc.get("owner") in (1, 2):
                    out["disposition"] = f"deduplicated_source_main_allocated_to_agent_{alloc['owner']}"
                    out["source_main_owner"] = alloc["owner"]
                    out["source_main_unit_key"] = alloc.get("unit_key")
                    out["reason"] = "This branch blob is an exact source-main copy, and the source-main content is independently assigned to the recorded sibling shard; no branch duplicate is imported."
                elif alloc.get("frozen_set_member"):
                    out["disposition"] = "deduplicated_frozen_report_migration"
                    out["reason"] = "This exact source-main report belongs to the verified frozen Target C set; the existing frozen report ledger remains authoritative."
                else:
                    out["disposition"] = "unresolved_source_main_duplicate_mapping"
                    out["reason"] = "The branch blob matches pinned source main, but no destination, frozen-set, or sibling-shard mapping was found."
            else:
                out["disposition"] = "exact_destination_content_duplicate"
                out["destination_path"] = row["destination_identical_blob_paths"][0] if row["destination_identical_blob_paths"] else p
                out["destination_sha256"] = row["source_sha256"]
                out["destination_git_blob_sha1"] = oid
                out["reason"] = "Exact Git blob is already present in destination main; no duplicate is imported."
            out_rows.append(out)
            continue

        # Compare proof text independent of source theorem-state comments when
        # the active destination contains the same body under transformed metadata.
        dest_same_path = dest_tree.get(p)
        if dest_same_path and p.lower().endswith(".md"):
            dest_data = git(args.destination, "cat-file", "blob", dest_same_path)
            if normalized_body(content) == normalized_body(dest_data):
                out["disposition"] = "exact_destination_body_duplicate"
                out["destination_path"] = p
                out["destination_sha256"] = sha(dest_data)
                out["destination_git_blob_sha1"] = dest_same_path
                out["source_body_sha256"] = sha(normalized_body(content))
                out["destination_body_sha256"] = sha(normalized_body(dest_data))
                out["reason"] = "The exact mathematical body already exists at this destination path after removing generated theorem-state/provenance metadata."
                out_rows.append(out)
                continue

        if p.lower().endswith(".md"):
            lines = content.splitlines(keepends=True)
            if lines and lines[0].startswith(b"<!-- theorem-state:"):
                out["source_theorem_state_header"] = lines.pop(0).decode("utf-8", "replace").rstrip("\r\n")
                content = b"".join(lines)
                out["transformations"].append("removed_source_theorem_state_header")
            out["source_body_sha256"] = sha(content)
        else:
            out["source_body_sha256"] = sha(content)

        withdrawn = bool(RATE_OR_INVERSE.search(content))
        active = (p, oid) in selected_active
        if row["source_relation"] in ("same_path_destination_conflict", "same_path_source_main_conflict") or withdrawn or not active:
            branch_tag = (row["primary_branch_refs"][0].removeprefix("refs/heads/")
                          if row["primary_branch_refs"] else "unmapped")
            commit_tag = newest[:12] if newest else oid[:12]
            target = f"{ARCHIVE}/{branch_tag}/commits/{commit_tag}/{p}"
            if p.lower().endswith(".md"):
                target += ".source"
            out["disposition"] = "preserved_historical_branch_snapshot"
            if row["source_relation"] in ("same_path_destination_conflict", "same_path_source_main_conflict"):
                out["reason"] = "Pinned destination or source main has different content at this path; the current main version remains and branch history is archived."
            elif withdrawn:
                out["reason"] = "Withdrawn inverse-phase or unsupported rate text remains only as historical source evidence with an explicit warning."
            else:
                out["reason"] = "This unique branch version is superseded or absent from current Agent 3 branch heads; preserved as history, not selected as current branch content."
            if p.lower().endswith(".md"):
                marker = {"source_repository": "https://github.com/1337isnot1337/e-99",
                          "source_branch_refs": row["primary_branch_refs"], "source_commit": newest,
                          "source_path": p, "source_blob": oid, "source_sha256": row["source_sha256"],
                          "source_lifecycle": (out.get("source_artifact_index_entry") or {}).get("status", "not indexed"),
                          "destination_status": "historical_unreviewed_noncanonical"}
                warning = ("> **Historical branch snapshot; destination authority remains current.** " + out["reason"] + "\n\n")
                if withdrawn:
                    warning += ("> **Withdrawn inference warning:** do not use the global `K'/D`-Lipschitz inverse-phase conclusion "
                                "or `q=O(D^(4/5))` rate as a premise.\n\n")
                content = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n" + warning).encode() + content
                out["transformations"].append("added_historical_nonpromotion_notice")
        else:
            target = p
            out["disposition"] = "preserved_current_unreviewed_branch_artifact"
            out["reason"] = "This exact first-party artifact remains at an Agent 3 owned non-PR branch head and has no destination path conflict."
            if p.lower().endswith(".md"):
                marker = {"source_repository": "https://github.com/1337isnot1337/e-99",
                          "source_branch_refs": row.get("live_agent3_head_refs", row["primary_branch_refs"]),
                          "source_commit": newest, "source_path": p, "source_blob": oid,
                          "source_sha256": row["source_sha256"],
                          "source_lifecycle": (out.get("source_artifact_index_entry") or {}).get("status", "not indexed"),
                          "destination_status": "unreviewed_noncanonical"}
                content = ("<!-- migration-provenance: " + json.dumps(marker, sort_keys=True) + " -->\n\n" +
                           "> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.\n\n").encode() + content
                out["transformations"].append("added_source_provenance_and_nonpromotion_notice")
        out["destination_path"] = target
        out["destination_sha256"] = sha(content)
        out["destination_git_blob_sha1"] = git_blob(content)
        out["destination_body_sha256"] = sha(normalized_body(content) if p.lower().endswith(".md") else content)
        out["destination_bytes"] = len(content)
        if args.materialize:
            target_path = args.destination / target
            if target_path.exists() and target_path.read_bytes() != content:
                target = target + ".agent3-" + row["source_sha256"][:12]
                out["destination_path"] = target
                out["transformations"].append("collision_avoided_with_source_sha256_suffix")
                target_path = args.destination / target
            target_path.parent.mkdir(parents=True, exist_ok=True)
            if target_path.exists():
                if target_path.read_bytes() != content:
                    raise RuntimeError(f"refusing to overwrite nonidentical existing path {target}")
            else:
                target_path.write_bytes(content)
        copied.append(out)
        out_rows.append(out)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in out_rows))
    summary = {
        "branch_file_version_count": len(artifacts),
        "disposition_counts": dict(Counter(r["disposition"] for r in out_rows)),
        "materialized_file_count": len(copied),
        "materialized_bytes": sum(r.get("destination_bytes", 0) for r in copied),
        "active_branch_artifact_count": sum(r["disposition"] == "preserved_current_unreviewed_branch_artifact" for r in out_rows),
        "historical_snapshot_count": sum(r["disposition"] == "preserved_historical_branch_snapshot" for r in out_rows),
    }
    (args.output.parent / "source-branch-disposition-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
