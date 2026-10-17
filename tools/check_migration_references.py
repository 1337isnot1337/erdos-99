#!/usr/bin/env python3
"""Check literal links in documents named by the migration link receipt.

A file preserved in another archive does not repair a literal relative link.
This check does not execute research code or certify mathematical claims.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = "docs/research/migration/2026-10-16/"
RECEIPT = ROOT + "agent-3/evidence/markdown-link-audit.json"
INVENTORY = ROOT + "agent-1/evidence/source-main-three-way-assignment.jsonl"
PINNED_EVIDENCE = {
    RECEIPT: "364cef4f5bccbf81f7bfa3f0d88b263abc55c0fb",
    INVENTORY: "7e465ddb9ff53fb529200531c25844555ac2d4e4",
}
INLINE = re.compile(r"!?\[[^\]\n]*\]\((?:<([^>\n]+)>|([^\s)]+))(?:\s+[^)\n]*)?\)")
OID = re.compile(r"[0-9a-f]{40}\Z")
REGULAR = {"100644", "100755"}


class ReferenceError(ValueError):
    pass


def safe_path(path: str) -> str:
    if not isinstance(path, str) or not path or "\\" in path:
        raise ReferenceError("Invalid repository path")
    if any(ord(c) < 32 for c in path):
        raise ReferenceError("Control character in repository path")
    if any(p in ("", ".", "..") or p.casefold() == ".git" for p in path.split("/")):
        raise ReferenceError("Unsafe repository path")
    return path


def local_target(document: str, link: str) -> tuple[str, str | None]:
    safe_path(document)
    if not isinstance(link, str) or any(ord(c) < 32 for c in link):
        raise ReferenceError("Invalid link")
    url = urlsplit(link)
    if url.scheme in {"http", "https", "mailto"} or (url.netloc and not url.scheme):
        return "external", None
    if url.scheme or url.netloc:
        raise ReferenceError("Unsupported link scheme")
    if not url.path:
        return "anchor", None
    path = unquote(url.path)
    if path.startswith("/"):
        raise ReferenceError("Rooted link needs an explicit repository mapping")
    result = posixpath.normpath(posixpath.join(posixpath.dirname(document), path))
    return "local", safe_path(result)


def reference_excluded(path: str) -> bool:
    return path.startswith("extracted/") or (
        path.startswith("papers/") and not path.endswith((".md", ".bib", ".json")))


def analyze(receipt: dict, tree: dict[str, tuple[str, str]],
            documents: dict[str, str], source: dict[str, str]) -> dict:
    rows = receipt.get("unresolved_relative_links")
    if not isinstance(rows, list):
        raise ReferenceError("Missing unresolved-reference inventory")
    hints = {}
    selected = set()
    for row in rows:
        document = safe_path(row["markdown_destination"])
        original = safe_path(row["markdown_source_path"])
        link = row["link_target"]
        kind, source_target = local_target(original, link)
        if kind != "local" or source_target != row["normalized_source_target"]:
            raise ReferenceError("Reference record has an inconsistent source target")
        key = (document, link)
        if key in hints and hints[key] != source_target:
            raise ReferenceError("Conflicting reference records")
        hints[key] = source_target
        selected.add(document)
    by_blob = defaultdict(list)
    for path, (mode, oid) in tree.items():
        if mode in REGULAR:
            by_blob[oid].append(path)
    records, errors = [], []
    for document in sorted(selected):
        if document not in documents or tree.get(document, (None, None))[0] not in REGULAR:
            errors.append({"document": document, "status": "missing_document"})
            continue
        actual_links = {m.group(1) or m.group(2) for m in INLINE.finditer(documents[document])}
        for link in sorted(actual_links):
            record = {"document": document, "link": link}
            try:
                kind, target = local_target(document, link)
            except ReferenceError as exc:
                record.update(status="unsafe_reference", reason=str(exc))
                records.append(record)
                continue
            record["target"] = target
            if kind != "local":
                record["status"] = kind
            elif target in tree and tree[target][0] in REGULAR:
                record["status"] = "resolved_file"
            elif target in tree:
                record["status"] = "unsupported_target_mode"
            elif any(p.startswith(target + "/") for p in tree):
                record["status"] = "resolved_directory"
            else:
                source_target = hints.get((document, link), target)
                record["source_target"] = source_target
                if reference_excluded(source_target):
                    record["status"] = "reference_not_redistributed"
                else:
                    copies = sorted(by_blob.get(source.get(source_target), []))
                    record["status"] = "missing_link_preserved_elsewhere" if copies else "missing_link_and_content"
                    record["exact_archive_candidates"] = copies
            records.append(record)
        for (hint_document, link), target in hints.items():
            if hint_document == document and link not in actual_links:
                records.append({"document": document, "link": link, "source_target": target,
                                "status": "historical_receipt_link_changed_or_not_inline"})
    blocking = {"unsafe_reference", "unsupported_target_mode", "missing_link_preserved_elsewhere",
                "missing_link_and_content", "historical_receipt_link_changed_or_not_inline"}
    failures = errors + [r for r in records if r["status"] in blocking]
    return {"schema_version": 1, "documents_checked": len(selected),
            "counts": dict(Counter(r["status"] for r in records)), "references": records,
            "errors": errors, "blocking_references": failures,
            "status": "PASS_RECORDED_DOCUMENT_PATHS_ONLY" if not failures else "BLOCKED",
            "deprecation_ready": False, "release_verified": False, "mathematical_proof": False,
            "limits": ["Only documents named by the earlier receipt are scanned.",
                       "Only inline Markdown links are parsed. Fragments are not verified.",
                       "External reference bytes are not redistributed or fetched.",
                       "Archive presence does not resolve a broken literal link.",
                       "This is not source coverage, import closure, or Gate 2 verification."]}


class GitReader:
    def __init__(self, path: Path):
        self.path = path.resolve()

    def run(self, *args: str) -> bytes:
        proc = subprocess.run(["git", "-C", str(self.path), *args], capture_output=True)
        if proc.returncode:
            raise ReferenceError(proc.stderr.decode("utf-8", "replace").strip())
        return proc.stdout

    def tree(self, ref: str) -> tuple[str, dict[str, tuple[str, str]]]:
        commit = self.run("rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()
        result = {}
        for entry in self.run("ls-tree", "-rz", "--full-tree", commit).split(b"\0"):
            if not entry:
                continue
            head, path = entry.split(b"\t", 1)
            mode, kind, oid = head.decode().split()
            path = safe_path(path.decode("utf-8"))
            result[path] = (mode, oid)
        return commit, result

    def text(self, tree: dict, path: str) -> str:
        mode, oid = tree.get(path, (None, None))
        if mode not in REGULAR or not OID.fullmatch(oid or ""):
            raise ReferenceError("Missing regular file: " + path)
        data = self.run("cat-file", "blob", oid)
        if hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() != oid:
            raise ReferenceError("Blob identity mismatch: " + path)
        return data.decode("utf-8")


def require_recorded_blobs(tree: dict) -> None:
    for path, expected in PINNED_EVIDENCE.items():
        if tree.get(path) != ("100644", expected):
            raise ReferenceError("Historical evidence changed: " + path)


def write_receipt(output: Path, repo: Path, result: dict) -> None:
    output = output.absolute()
    if output.is_relative_to(repo.resolve()) or output.exists() or output.is_symlink():
        raise ReferenceError("Receipt must be new and outside the checkout")
    if any(parent.is_symlink() for parent in output.parents):
        raise ReferenceError("Receipt path has a symlink ancestor")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        git = GitReader(args.repo)
        commit, tree = git.tree(args.ref)
        require_recorded_blobs(tree)
        receipt = json.loads(git.text(tree, RECEIPT))
        inventory = [json.loads(line) for line in git.text(tree, INVENTORY).splitlines() if line.strip()]
        source = {}
        for row in inventory:
            path, oid = safe_path(row["source_path"]), row["source_git_blob_sha1"]
            if path in source or not OID.fullmatch(oid):
                raise ReferenceError("Invalid or duplicate source identity")
            source[path] = oid
        paths = {r["markdown_destination"] for r in receipt["unresolved_relative_links"]}
        docs = {p: git.text(tree, p) for p in paths if tree.get(p, (None, None))[0] in REGULAR}
        report = analyze(receipt, tree, docs, source)
        report.update(candidate_commit=commit, reference_receipt=RECEIPT)
        write_receipt(args.output, args.repo, report)
        print(json.dumps({k: report[k] for k in ("status", "candidate_commit", "counts")}))
        return int(bool(report["blocking_references"]))
    except (ReferenceError, OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print("migration-references: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
