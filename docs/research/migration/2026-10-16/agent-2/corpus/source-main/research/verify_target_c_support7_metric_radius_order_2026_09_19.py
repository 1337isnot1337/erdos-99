#!/usr/bin/env python3
"""Finite certificate for the seven-radius total-preorder layer.

The analytic input is proved in the companion note:

    sgn(A_ij - A_ji) = sgn(rho_j - rho_i).

This script checks only the finite weak-order combinatorics.  It uses exact
integer arithmetic and exhaustive enumeration; no floating point is used.
"""

from collections import Counter
from itertools import permutations, product
from math import factorial

N = 7


def sgn(x):
    return (x > 0) - (x < 0)


def canonical_rank_vector(ranks):
    """True iff used ranks are exactly 0,...,m-1 for some m."""
    levels = sorted(set(ranks))
    return levels == list(range(len(levels)))


def pair_signs(ranks):
    """D_ij sign for i<j when rank increases with reciprocal radius."""
    return tuple(
        sgn(ranks[j] - ranks[i])
        for i in range(N)
        for j in range(i + 1, N)
    )


WEAK = tuple(
    ranks
    for ranks in product(range(N), repeat=N)
    if canonical_rank_vector(ranks)
)
assert len(WEAK) == 47293
assert len({pair_signs(r) for r in WEAK}) == len(WEAK)

BY_LEVELS = Counter(len(set(r)) for r in WEAK)
assert BY_LEVELS == Counter({
    1: 1,
    2: 126,
    3: 1806,
    4: 8400,
    5: 16800,
    6: 15120,
    7: 5040,
})

STRICT = tuple(r for r in WEAK if len(set(r)) == N)
assert len(STRICT) == 5040
assert len(STRICT) == len(tuple(permutations(range(N))))


def one_linear_extension(ranks):
    """A deterministic strict total order extending one weak radius order."""
    return tuple(sorted(range(N), key=lambda i: (ranks[i], i)))


# Every weak order lies in at least one closed total-order cone.  Sorting first
# by weak rank and then by label supplies a linear extension.  The exact number
# of extensions is the product of factorials of equal-radius block sizes.
extension_histogram = Counter()
for ranks in WEAK:
    perm = one_linear_extension(ranks)
    assert all(
        ranks[perm[a]] <= ranks[perm[b]]
        for a in range(N)
        for b in range(a + 1, N)
    )
    expected = 1
    counts = Counter(ranks)
    for size in counts.values():
        expected *= factorial(size)
    assert expected >= 1
    extension_histogram[expected] += 1


# Local three-label restrictions are exactly the 13 weak orders on three
# labelled elements.  Strict restrictions have 6 transitive tournaments, not
# either of the two directed 3-cycles.
LOCAL = {
    tuple(
        sgn(r[j] - r[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    for r in product(range(3), repeat=3)
    if canonical_rank_vector(r)
}
assert len(LOCAL) == 13
STRICT_LOCAL = {p for p in LOCAL if 0 not in p}
assert len(STRICT_LOCAL) == 6
assert (1, -1, 1) not in STRICT_LOCAL
assert (-1, 1, -1) not in STRICT_LOCAL

print("PASS: seven-radius weak-order combinatorics")
print("weak orders:", len(WEAK))
print("strict total orders:", len(STRICT))
print("by number of radius levels:", dict(sorted(BY_LEVELS.items())))
print("local three-label weak orders:", len(LOCAL))
