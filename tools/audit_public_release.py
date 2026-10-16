#!/usr/bin/env python3
"""Fail-closed release audit for a curated E99 repository.

Independent of the theorem verifier: checks publication boundaries, recorded
source inventory, exact public file hashes, credential markers in current
and historical blobs or commit messages, and all reachable commit metadata. It is NOT legal rights clearance, mathematical proof review,
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
SAFE_EXACT_EMAILS = {"noreply@github.com"}
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def safe_email(email: str) -> bool:
    """Recognize explicit noreply forms without allowing whole provider domains."""
    normalized = email.casefold()
    return normalized in SAFE_EXACT_EMAILS or normalized.endswith(SAFE_EMAIL_SUFFIXES)


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
    # Final-candidate evidence must describe Git objects, never substituted worktree bytes.
    return json.loads(git(root, "show", "HEAD:" + path))


OWNER_RIGHTS_RECORD = "docs/publication/owner-rights-authorization.json"
OWNER_APPROVED_MANIFEST_BLOB = "f521850703b01b204399613d640a0b99ca895080"
OWNER_RIGHTS_EVIDENCE = "https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207244081"
OWNER_EMAIL_EVIDENCE = "https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207434631"
OWNER_APPROVED_EMAIL = "cinnajdavis@gmail.com"


def attested_owner_permissions(root: Path, manifest: dict) -> dict | None:
    """Check the exact owner-granted source scope; never infer rights from a scan.

    This records an external, owner-authored confirmation pinned to one immutable
    inclusion-manifest Git blob. No generic waiver for arbitrary source files or
    personal Git authors is allowed. GitHub owner identity and license exceptions
    still require release-owner judgment independent of this structural check.
    """
    try:
        record = read_json(root, OWNER_RIGHTS_RECORD)
        blob = git(root, "rev-parse", "HEAD:docs/publication/inclusion.json").decode("ascii").strip()
        entries = manifest["entries"]
        m = record["source_manifest"]
        owner = record["owner_declaration"]
        external = record["external_expression_review"]
        bounds = record["release_boundaries"]
        if record.get("schema_version") != 1 or record.get("repository") != "1337isnot1337/erdos-99":
            return None
        if not HEX40.fullmatch(blob) or m.get("path") != "docs/publication/inclusion.json" or m.get("git_blob_sha") != OWNER_APPROVED_MANIFEST_BLOB or blob != OWNER_APPROVED_MANIFEST_BLOB:
            return None
        if not entries or m.get("retained_source_records") != len(entries) or m.get("source_pins") != len({e["source_commit"] for e in entries}):
            return None
        if owner.get("evidence_url") != OWNER_RIGHTS_EVIDENCE or owner.get("disposition") != "OWNER AUTHORIZED FOR PROJECT-CONTROLLED SOURCE EXPRESSION":
            return None
        if not owner.get("license_terms", "").startswith("Apache-2.0"):
            return None
        if external.get("confirmed_uncleared_redistributed_third_party_exceptions") != []:
            return None
        if bounds.get("repository_visibility_change_authorized") is not False:
            return None
        emails = set()
        metadata = record.get("history_email_consent", {})
        if metadata.get("comment_url") == OWNER_EMAIL_EVIDENCE and metadata.get("personal_domain_emails_found") == [OWNER_APPROVED_EMAIL]:
            emails.add(OWNER_APPROVED_EMAIL)
        return {"imported_entries": len(entries), "owner_approved_emails": emails}
    except (KeyError, TypeError, AttributeError, ValueError, UnicodeError, OSError, subprocess.SubprocessError):
        return None


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
    seen_paths: set[str] = set()
    counts = Counter()
    candidate = tree = None

    def finding(where: str, kind: str, detail: str, *, block: bool = True):
        (blockers if block else warnings).append({"path": where, "kind": kind, "detail": detail})

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
    except (subprocess.SubprocessError, ValueError, UnicodeError) as exc:
        finding("<git>", "unavailable-committed-tree", type(exc).__name__)
        entries = []

    for path, mode, typ, blob in entries:
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
            data = git(root, "cat-file", "blob", blob)
        except (OSError, subprocess.SubprocessError) as exc:
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
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError) as error:
        finding("docs/publication/", "invalid-inventory", type(error).__name__)
        inc = None

    owner_perms = attested_owner_permissions(root, inc) if inc is not None else None
    if owner_perms is not None:
        counts["owner_attested_source_rights"] = owner_perms["imported_entries"]
    elif OWNER_RIGHTS_RECORD in seen_paths:
        finding(OWNER_RIGHTS_RECORD, "unverified-owner-rights-record",
                "Owner attestation must match the exact committed inclusion manifest and permission evidence")

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
                actual = hashlib.sha256(git(root, "show", "HEAD:" + dest)).hexdigest()
                if actual != rec.get("public_sha256"):
                    finding(dest, "hash-mismatch", "Published bytes differ from recorded SHA256")
            if rec.get("publication_clearance", "").startswith("pending"):
                if owner_perms is not None:
                    counts["owner_attested_pending_source_records"] += 1
                else:
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

    # HEAD-only scans are insufficient for publication. Git exposes deleted
    # files in ancestor commits and files reachable through other branch refs.
    # Walk every reachable tree; inspect historical-only blob bytes as well.
    try:
        history_revs = git(root, "rev-list", "--all").decode("ascii").splitlines()
        current_blobs = {oid for _, _, kind, oid in entries if kind == "blob"}
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
            for role, email in (("author", author), ("committer", committer)):
                if "@" in email and not safe_email(email):
                    if owner_perms is not None and email.casefold() in owner_perms["owner_approved_emails"]:
                        counts["owner_authorized_git_email_occurrences"] += 1
                    else:
                        counts["personal_domain_git_emails"] += 1
                        finding("<git:" + sha[:12] + ">", "personal-git-email",
                                "Reachable " + role + " email uses a personal/non-noreply domain; owner must approve or sanitize history")
    except (subprocess.SubprocessError, UnicodeError) as error:
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
                for label, pattern in PRIVATE_REFERENCE_PATTERNS.items():
                    if pattern.search(data) and (kind != 'blob' or oid not in current_blobs):
                        finding(where, 'historical-private-reference', label + ' in reachable history; review suitability', block=False)
                if kind in ("commit", "tag"):
                    for email in re.findall(rb"(?im)^(?:tagger |co-authored-by: )[^\n]*<([^<>\n]+)>", data):
                        decoded_email = email.decode("utf-8", "replace")
                        if b"@" in email and not safe_email(decoded_email):
                            visible = email.decode("utf-8", "replace").casefold()
                            if owner_perms is not None and visible in owner_perms["owner_approved_emails"]:
                                counts["owner_authorized_trailer_email_occurrences"] += 1
                            else:
                                finding(where, "personal-git-trailer-or-tag-email", "Tagger or contributor trailer has non-noreply metadata; values redacted")
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
            "Historical scan covers refs reachable with git --all, not unreachable loose objects.",
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

