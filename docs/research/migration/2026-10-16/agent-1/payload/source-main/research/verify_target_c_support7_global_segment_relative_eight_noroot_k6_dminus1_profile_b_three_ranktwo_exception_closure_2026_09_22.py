#!/usr/bin/env python3
"""Exact closure of the three-rank-two singleton exception in Profile B.

Inputs already proved in the repository:

* the remaining eight-no-root Profile B source has rank(P)=2 and d1(P)>=4;
* if three singleton blocks have rank-two local empty spaces, then necessarily
  d2(P)=6 with projective multiplicities (2,2,2), and up to S7 the three root
  blocks are 123,124,125;
* all eight source coordinates are three-clean, so every two-coordinate
  puncture must retain coefficient rank two and virtual deficiency three.

This verifier exactifies the unique three-rank-two geometry.  It first checks
all 27 choices of singleton local directions on 123,124,125 and proves that
only one normalized direction triple realizes the required (2,2,2) coefficient
plane.  That fixes the six nonzero source coordinates.  It then exhausts the
87 possible zero-column cycles, hence 3741 unordered zero-column pairs, and
computes the canonical complete-block deficiency exactly over Q.  Only three
pairs have source deficiency three; every one has a rank-preserving two-row
puncture with deficiency two.  This contradicts three-clean synchronization.

Thus the exceptional three-rank-two Profile B source does not exist.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py"
spec = importlib.util.spec_from_file_location("profile_b_three_ranktwo_base", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

ROOT_FACES = ((1, 2, 3), (1, 2, 4), (1, 2, 5))
ROOT_BLOCKS = tuple(R.BLOCK_INDEX[face] for face in ROOT_FACES)
PAIR_FOURSETS = {
    (0, 1): frozenset((1, 2, 3, 4)),
    (0, 2): frozenset((1, 2, 3, 5)),
    (1, 2): frozenset((1, 2, 4, 5)),
}

COMPLETE_T = tuple(
    tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )
    for ids in R.BLOCKS
)


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def singleton_row(ext, block, direction):
    return tuple(det(direction, R.QCOMP[e][block]) for e in ext)


def touched_blocks(ext):
    return tuple(
        b for b in range(35)
        if any(R.QCOMP[e][b] != (0, 0) for e in ext)
    )


def local_empty_space(ext, block):
    vals = tuple(R.QCOMP[e][block] for e in ext)
    return R.rowspace_key((
        tuple(v[0] for v in vals),
        tuple(v[1] for v in vals),
    ))


def is_subspace(a, b):
    return len(R.union_key(a, b)) == len(b)


def canonical_deficiency(ext, space):
    complete = tuple(
        b for b in touched_blocks(ext)
        if not is_subspace(local_empty_space(ext, b), space)
    )
    rank = len(R.rowspace_key(tuple(COMPLETE_T[b] for b in complete)))
    return len(complete) - rank, complete


def project_space(space, drops):
    drops = frozenset(drops)
    return R.rowspace_key(tuple(
        tuple(x for j, x in enumerate(row) if j not in drops)
        for row in space
    ))


def projective_column_profile(space):
    basis = R.rowspace_key(space)
    assert len(basis) == 2
    counts = Counter()
    zero = 0
    for j in range(len(basis[0])):
        x, y = basis[0][j], basis[1][j]
        if x == 0 and y == 0:
            zero += 1
            continue
        if x != 0:
            key = (Fraction(1), y / x)
        else:
            key = (Fraction(0), Fraction(1))
        counts[key] += 1
    return zero, tuple(sorted(counts.values(), reverse=True))


def cycles_on(fourset):
    return tuple(e for e in R.NO_ROOT if frozenset(R.DESC[e]) == fourset)


def direction_rigidity():
    """Return the unique normalized three-block rank-two realization."""
    surviving = []
    for directions in product(R.LOCAL, repeat=3):
        packets = {}
        valid = True
        for pair, fourset in PAIR_FOURSETS.items():
            i, j = pair
            common = cycles_on(fourset)
            assert len(common) == 3
            packet = tuple(
                e for e in common
                if det(directions[i], R.QCOMP[e][ROOT_BLOCKS[i]]) != 0
                and det(directions[j], R.QCOMP[e][ROOT_BLOCKS[j]]) != 0
            )
            if len(packet) != 2:
                valid = False
                break
            packets[pair] = packet
        if not valid:
            continue

        six = tuple(e for pair in ((0, 1), (0, 2), (1, 2)) for e in packets[pair])
        if len(set(six)) != 6:
            continue
        rows = tuple(
            singleton_row(six, block, direction)
            for block, direction in zip(ROOT_BLOCKS, directions)
        )
        plane = R.rowspace_key(rows)
        if len(plane) != 2:
            continue
        if projective_column_profile(plane) != (0, (2, 2, 2)):
            continue
        surviving.append((directions, packets, six, rows, plane))

    assert len(surviving) == 1
    directions, packets, six, rows, plane = surviving[0]
    assert directions == (R.LOCAL[1], R.LOCAL[1], R.LOCAL[1])
    assert rows == (
        (-1, 1, -1, 1, 0, 0),
        (1, -1, 0, 0, -1, 1),
        (0, 0, 1, -1, 1, -1),
    )
    assert tuple(x + y + z for x, y, z in zip(*rows)) == (0, 0, 0, 0, 0, 0)
    return directions, packets, six, plane


def main():
    directions, packets, six, _plane6 = direction_rigidity()

    omitted = {}
    for pair, fourset in PAIR_FOURSETS.items():
        common = set(cycles_on(fourset))
        missing = tuple(common - set(packets[pair]))
        assert len(missing) == 1
        omitted[pair] = missing[0]

    zero_candidates = tuple(
        e for e in R.NO_ROOT
        if e not in set(six)
        and all(
            det(direction, R.QCOMP[e][block]) == 0
            for block, direction in zip(ROOT_BLOCKS, directions)
        )
    )
    assert len(zero_candidates) == 87

    deficiency_histogram = Counter()
    d3_records = []
    for zeros in combinations(zero_candidates, 2):
        ext8 = six + zeros
        rows8 = tuple(
            singleton_row(ext8, block, direction)
            for block, direction in zip(ROOT_BLOCKS, directions)
        )
        plane8 = R.rowspace_key(rows8)
        assert len(plane8) == 2
        assert projective_column_profile(plane8) == (2, (2, 2, 2))
        d8, complete8 = canonical_deficiency(ext8, plane8)
        deficiency_histogram[d8] += 1
        if d8 == 3:
            d3_records.append((zeros, ext8, plane8, complete8))

    assert deficiency_histogram == Counter({5: 2982, 6: 441, 4: 315, 3: 3})
    expected_zero_pairs = {
        frozenset(pair) for pair in combinations(tuple(omitted.values()), 2)
    }
    assert {frozenset(record[0]) for record in d3_records} == expected_zero_pairs

    expected_complete_faces = {
        (1, 2, 3), (1, 2, 4), (1, 2, 5),
        (1, 3, 4), (1, 3, 5), (1, 4, 5),
        (2, 3, 4), (2, 3, 5), (2, 4, 5),
    }

    puncture_records = []
    for zeros, ext8, plane8, complete8 in d3_records:
        assert {R.BLOCK_LABELS[b] for b in complete8} == expected_complete_faces

        missing_pair = next(pair for pair, e in omitted.items() if e not in zeros)
        drop_cycles = frozenset(packets[missing_pair])
        drop_positions = tuple(i for i, e in enumerate(ext8) if e in drop_cycles)
        assert len(drop_positions) == 2

        ext6 = tuple(e for i, e in enumerate(ext8) if i not in drop_positions)
        plane6_child = project_space(plane8, drop_positions)
        assert len(plane6_child) == 2
        d6, complete6 = canonical_deficiency(ext6, plane6_child)
        assert d6 == 2
        puncture_records.append((zeros, missing_pair, drop_positions, complete6))

    assert len(puncture_records) == 3

    print("PASS: Profile B three-rank-two exceptional geometry excluded")
    print("direction_triples_checked", 27)
    print("normalized_surviving_direction", directions)
    print("forced_nonzero_cycles", tuple(R.DESC[e] for e in six))
    print("omitted_pair_orientations", {
        pair: R.DESC[e] for pair, e in omitted.items()
    })
    print("zero_column_candidates", len(zero_candidates))
    print("zero_column_pairs", len(tuple(combinations(zero_candidates, 2))))
    print("source_deficiency_histogram", dict(sorted(deficiency_histogram.items())))
    print("source_d3_candidates", len(d3_records))
    print("forced_two_puncture_deficiency", 2)


if __name__ == "__main__":
    main()
