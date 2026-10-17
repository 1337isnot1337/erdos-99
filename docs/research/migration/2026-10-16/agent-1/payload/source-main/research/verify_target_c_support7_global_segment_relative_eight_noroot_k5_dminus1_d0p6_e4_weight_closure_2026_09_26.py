#!/usr/bin/env python3
"""Exact closure of the e=4 slice in the final p=6 branch.

The proof inputs are already committed:
  * rank(P)=3 and generalized weights (d1,d2,d3)>=(2,4,5);
  * six singleton replacements, no selected pair;
  * e actual-empty touched blocks;
  * nu(T)<=e+1;
  * for nu(T)<=5, support families have 3<=m<=6.

This verifier enumerates the e=4 support/multiplicity quotient, applies
phase-independent necessary conditions for four empty blocks, then checks every
remaining phase. Mod-2 rank is used only as a lower-bound rejection:
rank_F2(U)>3 implies rank_Q(U)>3. All cases not rejected mod 2 are exactified
over Q with the committed Fraction row-space routine.
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import contextlib
import functools
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("p6_e4_base", BASE)
M = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(M)

SUPPORTS = M.SUPPORTS
PERM_DATA = M.PERM_DATA
SUPPORT_CYCLES = M.SUPPORT_CYCLES
LOCAL = M.LOCAL


def support_nullity(ss):
    touched = tuple(
        b for b, tri in enumerate(M.R.BLOCK_LABELS)
        if any(set(tri).issubset(SUPPORTS[si]) for si in ss)
    )
    return len(touched) - M.R.exact_rank(tuple(M.HROW[b] for b in touched))


def canonical_support(ss):
    return min(
        tuple(sorted(smap[i] for i in ss))
        for smap, _ in PERM_DATA
    )


def support_orbits():
    reps = {}
    unseen = set(combinations(range(35), 3))
    r3 = []
    while unseen:
        ss = min(unseen)
        orbit = {
            tuple(sorted(smap[i] for i in ss))
            for smap, _ in PERM_DATA
        }
        unseen.difference_update(orbit)
        if support_nullity(ss) <= 5:
            r3.append(ss)
    reps[3] = tuple(r3)

    for m in range(4, 7):
        cands = set()
        for ss in reps[m - 1]:
            for j in range(35):
                if j in ss:
                    continue
                u = tuple(sorted(ss + (j,)))
                if support_nullity(u) <= 5:
                    cands.add(canonical_support(u))
        reps[m] = tuple(sorted(cands))

    got = {
        m: (len(v), dict(sorted(Counter(support_nullity(s) for s in v).items())))
        for m, v in reps.items()
    }
    assert got == {
        3: (10, {3: 10}),
        4: (38, {4: 35, 5: 3}),
        5: (108, {4: 1, 5: 107}),
        6: (2, {5: 2}),
    }, got
    return reps


PROFILES = {
    3: ((3, 3, 2),),
    4: ((3, 3, 1, 1), (3, 2, 2, 1), (2, 2, 2, 2)),
    5: ((3, 2, 1, 1, 1), (2, 2, 2, 1, 1)),
    6: ((3, 1, 1, 1, 1, 1), (2, 2, 1, 1, 1, 1)),
}


@functools.lru_cache(maxsize=None)
def assignment_orbits(ss, profile):
    ss = tuple(ss)
    pos = {s: i for i, s in enumerate(ss)}
    stab = [
        smap for smap, _ in PERM_DATA
        if tuple(sorted(smap[i] for i in ss)) == ss
    ]
    unseen = set(permutations(profile))
    out = []
    while unseen:
        a = min(unseen)
        amap = dict(zip(ss, a))
        orbit = set()
        for smap in stab:
            z = [None] * len(ss)
            for s, v in amap.items():
                z[pos[smap[s]]] = v
            orbit.add(tuple(z))
        unseen.difference_update(orbit)
        out.append(a)
    return tuple(out)


def possible_empty_quads(ss, a):
    poss = {}
    for b, tri in enumerate(M.R.BLOCK_LABELS):
        idx = tuple(
            j for j, si in enumerate(ss)
            if set(tri).issubset(SUPPORTS[si])
        )
        if not idx:
            continue
        n = sum(a[j] for j in idx)
        forced_two = any(a[j] >= 2 for j in idx)
        if forced_two:
            if n < 4:
                continue
            poss[b] = (idx, 2)
        else:
            if n < 2:
                continue
            poss[b] = (idx, 1)

    out = []
    for q in combinations(poss, 4):
        ok = True
        for x, y in combinations(q, 2):
            if poss[x][1] == poss[y][1] == 2:
                shared = set(poss[x][0]) & set(poss[y][0])
                if sum(a[j] for j in shared) < 2:
                    ok = False
                    break
        if ok:
            out.append(q)
    return tuple(out)


def phase_exts(ss, a):
    opts = []
    for si, mult in zip(ss, a):
        es = SUPPORT_CYCLES[SUPPORTS[si]]
        if mult == 3:
            opts.append((es,))
        elif mult == 2:
            opts.append(tuple(combinations(es, 2)))
        elif mult == 1:
            opts.append(tuple((e,) for e in es))
        else:
            raise AssertionError(mult)
    for choice in product(*opts):
        ext = tuple(sorted(e for subset in choice for e in subset))
        assert len(ext) == 8
        yield ext


def empty_rows(ext, b):
    return (
        tuple(M.R.QCOMP[e][b][0] for e in ext),
        tuple(M.R.QCOMP[e][b][1] for e in ext),
    )


def rank_mod2(rows):
    a = [[x & 1 for x in row] for row in rows]
    r = 0
    for c in range(8):
        piv = next((i for i in range(r, len(a)) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def touched_blocks(ext):
    return tuple(
        b for b in range(35)
        if any(M.R.QCOMP[e][b] != (0, 0) for e in ext)
    )


def singleton_line(ext, b, direction):
    lx, ly = direction
    return tuple(
        lx * M.R.QCOMP[e][b][1] - ly * M.R.QCOMP[e][b][0]
        for e in ext
    )


def candidate_spaces(ext, quad, U):
    r = len(U)
    if r > 3:
        return ()
    if r == 3:
        return (U,)
    if r == 0:
        return ()

    lines = []
    seen = set()
    for b in touched_blocks(ext):
        if b in quad:
            continue
        for direction in LOCAL:
            line = M.R.rowspace_key((singleton_line(ext, b, direction),))
            if len(line) == 1 and line not in seen:
                seen.add(line)
                lines.append(line[0])

    out = set()
    if r == 2:
        for line in lines:
            P = M.R.rowspace_key(U + (line,))
            if len(P) == 3:
                out.add(P)
    elif r == 1:
        for a, b in combinations(lines, 2):
            P = M.R.rowspace_key(U + (a, b))
            if len(P) == 3:
                out.add(P)
    return tuple(out)


def generalized_weights(P):
    assert len(P) == 3
    cols = [tuple(row[j] for row in P) for j in range(8)]
    zero = (0, 0, 0)
    z = cols.count(zero)
    d3 = 8 - z

    directions = Counter(
        M.R.rowspace_key((c,))
        for c in cols if c != zero
    )
    d2 = 8 - (z + max(directions.values()))

    nonzero = [c for c in cols if c != zero]
    normals = set()
    for a, b in combinations(nonzero, 2):
        n = (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )
        if any(n):
            normals.add(M.R.rowspace_key((n,))[0])
    assert normals
    max_plane = max(
        sum(sum(n[i] * c[i] for i in range(3)) == 0 for c in cols)
        for n in normals
    )
    return 8 - max_plane, d2, d3


def main():
    reps = support_orbits()

    assignment_count = Counter()
    prefilter = Counter()
    kept = []
    total_assignments = 0

    for m in range(3, 7):
        for ss in reps[m]:
            for profile in PROFILES[m]:
                for a in assignment_orbits(ss, profile):
                    total_assignments += 1
                    assignment_count[m] += 1
                    quads = possible_empty_quads(ss, a)
                    if quads:
                        key = (m, tuple(sorted(a, reverse=True)))
                        prefilter[(key, "assignments")] += 1
                        prefilter[(key, "quads")] += len(quads)
                        kept.append((ss, a, quads))

    assert total_assignments == 2608
    assert dict(assignment_count) == {3: 17, 4: 399, 5: 2176, 6: 16}
    expected_prefilter = {
        (4, (3, 3, 1, 1)): (2, 3),
        (5, (3, 2, 1, 1, 1)): (150, 363),
        (5, (2, 2, 2, 1, 1)): (15, 15),
        (6, (3, 1, 1, 1, 1, 1)): (6, 1260),
        (6, (2, 2, 1, 1, 1, 1)): (10, 90),
    }
    got_prefilter = {}
    for key in expected_prefilter:
        got_prefilter[key] = (
            prefilter[(key, "assignments")],
            prefilter[(key, "quads")],
        )
    assert got_prefilter == expected_prefilter, got_prefilter
    assert len(kept) == 183
    assert sum(len(q) for _, _, q in kept) == 1731

    counts = Counter()
    weights = Counter()

    for ss, a, quads in kept:
        counts["phase_configs"] += 3 ** sum(mult < 3 for mult in a)
        for ext in phase_exts(ss, a):
            for quad in quads:
                counts["phase_quad_pairs"] += 1
                rows = []
                for b in quad:
                    rows.extend(empty_rows(ext, b))

                if rank_mod2(rows) > 3:
                    counts["mod2_reject"] += 1
                    continue

                counts["exact_checks"] += 1
                U = M.R.rowspace_key(tuple(rows))
                counts[f"exact_U_rank_{len(U)}"] += 1
                spaces = candidate_spaces(ext, quad, U)
                counts["candidate_spaces"] += len(spaces)

                for P in spaces:
                    w = generalized_weights(P)
                    weights[w] += 1
                    if w[0] >= 2 and w[1] >= 4 and w[2] >= 5:
                        counts["generalized_weight_survivors"] += 1

    assert counts["phase_configs"] == 24561
    assert counts["phase_quad_pairs"] == 404865
    assert counts["mod2_reject"] == 404047
    assert counts["exact_checks"] == 818
    assert counts["exact_U_rank_3"] == 818
    assert sum(v for k, v in counts.items() if k.startswith("exact_U_rank_") and k != "exact_U_rank_3") == 0
    assert counts["candidate_spaces"] == 818
    assert dict(weights) == {(2, 3, 4): 768, (2, 3, 5): 50}
    assert counts["generalized_weight_survivors"] == 0

    print("PASS: p=6 e=4 generalized-weight closure")
    print("support_orbits", {m: len(v) for m, v in reps.items()})
    print("support_multiplicity_orbits", total_assignments)
    print("prefilter_assignments", len(kept))
    print("prefilter_empty_quadruples", sum(len(q) for _, _, q in kept))
    print("phase_configs", counts["phase_configs"])
    print("phase_quad_pairs", counts["phase_quad_pairs"])
    print("mod2_rank_gt3_rejections", counts["mod2_reject"])
    print("exact_checks", counts["exact_checks"])
    print("exact_U_rank_3", counts["exact_U_rank_3"])
    print("generalized_weights", dict(sorted(weights.items())))


if __name__ == "__main__":
    main()
