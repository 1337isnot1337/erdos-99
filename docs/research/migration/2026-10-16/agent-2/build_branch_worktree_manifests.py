#!/usr/bin/env python3
"""Partition and reconcile source branch heads and frozen dirty worktree paths.

This only reads the source repositories/worktrees. It emits full branch-head
and worktree-path assignments, residual branch-file dispositions, and copies
recoverable Agent 2 first-party artifacts into the private migration archive.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import subprocess


SOURCE_MAIN = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
DESTINATION_MAIN = "c6e0394b3152d21075328bf4f26e6c070229bf13"


def run(*args: str, input_bytes: bytes | None = None) -> bytes:
    return subprocess.check_output(list(args), input=input_bytes)


def git(repo: str, *args: str) -> bytes:
    return run("git", "-C", repo, *args)


def jsonl(path: pathlib.Path) -> list[dict]:
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def git_tree(repo: str, rev: str) -> dict[str, tuple[str, str]]:
    result = {}
    for item in git(repo, "ls-tree", "-r", "-z", rev).split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        if kind == "blob":
            result[raw_path.decode("utf-8", "surrogateescape")] = (mode, oid)
    return result


def ref_remainder(refname: str) -> int:
    return int.from_bytes(hashlib.sha256(refname.encode("utf-8")).digest(), "big") % 3


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def preserved_class(path: str) -> tuple[str, str]:
    if path.startswith("extracted/") or (path.startswith("papers/") and path.lower().endswith(".pdf")):
        return "excluded_third_party_source", "third-party scans, extracted paper text, and PDFs are not copied without redistribution rights"
    if path.startswith("docs/state/") or path == "docs/STATE.md":
        return "excluded_coordinator_owned_state", "source state and registries are recorded as provenance only"
    if path.startswith((".github/", "tools/", "scripts/", "tests/", "docs/ci/", "docs/launch/", "docs/maintenance/", "research-packages/")):
        return "excluded_repository_or_operations_material", "source workflow, test, release, or operations infrastructure is not mathematical payload"
    if path in {".editorconfig", ".gitignore", "AGENTS.md", "CONTRIBUTING.md", "README.md", "autoresearch.md", "docs/README.md", "docs/COORDINATION.md", "docs/MAINTENANCE.md", "docs/RESEARCH_WORKFLOW.md", "docs/START_HERE.md", "docs/KNOWLEDGE_MAP.md"}:
        return "excluded_superseded_navigation_or_policy", "destination has independent current instructions and navigation"
    if path == "research/cleanup/slot2-8f-ref-artifact-map-2026-10-05.tsv":
        return "excluded_migration_operations_metadata", "cleanup/artifact-map bookkeeping is not mathematical evidence"
    if path == "docs/archive/homelab_audit_history_v1.7.0.md":
        return "excluded_unrelated_private_operational_history", "outside Erdős #99 research preservation"
    if path.startswith("research/") or path.startswith(("docs/reports/", "docs/audits/", "docs/targets/", "docs/canonical/", "docs/problem/", "docs/prompts/")):
        return "preserved_first_party_research", "source branch/worktree mathematics or first-party research context; retained as noncanonical evidence"
    if path in {"docs/bibliography.bib", "papers/README.md", "papers/primary/README.md", "papers/related/README.md", "papers/supplementary/README.md"}:
        return "preserved_bibliographic_metadata", "citation metadata only; no paper body is copied"
    return "excluded_nonresearch_source_file", "not a first-party mathematical proof, research result, or required verifier dependency"


def archived_path(root: pathlib.Path, group: pathlib.Path, original: str) -> pathlib.Path:
    target = root / group / pathlib.PurePosixPath(original)
    if target.suffix.lower() == ".md":
        target = target.with_name(target.name + ".source")
    return target


def preserve_blob(repo: str, oid: str, output: pathlib.Path, expected_sha256: str | None = None) -> str:
    data = git(repo, "cat-file", "blob", oid)
    sha = hashlib.sha256(data).hexdigest()
    if expected_sha256 and sha != expected_sha256:
        raise RuntimeError(f"source blob SHA256 mismatch for {output}")
    if output.exists():
        if hashlib.sha256(output.read_bytes()).hexdigest() != sha:
            raise RuntimeError(f"refusing to overwrite {output}")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        output.chmod(0o644)
    return sha


def preserve_bytes(data: bytes, output: pathlib.Path, expected_sha256: str) -> str:
    sha = hashlib.sha256(data).hexdigest()
    if sha != expected_sha256:
        raise RuntimeError(f"worktree SHA256 mismatch for {output}")
    if output.exists():
        if hashlib.sha256(output.read_bytes()).hexdigest() != sha:
            raise RuntimeError(f"refusing to overwrite {output}")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        output.chmod(0o644)
    return sha


def write_jsonl(path: pathlib.Path, rows: list[dict]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, sort_keys=True, separators=(",", ":")) + "\n" for r in rows))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source", required=True)
    p.add_argument("--destination", required=True)
    p.add_argument("--open-prs", type=pathlib.Path, required=True)
    p.add_argument("--worktree-audit", type=pathlib.Path, required=True)
    p.add_argument("--output-root", type=pathlib.Path, required=True)
    args = p.parse_args()

    if git(args.source, "rev-parse", SOURCE_MAIN + "^{commit}").decode().strip() != SOURCE_MAIN:
        raise SystemExit("pinned source main mismatch")
    if git(args.destination, "rev-parse", DESTINATION_MAIN + "^{commit}").decode().strip() != DESTINATION_MAIN:
        raise SystemExit("pinned destination main mismatch")

    local_refs = {
        ref: oid
        for ref, oid in (line.split("\t") for line in git(args.source, "for-each-ref", "--format=%(refname)%09%(objectname)", "refs/heads").decode().splitlines())
    }
    remote_rows = run("git", "ls-remote", "https://github.com/1337isnot1337/e-99.git", "refs/heads/*").decode().splitlines()
    remote_refs = {ref: oid for oid, ref in (line.split("\t") for line in remote_rows)}
    sources: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    for ref, oid in local_refs.items():
        sources[(ref, oid)].add("local_source_cache")
    for ref, oid in remote_refs.items():
        sources[(ref, oid)].add("live_remote_advertised")

    prs = json.loads(args.open_prs.read_text())
    pr_by_head = {pr["headRefOid"]: pr for pr in prs}
    source_tree = git_tree(args.source, SOURCE_MAIN)
    destination_tree = git_tree(args.destination, DESTINATION_MAIN)
    source_blob_oids = {oid for _, oid in source_tree.values()}
    destination_blob_oids = {oid for _, oid in destination_tree.values()}
    open_pr_blob_oids: set[str] = set()
    pr_trees: dict[str, dict[str, tuple[str, str]]] = {}
    for pr in prs:
        head = pr["headRefOid"]
        try:
            tree = git_tree(args.source, head)
        except subprocess.CalledProcessError as exc:
            raise SystemExit(f"open PR head unavailable locally; fetch in isolated source store: #{pr['number']} {head}") from exc
        pr_trees[head] = tree
        open_pr_blob_oids.update(oid for _, oid in tree.values())

    branch_rows: list[dict] = []
    residual_rows: list[dict] = []
    per_head = []
    saved_blobs: dict[str, str] = {}
    for (ref, head), scopes in sorted(sources.items()):
        mod = ref_remainder(ref)
        owner = mod + 1
        q = git(args.source, "rev-list", "--count", SOURCE_MAIN + ".." + head).decode().strip()
        ahead_count = int(q)
        ahead = ahead_count > 0
        pr = pr_by_head.get(head)
        belongs = ahead and pr is None
        row = {
            "full_refname": ref,
            "head_sha": head,
            "observed_in": sorted(scopes),
            "ahead_commits_from_pinned_source_main": ahead_count,
            "ahead_of_pinned_source_main": ahead,
            "is_current_open_pr_head": pr is not None,
            "open_pr_number": pr["number"] if pr else None,
            "sha256_mod_3_remainder": mod,
            "assigned_agent": owner if belongs else None,
            "assignment_status": "partitioned_non_pr_ahead_head" if belongs else ("excluded_open_pr_head" if pr else "not_ahead_of_pinned_main"),
        }
        branch_rows.append(row)
        if not belongs or owner != 2:
            continue

        branch_tree = git_tree(args.source, head)
        counts = collections.Counter()
        for path, (mode, oid) in sorted(branch_tree.items()):
            if oid in source_blob_oids:
                counts["accounted_by_source_main_exact_content"] += 1
                continue
            if oid in open_pr_blob_oids:
                counts["accounted_by_open_pr_exact_content"] += 1
                continue
            if oid in destination_blob_oids:
                counts["already_exact_in_destination"] += 1
                continue

            classification, rationale = preserved_class(path)
            source_sha = hashlib.sha256(git(args.source, "cat-file", "blob", oid)).hexdigest()
            dest_path = None
            if classification.startswith("preserved_"):
                rel_branch = pathlib.PurePosixPath(ref.removeprefix("refs/heads/")) / head[:12]
                dest = archived_path(args.output_root.parent, pathlib.Path("branches/agent-2") / rel_branch, path)
                if oid in saved_blobs:
                    dest_path = saved_blobs[oid]
                else:
                    preserve_blob(args.source, oid, dest, source_sha)
                    dest_path = dest.relative_to(args.output_root.parent).as_posix()
                    saved_blobs[oid] = dest_path
                counts["preserved_branch_only_artifacts"] += 1
            else:
                counts["excluded_branch_only_artifacts"] += 1

            residual_rows.append({
                "full_refname": ref,
                "head_sha": head,
                "path": path,
                "source_mode": mode,
                "source_git_blob_sha1": oid,
                "source_sha256": source_sha,
                "destination_main_same_path_sha256": (
                    hashlib.sha256(git(args.destination, "cat-file", "blob", destination_tree[path][1])).hexdigest()
                    if path in destination_tree else None
                ),
                "disposition": classification,
                "rationale": rationale,
                "preserved_destination_path": dest_path,
            })
        per_head.append({
            "full_refname": ref,
            "head_sha": head,
            "tracked_paths": len(branch_tree),
            "exact_content_already_in_source_main": counts["accounted_by_source_main_exact_content"],
            "exact_content_already_in_open_prs": counts["accounted_by_open_pr_exact_content"],
            "exact_content_already_in_destination": counts["already_exact_in_destination"],
            "branch_only_preserved": counts["preserved_branch_only_artifacts"],
            "branch_only_excluded": counts["excluded_branch_only_artifacts"],
        })

    worktrees = jsonl(args.worktree_audit)
    wt_rows = []
    worktree_artifacts: list[dict] = []
    shared_blob_artifact: dict[str, str] = {}
    branch_blob_rows: dict[str, dict] = {}
    for branch_artifact in residual_rows:
        branch_blob_rows.setdefault(branch_artifact["source_git_blob_sha1"], branch_artifact)
    for record in worktrees:
        path = record.get("path")
        if not path:
            wt_rows.append({
                **record,
                "sha256_mod_3_remainder": None,
                "assigned_agent": None,
                "assignment_status": "unresolved_missing_registered_path",
                "action": "unresolved_unavailable_artifact_identity",
                "rationale": "audit records a broken worktree registration without an artifact path/hash to partition or preserve",
            })
            continue
        mod = ref_remainder(path)
        owner = mod + 1
        full = pathlib.Path(record["worktree"]) / pathlib.PurePosixPath(path)
        exists = full.is_file()
        current_sha = hashlib.sha256(full.read_bytes()).hexdigest() if exists else None
        row = {
            **record,
            "live_file_exists": exists,
            "live_sha256": current_sha,
            "sha256_mod_3_remainder": mod,
            "assigned_agent": owner,
            "assignment_status": "owned_dirty_worktree_path",
        }
        if not exists:
            row.update(action="unresolved_worktree_file_unavailable", rationale="current path is absent; no preservation inferred")
        elif current_sha != record.get("local_sha256"):
            row.update(action="unresolved_worktree_file_changed_since_freeze", rationale="live SHA256 differs from frozen audit; preserve neither version without a new exact receipt")
        elif owner != 2:
            row.update(action="assigned_to_other_agent", rationale="SHA256(path) modulo three assigns this path to another shard")
        else:
            data = full.read_bytes()
            oid = git_blob_sha(data)
            if oid in source_blob_oids:
                row.update(action="duplicate_source_main_content", rationale="exact bytes are already accounted by pinned source main")
            elif oid in open_pr_blob_oids:
                row.update(action="duplicate_open_pr_content", rationale="exact bytes are already accounted by an open source PR head")
            elif oid in destination_blob_oids:
                row.update(action="duplicate_destination_content", rationale="exact bytes already exist on pinned destination main")
            elif oid in branch_blob_rows and branch_blob_rows[oid].get("preserved_destination_path"):
                row.update(
                    action="duplicate_agent2_branch_artifact",
                    rationale="the exact worktree blob is already preserved from an assigned non-PR branch head",
                    preserved_destination_path=branch_blob_rows[oid]["preserved_destination_path"],
                    source_git_blob_sha1=oid,
                )
            elif path == "docs/state/artifact-index.jsonl" or path.startswith("docs/state/"):
                row.update(action="excluded_coordinator_owned_registry", rationale="dirty registry/state files are not copied; coordinator gets exact path and hash in this ledger")
            else:
                classification, rationale = preserved_class(path)
                if classification.startswith("preserved_"):
                    if oid in shared_blob_artifact:
                        dest_path = shared_blob_artifact[oid]
                        action = "duplicate_agent2_branch_or_worktree_artifact"
                    else:
                        worktree_label = pathlib.Path(record["worktree"]).name
                        dest = archived_path(args.output_root.parent, pathlib.Path("branches/agent-2/worktrees") / worktree_label, path)
                        preserve_bytes(data, dest, current_sha)
                        dest_path = dest.relative_to(args.output_root.parent).as_posix()
                        shared_blob_artifact[oid] = dest_path
                        action = "preserved_exact_worktree_bytes"
                    row.update(action=action, rationale=rationale, preserved_destination_path=dest_path, source_git_blob_sha1=oid)
                    worktree_artifacts.append(row)
                else:
                    row.update(action=classification, rationale=rationale)
        wt_rows.append(row)

    out = args.output_root
    branch_sha = write_jsonl(out / "branch-head-assignment.jsonl", branch_rows)
    branch_files_sha = write_jsonl(out / "branch-file-dispositions.jsonl", residual_rows)
    per_head_sha = write_jsonl(out / "branch-head-summaries.jsonl", per_head)
    worktree_sha = write_jsonl(out / "worktree-path-assignment.jsonl", wt_rows)
    summary = {
        "source_main": SOURCE_MAIN,
        "destination_main": DESTINATION_MAIN,
        "open_source_pr_count": len(prs),
        "local_branch_ref_count": len(local_refs),
        "live_remote_branch_ref_count": len(remote_refs),
        "unique_refname_head_pairs": len(sources),
        "non_pr_ahead_heads": sum(r["ahead_of_pinned_source_main"] and not r["is_current_open_pr_head"] for r in branch_rows),
        "agent_2_non_pr_ahead_heads": sum(r["assigned_agent"] == 2 for r in branch_rows),
        "agent_2_branch_file_rows": sum(r["disposition"].startswith("preserved_") or r["disposition"].startswith("excluded_") for r in residual_rows),
        "agent_2_branch_artifacts_preserved": sum(r["disposition"].startswith("preserved_") for r in residual_rows),
        "agent_2_branch_artifacts_excluded": sum(r["disposition"].startswith("excluded_") for r in residual_rows),
        "dirty_worktree_audit_rows": len(worktrees),
        "dirty_worktree_paths_with_identity": sum(bool(r.get("path")) for r in worktrees),
        "dirty_worktree_paths_by_remainder": {str(k): sum(bool(r.get("path")) and ref_remainder(r["path"]) == k for r in worktrees) for k in (0,1,2)},
        "agent_2_dirty_worktree_paths": sum(r.get("assigned_agent") == 2 for r in wt_rows),
        "agent_2_dirty_worktree_preserved": sum(r.get("action") == "preserved_exact_worktree_bytes" for r in wt_rows),
        "agent_2_dirty_worktree_excluded_registry": sum(r.get("action") == "excluded_coordinator_owned_registry" for r in wt_rows),
        "unresolved_missing_registered_worktree_rows": sum(r.get("action") == "unresolved_unavailable_artifact_identity" for r in wt_rows),
        "branch_head_assignment_sha256": branch_sha,
        "branch_file_dispositions_sha256": branch_files_sha,
        "branch_head_summaries_sha256": per_head_sha,
        "worktree_path_assignment_sha256": worktree_sha,
    }
    (out / "branch-worktree-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
