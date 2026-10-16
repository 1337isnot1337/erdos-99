#!/usr/bin/env python3
"""List public task reading, claim prerequisites, and scoped runnable evidence.

This is navigation, never a proof-completeness or theorem-promotion checker.
It does not execute discovered commands.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

import yaml

try:
    from .run_theorem_certificates import entry_records
except ImportError:
    from run_theorem_certificates import entry_records

ROOT = Path(__file__).resolve().parents[1]


def has_main_guard(path: Path) -> bool:
    """Separate standalone supporting checks from import-only helpers."""
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.If) and isinstance(node.test, ast.Compare):
            test = node.test
            if (isinstance(test.left, ast.Name) and test.left.id == "__name__"
                    and len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq)
                    and len(test.comparators) == 1
                    and isinstance(test.comparators[0], ast.Constant)
                    and test.comparators[0].value == "__main__"):
                return True
    return False


def context(task_id: str, root: Path = ROOT) -> dict:
    root = root.resolve()

    def read_json(path):
        return json.loads((root / path).read_text(encoding="utf-8"))

    def public_file(path):
        if not isinstance(path, str) or Path(path).is_absolute() or ".." in Path(path).parts:
            raise ValueError(f"outside public repository: {path!r}")
        candidate = root / path
        if not candidate.is_file() or not candidate.resolve().is_relative_to(root):
            raise ValueError(f"missing or outside public repository: {path}")
        return path

    catalogue = read_json("docs/research/agent-task-catalog.json")
    task = next((t for t in catalogue["tasks"] if t["id"] == task_id), None)
    if task is None:
        raise ValueError(f"unknown task: {task_id}")
    inclusion = read_json("docs/publication/inclusion.json")
    graph = {r["public_path"]: set(r.get("dependencies", [])) for r in inclusion["entries"]}
    supplement_path = root / "docs/research/onboarding-prerequisites.json"
    supplement = read_json(supplement_path.relative_to(root)) if supplement_path.is_file() else {}
    for path, dependencies in supplement.get("file_dependencies", {}).items():
        graph.setdefault(path, set()).update(dependencies)
    extra = supplement.get("tasks", {}).get(task_id, {})
    premise_fields = ("canonical_dependencies", "previous_obstructions", "audited_working_premises")
    seeds = [r["path"] for k in premise_fields
             for r in task.get(k, [])]
    reading_order = extra.get("reading_order", [])
    seeds += [r["path"] for r in reading_order]
    seeds += extra.get("supporting_obstructions", [])

    state = yaml.safe_load((root / "docs/state/theorem-state.yaml").read_text(encoding="utf-8"))
    claims = {e["id"]: (target, bucket, e) for target, bucket, e in entry_records(state)}
    selected_claims = {r["claim_id"] for k in premise_fields
                       for r in task.get(k, []) if r.get("claim_id")}
    seen, pending = set(), set(seeds)
    expanded_claims = set()
    while pending or selected_claims - expanded_claims:
        while pending:
            path = public_file(pending.pop())
            if path in seen:
                continue
            seen.add(path)
            pending.update(graph.get(path, set()) - seen)
            for ident, (_, _, entry) in claims.items():
                if path in (entry.get("report"), entry.get("audit")):
                    selected_claims.add(ident)
        for ident in sorted(selected_claims - expanded_claims):
            if ident not in claims:
                raise ValueError(f"unknown prerequisite claim: {ident}")
            _, _, entry = claims[ident]
            expanded_claims.add(ident)
            selected_claims.update(entry.get("depends_on", []))
            pending.update(p for p in (entry.get("report"), entry.get("audit")) if p and p not in seen)
            pending.update(p for p in entry.get("certificates", []) if p not in seen)

    registry = read_json("research/certificates.json")["certificates"]
    registered = {r["path"]: r for r in registry}
    evidence = []
    for path, record in sorted(registered.items()):
        if path in seen or set(record.get("proof_sources", [])) & seen:
            public_file(path)
            evidence.append({
                "path": path, "command": record["command"], "registration": "theorem registry",
                "claims": record.get("claims", []), "scope": record.get("scope", []),
                "does_not_establish": record.get("does_not_establish"),
            })
    # A reachable script may be supporting or unreviewed evidence. Never silently
    # register it or imply the source report's lifecycle applies to the script.
    helpers = []
    for path in sorted(seen):
        if path.startswith("research/") and path.endswith(".py") and path not in registered:
            if not has_main_guard(root / path):
                helpers.append(path)
                continue
            evidence.append({
                "path": path, "command": "python " + path,
                "registration": "supporting file; not in theorem registry",
                "scope": ["Inspect the script and linked proof; helpers may not be standalone checks."],
                "does_not_establish": "Registration, canonical promotion, global realization or global optimality.",
            })

    return {
        "task": task_id, "question": task["question"],
        "read_first": [r["path"] for r in task["canonical_dependencies"]],
        "reading_order_supplement": reading_order,
        "transitive_file_prerequisites": sorted(seen),
        "reachable_claims": [
            {"id": ident, "target": claims[ident][0], "bucket": claims[ident][1],
             "status": claims[ident][2].get("status"), "scope": claims[ident][2].get("scope")}
            for ident in sorted(expanded_claims)
        ],
        "certificate_commands": [r["command"] for r in evidence if r["registration"] == "theorem registry"],
        "supporting_evidence_commands": [r["command"] for r in evidence if r["registration"] != "theorem registry"],
        "supporting_helpers": helpers,
        "evidence": evidence,
        "note": "File and claim reachability is navigation, not proof completeness. Read full statements, proofs and inline section references. Registered certificates and supporting scripts have separate scopes; neither supplies unencoded global hypotheses. Commands are listed, never executed.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_id")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = context(args.task_id, args.root)
    except (OSError, ValueError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
