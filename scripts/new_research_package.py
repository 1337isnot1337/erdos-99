#!/usr/bin/env python3
"""Create an unreviewed, deliberately failing package using the existing isolated replay protocol."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

try:
    from scripts.workflow_common import ROOT, git, regular_file, repo_path
except ModuleNotFoundError:
    from workflow_common import ROOT, git, regular_file, repo_path


def create(root, name, task_id, author, sources):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("package name must be a lowercase hyphenated slug")
    catalog = json.loads((root / "docs/research/agent-task-catalog.json").read_text())
    if task_id not in {row["id"] for row in catalog["tasks"]}:
        raise ValueError("unknown task")
    if not author.strip() or not sources or len(sources) != len(set(sources)):
        raise ValueError("author and distinct source paths are required")
    baseline = git(root, "rev-parse", "HEAD")
    inputs = []
    for raw in sources:
        source = repo_path(raw)
        content = regular_file(root, source).read_bytes()
        pinned = subprocess.check_output(["git", "-C", str(root), "show", f"{baseline}:{source}"],
                                         stderr=subprocess.PIPE, timeout=60)
        if content != pinned:
            raise ValueError("source differs from HEAD; commit it before freezing its identity")
        inputs.append(dict(path=source, sha256=hashlib.sha256(content).hexdigest(),
                           identity=source, generated_from=[], commit=baseline))
    parent = root / "research-packages"
    if parent.is_symlink():
        raise ValueError("research-packages must not be a symlink")
    directory = parent / name
    parent.mkdir(exist_ok=True)
    directory.mkdir()  # Never overwrite an existing or frozen package.
    try:
        script = f"research-packages/{name}/verify.py"
        code = '"""Draft checker: replace with a scoped check and meaningful failure controls."""\nraise RuntimeError("Draft package: no evidence checker has been implemented")\n'
        inputs.append(dict(path=script, sha256=hashlib.sha256(code.encode()).hexdigest(),
                           identity="draft-checker", generated_from=[]))
        domain = "DRAFT: specify the exact finite domain or proof obligation"
        task = dict(version=1, id=name, classification="unreviewed",
                    scope=dict(statement="DRAFT: state the exact claim and hypotheses", domain=domain,
                               limitations="Draft only; establishes no mathematical result or canonical promotion"),
                    result="DRAFT: no checked result", remaining_questions=["Implement and independently check the scoped evidence"])
        provenance = dict(version=1, baseline_commit=baseline, inputs=inputs, packages=[],
                          unresolved=["Draft checker and source closure require review"])
        verify = dict(version=1, inputs=[row["path"] for row in inputs], domain=domain,
                      environment=dict(python="3.14", dependencies=[]),
                      commands=[dict(argv=["{python}", script], timeout_seconds=30)])
        for filename, data in [("TASK.json", task), ("SOURCES.json", provenance), ("VERIFY.json", verify)]:
            (directory / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        (directory / "verify.py").write_text(code, encoding="utf-8")
        (directory / "README.md").write_text(f"""# {name}

**Unreviewed draft. No mathematical result is established.**

Contributor: {author}. Task: `{task_id}`. Baseline: `{baseline}`.
Prepared with AI assistance; record originating and reviewing agent roles when known.
New contributions use Apache-2.0; retain predecessor attribution and source notices.

## Exact question and scope

Replace this section with the complete statement, definitions, hypotheses,
finite domain and candidate-to-endpoint implication. Name what is not proved.

## Evidence and falsification

Implement `verify.py`, add a positive case and meaningful failure controls,
and record exact inputs, arithmetic, commands, environment and actual output.
The generated checker deliberately fails. Update its SHA-256 in SOURCES.json.
Remove unresolved closure only after justifying every dependency.
Metadata check from the repository root:

```sh
python scripts/research_package.py --package research-packages/{name} --check-only
```

Commit the package before asking the localized planner to inspect Git blobs.
The isolated replay backend is optional; no new runner is introduced here.

## Open next questions

- Question: what exact implication remains after this result?
- Downstream use: which claim or decision can this extension change, and which exact quantity does it control?
- Changed hypothesis: what new source, domain or assumption makes this more than another instance of the completed experiment?
- Outcome: what would either a proof or a counterexample let the next worker do?
- First step: one feasible command or delicate proof reconstruction.
- Blocker: the precise missing hypothesis, source or execution obligation.

## Predecessors and handoff

Link the investigation thread, nearest work and exact source commits.
Record the priority/state revisions, checked scope and one next useful action.
Required repository-wide replay is deferred to the merging agent.
""", encoding="utf-8")
    except BaseException:
        shutil.rmtree(directory)
        raise
    return directory


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--task", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        print(create(args.root.resolve(), args.name, args.task, args.author, args.source))
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
