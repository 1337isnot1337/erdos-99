#!/usr/bin/env python3
"""Exact certificate for 34 additional generic-H6 cells using two faces.

Starting point: the committed 4,944-cell generic support-seven H6 endpoint after
the exact one-face adaptive-branch reduction.

For each listed cell, two physical pentagon faces are selected. Each face has
20 closed local branches: ten admissible cyclic gap orders times the low/high
median side, with the exact branch-adaptive closure secants already certified
by verify_target_c_pentagon_branch_adaptive_secants_2026_09_19.py.

A pair of local branches is covered if either constituent branch already has an
exact one-face Farkas contradiction, or their combined closed facets have an
exact two-face Farkas contradiction. A cell is excluded only after all 20*20
branch pairs are covered.

Floating-point LPs are used only to propose dual supports. Acceptance uses the
exact Fraction checker from the committed one-face adaptive verifier.
"""

from collections import Counter
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


A = load(
    "h6_adaptive",
    "verify_target_c_support7_h6_adaptive_branch_reduction_2026_09_19.py",
)
O = A.O

BRANCH_KEYS = tuple(
    (order, side)
    for order in A.STRICT_ORDERS
    for side in ("low", "high")
)
assert len(BRANCH_KEYS) == 20

# q indexes the committed 5,692-cell complete-angle endpoint. expected_idx is
# the corresponding index in the 14,174-cell generic-H6 state list.
CANDIDATES = (
    (6, 15, (2, 7), "C7", "245"),
    (7, 16, (2, 3), "C7", "256"),
    (8, 19, (2, 7), "C7", "356"),
    (11, 23, (2, 3), "C7", "256"),
    (13, 25, (2, 6), "C3+C4", "345"),
    (18, 36, (2, 7), "C3+C4", "245"),
    (20, 44, (2, 7), "C3+C4", "245"),
    (22, 50, (2, 6), "C3+C4", "245"),
    (27, 58, (2, 6), "C3+C4", "245"),
    (28, 62, (2, 6), "C7", "356"),
    (31, 66, (2, 3), "C7", "256"),
    (33, 68, (2, 7), "C3+C4", "345"),
    (34, 73, (2, 6), "C7", "245"),
    (35, 74, (2, 3), "C7", "256"),
    (47, 102, (2, 3), "C7", "256"),
    (53, 114, (2, 3), "C7", "256"),
    (61, 139, (2, 4), "C7", "256"),
    (65, 145, (2, 3), "C7", "256"),
    (66, 147, (2, 7), "C3+C4", "245"),
    (73, 155, (2, 3), "C7", "256"),
    (84, 174, (2, 4), "C7", "256"),
    (89, 182, (2, 3), "C7", "356"),
    (92, 185, (2, 3), "C7", "256"),
    (98, 196, (2, 3), "C7", "256"),
    (105, 207, (2, 7), "C7", "256"),
    (108, 217, (2, 7), "C7", "256"),
    (111, 230, (2, 7), "C7", "256"),
    (118, 253, (2, 3), "C7", "256"),
    (119, 254, (2, 3), "C3+C4", "346"),
    (122, 260, (2, 7), "C7", "256"),
    (129, 278, (2, 7), "C7", "235"),
    (130, 279, (2, 3), "C7", "256"),
    (131, 282, (2, 3), "C7", "356"),
    (135, 287, (2, 3), "C7", "256"),
)


def record_certificate(cert, forced, denominators):
    value, denominator = cert
    forced["zero" if value == 0 else "negative"] += 1
    denominators.append(denominator)


def main():
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692

    first_dead = {q for q, _, _, _ in A.CANDIDATES}
    assert len(first_dead) == 32
    assert len(CANDIDATES) == len({q for q, _, _, _, _ in CANDIDATES}) == 34
    assert all(q not in first_dead for q, _, _, _, _ in CANDIDATES)

    graph = Counter()
    pattern = Counter()
    pairs = Counter()
    forced = Counter()
    denominators = [1]
    one_face_certificates = 0
    two_face_certificates = 0

    for q, expected_idx, face_pair, expected_graph, expected_pattern in CANDIDATES:
        idx = previous[q]
        assert idx == expected_idx
        st = states[idx]
        assert st[1] == expected_graph
        pat = "".join(map(str, st[5]))
        assert pat == expected_pattern
        system = O.C.build_system(st)

        # These cells must survive the previous 716-cell order-hull reduction;
        # q not in first_dead above then places them in the 4,944-cell endpoint.
        assert A.survives_previous_order_hull(system)

        a, b = face_pair
        exact_dead = {}
        for face in (a, b):
            dead = set()
            for branch_index, (order, side) in enumerate(BRANCH_KEYS):
                closed = A.BRANCH[(face, order, side)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                if margin <= 1e-8:
                    cert = A.exactify_support(system, closed, result)
                    if cert is not None:
                        dead.add(branch_index)
                        record_certificate(cert, forced, denominators)
                        one_face_certificates += 1
            exact_dead[face] = dead

        covered = 0
        for ia, (oa, sa) in enumerate(BRANCH_KEYS):
            for ib, (ob, sb) in enumerate(BRANCH_KEYS):
                if ia in exact_dead[a] or ib in exact_dead[b]:
                    covered += 1
                    continue

                closed = A.BRANCH[(a, oa, sa)] + A.BRANCH[(b, ob, sb)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                assert margin <= 1e-8
                cert = A.exactify_support(system, closed, result)
                assert cert is not None
                record_certificate(cert, forced, denominators)
                two_face_certificates += 1
                covered += 1

        assert covered == 400
        graph[st[1]] += 1
        pattern[pat] += 1
        pairs[face_pair] += 1

    assert graph == Counter({"C7": 26, "C3+C4": 8})
    assert pattern == Counter({
        "235": 1,
        "245": 7,
        "256": 19,
        "345": 2,
        "346": 1,
        "356": 4,
    })
    assert pairs == Counter({(2, 3): 16, (2, 7): 11, (2, 6): 5, (2, 4): 2})
    assert one_face_certificates == 929
    assert two_face_certificates == 1562
    assert one_face_certificates + two_face_certificates == 2491
    assert forced == Counter({"negative": 2390, "zero": 101})
    assert max(denominators) == 3575688275930909083760258

    remaining_graph = Counter({"C7": 3940, "C3+C4": 1004}) - graph
    assert remaining_graph == Counter({"C7": 3914, "C3+C4": 996})

    remaining_pattern = Counter({
        "145": 4,
        "156": 16,
        "235": 674,
        "236": 1282,
        "237": 16,
        "245": 484,
        "256": 1282,
        "345": 24,
        "346": 484,
        "347": 4,
        "356": 674,
    }) - pattern
    assert remaining_pattern == Counter({
        "145": 4,
        "156": 16,
        "235": 673,
        "236": 1282,
        "237": 16,
        "245": 477,
        "256": 1263,
        "345": 22,
        "346": 483,
        "347": 4,
        "356": 670,
    })
    assert sum(remaining_pattern.values()) == 4910

    print("PASS")
    print("previous generic H6 endpoint: 4944 = 3940 C7 + 1004 C3+C4")
    print("new exact two-face exclusions: 34 = 26 C7 + 8 C3+C4")
    print("exact one-face branch certificates used:", one_face_certificates)
    print("exact two-face branch certificates used:", two_face_certificates)
    print("certificate forced values:", dict(forced))
    print("maximum exact dual denominator:", max(denominators))
    print("remaining certified endpoint: 4910 = 3914 C7 + 996 C3+C4")
    print("excluded by ground pattern:", dict(sorted(pattern.items())))
    print("witness face-pair counts:", {f"{a}-{b}": n for (a, b), n in sorted(pairs.items())})


if __name__ == "__main__":
    main()
