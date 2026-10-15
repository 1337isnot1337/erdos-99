#!/usr/bin/env python3
"""Run every computational certificate attached to a theorem-ledger entry."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

BUCKETS = ("current_canonical_entries", "audited_working", "regressions", "rejected_or_overridden")

# Only reviewed workflow prose can skip computation. All other paths fail
# closed, including every research file (registered or not). This intentionally
# covers imports of imports, dynamic imports, globbed/relative inputs, removals
# and renames without pretending to infer a complete dependency graph.
SAFE_PROSE_PATHS = {
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "autoresearch.md",
    "docs/README.md", "docs/START_HERE.md", "docs/GLOSSARY.md",
    "docs/COORDINATION.md", "docs/REVIEW_POLICY.md",
    "docs/RESEARCH_WORKFLOW.md", ".github/copilot-instructions.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
}
SAFE_PROSE_PREFIXES = ("docs/launch/", "docs/prompts/")



@dataclass(frozen=True)
class CertificateSelection:
    """A missing paths tuple means run all registered certificates."""

    paths: tuple[str, ...] | None
    reason: str


def entry_records(state: dict[str, Any]) -> Iterable[tuple[str, str, dict[str, Any]]]:
    for target, target_state in state.get("targets", {}).items():
        if not isinstance(target_state, dict):
            continue
        for bucket in BUCKETS:
            for entry in target_state.get(bucket, []) or []:
                if isinstance(entry, dict):
                    yield target, bucket, entry


def entries(state: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for _, _, entry in entry_records(state):
        yield entry


def registered_certificates(state: dict[str, Any]) -> dict[str, list[str]]:
    owners: dict[str, list[str]] = {}
    for _, _, entry in entry_records(state):
        ident = str(entry.get("id", "<unknown>"))
        for path in entry.get("certificates", []) or []:
            if isinstance(path, str):
                owners.setdefault(path, []).append(ident)
    return owners


def is_canonical(bucket: str, entry: dict[str, Any]) -> bool:
    return bucket == "current_canonical_entries" or entry.get("status") == "canonical"


def select_certificates(
    state: dict[str, Any], changed_paths: set[str] | None
) -> CertificateSelection:
    """Skip only explicitly reviewed prose; unknown dependencies run all."""
    if changed_paths is None:
        return CertificateSelection(None, "diff unavailable or untrusted; fail closed")
    canonical_sources = set()
    for _, bucket, entry in entry_records(state):
        if is_canonical(bucket, entry):
            canonical_sources.update(entry.get(k) for k in ("report", "audit"))
    for path in sorted(changed_paths):
        if path in canonical_sources:
            return CertificateSelection(None, "a canonical theorem source changed")
        # JSON/YAML under launch is machinery/data, never prose.
        safe = path in SAFE_PROSE_PATHS or (
            path.endswith(".md") and path.startswith(SAFE_PROSE_PREFIXES)
        )
        if not safe:
            return CertificateSelection(None, f"proof/code/data or unknown dependency: {path}")
    return CertificateSelection((), "only reviewed workflow prose changed")


def changed_paths_from_git(
    root: Path, base_ref: str, head_ref: str = "HEAD", *, push: bool = False,
    forced: bool = False,
) -> tuple[set[str] | None, str | None]:
    """Use a PR merge base or a verified fast-forward push's complete tree diff.

    No renames and NUL delimiters preserve both names and unusual filenames.
    Missing/shallow/ambiguous ancestry or dirty trees require full verification.
    """
    def git(*args: str) -> str:
        return subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(root), *args], stderr=subprocess.PIPE,
        ).decode("utf-8", errors="surrogateescape")
    try:
        if forced:
            raise ValueError("forced push")
        if any(not re.fullmatch(r"[A-Za-z0-9_./^~-]+", r) or r.startswith("-")
               for r in (base_ref, head_ref)):
            raise ValueError("unsafe revision")
        if git("rev-parse", "--is-shallow-repository").strip() != "false":
            raise ValueError("shallow ancestry")
        if git("status", "--porcelain", "--untracked-files=all").strip():
            raise ValueError("dirty checkout")
        base = git("rev-parse", "--verify", f"{base_ref}^{{commit}}").strip()
        head = git("rev-parse", "--verify", f"{head_ref}^{{commit}}").strip()
        if git("rev-parse", "HEAD").strip() != head:
            raise ValueError("checkout differs from requested head")
        if push:
            git("merge-base", "--is-ancestor", base, head)
            start = base
        else:
            bases = git("merge-base", "--all", base, head).splitlines()
            if len(bases) != 1:
                raise ValueError("missing or ambiguous merge base")
            start = bases[0]
        output = git("diff", "--no-renames", "--name-only", "-z", start, head, "--")
        return set(output.split("\0")) - {""}, None
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        return None, str(exc)


def changed_paths_from_event(root: Path, event: dict) -> tuple[set[str] | None, str | None]:
    try:
        if "pull_request" in event:
            pr = event["pull_request"]
            return changed_paths_from_git(root, pr["base"]["sha"], pr["head"]["sha"])
        before, after = event["before"], event["after"]
        if any(not isinstance(s, str) or not re.fullmatch(r"[0-9a-f]{40}", s)
               or s == "0" * 40 for s in (before, after)):
            raise ValueError("missing/zero push endpoint")
        if event.get("forced") is not False:
            raise ValueError("push fast-forward metadata absent or forced")
        return changed_paths_from_git(root, before, after, push=True)
    except (KeyError, TypeError, ValueError) as exc:
        return None, str(exc)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--base-ref",
        help="select certificates from a three-dot diff against this base ref; failures run all",
    )
    parser.add_argument("--event-file", type=Path, help="GitHub event JSON for PR/push range")
    parser.add_argument("--plan", action="store_true", help="print selection JSON without execution")
    args = parser.parse_args(argv)
    if args.base_ref and args.event_file:
        parser.error("choose --base-ref or --event-file")
    root = args.root.resolve()
    state = yaml.safe_load((root / "docs/state/theorem-state.yaml").read_text(encoding="utf-8"))
    if not isinstance(state, dict):
        print("certificate-runner: manifest is not a mapping", file=sys.stderr)
        return 1

    owners = registered_certificates(state)

    if not owners:
        print("certificate-runner: no certificates registered")
        return 0

    if args.event_file:
        try:
            changed_paths, git_error = changed_paths_from_event(root, json.loads(args.event_file.read_text()))
        except (OSError, ValueError) as exc:
            changed_paths, git_error = None, str(exc)
        selection = select_certificates(state, changed_paths)
    elif args.base_ref:
        changed_paths, git_error = changed_paths_from_git(root, args.base_ref)
        selection = select_certificates(state, changed_paths)
        if git_error:
            print(
                f"certificate-runner: WARNING unable to compute PR diff ({git_error}); running all",
                file=sys.stderr,
            )
    else:
        selection = CertificateSelection(None, "full verification requested")

    selected = set(owners) if selection.paths is None else set(selection.paths)
    if args.plan:
        print(json.dumps({"full": selection.paths is None, "reason": selection.reason,
                          "count": len(selected), "paths": sorted(selected)}, sort_keys=True))
        return 0
    print(
        f"certificate-runner: selection={len(selected)}/{len(owners)} ({selection.reason})",
        flush=True,
    )
    if not selected:
        print("certificate-runner: OK (no affected certificates)")
        return 0

    for rel in sorted(selected):
        path = root / rel
        if not path.is_file():
            print(f"certificate-runner: missing {rel} for {owners[rel]}", file=sys.stderr)
            return 1
        if path.suffix != ".py":
            print(f"certificate-runner: unsupported certificate type: {rel}", file=sys.stderr)
            return 1
        print(f"certificate-runner: RUN {rel} <- {', '.join(sorted(owners[rel]))}", flush=True)
        proc = subprocess.run([sys.executable, path.name], cwd=path.parent)
        if proc.returncode:
            print(f"certificate-runner: FAIL {rel} ({proc.returncode})", file=sys.stderr)
            return proc.returncode
        print(f"certificate-runner: PASS {rel}", flush=True)

    print(f"certificate-runner: OK ({len(selected)} selected of {len(owners)} unique certificates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
