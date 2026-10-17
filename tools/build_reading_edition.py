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
REPAIR_REGISTRY = "docs/publication/reading-tex-repairs.json"
WORDING = {
    "autoresearch.md": [
        ("Contribute one useful, independently reviewable result to this repository.",
         "Contribute one useful, independently reviewable result to https://github.com/1337isnot1337/erdos-99."),
    ],
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


def fenced_mask(text: str) -> str:
    """Mask code inside quotes/lists as well as top-level fenced blocks."""
    result = []
    fence = None
    for line in text.splitlines(keepends=True):
        plain = re.sub(r"^(?:[ \t]*>[ \t]?)+", "", line)
        match = re.match(r"^[ \t]*(`{3,}|~{3,})(.*?)(?:\n)?$", plain)
        if fence is None and match and not (match[1][0] == "`" and "`" in match[2]):
            fence = (match[1][0], len(match[1]))
            result.append(re.sub(r"[^\r\n]", " ", line))
        elif fence is not None:
            result.append(re.sub(r"[^\r\n]", " ", line))
            if re.fullmatch(rf"[ \t]*{re.escape(fence[0])}{{{fence[1]},}}[ \t]*(?:\n)?", plain):
                fence = None
        else:
            result.append(line)
    return "".join(result)


def visible_text(text: str) -> str:
    """Mask code and comments while retaining character offsets."""
    text = fenced_mask(text)
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


def math_delimiters(text: str, diagnostics: dict | None = None,
                    literal_displays: tuple[str, ...] = ()) -> tuple[str, int]:
    """Protect TeX from Markdown unescaping; preserve formula content."""
    visible = visible_text(text)
    tokens = list(re.finditer(r"(?<!\\)\\[\[\]]|(?<![\\$])\$\$(?!\$)", visible))
    edits = []
    pairs = repairs = literal_count = 0
    i = 0
    while i < len(tokens):
        opening = tokens[i]
        if opening[0] == r"\]":
            # An orphaned delimiter is presentation damage, not formula text.
            edits.append((opening.start(), opening.end(), ""))
            repairs += 1
            i += 1
            continue
        close_token = r"\]" if opening[0] == r"\[" else "$$"
        j = i + 1
        while j < len(tokens) and tokens[j][0] not in (close_token, r"\["):
            j += 1
        if j < len(tokens) and tokens[j][0] == close_token:
            end, consumed = tokens[j].start(), tokens[j].end()
            next_i = j + 1
        else:
            # Several retained reports omit a closing delimiter. Bound the
            # reading repair at the first paragraph break, never the next
            # formula. The page header discloses this source formatting repair.
            limit = tokens[j].start() if j < len(tokens) else len(text)
            boundary = re.search(r"\n[ \t]*\n", visible[opening.end():limit])
            end = opening.end() + boundary.start() if boundary else limit
            consumed = end
            next_i = i + 1
            repairs += 1
        body = text[opening.end():end]
        line_start = text.rfind("\n", 0, opening.start()) + 1
        prefix = text[line_start:opening.start()]
        container = re.fullmatch(r"(?P<quote>(?:[ \t]*>[ \t]?)*)(?P<indent>[ \t]*)", prefix)
        block_prefix = prefix if container else ""
        before = "" if container else "\n\n"
        quote_depth = prefix.count(">") if container else 0
        indent = container["indent"] if container else ""
        payload = []
        for line in body.split("\n"):
            for _ in range(quote_depth):
                line = re.sub(r"^[ \t]*>[ \t]?", "", line, count=1)
            if indent and line.startswith(indent):
                line = line[len(indent):]
            payload.append(line)
        body = "\n".join(payload).strip("\n")
        language = "math"
        if body.strip() in literal_displays:
            language = "text"
            literal_count += 1
        suffix_end = text.find("\n", consumed)
        suffix_end = len(text) if suffix_end < 0 else suffix_end
        after = "" if not text[consumed:suffix_end].strip() else "\n\n" + block_prefix
        if container and indent:
            # GitHub's math filter needs a loose list item around fenced math.
            before = "\n" + block_prefix
            after = after or "\n"
        fenced = (before + "```" + language + "\n"
                  + "\n".join(block_prefix + line for line in body.split("\n"))
                  + "\n" + block_prefix + "```" + after)
        edits.append((opening.start(), consumed, fenced))
        pairs += 1
        i = next_i
        while i < len(tokens) and tokens[i].start() < consumed:
            i += 1
    for a, b, replacement in reversed(edits):
        text = text[:a] + replacement + text[b:]

    visible = visible_text(text)
    edits = []
    for match in re.finditer(r"(?<!\\)\\\((.*?)\\\)", visible, re.S):
        body = text[match.start() + 2:match.end() - 2]
        if "\n\n" not in body and "`" not in body:
            edits.append((match.start(), match.end(), "$`" + body + "`$"))
    for a, b, replacement in reversed(edits):
        text = text[:a] + replacement + text[b:]
    pairs += len(edits)

    # Do not invent mathematical boundaries where an inherited inline marker
    # is malformed. Preserve that paragraph as an explicit source excerpt.
    visible = visible_text(text)
    fence_ranges = []
    fence_start = fence_length = 0
    fence_char = None
    offset = 0
    for line in text.splitlines(keepends=True):
        if fence_char is None:
            match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*?)(?:\r?\n)?$", line)
            if match and not (match[1][0] == "`" and "`" in match[2]):
                fence_start, fence_length, fence_char = offset, len(match[1]), match[1][0]
        elif re.fullmatch(rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*(?:\r?\n)?", line):
            fence_ranges.append((fence_start, offset + len(line)))
            fence_char = None
        offset += len(line)
    excerpts = set()
    for match in re.finditer(r"(?<!\\)\\[()]", visible):
        previous = list(re.finditer(r"\n[ \t]*\n|(?m:^#{1,6}[^\n]*\n)", text[:match.start()]))
        start = previous[-1].end() if previous else 0
        start = max([start] + [b for _, b in fence_ranges if b <= match.start()])
        following = re.search(r"\n[ \t]*\n|(?m:^#{1,6}[ \t])", text[match.end():])
        end = match.end() + following.start() if following else len(text)
        end = min([end] + [a for a, _ in fence_ranges if a >= match.end()])
        excerpts.add((start, end))
    for a, b in sorted(excerpts, reverse=True):
        body = text[a:b]
        longest = max((len(m[0]) for m in re.finditer(r"`+", body)), default=0)
        fence = "`" * max(3, longest + 1)
        replacement = ("\n\n**Source formatting excerpt (unbalanced inline math in the original):**\n\n"
                       + fence + "text\n" + body
                       + ("" if body.endswith("\n") else "\n") + fence + "\n\n")
        text = text[:a] + replacement + text[b:]

    # Existing dollar math needs the same protection: bare \{ is otherwise
    # consumed by CommonMark before GitHub's MathJax renderer sees it.
    visible = visible_text(text)
    edits = []
    for match in re.finditer(r"(?<![\\$])\$(?!\$)([^$]+?)(?<!\\)\$(?!\$)", visible):
        body = text[match.start() + 1:match.end() - 1]
        if body and not body[0].isspace() and not body[-1].isspace() and "`" not in body and "\n\n" not in body:
            edits.append((match.start(), match.end(), "$`" + body + "`$"))
    for a, b, replacement in reversed(edits):
        text = text[:a] + replacement + text[b:]
    pairs += len(edits)
    if diagnostics is not None:
        diagnostics["repaired_source_delimiters"] = repairs
        diagnostics["source_excerpts"] = len(excerpts)
        diagnostics["literal_math_excerpts"] = literal_count
    return text, pairs


def repair_source(source: str, raw: str, digest: str, registry: dict) -> tuple[str, int, tuple[str, ...]]:
    """Apply only reviewed, exact-source-bound presentation repairs."""
    record = registry.get(source)
    if record is None:
        return raw, 0, ()
    if record["source_sha256"] != digest:
        raise ValueError("stale reading repair source: " + source)
    count = 0
    for replacement in record.get("replacements", []):
        old, new, expected = replacement["old"], replacement["new"], replacement["count"]
        if raw.count(old) != expected:
            raise ValueError("stale reading replacement: " + source + ": " + repr(old))
        raw = raw.replace(old, new)
        count += expected
    excerpts = tuple(record.get("literal_displays", []))
    for excerpt in excerpts:
        if raw.count(excerpt) != 1:
            raise ValueError("stale literal math excerpt: " + source)
    return raw, count, excerpts


def table_math(text: str) -> str:
    """Escape GFM cell separators inside math, retaining the rendered TeX pipe."""
    result = []
    visible = fenced_mask(text)
    offset = 0
    for line in text.splitlines(keepends=True):
        check = visible[offset:offset + len(line)]
        offset += len(line)
        if check.lstrip().startswith("|"):
            line = re.sub(r"\$`([^`]*?)`\$", lambda m: "$`" + re.sub(r"(?<!\\)\|", r"\\|", m[1]) + "`$", line)
        result.append(line)
    return "".join(result)


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


def render(source: str, raw: str, available: set[str], root: Path,
           source_sha256: str | None = None, repair_registry: dict | None = None) -> tuple[str, int]:
    digest = source_sha256 or hashlib.sha256(raw.encode()).hexdigest()
    text, repair_count, literal_displays = repair_source(source, raw, digest, repair_registry or {})
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for old, new in WORDING.get(source, []):
        text = text.replace(old, new)
    if source == "docs/problem/literature_baseline.md":
        text = re.sub(r"\[([1-7])((?:, [^\]\n]+)?)\]",
                      lambda m: f"[{m[1]}{m[2]}](../BIBLIOGRAPHY.md#ref-{m[1]})", text)
    diagnostics = {}
    text, pairs = math_delimiters(text, diagnostics, literal_displays)
    text = table_math(text)
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
    state_link = quote(relative_link(destination, reading_path("docs/STATE.md")), safe="/-._~")
    header = (f"> Generated reading edition · [exact source]({quote(relative_link(destination, source), safe='/-._~')}) "
              f"· source SHA-256 `{digest}`.\n"
              f"> [Current theorem state]({state_link}) controls lifecycle and scope; historical claims retain their recorded status.\n\n")
    if repair_count:
        repair_link = quote(relative_link(destination, REPAIR_REGISTRY), safe="/-._~")
        header += (f"> Presentation repairs: {repair_count} exact-source-bound TeX/escape correction(s); "
                   f"[reviewed repair ledger]({repair_link}). Frozen source bytes are unchanged.\n\n")
    if diagnostics["literal_math_excerpts"]:
        header += (f"> Source excerpt note: {diagnostics['literal_math_excerpts']} deliberately truncated "
                   "formula quotation(s) are displayed as literal text, with no reconstructed equation.\n\n")
    if diagnostics["repaired_source_delimiters"]:
        header += (f"> Source formatting note: {diagnostics['repaired_source_delimiters']} unbalanced display "
                   "delimiter(s) repaired at paragraph boundaries; consult the exact source.\n\n")
    if diagnostics["source_excerpts"]:
        header += (f"> Source formatting note: {diagnostics['source_excerpts']} paragraph(s) with malformed "
                   "inline math are preserved as explicit source excerpts rather than guessed equations.\n\n")
    return header + text.rstrip() + "\n", pairs


def expected_files(root: Path) -> dict[str, str]:
    available = set(sources(root))
    registry_path = root / REPAIR_REGISTRY
    registry = json.loads(registry_path.read_text())["documents"] if registry_path.exists() else {}
    if set(registry) - available:
        raise ValueError("reading repair refers to a missing/excluded source")
    outputs = {}
    records = []
    total = 0
    for source in sorted(available):
        original = (root / source).read_bytes()
        digest = hashlib.sha256(original).hexdigest()
        raw = original.decode("utf-8")
        text, pairs = render(source, raw, available, root, source_sha256=digest, repair_registry=registry)
        destination = reading_path(source)
        outputs[destination] = text
        total += pairs
        records.append({"source": source, "source_sha256": digest,
                        "reading_path": destination, "reading_sha256": hashlib.sha256(text.encode()).hexdigest(),
                        "math_pairs_normalized": pairs})
    outputs[EDITION + "/README.md"] = """# GitHub reading edition

This edition provides GitHub-compatible mathematical formatting and usable public
navigation. The exact source documents remain unchanged, including frozen proofs
and historical archives. Every page links to its source and records its SHA-256.
The [generation manifest](manifest.json) binds all reading pages to those sources.
No statement, hypothesis, proof, or mathematical lifecycle is promoted here.

Unclosed source display delimiters are repaired only at paragraph boundaries and
flagged on their pages. Paragraphs with ambiguous inline delimiters are shown as
explicit source excerpts. These presentation notes preserve the underlying text
and make source formatting damage visible rather than inventing an equation.
Exact-source-bound TeX escape and punctuation corrections are disclosed on each
affected page and in the [presentation repair ledger](../docs/publication/reading-tex-repairs.json).
Deliberately truncated formula quotations remain literal text. Quoted and listed
equations retain their Markdown containers; the mathematical payload does not
include Markdown quote or table separators.

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
        if target.is_symlink() or not target.is_file() or target.read_bytes() != text.encode("utf-8"):
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
        target.write_bytes(text.encode("utf-8"))
    manifest = json.loads(outputs[EDITION + "/manifest.json"])
    print(json.dumps({k: v for k, v in manifest.items() if k != "documents"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
