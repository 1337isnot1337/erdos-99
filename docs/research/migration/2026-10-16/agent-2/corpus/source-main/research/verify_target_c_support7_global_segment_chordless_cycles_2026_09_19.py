#!/usr/bin/env python3
"""Exact finite certificate for chordless cycles of L(K8).

The reciprocal segment-order graph is the line graph L(K8). This verifier
checks the complete induced-cycle census using integer graph combinatorics only.
No floating-point arithmetic is used.
"""
from collections import Counter
from itertools import combinations
from math import factorial

V = tuple(range(8))
SEGMENTS = tuple(combinations(V, 2))
assert len(SEGMENTS) == 28


def common_endpoint(e, f):
    inter = set(e) & set(f)
    return next(iter(inter)) if len(inter) == 1 else None


NEIGHBORS = {e: set() for e in SEGMENTS}
for e, f in combinations(SEGMENTS, 2):
    if common_endpoint(e, f) is not None:
        NEIGHBORS[e].add(f)
        NEIGHBORS[f].add(e)
assert all(len(NEIGHBORS[e]) == 12 for e in SEGMENTS)


def connected(subset):
    subset = set(subset)
    todo = [next(iter(subset))]
    seen = set(todo)
    while todo:
        e = todo.pop()
        for f in NEIGHBORS[e] & subset:
            if f not in seen:
                seen.add(f)
                todo.append(f)
    return len(seen) == len(subset)


def is_induced_cycle(subset):
    subset = tuple(subset)
    return (
        len(subset) >= 3
        and all(
            sum(f in NEIGHBORS[e] for f in subset if f != e) == 2
            for e in subset
        )
        and connected(subset)
    )


# Exhaustively enumerate all induced cycles. The largest possible length is 8;
# for k>=4 each one corresponds to a simple k-cycle of the underlying K8.
counts = Counter()
cycles_by_length = {}
for k in range(3, 9):
    found = tuple(
        subset
        for subset in combinations(SEGMENTS, k)
        if is_induced_cycle(subset)
    )
    cycles_by_length[k] = found
    counts[k] = len(found)

assert counts == Counter({
    3: 336,
    4: 210,
    5: 672,
    6: 1680,
    7: 2880,
    8: 2520,
})

# For k>=4, compare the exhaustive line-graph census to the closed form for
# undirected labelled simple k-cycles in K8.
for k in range(4, 9):
    expected = factorial(8) // (2 * k * factorial(8 - k))
    assert counts[k] == expected
assert sum(counts[k] for k in range(4, 9)) == 7962

# Classify the 336 line-graph triangles: either three K8 edges incident to one
# common root, or the three sides of one K8 triangle.
star = 0
side = 0
for tri in cycles_by_length[3]:
    common = set(tri[0]) & set(tri[1]) & set(tri[2])
    if common:
        star += 1
    else:
        vertices = set().union(*map(set, tri))
        assert len(vertices) == 3
        side += 1
assert star == 8 * 35 == 280
assert side == 56

# Side triangles are the 56 triples {ab,bc,ca}; verify the classification
# against direct K8 triangle construction.
side_sets = {
    frozenset((tuple(sorted((a, b))), tuple(sorted((b, c))), tuple(sorted((a, c)))))
    for a, b, c in combinations(V, 3)
}
assert len(side_sets) == 56
assert side_sets == {
    frozenset(tri)
    for tri in cycles_by_length[3]
    if not (set(tri[0]) & set(tri[1]) & set(tri[2]))
}

# Nontrivial minimal strict metric-order templates: all 280 root-star triangles
# plus every induced cycle of length 4..8. The 56 side triangles compare the
# three ordinary opposite angles of one Euclidean triangle and are already
# order-tautological on the complete-angle system.
nontrivial = star + sum(counts[k] for k in range(4, 9))
assert nontrivial == 8242

# One explicit length-k representative for every k=4..8 is the K8 polygon
# 0-1-...-(k-1)-0. Check its edge set is present in the exhaustive induced list.
for k in range(4, 9):
    polygon = frozenset(
        tuple(sorted((i, (i + 1) % k)))
        for i in range(k)
    )
    assert polygon in {frozenset(c) for c in cycles_by_length[k]}

print("PASS: L(K8) chordless-cycle certificate")
print("induced-cycle counts:", dict(sorted(counts.items())))
print("triangle split: 280 root-star + 56 triangle-side")
print("cross-root simple cycles length 4..8:", sum(counts[k] for k in range(4, 9)))
print("nontrivial strict directed-cycle templates:", nontrivial)
