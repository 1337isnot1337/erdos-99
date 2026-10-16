#!/usr/bin/env python3
from collections import Counter

import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28 as B

SUPPORT = [
    ((0, 1, 2, 3), 3),
    ((0, 1, 2, 4), 1),
    ((0, 1, 3, 4), 1),
    ((0, 1, 4, 5), 1),
    ((0, 2, 3, 4), 1),
    ((1, 2, 3, 4), 1),
    ((2, 3, 4, 6), 1),
]

START = 54
STOP = 81


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


def main():
    census = Counter()
    for index, ext in enumerate(B.oriented_exts(SUPPORT)):
        if index < START:
            continue
        if index >= STOP:
            break
        census["orientations"] += 1
        touched = tuple(sorted({
            b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)
        }))
        spaces = candidate_rank4_spaces(ext, touched)
        census["rank4_spaces"] += len(spaces)
        for W in spaces:
            if B.parity_profile_ok(W):
                census["weight_pass"] += 1
    expected = Counter({"orientations": 27, "rank4_spaces": 40586})
    print(dict(census))
    assert census == expected, (census, expected)
    print("PASS: support12 orientation shard [54,81) has no generalized-weight-admissible rank-four space")


if __name__ == "__main__":
    main()
