#!/usr/bin/env python3
"""Exact certificate for 101 further generic-H6 cells using physical faces 2 and 3.

Starting point: the committed 4,805-cell generic support-seven H6 endpoint.
The 101 q-indices below are candidates found in positions 700..1199 of the
4,944-cell one-face-adaptive endpoint. Earlier committed face-(2,3) extension
batches cover positions below 700, so this batch is disjoint from them.

For every listed cell, the verifier reconstructs the global 85-variable
complete-angle system. At each of physical faces 2 and 3 it tests all twenty
closed local branches (ten cyclic gap orders times low/high median side). A
locally dead branch is accepted only after exact rational Farkas recovery. For
every pair of locally live branches, the two-face product is again required to
have an exact rational Farkas contradiction. Thus all 20*20 covering products
are certified impossible.

Floating-point LPs are used only to propose dual supports. Every accepted
certificate is re-solved and checked by the committed Fraction-based checker.
Use --start/--stop to recheck a contiguous candidate chunk. With no arguments
the script verifies all 101 exclusions and the resulting census.
"""

from argparse import ArgumentParser
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


E3 = load(
    "h6_two_face_23_extension3",
    "verify_target_c_support7_h6_two_face_23_extension3_2026_09_19.py",
)
E2 = E3.E2
E = E3.E
T = E3.T
A = E3.A
O = E3.O
BRANCH_KEYS = E3.BRANCH_KEYS

CANDIDATE_Q = (
    819, 829, 844, 847, 848, 854, 855, 863, 868, 896, 904, 905,
    906, 908, 917, 920, 935, 941, 943, 949, 968, 971, 992, 1016,
    1030, 1032, 1040, 1056, 1068, 1072, 1074, 1083, 1090, 1095, 1099, 1101,
    1103, 1104, 1110, 1111, 1120, 1128, 1146, 1148, 1154, 1165, 1169, 1170,
    1178, 1180, 1181, 1184, 1190, 1192, 1193, 1196, 1219, 1220, 1232, 1234,
    1244, 1263, 1264, 1268, 1273, 1274, 1279, 1292, 1296, 1298, 1305, 1306,
    1308, 1310, 1312, 1314, 1319, 1322, 1324, 1327, 1330, 1332, 1336, 1338,
    1342, 1344, 1347, 1353, 1362, 1364, 1365, 1371, 1377, 1381, 1383, 1384,
    1385, 1392, 1394, 1407, 1408,
)
assert len(CANDIDATE_Q) == len(set(CANDIDATE_Q)) == 101


def qset(module):
    return {int(row[0]) for row in module.CANDIDATES}


def verify_range(start, stop):
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692

    old = qset(A) | qset(T) | qset(E) | qset(E2) | qset(E3)
    assert len(old) == 171
    assert old.isdisjoint(CANDIDATE_Q)

    selected = CANDIDATE_Q[start:stop]
    graph = Counter()
    pattern = Counter()
    forced = Counter()
    denominators = [1]
    one_face_certificates = 0
    two_face_certificates = 0

    for serial, q in enumerate(selected, start=start):
        idx = previous[q]
        st = states[idx]
        pat = "".join(map(str, st[5]))
        system = O.C.build_system(st)

        # Recheck the preceding 716-cell order-hull reduction. Disjointness
        # from A/T/E/E2/E3 then places the cell in the committed 4,805 endpoint.
        assert A.survives_previous_order_hull(system)

        live = {}
        for face in (2, 3):
            live_here = []
            for branch_index, (order, side) in enumerate(BRANCH_KEYS):
                closed = A.BRANCH[(face, order, side)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                if margin > 1e-8:
                    live_here.append(branch_index)
                    continue
                cert = A.exactify_support(system, closed, result)
                assert cert is not None
                T.record_certificate(cert, forced, denominators)
                one_face_certificates += 1
            assert live_here
            live[face] = live_here

        for i2 in live[2]:
            o2, s2 = BRANCH_KEYS[i2]
            for i3 in live[3]:
                o3, s3 = BRANCH_KEYS[i3]
                closed = A.BRANCH[(2, o2, s2)] + A.BRANCH[(3, o3, s3)]
                margin, result = O.numerical_candidate(system, closed)
                assert margin is not None, result.message
                assert margin <= 1e-8
                cert = A.exactify_support(system, closed, result)
                assert cert is not None
                T.record_certificate(cert, forced, denominators)
                two_face_certificates += 1

        graph[st[1]] += 1
        pattern[pat] += 1
        print(
            "verified", serial + 1, "/", len(CANDIDATE_Q),
            "q", q, "idx", idx, "live", len(live[2]), len(live[3]),
            flush=True,
        )

    if start == 0 and stop == len(CANDIDATE_Q):
        assert graph == Counter({"C7": 63, "C3+C4": 38})
        assert pattern == Counter({
            "235": 12,
            "236": 15,
            "245": 3,
            "256": 51,
            "345": 1,
            "346": 1,
            "356": 18,
        })
        assert one_face_certificates == 2657
        assert two_face_certificates == 5589
        assert one_face_certificates + two_face_certificates == 8246
        assert forced == Counter({"negative": 7826, "zero": 420})
        assert max(denominators) == 5955951748146827421119871

        remaining_graph = Counter({"C7": 3823, "C3+C4": 982}) - graph
        assert remaining_graph == Counter({"C7": 3760, "C3+C4": 944})

        remaining_pattern = Counter({
            "145": 4,
            "156": 16,
            "235": 654,
            "236": 1278,
            "237": 16,
            "245": 474,
            "256": 1204,
            "345": 21,
            "346": 479,
            "347": 4,
            "356": 655,
        }) - pattern
        assert remaining_pattern == Counter({
            "145": 4,
            "156": 16,
            "235": 642,
            "236": 1263,
            "237": 16,
            "245": 471,
            "256": 1153,
            "345": 20,
            "346": 478,
            "347": 4,
            "356": 637,
        })
        assert sum(remaining_pattern.values()) == 4704

        mirror_pairs = (
            ("145", "347"),
            ("156", "237"),
            ("235", "356"),
            ("236", "256"),
            ("245", "346"),
        )
        reflection_gain = sum(
            abs(remaining_pattern[a] - remaining_pattern[b])
            for a, b in mirror_pairs
        )
        assert reflection_gain == 122
        reflection_upper_bound = 4704 - reflection_gain
        assert reflection_upper_bound == 4582

        print("PASS")
        print("previous certified generic H6 endpoint: 4805 = 3823 C7 + 982 C3+C4")
        print("new exact face-(2,3) exclusions: 101 = 63 C7 + 38 C3+C4")
        print("exact one-face branch certificates:", one_face_certificates)
        print("exact two-face product certificates:", two_face_certificates)
        print("total exact certificates:", one_face_certificates + two_face_certificates)
        print("certificate forced values:", dict(forced))
        print("maximum exact dual denominator:", max(denominators))
        print("remaining explicit endpoint: 4704 = 3760 C7 + 944 C3+C4")
        print("excluded by ground pattern:", dict(sorted(pattern.items())))
        print("reflection-closed survivor upper bound:", reflection_upper_bound)
    else:
        print("PASS chunk", start, stop)
        print("selected exclusions:", len(selected))
        print("graph:", dict(graph))
        print("patterns:", dict(sorted(pattern.items())))
        print("certificates:", one_face_certificates + two_face_certificates)
        print("forced:", dict(forced))
        print("maximum exact dual denominator:", max(denominators))


def main():
    parser = ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=len(CANDIDATE_Q))
    args = parser.parse_args()
    assert 0 <= args.start <= args.stop <= len(CANDIDATE_Q)
    verify_range(args.start, args.stop)


if __name__ == "__main__":
    main()
