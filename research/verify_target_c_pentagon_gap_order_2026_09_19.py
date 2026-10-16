#!/usr/bin/env python3
"""Exact combinatorial certificate for physical equilateral-pentagon gap orders.

The analytic input, proved in the companion note from the force-closure cosine
identities, is the cyclic sign/equality relation

    sgn(x[k+1]-x[k-1]) = sgn(x[k+3]-x[k+2])       (mod 5).

This script performs the finite part only.  It uses integers and exhaustive
enumeration, with no floating point arithmetic or optimization.
"""
from itertools import permutations, product
from collections import Counter

N = 5


def sgn(a):
    return (a > 0) - (a < 0)


def relation_holds(ranks):
    """ranks[i] is the weak rank of x_i; equal ranks mean equal gaps."""
    for k in range(N):
        lhs = sgn(ranks[(k + 1) % N] - ranks[(k - 1) % N])
        rhs = sgn(ranks[(k + 3) % N] - ranks[(k + 2) % N])
        if lhs != rhs:
            return False
    return True


def rank_vector_from_increasing_order(order):
    ranks = [None] * N
    for r, i in enumerate(order):
        ranks[i] = r
    return tuple(ranks)


# Strict case: all 5! possible gap orders.
STRICT = []
for order in permutations(range(N)):
    ranks = rank_vector_from_increasing_order(order)
    if relation_holds(ranks):
        STRICT.append(order)

EXPECTED_STRICT = [
    (0, 2, 3, 4, 1),
    (0, 3, 2, 1, 4),
    (1, 3, 4, 0, 2),
    (1, 4, 3, 2, 0),
    (2, 0, 4, 3, 1),
    (2, 4, 0, 1, 3),
    (3, 0, 1, 2, 4),
    (3, 1, 0, 4, 2),
    (4, 1, 2, 3, 0),
    (4, 2, 1, 0, 3),
]
assert STRICT == EXPECTED_STRICT
assert len(STRICT) == 10


def transform_index(i, shift, reflected):
    return (shift - i) % N if reflected else (shift + i) % N


def transform_order(order, shift, reflected):
    return tuple(transform_index(i, shift, reflected) for i in order)


# The ten strict orders are one full dihedral orbit.  A canonical representative
# has cyclic rank vector (0,4,1,2,3), i.e. ranks 1,5,2,3,4 around the pentagon.
base = STRICT[0]
dihedral_orbit = {
    transform_order(base, shift, reflected)
    for shift in range(N)
    for reflected in (False, True)
}
assert len(dihedral_orbit) == 10
assert dihedral_orbit == set(STRICT)
canonical_ranks = rank_vector_from_increasing_order(base)
assert canonical_ranks == (0, 4, 1, 2, 3)

# In every strict admissible order, the minimum and maximum positions are cyclic
# neighbors.  This is a convenient invariant form of the classification.
for order in STRICT:
    imin, imax = order[0], order[-1]
    assert (imin - imax) % N in (1, N - 1)


# Weak orders.  Enumerate every ordered set partition by surjective rank vectors
# 0,...,m-1.  There are 541 total weak orders on five labelled entries; only 21
# satisfy all five sign/equality relations.
WEAK = []
ALL_WEAK = []
for ranks in product(range(N), repeat=N):
    levels = sorted(set(ranks))
    if levels != list(range(len(levels))):
        continue
    ALL_WEAK.append(ranks)
    if relation_holds(ranks):
        WEAK.append(ranks)
assert len(ALL_WEAK) == 541
assert len(WEAK) == 21
assert Counter(len(set(r)) for r in WEAK) == Counter({5: 10, 3: 10, 1: 1})

# No physical weak order with exactly 2 or 4 distinct levels survives the sign
# relations.  Every nonregular equality case has two equal pairs and one singleton.
THREE_LEVEL = [r for r in WEAK if len(set(r)) == 3]
assert len(THREE_LEVEL) == 10
for r in THREE_LEVEL:
    counts = sorted(Counter(r).values())
    assert counts == [1, 2, 2]
    singleton_rank = next(level for level, c in Counter(r).items() if c == 1)
    assert singleton_rank in (0, 2)  # the singleton is the minimum or maximum

# The ten three-level patterns split into the two five-element dihedral orbits
# "singleton minimum" and "singleton maximum".
def transform_ranks(ranks, shift, reflected):
    out = [None] * N
    for i, rank in enumerate(ranks):
        out[transform_index(i, shift, reflected)] = rank
    return tuple(out)

three_min = tuple(r for r in THREE_LEVEL if Counter(r)[0] == 1)[0]
three_max = tuple(r for r in THREE_LEVEL if Counter(r)[2] == 1)[0]
orb_min = {transform_ranks(three_min, s, q) for s in range(N) for q in (False, True)}
orb_max = {transform_ranks(three_max, s, q) for s in range(N) for q in (False, True)}
assert len(orb_min) == len(orb_max) == 5
assert orb_min.isdisjoint(orb_max)
assert orb_min | orb_max == set(THREE_LEVEL)

# Closed-cone coverage: every weak admissible rank pattern is a coarsening of at
# least one of the ten strict orders.  Therefore the union of the closures of the
# ten strict permutation cones covers all equality cases too.
for ranks in WEAK:
    extensions = []
    for order in STRICT:
        seq = [ranks[i] for i in order]
        if all(a <= b for a, b in zip(seq, seq[1:])):
            extensions.append(order)
    assert extensions, ranks

# Canonical three-level representatives can be chosen as
#   T < B=D < A=E   and   A=E < B=D < T,
# corresponding to rank vectors below in cyclic coordinates (T,A,B,D,E).
assert (0, 2, 1, 1, 2) in THREE_LEVEL
assert (2, 0, 1, 1, 0) in THREE_LEVEL

print("PASS: physical pentagon gap-order finite classification")
print("strict orders: 10 = one D5 orbit")
print("weak admissible orders: 21 = 10 strict + 10 three-level + 1 regular")
print("equality cases: only 1, 3, or 5 distinct gap levels; three-level multiplicities 1+2+2")
