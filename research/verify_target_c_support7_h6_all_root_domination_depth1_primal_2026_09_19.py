#!/usr/bin/env python3
"""Exact primal audit of the depth-one all-root domination barrier.

For every cell in the frozen 3,874-cell generic-H6 endpoint and every one of
the fourteen root/target domination disjunctions, try to exhibit an exact
rational point satisfying the complete 85-variable affine system together with
one closed branch of that disjunction.  If this succeeds for all fourteen
pairs, that cell cannot be excluded by any single domination disjunction in
isolation.

Floating point LPs are used only to choose promising primal vertices.  A
reported witness is accepted only after coordinatewise rational reconstruction
and exact Fraction checks of every equality, every original strict facet, and
the added closed branch facet.  Numerical feasibility alone never certifies a
witness.
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


D = load(
    "h6_rootdom_depth1",
    "verify_target_c_support7_h6_all_root_domination_depth1_2026_09_19.py",
)
E = load(
    "h6_endpoint_3874",
    "target_c_support7_h6_endpoint_3874_ledger_2026_09_19.py",
)
O = D.O
C = D.C
NVAR = D.NVAR
INTERIOR = D.INTERIOR
ROOT_PRIORITY = (1, 2, 3, 4, 5, 6, 7, 0)
LIMITS = (1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000)
EXPECTED_PAIRS_PER_CELL = 14


def dot(row, x):
    return sum((F(a) * b for a, b in zip(row, x) if a), F(0))


def exactify_primal(system, closed, result):
    """Recover an exact rational feasible point from a numerical LP vertex."""
    rows, rhs, _, strict = system
    numeric = result.x[:NVAR]

    for limit in LIMITS:
        x = tuple(F(float(z)).limit_denominator(limit) for z in numeric)

        if any(dot(row, x) != F(b) for row, b in zip(rows, rhs)):
            continue

        strict_values = tuple(F(const) + dot(row, x) for row, const, _ in strict)
        if any(v <= 0 for v in strict_values):
            continue

        closed_values = tuple(F(const) + dot(row, x) for row, const, _ in closed)
        if any(v < 0 for v in closed_values):
            continue

        max_den = max((z.denominator for z in x), default=1)
        min_strict = min(strict_values)
        min_closed = min(closed_values, default=F(0))
        return {
            "limit": limit,
            "max_denominator": max_den,
            "min_strict_num": min_strict.numerator,
            "min_strict_den": min_strict.denominator,
            "min_closed_num": min_closed.numerator,
            "min_closed_den": min_closed.denominator,
        }

    return None


def scan(part, parts, output):
    assert parts > 0 and 0 <= part < parts
    endpoint = E.decode_endpoint()
    assert len(endpoint) == E.ENDPOINT_SIZE == 3874
    states = O.tri.collect_survivors()
    assert len(states) == E.UNIVERSE_SIZE == 14174

    start = part * len(endpoint) // parts
    stop = (part + 1) * len(endpoint) // parts

    certified_cells = 0
    exact_pairs = 0
    unresolved = []
    graph_unresolved = Counter()
    pattern_unresolved = Counter()
    branch_lp = 0
    numerical_live = 0
    exact_primal_failures = 0
    max_denominator = 1
    limit_counts = Counter()
    min_positive_strict = None
    zero_closed_witnesses = 0

    for serial in range(start, stop):
        idx = endpoint[serial]
        state = states[idx]
        system = C.build_system(state)
        orders = C.orders_for_state(state)
        cell_ok = True
        failed_pairs = []

        for target in INTERIOR:
            for root in ROOT_PRIORITY:
                if root == target:
                    continue
                a, b = D.bracketing_hull_edge(orders, root, target)
                pair_ok = False

                for h in (a, b):
                    closed = D.domination_branch(state, orders, root, target, h)
                    margin, result = O.numerical_candidate(system, closed)
                    branch_lp += 1
                    if margin is None or margin <= 1e-9:
                        continue
                    numerical_live += 1
                    witness = exactify_primal(system, closed, result)
                    if witness is None:
                        exact_primal_failures += 1
                        continue

                    pair_ok = True
                    exact_pairs += 1
                    max_denominator = max(max_denominator, witness["max_denominator"])
                    limit_counts[witness["limit"]] += 1
                    s = F(witness["min_strict_num"], witness["min_strict_den"])
                    if min_positive_strict is None or s < min_positive_strict:
                        min_positive_strict = s
                    if witness["min_closed_num"] == 0:
                        zero_closed_witnesses += 1
                    break

                if not pair_ok:
                    cell_ok = False
                    failed_pairs.append((root, target, a, b))

        if cell_ok:
            certified_cells += 1
        else:
            graph_unresolved[state[1]] += 1
            pat = "".join(map(str, state[5]))
            pattern_unresolved[pat] += 1
            unresolved.append({
                "serial": serial,
                "state_index": idx,
                "graph": state[1],
                "pattern": pat,
                "failed_pairs": failed_pairs,
            })
            print("UNRESOLVED", serial, idx, failed_pairs, flush=True)

    payload = {
        "part": part,
        "parts": parts,
        "start": start,
        "stop": stop,
        "checked_cells": stop - start,
        "certified_cells": certified_cells,
        "unresolved_cells": len(unresolved),
        "exact_pairs": exact_pairs,
        "expected_pairs": (stop - start) * EXPECTED_PAIRS_PER_CELL,
        "branch_lp": branch_lp,
        "numerical_live": numerical_live,
        "exact_primal_failures": exact_primal_failures,
        "max_denominator": max_denominator,
        "limit_counts": {str(k): v for k, v in sorted(limit_counts.items())},
        "min_positive_strict": None if min_positive_strict is None else [
            min_positive_strict.numerator, min_positive_strict.denominator,
        ],
        "zero_closed_witnesses": zero_closed_witnesses,
        "graph_unresolved": dict(sorted(graph_unresolved.items())),
        "pattern_unresolved": dict(sorted(pattern_unresolved.items())),
        "unresolved": unresolved,
    }
    Path(output).write_text(json.dumps(payload, sort_keys=True) + "\n")

    print("PASS scan")
    for k in (
        "part", "parts", "start", "stop", "checked_cells",
        "certified_cells", "unresolved_cells", "exact_pairs",
        "expected_pairs", "branch_lp", "numerical_live",
        "exact_primal_failures", "max_denominator", "zero_closed_witnesses",
    ):
        print(k, payload[k])
    print("limit_counts", payload["limit_counts"])
    print("min_positive_strict", payload["min_positive_strict"])
    print("graph_unresolved", payload["graph_unresolved"])
    print("pattern_unresolved", payload["pattern_unresolved"])


def summarize(directory, output=None):
    files = sorted(Path(directory).glob("primal-*.json"))
    assert files
    payloads = [json.loads(p.read_text()) for p in files]
    parts_set = {p["parts"] for p in payloads}
    assert len(parts_set) == 1
    parts = parts_set.pop()
    assert len(payloads) == parts
    assert {p["part"] for p in payloads} == set(range(parts))
    ranges = sorted((p["start"], p["stop"]) for p in payloads)
    assert ranges[0][0] == 0 and ranges[-1][1] == E.ENDPOINT_SIZE
    assert all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))

    unresolved = [x for p in payloads for x in p["unresolved"]]
    limit_counts = Counter()
    for p in payloads:
        limit_counts.update({int(k): v for k, v in p["limit_counts"].items()})
    min_stricts = [
        F(*p["min_positive_strict"])
        for p in payloads if p["min_positive_strict"] is not None
    ]
    summary = {
        "endpoint_size": E.ENDPOINT_SIZE,
        "endpoint_sha256": E.INDEX_SHA256,
        "certified_cells": sum(p["certified_cells"] for p in payloads),
        "unresolved_cells": len(unresolved),
        "exact_pairs": sum(p["exact_pairs"] for p in payloads),
        "expected_pairs": E.ENDPOINT_SIZE * EXPECTED_PAIRS_PER_CELL,
        "branch_lp": sum(p["branch_lp"] for p in payloads),
        "numerical_live": sum(p["numerical_live"] for p in payloads),
        "exact_primal_failures": sum(p["exact_primal_failures"] for p in payloads),
        "max_denominator": max(p["max_denominator"] for p in payloads),
        "limit_counts": {str(k): v for k, v in sorted(limit_counts.items())},
        "min_positive_strict": None if not min_stricts else [
            min(min_stricts).numerator, min(min_stricts).denominator,
        ],
        "zero_closed_witnesses": sum(p["zero_closed_witnesses"] for p in payloads),
        "unresolved": unresolved,
    }
    if output:
        Path(output).write_text(json.dumps(summary, sort_keys=True) + "\n")

    print("PASS summary")
    for k in (
        "endpoint_size", "certified_cells", "unresolved_cells", "exact_pairs",
        "expected_pairs", "branch_lp", "numerical_live",
        "exact_primal_failures", "max_denominator", "zero_closed_witnesses",
    ):
        print(k, summary[k])
    print("limit_counts", summary["limit_counts"])
    print("min_positive_strict", summary["min_positive_strict"])


def main():
    parser = ArgumentParser()
    parser.add_argument("--part", type=int)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--output")
    parser.add_argument("--summary-dir")
    parser.add_argument("--summary-output")
    args = parser.parse_args()

    if args.summary_dir:
        assert args.part is None and args.parts is None
        summarize(args.summary_dir, args.summary_output)
        return

    assert args.part is not None and args.parts is not None and args.output
    scan(args.part, args.parts, args.output)


if __name__ == "__main__":
    main()
