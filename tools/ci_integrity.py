#!/usr/bin/env python3
"""Fast, trusted structural checks against a read-only contributed checkout.

This checker never imports or executes Python from the candidate. It intentionally
does not certify mathematical results or replace canonical theorem verification.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
from localized_ci.packages import Invalid, path as safe_path, strict_json, MAX_BLOB
from public_links import markdown_targets

REQUIRED = ("README.md", "AGENTS.md", "autoresearch.md", "CONTRIBUTING.md",
            "LICENSE", "NOTICE")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "--no-replace-objects", "-C", str(root), *args],
        stderr=subprocess.PIPE, timeout=30
    )


def changed_paths(root: Path, base: str) -> list[str]:
    raw = git(root, "diff", "--no-renames", "--name-only", "-z", base, "HEAD", "--")
    return [part.decode("utf-8", "surrogateescape") for part in raw.split(b"\0") if part]


def safe_file(root: Path, relative: str) -> Path:
    safe_path(relative)
    target = root / relative
    if target.is_symlink() or not target.is_file() or not target.resolve().is_relative_to(root):
        raise Invalid("missing/symlink/unsafe file: " + relative)
    return target


def validate(root: Path, base: str) -> list[str]:
    errors = []
    for rel in REQUIRED:
        try:
            safe_file(root, rel)
        except Invalid as exc:
            errors.append(str(exc))

    index = root / "tasks/index.json"
    if index.exists():
        try:
            obj = strict_json(safe_file(root, "tasks/index.json").read_bytes())
            if not isinstance(obj, dict) or not isinstance(obj.get("tasks"), list):
                raise Invalid("task catalogue must have a tasks array")
            used = set()
            for entry in obj["tasks"]:
                if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
                    raise Invalid("task entry without an id")
                if entry["id"] in used:
                    raise Invalid("duplicate task id " + entry["id"])
                used.add(entry["id"])
                if isinstance(entry.get("path"), str):
                    safe_file(root, entry["path"])
        except (Invalid, ValueError, UnicodeError, OSError) as exc:
            errors.append("tasks/index.json: " + str(exc))

    try:
        changed = changed_paths(root, base)
    except (OSError, subprocess.SubprocessError) as exc:
        return errors + ["cannot read trusted change range: " + str(exc)]
    for rel in changed:
        candidate = root / rel
        if not candidate.exists() and not candidate.is_symlink():
            continue
        try:
            file = safe_file(root, rel)
            if file.stat().st_size > MAX_BLOB:
                raise Invalid("changed input too large for Tier 0: " + rel)
            if rel.endswith(".json"):
                strict_json(file.read_bytes())
            elif rel.endswith(".md"):
                content = file.read_text(encoding="utf-8")
                for target in markdown_targets(rel, content):
                    linked = (root / target).resolve()
                    if not linked.is_relative_to(root) or not linked.exists():
                        errors.append(rel + ": broken or unsafe local link: " + target)
        except (Invalid, OSError, ValueError, UnicodeError) as exc:
            errors.append(rel + ": " + str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--base-ref", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    failures = validate(root, args.base_ref)
    from check_public import validate as public_validate
    from check_theorem_state_pr import Checker as StateChecker
    class TrustedChecker(StateChecker):
        def run_subcheck(self, script):
            result = subprocess.run([sys.executable, '-I', str(TOOLS / Path(script).name),
                                     '--root', str(self.root)], cwd=self.root,
                                    capture_output=True, text=True, timeout=30)
            if result.returncode:
                self.err(f'{script}: {result.stdout}{result.stderr}')
    failures.extend(TrustedChecker(root, base_ref=args.base_ref).run())
    public_errors, _ = public_validate(root)
    failures.extend(public_errors)
    for error in failures:
        print("integrity: " + error)
    print(f"integrity: {len(failures)} structural errors; mathematical verification not attempted")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
