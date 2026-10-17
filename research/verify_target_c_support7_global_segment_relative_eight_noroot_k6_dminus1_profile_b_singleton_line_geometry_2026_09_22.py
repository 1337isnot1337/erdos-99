#!/usr/bin/env python3
"""Arithmetic certificate for the strengthened Profile B singleton-line geometry.

A rank-two coefficient plane P<=Q^8 with d1(P)>=4 has n=d2(P) nonzero
coordinate columns. Write their nonzero projective multiplicities as m_i.

For a rank-two local-empty compatible singleton block b, its singleton
constraint L_b is a nonzero codeword line of P. If b and c are distinct such
blocks, then supp(L_b) and supp(L_c) meet in at most TWO coordinates. Indeed,
when the root triples share two vertices, their only common no-root cycles are
the three orientations of the common four-set, and those give all three local
projective directions at b. The chosen singleton direction at b kills one of
those three orientations, so L_b is supported on at most two of them. If the
root triples do not share two vertices, they have no common touching cycle.

For non-generic codeword lines whose kernel directions are projective column
classes i,j, the support intersection therefore satisfies

    n - m_i - m_j <= 2,

or m_i+m_j >= n-2. A generic codeword line cannot coexist with a second
rank-two singleton line because its support meets every other nonzero codeword
in at least d1(P)>=4 coordinates. This script exhausts the integer projective
multiplicity profiles and checks the resulting count bounds.
"""

from itertools import combinations

VERTICES = tuple(range(1, 8))
ROOT_BLOCKS = tuple(combinations(VERTICES, 3))


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def max_rank_two_singleton_lines(n, multiplicities):
    """Largest projective-class subset with pairwise support intersection <=2."""
    h = len(multiplicities)
    best = 0
    for size in range(h + 1):
        for chosen in combinations(range(h), size):
            if all(
                multiplicities[i] + multiplicities[j] >= n - 2
                for i, j in combinations(chosen, 2)
            ):
                best = max(best, size)
    return best


def three_rank_two_root_geometry_check():
    """Classify triples of root blocks that are pairwise co-touchable.

    Positive pairwise coefficient-support intersections force each pair of
    root triples to share two vertices. There are exactly two incidence
    types: three faces of one four-set, or three triples with one common
    two-set. The first type cannot support the exceptional (2,2,2) profile,
    because all three block pairs are co-touched only on the same three
    four-cycle orientations, whereas the three coefficient-support
    intersections are disjoint two-sets.
    """
    candidates = []
    signatures = set()
    for blocks in combinations(ROOT_BLOCKS, 3):
        if not all(len(set(a) & set(b)) == 2 for a, b in combinations(blocks, 2)):
            continue
        common = set(blocks[0]) & set(blocks[1]) & set(blocks[2])
        union = set().union(*map(set, blocks))
        signature = (len(common), len(union))
        signatures.add(signature)
        candidates.append((blocks, signature))

    assert candidates
    assert signatures == {(1, 4), (2, 5)}

    # In the (1,4) type every pair has the same four-set union, hence the
    # same three possible common cycle orientations. Three disjoint pairwise
    # support intersections of size two would require six distinct cycles.
    for blocks, signature in candidates:
        pair_unions = {
            frozenset(set(a) | set(b)) for a, b in combinations(blocks, 2)
        }
        if signature == (1, 4):
            assert len(pair_unions) == 1
        else:
            assert len(pair_unions) == 3


def main():
    profiles = []
    for n in range(2, 9):
        for multiplicities in partitions(n):
            if len(multiplicities) < 2:
                continue
            d1 = n - max(multiplicities)
            if d1 < 4:
                continue
            rmax = max_rank_two_singleton_lines(n, multiplicities)
            profiles.append((8 - n, n, multiplicities, d1, rmax))

    three_rank_two_root_geometry_check()

    assert profiles
    assert len(profiles) == 28
    assert min(n for _z, n, _m, _d1, _r in profiles) == 5

    maxima = {
        n: max(r for _z, n0, _m, _d1, r in profiles if n0 == n)
        for n in range(5, 9)
    }
    assert maxima == {5: 1, 6: 3, 7: 2, 8: 2}

    # Three rank-two singleton blocks occur in exactly one integer projective
    # profile: two zero columns and three nonzero projective classes, each with
    # multiplicity two.
    three = [row for row in profiles if row[4] >= 3]
    assert three == [(2, 6, (2, 2, 2), 4, 3)]

    # Hence every nine-singleton Profile B source has at least six aligned
    # rank-one singleton blocks. Outside the unique n=6 profile above it has at
    # least seven, and when n=5 it has at least eight.
    aligned_minima = {n: 9 - maxima[n] for n in maxima}
    assert aligned_minima == {5: 8, 6: 6, 7: 7, 8: 7}

    print("PASS: strengthened Profile B singleton-line projective arithmetic")
    print("projective_profiles", len(profiles))
    print("minimum_d2", min(n for _z, n, _m, _d1, _r in profiles))
    print("max_rank_two_by_d2", maxima)
    print("minimum_aligned_by_d2", aligned_minima)
    print("unique_three_rank_two_profile", three[0])


if __name__ == "__main__":
    main()
