#!/usr/bin/env python3
"""Finite regression for the minimal K5 reciprocal exclusion.

The proof in target_c_minimal_k5_reciprocal_exclusion_2026-09-18.md is analytic.
This script checks the finite sign-graph step only: after local raw-ray alternation at
the five non-ground vertices of a cyclically labelled convex hexagon, exactly two
undirected sign graphs remain. They are complements, with 6 and 9 edges; the 6-edge
graph is C3 disjoint union C3. In particular no 7-edge sign graph survives.
"""

from itertools import combinations

V = tuple(range(6))
EDGES = tuple(combinations(V, 2))


def incident_neighbors(mask: int, i: int) -> set[int]:
    out: set[int] = set()
    for bit, (a, b) in enumerate(EDGES):
        if not (mask >> bit) & 1:
            continue
        if a == i:
            out.add(b)
        elif b == i:
            out.add(a)
    return out


def permitted_local_set(i: int, nbrs: set[int]) -> bool:
    degree_two = {(i - 2) % 6, (i + 2) % 6}
    degree_three = {(i - 1) % 6, (i + 1) % 6, (i + 3) % 6}
    return nbrs == degree_two or nbrs == degree_three


survivors: list[int] = []
for mask in range(1 << len(EDGES)):
    if all(permitted_local_set(i, incident_neighbors(mask, i)) for i in range(1, 6)):
        # The convex-hexagon theorem also gives a 2+3 split at the ground vertex.
        if len(incident_neighbors(mask, 0)) in (2, 3):
            survivors.append(mask)

assert len(survivors) == 2, survivors
counts = sorted(mask.bit_count() for mask in survivors)
assert counts == [6, 9], counts
assert survivors[0] ^ survivors[1] == (1 << len(EDGES)) - 1

six = next(mask for mask in survivors if mask.bit_count() == 6)
six_edges = {EDGES[bit] for bit in range(len(EDGES)) if (six >> bit) & 1}
expected = {
    (0, 2), (2, 4), (0, 4),
    (1, 3), (3, 5), (1, 5),
}
assert six_edges == expected, (six_edges, expected)

# Explicitly confirm that the old 7+8 branch has no survivor.
assert all(mask.bit_count() != 7 for mask in survivors)

print("PASS")
print("surviving edge counts:", counts)
print("6-edge survivor:", sorted(six_edges))
print("9-edge survivor is its complement")
