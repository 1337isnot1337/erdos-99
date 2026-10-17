#!/usr/bin/env python3
"""Generate GitHub-readable Markdown without rewriting frozen source documents.

Only presentation delimiters, navigation, and listed wording corrections change.
Every output records its exact source hash. No claim or lifecycle is promoted.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import quote, unquote, urlsplit, urlunsplit

from public_links import markdown_destinations, strip_fenced_code

ROOT = Path(__file__).resolve().parents[1]
EDITION = "reading"
EXCLUDED = ("docs/archive/", "docs/research/migration/")
ROOT_DOCUMENTS = {"AGENTS.md", "CONTRIBUTING.md", "autoresearch.md"}
WORDING = {
    "docs/problem/statement.md": [
        ("minimum pairwise distance (1)", "minimum pairwise distance exactly $1$"),
    ],
    "docs/problem/README.md": [
        ("additional primary literature collected in `papers/related/`.",
         "additional primary literature linked in the [public bibliography](../BIBLIOGRAPHY.md)."),
    ],
    "docs/literature_review.md": [
        ("the public bibliography", "the [public bibliography](BIBLIOGRAPHY.md)"),
    ],
    "docs/problem/literature_baseline.md": [
        ("circumradius (1)", "circumradius $1$"),
        ("minimum distance to (1)", "minimum distance to $1$"),
    ],
}


def visible_text(text: str) -> str:
    """Mask code and comments while retaining character offsets."""
    text = strip_fenced_code(text)
    mask = lambda value: re.sub(r"[^\r\n]", " ", value)
    text = re.sub(r"(?s)<!--.*?-->", lambda m: mask(m[0]), text)
    runs = list(re.finditer(r"(?<!`)`+(?!`)", text))
    edits = []
    i = 0
    while i < len(runs):
        opening = runs[i]
        closing = next((j for j in range(i + 1, len(runs))
                        if len(runs[j][0]) == len(opening[0])), None)
        if closing is not None and not re.search(r"\n[ \t]*\n", text[opening.end():runs[closing].start()]):
            edits.append((opening.start(), runs[closing].end()))
            i = closing + 1
        else:
            i += 1
    for a, b in reversed(edits):
        text = text[:a] + mask(text[a:b]) + text[b:]
    return text


def math_delimiters(text: str) -> tuple[str, int]:
    """Replace paired legacy delimiters, leaving every formula byte intact."""
    visible = visible_text(text)
    opening = None
    edits = []
    pairs = 0
    for match in re.finditer(r"(?<!\\)\\([\[\]()])", visible):
        token = match[1]
        if opening is None:
            if token in "[(":
                opening = match
            continue
        if (opening[1], token) not in {("[", "]"), ("(", ")")}:
            continue
        if opening[1] == "(":
            left = right = "$"
        else:
            a = text.rfind("\n", 0, opening.start()) + 1
            b = text.find("\n", opening.end())
            b = len(text) if b < 0 else b
            c = text.rfind("\n", 0, match.start()) + 1
            d = text.find("\n", match.end())
            d = len(text) if d < 0 else d
            left = "$$" if not text[a:opening.start()].strip() and not text[opening.end():b].strip() else "\n\n$$\n"
            right = "$$" if not text[c:match.start()].strip() and not text[match.end():d].strip() else "\n$$\n\n"
        edits.extend([(opening.start(), opening.end(), left),
                      (match.start(), match.end(), right)])
        opening = None
        pairs += 1
    for a, b, replacement in reversed(edits):
        text = text[:a] + replacement + text[b:]
    return text, pairs


def sources(root: Path) -> list[str]:
    result = []
    for directory in ("docs", "tasks", "research"):
        for path in (root / directory).rglob("*.md"):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                raise ValueError("symlinked source document: " + rel)
            if not rel.startswith(EXCLUDED):
                result.append(rel)
    result.extend(path for path in ROOT_DOCUMENTS if (root / path).is_file())
    return sorted(set(result))


def reading_path(source: str) -> str:
    return EDITION + "/" + source


def relative_link(source: str, destination: str) -> str:
    return posixpath.relpath(destination, posixpath.dirname(source))


def render(source: str, raw: str, available: set[str], root: Path) -> tuple[str, int]:
    text = raw
    for old, new in WORDING.get(source, []):
        text = text.replace(old, new)
    if source == "docs/problem/literature_baseline.md":
        text = re.sub(r"\[([1-7])((?:, [^\]\n]+)?)\]",
                      lambda m: f"[{m[1]}{m[2]}](../BIBLIOGRAPHY.md#ref-{m[1]})", text)
    text, pairs = math_delimiters(text)
    destination = reading_path(source)
    edits = []
    for a, b, raw_target in markdown_destinations(text):
        target = html.unescape(raw_target.strip("<>"))
        target = re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", target)
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        path = posixpath.normpath(path.lstrip("/") if path.startswith("/") else
                                  posixpath.join(posixpath.dirname(source), path))
        if path == ".." or path.startswith("../"):
            raise ValueError("source link escapes repository: " + source)
        if path in available:
            path = reading_path(path)
        elif not (root / path).exists():
            if path.startswith(("papers/", "extracted/")):
                path = reading_path("docs/BIBLIOGRAPHY.md")
                url = url._replace(fragment="")
            else:
                raise ValueError(f"missing reading prerequisite: {source}: {path}")
        rewritten = quote(relative_link(destination, path), safe="/-._~")
        edits.append((a, b, urlunsplit(("", "", rewritten, url.query, url.fragment))))
    for a, b, replacement in reversed(edits):
        text = text[:a] + replacement + text[b:]
    digest = hashlib.sha256(raw.encode()).hexdigest()
    header = (f"> Generated reading edition · [exact source]({quote(relative_link(destination, source), safe='/-._~')}) "
              f"· source SHA-256 `{digest}`.\n"
              "> Formatting and navigation only; the source and theorem ledger control mathematical status.\n\n")
    return header + text, pairs


def expected_files(root: Path) -> dict[str, str]:
    available = set(sources(root))
    outputs = {}
    records = []
    total = 0
    for source in sorted(available):
        raw = (root / source).read_text()
        text, pairs = render(source, raw, available, root)
        destination = reading_path(source)
        outputs[destination] = text
        total += pairs
        records.append({"source": source, "source_sha256": hashlib.sha256(raw.encode()).hexdigest(),
                        "reading_path": destination, "reading_sha256": hashlib.sha256(text.encode()).hexdigest(),
                        "math_pairs_normalized": pairs})
    outputs[EDITION + "/README.md"] = """# GitHub reading edition

This edition provides GitHub-compatible mathematical formatting and usable public
navigation. The exact source documents remain unchanged, including frozen proofs
and historical archives. Every page links to its source and records its SHA-256.
The [generation manifest](manifest.json) binds all reading pages to those sources.
No statement, hypothesis, proof, or mathematical lifecycle is promoted here.

Start with the [problem](docs/problem/statement.md), [current state](docs/STATE.md),
[research map](docs/KNOWLEDGE_MAP.md), [glossary](docs/GLOSSARY.md), and
[numbered bibliography](docs/BIBLIOGRAPHY.md). Then choose [A](docs/targets/target-a/README.md),
[B](docs/targets/target-b/README.md), [C-II](docs/targets/target-c/CURRENT.md), or
a [current task](tasks/README.md). The [original repository overview](../README.md)
and [exact source documentation](../docs/README.md) remain available.

Regenerate with `python tools/build_reading_edition.py` from the repository root;
`python tools/build_reading_edition.py --check` verifies the entire edition.
"""
    outputs[EDITION + "/manifest.json"] = json.dumps({
        "schema": "erdos-99-reading-edition/v1", "mathematical_proof": False,
        "source_documents": len(records), "math_pairs_normalized": total, "documents": records,
    }, indent=2, ensure_ascii=False) + "\n"
    return outputs


def check(root: Path) -> list[str]:
    expected = expected_files(root)
    actual = {p.relative_to(root).as_posix() for p in (root / EDITION).rglob("*") if p.is_file()}
    errors = ["unexpected reading file: " + p for p in sorted(actual - expected.keys())]
    for path, text in expected.items():
        target = root / path
        if target.is_symlink() or not target.is_file() or target.read_text() != text:
            errors.append("stale or missing reading page: " + path)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.check:
        errors = check(root)
        for error in errors:
            print(error)
        print(json.dumps({"reading_edition": "failed" if errors else "passed", "errors": len(errors)}))
        return bool(errors)
    outputs = expected_files(root)
    for path, text in outputs.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if any(p.is_symlink() for p in (target, *target.parents) if p.is_relative_to(root)):
            raise ValueError("refusing symlinked output: " + path)
        target.write_text(text)
    manifest = json.loads(outputs[EDITION + "/manifest.json"])
    print(json.dumps({k: v for k, v in manifest.items() if k != "documents"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
