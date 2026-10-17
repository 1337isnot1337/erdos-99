#!/usr/bin/env python3
"""Exact graph certificate for generic support-seven H6 complete metric integrability.

Checks all 465 labelled 2-regular missing graphs on seven non-ground vertices.
The present relation graph always has cycle rank 8. Completing the seven missing
edges raises the cycle-space rank to 15, matching the 15 root-fan triangles
1-i-j-1 of K7.
"""
from fractions import Fraction
from itertools import combinations, permutations

V = tuple(range(1, 8))
EDGES = tuple(combinations(V, 2))
EIDX = {e: i for i, e in enumerate(EDGES)}


def edge(a, b):
    return (a, b) if a < b else (b, a)


def graph_rank(edges):
    """Return (cycle-space rank, component count)."""
    adj = {v: set() for v in V}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    components = 0
    for start in V:
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return len(edges) - len(V) + components, components


def canonical_cycle_edges(cycle):
    return frozenset(
        edge(cycle[i], cycle[(i + 1) % len(cycle)])
        for i in range(len(cycle))
    )


def missing_graphs():
    out = set()

    # Hamiltonian C7.
    for tail in permutations(V[1:]):
        out.add(canonical_cycle_edges((V[0],) + tail))

    # Disjoint C3 + C4.
    for tri in combinations(V, 3):
        tri = set(tri)
        quad = set(V) - tri
        tri_edges = canonical_cycle_edges(tuple(sorted(tri)))
        q0 = min(quad)
        for tail in permutations(sorted(quad - {q0})):
            quad_edges = canonical_cycle_edges((q0,) + tail)
            out.add(frozenset(set(tri_edges) | set(quad_edges)))

    return tuple(out)


def component_sizes(edges):
    adj = {v: set() for v in V}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    sizes = []
    for start in V:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        sizes.append(size)
    return tuple(sorted(sizes))


def oriented_edge(a, b):
    if a < b:
        return edge(a, b), 1
    return edge(a, b), -1


def cycle_row(cycle):
    row = [Fraction(0) for _ in EDGES]
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        e, sign = oriented_edge(a, b)
        row[EIDX[e]] += sign
    return row


def row_rank(rows):
    a = [row[:] for row in rows]
    rank = 0
    for col in range(len(EDGES)):
        pivot = next(
            (i for i in range(rank, len(a)) if a[i][col]),
            None,
        )
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = a[rank][col]
        a[rank] = [x / q for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


MISSING = missing_graphs()
assert len(MISSING) == 465
assert sum(component_sizes(m) == (7,) for m in MISSING) == 360
assert sum(component_sizes(m) == (3, 4) for m in MISSING) == 105

ALL_EDGES = set(EDGES)
for missing in MISSING:
    present = ALL_EDGES - set(missing)
    cycle_rank, components = graph_rank(present)
    assert len(present) == 14
    assert components == 1
    assert cycle_rank == 8

    full_rank, full_components = graph_rank(ALL_EDGES)
    assert full_components == 1
    assert full_rank == 15
    assert full_rank - cycle_rank == len(missing) == 7

# Star tree rooted at 1. Every non-tree edge ij, 2 <= i < j <= 7,
# gives the fundamental triangle 1-i-j-1.
FUNDAMENTAL = [
    cycle_row((1, i, j))
    for i, j in combinations(range(2, 8), 2)
]
assert len(FUNDAMENTAL) == 15
assert row_rank(FUNDAMENTAL) == 15

# Each row has the exact potential-difference form
#   g_1i + g_ij - g_1j = 0,
# so g_ij = g_1j - g_1i once the root-star values are fixed.
for i, j in combinations(range(2, 8), 2):
    row = cycle_row((1, i, j))
    assert row[EIDX[(1, i)]] == 1
    assert row[EIDX[(i, j)]] == 1
    assert row[EIDX[(1, j)]] == -1
    assert sum(x != 0 for x in row) == 3

print("PASS")
print("labelled missing graphs: 465 = 360 C7 + 105 C3+C4")
print("present relation cycle rank: 8")
print("complete K7 cycle rank: 15")
print("independent missing-edge metric conditions added: 7")
print("root-fan fundamental triangles: 15 rank 15")
