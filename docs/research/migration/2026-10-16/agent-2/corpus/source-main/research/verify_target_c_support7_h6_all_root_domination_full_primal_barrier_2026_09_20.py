#!/usr/bin/env python3
"""Exact joint-primal audit for all fourteen H6 domination disjunctions.

For every cell in the frozen 3,874-cell generic-H6 endpoint, solve the base
85-variable complete-angle affine relaxation once.  The numerical LP point is
used only to choose one of the two domination alternatives for each of the
fourteen root/target pairs.  A cell is certified only if the existing rational
primal reconstructor then produces one exact point satisfying simultaneously

* every complete-angle equality,
* every original strict affine facet, and
* all fourteen selected domination halfspaces.

Thus a successful cell is an exact witness that the complete-angle affine
relaxation plus the full all-root domination cover cannot exclude that cell.
Numerical feasibility alone never certifies a witness.

The script is chunkable with --part/--parts and can combine JSON outputs with
--summary-dir.  It does not claim Euclidean realizability of any cell.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import contextlib
import importlib.util
import io
import json

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


B = load(
    "h6_rootdom_full_bnb",
    "verify_target_c_support7_h6_all_root_domination_full_bnb_2026_09_19.py",
)
E = B.E
P = B.P
O = B.O
C = B.C
NVAR = B.NVAR
EXPECTED_SIZE = 3874
EXPECTED_SHA256 = "b5e05331a267ea5c764b96ef834c1a6ffd5f03599b372e86cae3b8e77ea9666a"

assert E.ENDPOINT_SIZE == EXPECTED_SIZE
assert E.INDEX_SHA256 == EXPECTED_SHA256


def certify_root_witness(system, state, orders):
    """Return one exact fourteen-branch witness summary, or an unresolved reason."""
    margin, result = O.numerical_candidate(system, ())
    if margin is None:
        return None, "solver_failure"
    if margin <= 1e-8:
        return None, "nonpositive_base_margin"

    clauses = B.make_clauses(state, orders)
    numeric = result.x[:NVAR]
    choices = {}
    numerical_slacks = []
    for i, clause in enumerate(clauses):
        slacks = tuple(
            B.float_slack(branch_closed, numeric)
            for _, branch_closed in clause["branches"]
        )
        choice = 0 if slacks[0] >= slacks[1] else 1
        if slacks[choice] < -1e-9:
            return None, "root_point_misses_disjunction"
        choices[i] = choice
        numerical_slacks.append(slacks[choice])

    full_closed = tuple(
        inequality
        for i, choice in sorted(choices.items())
        for inequality in clauses[i]["branches"][choice][1]
    )
    assert len(full_closed) == len(clauses) == 14

    witness = P.exactify_primal(system, full_closed, result)
    if witness is None:
        return None, "exact_primal_reconstruction_failure"

    min_strict = F(witness["min_strict_num"], witness["min_strict_den"])
    min_closed = F(witness["min_closed_num"], witness["min_closed_den"])
    assert min_strict > 0
    assert min_closed >= 0

    return {
        "limit": witness["limit"],
        "max_denominator": witness["max_denominator"],
        "min_strict": [min_strict.numerator, min_strict.denominator],
        "min_closed": [min_closed.numerator, min_closed.denominator],
        "strict_domination": min_closed > 0,
        "min_numerical_selected_slack": min(numerical_slacks),
    }, None


def scan(part, parts, output):
    assert parts > 0 and 0 <= part < parts
    endpoint = E.decode_endpoint()
    states = O.tri.collect_survivors()
    assert len(endpoint) == EXPECTED_SIZE
    assert len(states) == E.UNIVERSE_SIZE == 14174

    start = part * len(endpoint) // parts
    stop = (part + 1) * len(endpoint) // parts
    status = Counter()
    graph = Counter()
    pattern = Counter()
    limit_counts = Counter()
    max_denominator = 1
    min_strict = None
    min_closed = None
    strict_domination = 0
    unresolved = []

    for serial in range(start, stop):
        idx = endpoint[serial]
        state = states[idx]
        system = C.build_system(state)
        orders = C.orders_for_state(state)
        witness, reason = certify_root_witness(system, state, orders)
        if witness is None:
            status[reason] += 1
            unresolved.append({
                "serial": serial,
                "state_index": idx,
                "graph": state[1],
                "pattern": "".join(map(str, state[5])),
                "reason": reason,
            })
            print("UNRESOLVED", serial, idx, reason, flush=True)
            continue

        status["exact_joint_witness"] += 1
        graph[state[1]] += 1
        pattern["".join(map(str, state[5]))] += 1
        limit_counts[witness["limit"]] += 1
        max_denominator = max(max_denominator, witness["max_denominator"])
        s = F(*witness["min_strict"])
        c = F(*witness["min_closed"])
        if min_strict is None or s < min_strict:
            min_strict = s
        if min_closed is None or c < min_closed:
            min_closed = c
        strict_domination += int(witness["strict_domination"])

    payload = {
        "endpoint_size": EXPECTED_SIZE,
        "endpoint_sha256": EXPECTED_SHA256,
        "part": part,
        "parts": parts,
        "start": start,
        "stop": stop,
        "checked": stop - start,
        "status": dict(sorted(status.items())),
        "exact_joint_witnesses": status["exact_joint_witness"],
        "strict_domination_witnesses": strict_domination,
        "unresolved": unresolved,
        "graph": dict(sorted(graph.items())),
        "patterns": dict(sorted(pattern.items())),
        "limit_counts": {str(k): v for k, v in sorted(limit_counts.items())},
        "max_denominator": max_denominator,
        "min_strict": None if min_strict is None else [min_strict.numerator, min_strict.denominator],
        "min_closed": None if min_closed is None else [min_closed.numerator, min_closed.denominator],
    }
    Path(output).write_text(json.dumps(payload, sort_keys=True) + "\n")

    print("PASS scan")
    for key in (
        "part", "parts", "start", "stop", "checked", "exact_joint_witnesses",
        "strict_domination_witnesses", "max_denominator", "min_strict", "min_closed",
    ):
        print(key, payload[key])
    print("status", payload["status"])
    print("limit_counts", payload["limit_counts"])
    print("graph", payload["graph"])
    print("patterns", payload["patterns"])


def summarize(directory, output=None):
    files = sorted(Path(directory).glob("joint-primal-*.json"))
    assert files, directory
    payloads = [json.loads(path.read_text()) for path in files]
    parts_set = {p["parts"] for p in payloads}
    assert len(parts_set) == 1
    parts = parts_set.pop()
    assert len(payloads) == parts
    assert {p["part"] for p in payloads} == set(range(parts))
    assert all(p["endpoint_sha256"] == EXPECTED_SHA256 for p in payloads)

    ranges = sorted((p["start"], p["stop"]) for p in payloads)
    assert ranges[0][0] == 0 and ranges[-1][1] == EXPECTED_SIZE
    assert all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
    assert sum(p["checked"] for p in payloads) == EXPECTED_SIZE

    unresolved = [item for p in payloads for item in p["unresolved"]]
    graph = Counter()
    pattern = Counter()
    limits = Counter()
    for p in payloads:
        graph.update(p["graph"])
        pattern.update(p["patterns"])
        limits.update({int(k): v for k, v in p["limit_counts"].items()})

    strict_values = [F(*p["min_strict"]) for p in payloads if p["min_strict"] is not None]
    closed_values = [F(*p["min_closed"]) for p in payloads if p["min_closed"] is not None]
    summary = {
        "endpoint_size": EXPECTED_SIZE,
        "endpoint_sha256": EXPECTED_SHA256,
        "checked": sum(p["checked"] for p in payloads),
        "exact_joint_witnesses": sum(p["exact_joint_witnesses"] for p in payloads),
        "strict_domination_witnesses": sum(p["strict_domination_witnesses"] for p in payloads),
        "unresolved": unresolved,
        "graph": dict(sorted(graph.items())),
        "patterns": dict(sorted(pattern.items())),
        "limit_counts": {str(k): v for k, v in sorted(limits.items())},
        "max_denominator": max(p["max_denominator"] for p in payloads),
        "min_strict": None if not strict_values else [min(strict_values).numerator, min(strict_values).denominator],
        "min_closed": None if not closed_values else [min(closed_values).numerator, min(closed_values).denominator],
    }

    # A complete audit proves the barrier only when every endpoint cell has one
    # exact witness, and every selected domination inequality is strict in that
    # witness.  The latter is stronger than necessary for the closed cover.
    assert summary["checked"] == EXPECTED_SIZE
    assert summary["exact_joint_witnesses"] == EXPECTED_SIZE
    assert summary["strict_domination_witnesses"] == EXPECTED_SIZE
    assert not unresolved
    assert sum(graph.values()) == EXPECTED_SIZE
    assert sum(pattern.values()) == EXPECTED_SIZE

    if output:
        Path(output).write_text(json.dumps(summary, sort_keys=True) + "\n")

    print("PASS summary: every endpoint cell has one exact joint all-root domination witness")
    for key in (
        "endpoint_size", "checked", "exact_joint_witnesses",
        "strict_domination_witnesses", "max_denominator", "min_strict", "min_closed",
    ):
        print(key, summary[key])
    print("limit_counts", summary["limit_counts"])
    print("graph", summary["graph"])
    print("patterns", summary["patterns"])


def main():
    parser = ArgumentParser()
    parser.add_argument("--part", type=int)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--output")
    parser.add_argument("--summary-dir")
    parser.add_argument("--summary-output")
    args = parser.parse_args()

    if args.summary_dir:
        assert args.part is None and args.parts is None and args.output is None
        summarize(args.summary_dir, args.summary_output)
        return

    assert args.part is not None and args.parts is not None and args.output
    scan(args.part, args.parts, args.output)


if __name__ == "__main__":
    main()
