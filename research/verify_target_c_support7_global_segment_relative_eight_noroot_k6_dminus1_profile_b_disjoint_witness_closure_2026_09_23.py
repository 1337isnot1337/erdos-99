#!/usr/bin/env python3
"""Exact exclusion of the disjoint two-witness Profile B branch.

The preceding exact-profile theorem leaves two aligned touch-three witnesses
b,c and one rank-two singleton r.  If the witness touch triples T,U are
disjoint, the coefficient line supplied by r is forced by d1(P)>=4 to have
weight exactly four: one support coordinate in T, one in U, and both source
coordinates outside T union U.

This certificate exhausts all 17 S7 role orbits of a distinguished r and an
unordered pair {b,c}.  For every source/line case satisfying that forced
pattern, it exhausts every incidence pattern of a rational rank-two coefficient
plane P containing the line.  No case has virtual canonical deficiency d8=3.

All dependency ranks are exact over Q through the imported K8 normal form.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_exact_two_witness_profile_2026_09_23.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_exact_two_witness", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)

C = B.C
G = B.G
R = B.R


def global_singleton_support(block, direction):
    return frozenset(
        e for e in R.NO_ROOT
        if G.det(direction, R.QCOMP[e][block]) != 0
    )


def enumerate_disjoint_cases(state):
    """All labeled cases for one role-orbit representative.

    state=(r,b,c), with r distinguished and {b,c} unordered.  The output is
    intentionally not stabilizer-quotiented; duplicates are harmless because
    this is an exclusion certificate.
    """
    r, b, c = state
    cases = {}

    for sb, sc, sr in product(range(3), repeat=3):
        star_b = G.aligned_star(b, R.LOCAL[sb])
        star_c = G.aligned_star(c, R.LOCAL[sc])
        support_r = global_singleton_support(r, R.LOCAL[sr])

        for omitted_b in star_b:
            T = star_b - {omitted_b}
            for omitted_c in star_c:
                U = star_c - {omitted_c}

                if T & U:
                    continue
                base = T | U
                assert len(base) == 6

                # Exact touch-three means the selected base must not include
                # either omitted star member through the other witness star.
                if base & star_b != T or base & star_c != U:
                    continue

                # In the disjoint branch d1(P)>=4 forces exactly one line
                # support point in each witness triple.
                if len(T & support_r) != 1 or len(U & support_r) != 1:
                    continue

                # The only two source coordinates outside T union U must both
                # lie in the forced line support and outside both full stars.
                outside_support = tuple(
                    e for e in support_r
                    if e not in star_b and e not in star_c
                )
                for x, y in combinations(outside_support, 2):
                    ext = tuple(sorted(base | {x, y}))
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
                    if len(support) != 4:
                        continue
                    if len(support & T) != 1 or len(support & U) != 1:
                        continue
                    if len(support - base) != 2:
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


def deficiency_histogram(cases):
    hist = Counter()
    pattern_count = 0

    for ext, _sr, line, _T, _U in cases:
        touched, _spaces, patterns = C.incidence_patterns_containing_line(ext, line)
        local = C.pattern_deficiency_histogram(touched, patterns)
        assert local.get(3, 0) == 0
        hist.update(local)
        pattern_count += len(patterns)

    return hist, pattern_count


def main():
    roles = B.role_orbits_touch4_two_touch3()
    assert len(roles) == 17
    assert sum(size for _state, size in roles) == 19635

    expected_nonempty = {
        0: (
            ((1, 2, 3), (1, 2, 4), (1, 2, 5)),
            1102,
            9068,
            Counter({6: 4768, 5: 2024, 7: 2018, 8: 154, 4: 104}),
        ),
        1: (
            ((1, 2, 3), (1, 2, 4), (1, 3, 4)),
            810,
            7092,
            Counter({6: 5562, 5: 882, 7: 648}),
        ),
        2: (
            ((1, 2, 3), (1, 2, 4), (1, 3, 5)),
            1566,
            16260,
            Counter({6: 9972, 7: 5358, 5: 552, 8: 378}),
        ),
    }

    total_cases = 0
    total_patterns = 0
    total_hist = Counter()
    records = []

    for orbit_index, (state, _orbit_size) in enumerate(roles):
        labels = tuple(R.BLOCK_LABELS[x] for x in state)
        cases = enumerate_disjoint_cases(state)
        hist, pattern_count = deficiency_histogram(cases)

        if orbit_index in expected_nonempty:
            exp_labels, exp_cases, exp_patterns, exp_hist = expected_nonempty[orbit_index]
            assert labels == exp_labels
            assert len(cases) == exp_cases
            assert pattern_count == exp_patterns
            assert hist == exp_hist
        else:
            assert not cases
            assert pattern_count == 0
            assert not hist

        total_cases += len(cases)
        total_patterns += pattern_count
        total_hist.update(hist)
        records.append((labels, len(cases), pattern_count, hist))

    assert total_cases == 3478
    assert total_patterns == 32420
    assert total_hist == Counter({
        6: 20302,
        7: 8024,
        5: 3458,
        8: 532,
        4: 104,
    })
    assert total_hist.get(3, 0) == 0

    print("PASS: disjoint two-witness Profile B branch excluded")
    print("role_orbits", len(roles))
    print("labeled_role_configurations", sum(size for _state, size in roles))
    print("source_line_cases", total_cases)
    print("coefficient_plane_incidence_patterns", total_patterns)
    print("deficiency_histogram", dict(sorted(total_hist.items())))
    print("consequence", "the two witness touch triples intersect in exactly one source cycle")


if __name__ == "__main__":
    main()
