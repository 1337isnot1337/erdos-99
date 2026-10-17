"""Exact operational edits after the completed migration; frozen proofs stay fixed.

The listed baseline identities are public Git objects at the pinned commit.
Every changed file retains an exact byte/mode archive. This layer does not
authorize mathematical edits or weaken the original migration policy.
"""
from __future__ import annotations
import hashlib
import json

BASELINE = "2de788bf461d765859be99152ce40318b3e9bcbe"
LEDGER = "docs/publication/publication-polish-20261017.json"
ARCHIVE = "docs/archive/publication-polish-20261017/"
BASELINE_ENTRIES = {
    "README.md": [
        "100644",
        "6324ff1fd8885ef7a8a5cf4dcaea5aafa0e25569"
    ],
    "CITATION.cff": [
        "100644",
        "4c8fc3c8556ce39c983aad23d595aaf0f56b5810"
    ],
    "scripts/choose_research_task.py": [
        "100755",
        "dc16cb3f6c3698290c7bde9f1b655d697e2f8fc4"
    ],
    "docs/launch/GATE_2_VERIFICATION.md": [
        "100644",
        "a701f5b1b4e3f1f1f645f2871392754c7a554da5"
    ],
    "docs/launch/READINESS.md": [
        "100644",
        "71579e4116156abea52b6e0c3931efb707c71d83"
    ],
    "docs/launch/PUBLICATION_AUDIT.md": [
        "100644",
        "b94fa28a143c9031e2abe347401be5ef2225fe27"
    ],
    "tools/check_public.py": [
        "100644",
        "0801b0614b03f75bafcd80ec6a85f70a06b258c9"
    ],
    "tools/verify_publication_candidate.py": [
        "100644",
        "96a884c5facf38441a3f2adc79cc5c022b8196cb"
    ],
    "tools/audit_public_release.py": [
        "100644",
        "654df0bd54d5523370a78f664de3002fdc7c1023"
    ],
    "tools/publication_migration.py": [
        "100644",
        "89a1ee5fea4ba23c9a768960f4a1038a0d703505"
    ],
    "docs/publication/inclusion.json": [
        "100644",
        "2dd1f35f72407d185861db0127429236c1248119"
    ],
    ".github/workflows/migration-namespace-canary.yml": [
        "100644",
        "0db51fcefd1dedf2c4883c7cc739b82d9378e8ee"
    ],
    ".gitattributes": [
        "100644",
        "5e6c655e97456081fc0fdf78a0cb8f76be90b26a"
    ],
    "tools/verify_frozen_target_c_813_migration.py": [
        "100644",
        "76aed04e7996f7b0123cf91c60c67ee43a4669df"
    ]
}


def identity(data, mode):
    return {"mode": mode,
            "git_blob_sha1": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def original_tree(read_blob, tree):
    """Verify all declared operational edits, then expose the preserved baseline."""
    if LEDGER not in tree:
        return tree, set()
    if tree[LEDGER][0] != "100644":
        raise ValueError("publication follow-up ledger has an invalid mode")
    ledger = json.loads(read_blob(tree[LEDGER][1]))
    if (ledger.get("schema") != "erdos-99-publication-polish/v1"
            or ledger.get("baseline_commit") != BASELINE
            or not isinstance(ledger.get("edits"), list)):
        raise ValueError("invalid publication follow-up ledger")
    result = dict(tree)
    seen = set()
    for row in ledger["edits"]:
        path = row.get("path")
        if path not in BASELINE_ENTRIES or path in seen:
            raise ValueError("unapproved or duplicate follow-up path")
        seen.add(path)
        before = tuple(BASELINE_ENTRIES[path])
        original = ARCHIVE + path + ".source"
        if row.get("preserved_original") != original or tree.get(original) != before:
            raise ValueError("exact publication baseline archive missing: " + path)
        if row.get("before") != identity(read_blob(before[1]), before[0]):
            raise ValueError("publication baseline identity mismatch: " + path)
        after = row.get("after")
        current = tree.get(path)
        if after is None:
            if current is not None:
                raise ValueError("retired file remains active: " + path)
        elif (current is None or current[0] not in ("100644", "100755")
              or current[0] != after.get("mode")
              or after != identity(read_blob(current[1]), current[0])):
            raise ValueError("publication edit identity mismatch: " + path)
        if not isinstance(row.get("reason"), str) or not row["reason"].strip():
            raise ValueError("publication edit needs a reason")
        result[path] = before
    changed = {path for path, before in BASELINE_ENTRIES.items()
               if tree.get(path) != tuple(before)}
    if seen != changed:
        raise ValueError("publication follow-up inventory is incomplete")
    return result, seen
