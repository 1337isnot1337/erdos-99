#!/usr/bin/env python3
"""Rebuild Agent 3's deterministic source-main allocation and file ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


def git(repo: Path, *args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repo), *args], input=data, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def tree(repo: Path, revision: str) -> list[dict[str, str]]:
    raw = git(repo, "ls-tree", "-rz", "--full-tree", revision)
    records = []
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        records.append({"path": path.decode("utf-8", "surrogateescape"),
                        "mode": mode, "kind": kind, "blob": oid})
    return records


def batch_blobs(repo: Path, records: list[dict[str, str]]) -> list[bytes]:
    payload = b"".join((r["blob"] + "\n").encode("ascii") for r in records)
    result = git(repo, "cat-file", "--batch", data=payload)
    out = []
    offset = 0
    for record in records:
        end = result.index(b"\n", offset)
        header = result[offset:end].split()
        if len(header) != 3 or header[1] != b"blob":
            raise RuntimeError(f"unexpected cat-file header for {record['path']}")
        size = int(header[2])
        start = end + 1
        finish = start + size
        out.append(result[start:finish])
        if result[finish:finish + 1] != b"\n":
            raise RuntimeError(f"malformed cat-file response for {record['path']}")
        offset = finish + 1
    return out


def normalized_stem(path: str) -> str | None:
    name = path.rsplit("/", 1)[-1]
    name = re.sub(r"\.[^.]+$", "", name)
    name = re.sub(r"^verify_", "", name)
    if not name.startswith(("target_a_", "target_b_", "target_c_", "global_")):
        return None
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\1_\2_\3", name)


def is_research_markdown(path: str) -> bool:
    if not path.lower().endswith(".md"):
        return False
    return path.startswith(("docs/reports/", "docs/audits/", "docs/targets/",
                            "docs/theory/", "docs/research/", "docs/prompts/",
                            "research/"))


def is_verifier(path: str) -> bool:
    if not path.lower().endswith((".py", ".cpp")):
        return False
    name = path.rsplit("/", 1)[-1].lower()
    return name.startswith(("verify_", "check_")) or "/verify" in path.lower()


def is_third_party_exclusion_review(path: str) -> bool:
    # The source's paper corpus contains externally authored papers and OCR
    # derivatives. Preserve citations and hashes in the ledger; do not copy.
    return path.startswith(("papers/", "extracted/"))


def file_cost(path: str, size: int, conflict: bool) -> int:
    if is_third_party_exclusion_review(path):
        return 1
    if is_research_markdown(path):
        addition = min(12, math.ceil(size / 10_000))
        cost = 3 + addition
    elif is_verifier(path):
        addition = min(12, math.ceil(size / 8_000))
        cost = 3 + addition
    else:
        addition = min(12, math.ceil(size / 20_000))
        cost = 1 + addition
    return cost + (3 if conflict else 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--destination-commit", required=True)
    parser.add_argument("--frozen-index", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    src = tree(args.source, args.source_commit)
    dst = tree(args.destination, args.destination_commit)
    dst_paths = {r["path"]: r["blob"] for r in dst if r["kind"] == "blob"}
    dst_blobs = {r["blob"] for r in dst if r["kind"] == "blob"}
    src_blobs = batch_blobs(args.source, [r for r in src if r["kind"] == "blob"])
    by_path = {r["path"]: (r, data) for r, data in zip(
        [r for r in src if r["kind"] == "blob"], src_blobs)}

    frozen = {}
    for line in args.frozen_index.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        frozen[row["path"]] = row.get("source_sha256")

    provisional: list[dict] = []
    for record in src:
        if record["kind"] != "blob":
            continue
        path = record["path"]
        data = by_path[path][1]
        sha256 = hashlib.sha256(data).hexdigest()
        if record["blob"] in dst_blobs:
            relation = "exact_content_copy"
        elif path in frozen:
            relation = "frozen_813_excluded"
        elif path in dst_paths:
            relation = "same_path_content_conflict"
        else:
            relation = "missing_content"
        conflict = relation == "same_path_content_conflict"
        identical_paths = sorted(r["path"] for r in dst
                                 if r["kind"] == "blob" and r["blob"] == record["blob"])
        provisional.append({
            "source_path": path,
            "source_mode": record["mode"],
            "source_blob": record["blob"],
            "source_sha256": sha256,
            "bytes": len(data),
            "source_relation": relation,
            "destination_same_path_blob": dst_paths.get(path),
            "destination_identical_blob_paths": identical_paths,
            "frozen_source_sha256": frozen.get(path),
            "third_party_exclusion_review": is_third_party_exclusion_review(path),
            "unit_key": None,
            "file_cost": file_cost(path, len(data), conflict)
                      if relation in ("missing_content", "same_path_content_conflict") else 0,
        })

    obligations = [r for r in provisional if r["source_relation"] in
                   ("missing_content", "same_path_content_conflict")]
    md: dict[str, list[dict]] = defaultdict(list)
    verifiers: dict[str, list[dict]] = defaultdict(list)
    for row in obligations:
        stem = normalized_stem(row["source_path"])
        if not stem:
            continue
        if is_research_markdown(row["source_path"]):
            md[stem].append(row)
        elif is_verifier(row["source_path"]):
            verifiers[stem].append(row)

    groups: dict[str, list[dict]] = {}
    paired: set[str] = set()
    for stem in sorted(set(md) & set(verifiers)):
        group = sorted(md[stem] + verifiers[stem], key=lambda r: r["source_path"])
        key = "paired:" + stem
        groups[key] = group
        paired.update(r["source_path"] for r in group)
    for row in obligations:
        if row["source_path"] not in paired:
            groups["path:" + row["source_path"]] = [row]

    units = []
    for key, rows in groups.items():
        cost = sum(r["file_cost"] for r in rows)
        for row in rows:
            row["unit_key"] = key
        units.append({"unit_key": key, "cost": cost,
                      "paths": [r["source_path"] for r in rows],
                      "file_count": len(rows)})
    units.sort(key=lambda unit: (-unit["cost"], unit["unit_key"]))

    loads = [90, 75, 60]
    for unit in units:
        owner = min(range(3), key=lambda i: (loads[i], i))
        unit["owner"] = owner + 1
        loads[owner] += unit["cost"]
    ownership = {unit["unit_key"]: unit["owner"] for unit in units}
    for row in provisional:
        if row["unit_key"]:
            row["owner"] = ownership[row["unit_key"]]
        else:
            row["owner"] = None
        if row["source_path"] in frozen:
            row["frozen_set_member"] = True
        else:
            row["frozen_set_member"] = False

    args.output.mkdir(parents=True, exist_ok=True)
    alloc_path = args.output / "source-main-allocation.jsonl"
    alloc_path.write_text("".join(json.dumps(row, sort_keys=True) + "\n"
                               for row in sorted(provisional, key=lambda r: r["source_path"])))
    units_path = args.output / "source-main-units.jsonl"
    units_path.write_text("".join(json.dumps(unit, sort_keys=True) + "\n" for unit in units))
    summary = {
        "source_commit": args.source_commit,
        "source_tree": git(args.source, "rev-parse", f"{args.source_commit}^{{tree}}").decode().strip(),
        "destination_commit": args.destination_commit,
        "destination_tree": git(args.destination, "rev-parse", f"{args.destination_commit}^{{tree}}").decode().strip(),
        "frozen_813_index_sha256": hashlib.sha256(args.frozen_index.read_bytes()).hexdigest(),
        "source_file_count": len(provisional),
        "relation_counts": dict(Counter(r["source_relation"] for r in provisional)),
        "frozen_set_members": len(frozen),
        "frozen_set_present_in_source": sum(path in by_path for path in frozen),
        "obligation_file_count": len(obligations),
        "unit_count": len(units),
        "obligation_file_count_by_agent": {
            str(agent): sum(1 for r in obligations if r["owner"] == agent) for agent in (1, 2, 3)
        },
        "unit_count_by_agent": {
            str(agent): sum(1 for u in units if u["owner"] == agent) for agent in (1, 2, 3)
        },
        "workload_scores_seeded": {str(i + 1): loads[i] for i in range(3)},
        "max_minus_min_percent_of_mean": (max(loads) - min(loads)) / (sum(loads) / 3) * 100,
        "unit_cost_rule": "third-party exclusion review 1; otherwise markdown research/proof 3+min(12,ceil(bytes/10000)); Python/C++ verifier 3+min(12,ceil(bytes/8000)); other 1+min(12,ceil(bytes/20000)); +3 per same-path content conflict file",
        "pairing_rule": "pair target_a_, target_b_, target_c_, or global_ Markdown research files with Python/C++ verifier basenames after stripping verify_, extensions, and normalizing YYYY-MM-DD versus YYYY_MM_DD; all unpaired obligations use their full source path as unit key",
        "assignment_rule": "units sorted by descending cost then lexicographic unit key; seed [90,75,60]; sequentially assign to least-loaded agent, ties by agent number",
        "outputs_sha256": {},
    }
    summary["outputs_sha256"][alloc_path.name] = hashlib.sha256(alloc_path.read_bytes()).hexdigest()
    summary["outputs_sha256"][units_path.name] = hashlib.sha256(units_path.read_bytes()).hexdigest()
    (args.output / "source-main-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
