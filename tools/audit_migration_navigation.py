#!/usr/bin/env python3
"""Audit all Markdown paths and map immutable source references to exact copies.

The literal-link audit and the historical reference map are separate results.
A mapped archive target never turns a broken literal link into a working link.
The tool reads Git objects, does not fetch URLs, and does not execute research.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import quote, unquote, urlsplit

from check_migration_references import (GitReader, ReferenceError, REGULAR, require_recorded_blobs,
                                        safe_path, write_receipt)

SOURCE = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
INVENTORY = "docs/research/migration/2026-10-16/agent-1/evidence/source-main-three-way-assignment.jsonl"
CONTEXT_RECEIPTS = {
    "docs/research/migration/2026-10-16/agent-1/evidence/source-dirty-worktrees/source-dirty-worktree-assignments.jsonl":
        "4854bc7ba57cea323cb37f17d3441fa349b472ce",
}
MARKDOWN = re.compile(r"\.md(?:\.source(?:\.[^/]*)?)?$", re.I)
ARCHIVED = re.compile(r"(?:^docs/archive/|/payload/|/integration/source-main/|/commits/[0-9a-f]{12,40}/)")
HISTORICAL_NAVIGATION_ALIASES = {
    "research/target_c_allregime_fan_train_floor_reaudit_2026-09-12.md":
        "research/target_c_allregime_fan_train_floor_hostile_audit_2026-09-12.md",
    "research/target_c_phase_atomic_route_surplus_self_audit.md":
        "docs/audits/target_c_phase_atomic_route_surplus_self_audit_2026-09-12.md",
    "docs/reports/target_c_acute_binary_owner_laminarity_and_crossing_scope_2026-10-06.md":
        "docs/research/migration/2026-10-16/agent-1/payload/source-pr-737/docs/reports/target_c_binary_owner_laminarity_and_crossing_scope_2026-10-06.md",
}


def prose(text: str) -> str:
    """Mask code while retaining line positions for the audit receipt."""
    lines = text.splitlines(keepends=True)
    fence = None
    for i, line in enumerate(lines):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines[i] = "".join("\n" if x == "\n" else " " for x in line)
        elif fence is not None:
            lines[i] = "".join("\n" if x == "\n" else " " for x in line)
    result = "".join(lines)
    def mask(match):
        return "".join("\n" if x == "\n" else " " for x in match.group(0))
    result = re.sub(r"(`+)(.*?)\1", mask, result)
    # A bracket immediately followed by parentheses is ordinary algebra in
    # math blocks, for example [J(C)-c](3C-W), rather than a Markdown link.
    result = re.sub(r"\\\[.*?\\\]", mask, result, flags=re.S)
    result = re.sub(r"(?<!\S)\\\(.*?\\\)", mask, result, flags=re.S)
    result = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", mask, result, flags=re.S)
    return re.sub(r"(?<!\\)\$(?!\$)[^\n$]*(?<!\\)\$", mask, result)


def markdown_links(text: str) -> list[tuple[str, int]]:
    """Read inline and defined reference links, excluding code and bare URLs.

    This is a bounded Markdown link parser, not an HTML renderer. HTML href/src
    attributes, shortcut references, and fragments need separate verification.
    """
    text = prose(text)
    result = []
    # Inline targets can contain balanced parentheses and escaped punctuation.
    for match in re.finditer(r"(?<!\\)\]\(", text):
        start = match.end()
        while start < len(text) and text[start].isspace():
            start += 1
        end = start
        if start < len(text) and text[start] == "<":
            end = text.find(">", start + 1)
            if end < 0:
                continue
            value = text[start + 1:end]
        else:
            depth = 0
            escaped = False
            while end < len(text):
                char = text[end]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char.isspace() and depth == 0:
                    break
                end += 1
            value = re.sub(r"\\([()<> ])", r"\1", text[start:end])
        if value:
            result.append((value, text.count("\n", 0, match.start()) + 1))
    # Explicit/collapsed reference links use the definition's destination.
    definitions = {}
    for match in re.finditer(r"^ {0,3}\[([^]\n]+)\]:\s*(?:<([^>\n]+)>|(\S+))", text, re.M):
        definitions[" ".join(match.group(1).split()).casefold()] = match.group(2) or match.group(3)
    for match in re.finditer(r"\[([^]\n]+)\]\[([^]\n]*)\]", text):
        label = " ".join((match.group(2) or match.group(1)).split()).casefold()
        if label in definitions:
            result.append((definitions[label], text.count("\n", 0, match.start()) + 1))
    return sorted(set(result), key=lambda row: (row[1], row[0]))


def resolve(document: str, link: str) -> tuple[str, str | None]:
    url = urlsplit(link)
    if url.scheme in {"http", "https", "mailto"} or (url.netloc and not url.scheme):
        return "external", None
    if url.scheme or url.netloc or any(ord(c) < 32 for c in link):
        return "unsafe_reference", None
    if not url.path:
        return "anchor", None
    path = unquote(url.path)
    if path.startswith("/") or "\\" in path:
        return "unsafe_reference", None
    target = posixpath.normpath(posixpath.join(posixpath.dirname(document), path))
    try:
        return "local", safe_path(target)
    except ReferenceError:
        return "unsafe_reference", None


def reference_only(path: str) -> bool:
    return path.startswith("extracted/") or (path.startswith("papers/") and not path.endswith((".md", ".bib", ".json")))


def original_context(path: str, source: dict, by_source_blob: dict, oid: str) -> str | None:
    if path in source:
        return path
    for marker in ("/payload/source-main/", "/integration/source-main/", "/corpus/source-main/"):
        if marker in path:
            return re.sub(r"\.source(?:\.[^/]*)?$", "", path.split(marker, 1)[1])
    match = re.search(r"/source-e99-main-[0-9a-f]+/(.+)$", path)
    if match:
        return re.sub(r"\.source(?:\.[^/]*)?$", "", match.group(1))
    match = re.search(r"/(?:commits/)?(?:[0-9a-f]{12}|[0-9a-f]{40})/(.+)$", path)
    if match:
        return re.sub(r"\.source(?:\.[^/]*)?$", "", match.group(1))
    match = re.search(r"/payload/source-pr-[0-9]+/(.+)$", path)
    if match:
        return re.sub(r"\.source(?:\.[^/]*)?$", "", match.group(1))
    match = re.search(r"/(?:source-pr/pr-[0-9]+|branches/agent-[123]/worktrees/[^/]+)/(.+)$", path)
    if match:
        return re.sub(r"\.source(?:\.[^/]*)?$", "", match.group(1))
    # Dirty-worktree archive roots include slash-bearing branch names. Match
    # the longest complete original path rather than guessing their depth.
    parts = path.split("/")
    suffixes = [re.sub(r"\.source(?:\.[^/]*)?$", "", "/".join(parts[i:])) for i in range(1, len(parts))]
    matches = [p for p in suffixes if p in source]
    if matches:
        return max(matches, key=len)
    paths = by_source_blob.get(oid, [])
    return paths[0] if len(paths) == 1 else None


def preferred(paths: list[str], original: str) -> str:
    return min(paths, key=lambda p: (p != original, p.count("/"), len(p), p))


def audit(tree: dict, documents: dict, source: dict, context_overrides: dict | None = None) -> dict:
    context_overrides = context_overrides or {}
    def context_for(path, oid):
        return context_overrides.get(path) or original_context(path, source, by_source_blob, oid)
    by_blob, by_source_blob = defaultdict(list), defaultdict(list)
    for path, (mode, oid) in tree.items():
        if mode in REGULAR:
            by_blob[oid].append(path)
    for path, oid in source.items():
        by_source_blob[oid].append(path)
    snapshot_roots, snapshot_targets, historical_targets = {}, defaultdict(list), defaultdict(list)
    for path, (mode, oid) in tree.items():
        if mode not in REGULAR or not (ARCHIVED.search(path) or ".source" in path):
            continue
        context = context_for(path, oid)
        stripped = re.sub(r"\.source(?:\.[^/]*)?$", "", path)
        if context and stripped.endswith(context):
            root = stripped[:-len(context)]
            snapshot_roots[path] = root
            snapshot_targets[root, context].append(path)
            historical_targets[context].append(path)
    dirs = set()
    for path in tree:
        parts = path.split("/")
        dirs.update("/".join(parts[:i]) for i in range(1, len(parts)))
    records = []
    for document, text in sorted(documents.items()):
        historical = bool(ARCHIVED.search(document) or ".md.source" in document.rsplit("/", 1)[-1])
        branch_snapshot = historical and "/source-main/" not in document and not re.search(r"/source-e99-main-[0-9a-f]+/", document)
        context = context_for(document, tree[document][1])
        for link, line in markdown_links(text):
            kind, target = resolve(document, link)
            row = dict(document=document, line=line, link=link, target=target, historical=historical)
            if kind != "local":
                row["status"] = kind
                records.append(row)
                continue
            if target in tree:
                row["status"] = "resolved_file" if tree[target][0] in REGULAR else "unsupported_target_mode"
            elif target in dirs:
                row["status"] = "resolved_directory"
            else:
                row["status"] = "broken_literal_link"
                source_target = None
                if context:
                    source_kind, source_target = resolve(context, link)
                    if source_kind != "local":
                        source_target = None
                source_target = source_target or target
                row["source_document"] = context
                row["source_target"] = source_target
                snapshot_copies = snapshot_targets.get((snapshot_roots.get(document), source_target), [])
                if reference_only(source_target):
                    row["mapping_status"] = "external_reference_not_redistributed"
                elif snapshot_copies:
                    copies = sorted(snapshot_copies)
                    row.update(mapping_status="same_snapshot_preserved_target", exact_candidates=copies,
                               navigation_target=preferred(copies, source_target))
                elif source_target in source and by_blob.get(source[source_target]):
                    copies = sorted(by_blob[source[source_target]])
                    row.update(mapping_status="pinned_source_main_target_preserved" if branch_snapshot else "exact_source_target_preserved", exact_candidates=copies,
                               navigation_target=preferred(copies, source_target), source_blob=source[source_target])
                    if branch_snapshot:
                        row["mapping_limit"] = "This points to the pinned source-main version; the old branch dependency version is not established."
                elif source_target in tree and tree[source_target][0] in REGULAR:
                    row.update(mapping_status="current_destination_target", navigation_target=source_target)
                elif source_target in dirs:
                    row.update(mapping_status="current_destination_directory", navigation_target=source_target)
                elif historical and historical_targets.get(source_target):
                    copies = sorted(historical_targets[source_target])
                    row.update(mapping_status="other_historical_target_version_unverified", exact_candidates=copies,
                               navigation_target=preferred(copies, source_target),
                               mapping_limit="A historical file at this original path survives; its version relative to this reference is not established.")
                elif historical and tree.get(HISTORICAL_NAVIGATION_ALIASES.get(source_target), (None, None))[0] in REGULAR:
                    row.update(mapping_status="corrected_historical_filename",
                               navigation_target=HISTORICAL_NAVIGATION_ALIASES[source_target],
                               mapping_limit="Navigation to a later audit under its corrected filename; no old dependency version or byte identity is asserted.")
                else:
                    row["mapping_status"] = "unresolved"
            records.append(row)
    broken = [r for r in records if r["status"] in {"broken_literal_link", "unsafe_reference", "unsupported_target_mode"}]
    active = [r for r in broken if not r["historical"] and r.get("mapping_status") != "external_reference_not_redistributed"]
    historical_unresolved = [r for r in broken if r["historical"] and r.get("mapping_status") in {None, "unresolved"}]
    return dict(schema_version=1, status="PASS_ACTIVE_DOCUMENT_PATHS" if not active else "BLOCKED_ACTIVE_DOCUMENT_PATHS",
                source_commit=SOURCE, documents_checked=len(documents), reference_counts=dict(Counter(r["status"] for r in records)),
                historical_mapping_counts=dict(Counter(r.get("mapping_status", r["status"]) for r in broken if r["historical"])),
                active_blocking_references=active, historical_unresolved_references=historical_unresolved,
                references=records, deprecation_ready=False, release_verified=False, mathematical_proof=False,
                limits=["The tool checks file paths, not Markdown fragments or external URL availability.",
                        "Fenced code and inline code are excluded; HTML href/src and shortcut reference links are outside this parser.",
                        "An exact archive mapping is navigation evidence and does not repair the archived literal link.",
                        "A branch snapshot fallback identifies source-main bytes, not its old dependency version.",
                        "Explicitly listed stale filenames have navigation aliases; their old versions are not inferred.",
                        "Source replay uses the separately verified source-identity map; no research program runs here."])


def navigation_markdown(report: dict, destination: str) -> str:
    """Write explicit links without changing immutable historical source bytes."""
    def relative(path):
        return quote(posixpath.relpath(path, posixpath.dirname(destination)), safe="/._-")
    lines = ["# Historical reference map", "", "This map preserves navigation for immutable source snapshots.",
             "The archived files retain their original bytes and original literal links.",
             "The source replay command reconstructs their original file layout outside the checkout.",
             "Current theorem authority remains `docs/STATE.md` and its manifest.", "",
             "Links marked unresolved have no demonstrated destination in this candidate.", ""]
    grouped = defaultdict(list)
    for row in report["references"]:
        if row["historical"] and row["status"] == "broken_literal_link":
            grouped[(row.get("source_target", row["link"]), row.get("mapping_status", "unresolved"), row.get("navigation_target", ""))].append(row)
    lines.extend(["The table groups identical source targets and destination versions.",
                  "The count gives the number of archived link occurrences in this scan.",
                  "A source-main fallback does not establish an older branch dependency version.", "",
                  "| Source-relative target | Preserved target | Archive example | Links |", "| --- | --- | --- | ---: |"])
    for (original, status, target), rows in sorted(grouped.items()):
        if target:
            link = "[" + status + "](" + relative(target) + ")"
        elif status == "external_reference_not_redistributed":
            link = "External reference; bytes not redistributed"
        else:
            link = "Unresolved"
        source_link = "[Immutable source](" + relative(rows[0]["document"]) + ")"
        lines.append("| `" + original.replace("|", "\\|") + "` | " + link + " | " + source_link + " | " + str(len(rows)) + " |")
    return "\n".join(lines) + "\n"


def write_navigation(output: Path, repo: Path, text: str) -> None:
    output = output.absolute()
    if output.is_relative_to(repo.resolve()) or output.exists() or output.is_symlink():
        raise ReferenceError("Navigation output must be new and outside the checkout")
    if any(parent.is_symlink() for parent in output.parents):
        raise ReferenceError("Navigation output has a symlink ancestor")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        stream.write(text)


def context_overrides(git: GitReader, tree: dict) -> dict:
    result = {}
    for receipt, oid in CONTEXT_RECEIPTS.items():
        if tree.get(receipt) != ("100644", oid):
            raise ReferenceError("Historical source-context evidence changed: " + receipt)
        for line in git.text(tree, receipt).splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            destination, original = row.get("destination_path"), row.get("source_path")
            if not destination or not original:
                continue
            destination, original = safe_path(destination), safe_path(original)
            if tree.get(destination, (None, None))[0] not in REGULAR:
                continue
            if destination in result and result[destination] != original:
                raise ReferenceError("Conflicting historical source context: " + destination)
            result[destination] = original
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--navigation-output", type=Path)
    parser.add_argument("--navigation-repository-path", default="docs/research/migration/2026-10-16/integration/historical-reference-map.md")
    args = parser.parse_args()
    try:
        git = GitReader(args.repo)
        commit, tree = git.tree(args.ref)
        require_recorded_blobs(tree)
        source = {}
        for line in git.text(tree, INVENTORY).splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            path, oid = safe_path(row["source_path"]), row["source_git_blob_sha1"]
            if path in source or not re.fullmatch(r"[0-9a-f]{40}", oid):
                raise ReferenceError("Invalid source identity inventory")
            source[path] = oid
        documents = {p: git.text(tree, p) for p, (mode, _) in tree.items() if mode in REGULAR and MARKDOWN.search(p)}
        report = audit(tree, documents, source, context_overrides(git, tree))
        report["candidate_commit"] = commit
        write_receipt(args.output, args.repo, report)
        if args.navigation_output:
            write_navigation(args.navigation_output, args.repo,
                             navigation_markdown(report, safe_path(args.navigation_repository_path)))
        print(json.dumps({k: report[k] for k in ("status", "candidate_commit", "documents_checked", "reference_counts", "historical_mapping_counts")}))
        return int(bool(report["active_blocking_references"]))
    except (ReferenceError, OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print("migration-navigation: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
