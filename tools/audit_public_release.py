#!/usr/bin/env python3
"""Fail-closed release audit for a curated E99 repository.

Independent of the theorem verifier: checks publication boundaries, recorded
source inventory, exact public file hashes, known credential markers and reachable
commit metadata. It is NOT legal rights clearance, mathematical proof review,
or an all-pattern secret scanner.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

RESTRICTED_PREFIXES = ("papers/", "extracted/", ".git/", ".private/")
RESTRICTED_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp", ".zip", ".tar", ".7z")
TOKEN_PATTERNS = {
    "github-token": re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b"),
    "openai-key": re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    "google-key": re.compile(rb"\bAIza[0-9A-Za-z_-]{35}\b"),
    "pem-private-key": re.compile(rb"(?m)^-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----\r?$"),
}
PRIVATE_REFERENCE_PATTERNS = {
    "private-source-url": re.compile(rb"https?://(?:www\.)?github\.com/1337isnot1337/e-99(?:[/#?]|\b)"),
    "private-worktree-path": re.compile(rb"(?:/tmp/e99-private|/home/oai/|/workspace/projects/)"),
}
SAFE_EMAIL_SUFFIXES = ("@users.noreply.github.com", "@noreply.github.com", "@example.invalid")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "--no-replace-objects", "-C", str(root), *args],
        timeout=30, stderr=subprocess.PIPE,
    )


def allowed_relative(raw: object) -> bool:
    if not isinstance(raw, str) or not raw or raw.startswith(("/", "-", "./")):
        return False
    if "\\" in raw or "\x00" in raw or any(part in ("", ".", "..") for part in raw.split("/")):
        return False
    return PurePosixPath(raw).as_posix() == raw


def read_json(root: Path, path: str):
    return json.loads((root / path).read_text(encoding="utf-8"))


def audit(root: Path, *, scan_content: bool = True) -> dict:
    root = root.resolve()
    blockers: list[dict] = []
    warnings: list[dict] = []
    seen_paths: set[str] = set()
    counts = Counter()

    def finding(where: str, kind: str, detail: str, *, block: bool = True):
        (blockers if block else warnings).append({"path": where, "kind": kind, "detail": detail})

    try:
        raw = git(root, "ls-tree", "-r", "-z", "HEAD")
        entries = []
        for rec in raw.split(b"\x00"):
            if not rec:
                continue
            meta, name = rec.split(b"\t", 1)
            mode, typ, sha = meta.decode().split()
            path = name.decode("utf-8", "surrogateescape")
            entries.append((path, mode, typ, sha))
        counts["committed_files"] = len(entries)
    except (subprocess.SubprocessError, ValueError, UnicodeError) as exc:
        finding("<git>", "unavailable-committed-tree", type(exc).__name__)
        entries = []

    for path, mode, typ, _ in entries:
        seen_paths.add(path)
        if not allowed_relative(path):
            finding(path, "unsafe-path", "Noncanonical repository path")
        if typ != "blob" or mode not in ("100644", "100755"):
            finding(path, "special-object", "Git mode/type is not a regular file")
        if path.startswith(RESTRICTED_PREFIXES) or path.lower().endswith(RESTRICTED_EXTENSIONS):
            finding(path, "restricted-redistribution", "Third-party/binary source requires independent clearance")
        target = root / path
        if target.is_symlink() or not target.is_file():
            finding(path, "symlink-or-missing", "Committed path not present as a regular file")
            continue
        if not target.resolve().is_relative_to(root):
            finding(path, "path-escape", "Committed path escapes the checkout")
            continue
        if not scan_content:
            continue
        try:
            data = target.read_bytes()
        except OSError as exc:
            finding(path, "unreadable", type(exc).__name__)
            continue
        counts["content_bytes"] += len(data)
        for label, pattern in TOKEN_PATTERNS.items():
            if pattern.search(data):
                finding(path, "credential-indicator", label + " matched; inspect privately; no secret values are logged")
        for label, pattern in PRIVATE_REFERENCE_PATTERNS.items():
            if pattern.search(data):
                finding(path, "private-reference", label + " occurs; determine whether the reference is appropriate", block=False)

    manifest_path = root / "docs/publication/inclusion.json"
    exclusion_path = root / "docs/publication/exclusion.json"
    inc = exc = None
    try:
        inc = read_json(root, "docs/publication/inclusion.json")
        exc = read_json(root, "docs/publication/exclusion.json")
        if not isinstance(inc, dict) or not isinstance(inc.get("entries"), list):
            raise ValueError("inclusion manifest requires entries array")
        if not isinstance(exc, list):
            raise ValueError("exclusion manifest requires an array")
    except (OSError, ValueError, UnicodeError) as error:
        finding("docs/publication/", "invalid-inventory", type(error).__name__)
        inc = None

    if inc is not None:
        included = set()
        source_paths = set()
        source_commit = inc.get("source_commit")
        if not isinstance(source_commit, str) or not HEX40.fullmatch(source_commit):
            finding("docs/publication/inclusion.json", "source-commit", "Invalid pinned source SHA")
        for rec in inc["entries"]:
            if not isinstance(rec, dict):
                finding("docs/publication/inclusion.json", "entry-schema", "Nonobject retained entry")
                continue
            dest = rec.get("public_path")
            source_path = rec.get("source_path")
            counts["imported_entries"] += 1
            if not allowed_relative(dest) or not allowed_relative(source_path):
                finding(str(dest), "invalid-included-path", "Unsafe or absent source/public path")
                continue
            if dest in included:
                finding(dest, "duplicate-included-path", "Same destination recorded twice")
            included.add(dest)
            source_paths.add(source_path)
            for field, length in (("source_blob", 40), ("source_sha256", 64), ("public_sha256", 64)):
                val = rec.get(field)
                if not isinstance(val, str) or (HEX40 if length == 40 else HEX64).fullmatch(val) is None:
                    finding(dest, "invalid-provenance", field + " is absent or malformed")
            if dest not in seen_paths:
                finding(dest, "missing-import", "Retained source absent from committed tree")
                continue
            if scan_content:
                actual = hashlib.sha256((root / dest).read_bytes()).hexdigest()
                if actual != rec.get("public_sha256"):
                    finding(dest, "hash-mismatch", "Published bytes differ from recorded SHA256")
            if rec.get("publication_clearance", "").startswith("pending"):
                counts["pending_rights_reviews"] += 1
            elif rec.get("publication_clearance") not in ("approved", "cleared"):
                counts["unknown_rights_reviews"] += 1
            for dep in rec.get("dependencies", []):
                if not allowed_relative(dep) or dep not in seen_paths:
                    finding(dest, "missing-declared-dependency", "Declared prerequisite omitted or unsafe")
                else:
                    counts["declared_dependency_edges"] += 1
        if inc.get("unresolved_dependencies"):
            finding("docs/publication/inclusion.json", "unresolved-dependencies",
                    str(len(inc["unresolved_dependencies"])) + " source dependencies unresolved")
        if exc is not None:
            excluded = []
            for rec in exc:
                path = rec.get("source_path") if isinstance(rec, dict) else None
                if not allowed_relative(path):
                    finding("docs/publication/exclusion.json", "invalid-exclusion", "Noncanonical excluded path")
                    continue
                excluded.append(path)
            counts["excluded_entries"] = len(excluded)
            if len(set(excluded)) != len(excluded):
                finding("docs/publication/exclusion.json", "duplicate-exclusion", "Excluded path duplicated")
            overlap = source_paths & set(excluded)
            if overlap:
                finding("docs/publication/", "inclusion-exclusion-conflict", str(len(overlap)) + " source paths both included and excluded")
        if counts["pending_rights_reviews"] or counts["unknown_rights_reviews"]:
            finding("docs/publication/inclusion.json", "rights-clearance-pending",
                    f'{counts["pending_rights_reviews"]} pending and {counts["unknown_rights_reviews"]} unknown source rights; project license does not clear them')

    try:
        log = git(root, "log", "--all", "--format=%H%x00%ae%x00%ce%x00").decode("utf-8")
        fields = log.split("\x00")
        counts["reachable_commits"] = 0
        for i in range(0, len(fields) - 2, 3):
            sha, author, committer = fields[i].strip(), fields[i+1], fields[i+2]
            if not HEX40.fullmatch(sha):
                continue
            counts["reachable_commits"] += 1
            for role, email in (("author", author), ("committer", committer)):
                if "@" in email and not email.lower().endswith(SAFE_EMAIL_SUFFIXES):
                    counts["personal_domain_git_emails"] += 1
                    finding("<git:" + sha[:12] + ">", "personal-git-email",
                            "Reachable " + role + " email uses a personal/non-noreply domain; owner must approve or sanitize history")
    except (subprocess.SubprocessError, UnicodeError) as error:
        finding("<git>", "history-scan-failure", type(error).__name__)

    return {
        "status": "BLOCKED" if blockers else "STRUCTURAL_PRECHECK_PASSED",
        "counts": dict(sorted(counts.items())),
        "blockers": blockers,
        "warnings": warnings,
        "limits": [
            "This tool cannot grant copyright rights or verify contributor consent.",
            "No regex scan certifies absence of every possible secret.",
            "Machine-valid dependency paths do not prove implicit mathematical dependency closure.",
            "Proof review, clean-history origin, hosted-CI safety and anonymous public onboarding remain separate gates.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--skip-content", action="store_true", help="Only structural checks; NOT a publication clearance")
    ap.add_argument("--output", type=Path, help="Write a JSON report to this private local path")
    args = ap.parse_args()
    result = audit(args.root, scan_content=not args.skip_content)
    output = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(output + "\n")
    print(json.dumps({
        "status": result["status"],
        "counts": result["counts"],
        "blocker_count": len(result["blockers"]),
        "warning_count": len(result["warnings"]),
        "blockers_by_type": dict(Counter(x["kind"] for x in result["blockers"])),
        "warnings_by_type": dict(Counter(x["kind"] for x in result["warnings"])),
    }, indent=2, sort_keys=True))
    return int(bool(result["blockers"]))


if __name__ == "__main__":
    sys.exit(main())

