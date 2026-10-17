#!/usr/bin/env python3
from collections import Counter

import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28 as B
import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_two_singleton_support3_orientation_symmetry_2026_09_29 as S

SUPPORT = [
    ((0, 1, 2, 3), 3),
    ((0, 1, 2, 4), 2),
    ((0, 1, 3, 4), 2),
    ((0, 2, 3, 4), 2),
]
TARGET_STATES = tuple(a for a, _ in S.EXPECTED_REPS_AND_SIZES)
TARGET_INDICES = tuple(a[0] * 9 + a[1] * 3 + a[2] for a in TARGET_STATES)
EXPECTED_PER_INDEX = {
    0: (2014, 33),
    1: (2069, 38),
    3: (2142, 40),
    4: (2117, 42),
    5: (2126, 39),
    6: (2095, 36),
    13: (2032, 42),
}


def local_rows(ext, block):
    vals = [B.QCOMP[e][block] for e in ext]
    return tuple(v[0] for v in vals), tuple(v[1] for v in vals)


def singleton_keys(ext, block):
    xrow, yrow = local_rows(ext, block)
    out = []
    for lx, ly in B.LOCAL:
        normal = tuple(lx * y - ly * x for x, y in zip(xrow, yrow))
        out.append(B.rowspace_key((normal,)))
    return tuple(out)


def candidate_rank4_spaces(ext, touched):
    empty_sources = []
    singleton_sources = []
    for block in touched:
        E = B.empty_key(ext, block)
        if E:
            empty_sources.append(E)
        singleton_sources.extend(L for L in singleton_keys(ext, block) if L)
    empty_sources = list(dict.fromkeys(empty_sources))
    singleton_sources = list(dict.fromkeys(singleton_sources))

    states = {((), 0)}
    for E in empty_sources:
        nxt = set(states)
        for W, q in states:
            J = B.union_key(W, E)
            if len(J) <= 4:
                nxt.add((J, q))
        states = nxt
    for L in singleton_sources:
        nxt = set(states)
        for W, q in states:
            if q >= 2:
                continue
            J = B.union_key(W, L)
            if len(J) <= 4:
                nxt.add((J, q + 1))
        states = nxt
    return {W for W, _ in states if len(W) == 4}


def check_state_convention():
    varying = [tuple(sorted(s)) for s in S.VARYING]
    assert varying == [(0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4)]
    for support in varying:
        b_cycles = tuple(S.cycle_key(tuple(v - 1 for v in B.DESC[e])) for e in B.support_cycles(support))
        assert b_cycles == S.cycles_on(support)
    assert TARGET_INDICES == (0, 1, 3, 4, 5, 6, 13)


def main():
    check_state_convention()
    census = Counter()
    virtual_empty_census = Counter()
    per_index = {}

    for index, ext in enumerate(B.oriented_exts(SUPPORT)):
        if index not in TARGET_INDICES:
            continue
        touched = tuple(sorted({
            b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)
        }))
        touched_mask = sum(1 << b for b in touched)
        assert len(touched) == 10
        assert B.h_rank(touched_mask) == 6

        spaces = candidate_rank4_spaces(ext, touched)
        passed = [W for W in spaces if B.parity_profile_ok(W)]
        per_index[index] = (len(spaces), len(passed))
        census["orientations"] += 1
        census["rank4_spaces"] += len(spaces)
        census["weight_pass"] += len(passed)

        for W in passed:
            virtual_empty = tuple(
                b for b in touched if B.is_subspace(B.empty_key(ext, b), W)
            )
            virtual_empty_census[len(virtual_empty)] += 1
            assert len(virtual_empty) <= 2

    assert per_index == EXPECTED_PER_INDEX, per_index
    assert census == Counter({"rank4_spaces": 14595, "weight_pass": 270, "orientations": 7}), census
    assert virtual_empty_census == Counter({1: 249, 2: 21}), virtual_empty_census

    print("target_indices", TARGET_INDICES)
    print("per_index", per_index)
    print("census", dict(census))
    print("virtual_empty_census", dict(sorted(virtual_empty_census.items())))
    print("PASS: support3 has no realizable orientation")


if __name__ == "__main__":
    main()
