#!/usr/bin/env python3
"""Fail-closed release audit for a curated E99 repository.

Checks committed paths, regular-file types, worktree cleanliness, and credential
markers in the current tree and reachable Git history. It does not read import
manifests or require historical file hashes to match current files. Ordinary
author, committer, tagger and contributor attribution is allowed.

This is not legal rights clearance, mathematical proof review, or an all-pattern
secret scanner.
"""
from __future__ import annotations

import argparse
from collections import Counter
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
HEX40 = re.compile(r"^[0-9a-f]{40}$")


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


def reachable_objects(root: Path):
    """Read each reachable object once, including non-default and fetched PR refs."""
    records = git(root, "rev-list", "--objects", "--all").splitlines()
    names = {}
    for record in records:
        oid, _, name = record.partition(b" ")
        names[oid.decode("ascii")] = name.decode("utf-8", "surrogateescape")
    # cat-file batch avoids thousands of subprocesses and does not execute repo code.
    proc = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(root), "cat-file", "--batch"],
        input=b"".join(oid.encode() + b"\n" for oid in names),
        capture_output=True, check=True, timeout=120,
    )
    offset = 0
    for expected, name in names.items():
        end = proc.stdout.index(b"\n", offset)
        oid, kind, length = proc.stdout[offset:end].split()
        size = int(length)
        start = end + 1
        data = proc.stdout[start:start + size]
        if oid.decode() != expected or len(data) != size or proc.stdout[start + size:start + size + 1] != b"\n":
            raise ValueError("invalid Git batch response")
        offset = start + size + 1
        yield expected, kind.decode(), name, data


def audit(root: Path, *, scan_content: bool = True) -> dict:
    root = root.resolve()
    blockers: list[dict] = []
    warnings: list[dict] = []
    counts = Counter()
    candidate = tree = None

    def finding(where: str, kind: str, detail: str):
        blockers.append({"path": where, "kind": kind, "detail": detail})

    try:
        candidate = git(root, "rev-parse", "HEAD").decode().strip()
        tree = git(root, "rev-parse", "HEAD^{tree}").decode().strip()
        dirty = git(root, "status", "--porcelain", "--untracked-files=normal").splitlines()
        counts["dirty_worktree_records"] = len(dirty)
        if dirty:
            finding("<worktree>", "dirty-candidate", "Commit or remove pending changes before recording final-candidate evidence")
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
    except (OSError, subprocess.SubprocessError, ValueError, UnicodeError) as exc:
        finding("<git>", "unavailable-committed-tree", type(exc).__name__)
        entries = []

    for path, mode, typ, blob in entries:
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
            data = git(root, "cat-file", "blob", blob)
        except (OSError, subprocess.SubprocessError) as exc:
            finding(path, "unreadable", type(exc).__name__)
            continue
        counts["content_bytes"] += len(data)
        for label, pattern in TOKEN_PATTERNS.items():
            if pattern.search(data):
                finding(path, "credential-indicator", label + " matched; inspect privately; no secret values are logged")

    # HEAD-only scans are insufficient for publication. Git exposes deleted
    # files in ancestor commits and files reachable through other branch refs.
    # Walk every reachable tree; inspect historical-only blob bytes as well.
    current_blobs = {oid for _, _, kind, oid in entries if kind == "blob"}
    try:
        history_revs = git(root, "rev-list", "--all").decode("ascii").splitlines()
        current_entries = set(entries)
        historic_seen = set()
        historic_blobs = {}
        counts["reachable_history_commits_scanned"] = len(history_revs)
        for rev in history_revs:
            if not HEX40.fullmatch(rev):
                raise ValueError("invalid commit SHA in reachable revision list")
            for item in git(root, "ls-tree", "-r", "-z", rev).split(b"\x00"):
                if not item:
                    continue
                meta, name = item.split(b"\t", 1)
                mode, kind, oid = meta.decode("ascii").split()
                rel = name.decode("utf-8", "surrogateescape")
                entry = (rel, mode, kind, oid)
                if entry in current_entries or entry in historic_seen:
                    continue
                historic_seen.add(entry)
                where = "<history:" + rev[:12] + ">/" + rel
                if not allowed_relative(rel):
                    finding(where, "historical-unsafe-path", "Historic path is noncanonical")
                if kind != "blob" or mode not in ("100644", "100755"):
                    finding(where, "historical-special-object",
                            "Historical Git object was not a regular file")
                if rel.startswith(RESTRICTED_PREFIXES) or rel.lower().endswith(RESTRICTED_EXTENSIONS):
                    finding(where, "historical-restricted-redistribution",
                            "A previously committed restricted source remains reachable")
                if kind == "blob" and oid not in current_blobs:
                    historic_blobs.setdefault(oid, (rev, rel))
        counts["historic_distinct_paths_or_versions"] = len(historic_seen)
        counts["historical_only_blobs"] = len(historic_blobs)
        # Content and messages are scanned once in the batched object walk below.
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError):
        finding("<git-history>", "history-blob-audit-incomplete",
                "Unable to inspect all reachable historical paths, blobs and commit messages")

    try:
        log = git(root, "log", "--all", "--format=%H%x00%ae%x00%ce%x00").decode("utf-8")
        fields = log.split("\x00")
        counts["reachable_commits"] = 0
        for i in range(0, len(fields) - 2, 3):
            sha, author, committer = fields[i].strip(), fields[i+1], fields[i+2]
            if not HEX40.fullmatch(sha):
                continue
            counts["reachable_commits"] += 1
            # Standard Git attribution belongs to the contributor's recorded
            # history. Count coverage, but never block on its email domain.
            # Historical commit objects are still independently scanned for
            # credential patterns in the all-object walk below.
            if author:
                counts["git_author_email_metadata_records"] += 1
            if committer:
                counts["git_committer_email_metadata_records"] += 1
    except (OSError, subprocess.SubprocessError, UnicodeError) as error:
        finding("<git>", "history-scan-failure", type(error).__name__)

    if scan_content:
        try:
            for oid, kind, name, data in reachable_objects(root):
                if kind not in ("blob", "commit", "tag"):
                    continue
                counts["reachable_" + kind + "_objects_scanned"] += 1
                # Object ids identify findings without reproducing sensitive paths or values.
                where = "<git-object:" + oid + ">"
                for label, pattern in TOKEN_PATTERNS.items():
                    if pattern.search(data):
                        finding(where, "historical-credential-indicator", label + " matched; inspect privately")
                if kind == 'blob' and oid not in current_blobs:
                    counts['historic_content_bytes'] += len(data)
                if kind in ("commit", "tag"):
                    # Tagger and Co-authored-by metadata is retained, not
                    # suppressed. Any credential contained in the same object
                    # has already been checked by TOKEN_PATTERNS above.
                    counts["git_tag_and_contributor_email_metadata_records"] += len(
                        re.findall(rb"(?im)^(?:tagger |co-authored-by: )[^\n]*<([^<>\n]+)>", data)
                    )
        except (OSError, subprocess.SubprocessError, ValueError, UnicodeError) as error:
            finding("<git>", "historical-content-scan-failure", type(error).__name__)

    return {
        "status": "BLOCKED" if blockers else ("STRUCTURAL_PRECHECK_PASSED" if scan_content else "CONTENT_SCAN_SKIPPED"),
        "candidate_commit": candidate,
        "candidate_tree": tree,
        "full_content_scan": scan_content,
        "counts": dict(sorted(counts.items())),
        "blockers": blockers,
        "warnings": warnings,
        "limits": [
            "This tool cannot grant copyright rights or verify contributor consent.",
            "No regex scan certifies absence of every possible secret.",
            "Ordinary Git attribution metadata is preserved and does not require email-domain consent; credentials in Git objects are still screened.",
            "Historical scan covers refs reachable with git --all, not unreachable loose objects.",
            "Mathematical verification, dependency checks and public onboarding are outside this audit.",
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

