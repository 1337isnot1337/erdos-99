#!/usr/bin/env python3
"""Check that active Target C authority surfaces match the canonical manifest."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

MANIFEST = "docs/state/theorem-state.yaml"
README = "README.md"
TARGET_C_DIR = "docs/targets/target-c"
TARGET_C_CURRENT = "docs/targets/target-c/CURRENT.md"
TARGET_C_README = "docs/targets/target-c/README.md"
TARGET_C_PROMPT = "docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md"
STATE_LOCK = "docs/STATE.md"
ACTIVE_TARGET_C_FILES = (
    README,
    STATE_LOCK,
    TARGET_C_CURRENT,
    TARGET_C_README,
    TARGET_C_PROMPT,
)
TARGET_C_PATH_RE = re.compile(r"^docs/targets/target-c/(\d+)-")
# The early Target C archive intentionally contains duplicate NN-*-frontier.md names.
# The modern theorem-section namespace is the numbered *-audit.md family; collisions
# there make theorem provenance ambiguous and are always an error.
TARGET_C_FILE_RE = re.compile(r"^(\d+)-.*-audit\.md$")
TARGET_C_BULLET_RE = re.compile(
    r"(?ms)^- \*\*Target C:\*\*(.*?)(?=^- \*\*Target [A-Z]:\*\*|^## )"
)
TARGET_C_MAX_RE = re.compile(
    r"Highest-numbered canonical Target C theorem source:\s*Section\s+(\d+)\b",
    re.I,
)
TARGET_C_LEGACY_THROUGH_RE = re.compile(
    r"\bcanonical(?:\s+[A-Za-z-]+){0,5}\s+(?:now\s+|currently\s+)?"
    r"(?:runs\s+|reaches\s+)?through\s+Section\s+(\d+)\b",
    re.I,
)
OBSOLETE_ENDPOINT_PATTERNS = (
    re.compile(r"sharp\s+§?96\s+endpoint", re.I),
    re.compile(r"Section-96\s+boundary\s+endpoint", re.I),
)


def load_state(root: Path) -> dict:
    data = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{MANIFEST} must contain a mapping")
    return data


def numbered_target_c_canonical_sections(state: dict) -> set[int]:
    target = state.get("targets", {}).get("target-c", {})
    if not isinstance(target, dict):
        return set()

    paths: list[str] = []
    for path in target.get("canonical_modules", []) or []:
        if isinstance(path, str):
            paths.append(path)

    for entry in target.get("current_canonical_entries", []) or []:
        if not isinstance(entry, dict) or entry.get("status") != "canonical":
            continue
        report = entry.get("report")
        if isinstance(report, str):
            paths.append(report)

    sections: set[int] = set()
    for path in paths:
        match = TARGET_C_PATH_RE.match(path)
        if match:
            sections.add(int(match.group(1)))
    return sections


def duplicate_target_c_sections(root: Path) -> dict[int, list[str]]:
    target_dir = root / TARGET_C_DIR
    if not target_dir.is_dir():
        return {}

    by_section: dict[int, list[str]] = defaultdict(list)
    for path in target_dir.iterdir():
        if not path.is_file():
            continue
        match = TARGET_C_FILE_RE.match(path.name)
        if match:
            by_section[int(match.group(1))].append(path.name)

    return {
        section: sorted(paths)
        for section, paths in by_section.items()
        if len(paths) > 1
    }


def target_c_summary(readme: str) -> str:
    match = TARGET_C_BULLET_RE.search(readme)
    if match:
        return match.group(1)
    # The newcomer README uses a route table; mathematical assertions do not
    # depend on whether navigation is formatted as a bullet or row.
    row = re.search(r"(?m)^\| \*\*C(?:\s|\*).*?$", readme)
    return row.group(0).replace("**", "") if row else ""


def read_authority_files(root: Path) -> tuple[dict[str, str], list[str]]:
    texts: dict[str, str] = {}
    errors: list[str] = []
    for relative in ACTIVE_TARGET_C_FILES:
        try:
            texts[relative] = (root / relative).read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"cannot read {relative}: {exc}")
    return texts, errors


def run_checks(root: Path) -> list[str]:
    errors: list[str] = []

    duplicates = duplicate_target_c_sections(root)
    for section, paths in sorted(duplicates.items()):
        errors.append(
            f"duplicate Target C audit Section {section} filenames: {', '.join(paths)}"
        )

    try:
        state = load_state(root)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"cannot load {MANIFEST}: {exc}")
        return errors

    texts, read_errors = read_authority_files(root)
    errors.extend(read_errors)
    if read_errors:
        return errors

    summary = target_c_summary(texts[README])
    if not summary:
        errors.append("README.md is missing the Target C route-status summary")
        return errors

    target = state.get("targets", {}).get("target-c", {})
    if isinstance(target, dict):
        for key, label in (("c_i", "C-I"), ("c_ii", "C-II")):
            expected = target.get(key)
            if expected in {"open", "closed"}:
                pattern = re.compile(
                    rf"\b{re.escape(label)}\b\s+(?:is\s+)?{re.escape(expected)}\b",
                    re.I,
                )
                if not pattern.search(summary):
                    errors.append(
                        f"README Target C summary does not declare {label} {expected}"
                    )

    sections = numbered_target_c_canonical_sections(state)
    if not sections:
        errors.append("manifest exposes no numbered canonical Target C theorem source")
        return errors
    expected_max = max(sections)

    max_match = TARGET_C_MAX_RE.search(summary)
    # The maximum section number is optional navigation. If stated it must
    # match; a direct link to the current route avoids maintaining duplicate
    # section inventories in a newcomer guide.
    if max_match and int(max_match.group(1)) != expected_max:
        errors.append(
            "README Target C summary gives highest canonical Section "
            f"{max_match.group(1)}, but the manifest gives Section {expected_max}"
        )

    for match in TARGET_C_LEGACY_THROUGH_RE.finditer(summary):
        if int(match.group(1)) != expected_max:
            errors.append(
                "stale Target C canonical-section claim in README.md: "
                f"Section {match.group(1)}; manifest gives Section {expected_max}"
            )

    state_version = state.get("state_version")
    if isinstance(state_version, str) and state_version:
        prompt_state = re.search(
            r"^\*\*State:\*\*\s*`([^`]+)`", texts[TARGET_C_PROMPT], re.M
        )
        if prompt_state and prompt_state.group(1) != state_version:
            errors.append(
                f"{TARGET_C_PROMPT} gives state {prompt_state.group(1)}, "
                f"but the manifest gives {state_version}"
            )

    for relative in (TARGET_C_CURRENT, TARGET_C_README, TARGET_C_PROMPT):
        for pattern in OBSOLETE_ENDPOINT_PATTERNS:
            if pattern.search(texts[relative]):
                errors.append(
                    f"{relative} still directs research to the obsolete Section-96 endpoint"
                )
                break

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = run_checks(args.root.resolve())
    if errors:
        for error in errors:
            print(f"active-route-summary: {error}", file=sys.stderr)
        print(f"active-route-summary: FAILED ({len(errors)} errors)", file=sys.stderr)
        return 1
    print("active-route-summary: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
