#!/usr/bin/env python3
"""Search cached GitHub text and tracked research notes without posting or running research."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess

try:
    from scripts.research_coordination import DEFAULT_CACHE, GROUPS, handoff_leads, local_records, query_open_work, search
    from scripts.workflow_common import ROOT, git
except ModuleNotFoundError:
    from research_coordination import DEFAULT_CACHE, GROUPS, handoff_leads, local_records, query_open_work, search
    from workflow_common import ROOT, git


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*")
    parser.add_argument("--task")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--include-closed", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    if args.refresh and args.offline:
        parser.error("--refresh and --offline are mutually exclusive")
    try:
        terms = list(args.terms)
        if args.task:
            catalog = json.loads((args.root / "docs/research/agent-task-catalog.json").read_text())
            task = next((row for row in catalog["tasks"] if row["id"] == args.task), None)
            if task is None:
                raise ValueError("unknown task")
            terms += [args.task, *task["overlap_terms"]]
        snapshot = query_open_work(cache=args.cache, refresh=args.refresh, offline=args.offline,
                                   include_closed=args.include_closed)
        remote = [row for group in GROUPS if group != "closed_pulls" or args.include_closed
                  for row in snapshot.get(group, [])]
        local = local_records(args.root)
        result = dict(repository=snapshot["repository"], source=snapshot["source"],
                      queried_at=snapshot["queried_at"], coverage=snapshot.get("coverage", {}),
                      local=dict(checkout_commit=git(args.root, "rev-parse", "HEAD"),
                                 records=len(local), scope="tracked working-tree research notes; archives and migration omitted"),
                      handoffs=handoff_leads(snapshot), terms=terms,
                      discussion_threads=[{key: row[key] for key in ("number", "title", "url")}
                                          for row in snapshot.get("discussions", []) if row.get("kind") == "discussion"],
                      warnings=snapshot.get("warnings", []),
                      matches=search(remote + local, terms),
                      limits="Keyword matches are leads. Cached/offline coverage can be stale; absence is not novelty. PR comments, closed Issues and remote changed-file inventories are not searched.")
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Remote: {result['source']} at {result['queried_at']}")
        print("Coverage: " + json.dumps(result["coverage"]))
        print("Handoffs: " + json.dumps(result["handoffs"]))
        print("Discussion threads (also inspect prose-only requests): " + json.dumps(result["discussion_threads"]))
        for warning in result["warnings"]:
            print("Warning: " + warning)
        for row in result["matches"]:
            print(f"{row['kind']}: {row['title']} — {row.get('url') or row.get('path')}")
            print("  " + row["excerpt"].replace("\n", " "))
        print(result["limits"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
