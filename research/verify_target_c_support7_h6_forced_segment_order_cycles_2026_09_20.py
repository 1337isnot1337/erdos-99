#!/usr/bin/env python3
"""Exact forced-segment-order cycle filter for the frozen 3,874-state H6 endpoint.

For each endpoint cell, inspect the 168 rooted angle differences

    D^(r)_{ij} = angle(r,i,j) - angle(r,j,i).

The global sine-law sign identity gives

    sign D^(r)_{ij} = sign(|rj|-|ri|).

A numerical LP point chooses which strict sign to try to prove.  To certify
D>0, the verifier adds the closed opposite halfspace D<=0 and accepts the sign
only when the existing exact rational Farkas routine proves that halfspace
infeasible.  D<0 is handled symmetrically.  Numerically feasible opposite
halfspaces are never treated as forced.

Certified strict comparisons orient edges of L(K8) from shorter segment to
longer segment.  A cell is excluded only after these exact forced edges contain
a directed cycle.  The reported cycle stores one exact Farkas certificate per
edge.  No floating-point result is itself a certificate.

The scan is chunkable with --part/--parts and can combine JSON outputs with
--summary-dir.  It is conservative: failure to exactify a candidate forced edge
merely discards that edge.
"""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
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
    "h6_rootdom_depth1_for_segment_cycles",
    "verify_target_c_support7_h6_all_root_domination_depth1_2026_09_19.py",
)
E = load(
    "h6_endpoint_3874_for_segment_cycles",
    "target_c_support7_h6_endpoint_3874_ledger_2026_09_19.py",
)
O = D.O
A = D.A
C = D.C
NVAR = D.NVAR
EXPECTED_SIZE = 3874
EXPECTED_SHA256 = "b5e05331a267ea5c764b96ef834c1a6ffd5f03599b372e86cae3b8e77ea9666a"
assert E.ENDPOINT_SIZE == EXPECTED_SIZE
assert E.INDEX_SHA256 == EXPECTED_SHA256

V = tuple(range(8))
SEGMENTS = tuple(combinations(V, 2))
assert len(SEGMENTS) == 28

COMPARISONS = tuple(
    (r, i, j)
    for r in V
    for i, j in combinations(tuple(v for v in V if v != r), 2)
)
assert len(COMPARISONS) == 168


def segment_difference(state, orders, root, i, j):
    """Return exact affine (row,const) for D^(root)_{ij}."""
    chi = state[4]
    # angle(root,i,j) is the ordinary angle at reciprocal vertex i between
    # the rays to root and j; likewise angle(root,j,i) is at j.
    row_i, const_i = C.ordinary_angle(orders, chi, i, root, j)
    row_j, const_j = C.ordinary_angle(orders, chi, j, root, i)
    row = tuple(F(a) - F(b) for a, b in zip(row_i, row_j))
    const = F(const_i) - F(const_j)
    assert len(row) == NVAR
    return row, const


def affine_value(row, const, x):
    return float(const) + sum(float(a) * float(b) for a, b in zip(row, x) if a)


def opposite_closed(row, const, forced_sign, label):
    """Closed opposite sign branch under convention const + row*x >= 0."""
    if forced_sign > 0:
        # Candidate D>0; test D<=0, i.e. -D >= 0.
        return ((tuple(-a for a in row), -const, label + ("LE0",)),)
    # Candidate D<0; test D>=0.
    return ((tuple(row), const, label + ("GE0",)),)


def orientation(root, i, j, forced_sign):
    """Return directed L(K8) edge shorter -> longer."""
    ri = tuple(sorted((root, i)))
    rj = tuple(sorted((root, j)))
    assert ri != rj
    if forced_sign > 0:
        # D>0 iff |rj|>|ri|.
        return ri, rj
    return rj, ri


def find_cycle(edge_records):
    """Return one directed simple cycle as ordered (u,v) edges, or None."""
    out = {e: [] for e in SEGMENTS}
    for u, v in edge_records:
        out[u].append(v)
    for u in out:
        out[u].sort()

    color = {e: 0 for e in SEGMENTS}
    parent = {}

    def dfs(u):
        color[u] = 1
        for v in out[u]:
            if color[v] == 0:
                parent[v] = u
                got = dfs(v)
                if got is not None:
                    return got
            elif color[v] == 1:
                # Back edge u->v. Recover v -> ... -> u -> v.
                verts = [u]
                while verts[-1] != v:
                    verts.append(parent[verts[-1]])
                verts.reverse()
                return tuple(
                    (verts[k], verts[k + 1])
                    for k in range(len(verts) - 1)
                ) + ((u, v),)
        color[u] = 2
        return None

    for start in SEGMENTS:
        if color[start] == 0:
            got = dfs(start)
            if got is not None:
                return got
    return None


def exactify_cycle(system, edge_records, stats):
    """Exactify one candidate cycle; discard any edge whose proof misses."""
    while True:
        cycle = find_cycle(edge_records)
        if cycle is None:
            return None
        packed = []
        failed = None
        for edge in cycle:
            rec = edge_records[edge]
            if rec.get("certificate") is None:
                cert = A.exactify_support(system, rec["closed"], rec["result"])
                stats["exactification_attempts"] += 1
                if cert is None:
                    stats["exactification_misses"] += 1
                    failed = edge
                    break
                value, denominator = cert
                rec["certificate"] = {
                    "forced_num": value.numerator,
                    "forced_den": value.denominator,
                    "max_multiplier_denominator": denominator,
                }
                stats["max_multiplier_denominator"] = max(
                    stats["max_multiplier_denominator"], denominator
                )
                stats["farkas_forced_zero" if value == 0 else "farkas_forced_negative"] += 1
            packed.append(rec)
        if failed is not None:
            # A numerical candidate is not evidence. Remove this edge from the
            # candidate graph and search for a different exactifiable cycle.
            del edge_records[failed]
            continue
        return packed


def candidate_tests_for_difference(d, tol=1e-9):
    if d > tol:
        return (1,)
    if d < -tol:
        return (-1,)
    # Near a wall, do not trust the numerical sign. Test both closed sides;
    # exact Farkas recovery, if any, decides the strict sign.
    return (1, -1)


def certify_cell(system, state, orders, stats):
    margin, base_result = O.numerical_candidate(system, ())
    stats["base_lp"] += 1
    if margin is None:
        stats["base_solver_failures"] += 1
        return None, "base_solver_failure"
    if margin <= 1e-8:
        # Frozen endpoint cells are known exactly affine-feasible. Treat an
        # unexpected numerical failure as unresolved, never as an exclusion.
        stats["base_nonpositive_margin"] += 1
        return None, "base_nonpositive_margin"

    numeric = base_result.x[:NVAR]
    edge_records = {}

    for root, i, j in COMPARISONS:
        row, const = segment_difference(state, orders, root, i, j)
        d = affine_value(row, const, numeric)
        label = ("SEGORDER", root, i, j)
        for sign in candidate_tests_for_difference(d):
            closed = opposite_closed(row, const, sign, label)
            branch_margin, result = O.numerical_candidate(system, closed)
            stats["opposite_branch_lp"] += 1
            if branch_margin is None:
                stats["branch_solver_failures"] += 1
                continue
            if branch_margin > 1e-8:
                continue

            u, v = orientation(root, i, j, sign)
            reverse = (v, u)
            rec = {
                "root": root,
                "i": i,
                "j": j,
                "forced_sign": sign,
                "u": u,
                "v": v,
                "closed": closed,
                "result": result,
                "numerical_margin": float(branch_margin),
                "certificate": None,
            }
            if reverse in edge_records:
                # Both opposite closed branches cannot be exactly infeasible in
                # a nonempty cell. Numerical ambiguity is discarded conservatively.
                if edge_records[reverse].get("certificate") is None:
                    del edge_records[reverse]
                stats["opposite_candidate_collisions"] += 1
                continue
            edge_records[(u, v)] = rec
            stats["numerical_forced_candidates"] += 1

            cycle = exactify_cycle(system, edge_records, stats)
            if cycle is not None:
                payload = []
                for item in cycle:
                    payload.append({
                        "root": item["root"],
                        "i": item["i"],
                        "j": item["j"],
                        "forced_sign": item["forced_sign"],
                        "shorter": list(item["u"]),
                        "longer": list(item["v"]),
                        "certificate": item["certificate"],
                    })
                return payload, None

    return None, "no_exact_forced_cycle"


def new_stats():
    return Counter({
        "base_lp": 0,
        "base_solver_failures": 0,
        "base_nonpositive_margin": 0,
        "opposite_branch_lp": 0,
        "branch_solver_failures": 0,
        "numerical_forced_candidates": 0,
        "opposite_candidate_collisions": 0,
        "exactification_attempts": 0,
        "exactification_misses": 0,
        "farkas_forced_zero": 0,
        "farkas_forced_negative": 0,
        "max_multiplier_denominator": 1,
    })


def scan(part, parts, output):
    assert parts > 0 and 0 <= part < parts
    endpoint = E.decode_endpoint()
    states = O.tri.collect_survivors()
    assert len(endpoint) == EXPECTED_SIZE
    assert len(states) == E.UNIVERSE_SIZE == 14174

    start = part * len(endpoint) // parts
    stop = (part + 1) * len(endpoint) // parts
    stats = new_stats()
    excluded = []
    graph = Counter()
    pattern = Counter()
    cycle_lengths = Counter()
    records = []
    unresolved = []

    for serial in range(start, stop):
        idx = endpoint[serial]
        state = states[idx]
        system = C.build_system(state)
        orders = C.orders_for_state(state)
        cycle, reason = certify_cell(system, state, orders, stats)
        if cycle is None:
            if reason != "no_exact_forced_cycle":
                unresolved.append({"serial": serial, "state_index": idx, "reason": reason})
            continue

        excluded.append(idx)
        graph[state[1]] += 1
        pat = "".join(map(str, state[5]))
        pattern[pat] += 1
        cycle_lengths[len(cycle)] += 1
        records.append({
            "serial": serial,
            "state_index": idx,
            "graph": state[1],
            "pattern": pat,
            "cycle_length": len(cycle),
            "cycle": cycle,
        })
        print(
            "EXCLUDE", serial, idx, state[1], pat,
            "cycle_length", len(cycle), flush=True,
        )

    payload = {
        "endpoint_size": EXPECTED_SIZE,
        "endpoint_sha256": EXPECTED_SHA256,
        "part": part,
        "parts": parts,
        "start": start,
        "stop": stop,
        "checked": stop - start,
        "excluded": excluded,
        "graph": dict(sorted(graph.items())),
        "patterns": dict(sorted(pattern.items())),
        "cycle_lengths": {str(k): v for k, v in sorted(cycle_lengths.items())},
        "stats": dict(stats),
        "unresolved": unresolved,
        "records": records,
    }
    Path(output).write_text(json.dumps(payload, sort_keys=True) + "\n")

    print("PASS scan")
    print("part", part, "parts", parts, "range", start, stop)
    print("checked", payload["checked"], "excluded", len(excluded))
    print("graph", payload["graph"])
    print("patterns", payload["patterns"])
    print("cycle_lengths", payload["cycle_lengths"])
    print("unresolved", len(unresolved))
    print("stats", payload["stats"])


def summarize(directory, output=None):
    files = sorted(Path(directory).glob("segment-cycle-*.json"))
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
    assert all(ranges[k][1] == ranges[k + 1][0] for k in range(len(ranges) - 1))

    excluded = []
    records = []
    unresolved = []
    graph = Counter()
    patterns = Counter()
    cycle_lengths = Counter()
    stats = Counter()
    for p in payloads:
        excluded.extend(p["excluded"])
        records.extend(p["records"])
        unresolved.extend(p["unresolved"])
        graph.update(p["graph"])
        patterns.update(p["patterns"])
        cycle_lengths.update({int(k): v for k, v in p["cycle_lengths"].items()})
        for key, value in p["stats"].items():
            if key == "max_multiplier_denominator":
                stats[key] = max(stats[key], value)
            else:
                stats[key] += value

    assert len(excluded) == len(set(excluded))
    summary = {
        "endpoint_size": EXPECTED_SIZE,
        "endpoint_sha256": EXPECTED_SHA256,
        "checked": sum(p["checked"] for p in payloads),
        "excluded_count": len(excluded),
        "survivor_count": EXPECTED_SIZE - len(excluded),
        "excluded": sorted(excluded),
        "graph": dict(sorted(graph.items())),
        "patterns": dict(sorted(patterns.items())),
        "cycle_lengths": {str(k): v for k, v in sorted(cycle_lengths.items())},
        "unresolved": unresolved,
        "stats": dict(stats),
        "records": sorted(records, key=lambda item: item["serial"]),
    }
    assert summary["checked"] == EXPECTED_SIZE
    if output:
        Path(output).write_text(json.dumps(summary, sort_keys=True) + "\n")

    print("PASS summary")
    for key in ("checked", "excluded_count", "survivor_count"):
        print(key, summary[key])
    print("graph", summary["graph"])
    print("patterns", summary["patterns"])
    print("cycle_lengths", summary["cycle_lengths"])
    print("unresolved", len(unresolved))
    print("stats", summary["stats"])


def main():
    parser = ArgumentParser()
    parser.add_argument("--part", type=int)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--output")
    parser.add_argument("--summary-dir")
    parser.add_argument("--summary-output")
    args = parser.parse_args()

    if args.summary_dir:
        summarize(args.summary_dir, args.summary_output)
        return
    if args.part is None or args.parts is None or not args.output:
        parser.error("scan mode requires --part, --parts, and --output")
    scan(args.part, args.parts, args.output)


if __name__ == "__main__":
    main()
