#!/usr/bin/env python3
"""Exact certificate forcing two Profile B touch-three kernel witnesses.

This closes every remaining branch with exactly one dependency-active aligned
source block of touch count three.  The proof reduces that hypothesis to two
normalized source geometries.  For each geometry we enumerate a *superset* of
all rank-two coefficient planes by their incidences with the finitely many
local empty spaces and show that virtual canonical deficiency d8=3 never
occurs.

The first branch has two active aligned touch-four blocks and no rank-two
singleton block.  The second has one active touch-four block and one active
rank-two singleton block.  All calculations are exact over Fraction through
the imported K8 normal form.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_touch4_alternative_closure_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_touch4", BASE)
G = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(G)
R = G.R


def deficiency_from_complete(complete):
    rank = len(R.rowspace_key(tuple(G.COMPLETE_T[b] for b in complete)))
    return len(complete) - rank


def local_spaces(ext):
    touched = G.touched_blocks(ext)
    return touched, {b: G.local_empty_space(ext, b) for b in touched}


def incidence_patterns_unrestricted(ext):
    """All incomplete-block patterns induced by an arbitrary rank-two P.

    A two-dimensional local empty space can be contained only when it equals P.
    Two distinct rank-one local lines determine P.  The remaining possibilities
    are a generic plane through one line class, or a generic plane through none
    of the finitely many local spaces.
    """
    touched, spaces = local_spaces(ext)
    planes = set()
    lines = set()
    for space in spaces.values():
        if len(space) == 2:
            planes.add(space)
        elif len(space) == 1:
            lines.add(space)
        else:
            raise AssertionError("touched block has zero local empty rank")

    for a, b in combinations(tuple(lines), 2):
        plane = R.rowspace_key(a + b)
        if len(plane) == 2:
            planes.add(plane)

    patterns = set()
    for plane in planes:
        patterns.add(frozenset(
            b for b, space in spaces.items() if G.is_subspace(space, plane)
        ))

    for line in lines:
        patterns.add(frozenset(
            b for b, space in spaces.items() if len(space) == 1 and space == line
        ))

    patterns.add(frozenset())
    return touched, spaces, patterns


def incidence_patterns_containing_line(ext, line_row):
    """All incomplete patterns for rank-two P containing one forced line."""
    touched, spaces = local_spaces(ext)
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

    patterns = set()
    for plane in planes:
        patterns.add(frozenset(
            b for b, space in spaces.items() if G.is_subspace(space, plane)
        ))

    # Generic rational plane through the forced line and no additional local
    # line.  Any local line equal to the forced line is necessarily contained.
    patterns.add(frozenset(
        b for b, space in spaces.items() if len(space) == 1 and space == line
    ))
    return touched, spaces, patterns


def pattern_deficiency_histogram(touched, patterns):
    hist = Counter()
    for incomplete in patterns:
        complete = tuple(b for b in touched if b not in incomplete)
        hist[deficiency_from_complete(complete)] += 1
    return hist


def two_touch4_branch():
    """Case A: one touch-three star plus two full touch-four stars."""
    b = R.BLOCK_INDEX[(1, 2, 3)]
    c = R.BLOCK_INDEX[(1, 2, 4)]
    d = R.BLOCK_INDEX[(1, 2, 5)]

    records = []
    source_sets = set()
    for sb, sc, sd in product(range(3), repeat=3):
        b_star = G.aligned_star(b, R.LOCAL[sb])
        c_star = G.aligned_star(c, R.LOCAL[sc])
        d_star = G.aligned_star(d, R.LOCAL[sd])
        for omitted in b_star:
            touch_three = b_star - {omitted}
            ext = frozenset(c_star | d_star | touch_three)
            if len(ext) != 8:
                continue
            if ext & b_star != touch_three:
                continue
            records.append((sb, sc, sd, omitted, tuple(sorted(ext))))
            source_sets.add(tuple(sorted(ext)))

    assert len(records) == 2
    assert len(source_sets) == 2

    total = Counter()
    per_source = []
    for ext in sorted(source_sets):
        touched, _spaces, patterns = incidence_patterns_unrestricted(ext)
        hist = pattern_deficiency_histogram(touched, patterns)
        assert len(patterns) == 90
        assert hist == Counter({6: 76, 7: 13, 8: 1})
        assert 3 not in hist
        total.update(hist)
        per_source.append(hist)

    assert total == Counter({6: 152, 7: 26, 8: 2})
    return records, per_source, total


def mixed_branch():
    """Case B: touch-three b, touch-four c, rank-two singleton r."""
    b = R.BLOCK_INDEX[(1, 2, 3)]
    c = R.BLOCK_INDEX[(1, 2, 4)]
    r = R.BLOCK_INDEX[(1, 2, 5)]

    cases = {}
    for sb, sc, sr in product(range(3), repeat=3):
        b_star = G.aligned_star(b, R.LOCAL[sb])
        c_star = G.aligned_star(c, R.LOCAL[sc])

        for omitted in b_star:
            touch_three = b_star - {omitted}
            union = touch_three | c_star
            if len(union) != 6:
                continue
            if union & b_star != touch_three:
                continue

            outside = []
            for e in R.NO_ROOT:
                if e in union:
                    continue
                if R.QCOMP[e][b] != (0, 0) or R.QCOMP[e][c] != (0, 0):
                    continue
                if G.det(R.LOCAL[sr], R.QCOMP[e][r]) == 0:
                    continue
                outside.append(e)

            for x, y in combinations(outside, 2):
                ext = tuple(sorted(union | {x, y}))
                if len(ext) != 8:
                    continue
                ext_set = frozenset(ext)
                if ext_set & b_star != touch_three or ext_set & c_star != c_star:
                    continue

                line = G.singleton_row(ext, r, R.LOCAL[sr])
                support = {ext[i] for i, value in enumerate(line) if value}
                if len(support) != 4:
                    continue
                if len(G.local_empty_space(ext, r)) != 2:
                    continue
                if len(support & touch_three) != 1:
                    continue
                if len(support & c_star) != 1:
                    continue
                if len(support - (touch_three | c_star)) != 2:
                    continue

                key = (ext, sr, tuple(Fraction(x) for x in line))
                cases[key] = (sb, sc, sr, omitted, touch_three, c_star, line)

    assert len(cases) == 44

    total = Counter()
    pattern_count_distribution = Counter()
    for (ext, _sr, line_key), _meta in cases.items():
        touched, _spaces, patterns = incidence_patterns_containing_line(ext, line_key)
        hist = pattern_deficiency_histogram(touched, patterns)
        assert 3 not in hist
        pattern_count_distribution[len(patterns)] += 1
        total.update(hist)

    assert pattern_count_distribution == Counter({12: 20, 10: 12, 11: 8, 13: 4})
    assert total == Counter({7: 308, 6: 164, 8: 28})
    assert sum(total.values()) == 500
    return cases, pattern_count_distribution, total


def main():
    records, _per_source, case_a = two_touch4_branch()
    cases, distribution, case_b = mixed_branch()

    print("PASS: every remaining Profile B source has at least two active aligned touch-three blocks")
    print("case_A_labeled_source_sets", len(records))
    print("case_A_deficiency_histogram", dict(sorted(case_a.items())))
    print("case_B_normalized_cases", len(cases))
    print("case_B_pattern_count_distribution", dict(sorted(distribution.items())))
    print("case_B_incidence_patterns", sum(case_b.values()))
    print("case_B_deficiency_histogram", dict(sorted(case_b.items())))
    print("consequence", "at least two distinct d5=2 touch-three punctures with coordinate-split kernels")


if __name__ == "__main__":
    main()
