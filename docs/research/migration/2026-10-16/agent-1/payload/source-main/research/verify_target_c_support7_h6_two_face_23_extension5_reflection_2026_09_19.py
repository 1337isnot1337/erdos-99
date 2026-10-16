#!/usr/bin/env python3
"""Exact face-(2,3) extension beyond position 1200, closed under H6 reflection.

This verifier certifies 94 direct generic-H6 exclusions from positions 1200..1699
of the 4,944-cell one-face-adaptive endpoint. Every direct exclusion covers all
20*20 local branch products at physical faces 2 and 3 with exact rational
Farkas certificates. The already-certified hull reflection involution carries
those 94 exclusions to 94 distinct states, yielding 188 exclusions from the
reflection-closed 4,464-state endpoint.
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


E4 = load(
    "h6_two_face_23_extension4",
    "verify_target_c_support7_h6_two_face_23_extension4_2026_09_19.py",
)
R = load(
    "h6_state_reflection_closure",
    "verify_target_c_support7_h6_state_reflection_closure_2026_09_19.py",
)
E3 = E4.E3
E2 = E4.E2
E = E4.E
T = E4.T
A = E4.A
O = E4.O
BRANCH_KEYS = E4.BRANCH_KEYS

CANDIDATE_Q = (
    1418, 1419, 1422, 1423, 1426, 1435, 1438, 1439, 1443, 1444,
    1450, 1456, 1460, 1462, 1486, 1488, 1490, 1495, 1499, 1501,
    1502, 1503, 1506, 1510, 1511, 1513, 1515, 1516, 1518, 1519,
    1522, 1525, 1528, 1533, 1534, 1535, 1536, 1539, 1542, 1545,
    1547, 1549, 1550, 1553, 1554, 1557, 1560, 1561, 1566, 1568,
    1569, 1573, 1574, 1579, 1580, 1583, 1584, 1612, 1617, 1639,
    1654, 1661, 1671, 1689, 1696, 1710, 1736, 1738, 1740, 1745,
    1748, 1753, 1757, 1787, 1812, 1823, 1831, 1832, 1833, 1834,
    1841, 1846, 1848, 1849, 1851, 1862, 1874, 1881, 1883, 1919,
    1931, 1939, 1960, 1962,
)
assert len(CANDIDATE_Q) == len(set(CANDIDATE_Q)) == 94


def reflection_data(states):
    current = R.decode_ledger(R.CURRENT_HEX, R.CURRENT_SHA256)
    assert len(current) == 4704
    by_key = {R.state_key(st): i for i, st in enumerate(states)}
    assert len(by_key) == len(states)
    reflected = [by_key[R.reflected_key(st)] for st in states]
    assert len(set(reflected)) == len(states)
    assert all(reflected[reflected[i]] == i for i in range(len(states)))
    closure = current & {reflected[i] for i in current}
    assert len(closure) == 4464
    return reflected, closure


def verify_range(start, stop):
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692
    reflected, closure = reflection_data(states)

    direct_idx = {previous[q] for q in CANDIDATE_Q}
    assert len(direct_idx) == 94
    assert direct_idx <= closure
    reflected_idx = {reflected[i] for i in direct_idx}
    assert len(reflected_idx) == 94
    assert reflected_idx <= closure
    assert direct_idx.isdisjoint(reflected_idx)

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
        assert idx in closure
        pat = "".join(map(str, st[5]))
        system = O.C.build_system(st)
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
        assert graph == Counter({"C7": 79, "C3+C4": 15})
        assert pattern == Counter({
            "235": 11,
            "236": 13,
            "245": 5,
            "256": 51,
            "356": 14,
        })
        assert one_face_certificates == 2535
        assert two_face_certificates == 4333
        assert one_face_certificates + two_face_certificates == 6868
        assert forced == Counter({"negative": 6426, "zero": 442})
        assert max(denominators) == 2571181654016275976801158271

        union = direct_idx | reflected_idx
        assert len(union) == 188
        remaining = closure - union
        assert len(remaining) == 4276
        remaining_graph = Counter(states[i][1] for i in remaining)
        assert remaining_graph == Counter({"C7": 3422, "C3+C4": 854})
        remaining_pattern = Counter("".join(map(str, states[i][5])) for i in remaining)
        assert remaining_pattern == Counter({
            "145": 4,
            "156": 16,
            "235": 580,
            "236": 1070,
            "237": 16,
            "245": 460,
            "256": 1070,
            "345": 16,
            "346": 460,
            "347": 4,
            "356": 580,
        })
        assert all(
            remaining_pattern[a] == remaining_pattern[b]
            for a, b in (("145", "347"), ("156", "237"), ("235", "356"),
                         ("236", "256"), ("245", "346"))
        )

        print("PASS")
        print("starting reflection-closed generic H6 endpoint: 4464 = 3580 C7 + 884 C3+C4")
        print("direct exact face-(2,3) exclusions:", len(direct_idx))
        print("new reflected exclusions:", len(reflected_idx))
        print("total new reflection-closed exclusions:", len(union))
        print("exact one-face branch certificates:", one_face_certificates)
        print("exact two-face product certificates:", two_face_certificates)
        print("total exact certificates:", one_face_certificates + two_face_certificates)
        print("certificate forced values:", dict(forced))
        print("maximum exact dual denominator:", max(denominators))
        print("remaining explicit endpoint: 4276 = 3422 C7 + 854 C3+C4")
        print("direct excluded ground patterns:", dict(sorted(pattern.items())))
        print("remaining reflection-symmetric patterns:", dict(sorted(remaining_pattern.items())))
    else:
        print("PASS chunk", start, stop)
        print("selected direct exclusions:", len(selected))
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
