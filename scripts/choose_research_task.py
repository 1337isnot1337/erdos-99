#!/usr/bin/env python3
"""Read-only, reproducible suggestions from the E99 task catalogue."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import secrets
import subprocess
import sys
from typing import Any

try:
    from scripts.research_coordination import query_open_work, overlap_for_task, claim_text
except ModuleNotFoundError:
    from research_coordination import query_open_work, overlap_for_task, claim_text


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "docs/research/agent-task-catalog.json"
STATE_PATH = ROOT / "docs/state/theorem-state.yaml"
HEX_SEED = re.compile(r"^[0-9a-fA-F]{32}$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class CatalogError(ValueError):
    """The catalogue is malformed or references unavailable material."""


def _require_text(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{label} must be a non-empty string")


def _check_repo_file(root: Path, raw_path: Any, label: str) -> None:
    _require_text(raw_path, f"{label}.path")
    root_resolved = root.resolve()
    candidate = (root / raw_path).resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError as exc:
        raise CatalogError(f"{label} points outside the repository: {raw_path}") from exc
    if not candidate.is_file():
        raise CatalogError(f"{label} references a missing file: {raw_path}")


def validate_catalog(catalog: Any, root: Path = ROOT) -> None:
    # The public graph is generated from the authoritative manifest. Proof
    # modules need not repeat the machine claim ID in their prose.
    graph = json.loads((root / "docs/publication/proof-graph.json").read_text())
    claims = {claim["id"]: claim for claim in graph["claims"]}
    if not isinstance(catalog, dict) or catalog.get("schema_version") != 1:
        raise CatalogError("unsupported or malformed catalogue schema")
    _require_text(catalog.get("reviewed_base_commit"), "reviewed_base_commit")
    if not re.fullmatch(r"[0-9a-f]{40}", catalog["reviewed_base_commit"]):
        raise CatalogError("reviewed_base_commit must be a 40-character lowercase Git SHA")
    _require_text(catalog.get("reviewed_state_version"), "reviewed_state_version")
    _require_text(catalog.get("catalogue_revision"), "catalogue_revision")
    if catalog.get("problem_status") != "open":
        raise CatalogError("problem_status must remain open")
    authority = catalog.get("authority")
    if not isinstance(authority, list) or not authority:
        raise CatalogError("authority must be a non-empty array of repository paths")
    for index, path in enumerate(authority):
        _check_repo_file(root, path, f"authority[{index}]")
    policy = catalog.get("selection_policy")
    if not isinstance(policy, dict) or policy.get("reservation") is not False:
        raise CatalogError("selection_policy must explicitly state reservation=false")
    if policy.get("novelty_claim") is not False:
        raise CatalogError("selection_policy must explicitly state novelty_claim=false")

    tracks = catalog.get("tracks")
    if not isinstance(tracks, list) or not tracks:
        raise CatalogError("tracks must be a non-empty array")
    track_ids: set[str] = set()
    for index, track in enumerate(tracks):
        if not isinstance(track, dict):
            raise CatalogError(f"tracks[{index}] must be an object")
        track_id = track.get("id")
        if not isinstance(track_id, str) or not SLUG.fullmatch(track_id):
            raise CatalogError(f"tracks[{index}] has an invalid id")
        if track_id in track_ids:
            raise CatalogError(f"duplicate track id: {track_id}")
        track_ids.add(track_id)
        weight = track.get("weight")
        if type(weight) is not int or weight <= 0:
            raise CatalogError(f"track {track_id} weight must be a positive integer")
        _require_text(track.get("description"), f"track {track_id}.description")
    if sum(track["weight"] for track in tracks) != 100:
        raise CatalogError("track weights must sum to 100")

    tasks = catalog.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise CatalogError("tasks must be a nonempty array")
    task_ids: set[str] = set()
    by_track = {track_id: 0 for track_id in track_ids}
    required = (
        "question",
        "frontier_relation",
        "starting_experiment",
        "stopping_condition",
    )
    required_lists = (
        "assumptions",
        "canonical_dependencies",
        "previous_obstructions",
        "expected_evidence",
        "methods",
        "overlap_terms",
    )
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise CatalogError(f"tasks[{index}] must be an object")
        task_id = task.get("id")
        if not isinstance(task_id, str) or not SLUG.fullmatch(task_id):
            raise CatalogError(f"tasks[{index}] has an invalid id")
        if task_id in task_ids:
            raise CatalogError(f"duplicate task id: {task_id}")
        task_ids.add(task_id)
        track_id = task.get("track")
        if track_id not in track_ids:
            raise CatalogError(f"task {task_id} has unknown track: {track_id}")
        by_track[track_id] += 1
        if type(task.get("selection_weight")) is not int or task["selection_weight"] <= 0:
            raise CatalogError(f"task {task_id} selection_weight must be a positive integer")
        for key in required:
            _require_text(task.get(key), f"task {task_id}.{key}")
        if task.get("frontier_relation") not in {
            "current-frontier",
            "peripheral-to-frontier",
            "audit-of-canonical-result",
            "finite-model-only",
            "finite-verification-only",
            "literature-supporting",
            "exploratory-global-route",
        }:
            raise CatalogError(f"task {task_id} has unknown frontier_relation")
        for key in required_lists:
            value = task.get(key)
            if not isinstance(value, list) or not value:
                raise CatalogError(f"task {task_id}.{key} must be a non-empty array")
        for key in ("assumptions", "expected_evidence", "methods", "overlap_terms"):
            for item_index, item in enumerate(task[key]):
                _require_text(item, f"task {task_id}.{key}[{item_index}]")
        for key in ("canonical_dependencies", "previous_obstructions"):
            for ref_index, ref in enumerate(task[key]):
                if not isinstance(ref, dict):
                    raise CatalogError(f"task {task_id}.{key}[{ref_index}] must be an object")
                _check_repo_file(root, ref.get("path"), f"task {task_id}.{key}[{ref_index}]")
                _require_text(ref.get("claim"), f"task {task_id}.{key}[{ref_index}].claim")
                claim_id = ref.get("claim_id")
                if claim_id is not None:
                    _require_text(claim_id, f"task {task_id}.{key}[{ref_index}].claim_id")
                    claim = claims.get(claim_id)
                    sources = set() if claim is None else {
                        claim.get("proof"), claim.get("formal_statement_source"),
                        claim.get("independent_audit"), "docs/state/theorem-state.yaml",
                    }
                    if claim is None or ref["path"] not in sources:
                        raise CatalogError(
                            f"task {task_id} claim ID {claim_id} does not map to {ref['path']}"
                        )
        overlap_prs = task.get("potential_open_overlap_prs", [])
        if not isinstance(overlap_prs, list):
            raise CatalogError(f"task {task_id}.potential_open_overlap_prs must be an array")
        for pr in overlap_prs:
            if type(pr) is not int or pr <= 0:
                raise CatalogError(f"task {task_id} has an invalid PR overlap pointer")
    empty_tracks = sorted(track_id for track_id, count in by_track.items() if count == 0)
    if empty_tracks:
        raise CatalogError(f"tracks without tasks: {', '.join(empty_tracks)}")

    snapshot = catalog.get("open_pr_snapshot")
    if not isinstance(snapshot, list):
        raise CatalogError("open_pr_snapshot must be an array")
    snapshot_ids: set[int] = set()
    for index, pr in enumerate(snapshot):
        if not isinstance(pr, dict) or type(pr.get("number")) is not int or pr["number"] <= 0:
            raise CatalogError(f"open_pr_snapshot[{index}] has an invalid number")
        if pr["number"] in snapshot_ids:
            raise CatalogError(f"duplicate PR in overlap snapshot: {pr['number']}")
        snapshot_ids.add(pr["number"])
        _require_text(pr.get("title"), f"open_pr_snapshot[{index}].title")
    for task in tasks:
        missing = set(task.get("potential_open_overlap_prs", [])) - snapshot_ids
        if missing:
            raise CatalogError(
                f"task {task['id']} has PR pointers absent from snapshot: {sorted(missing)}"
            )


class HashStream:
    """Version-independent deterministic byte stream derived from a 128-bit seed."""

    def __init__(self, seed_hex: str):
        if not HEX_SEED.fullmatch(seed_hex):
            raise CatalogError("seed must be exactly 32 hexadecimal digits")
        self._seed = bytes.fromhex(seed_hex)
        self._counter = 0

    def randbelow(self, limit: int) -> int:
        if limit <= 0:
            raise CatalogError("random selection limit must be positive")
        ceiling = 1 << 256
        cutoff = ceiling - ceiling % limit
        while True:
            block = hashlib.sha256(self._seed + self._counter.to_bytes(8, "big")).digest()
            self._counter += 1
            value = int.from_bytes(block, "big")
            if value < cutoff:
                return value % limit


def _weighted_pick(items: list[dict[str, Any]], weight_key: str, stream: HashStream) -> dict[str, Any]:
    total = sum(item[weight_key] for item in items)
    ticket = stream.randbelow(total)
    for item in items:
        ticket -= item[weight_key]
        if ticket < 0:
            return item
    raise AssertionError("weighted selection fell through")


def scope_key(task_id: str, method: str) -> str:
    payload = json.dumps(
        {"task_id": task_id, "method": method}, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:20]


def select_tasks(
    catalog: dict[str, Any],
    seed: str,
    count: int = 3,
    track_id: str | None = None,
    task_id: str | None = None,
) -> list[dict[str, Any]]:
    validate_catalog(catalog)
    if type(count) is not int or count < 1:
        raise CatalogError("count must be a positive integer")
    stream = HashStream(seed)
    tasks = catalog["tasks"]
    tracks = catalog["tracks"]

    if task_id is not None:
        matches = [task for task in tasks if task["id"] == task_id]
        if len(matches) != 1:
            raise CatalogError(f"unknown task: {task_id}")
        if track_id is not None and matches[0]["track"] != track_id:
            raise CatalogError("task and track do not match")
        selected = matches
    else:
        eligible_tracks = [track for track in tracks if track_id is None or track["id"] == track_id]
        if not eligible_tracks:
            raise CatalogError(f"unknown track: {track_id}")
        available = {track["id"]: [task for task in tasks if task["track"] == track["id"]]
                     for track in eligible_tracks}
        available_tracks = list(eligible_tracks)
        selected = []
        seen_tracks: set[str] = set()
        while len(selected) < count:
            remaining_tracks = [track for track in available_tracks if available[track["id"]]]
            if not remaining_tracks:
                raise CatalogError("count exceeds the number of available task cards")
            fresh_tracks = [track for track in remaining_tracks if track["id"] not in seen_tracks]
            pool = fresh_tracks or remaining_tracks
            chosen_track = _weighted_pick(pool, "weight", stream)
            card = _weighted_pick(available[chosen_track["id"]], "selection_weight", stream)
            selected.append(card)
            available[chosen_track["id"]].remove(card)
            seen_tracks.add(chosen_track["id"])

    suggestions: list[dict[str, Any]] = []
    for task in selected:
        method = task["methods"][stream.randbelow(len(task["methods"]))]
        suggestions.append(
            {
                **task,
                "selected_method": method,
                "scope_key": scope_key(task["id"], method),
            }
        )
    return suggestions


def _git_head(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def _state_version(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r'^state_version:\s*["\']?([^"\'\s]+)', text, re.MULTILINE)
    return match.group(1) if match else None


def make_result(catalog: dict[str, Any], seed: str, suggestions: list[dict[str, Any]]) -> dict[str, Any]:
    current_state = _state_version(STATE_PATH)
    reviewed_state = catalog["reviewed_state_version"]
    return {
        "status": "SUGGESTIONS_ONLY_NOT_RESERVED",
        "selection_nonce": seed.lower(),
        "catalogue_revision": catalog["catalogue_revision"],
        "catalogue_reviewed_base_commit": catalog["reviewed_base_commit"],
        "catalogue_reviewed_state_version": reviewed_state,
        "checkout_commit": _git_head(ROOT),
        "checkout_state_version": current_state,
        "state_matches_reviewed_snapshot": current_state == reviewed_state,
        "warning": None if current_state == reviewed_state else (
            "The theorem-state version differs from this catalogue snapshot. Re-read the current state and route before using a suggestion."
        ),
        "suggestions": suggestions,
    }


def _format_text(result: dict[str, Any]) -> str:
    lines = [
        "E99 task suggestions — not reservations",
        f"Seed: {result['selection_nonce']}",
        f"Catalogue base: {result['catalogue_reviewed_base_commit']}",
        f"Checkout: {result['checkout_commit'] or 'unavailable'}",
        f"Theorem state: {result['checkout_state_version'] or 'unavailable'}",
    ]
    lines.extend([f"Overlap source: {result.get('overlap_status', 'not queried')}",
                  result.get("overlap_warning", "")])
    if result["warning"]:
        lines.append(f"WARNING: {result['warning']}")
    for index, task in enumerate(result["suggestions"], 1):
        lines.extend(
            [
                "",
                f"{index}. {task['id']} [{task['track']}; {task['frontier_relation']}]",
                f"   Question: {task['question']}",
                f"   Method: {task['selected_method']}",
                f"   Scope key: {task['scope_key']}",
                f"   Overlap leads: PRs {[r['number'] for r in task.get('current_overlap', {}).get('pulls', [])]}; issues {[r['number'] for r in task.get('current_overlap', {}).get('issues', [])]}",
                f"   Start: {task['starting_experiment']}",
                f"   Stop: {task['stopping_condition']}",
            ]
        )
    lines.extend(
        [
            "",
            "Before work: refresh open PRs, compare the exact object/hypotheses/method, and record the base SHA and state version.",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", help="32 hex digits; default: fresh OS-random 128-bit nonce")
    parser.add_argument("--track", help="force one catalogue track")
    parser.add_argument("--task", help="retrieve one named task without drawing a new task")
    parser.add_argument("--count", type=int, default=3, help="number of suggestions (default: 3)")
    parser.add_argument("--json", action="store_true", help="print the complete machine-readable selection")
    parser.add_argument("--live-overlap", action="store_true", help="read current PRs/issues using gh; never reserves work")
    parser.add_argument("--overlap-snapshot", type=Path, help="saved read-only query JSON for offline use")
    parser.add_argument("--claim-template", action="store_true", help="print claim and handoff text for one suggestion; does not create an issue")
    args = parser.parse_args(argv)
    if args.live_overlap and args.overlap_snapshot:
        parser.error("choose live query or offline snapshot")
    seed = args.seed if args.seed is not None else secrets.token_hex(16)
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        validate_catalog(catalog)
        suggestions = select_tasks(catalog, seed, args.count, args.track, args.task)
        result = make_result(catalog, seed, suggestions)
        if args.live_overlap:
            try:
                snapshot = query_open_work()
            except (OSError, ValueError, subprocess.SubprocessError) as exc:
                raise CatalogError("Live overlap query failed; use --overlap-snapshot or the explicitly dated offline catalogue, then refresh before claiming.") from exc
        elif args.overlap_snapshot:
            snapshot = json.loads(args.overlap_snapshot.read_text())
            if snapshot.get("schema_version") != 1 or snapshot.get("repository") != "1337isnot1337/e-99":
                raise CatalogError("invalid overlap snapshot")
            snapshot["source"] = "offline-saved-query"
        else:
            snapshot = {"source": "offline-catalogue-snapshot", "queried_at": catalog.get("open_pr_snapshot_date", catalog["reviewed_on"]),
                        "pulls": catalog["open_pr_snapshot"], "issues": []}
        result["overlap_status"] = snapshot["source"]
        result["overlap_warning"] = "Suggestions are not claims. Offline data can be stale and cannot establish that no claim exists."
        for task in suggestions:
            task["current_overlap"] = overlap_for_task(task, snapshot)
    except (OSError, json.JSONDecodeError, CatalogError, TypeError, KeyError) as exc:
        parser.error(str(exc))
        return 2
    if args.claim_template:
        if len(suggestions) != 1:
            parser.error("--claim-template requires --count 1 or --task")
        print(claim_text(result, suggestions[0]))
    else:
        print(json.dumps(result, indent=2) if args.json else _format_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
