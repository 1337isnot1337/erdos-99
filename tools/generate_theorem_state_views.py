#!/usr/bin/env python3
"""Generate human-readable theorem-state views and embedded status snapshots."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

import yaml

MANIFEST = "docs/state/theorem-state.yaml"
STATE_DOC = "docs/STATE.md"
TARGET_C_DOC = "docs/targets/target-c/CURRENT.md"
STATE_BEGIN = "<!-- BEGIN GENERATED: theorem-state-snapshot -->"
STATE_END = "<!-- END GENERATED: theorem-state-snapshot -->"
C_BEGIN = "<!-- BEGIN GENERATED: target-c-ledger -->"
C_END = "<!-- END GENERATED: target-c-ledger -->"
PUBLIC_PROOF_GRAPH = "docs/publication/proof-graph.json"
BUCKETS = ("current_canonical_entries", "audited_working", "regressions", "rejected_or_overridden")


def load(root: Path) -> dict[str, Any]:
    data = yaml.safe_load((root / MANIFEST).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest must be a mapping")
    return data


def entries(state: dict[str, Any]) -> Iterable[tuple[str, str, dict[str, Any]]]:
    for target_name, target in state.get("targets", {}).items():
        if not isinstance(target, dict):
            continue
        for bucket in BUCKETS:
            for entry in target.get(bucket, []) or []:
                if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                    yield target_name, bucket, entry


def status_summary(state: dict[str, Any]) -> str:
    lines = [
        "# Generated theorem-state summary",
        "",
        "This file is generated from `docs/state/theorem-state.yaml`. Do not edit it by hand.",
        "",
        f"- State version: `{state['state_version']}`",
        f"- State date: `{state['state_date']}`",
        f"- Level I: **{str(state['level_i_status']).upper()}**",
        "",
        "## Targets",
        "",
        "| Target | Status | Current gate / endpoint |",
        "| --- | --- | --- |",
    ]
    a = state["targets"]["target-a"]
    b = state["targets"]["target-b"]
    c = state["targets"]["target-c"]
    lines.extend([
        f"| Target A | {a['status']} | through Section {a['canonical_sections_through']}; {a['locked_branch_endpoint']} |",
        f"| Target B | {b['status']} | {b['global_endpoint']} |",
        f"| Target C | {c['status']} | C-I {c['c_i']}; C-II {c['c_ii']} |",
        "",
        "## Active prompts",
        "",
    ])
    for name, path in state["active_prompts"].items():
        lines.append(f"- `{name}` -> `{path}`")

    lines.extend(["", "## Ledger entries", "", "| ID | Target | Status | Depends on | Source |", "| --- | --- | --- | --- | --- |"])
    for target, _, entry in entries(state):
        deps = ", ".join(f"`{x}`" for x in entry.get("depends_on", []) or []) or "—"
        source = entry.get("report") or entry.get("report_family") or "—"
        lines.append(f"| `{entry['id']}` | {target} | {entry['status']} | {deps} | `{source}` |")
    lines.append("")
    return "\n".join(lines)


def theorem_graph(state: dict[str, Any]) -> str:
    all_entries = list(entries(state))
    lines = [
        "# Generated theorem dependency graph",
        "",
        f"State version: `{state['state_version']}`.",
        "",
        "This file is generated from `docs/state/theorem-state.yaml`. Edges are lifecycle dependencies, not a replacement for the proofs.",
        "",
        "```mermaid",
        "graph TD",
    ]
    for _, _, entry in all_entries:
        ident = entry["id"]
        label = f"{ident} [{entry['status']}]".replace('"', "'")
        lines.append(f'  {ident.replace("-", "_")}["{label}"]')
    for _, _, entry in all_entries:
        src = entry["id"].replace("-", "_")
        for dep in entry.get("depends_on", []) or []:
            lines.append(f"  {dep.replace('-', '_')} --> {src}")
        for target in entry.get("invalidates", []) or []:
            lines.append(f"  {src} -. invalidates .-> {target.replace('-', '_')}")
        for target in entry.get("supersedes", []) or []:
            lines.append(f"  {src} -. supersedes .-> {target.replace('-', '_')}")
    lines.extend(["```", "", "## Edge list", ""])
    for _, _, entry in all_entries:
        for kind in ("depends_on", "invalidates", "supersedes"):
            for target in entry.get(kind, []) or []:
                arrow = "depends on" if kind == "depends_on" else kind
                lines.append(f"- `{entry['id']}` {arrow} `{target}`")
    if lines[-1] == "## Edge list":
        lines.append("No explicit edges.")
    lines.append("")
    return "\n".join(lines)


def state_block(state: dict[str, Any]) -> str:
    a, b, c = (state["targets"][key] for key in ("target-a", "target-b", "target-c"))
    return "\n".join([
        STATE_BEGIN,
        f"**Generated state snapshot (`{state['state_version']}`):** Level I **{str(state['level_i_status']).upper()}**; "
        f"Target A **{str(a['status']).upper()}** through Section {a['canonical_sections_through']}; "
        f"Target B **{str(b['status']).upper()}**; Target C **C-I {str(c['c_i']).upper()} / C-II {str(c['c_ii']).upper()}**.",
        "",
        "Machine-derived tables: [`state/STATUS.generated.md`](state/STATUS.generated.md) and "
        "[`state/THEOREM_GRAPH.generated.md`](state/THEOREM_GRAPH.generated.md).",
        STATE_END,
    ])


def target_c_block(state: dict[str, Any]) -> str:
    c = state["targets"]["target-c"]
    canonical = [entry["id"] for entry in c.get("current_canonical_entries", []) or []]
    regressions = [entry["id"] for entry in c.get("regressions", []) or []]
    rejected = [entry["id"] for entry in c.get("rejected_or_overridden", []) or []]
    return "\n".join([
        C_BEGIN,
        f"**Generated ledger snapshot (`{state['state_version']}`):** C-I **{str(c['c_i']).upper()}**; C-II **{str(c['c_ii']).upper()}**.",
        "",
        "Canonical IDs: " + (", ".join(f"`{x}`" for x in canonical) or "none") + ".",
        "Regression IDs: " + (", ".join(f"`{x}`" for x in regressions) or "none") + ".",
        "Rejected/overridden IDs: " + (", ".join(f"`{x}`" for x in rejected) or "none") + ".",
        C_END,
    ])


def replace_or_insert(text: str, begin: str, end: str, block: str) -> str:
    if begin in text or end in text:
        if text.count(begin) != 1 or text.count(end) != 1 or text.index(begin) > text.index(end):
            raise ValueError(f"malformed generated block markers: {begin}")
        start = text.index(begin)
        finish = text.index(end, start) + len(end)
        return text[:start] + block + text[finish:]
    lines = text.splitlines(keepends=True)
    if not lines:
        return block + "\n"
    insert_at = 1
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1
    return "".join(lines[:insert_at]) + "\n" + block + "\n\n" + "".join(lines[insert_at:])


def publication_proof_graph(root: Path, state: dict[str, Any]) -> str:
    """Keep the public machine view aligned with claim lifecycle and file edges."""
    inclusion = json.loads((root / "docs/publication/inclusion.json").read_text(encoding="utf-8"))
    claims = []
    for target, _, claim in entries(state):
        claims.append({
            "id": claim["id"], "track": target, "status": claim["status"],
            "formal_statement_source": claim.get("report"),
            "statement": claim.get("conclusion", claim.get("reason", "Read exact source statement")),
            "assumptions": claim.get("scope", "Exact definitions and hypotheses in named proof module"),
            "immediate_theorem_prerequisites": claim.get("depends_on", []),
            "proof": claim.get("report"), "independent_audit": claim.get("audit"),
            "certificates": claim.get("certificates", []),
            "review_identity": "inherited internal audit unless explicitly recorded otherwise; no human review inferred",
            "limitations": claim.get("scope", claim.get("reason", "No scope beyond the exact proved statement")),
        })
    file_edges = sorted({(row["public_path"], dependency)
                         for row in inclusion["entries"]
                         for dependency in row.get("dependencies", [])})
    return json.dumps({"state_version": state["state_version"], "claims": claims,
                       "file_edges": file_edges}, indent=2) + "\n"


def expected_files(root: Path, state: dict[str, Any]) -> dict[str, str]:
    status_path = state["generated_views"]["status_summary"]
    graph_path = state["generated_views"]["theorem_graph"]
    state_text = (root / STATE_DOC).read_text(encoding="utf-8")
    c_text = (root / TARGET_C_DOC).read_text(encoding="utf-8")
    return {
        status_path: status_summary(state),
        graph_path: theorem_graph(state),
        PUBLIC_PROOF_GRAPH: publication_proof_graph(root, state),
        STATE_DOC: replace_or_insert(state_text, STATE_BEGIN, STATE_END, state_block(state)),
        TARGET_C_DOC: replace_or_insert(c_text, C_BEGIN, C_END, target_c_block(state)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        state = load(root)
        expected = expected_files(root, state)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as exc:
        print(f"generated-state: {exc}", file=sys.stderr)
        return 1

    if args.write:
        for rel, content in expected.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if not content.endswith("\n"):
                content += "\n"
            path.write_text(content, encoding="utf-8")
        print(f"generated-state: wrote {len(expected)} views/doc blocks")
        return 0

    errors = []
    for rel, content in expected.items():
        if not content.endswith("\n"):
            content += "\n"
        path = root / rel
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            errors.append(rel)
    if errors:
        print("generated-state: stale generated views: " + ", ".join(errors), file=sys.stderr)
        print("run: python3 tools/generate_theorem_state_views.py --write", file=sys.stderr)
        return 1
    print("generated-state: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
