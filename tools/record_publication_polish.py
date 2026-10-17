#!/usr/bin/env python3
"""Record explicitly scoped operational edits and preserve their exact originals."""
import json
from pathlib import Path
import subprocess

from publication_followup import ARCHIVE, BASELINE, BASELINE_ENTRIES, LEDGER, identity

ROOT = Path(__file__).resolve().parents[1]
REASONS = {
    "README.md": "Route readers through the generated math edition; expose glossary, bibliography and current release summary.",
    "CITATION.cff": "Identify the dated 0.1.0-rc.1 release candidate.",
    "scripts/choose_research_task.py": "Resolve prerequisite IDs through the generated authoritative graph rather than literal proof prose.",
    "docs/launch/GATE_2_VERIFICATION.md": "Replace stale PR16 status and document direct newcomer/reading checks.",
    "docs/launch/READINESS.md": "Prepend current publication status; preserve the complete previous narrative.",
    "docs/launch/PUBLICATION_AUDIT.md": "Prepend current publication status; preserve the complete previous narrative.",
    "tools/check_public.py": "Check every generated reading page in ordinary public integrity validation.",
    "tools/verify_publication_candidate.py": "Directly exercise the published selector and reading-edition entry commands.",
    "tools/audit_public_release.py": "Retain unchanged owner-granted source scope across the exact archived operational selector edit.",
    "tools/publication_migration.py": "Validate exact archived post-migration operational edits before the unchanged historical policy.",
    "docs/publication/inclusion.json": "Update only the selector's actual public hash and editorial description; all source and rights identities unchanged.",
    ".github/workflows/migration-namespace-canary.yml": "Retire the completed PR75-only canary while retaining its exact archived bytes and mode.",
}


def main():
    edits = []
    for path, (mode, blob) in BASELINE_ENTRIES.items():
        original = subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(ROOT), "show", BASELINE + ":" + path])
        assert identity(original, mode)["git_blob_sha1"] == blob
        target = ROOT / path
        if target.is_symlink():
            raise ValueError("operational target must be regular: " + path)
        after = (identity(target.read_bytes(), "100755" if target.stat().st_mode & 0o111 else "100644")
                 if target.exists() else None)
        before = identity(original, mode)
        if before == after:
            continue
        archived = ARCHIVE + path + ".source"
        saved = ROOT / archived
        if saved.exists() and saved.read_bytes() != original:
            raise ValueError("refusing to overwrite a different original: " + archived)
        saved.parent.mkdir(parents=True, exist_ok=True)
        saved.write_bytes(original)
        saved.chmod(0o755 if mode == "100755" else 0o644)
        edits.append({"path": path, "before": before, "after": after,
                      "preserved_original": archived, "reason": REASONS[path]})
    result = {"schema": "erdos-99-publication-polish/v1", "baseline_commit": BASELINE,
              "scope": "Owner-directed operational and presentation fixes; no mathematical promotion or source-rights extension.",
              "edits": edits}
    (ROOT / LEDGER).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(f"Recorded {len(edits)} exact operational edits; originals preserved.")


if __name__ == "__main__":
    main()
