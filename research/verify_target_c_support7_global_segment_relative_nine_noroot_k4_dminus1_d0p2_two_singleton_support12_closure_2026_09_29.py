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
AUTOS = [
    (0, 1, 2, 3, 4, 5, 6),
    (0, 1, 3, 2, 4, 5, 6),
    (1, 0, 2, 3, 4, 5, 6),
    (1, 0, 3, 2, 4, 5, 6),
    (2, 3, 0, 1, 4, 6, 5),
    (2, 3, 1, 0, 4, 6, 5),
    (3, 2, 0, 1, 4, 6, 5),
    (3, 2, 1, 0, 4, 6, 5),
]
TARGET_REPS = (660, 662, 716)


def cycle_key(t):
    t = tuple(t)
    n = len(t)
    candidates = []
    for s in range(n):
        candidates.append(t[s:] + t[:s])
    r = tuple(reversed(t))
    for s in range(n):
        candidates.append(r[s:] + r[:s])
    return min(candidates)


def orientation_orbits():
    edata = {}
    for e in B.NO_ROOT:
        cyc = tuple(v - 1 for v in B.DESC[e])
        edata[e] = (tuple(sorted(cyc)), cycle_key(cyc))
    lookup = {(supp, key): e for e, (supp, key) in edata.items()}
    assert len(lookup) == len(B.NO_ROOT)

    def map_e(e, g):
        cyc = tuple(v - 1 for v in B.DESC[e])
        mapped = tuple(g[v] for v in cyc)
        return lookup[(tuple(sorted(mapped)), cycle_key(mapped))]

    exts = list(B.oriented_exts(SUPPORT))
    assert len(exts) == 729
    ext_index = {ext: i for i, ext in enumerate(exts)}
    actions = []
    for g in AUTOS:
        action = []
        for ext in exts:
            mapped = tuple(sorted(map_e(e, g) for e in ext))
            action.append(ext_index[mapped])
        assert sorted(action) == list(range(729))
        actions.append(tuple(action))

    seen = set()
    orbits = []
    for i in range(729):
        if i in seen:
            continue
        orbit = {p[i] for p in actions}
        changed = True
        while changed:
            changed = False
            for j in tuple(orbit):
                for p in actions:
                    k = p[j]
                    if k not in orbit:
                        orbit.add(k)
                        changed = True
        seen.update(orbit)
        orbits.append(tuple(sorted(orbit)))

    assert len(orbits) == 102
    assert Counter(map(len, orbits)) == Counter({8: 82, 4: 17, 2: 2, 1: 1})
    return orbits


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
    orbits = orientation_orbits()

    excluded = set(range(0, 81)) | set(range(135, 270))
    hit = [orb for orb in orbits if set(orb) & excluded]
    saturated = set().union(*(set(orb) for orb in hit))
    remaining = [orb for orb in orbits if not (set(orb) & saturated)]
    expected_remaining = [
        (660, 661, 687, 688),
        (662, 689, 714, 715),
        (716,),
    ]
    assert len(hit) == 99
    assert len(saturated) == 720
    assert remaining == expected_remaining, remaining

    census = Counter()
    per_index = {}
    for index, ext in enumerate(B.oriented_exts(SUPPORT)):
        if index not in TARGET_REPS:
            continue
        touched = tuple(sorted({
            b for e in ext for b, v in enumerate(B.QCOMP[e]) if v != (0, 0)
        }))
        spaces = candidate_rank4_spaces(ext, touched)
        passed = [W for W in spaces if B.parity_profile_ok(W)]
        per_index[index] = (len(spaces), len(passed))
        census["orientations"] += 1
        census["rank4_spaces"] += len(spaces)
        census["weight_pass"] += len(passed)

        if index == 716:
            assert len(touched) == 16
            assert len(passed) == 8
            for W in passed:
                virtual_empty = {b for b in touched if B.is_subspace(B.empty_key(ext, b), W)}
                c0 = tuple(b for b in touched if b not in virtual_empty)
                mask = sum(1 << b for b in c0)
                assert len(virtual_empty) == 2
                assert len(c0) == 14
                assert B.h_rank(mask) == 10

    assert per_index == {660: (1121, 0), 662: (1198, 0), 716: (1394, 8)}, per_index
    assert census == Counter({"rank4_spaces": 3713, "weight_pass": 8, "orientations": 3})
    print("orbit_sizes", dict(sorted(Counter(map(len, orbits)).items())))
    print("saturated_classes", len(hit), "saturated_raw", len(saturated))
    print("remaining_orbits", remaining)
    print("final_census", dict(census))
    print("PASS: support12 has no realizable orientation once the existing [0,81) proof and executed [135,270) shards are included")


if __name__ == "__main__":
    main()
