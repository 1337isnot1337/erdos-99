#!/usr/bin/env python3
"""Verify Agent 3 source identity, transformed text, destination hashes, links, and imports."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import re
import posixpath
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

BASE = Path(__file__).resolve().parent
PRIVATE_HOME = re.compile(rb"(?<![A-Za-z0-9_.-])/home/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MIGRATION_WARNINGS = (b"> **Historical source snapshot", b"> **Imported source research",
                      b"> **Imported unreviewed source research", b"> **Imported unreviewed branch research",
                      b"> **Historical branch snapshot", b"> **Historical PR snapshot",
                      b"> **Historical dirty-worktree snapshot", b"> **Withdrawn inference warning")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args])


def source_blob(source: Path, commit: str, path: str, expected_oid: str, expected_sha: str,
                errors: list[str], label: str) -> bytes | None:
    try:
        oid = git(source, "rev-parse", f"{commit}:{path}").decode().strip()
        data = git(source, "cat-file", "blob", oid)
    except subprocess.CalledProcessError:
        errors.append(f"{label}: source path/blob missing at {commit[:12]}:{path}")
        return None
    if oid != expected_oid:
        errors.append(f"{label}: source Git blob mismatch at {path}")
    if sha(data) != expected_sha:
        errors.append(f"{label}: source SHA-256 mismatch at {path}")
    return data


def source_body(data: bytes) -> bytes:
    if data.startswith(b"<!-- theorem-state:"):
        lines = data.splitlines(keepends=True)
        return b"".join(lines[1:])
    return data


def normalized_source_body(data: bytes) -> bytes:
    lines = data.splitlines(keepends=True)
    while lines:
        first = lines[0]
        if first.startswith((b"<!-- theorem-state:", b"<!-- migration-provenance:")) or not first.strip() or first.startswith(MIGRATION_WARNINGS):
            lines.pop(0)
            continue
        break
    return b"".join(lines)


def unwrapped_destination(data: bytes) -> bytes:
    lines = data.splitlines(keepends=True)
    if not lines or not lines[0].startswith(b"<!-- migration-provenance:"):
        return data
    i = 1
    if i < len(lines) and not lines[i].strip():
        i += 1
    saw_notice = False
    while i < len(lines):
        if lines[i].startswith(MIGRATION_WARNINGS):
            saw_notice = True
            i += 1
            continue
        if saw_notice and not lines[i].strip():
            i += 1
            continue
        break
    return b"".join(lines[i:])


def check_destination(root: Path, path: str | None, expected_sha: str | None,
                      expected_blob: str | None, errors: list[str], label: str) -> bytes | None:
    if not path:
        return None
    target = root / path
    if not target.is_file():
        errors.append(f"{label}: destination file missing: {path}")
        return None
    data = target.read_bytes()
    if expected_sha and sha(data) != expected_sha:
        errors.append(f"{label}: destination SHA-256 mismatch: {path}")
    if expected_blob:
        actual_blob = git(root, "hash-object", "--", str(target)).decode().strip()
        if actual_blob != expected_blob:
            errors.append(f"{label}: destination Git blob mismatch: {path}")
    return data


def verify_main(source: Path, root: Path, errors: list[str], counts: Counter,
                markdown_rows: list[tuple[str, str, bytes]]) -> None:
    for row in jsonl(BASE / "source-main-dispositions.jsonl"):
        path, commit = row["source_path"], row["source_commit"]
        data = source_blob(source, commit, path, row["source_blob"], row["source_sha256"], errors, "source-main")
        counts["source_main_rows"] += 1
        status = row.get("migration_status", "")
        if not status.startswith("preserved_"):
            counts[f"source_main_{status}"] += 1
            continue
        dest_path = row.get("destination_artifact_path")
        dest_data = check_destination(root, dest_path, row.get("destination_sha256"),
                                      row.get("destination_git_blob_sha1"), errors, "source-main")
        if data is None or dest_data is None:
            continue
        expected = source_body(data)
        if not path.lower().endswith((".py", ".cpp", ".hpp")):
            expected = PRIVATE_HOME.sub(b"[local filesystem path omitted]", expected)
        observed = unwrapped_destination(dest_data) if path.lower().endswith(".md") else dest_data
        if observed != expected:
            errors.append(f"source-main: mathematical/source body differs after recorded transformations: {path}")
        if sha(expected) != row.get("source_body_sha256") and "redacted_absolute_owner_local_paths_in_prose_or_data" not in row.get("transformations", []):
            errors.append(f"source-main: recorded body hash mismatch: {path}")
        counts["source_main_materialized"] += 1
        if path.lower().endswith(".md"):
            markdown_rows.append((dest_path, path, observed))


def verify_prs(source: Path, diff_repo: Path, root: Path, errors: list[str], counts: Counter,
               markdown_rows: list[tuple[str, str, bytes]]) -> None:
    for row in jsonl(BASE / "pr-dispositions.jsonl"):
        label = f"PR #{row['source_pr']}"
        path = row["source_path"]
        data = source_blob(source, row["source_head"], path, row["source_blob"], row["source_sha256"], errors, label)
        counts["pr_file_rows"] += 1
        disposition = row["disposition"]
        if disposition.startswith("preserve_"):
            dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if data is not None and dest is not None:
                expected = source_body(data)
                observed = unwrapped_destination(dest) if path.lower().endswith(".md") else dest
                if observed != expected:
                    errors.append(f"{label}: source artifact body mismatch: {path}")
                if path.lower().endswith(".md"):
                    markdown_rows.append((row["destination_path"], path, observed))
                counts["pr_materialized"] += 1
        elif "duplicate" in disposition:
            target = row.get("destination_path")
            dest = check_destination(root, target, row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if data is not None and dest is not None and data != dest:
                errors.append(f"{label}: exact duplicate differs: {path}")
            counts["pr_deduplicated"] += 1
        else:
            counts[f"pr_{disposition}"] += 1
            if disposition == "exclude_shared_research_navigation_change":
                base = row["source_base"]
                patch = git(diff_repo, "diff", "--no-ext-diff", "--unified=3", base,
                            row["source_head"], "--", path)
                if sha(patch) != row.get("source_change_diff_sha256"):
                    errors.append(f"{label}: shared navigation diff hash mismatch: {path}")


def verify_branches(source: Path, root: Path, errors: list[str], counts: Counter,
                    markdown_rows: list[tuple[str, str, bytes]]) -> None:
    main_allocation = {r["source_path"]: r for r in jsonl(BASE / "source-main-allocation.jsonl")}
    for row in jsonl(BASE / "branch-dispositions.jsonl"):
        label = "source-branch"
        oid, path, commit = row.get("source_blob"), row.get("source_path"), row.get("source_commit")
        if not oid or not path or not commit:
            continue
        try:
            data = git(source, "cat-file", "blob", oid)
        except subprocess.CalledProcessError:
            errors.append(f"{label}: source blob object missing: {path} {oid}")
            continue
        if sha(data) != row.get("source_sha256"):
            errors.append(f"{label}: source SHA-256 mismatch: {path}")
        try:
            committed_oid = git(source, "rev-parse", f"{commit}:{path}").decode().strip()
            if committed_oid != oid:
                errors.append(f"{label}: selected source commit does not contain recorded path/blob: {path}")
        except subprocess.CalledProcessError:
            errors.append(f"{label}: selected source commit lacks recorded path: {path}")
        counts["branch_file_versions"] += 1
        disposition = row["disposition"]
        if disposition.startswith("preserved_"):
            dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if dest is None:
                continue
            expected = source_body(data) if path.lower().endswith(".md") else data
            observed = unwrapped_destination(dest) if path.lower().endswith(".md") else dest
            if observed != expected:
                errors.append(f"{label}: preserved body differs after recorded wrapper/header transformation: {path}")
            counts["branch_materialized_versions"] += 1
            if path.lower().endswith(".md"):
                markdown_rows.append((row["destination_path"], path, observed))
        elif disposition == "exact_destination_body_duplicate":
            dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if dest is not None and sha(normalized_source_body(unwrapped_destination(dest))) != row.get("source_body_sha256"):
                errors.append(f"{label}: destination proof body duplicate mismatch: {path}")
            counts["branch_body_deduplicated"] += 1
        elif disposition in ("deduplicated_existing_migration_record", "exact_source_main_body_migrated_by_source_main"):
            dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if dest is None:
                continue
            if disposition == "exact_source_main_body_migrated_by_source_main":
                if sha(normalized_source_body(unwrapped_destination(dest))) != row.get("destination_body_sha256"):
                    errors.append(f"{label}: source-main branch body handoff mismatch: {path}")
            counts["branch_deduplicated_existing_main_migration"] += 1
        elif disposition.startswith("deduplicated_source_main_allocated_to_agent_"):
            try:
                assigned_owner = int(disposition.rsplit("_", 1)[1])
            except ValueError:
                assigned_owner = None
            allocated = main_allocation.get(path)
            if (assigned_owner not in (1, 2) or not allocated
                    or allocated.get("owner") != assigned_owner
                    or allocated.get("source_blob") != oid
                    or allocated.get("source_sha256") != row.get("source_sha256")):
                errors.append(f"{label}: sibling-shard deduplication is not backed by the deterministic allocation: {path}")
            counts["branch_deduplicated_to_sibling_shard"] += 1
        elif disposition in ("deduplicated_existing_frozen_report_migration", "deduplicated_frozen_report_migration"):
            dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                     row.get("destination_git_blob_sha1"), errors, label)
            if dest is not None:
                counts["branch_deduplicated_frozen_report"] += 1
        else:
            dest = check_destination(root, row.get("destination_path"), row.get("source_sha256"),
                                     row.get("source_blob"), errors, label)
            if dest is not None and dest != data:
                errors.append(f"{label}: exact destination duplicate is not byte-identical: {path}")
            counts["branch_exact_deduplicated"] += 1


def verify_dirty(source: Path, root: Path, errors: list[str], counts: Counter,
                 markdown_rows: list[tuple[str, str, bytes]]) -> None:
    for row in jsonl(BASE / "dirty-dispositions.jsonl"):
        if row.get("owner") != 3:
            continue
        counts["agent3_dirty_rows"] += 1
        disposition = row.get("migration_disposition", "")
        if disposition == "unresolved_agent3_dirty_snapshot":
            counts["agent3_dirty_unresolved"] += 1
            continue
        if not disposition.startswith(("preserve_", "exclude_shared_navigation")):
            continue
        if disposition == "exclude_shared_navigation_save_diff":
            p = row["destination_path"]
            dest = check_destination(root, p, row["destination_sha256"], row["destination_git_blob_sha1"], errors, "dirty")
            if dest is None or sha(dest) != row.get("source_change_diff_sha256"):
                errors.append("dirty worktree README diff does not match its receipt")
            continue
        source_path = row.get("path")
        source_worktree = row.get("worktree")
        try:
            data = (Path(source_worktree) / source_path).read_bytes()
        except (TypeError, OSError):
            errors.append(f"dirty: source snapshot unavailable: {source_path}")
            continue
        if sha(data) != row.get("source_sha256"):
            errors.append(f"dirty: frozen worktree SHA-256 mismatch: {source_path}")
        dest = check_destination(root, row.get("destination_path"), row.get("destination_sha256"),
                                 row.get("destination_git_blob_sha1"), errors, "dirty")
        if dest is None:
            continue
        expected = source_body(data) if source_path.lower().endswith(".md") else data
        observed = unwrapped_destination(dest) if source_path.lower().endswith(".md") else dest
        if expected != observed:
            errors.append(f"dirty: preserved bytes/body mismatch: {source_path}")
        if source_path.lower().endswith(".md"):
            markdown_rows.append((row["destination_path"], source_path, observed))
        counts["dirty_materialized"] += 1


def link_audit(source: Path, root: Path, markdown_rows: list[tuple[str, str, bytes]]) -> dict:
    allocation = {r["source_path"]: r for r in jsonl(BASE / "source-main-allocation.jsonl")}
    dispositions = {r["source_path"]: r for r in jsonl(BASE / "source-main-dispositions.jsonl")}
    branch_paths = {r.get("source_path"): r for r in jsonl(BASE / "branch-dispositions.jsonl")}
    pr_paths = {r.get("source_path"): r for r in jsonl(BASE / "pr-dispositions.jsonl")}
    checked = external = anchors = valid = 0
    broken = []
    categories = Counter()
    for dest_path, source_path, data in markdown_rows:
        content = data.decode("utf-8", "replace")
        content = re.sub(r"```.*?```|~~~.*?~~~", "", content, flags=re.S)
        for match in LINK.finditer(content):
            target = match.group(1).strip().split(None, 1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "ftp://", "tel:")):
                external += 1
                continue
            if target.startswith("#"):
                anchors += 1
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                anchors += 1
                continue
            checked += 1
            rel_candidates = []
            if target.startswith("/"):
                rel_candidates.append(target.lstrip("/"))
            else:
                rel_candidates.extend([str(Path(source_path).parent / target),
                                       str(Path(dest_path).parent / target), target])
            found = False
            for rel in rel_candidates:
                candidate = root / rel
                if candidate.is_file() or (candidate.is_dir() and any((candidate / n).is_file() for n in ("README.md", "index.md"))):
                    found = True
                    break
            if found:
                valid += 1
                continue
            source_target = (target.lstrip("/") if target.startswith("/") else
                             posixpath.normpath(posixpath.join(posixpath.dirname(source_path), target)))
            mapped = dispositions.get(source_target) or allocation.get(source_target)
            owner = mapped.get("owner") if mapped else None
            dest_map = mapped.get("destination_artifact_path") if mapped else None
            category = "target_not_found_in_current_destination_or_agent3_ledgers"
            source_has_target = False
            if source_target.startswith(("papers/", "extracted/")):
                category = "third_party_reference_not_copied_by_scope"
            else:
                try:
                    git(source, "cat-file", "-e", f"42f0296d1aca068c809f74cee5dcdb4ebdb27c73:{source_target}")
                    source_has_target = True
                except subprocess.CalledProcessError:
                    pass
                if mapped:
                    if owner in (1, 2):
                        category = f"assigned_to_agent_{owner}"
                    elif owner == 3 and dest_map:
                        category = "agent3_target_relocated_or_not_present"
                    elif str(mapped.get("migration_status", "")).startswith("exclude_"):
                        category = "excluded_by_agent3_scope"
                    elif dest_map:
                        category = "mapped_destination_not_present"
                else:
                    branch = branch_paths.get(source_target)
                    pr = pr_paths.get(source_target)
                    if branch:
                        category = "mapped_source_branch_artifact"
                        owner = "branch shard"
                        dest_map = branch.get("destination_path")
                    elif pr:
                        category = "mapped_source_pr_artifact"
                        owner = "PR disposition"
                        dest_map = pr.get("destination_path")
                    elif source_has_target:
                        category = "source_main_target_not_in_agent3_allocation"
            categories[category] += 1
            if mapped is None:
                mapped = branch_paths.get(source_target) or pr_paths.get(source_target)
            broken.append({"markdown_destination": dest_path, "markdown_source_path": source_path,
                           "link_target": target, "normalized_source_target": source_target,
                           "source_target_in_pinned_main": source_has_target,
                           "category": category, "owner_or_scope": owner,
                           "mapped_destination": dest_map,
                           "in_pinned_source_main": source_target in allocation,
                           "disposition": mapped.get("migration_status", mapped.get("disposition")) if mapped else "unmapped_in_pinned_source_main_or_agent3_ledgers"})
    return {"markdown_files_checked": len(markdown_rows), "relative_links_checked": checked,
            "relative_links_resolved": valid, "external_links": external,
            "anchor_only_links": anchors, "unresolved_relative_links": broken,
            "unresolved_category_counts": dict(sorted(categories.items()))}


def import_audit(root: Path, errors: list[str]) -> dict:
    stdlib = sys.stdlib_module_names
    paths = set()
    for filename in ("source-main-dispositions.jsonl", "pr-dispositions.jsonl",
                     "branch-dispositions.jsonl", "dirty-dispositions.jsonl"):
        for row in jsonl(BASE / filename):
            source_path = row.get("source_path") or row.get("path")
            dest_path = row.get("destination_artifact_path") or row.get("destination_path")
            disposition = row.get("migration_status") or row.get("disposition") or row.get("migration_disposition") or ""
            if not source_path or not dest_path or not str(source_path).endswith((".py", ".py.source")) or str(disposition).startswith("exclude_"):
                continue
            paths.add((source_path, dest_path))
    missing = []
    external = Counter()
    modules_seen = set()
    for source_path, dest_path in sorted(paths):
        file_path = root / dest_path
        if not file_path.is_file():
            continue
        try:
            tree = ast.parse(file_path.read_text())
        except (OSError, SyntaxError) as exc:
            errors.append(f"verifier dependency scan could not parse {dest_path}: {exc}")
            continue
        for node in ast.walk(tree):
            module_names = []
            if isinstance(node, ast.Import):
                module_names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                module_names = [node.module]
            for module in module_names:
                top = module.split(".")[0]
                modules_seen.add(top)
                if top in stdlib or top == "__future__":
                    continue
                candidates = [root / "research" / f"{top}.py", root / f"{top}.py",
                              root / "research" / top / "__init__.py"]
                if any(candidate.is_file() for candidate in candidates):
                    continue
                try:
                    spec = importlib.util.find_spec(top)
                except (ImportError, ModuleNotFoundError, ValueError):
                    spec = None
                if spec is not None:
                    external[top] += 1
                    continue
                assigned = next((r for r in jsonl(BASE / "source-main-allocation.jsonl")
                                 if r.get("source_path") in (f"research/{top}.py", f"{top}.py")), None)
                missing.append({"destination_script": dest_path, "module": top,
                                "source_path": f"research/{top}.py",
                                "allocated_owner": assigned.get("owner") if assigned else None,
                                "unit_key": assigned.get("unit_key") if assigned else None})
    return {"python_sources_scanned": len(paths), "unique_import_names": len(modules_seen),
            "external_packages_detected": dict(sorted(external.items())),
            "missing_local_imports": missing,
            "missing_local_import_reference_count": len(missing)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--source-mirror", type=Path, required=True,
                    help="read-only bare mirror used to reproduce PR diff bytes independent of worktree attributes")
    ap.add_argument("--destination", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    source, diff_repo, root, output = args.source.resolve(), args.source_mirror.resolve(), args.destination.resolve(), args.output.resolve()
    errors: list[str] = []
    counts = Counter()
    markdown_rows: list[tuple[str, str, bytes]] = []
    verify_main(source, root, errors, counts, markdown_rows)
    verify_prs(source, diff_repo, root, errors, counts, markdown_rows)
    verify_branches(source, root, errors, counts, markdown_rows)
    verify_dirty(source, root, errors, counts, markdown_rows)
    links = link_audit(source, root, markdown_rows)
    imports = import_audit(root, errors)
    report = {"status": "PASS" if not errors else "FAIL",
              "source_main": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73",
              "destination_baseline": "c6e0394b3152d21075328bf4f26e6c070229bf13",
              "counts": dict(counts), "link_audit": links, "verifier_import_audit": imports,
              "errors": errors,
              "scope": "source identity, retained byte/body integrity, explicit links and local imports; no theorem correctness inferred"}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    links_path = output.with_name("markdown-link-audit.json")
    links_path.write_text(json.dumps(links, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": report["status"], "counts": report["counts"],
                      "link_counts": {k: (len(v) if isinstance(v, list) else v) for k, v in links.items()},
                      "import_audit": {"python_sources_scanned": imports["python_sources_scanned"],
                                       "external_packages_detected": imports["external_packages_detected"],
                                       "missing_local_import_reference_count": imports["missing_local_import_reference_count"],
                                       "missing_local_imports": imports["missing_local_imports"]},
                      "error_count": len(errors), "errors": errors[:50],
                      "report": str(output.relative_to(root)),
                      "link_report": str(links_path.relative_to(root))}, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
