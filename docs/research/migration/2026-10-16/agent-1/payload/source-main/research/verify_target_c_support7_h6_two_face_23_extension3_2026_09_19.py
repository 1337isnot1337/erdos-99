#!/usr/bin/env python3
"""Exact certificate for 36 further generic-H6 cells using physical faces 2 and 3.

Starting point: the committed 4,841-cell generic support-seven H6 endpoint.
For each listed cell, all 20*20 products of the exact local gap-order/median
branches at physical faces 2 and 3 are covered by exact rational Farkas
contradictions. Floating-point LPs only propose supports; every accepted
exclusion is rechecked coefficientwise over fractions.Fraction by the committed
adaptive-branch checker.
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

E2 = load(
    "h6_two_face_23_extension2",
    "verify_target_c_support7_h6_two_face_23_extension2_2026_09_19.py",
)
E = E2.E
T = E2.T
A = T.A
O = T.O
BRANCH_KEYS = T.BRANCH_KEYS

# q indexes the 5,692-cell complete-angle endpoint. expected_idx indexes the
# 14,174-cell generic-H6 state list. live2/live3 are the exact locally feasible
# branch counts before the two-face product contradictions are imposed.
CANDIDATES = (
    (530, 1160, "C7", "235", 14, 8),
    (533, 1163, "C3+C4", "235", 14, 8),
    (538, 1172, "C7", "256", 5, 7),
    (545, 1185, "C7", "235", 6, 7),
    (546, 1186, "C7", "256", 5, 7),
    (568, 1223, "C7", "256", 1, 6),
    (579, 1241, "C7", "256", 6, 6),
    (584, 1248, "C7", "256", 6, 7),
    (596, 1267, "C7", "256", 1, 6),
    (606, 1293, "C7", "256", 6, 7),
    (615, 1309, "C7", "256", 6, 6),
    (622, 1323, "C7", "256", 6, 7),
    (626, 1332, "C7", "256", 1, 5),
    (644, 1372, "C3+C4", "245", 1, 4),
    (649, 1381, "C3+C4", "245", 1, 4),
    (663, 1412, "C7", "256", 1, 5),
    (666, 1417, "C7", "256", 5, 10),
    (668, 1429, "C3+C4", "245", 1, 4),
    (674, 1459, "C7", "256", 1, 7),
    (680, 1471, "C7", "256", 1, 7),
    (709, 1529, "C7", "256", 6, 10),
    (720, 1554, "C7", "256", 6, 10),
    (724, 1561, "C7", "346", 7, 8),
    (730, 1570, "C7", "256", 2, 6),
    (741, 1595, "C7", "256", 4, 6),
    (752, 1616, "C7", "236", 14, 8),
    (753, 1617, "C7", "256", 2, 6),
    (757, 1622, "C7", "256", 2, 6),
    (765, 1630, "C7", "256", 4, 6),
    (766, 1632, "C7", "236", 9, 8),
    (771, 1637, "C3+C4", "235", 1, 4),
    (773, 1639, "C7", "256", 5, 10),
    (776, 1642, "C3+C4", "356", 6, 4),
    (798, 1690, "C7", "256", 6, 10),
    (805, 1705, "C7", "256", 6, 10),
    (816, 1728, "C7", "235", 14, 4),
)

def main():
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692

    old = (
        {q for q, _, _, _ in A.CANDIDATES}
        | {q for q, _, _, _, _ in T.CANDIDATES}
        | {q for q, _, _, _, _, _ in E.CANDIDATES}
        | {q for q, _, _, _, _, _ in E2.CANDIDATES}
    )
    new_q = {q for q, _, _, _, _, _ in CANDIDATES}
    assert len(old) == 135
    assert len(CANDIDATES) == len(new_q) == 36
    assert new_q.isdisjoint(old)

    graph = Counter()
    pattern = Counter()
    forced = Counter()
    denominators = [1]
    one_face_certificates = 0
    two_face_certificates = 0

    for q, expected_idx, expected_graph, expected_pattern, expected_live2, expected_live3 in CANDIDATES:
        idx = previous[q]
        assert idx == expected_idx
        st = states[idx]
        assert st[1] == expected_graph
        pat = "".join(map(str, st[5]))
        assert pat == expected_pattern
        system = O.C.build_system(st)
        assert A.survives_previous_order_hull(system)

        live = {}
        for face in (2, 3):
            live_here = set()
            for branch_index, (order, side) in enumerate(BRANCH_KEYS):
                closed = A.BRANCH[(face, order, side)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                if margin <= 1e-8:
                    cert = A.exactify_support(system, closed, result)
                    assert cert is not None
                    T.record_certificate(cert, forced, denominators)
                    one_face_certificates += 1
                else:
                    live_here.add(branch_index)
            live[face] = live_here

        assert len(live[2]) == expected_live2
        assert len(live[3]) == expected_live3

        pair_count = 0
        for i2 in sorted(live[2]):
            o2, s2 = BRANCH_KEYS[i2]
            for i3 in sorted(live[3]):
                o3, s3 = BRANCH_KEYS[i3]
                closed = A.BRANCH[(2, o2, s2)] + A.BRANCH[(3, o3, s3)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                assert margin <= 1e-8
                cert = A.exactify_support(system, closed, result)
                assert cert is not None
                T.record_certificate(cert, forced, denominators)
                two_face_certificates += 1
                pair_count += 1
        assert pair_count == expected_live2 * expected_live3

        graph[st[1]] += 1
        pattern[pat] += 1

    assert graph == Counter({"C7": 30, "C3+C4": 6})
    assert pattern == Counter({
        "235": 5, "236": 2, "245": 3,
        "256": 24, "346": 1, "356": 1,
    })

    remaining_graph = Counter({"C7": 3853, "C3+C4": 988}) - graph
    assert remaining_graph == Counter({"C7": 3823, "C3+C4": 982})
    remaining_pattern = Counter({
        "145": 4, "156": 16, "235": 659, "236": 1280, "237": 16,
        "245": 477, "256": 1228, "345": 21, "346": 480, "347": 4,
        "356": 656,
    }) - pattern
    assert remaining_pattern == Counter({
        "145": 4, "156": 16, "235": 654, "236": 1278, "237": 16,
        "245": 474, "256": 1204, "345": 21, "346": 479, "347": 4,
        "356": 655,
    })
    assert sum(remaining_pattern.values()) == 4805

    print("PASS")
    print("previous generic H6 endpoint: 4841 = 3853 C7 + 988 C3+C4")
    print("new exact face-(2,3) exclusions: 36 = 30 C7 + 6 C3+C4")
    print("exact one-face branch certificates used:", one_face_certificates)
    print("exact two-face product certificates used:", two_face_certificates)
    print("total exact certificates:", one_face_certificates + two_face_certificates)
    print("certificate forced values:", dict(forced))
    print("maximum exact dual denominator:", max(denominators))
    print("remaining certified endpoint: 4805 = 3823 C7 + 982 C3+C4")
    print("excluded by ground pattern:", dict(sorted(pattern.items())))

if __name__ == "__main__":
    main()
