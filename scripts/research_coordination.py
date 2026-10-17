"""Read-only, body-aware overlap snapshots and advisory handoff leads.

Workflow design informed by CrocSwap/integer-mult-bounds (Apache-2.0),
commit 463113d675af7410ac91d53a4fed51ec6494eb9a. Independently implemented here.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path
import re

try:
    from scripts.workflow_common import REPOSITORY, ROOT, atomic_json, git, gh, graphql, now, pages, regular_file, timestamp
except ModuleNotFoundError:
    from workflow_common import REPOSITORY, ROOT, atomic_json, git, gh, graphql, now, pages, regular_file, timestamp

DEFAULT_CACHE = Path.home() / ".cache/erdos99/overlap.json"
GROUPS = ("pulls", "issues", "discussions", "closed_pulls")
INVESTIGATION_STATES = {"open", "active", "awaiting-review", "completed", "exhausted", "superseded", "paused"}
ROLES = {"producer", "reviewer"}


def investigation_details(task, source_commit=None):
    """A card is a family; this object identifies its current bounded question."""
    declared = task.get("investigation", {})
    return dict(id=declared.get("id", task["id"]),
                source_commit=declared.get("source_commit", source_commit or ""),
                domain=declared.get("domain", " | ".join(task.get("assumptions", []))),
                question=declared.get("question", task.get("question", "")),
                status=declared.get("status", "open"))


def investigation_key(investigation):
    # Neither a random seed nor an unrelated checkout/method change creates work.
    identity = {key: " ".join(investigation.get(key, "").split())
                for key in ("id", "source_commit", "domain", "question")}
    payload = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:20]


def default_role(task):
    return "reviewer" if task.get("track") in ("independent-audit", "independent-verification") else "producer"


def markers(body):
    return {key: value.strip() for key, value in
            re.findall(r"(?m)^E99-([A-Z-]+):[^\S\r\n]*([^\r\n]+)", body)}


def claim_status(row):
    marked = row.get("markers", {})
    if not marked:
        return "not-a-marked-claim"
    if marked.get("STATUS", "").upper() in ("DONE", "COMPLETED", "CLOSED", "RELEASED", "SUPERSEDED", "EXHAUSTED"):
        return "ended"
    try:
        expiry = dt.datetime.fromisoformat(marked["CLAIM-EXPIRES"].replace("Z", "+00:00"))
        if expiry.tzinfo is None:
            raise ValueError("timezone missing")
        if expiry > now() + dt.timedelta(days=7):
            return "expiry-outside-seven-day-limit; check manually"
        return "active" if expiry > now() else "expired"
    except (KeyError, ValueError):
        return "expiry-unknown; check manually"


def _row(item, kind):
    body = item.get("body") or ""
    return dict(number=item["number"], title=item["title"], body=body,
                url=item.get("html_url", item.get("url")), kind=kind,
                updated_at=item.get("updated_at", item.get("updatedAt")),
                head_sha=item.get("head", {}).get("sha"), markers=markers(body),
                record_id=item.get("id"), thread_id=item.get("thread_id"),
                thread_url=item.get("thread_url"))


def _connection(node_id, node_type, field):
    cursor = None
    while True:
        query = """query($id:ID!,$cursor:String){node(id:$id){... on TYPE{
          FIELD(first:100,after:$cursor){nodes{id body url updatedAt}
          pageInfo{hasNextPage endCursor}}}}}""".replace("TYPE", node_type).replace("FIELD", field)
        node = graphql(query, id=node_id, cursor=cursor).get("node")
        if not isinstance(node, dict) or not isinstance(node.get(field), dict):
            raise ValueError("Discussion comment/reply access is unavailable; refresh was not completed")
        connection = node[field]
        yield from connection["nodes"]
        if not connection["pageInfo"]["hasNextPage"]:
            break
        cursor = connection["pageInfo"]["endCursor"]


def _discussions(repository):
    owner, name = repository.split("/")
    cursor, records = None, []
    while True:
        query = """query($owner:String!,$name:String!,$cursor:String){repository(owner:$owner,name:$name){
          discussions(first:100,after:$cursor){nodes{id number title body url updatedAt}
          pageInfo{hasNextPage endCursor}}}}"""
        repository_data = graphql(query, owner=owner, name=name, cursor=cursor).get("repository")
        if not isinstance(repository_data, dict) or not isinstance(repository_data.get("discussions"), dict):
            raise ValueError("Discussion access is unavailable; refresh was not completed")
        connection = repository_data["discussions"]
        for discussion in connection["nodes"]:
            records.append(_row({**discussion, "thread_id": discussion["id"],
                                 "thread_url": discussion["url"]}, "discussion"))
            for comment in _connection(discussion["id"], "Discussion", "comments"):
                thread = {"thread_id": comment["id"], "thread_url": comment["url"]}
                records.append(_row({**discussion, **comment, **thread}, "discussion-comment"))
                for reply in _connection(comment["id"], "DiscussionComment", "replies"):
                    records.append(_row({**discussion, **reply, **thread}, "discussion-reply"))
        if not connection["pageInfo"]["hasNextPage"]:
            return records
        cursor = connection["pageInfo"]["endCursor"]


def validate_snapshot(snapshot, repository=REPOSITORY):
    if (not isinstance(snapshot, dict) or snapshot.get("schema_version") not in (1, 2, 3)
            or snapshot.get("repository") != repository):
        raise ValueError("overlap snapshot belongs to another repository or schema")
    for group in GROUPS:
        if not isinstance(snapshot.get(group, []), list):
            raise ValueError("invalid overlap records")
        for row in snapshot.get(group, []):
            if (not isinstance(row, dict) or type(row.get("number")) is not int
                    or not isinstance(row.get("title"), str)
                    or not isinstance(row.get("body", ""), str)
                    or not isinstance(row.get("markers", {}), dict)
                    or any(not isinstance(value, str) for value in row.get("markers", {}).values())):
                raise ValueError("invalid overlap record fields")
    checked = snapshot.get("queried_at")
    if not isinstance(checked, str):
        raise ValueError("missing cache timestamp")
    return snapshot


def query_open_work(repository=REPOSITORY, *, cache=None, refresh=False,
                    offline=False, include_closed=False, max_age=300):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("invalid repository")
    cache = Path(cache).expanduser() if cache is not None else None
    saved = None
    if cache is not None and Path(cache).exists():
        saved = validate_snapshot(json.loads(Path(cache).read_text(encoding="utf-8")), repository)
    if saved is not None:
        checked = dt.datetime.fromisoformat(saved["queried_at"].replace("Z", "+00:00"))
        if checked.tzinfo is None or checked > now() + dt.timedelta(seconds=60):
            raise ValueError("invalid cache timestamp")
        age = (now() - checked).total_seconds()
        if offline or (not refresh and age <= max_age and
                       (not include_closed or "closed_pulls" in saved)):
            saved["source"] = "offline-saved-query" if offline else "cached-read-only"
            saved["warnings"] = []
            if include_closed and "closed_pulls" not in saved:
                saved["warnings"].append("Requested closed-PR coverage is unavailable in this offline snapshot.")
            if saved.get("schema_version") == 1:
                saved["warnings"].append("Legacy snapshot: body/comment coverage was not recorded.")
            if saved.get("schema_version") in (1, 2):
                saved["warnings"].append("Legacy snapshot: discussion reply roots may be unavailable; ambiguous status changes stay separate.")
            for group in GROUPS:
                for row in saved.get(group, []):
                    row["claim_status"] = claim_status(row)
            return saved
    if offline:
        return dict(schema_version=3, repository=repository, source="offline-no-remote-data",
                    queried_at=None, coverage={}, pulls=[], issues=[], discussions=[],
                    discussions_availability="unknown", warnings=["No remote snapshot is available; remote overlap is unknown."])
    records, coverage = {}, {}
    for group in ("pulls", "issues", "closed_pulls"):
        if group == "closed_pulls" and not include_closed:
            continue
        endpoint = "pulls" if group == "closed_pulls" else group
        state = "closed" if group == "closed_pulls" else "open"
        records[group] = [_row(item, group) for item in pages(
            f"repos/{repository}/{endpoint}?state={state}&per_page=100")
            if group != "issues" or "pull_request" not in item]
        coverage[group] = dict(fetched_at=timestamp(), complete_pagination=True,
                               records=len(records[group]), fields="titles and bodies")
    enabled = gh(f"repos/{repository}").get("has_discussions")
    if type(enabled) is not bool:
        raise ValueError("Discussion availability is unknown; refresh was not completed")
    records["discussions"] = _discussions(repository) if enabled else []
    coverage["discussions"] = dict(fetched_at=timestamp(), complete_pagination=True,
                                   available=enabled, records=len(records["discussions"]),
                                   fields="bodies, comments and replies")
    snapshot = dict(schema_version=3, repository=repository, source="live-read-only",
                    queried_at=timestamp(), coverage=coverage,
                    discussions_availability="enabled" if enabled else "disabled", **records)
    for group in GROUPS:
        for row in snapshot.get(group, []):
            row["claim_status"] = claim_status(row)
    if cache is not None:
        atomic_json(cache, snapshot)
    return snapshot


def local_records(root=ROOT):
    records = []
    for path in git(root, "ls-files", "-z").split("\0"):
        if (not path or path.startswith(("docs/archive/", "docs/research/migration/"))
                or not path.startswith(("docs/research/", "docs/reports/", "docs/audits/", "research/", "research-packages/", "tasks/"))
                or not (path.endswith(".md") or Path(path).name in ("TASK.json", "SOURCES.json"))):
            continue
        try:
            source = regular_file(root, path)
        except ValueError:
            continue
        body = source.read_text(encoding="utf-8")
        records.append(dict(kind="local-note", title=path, path=path, body=body,
                            markers=markers(body), url=None))
    return records


def search(records, terms):
    terms = [term.lower() for term in terms if term.strip()]
    matches = []
    for row in records:
        body = row.get("body", "")
        text = row.get("title", "") + " " + body + " " + " ".join(row.get("markers", {}).values())
        found = [term for term in terms if term in text.lower()]
        if found:
            positions = [body.lower().find(term) for term in found if term in body.lower()]
            start = max(0, min(positions, default=0) - 100)
            matches.append({k: v for k, v in row.items() if k != "body"} |
                           dict(matched_terms=found, excerpt=body[start:start + 500]))
    return matches


def _thread_key(group, row):
    if row.get("thread_id"):
        return group, "thread", row["thread_id"]
    if group != "discussions":
        return group, "number", row["number"]
    # Old snapshots did not retain reply roots. Never infer that all comments in
    # a hub concern one investigation. Explicit scope markers can still join them.
    return group, row.get("kind"), row.get("record_id") or row.get("url"), row["number"]


def _complete_identity(marked):
    if all(marked.get(key) for key in ("SOURCE-SHA", "DOMAIN", "QUESTION")):
        identity = marked.get("INVESTIGATION-ID") or marked.get("TASK-ID")
        if identity:
            return dict(id=identity, source_commit=marked["SOURCE-SHA"],
                        domain=marked["DOMAIN"], question=marked["QUESTION"])
    return None


def _marked_scope(marked, known_scopes=None):
    # The complete identity is authoritative. A copied scope digest must not
    # place changed-source/domain/question events in the old lifecycle.
    identity = _complete_identity(marked)
    if identity:
        return investigation_key(identity)
    scope = marked.get("SCOPE-ID")
    known = (known_scopes or {}).get(scope)
    if known and any(marked.get(marker)
                     and " ".join(marked[marker].split()) != " ".join(known[field].split())
                     for marker, field in (("INVESTIGATION-ID", "id"), ("SOURCE-SHA", "source_commit"),
                                           ("DOMAIN", "domain"), ("QUESTION", "question"))):
        return None
    return scope


def investigation_lifecycles(snapshot):
    """Latest status per exact scope/role, or per discussion comment root."""
    records, known_scopes = [], {}
    for group in GROUPS:
        rows = snapshot.get(group, [])
        roots = {_thread_key(group, row): row for row in rows
                 if row.get("kind") != "discussion-reply"}
        for row in rows:
            thread = _thread_key(group, row)
            root_markers = roots.get(thread, {}).get("markers", {})
            own = row.get("markers", {})
            # A separately named investigation in the same thread must not
            # inherit the old source identity or close the opening investigation.
            changed_identity = any(own.get(key) and root_markers.get(key)
                                   and " ".join(own[key].split()) != " ".join(root_markers[key].split())
                                   for key in ("INVESTIGATION-ID", "TASK-ID", "SCOPE-ID", "SOURCE-SHA", "DOMAIN", "QUESTION"))
            marked = {**({} if changed_identity else root_markers), **own}
            if changed_identity and marked.get("SCOPE-ID") == root_markers.get("SCOPE-ID"):
                # A partial identity change can also carry a copied old digest.
                # Without a full tuple it is an ambiguous new event, not a
                # terminal update to the original scope.
                marked.pop("SCOPE-ID", None)
            identity = _complete_identity(marked)
            if identity:
                known_scopes[investigation_key(identity)] = identity
            status = own.get("STATUS", "").upper()
            if not status and group == "pulls" and _marked_scope(marked):
                status = "SUBMITTED"
            if not status:
                continue
            role = marked.get("ROLE", "producer")
            records.append((group, thread, row, marked, status, role))
    # Resolve partial markers against every complete identity before grouping,
    # including identities in other threads or later in the snapshot ordering.
    latest = {}
    for group, thread, row, marked, status, role in records:
        scope = _marked_scope(marked, known_scopes)
        if scope:
            key = "scope", scope, role
        else:
            key = (*thread, marked.get("INVESTIGATION-ID"), marked.get("TASK-ID"),
                   marked.get("SOURCE-SHA"), marked.get("DOMAIN"), marked.get("QUESTION"), role)
        updated = row.get("updated_at") or ""
        if updated >= latest.get(key, {}).get("updated_at", ""):
            latest[key] = dict(surface=group, row=row, markers=marked,
                               updated_at=updated, status=status, role=role, scope_key=scope)
    return list(latest.values())


def handoff_leads(snapshot):
    """Advisory pointers only; read the current thread before accepting work."""
    leads = []
    for current in investigation_lifecycles(snapshot):
        if current["surface"] == "closed_pulls" or current["status"] != "HANDOFF":
            continue
        row, marked = current["row"], current["markers"]
        leads.append(dict(surface=current["surface"], number=row["number"], url=row["url"],
                          title=row["title"], task_id=marked.get("TASK-ID"),
                          investigation_id=marked.get("INVESTIGATION-ID"), scope_key=current["scope_key"],
                          role=current["role"], thread_url=row.get("thread_url"),
                          remaining=marked.get("REMAINING"), next_action=marked.get("NEXT-ACTION"),
                          source_sha=marked.get("SOURCE-SHA")))
    return leads


def investigation_availability(task, snapshot, role=None):
    """Filter exact completed/claimed scopes; keyword overlap remains advisory."""
    investigation = task["investigation"]
    role = role or default_role(task)
    scope = investigation_key(investigation)
    reasons, matches = [], []
    if investigation["status"] != "open":
        reasons.append("catalogue:" + investigation["status"])
    records = investigation_lifecycles(snapshot)
    # Open PR occupancy is an independent fact. A newer RELEASED claim, expired
    # claim or handoff elsewhere cannot close the PR or make its scope vacant.
    records.extend(dict(surface="pulls", row=row, markers=row.get("markers", {}),
                        status="OPEN-SUBMISSION", role=row.get("markers", {}).get("ROLE", "producer"),
                        scope_key=_marked_scope(row.get("markers", {})))
                   for row in snapshot.get("pulls", []))
    for current in records:
        if current["scope_key"] != scope or current["role"] != role:
            continue
        marked = current["markers"]
        # Reject a stale marker copied onto a different source/domain/question.
        if any(marked.get(marker) and " ".join(marked[marker].split()) != " ".join(investigation[field].split())
               for marker, field in (("INVESTIGATION-ID", "id"), ("SOURCE-SHA", "source_commit"),
                                     ("DOMAIN", "domain"), ("QUESTION", "question"))):
            continue
        status = current["status"]
        if status == "OPEN-SUBMISSION":
            reason = "open-exact-submission"
        elif status in ("DONE", "COMPLETED", "CLOSED", "SUPERSEDED", "EXHAUSTED"):
            reason = "completed-exact-scope"
        elif status in ("CLAIM", "ACTIVE") and claim_status({"markers": marked}) == "active":
            reason = "active-exact-claim"
        else:
            continue
        reasons.append(reason)
        row = current["row"]
        matches.append(dict(reason=reason, url=row.get("url"), number=row["number"],
                            surface=current["surface"], status=status))
    return dict(eligible=not reasons, reasons=sorted(set(reasons)), matches=matches)


def overlap_for_task(task, snapshot):
    terms = [task["id"], task.get("scope_key", task["id"]), *task["overlap_terms"]]
    matches = {}
    for group in GROUPS:
        matches[group] = search(snapshot.get(group, []), terms)
        seen = {row["number"] for row in matches[group]}
        if group == "pulls":
            matches[group] += [{k: v for k, v in row.items() if k != "body"}
                              for row in snapshot.get(group, [])
                              if row["number"] in task.get("potential_open_overlap_prs", [])
                              and row["number"] not in seen]
    return dict(source=snapshot.get("source", "offline"), queried_at=snapshot.get("queried_at"),
                coverage=snapshot.get("coverage", {}),
                discussions_availability=snapshot.get("discussions_availability", "unknown"), **matches,
                limits="Keyword and catalogue matches are leads; compare exact objects, hypotheses, files and drafts. No match establishes novelty.")


def claim_text(result, task, now=None):
    checked = now or dt.datetime.now(dt.timezone.utc)
    expiry = (checked + dt.timedelta(days=7)).isoformat()
    investigation = task["investigation"]
    return f"""CLAIM — {task['id']}
E99-TASK-ID: {task['id']}
E99-INVESTIGATION-ID: {investigation['id']}
E99-SCOPE-ID: {task['scope_key']}
E99-SOURCE-SHA: {investigation['source_commit']}
E99-DOMAIN: {' '.join(investigation['domain'].split())}
E99-QUESTION: {' '.join(investigation['question'].split())}
E99-ROLE: {task['role']}
E99-CLAIM-EXPIRES: {expiry}
E99-STATUS: CLAIM
Base commit: {result['checkout_commit']}
State version: {result['checkout_state_version']}
Priority revision: {result.get('priority_revision')}
Exact question: {investigation['question']}
Method: {task['selected_method']}
Dependencies: {', '.join(ref['path'] for ref in task['canonical_dependencies'])}
Stopping condition: {task['stopping_condition']}
Owner / branch: <claimant and branch>
Overlap comparison: <links and exact scope differences>

For a handoff, update this thread with:
    E99-STATUS: HANDOFF
    E99-REMAINING: <one exact unresolved implication>
    E99-NEXT-ACTION: <one feasible next step>
    Evidence / command: <public artifact, inputs, arithmetic and actual results>
    Limitations / attribution / AI role: <scope and credit>
    Independent review requested at commit: <exact artifact head SHA and scope>
"""
