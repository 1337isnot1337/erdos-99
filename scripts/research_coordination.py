#!/usr/bin/env python3
"""Read-only GitHub overlap queries and reproducible issue/handoff text."""
from __future__ import annotations

import datetime as dt
import json
import re
import subprocess

REPOSITORY = "1337isnot1337/erdos-99"


def query_open_work(repository: str = REPOSITORY) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("invalid repository")
    records = {}
    for kind in ("pulls", "issues"):
        raw = subprocess.check_output(
            ["gh", "api", "--paginate", "--slurp",
             f"repos/{repository}/{kind}?state=open&per_page=100"],
            stderr=subprocess.PIPE, timeout=60, text=True,
        )
        pages = json.loads(raw)
        rows = []
        for page in pages:
            for item in page:
                if kind == "issues" and "pull_request" in item:
                    continue
                body = item.get("body") or ""
                # Retain coordination markers, never private issue bodies.
                markers = {}
                for key in ("TASK-ID", "SCOPE-ID", "CLAIM-EXPIRES"):
                    match = re.search(rf"(?m)^E99-{key}:\s*(\S+)", body)
                    if match:
                        markers[key] = match[1]
                claim_status = "not-a-marked-claim"
                if markers:
                    try:
                        expiry = dt.datetime.fromisoformat(markers["CLAIM-EXPIRES"].replace("Z", "+00:00"))
                        if expiry.tzinfo is None:
                            raise ValueError("timezone missing")
                        claim_status = "active" if expiry > dt.datetime.now(dt.timezone.utc) else "expired"
                    except (KeyError, ValueError):
                        claim_status = "expiry-unknown; check manually"
                rows.append({"claim_status": claim_status, "number": item["number"], "title": item["title"],
                             "url": item["html_url"], "updated_at": item["updated_at"],
                             "head_sha": item.get("head", {}).get("sha"),
                             "markers": markers})
        records[kind] = sorted(rows, key=lambda x: x["number"])
    owner, name = repository.split('/')
    info = json.loads(subprocess.check_output(['gh', 'api', f'repos/{repository}'], text=True, timeout=60))
    records['discussions'] = []
    availability = 'disabled'
    if info.get('has_discussions'):
        availability = 'enabled'
        cursor = None
        while True:
            query = '''query($owner:String!,$name:String!,$cursor:String){repository(owner:$owner,name:$name){discussions(first:100,after:$cursor,orderBy:{field:UPDATED_AT,direction:DESC}){nodes{number title url updatedAt}pageInfo{hasNextPage endCursor}}}}'''
            argv = ['gh','api','graphql','-f','query='+query,'-f','owner='+owner,'-f','name='+name]
            if cursor: argv += ['-f','cursor='+cursor]
            page = json.loads(subprocess.check_output(argv,text=True,timeout=60))['data']['repository']['discussions']
            records['discussions'].extend(dict(r,markers={}) for r in page['nodes'])
            if not page['pageInfo']['hasNextPage']: break
            cursor = page['pageInfo']['endCursor']
    return {"schema_version": 1, "repository": repository, "source": "live-read-only",
            "discussions_availability": availability,
            "queried_at": dt.datetime.now(dt.timezone.utc).isoformat(), **records}


def overlap_for_task(task: dict, snapshot: dict) -> dict:
    terms = [task["id"].lower(), task["scope_key"].lower(),
             *[s.lower() for s in task["overlap_terms"]]]
    potential_prs = set(task.get("potential_open_overlap_prs", []))
    matches = {}
    for kind in ("pulls", "issues", "discussions"):
        matches[kind] = [r for r in snapshot.get(kind, []) if any(
            term in (r["title"] + " " + " ".join(r.get("markers", {}).values())).lower()
            for term in terms) or (kind == "pulls" and r["number"] in potential_prs)]
    return {"source": snapshot.get("source", "offline"),
            "queried_at": snapshot.get("queried_at"), **matches,
            "limits": "Catalogue PR pointers and title/marker matches are leads; manually compare objects, hypotheses, files and drafts."}


def claim_text(result: dict, task: dict, now: dt.datetime | None = None) -> str:
    now = now or dt.datetime.now(dt.timezone.utc)
    expiry = (now + dt.timedelta(days=7)).isoformat()
    return f"""CLAIM — {task['id']}
E99-TASK-ID: {task['id']}
E99-SCOPE-ID: {task['scope_key']}
E99-CLAIM-EXPIRES: {expiry}
Base commit: {result['checkout_commit']}
State version: {result['checkout_state_version']}
Exact question: {task['question']}
Method: {task['selected_method']}
Dependencies: {', '.join(r['path'] for r in task['canonical_dependencies'])}
Stopping condition: {task['stopping_condition']}
Owner / branch: <claimant and branch>
Overlap comparison: <links and exact scope differences; check live PRs and issues>
Status: exploratory; suggestion only until posted as a claim issue

HANDOFF
Claim classification: unreviewed candidate (change only with evidence)
Exact new statement / hypotheses: <complete statement>
Proof or certificate and reproduction command: <paths, inputs, arithmetic, command>
Binding regressions checked: <results and limits>
Remaining obligation / next step: <one exact step>
Attribution / AI assistance: <contributors and roles>
Independent review requested at commit: <exact head SHA and scope>
"""
