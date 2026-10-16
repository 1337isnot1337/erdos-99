#!/usr/bin/env python3
"""Exact closure of the intersecting two-witness Profile B branch.

Inputs already proved in the repository leave exactly two aligned touch-three
witnesses b,c, one dependency-active rank-two singleton r, coefficient rank two
with d1(P)>=4, and |T intersect U|=1 for the witness touch triples.

The shared source cycle forces |b intersect c|=2.  Since only three source
coordinates lie outside T union U, d1(P)>=4 forces the distinguished coefficient
line L_r to meet T union U.  Any such support coordinate touches r and at least
one witness block, forcing r to share two vertices with at least one of b,c.
Among the 17 role orbits from the preceding exact-profile verifier, only three
orbits satisfy these necessary intersection conditions.

For those three roles this certificate enumerates every exact one-overlap source
geometry compatible with the true aligned touch-three condition, the rank-two
singleton condition at r, and wt(L_r) in {4,5}.  For each source it classifies
all rational rank-two coefficient planes through L_r into finitely many
exceptional planes plus the generic incidence class.  Generic planes never have
source deficiency three.  Among all exceptional planes only four have
coefficient minimum distance at least four, and all four have deficiency seven.
Thus Profile B is empty.

All dependency and coefficient calculations are exact over Q through the
committed K8 normal form.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_disjoint_witness_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_disjoint", BASE)
D = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(D)

B = D.B
C = D.C
G = D.G
R = D.R


def role_signature(state):
    r, b, c = (set(R.BLOCK_LABELS[x]) for x in state)
    return len(b & c), len(r & b), len(r & c)


def surviving_role_orbits():
    roles = B.role_orbits_touch4_two_touch3()
    assert len(roles) == 17
    assert sum(size for _state, size in roles) == 19635

    survivors = []
    for state, orbit_size in roles:
        bc, rb, rc = role_signature(state)
        if bc == 2 and max(rb, rc) == 2:
            survivors.append((state, orbit_size))

    labels = tuple(
        tuple(R.BLOCK_LABELS[x] for x in state)
        for state, _size in survivors
    )
    assert labels == (
        ((1, 2, 3), (1, 2, 4), (1, 2, 5)),
        ((1, 2, 3), (1, 2, 4), (1, 3, 4)),
        ((1, 2, 3), (1, 2, 4), (1, 4, 5)),
    )
    return tuple(survivors)


def enumerate_overlap_cases(state):
    """Enumerate every genuine one-overlap source/line geometry for one role.

    The source has exact touch-three aligned witnesses, so the three coordinates
    outside T union U cannot touch b or c at all.  The base T union U is left
    slightly permissive: we do not reject accidental off-star cross-touches.
    This only enlarges the census and therefore keeps the exclusion safe.
    """
    r, b, c = state
    cases = {}

    for sb, sc, sr in product(range(3), repeat=3):
        star_b = G.aligned_star(b, R.LOCAL[sb])
        star_c = G.aligned_star(c, R.LOCAL[sc])
        support_r = D.global_singleton_support(r, R.LOCAL[sr])

        for omitted_b in star_b:
            T = star_b - {omitted_b}
            for omitted_c in star_c:
                U = star_c - {omitted_c}

                if len(T & U) != 1:
                    continue
                base = T | U
                if len(base) != 5:
                    continue
                if base & star_b != T or base & star_c != U:
                    continue

                base_support = frozenset(base & support_r)
                if len(base_support & T) > 1 or len(base_support & U) > 1:
                    continue

                outside = tuple(
                    e for e in R.NO_ROOT
                    if e not in base
                    and R.QCOMP[e][b] == (0, 0)
                    and R.QCOMP[e][c] == (0, 0)
                )
                outside_support = tuple(e for e in outside if e in support_r)
                outside_zero = tuple(e for e in outside if e not in support_r)
                base_weight = len(base_support)

                for weight in (4, 5):
                    need_support = weight - base_weight
                    if not 0 <= need_support <= 3:
                        continue
                    if len(outside_support) < need_support:
                        continue
                    if len(outside_zero) < 3 - need_support:
                        continue

                    for a in combinations(outside_support, need_support):
                        for z in combinations(outside_zero, 3 - need_support):
                            ext = tuple(sorted(base | set(a) | set(z)))
                            if len(ext) != 8:
                                continue
                            if len(G.local_empty_space(ext, r)) != 2:
                                continue

                            line = G.singleton_row(ext, r, R.LOCAL[sr])
                            line_key = R.rowspace_key((line,))
                            if len(line_key) != 1:
                                continue
                            support = frozenset(
                                ext[i] for i, value in enumerate(line) if value
                            )
                            if len(support) != weight:
                                continue
                            if len(support & T) > 1 or len(support & U) > 1:
                                continue

                            key = (
                                ext,
                                sr,
                                line_key[0],
                                tuple(sorted(T)),
                                tuple(sorted(U)),
                            )
                            cases[key] = None

    return cases


def projective_min_weight(plane):
    """Minimum Hamming weight of a nonzero row of a rational rank-two code."""
    plane = R.rowspace_key(plane)
    assert len(plane) == 2
    a, b = plane
    zero_columns = 0
    projective = Counter()

    for x, y in zip(a, b):
        if x == 0 and y == 0:
            zero_columns += 1
        elif x != 0:
            projective[(Fraction(1), y / x)] += 1
        else:
            projective[(Fraction(0), Fraction(1))] += 1

    max_projective = max(projective.values(), default=0)
    return len(a) - zero_columns - max_projective


def source_incidence_data(ext, line_row):
    """Return generic deficiency and all exceptional planes through L_r.

    Rank-two planes through one fixed line form a projective family.  A source
    local empty space changes its containment status only when the plane equals
    a two-dimensional local empty space containing L_r, or when it is spanned by
    L_r and a distinct one-dimensional local empty line.  These are exactly the
    finite exceptional planes below; every other plane has the same generic
    incomplete-block pattern.
    """
    touched = G.touched_blocks(ext)
    spaces = {b: G.local_empty_space(ext, b) for b in touched}
    line = R.rowspace_key((line_row,))
    assert len(line) == 1

    planes = set()
    for space in spaces.values():
        if len(space) == 2 and G.is_subspace(line, space):
            planes.add(space)
        elif len(space) == 1:
            plane = R.rowspace_key(line + space)
            if len(plane) == 2:
                planes.add(plane)

    generic_incomplete = frozenset(
        b for b, space in spaces.items()
        if len(space) == 1 and space == line
    )
    generic_complete = tuple(b for b in touched if b not in generic_incomplete)
    generic_deficiency = C.deficiency_from_complete(generic_complete)
    return touched, spaces, line, planes, generic_deficiency


def scan_role(state):
    cases = enumerate_overlap_cases(state)
    weight_hist = Counter()
    generic_hist = Counter()
    exceptional_planes = 0
    d1_valid_exceptional = 0
    valid_exceptional_hist = Counter()

    for ext, _sr, line_row, _T, _U in cases:
        weight_hist[sum(value != 0 for value in line_row)] += 1
        touched, spaces, line, planes, generic_d = source_incidence_data(
            ext, line_row
        )
        generic_hist[generic_d] += 1

        for plane in planes:
            exceptional_planes += 1
            if projective_min_weight(plane) < 4:
                continue
            d1_valid_exceptional += 1
            incomplete = frozenset(
                b for b, space in spaces.items()
                if G.is_subspace(space, plane)
            )
            complete = tuple(b for b in touched if b not in incomplete)
            deficiency = C.deficiency_from_complete(complete)
            valid_exceptional_hist[deficiency] += 1

    assert generic_hist.get(3, 0) == 0
    assert valid_exceptional_hist.get(3, 0) == 0
    return (
        len(cases),
        weight_hist,
        exceptional_planes,
        d1_valid_exceptional,
        generic_hist,
        valid_exceptional_hist,
    )


def main():
    roles = surviving_role_orbits()
    expected = (
        (
            7280,
            Counter({4: 7216, 5: 64}),
            77620,
            4,
            Counter({8: 3852, 7: 2544, 9: 576, 10: 192, 11: 84, 6: 32}),
            Counter({7: 4}),
        ),
        (
            1026,
            Counter({4: 1026}),
            11022,
            0,
            Counter({7: 648, 8: 378}),
            Counter(),
        ),
        (
            684,
            Counter({4: 684}),
            7156,
            0,
            Counter({7: 432, 8: 252}),
            Counter(),
        ),
    )

    records = []
    for (state, _orbit_size), exp in zip(roles, expected):
        record = scan_role(state)
        assert record == exp, (tuple(R.BLOCK_LABELS[x] for x in state), record, exp)
        records.append(record)

    total_cases = sum(x[0] for x in records)
    total_exceptional = sum(x[2] for x in records)
    total_valid_exceptional = sum(x[3] for x in records)
    generic_hist = Counter()
    exceptional_hist = Counter()
    for x in records:
        generic_hist.update(x[4])
        exceptional_hist.update(x[5])

    assert total_cases == 8990
    assert total_exceptional == 95798
    assert total_valid_exceptional == 4
    assert generic_hist == Counter({
        8: 4482,
        7: 3624,
        9: 576,
        10: 192,
        11: 84,
        6: 32,
    })
    assert exceptional_hist == Counter({7: 4})
    assert generic_hist.get(3, 0) == 0
    assert exceptional_hist.get(3, 0) == 0

    print("PASS: intersecting two-witness Profile B branch excluded")
    print("surviving_role_orbits", len(roles))
    print("source_line_cases", total_cases)
    print("exceptional_planes", total_exceptional)
    print("d1_ge_4_exceptional_planes", total_valid_exceptional)
    print("generic_deficiency_histogram", dict(sorted(generic_hist.items())))
    print("d1_ge_4_exceptional_deficiency_histogram", dict(sorted(exceptional_hist.items())))
    print("consequence", "Profile B is empty")


if __name__ == "__main__":
    main()
