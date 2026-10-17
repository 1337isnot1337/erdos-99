#!/usr/bin/env python3
"""Exact depth-one all-root interior-domination filter for generic support-seven H6.

The geometric input is proved in
`target_c_support7_h6_all_root_interior_domination_2026-09-19.md`.
For each interior target t in {6,7} and each root r != t, let a-b be the hull
edge bracketing the reciprocal ray r->t. Every genuine realization obeys

    D^(r)_{a,t} <= 0  or  D^(r)_{b,t} <= 0,

where D^(r)_{i,j}=angle(r,i,j)-angle(r,j,i). This verifier performs only the
first branch-and-bound level: a cell is excluded when both closed alternatives
for a single root-target pair have exact rational Farkas contradictions against
the 85-variable complete-angle system.

Numerical LPs are support discovery only. Every accepted dead branch is
recovered and checked exactly by the existing Fraction-based Farkas verifier.

Modes:
  --prepare-endpoint FILE
      reconstruct the exact post-face-(2,3)-saturation 3,874-cell endpoint and
      freeze its state-index ledger in FILE;
  --endpoint-file FILE --part P --parts N --output FILE
      exactify one deterministic partition of that endpoint;
  --endpoint-file FILE --summary-dir DIR [--summary-output FILE]
      combine partition ledgers, close exact exclusions under the certified
      hull reflection, and print the resulting exact census.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import contextlib
import hashlib
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


SAT = load(
    "h6_face23_saturation_fast",
    "verify_target_c_support7_h6_face23_saturation_fast_2026_09_19.py",
)
S = SAT.S
O = S.O
A = S.A
C = O.C
NVAR = C.NVAR
HULL = frozenset(range(6))
INTERIOR = (6, 7)
HULL_EDGES = frozenset(
    frozenset((i, (i + 1) % 6))
    for i in range(6)
)
EXPECTED_GRAPH = Counter({"C7": 3076, "C3+C4": 798})
EXPECTED_PATTERN = Counter({
    "145": 4,
    "156": 16,
    "235": 514,
    "236": 950,
    "237": 16,
    "245": 445,
    "256": 950,
    "345": 16,
    "346": 445,
    "347": 4,
    "356": 514,
})
EXPECTED_ENDPOINT_SIZE = 3874


def canonical_index_bytes(indices):
    return (",".join(map(str, indices)) + "\n").encode()


def write_endpoint(path, indices):
    indices = tuple(sorted(indices))
    payload = {
        "size": len(indices),
        "sha256": hashlib.sha256(canonical_index_bytes(indices)).hexdigest(),
        "indices": indices,
    }
    Path(path).write_text(json.dumps(payload, sort_keys=True) + "\n")
    return payload


def read_endpoint(path):
    payload = json.loads(Path(path).read_text())
    indices = tuple(int(x) for x in payload["indices"])
    assert indices == tuple(sorted(set(indices)))
    assert payload["size"] == len(indices) == EXPECTED_ENDPOINT_SIZE
    digest = hashlib.sha256(canonical_index_bytes(indices)).hexdigest()
    assert payload["sha256"] == digest
    return indices, digest


def endpoint_census(states, indices):
    graph = Counter(states[i][1] for i in indices)
    pattern = Counter("".join(map(str, states[i][5])) for i in indices)
    assert graph == EXPECTED_GRAPH
    assert pattern == EXPECTED_PATTERN
    return graph, pattern


def prepare_endpoint(path):
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    reflected, current, _ = S.predecessor_endpoint(states)
    assert len(current) == 4158

    direct = set(SAT.FRESH_IDX_4158)
    assert len(direct) == 192 and direct <= current
    image = {reflected[i] for i in direct}
    removed = direct | image
    assert len(direct & image) == 100
    assert len(removed) == 284
    assert {reflected[i] for i in removed} == removed

    endpoint = current - removed
    assert len(endpoint) == EXPECTED_ENDPOINT_SIZE
    assert {reflected[i] for i in endpoint} == endpoint
    endpoint_census(states, endpoint)
    payload = write_endpoint(path, endpoint)

    print("PASS prepare")
    print("endpoint_size", len(endpoint))
    print("endpoint_sha256", payload["sha256"])
    print("saturation_removed", len(removed))
    print("direct_image_overlap", len(direct & image))


def bracketing_hull_edge(orders, root, target):
    """Return the two hull rays immediately bracketing root->target."""
    order = tuple(orders[root])
    pos = order.index(target)

    if root in HULL:
        left = next(
            (order[k] for k in range(pos - 1, -1, -1) if order[k] in HULL),
            None,
        )
        right = next(
            (order[k] for k in range(pos + 1, len(order)) if order[k] in HULL),
            None,
        )
        assert left is not None and right is not None, (root, target, order)
    else:
        n = len(order)
        left = next(
            order[(pos - step) % n]
            for step in range(1, n)
            if order[(pos - step) % n] in HULL
        )
        right = next(
            order[(pos + step) % n]
            for step in range(1, n)
            if order[(pos + step) % n] in HULL
        )

    assert left != right
    assert frozenset((left, right)) in HULL_EDGES, (
        root, target, order, left, right,
    )
    return left, right


def domination_branch(state, orders, root, target, endpoint):
    """Encode the closed halfspace D^(root)_{endpoint,target} <= 0.

    A^(r)_{ij}=angle(r,i,j), so D=A^(r)_{ij}-A^(r)_{ji}. Added closed
    constraints use the repository convention const + row*x >= 0; therefore
    this branch is represented as -D >= 0.
    """
    chi = state[4]
    row1, const1 = C.ordinary_angle(orders, chi, endpoint, root, target)
    row2, const2 = C.ordinary_angle(orders, chi, target, root, endpoint)
    row = tuple(F(y) - F(x) for x, y in zip(row1, row2))
    const = F(const2) - F(const1)
    assert len(row) == NVAR
    return ((row, const, ("ROOT_DOM", root, target, endpoint)),)


def exact_dead_branch(system, closed):
    margin, result = O.numerical_candidate(system, closed)
    if margin is None:
        return "solver_failure", None
    if margin > 1e-8:
        return "live", None
    cert = A.exactify_support(system, closed, result)
    if cert is None:
        return "exactification_miss", None
    return "dead", cert


def scan_partition(endpoint_file, part, parts, output):
    assert parts > 0 and 0 <= part < parts
    indices, endpoint_sha = read_endpoint(endpoint_file)
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    endpoint_census(states, indices)

    start = part * len(indices) // parts
    stop = (part + 1) * len(indices) // parts
    excluded = []
    witness_records = []
    graph = Counter()
    pattern = Counter()
    witness_types = Counter()
    forced = Counter()
    max_denominator = 1
    branch_lp = 0
    solver_failures = 0
    exactification_misses = 0

    # Root 0 is the old ground-root special case. Test the genuinely new roots
    # first; root 0 remains in the list for completeness.
    root_priority = (1, 2, 3, 4, 5, 6, 7, 0)

    for serial in range(start, stop):
        idx = indices[serial]
        state = states[idx]
        system = C.build_system(state)
        orders = C.orders_for_state(state)
        found = None

        for target in INTERIOR:
            for root in root_priority:
                if root == target:
                    continue
                a, b = bracketing_hull_edge(orders, root, target)
                certs = []
                both_dead = True
                for h in (a, b):
                    closed = domination_branch(state, orders, root, target, h)
                    status, cert = exact_dead_branch(system, closed)
                    branch_lp += 1
                    if status == "solver_failure":
                        solver_failures += 1
                        both_dead = False
                        break
                    if status == "exactification_miss":
                        exactification_misses += 1
                        both_dead = False
                        break
                    if status == "live":
                        both_dead = False
                        break
                    certs.append(cert)
                if not both_dead:
                    continue

                assert len(certs) == 2
                found = (root, target, a, b, certs)
                break
            if found is not None:
                break

        if found is None:
            continue

        root, target, a, b, certs = found
        excluded.append(idx)
        graph[state[1]] += 1
        pat = "".join(map(str, state[5]))
        pattern[pat] += 1
        witness_types[(root, target, min(a, b), max(a, b))] += 1
        packed_certs = []
        for value, denominator in certs:
            forced["zero" if value == 0 else "negative"] += 1
            max_denominator = max(max_denominator, denominator)
            packed_certs.append({
                "forced_num": value.numerator,
                "forced_den": value.denominator,
                "max_multiplier_denominator": denominator,
            })
        witness_records.append({
            "state_index": idx,
            "serial": serial,
            "graph": state[1],
            "pattern": pat,
            "root": root,
            "target": target,
            "edge": [a, b],
            "certificates": packed_certs,
        })
        print(
            "EXCLUDE", serial, idx, state[1], pat,
            "root_target", root, target, "edge", a, b,
            flush=True,
        )

    result_payload = {
        "endpoint_sha256": endpoint_sha,
        "part": part,
        "parts": parts,
        "start": start,
        "stop": stop,
        "checked": stop - start,
        "excluded": excluded,
        "graph": dict(sorted(graph.items())),
        "patterns": dict(sorted(pattern.items())),
        "witness_types": {
            ",".join(map(str, k)): v for k, v in sorted(witness_types.items())
        },
        "forced": dict(sorted(forced.items())),
        "max_denominator": max_denominator,
        "branch_lp": branch_lp,
        "solver_failures": solver_failures,
        "exactification_misses": exactification_misses,
        "witness_records": witness_records,
    }
    Path(output).write_text(json.dumps(result_payload, sort_keys=True) + "\n")

    print("PASS scan")
    print("part", part, "of", parts)
    print("range", start, stop)
    print("checked", stop - start)
    print("excluded", len(excluded))
    print("graph", dict(sorted(graph.items())))
    print("patterns", dict(sorted(pattern.items())))
    print("branch_lp", branch_lp)
    print("forced", dict(sorted(forced.items())))
    print("max_denominator", max_denominator)
    print("solver_failures", solver_failures)
    print("exactification_misses", exactification_misses)


def summarize(endpoint_file, summary_dir, summary_output=None):
    indices, endpoint_sha = read_endpoint(endpoint_file)
    endpoint = set(indices)
    files = sorted(Path(summary_dir).glob("result-*.json"))
    assert files, summary_dir

    payloads = [json.loads(p.read_text()) for p in files]
    parts_values = {p["parts"] for p in payloads}
    assert len(parts_values) == 1
    parts = parts_values.pop()
    assert len(payloads) == parts
    assert {p["part"] for p in payloads} == set(range(parts))
    assert all(p["endpoint_sha256"] == endpoint_sha for p in payloads)

    ranges = sorted((p["start"], p["stop"]) for p in payloads)
    assert ranges[0][0] == 0 and ranges[-1][1] == len(indices)
    assert all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
    assert sum(p["checked"] for p in payloads) == len(indices)

    direct = set()
    for p in payloads:
        xs = set(p["excluded"])
        assert len(xs) == len(p["excluded"])
        assert direct.isdisjoint(xs)
        direct |= xs
    assert direct <= endpoint

    states = O.tri.collect_survivors()
    assert len(states) == 14174
    endpoint_census(states, indices)
    reflected, _ = S.E5.reflection_data(states)
    assert {reflected[i] for i in endpoint} == endpoint

    image = {reflected[i] for i in direct}
    removed = direct | image
    assert removed <= endpoint
    assert {reflected[i] for i in removed} == removed
    survivors = endpoint - removed
    assert {reflected[i] for i in survivors} == survivors

    graph_removed = Counter(states[i][1] for i in removed)
    pattern_removed = Counter("".join(map(str, states[i][5])) for i in removed)
    graph_survivors = Counter(states[i][1] for i in survivors)
    pattern_survivors = Counter("".join(map(str, states[i][5])) for i in survivors)
    assert graph_removed + graph_survivors == EXPECTED_GRAPH
    assert pattern_removed + pattern_survivors == EXPECTED_PATTERN

    summary = {
        "endpoint_sha256": endpoint_sha,
        "endpoint_size": len(endpoint),
        "direct_exclusions": len(direct),
        "reflected_image": len(image),
        "direct_image_overlap": len(direct & image),
        "removed_union": len(removed),
        "survivors": len(survivors),
        "graph_removed": dict(sorted(graph_removed.items())),
        "pattern_removed": dict(sorted(pattern_removed.items())),
        "graph_survivors": dict(sorted(graph_survivors.items())),
        "pattern_survivors": dict(sorted(pattern_survivors.items())),
        "direct_indices": sorted(direct),
        "removed_indices": sorted(removed),
        "survivor_indices": sorted(survivors),
        "solver_failures": sum(p["solver_failures"] for p in payloads),
        "exactification_misses": sum(p["exactification_misses"] for p in payloads),
        "branch_lp": sum(p["branch_lp"] for p in payloads),
    }
    if summary_output:
        Path(summary_output).write_text(json.dumps(summary, sort_keys=True) + "\n")

    print("PASS summary")
    for key in (
        "endpoint_size", "direct_exclusions", "reflected_image",
        "direct_image_overlap", "removed_union", "survivors",
        "solver_failures", "exactification_misses", "branch_lp",
    ):
        print(key, summary[key])
    print("graph_removed", summary["graph_removed"])
    print("pattern_removed", summary["pattern_removed"])
    print("graph_survivors", summary["graph_survivors"])
    print("pattern_survivors", summary["pattern_survivors"])


def main():
    parser = ArgumentParser()
    parser.add_argument("--prepare-endpoint")
    parser.add_argument("--endpoint-file")
    parser.add_argument("--part", type=int)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--output")
    parser.add_argument("--summary-dir")
    parser.add_argument("--summary-output")
    args = parser.parse_args()

    if args.prepare_endpoint:
        assert args.endpoint_file is None and args.part is None and args.summary_dir is None
        prepare_endpoint(args.prepare_endpoint)
        return

    assert args.endpoint_file is not None
    if args.summary_dir:
        assert args.part is None and args.parts is None
        summarize(args.endpoint_file, args.summary_dir, args.summary_output)
        return

    assert args.part is not None and args.parts is not None and args.output
    scan_partition(args.endpoint_file, args.part, args.parts, args.output)


if __name__ == "__main__":
    main()
