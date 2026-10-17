"""Validate the exact historical snapshots retained by the October migration.

Historical payloads keep their original bytes and source-relative references.
Their navigation is reported separately by audit_migration_navigation.py.
This policy never exempts security scanning or current claim prerequisites.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess

ROOT = "docs/research/migration/2026-10-16/"
POLICY = ROOT + "integration/integrity-policy.json"
FROZEN = ROOT + "frozen-target-c-813-dispositions.jsonl"
CAPTURE = "f282d53169df4d507117893bfdcc99f663855923"
BASE = "c6e0394b3152d21075328bf4f26e6c070229bf13"
SOURCE = "42f0296d1aca068c809f74cee5dcdb4ebdb27c73"
STATUS_DOCUMENTS = frozenset({"docs/launch/READINESS.md", "docs/launch/PUBLICATION_AUDIT.md"})
SUPPORT_CHANGES = frozenset({"tools/check_public.py", "tools/build_artifact_index.py",
                             "docs/state/artifact-index.jsonl", "tools/verify_publication_candidate.py",
                             "docs/publication/inclusion.json", "tools/audit_public_release.py",
                             "tools/verify_frozen_target_c_813_migration.py"}) | STATUS_DOCUMENTS
HISTORICAL_ROOTS = (
    "docs/archive/source-e99-branches/",
    ROOT + "agent-1/payload/",
    ROOT + "agent-2/corpus/source-main/",
    ROOT + "agent-2/branches/",
)


def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value:
        raise ValueError("invalid migration policy path")
    if any(part in ("", ".", "..") or part.lower() == ".git" for part in value.split("/")):
        raise ValueError("unsafe migration policy path: " + value)
    return value


def blob_hash(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def historical_candidate(path):
    return path.startswith(HISTORICAL_ROOTS) and path.endswith((".md", ".py"))


def parse_policy(data):
    policy = json.loads(data)
    if (not isinstance(policy, dict) or policy.get("schema") != "migration-integrity-policy-v1"
            or policy.get("captured_commit") != CAPTURE or policy.get("baseline_commit") != BASE):
        raise ValueError("invalid migration integrity policy identity")
    for name in ("historical_payloads", "noncanonical_metadata", "baseline_transformations"):
        if (not isinstance(policy.get(name), list)
                or any(not isinstance(row, dict) for row in policy[name])):
            raise ValueError("invalid migration integrity policy list: " + name)
    return policy


def identity_matches(data, row, mode):
    return (isinstance(row, dict) and row.get("mode") == mode
            and row.get("git_blob_sha1") == blob_hash(data)
            and row.get("sha256") == hashlib.sha256(data).hexdigest()
            and row.get("bytes") == len(data))


def git_tree(root, ref):
    result = subprocess.run(["git", "--no-replace-objects", "-C", str(root), "ls-tree", "-rz", ref],
                            check=True, capture_output=True)
    tree = {}
    for raw in result.stdout.split(b"\0"):
        if raw:
            header, path = raw.split(b"\t", 1)
            mode, kind, sha = header.decode().split()
            if kind != "blob":
                raise ValueError("unsupported migration capture object")
            tree[path.decode()] = (mode, sha)
    return tree


def regular_bytes(root, path):
    target = Path(root)
    for part in safe_path(path).split("/"):
        target = target / part
        if target.is_symlink():
            raise ValueError("symlink in migration policy input: " + path)
    if not target.is_file():
        raise ValueError("missing regular migration policy input: " + path)
    return target.read_bytes(), "100755" if target.stat().st_mode & 0o111 else "100644"


def load_policy(root):
    """Return validated, exact snapshot sets; absent policy grants no exemption."""
    root = Path(root)
    policy_path = root / POLICY
    if not policy_path.exists():
        return set(), set()
    if policy_path.is_symlink():
        raise ValueError("migration policy must be a regular file")
    policy_data, policy_mode = regular_bytes(root, POLICY)
    if policy_mode != "100644":
        raise ValueError("migration policy mode must be 100644")
    policy = parse_policy(policy_data)
    capture = git_tree(root, CAPTURE)
    historical = set()
    for row in policy["historical_payloads"]:
        path = safe_path(row.get("path"))
        target = root / path
        if path in historical or not historical_candidate(path):
            raise ValueError("invalid or duplicate historical payload: " + path)
        if capture.get(path) != (row.get("mode"), row.get("git_blob_sha1")):
            raise ValueError("historical payload differs from captured Git tree: " + path)
        data, mode = regular_bytes(root, path)
        if not identity_matches(data, row, mode):
            raise ValueError("historical payload byte/mode mismatch: " + path)
        historical.add(path)
    expected = {path for path in capture if historical_candidate(path)}
    if historical != expected:
        raise ValueError("historical payload inventory does not cover the captured snapshot set")

    source_manifests = (
        ROOT + "agent-1/evidence/source-main-three-way-assignment.jsonl",
        ROOT + "agent-1/evidence/source-branches/source-branch-artifacts.jsonl",
        ROOT + "agent-3/branch-dispositions.jsonl",
        ROOT + "agent-3/pr-dispositions.jsonl",
    )
    sources = set()
    for manifest in source_manifests:
        raw, mode = regular_bytes(root, manifest)
        if capture.get(manifest) != (mode, blob_hash(raw)) or mode != "100644":
            raise ValueError("source metadata inventory differs from capture: " + manifest)
        for entry in (json.loads(line) for line in raw.decode().splitlines() if line.strip()):
            sources.add((entry.get("source_path", entry.get("path")),
                         entry.get("source_git_blob_sha1", entry.get("source_blob")),
                         entry.get("source_sha256")))
    frozen_path = root / FROZEN
    baseline = git_tree(root, BASE)
    frozen_bytes, mode = regular_bytes(root, FROZEN)
    if mode != "100644" or baseline.get(FROZEN) != ("100644", blob_hash(frozen_bytes)):
        raise ValueError("frozen metadata ledger differs from the baseline")
    metadata = set()
    for row in policy["noncanonical_metadata"]:
        path = safe_path(row.get("path"))
        target = root / path
        if path in metadata or not path.startswith(("docs/reports/", "docs/audits/")):
            raise ValueError("metadata alternative is not a distinct imported report: " + path)
        data, mode = regular_bytes(root, path)
        if (not identity_matches(data, row, mode)
                or capture.get(path) != (row["mode"], row["git_blob_sha1"])):
            raise ValueError("captured import metadata identity mismatch: " + path)
        first = data.decode().splitlines()[0]
        prefix, suffix = "<!-- migration-provenance: ", " -->"
        if not first.startswith(prefix) or not first.endswith(suffix):
            raise ValueError("captured import has no provenance banner: " + path)
        provenance = json.loads(first[len(prefix):-len(suffix)])
        source_identity = (provenance.get("source_path"), provenance.get("source_blob"),
                           provenance.get("source_sha256"))
        if (provenance.get("destination_status") not in
                {"historical_unreviewed_noncanonical", "unreviewed_noncanonical"}
                or provenance.get("source_canonical") is True
                or provenance.get("source_lifecycle") != "unreviewed"
                or source_identity not in sources):
            raise ValueError("imported report provenance is inconsistent: " + path)
        metadata.add(path)
    return historical, metadata


def reference_exclusions(root):
    root = Path(root)
    path = ROOT + "agent-1/evidence/source-main-three-way-assignment.jsonl"
    raw, mode = regular_bytes(root, path)
    if mode != "100644" or git_tree(root, CAPTURE).get(path) != ("100644", blob_hash(raw)):
        raise ValueError("reference exclusion inventory differs from capture")
    paths = [r["source_path"] for r in (json.loads(line) for line in raw.decode().splitlines() if line.strip())]
    return {p for p in paths if p.startswith("extracted/") or
            (p.startswith("papers/") and not p.endswith((".md", ".bib", ".json")))}


def permitted_baseline_changes(read_blob, tree, base):
    """Validate narrowly scoped support changes using committed Git objects.

    Proofs and frozen reports cannot be changed by this policy. Every changed
    support file retains an exact old copy. Generated index rows may only grow.
    The two release-status documents may only prepend a current status section;
    their complete historical text and regular-file mode must be preserved.
    """
    from publication_followup import original_tree
    tree, followup = original_tree(read_blob, tree)
    changed = {path for path, entry in base.items() if tree.get(path) != entry}
    if not changed:
        return followup
    if not changed <= SUPPORT_CHANGES or POLICY not in tree:
        raise ValueError("unapproved baseline changes: " + ", ".join(sorted(changed)))
    policy = parse_policy(read_blob(tree[POLICY][1]))
    allowed = set()
    for row in policy["baseline_transformations"]:
        path = safe_path(row.get("path"))
        original = safe_path(row.get("preserved_original"))
        if path in allowed or path not in SUPPORT_CHANGES or path not in changed:
            raise ValueError("invalid baseline transformation: " + path)
        if not original.startswith(ROOT + "integration/baseline-originals/") or not original.endswith(".source"):
            raise ValueError("invalid preserved baseline path")
        old, new = base[path], tree.get(path)
        if new is None or tree.get(original) != old:
            raise ValueError("baseline original not preserved: " + path)
        old_data, new_data = read_blob(old[1]), read_blob(new[1])
        if (not identity_matches(old_data, row.get("before"), old[0])
                or not identity_matches(new_data, row.get("after"), new[0])):
            raise ValueError("baseline transformation identity mismatch: " + path)
        if path in STATUS_DOCUMENTS:
            if (old[0] != "100644" or new[0] != "100644" or not old_data
                    or new_data == old_data or not new_data.endswith(old_data)):
                raise ValueError("release status addition changed historical text or mode: " + path)
            prefix = new_data[:-len(old_data)]
            if (not prefix.startswith(b"# Migration completion scope\n\n")
                    or not prefix.endswith(b"\n\n")):
                raise ValueError("release status addition needs a distinct leading section: " + path)
        if path.endswith("artifact-index.jsonl"):
            def index(data):
                rows = [json.loads(line) for line in data.decode().splitlines() if line.strip()]
                result = {r["path"]: r for r in rows}
                if len(result) != len(rows):
                    raise ValueError("duplicate generated index path")
                return result
            old_rows, new_rows = index(old_data), index(new_data)
            if any(new_rows.get(p) != r for p, r in old_rows.items()):
                raise ValueError("existing artifact index rows changed")
            for p in new_rows.keys() - old_rows.keys():
                r = new_rows[p]
                if (r.get("status") != "unreviewed" or r.get("canonical") is not False
                        or r.get("claim_ids") or r.get("claim_statuses")
                        or r.get("depends_on") or r.get("invalidates") or r.get("supersedes")):
                    raise ValueError("new index row promotes a claim: " + p)
        if path == "docs/publication/inclusion.json":
            before, after = json.loads(old_data), json.loads(new_data)
            old_entries, new_entries = before.pop("entries"), after.pop("entries")
            if before != after or len(old_entries) != len(new_entries):
                raise ValueError("source inclusion scope changed")
            for old_entry, new_entry in zip(old_entries, new_entries):
                if old_entry == new_entry:
                    continue
                if old_entry.get("public_path") != "tools/build_artifact_index.py":
                    raise ValueError("unapproved source inclusion edit")
                allowed_fields = {"public_sha256", "editorial_change"}
                if ({k: v for k, v in old_entry.items() if k not in allowed_fields}
                        != {k: v for k, v in new_entry.items() if k not in allowed_fields}):
                    raise ValueError("retained source identities or rights changed")
                actual_hash = hashlib.sha256(read_blob(tree["tools/build_artifact_index.py"][1])).hexdigest()
                if new_entry.get("public_sha256") != actual_hash:
                    raise ValueError("source inclusion editorial hash mismatch")
        if not isinstance(row.get("reason"), str) or not row["reason"].strip():
            raise ValueError("baseline transformation needs a reason")
        allowed.add(path)
    if allowed != changed:
        raise ValueError("baseline transformation inventory is incomplete")
    return allowed | followup
