#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

import verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28 as B

REP5 = [
    ((0, 1, 2, 3), 3),
    ((0, 1, 2, 4), 3),
    ((0, 1, 3, 4), 1),
    ((0, 2, 3, 4), 1),
    ((1, 2, 3, 5), 1),
]

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

def structural_census(ext, W, touched):
    virtual_empty = {
        b for b in touched if B.is_subspace(B.empty_key(ext, b), W)
    }
    singleton_possible = [
        b for b in touched
        if any((not L) or B.is_subspace(L, W) for L in singleton_keys(ext, b))
    ]
    placements = [()]
    placements.extend((b,) for b in singleton_possible)
    placements.extend(combinations(singleton_possible, 2))
    touched_mask = sum(1 << b for b in touched)
    base_incomplete = sum(1 << b for b in virtual_empty)
    out = Counter()
    for selected in placements:
        incomplete = base_incomplete
        for b in selected:
            incomplete |= 1 << b
        complete = touched_mask & ~incomplete
        rc = B.h_rank(complete)
        out["placements"] += 1
        if rc != complete.bit_count():
            out["dependent"] += 1
            continue
        if B.h_rank(touched_mask) - rc < 4:
            out["capacity"] += 1
            continue
        out["pass"] += 1
    return out

def main():
    census = Counter()
    for ext in B.oriented_exts(REP5):
        census["orientations"] += 1
        touched = tuple(sorted({
            b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)
        }))
        spaces = candidate_rank4_spaces(ext, touched)
        census["rank4_spaces"] += len(spaces)
        for W in spaces:
            if not B.parity_profile_ok(W):
                continue
            census["weight_pass"] += 1
            census.update(structural_census(ext, W, touched))
    expected = Counter({
        "orientations": 27,
        "rank4_spaces": 34516,
        "weight_pass": 270,
        "placements": 11394,
        "dependent": 11394,
    })
    print(dict(census))
    assert census == expected, (census, expected)
    assert census["pass"] == 0
    assert census["capacity"] == 0
    print("PASS: two-singleton support representative 5 has zero structural survivors")

if __name__ == "__main__":
    main()
