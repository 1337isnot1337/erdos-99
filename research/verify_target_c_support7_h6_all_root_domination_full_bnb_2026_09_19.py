#!/usr/bin/env python3
"""Exact full branch-and-bound for the 14 H6 interior-domination disjunctions.

For every cell in the frozen 3,874-cell generic-H6 endpoint, every genuine
metric realization satisfies fourteen two-way affine disjunctions.  This
verifier searches their full joint cover without blindly enumerating all
2^14 leaves.

A node consists of a set of chosen closed domination halfspaces.  Numerical
LPs are used only to discover promising primal points or sparse dual supports.
Every terminal claim is exact:

* LIVE: an exact rational point satisfies the complete 85-variable affine
  system, every original strict facet, and one selected branch of all fourteen
  domination disjunctions;
* DEAD: exact rational Farkas certificates cover both children of every branch
  reached below the node;
* UNRESOLVED: the numerical solver failed, exact reconstruction failed, or an
  optional node budget was exhausted.

The search uses a lazy full-witness shortcut.  At any numerically feasible
node, its LP point is tested against every unassigned disjunction.  If at least
one branch of every disjunction is numerically satisfied, the better branch of
each pair is added and the same point is reconstructed exactly.  A successful
reconstruction proves LIVE immediately.  Otherwise the most violated remaining
disjunction is branched first.

This is a proof search, not a floating-point certificate.  Numerical outcomes
never by themselves exclude or retain a cell.
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
P = load(
    "h6_rootdom_depth1_primal",
    "verify_target_c_support7_h6_all_root_domination_depth1_primal_2026_09_19.py",
)
E = load(
    "h6_endpoint_3874",
    "target_c_support7_h6_endpoint_3874_ledger_2026_09_19.py",
)
O = D.O
A = D.A
C = D.C
NVAR = D.NVAR

# Put the two targets at each hull root next to each other.  If a cell needs
# branching, this reaches the already-motivated same-root coupled layer early.
CLAUSE_KEYS = tuple(
    (root, target)
    for root in range(6)
    for target in (6, 7)
) + ((6, 7), (7, 6))
assert len(CLAUSE_KEYS) == 14 == len(set(CLAUSE_KEYS))


def make_clauses(state, orders):
    clauses = []
    for root, target in CLAUSE_KEYS:
        a, b = D.bracketing_hull_edge(orders, root, target)
        branches = (
            (a, D.domination_branch(state, orders, root, target, a)),
            (b, D.domination_branch(state, orders, root, target, b)),
        )
        clauses.append({
            "root": root,
            "target": target,
            "edge": [a, b],
            "branches": branches,
        })
    return tuple(clauses)


def float_slack(closed, numeric):
    # Every domination branch currently contains one closed affine inequality.
    # Keep this generic in case the branch representation later acquires more.
    return min(
        float(const) + sum(float(a) * float(x) for a, x in zip(row, numeric) if a)
        for row, const, _ in closed
    )


def exact_farkas_summary(cert):
    value, denominator = cert
    return {
        "forced_num": value.numerator,
        "forced_den": value.denominator,
        "max_multiplier_denominator": denominator,
    }


def update_primal_stats(stats, witness):
    stats["exact_primal"] += 1
    stats["max_primal_denominator"] = max(
        stats["max_primal_denominator"], witness["max_denominator"]
    )
    stats["primal_limit_counts"][witness["limit"]] += 1
    strict = F(witness["min_strict_num"], witness["min_strict_den"])
    current = stats["min_positive_strict"]
    if current is None or strict < current:
        stats["min_positive_strict"] = strict
    if witness["min_closed_num"] == 0:
        stats["zero_closed_primal"] += 1


def exact_dead_node(system, closed, result, stats):
    cert = A.exactify_support(system, closed, result)
    if cert is None:
        stats["exact_farkas_failures"] += 1
        return None
    stats["exact_farkas"] += 1
    stats["max_farkas_denominator"] = max(
        stats["max_farkas_denominator"], cert[1]
    )
    if cert[0] == 0:
        stats["farkas_forced_zero"] += 1
    else:
        stats["farkas_forced_negative"] += 1
    return exact_farkas_summary(cert)


def numerical_node(system, closed, stats):
    margin, result = O.numerical_candidate(system, closed)
    stats["node_lp"] += 1
    if margin is None:
        stats["solver_failures"] += 1
        return "unresolved", None, None
    if margin <= 1e-8:
        cert = exact_dead_node(system, closed, result, stats)
        if cert is not None:
            return "dead", cert, margin
    return "open", result, margin


def chosen_branches_payload(clauses, choices):
    return [
        {
            "root": clauses[i]["root"],
            "target": clauses[i]["target"],
            "endpoint": clauses[i]["branches"][choice][0],
        }
        for i, choice in sorted(choices.items())
    ]


def certify_cell(system, state, orders, node_limit, stats):
    clauses = make_clauses(state, orders)
    memo = {}

    def search(choices, result_hint=None, margin_hint=None):
        if stats["nodes"] >= node_limit:
            stats["node_limit_hits"] += 1
            return {"status": "unresolved", "reason": "node_limit"}
        stats["nodes"] += 1
        stats["max_depth"] = max(stats["max_depth"], len(choices))

        key = tuple(sorted(choices.items()))
        if key in memo:
            stats["memo_hits"] += 1
            return memo[key]

        closed = tuple(
            inequality
            for clause_index, choice in sorted(choices.items())
            for inequality in clauses[clause_index]["branches"][choice][1]
        )

        if result_hint is None:
            node_status, payload, margin = numerical_node(system, closed, stats)
            if node_status == "dead":
                out = {
                    "status": "dead",
                    "depth": len(choices),
                    "certificate": payload,
                }
                memo[key] = out
                return out
            if node_status == "unresolved":
                out = {"status": "unresolved", "reason": "solver_failure"}
                memo[key] = out
                return out
            result = payload
        else:
            result = result_hint
            margin = margin_hint

        numeric = result.x[:NVAR]
        remaining = [i for i in range(len(clauses)) if i not in choices]

        # If the current LP point already satisfies at least one side of every
        # remaining disjunction, try to turn it into one exact full witness.
        suggested = dict(choices)
        violated = []
        for i in remaining:
            slacks = tuple(
                float_slack(branch_closed, numeric)
                for _, branch_closed in clauses[i]["branches"]
            )
            best = 0 if slacks[0] >= slacks[1] else 1
            if slacks[best] >= -1e-9:
                suggested[i] = best
            else:
                violated.append((slacks[best], i, slacks))

        if not violated:
            full_closed = tuple(
                inequality
                for clause_index, choice in sorted(suggested.items())
                for inequality in clauses[clause_index]["branches"][choice][1]
            )
            stats["full_witness_attempts"] += 1
            witness = P.exactify_primal(system, full_closed, result)
            if witness is not None:
                stats["full_witness_successes"] += 1
                update_primal_stats(stats, witness)
                out = {
                    "status": "live",
                    "depth": len(choices),
                    "choices": chosen_branches_payload(clauses, suggested),
                    "witness": witness,
                }
                memo[key] = out
                return out
            stats["exact_primal_failures"] += 1

        if not remaining:
            # We can reach a leaf only when exact reconstruction of the
            # numerically open leaf failed.  It is not safe to call it live.
            out = {
                "status": "unresolved",
                "reason": "leaf_primal_exactification_failure",
                "margin": float(margin),
            }
            memo[key] = out
            return out

        # Branch first on the disjunction most strongly violated by the current
        # LP point.  If none is violated (the full-witness exactification failed),
        # use the smallest best-branch slack as the next clause.
        if violated:
            _, branch_i, branch_slacks = min(violated, key=lambda item: item[0])
        else:
            candidates = []
            for i in remaining:
                slacks = tuple(
                    float_slack(branch_closed, numeric)
                    for _, branch_closed in clauses[i]["branches"]
                )
                candidates.append((max(slacks), i, slacks))
            _, branch_i, branch_slacks = min(candidates, key=lambda item: item[0])

        # Try the branch with larger current slack first, because one exact live
        # leaf proves the whole cell survives the domination cover.
        order = (0, 1) if branch_slacks[0] >= branch_slacks[1] else (1, 0)
        children = []
        saw_unresolved = False
        for choice in order:
            child_choices = dict(choices)
            child_choices[branch_i] = choice
            child_closed = closed + clauses[branch_i]["branches"][choice][1]
            child_status, child_payload, child_margin = numerical_node(
                system, child_closed, stats
            )
            if child_status == "dead":
                child = {
                    "status": "dead",
                    "depth": len(child_choices),
                    "branch": {
                        "root": clauses[branch_i]["root"],
                        "target": clauses[branch_i]["target"],
                        "endpoint": clauses[branch_i]["branches"][choice][0],
                    },
                    "certificate": child_payload,
                }
            elif child_status == "unresolved":
                child = {"status": "unresolved", "reason": "solver_failure"}
            else:
                child = search(child_choices, child_payload, child_margin)

            children.append(child)
            if child["status"] == "live":
                memo[key] = child
                return child
            if child["status"] == "unresolved":
                saw_unresolved = True

        if saw_unresolved:
            out = {
                "status": "unresolved",
                "reason": "incomplete_branch_cover",
                "branch_clause": {
                    "root": clauses[branch_i]["root"],
                    "target": clauses[branch_i]["target"],
                    "edge": clauses[branch_i]["edge"],
                },
                "children": children,
            }
        else:
            assert all(child["status"] == "dead" for child in children)
            out = {
                "status": "dead",
                "depth": len(choices),
                "branch_clause": {
                    "root": clauses[branch_i]["root"],
                    "target": clauses[branch_i]["target"],
                    "edge": clauses[branch_i]["edge"],
                },
                "children": children,
            }
        memo[key] = out
        return out

    return search({})


def new_stats():
    return {
        "nodes": 0,
        "node_lp": 0,
        "memo_hits": 0,
        "max_depth": 0,
        "full_witness_attempts": 0,
        "full_witness_successes": 0,
        "exact_primal": 0,
        "exact_primal_failures": 0,
        "solver_failures": 0,
        "exact_farkas": 0,
        "exact_farkas_failures": 0,
        "max_primal_denominator": 1,
        "max_farkas_denominator": 1,
        "primal_limit_counts": Counter(),
        "min_positive_strict": None,
        "zero_closed_primal": 0,
        "farkas_forced_zero": 0,
        "farkas_forced_negative": 0,
        "node_limit_hits": 0,
    }


def add_stats(total, cell):
    for key in (
        "nodes", "node_lp", "memo_hits", "full_witness_attempts",
        "full_witness_successes", "exact_primal", "exact_primal_failures",
        "solver_failures", "exact_farkas", "exact_farkas_failures",
        "zero_closed_primal", "farkas_forced_zero", "farkas_forced_negative",
        "node_limit_hits",
    ):
        total[key] += cell[key]
    total["max_depth"] = max(total["max_depth"], cell["max_depth"])
    total["max_primal_denominator"] = max(
        total["max_primal_denominator"], cell["max_primal_denominator"]
    )
    total["max_farkas_denominator"] = max(
        total["max_farkas_denominator"], cell["max_farkas_denominator"]
    )
    total["primal_limit_counts"].update(cell["primal_limit_counts"])
    s = cell["min_positive_strict"]
    if s is not None:
        current = total["min_positive_strict"]
        if current is None or s < current:
            total["min_positive_strict"] = s


def serializable_stats(stats):
    out = dict(stats)
    out["primal_limit_counts"] = {
        str(k): v for k, v in sorted(stats["primal_limit_counts"].items())
    }
    s = stats["min_positive_strict"]
    out["min_positive_strict"] = None if s is None else [s.numerator, s.denominator]
    return out


def scan(part, parts, output, node_limit):
    assert parts > 0 and 0 <= part < parts
    assert node_limit > 0
    endpoint = E.decode_endpoint()
    states = O.tri.collect_survivors()
    assert len(endpoint) == E.ENDPOINT_SIZE == 3874
    assert len(states) == E.UNIVERSE_SIZE == 14174

    start = part * len(endpoint) // parts
    stop = (part + 1) * len(endpoint) // parts
    total = new_stats()
    live = []
    dead = []
    unresolved = []
    live_graph = Counter()
    dead_graph = Counter()
    unresolved_graph = Counter()
    live_pattern = Counter()
    dead_pattern = Counter()
    unresolved_pattern = Counter()

    for serial in range(start, stop):
        idx = endpoint[serial]
        state = states[idx]
        system = C.build_system(state)
        orders = C.orders_for_state(state)
        cell_stats = new_stats()
        result = certify_cell(system, state, orders, node_limit, cell_stats)
        add_stats(total, cell_stats)

        pat = "".join(map(str, state[5]))
        record = {
            "serial": serial,
            "state_index": idx,
            "graph": state[1],
            "pattern": pat,
            "result": result,
            "stats": serializable_stats(cell_stats),
        }
        if result["status"] == "live":
            live.append(record)
            live_graph[state[1]] += 1
            live_pattern[pat] += 1
        elif result["status"] == "dead":
            dead.append(record)
            dead_graph[state[1]] += 1
            dead_pattern[pat] += 1
            print("EXCLUDED", serial, idx, state[1], pat, flush=True)
        else:
            unresolved.append(record)
            unresolved_graph[state[1]] += 1
            unresolved_pattern[pat] += 1
            print("UNRESOLVED", serial, idx, result.get("reason"), flush=True)

        if (serial - start + 1) % 25 == 0:
            print(
                "PROGRESS", serial + 1,
                "live", len(live), "dead", len(dead),
                "unresolved", len(unresolved), "nodes", total["nodes"],
                flush=True,
            )

    payload = {
        "endpoint_sha256": E.INDEX_SHA256,
        "part": part,
        "parts": parts,
        "start": start,
        "stop": stop,
        "node_limit": node_limit,
        "checked_cells": stop - start,
        "live_cells": len(live),
        "dead_cells": len(dead),
        "unresolved_cells": len(unresolved),
        "live_graph": dict(sorted(live_graph.items())),
        "dead_graph": dict(sorted(dead_graph.items())),
        "unresolved_graph": dict(sorted(unresolved_graph.items())),
        "live_pattern": dict(sorted(live_pattern.items())),
        "dead_pattern": dict(sorted(dead_pattern.items())),
        "unresolved_pattern": dict(sorted(unresolved_pattern.items())),
        "stats": serializable_stats(total),
        "live": live,
        "dead": dead,
        "unresolved": unresolved,
    }
    Path(output).write_text(json.dumps(payload, sort_keys=True) + "\n")

    print("PASS scan")
    print("range", start, stop)
    print("live_cells", len(live))
    print("dead_cells", len(dead))
    print("unresolved_cells", len(unresolved))
    print("stats", json.dumps(payload["stats"], sort_keys=True))


def summarize(directory, output=None):
    files = sorted(Path(directory).glob("full-bnb-*.json"))
    assert files
    payloads = [json.loads(path.read_text()) for path in files]
    parts_set = {p["parts"] for p in payloads}
    assert len(parts_set) == 1
    parts = parts_set.pop()
    assert len(payloads) == parts
    assert {p["part"] for p in payloads} == set(range(parts))
    assert all(p["endpoint_sha256"] == E.INDEX_SHA256 for p in payloads)
    ranges = sorted((p["start"], p["stop"]) for p in payloads)
    assert ranges[0][0] == 0 and ranges[-1][1] == E.ENDPOINT_SIZE
    assert all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))

    live = [x for p in payloads for x in p["live"]]
    dead = [x for p in payloads for x in p["dead"]]
    unresolved = [x for p in payloads for x in p["unresolved"]]
    assert len(live) + len(dead) + len(unresolved) == E.ENDPOINT_SIZE
    assert len({x["state_index"] for x in live + dead + unresolved}) == E.ENDPOINT_SIZE

    states = O.tri.collect_survivors()
    dead_idx = {x["state_index"] for x in dead}
    survivors = set(E.decode_endpoint()) - dead_idx
    graph_survivors = Counter(states[i][1] for i in survivors)
    pattern_survivors = Counter("".join(map(str, states[i][5])) for i in survivors)

    total = new_stats()
    for payload in payloads:
        s = payload["stats"]
        temp = new_stats()
        for key in temp:
            if key == "primal_limit_counts":
                temp[key] = Counter({int(k): v for k, v in s[key].items()})
            elif key == "min_positive_strict":
                temp[key] = None if s[key] is None else F(*s[key])
            else:
                temp[key] = s[key]
        add_stats(total, temp)

    summary = {
        "endpoint_size": E.ENDPOINT_SIZE,
        "endpoint_sha256": E.INDEX_SHA256,
        "live_cells": len(live),
        "dead_cells": len(dead),
        "unresolved_cells": len(unresolved),
        "survivors_after_exact_exclusions": len(survivors),
        "graph_survivors": dict(sorted(graph_survivors.items())),
        "pattern_survivors": dict(sorted(pattern_survivors.items())),
        "dead_indices": sorted(dead_idx),
        "survivor_indices": sorted(survivors),
        "stats": serializable_stats(total),
    }
    if output:
        Path(output).write_text(json.dumps(summary, sort_keys=True) + "\n")

    print("PASS summary")
    for key in (
        "endpoint_size", "live_cells", "dead_cells", "unresolved_cells",
        "survivors_after_exact_exclusions",
    ):
        print(key, summary[key])
    print("graph_survivors", summary["graph_survivors"])
    print("pattern_survivors", summary["pattern_survivors"])
    print("stats", json.dumps(summary["stats"], sort_keys=True))


def main():
    parser = ArgumentParser()
    parser.add_argument("--part", type=int)
    parser.add_argument("--parts", type=int)
    parser.add_argument("--output")
    parser.add_argument("--summary-dir")
    parser.add_argument("--summary-output")
    parser.add_argument("--node-limit", type=int, default=200_000)
    args = parser.parse_args()

    if args.summary_dir:
        assert args.part is None and args.parts is None
        summarize(args.summary_dir, args.summary_output)
        return

    assert args.part is not None and args.parts is not None and args.output
    scan(args.part, args.parts, args.output, args.node_limit)


if __name__ == "__main__":
    main()
