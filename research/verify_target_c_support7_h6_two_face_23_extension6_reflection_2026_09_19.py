#!/usr/bin/env python3
"""Exact face-(2,3) extension through positions 1700..2199, with reflection closure.

This verifier certifies 59 direct generic-H6 exclusions found in the next
500-position block of the 4,944-cell one-face-adaptive endpoint. Every direct
exclusion covers all 20*20 local branch products at physical faces 2 and 3
with exact rational Farkas certificates. The already-certified H6 hull
reflection maps those 59 states to 59 distinct current survivors, giving 118
new exclusions from the prior 4,276-state reflection-closed endpoint.
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


E5 = load(
    "h6_two_face_23_extension5_reflection",
    "verify_target_c_support7_h6_two_face_23_extension5_reflection_2026_09_19.py",
)
A = E5.A
O = E5.O
T = E5.T
BRANCH_KEYS = E5.BRANCH_KEYS

CANDIDATE_Q = (
    2001, 2032, 2035, 2039, 2054, 2055, 2057, 2058, 2066, 2067,
    2068, 2071, 2075, 2077, 2079, 2083, 2084, 2086, 2093, 2094,
    2096, 2099, 2105, 2108, 2116, 2118, 2123, 2135, 2167, 2173,
    2179, 2235, 2238, 2242, 2246, 2261, 2269, 2315, 2322, 2323,
    2341, 2351, 2391, 2396, 2399, 2403, 2408, 2409, 2412, 2413,
    2435, 2452, 2480, 2492, 2498, 2509, 2510, 2515, 2523,
)
assert len(CANDIDATE_Q) == len(set(CANDIDATE_Q)) == 59


def verify_range(start, stop):
    states = O.tri.collect_survivors()
    assert len(states) == 14174
    previous = O.complete_angle_survivors(states)
    assert len(previous) == 5692

    reflected, closure = E5.reflection_data(states)
    assert len(closure) == 4464

    old_direct = {previous[q] for q in E5.CANDIDATE_Q}
    assert len(old_direct) == 94
    old_reflected = {reflected[i] for i in old_direct}
    assert len(old_reflected) == 94
    assert old_direct <= closure and old_reflected <= closure
    assert old_direct.isdisjoint(old_reflected)
    current = closure - old_direct - old_reflected
    assert len(current) == 4276

    direct_idx = {previous[q] for q in CANDIDATE_Q}
    assert len(direct_idx) == 59
    assert direct_idx <= current
    reflected_idx = {reflected[i] for i in direct_idx}
    assert len(reflected_idx) == 59
    assert reflected_idx <= current
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
        assert idx in current
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
        assert graph == Counter({"C7": 53, "C3+C4": 6})
        assert pattern == Counter({
            "235": 21,
            "236": 17,
            "245": 2,
            "256": 7,
            "346": 9,
            "356": 3,
        })
        assert one_face_certificates == 1700
        assert two_face_certificates == 2321
        assert one_face_certificates + two_face_certificates == 4021
        assert forced == Counter({"negative": 3779, "zero": 242})
        assert max(denominators) == 16134134332079733307872774552

        union = direct_idx | reflected_idx
        assert len(union) == 118
        remaining = current - union
        assert len(remaining) == 4158
        remaining_graph = Counter(states[i][1] for i in remaining)
        assert remaining_graph == Counter({"C7": 3316, "C3+C4": 842})
        remaining_pattern = Counter("".join(map(str, states[i][5])) for i in remaining)
        assert remaining_pattern == Counter({
            "145": 4,
            "156": 16,
            "235": 556,
            "236": 1046,
            "237": 16,
            "245": 449,
            "256": 1046,
            "345": 16,
            "346": 449,
            "347": 4,
            "356": 556,
        })
        assert all(reflected[i] in remaining for i in remaining)

        print("PASS")
        print("starting reflection-closed generic H6 endpoint: 4276 = 3422 C7 + 854 C3+C4")
        print("direct exact face-(2,3) exclusions:", len(direct_idx))
        print("new reflected exclusions:", len(reflected_idx))
        print("total new reflection-closed exclusions:", len(union))
        print("exact one-face branch certificates:", one_face_certificates)
        print("exact two-face product certificates:", two_face_certificates)
        print("total exact certificates:", one_face_certificates + two_face_certificates)
        print("certificate forced values:", dict(forced))
        print("maximum exact dual denominator:", max(denominators))
        print("remaining explicit endpoint: 4158 = 3316 C7 + 842 C3+C4")
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
