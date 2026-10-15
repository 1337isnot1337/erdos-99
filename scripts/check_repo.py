#!/usr/bin/env python3
"""Fast standard-library checks for task metadata and local Markdown links."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_EVIDENCE = {
    "unreviewed-proposal",
    "conditional-claim",
    "reproduced-finite-evidence",
    "independently-agent-audited",
    "human-reviewed",
    "rejected",
    "superseded",
    "canonical-accepted-theorem",
}
REQUIRED_TASK_HEADINGS = (
    "Mathematical question",
    "Definitions and hypotheses",
    "Why it matters",
    "Public prerequisites",
    "Starting point",
    "First step",
    "Evidence expected",
    "Falsification strategy",
    "Reproduction",
    "Stopping condition",
    "Scope limit",
    "Next questions",
    "Attribution and AI disclosure",
)
LOCAL_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def heading_slug(title: str) -> str:
    title = re.sub(r"[`*_]", "", title).lower()
    title = re.sub(r"[^\w -]", "", title, flags=re.UNICODE)
    return re.sub(r"\s+", "-", title.strip())


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def check_task_index(errors: list[str]) -> None:
    index_path = ROOT / "tasks/index.json"
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"tasks/index.json: cannot read valid JSON ({exc})")
        return
    if data.get("schema_version") != 1 or not isinstance(data.get("tasks"), list):
        errors.append("tasks/index.json: expected schema_version 1 and a tasks array")
        return

    seen: set[str] = set()
    for task in data["tasks"]:
        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id:
            errors.append("tasks/index.json: each task needs a nonempty id")
            continue
        if task_id in seen:
            errors.append(f"tasks/index.json: duplicate id {task_id}")
        seen.add(task_id)
        if task.get("availability") != "open":
            errors.append(f"{task_id}: initial task availability must be open")
        if task.get("evidence_status") not in ALLOWED_EVIDENCE:
            errors.append(f"{task_id}: unknown evidence_status")
        task_path = ROOT / str(task.get("path", ""))
        if not task_path.is_file() or ROOT not in task_path.resolve().parents:
            errors.append(f"{task_id}: missing or out-of-repository task file")
            continue
        body = task_path.read_text(encoding="utf-8")
        if task_id not in body:
            errors.append(f"{task_id}: id is absent from its task file")
        for heading in REQUIRED_TASK_HEADINGS:
            if f"## {heading}" not in body:
                errors.append(f"{task_id}: missing section '{heading}'")


def check_local_links(errors: list[str]) -> None:
    for markdown in markdown_files():
        body = markdown.read_text(encoding="utf-8")
        headings = {heading_slug(match) for match in HEADING.findall(body)}
        for raw in LOCAL_LINK.findall(body):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            path_text = unquote(parsed.path)
            if not path_text:
                if parsed.fragment and heading_slug(unquote(parsed.fragment)) not in headings:
                    errors.append(f"{markdown.relative_to(ROOT)}: missing anchor #{parsed.fragment}")
                continue
            linked = (markdown.parent / path_text).resolve()
            if ROOT not in linked.parents and linked != ROOT:
                errors.append(f"{markdown.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not linked.exists():
                errors.append(f"{markdown.relative_to(ROOT)}: broken local link: {target}")
                continue
            if parsed.fragment and linked.suffix.lower() == ".md":
                linked_body = linked.read_text(encoding="utf-8")
                linked_headings = {heading_slug(match) for match in HEADING.findall(linked_body)}
                if heading_slug(unquote(parsed.fragment)) not in linked_headings:
                    errors.append(f"{markdown.relative_to(ROOT)}: missing anchor in {target}")


def validate() -> list[str]:
    errors: list[str] = []
    check_task_index(errors)
    check_local_links(errors)
    for required in ("LICENSE", "NOTICE", "CONTRIBUTING.md", "CITATION.cff"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required project file: {required}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("repository checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("repository checks: OK (task metadata, required sections, Apache files, local links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
