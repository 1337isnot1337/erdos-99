#!/usr/bin/env python3
"""Temporary state-level audit of generic-H6 reflection closure."""

from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


E3 = load(
    "h6_two_face_23_extension3_audit",
    "verify_target_c_support7_h6_two_face_23_extension3_2026_09_19.py",
)
E2 = E3.E2
E = E2.E
T = E.T
A = T.A
O = T.O
tri = O.tri
base = tri.base

R = {0: 0, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 6, 7: 7}


def edge(a, b):
    return (a, b) if a < b else (b, a)


def state_key(state):
    _, graph, missing, raws, chi, pattern, signs = state
    return (
        graph,
        tuple(sorted(missing)),
        tuple(tuple(row) for row in raws),
        tuple(sorted(chi.items())),
        tuple(pattern),
        tuple(sorted(signs.items())),
    )


def reflect_state_key(state):
    _, graph, missing, raws, chi, _, signs = state

    new_missing = frozenset(edge(R[a], R[b]) for a, b in missing)

    new_raws = [None] * 6
    for h in range(6):
        new_raws[R[h]] = tuple(R[v] for v in reversed(raws[h]))
    new_raws = tuple(new_raws)

    new_chi = {}
    for i, j, k in combinations(range(8), 3):
        new_chi[(i, j, k)] = -base.chi_value(chi, R[i], R[j], R[k])

    new_signs = {
        edge(R[a], R[b]): sign
        for (a, b), sign in signs.items()
    }
    new_pattern = tuple(
        pos
        for pos, v in enumerate(new_raws[0], 1)
        if new_signs[edge(0, v)] > 0
    )
    assert len(new_pattern) == 3

    transformed = (
        None,
        graph,
        new_missing,
        new_raws,
        new_chi,
        new_pattern,
        new_signs,
    )
    return state_key(transformed)


def pat(state):
    return "".join(map(str, state[5]))


def main():
    print("rebuilding 14,174 generic-H6 states", flush=True)
    states = tri.collect_survivors()
    assert len(states) == 14174

    keys = [state_key(st) for st in states]
    key_to_idx = {key: i for i, key in enumerate(keys)}
    assert len(key_to_idx) == len(states)

    print("constructing exact reflection involution", flush=True)
    reflection = []
    for i, st in enumerate(states):
        reflected_key = reflect_state_key(st)
        assert reflected_key in key_to_idx, (i, st[1], pat(st))
        reflection.append(key_to_idx[reflected_key])
    assert all(reflection[reflection[i]] == i for i in range(len(states)))

    expected_pattern_map = {
        "145": "347", "347": "145",
        "156": "237", "237": "156",
        "235": "356", "356": "235",
        "236": "256", "256": "236",
        "245": "346", "346": "245",
        "345": "345",
    }
    for i, j in enumerate(reflection):
        assert states[i][1] == states[j][1]
        assert pat(states[j]) == expected_pattern_map[pat(states[i])]

    print("rebuilding 5,692 complete-angle endpoint", flush=True)
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692
    q_of_idx = {idx: q for q, idx in enumerate(previous)}
    assert len(q_of_idx) == 5692

    previous_set = set(previous)
    complete_missing_images = [i for i in previous if reflection[i] not in previous_set]
    print("complete-angle reflection misses:", len(complete_missing_images), flush=True)

    print("rebuilding 716-cell order-hull exclusion", flush=True)
    order_dead_q = set()
    for q, idx in enumerate(previous):
        system = O.C.build_system(states[idx])
        if not A.survives_previous_order_hull(system):
            order_dead_q.add(q)
        if q and q % 500 == 0:
            print("order scan", q, "dead", len(order_dead_q), flush=True)
    assert len(order_dead_q) == 716

    one_face_dead_q = {q for q, _, _, _ in A.CANDIDATES}
    first_two_dead_q = {q for q, _, _, _, _ in T.CANDIDATES}
    ext1_dead_q = {q for q, _, _, _, _, _ in E.CANDIDATES}
    ext2_dead_q = {q for q, _, _, _, _, _ in E2.CANDIDATES}
    ext3_dead_q = {q for q, _, _, _, _, _ in E3.CANDIDATES}

    assert [len(s) for s in (
        one_face_dead_q, first_two_dead_q, ext1_dead_q, ext2_dead_q, ext3_dead_q
    )] == [32, 34, 39, 30, 36]

    all_dead_q = (
        order_dead_q
        | one_face_dead_q
        | first_two_dead_q
        | ext1_dead_q
        | ext2_dead_q
        | ext3_dead_q
    )
    assert len(all_dead_q) == 887
    current = [idx for q, idx in enumerate(previous) if q not in all_dead_q]
    assert len(current) == 4805
    current_set = set(current)

    current_graph = Counter(states[i][1] for i in current)
    current_pattern = Counter(pat(states[i]) for i in current)
    assert current_graph == Counter({"C7": 3823, "C3+C4": 982})
    assert current_pattern == Counter({
        "145": 4, "156": 16, "235": 654, "236": 1278,
        "237": 16, "245": 474, "256": 1204, "345": 21,
        "346": 479, "347": 4, "356": 655,
    })

    closed = [i for i in current if reflection[i] in current_set]
    closed_set = set(closed)
    assert all(reflection[i] in closed_set for i in closed)
    added_exclusions = len(current) - len(closed)

    closed_graph = Counter(states[i][1] for i in closed)
    closed_pattern = Counter(pat(states[i]) for i in closed)
    closed_graph_pattern = Counter((states[i][1], pat(states[i])) for i in closed)

    print("RESULT exact current survivors:", len(current), flush=True)
    print("RESULT exact reflection-closed survivors:", len(closed), flush=True)
    print("RESULT additional exclusions:", added_exclusions, flush=True)
    print("RESULT closed graph:", dict(sorted(closed_graph.items())), flush=True)
    print("RESULT closed pattern:", dict(sorted(closed_pattern.items())), flush=True)
    print("RESULT closed graph-pattern:", dict(sorted(closed_graph_pattern.items())), flush=True)

    base4944_dead_q = order_dead_q | one_face_dead_q
    base4944 = [idx for q, idx in enumerate(previous) if q not in base4944_dead_q]
    assert len(base4944) == 4944
    base4944_set = set(base4944)
    base4944_reflection_misses = [i for i in base4944 if reflection[i] not in base4944_set]
    print("4944 endpoint reflection misses:", len(base4944_reflection_misses), flush=True)

    recent_dead_q = first_two_dead_q | ext1_dead_q | ext2_dead_q | ext3_dead_q
    assert len(recent_dead_q) == 139
    recent_dead_idx = {previous[q] for q in recent_dead_q}
    recent_closure_idx = recent_dead_idx | {reflection[i] for i in recent_dead_idx}
    recent_closure_in_4944 = recent_closure_idx & base4944_set
    print("recent 139 reflected union inside 4944:", len(recent_closure_in_4944), flush=True)
    print("recent reflected additional inside 4944:", len(recent_closure_in_4944) - 139, flush=True)


if __name__ == "__main__":
    main()
