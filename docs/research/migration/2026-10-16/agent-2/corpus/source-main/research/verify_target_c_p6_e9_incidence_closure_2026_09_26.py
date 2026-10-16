#!/usr/bin/env python3
"""Exact finite certificate for the Johnson-graph lemma used in the p=6,e=9 closure.

Let G have as vertices the 35 tetrahedral supports (4-subsets of a 7-set), with
adjacency when two supports share a triangular face, equivalently when their
intersection has size 3. The closure note needs the fact that every 8-vertex
induced subgraph of G has at most 19 edges.

If an 8-set has maximum induced degree at most 4, it has at most 16 edges.
Otherwise choose a maximum-degree vertex. By S_7 transitivity we may fix it to
the first 4-subset. It has 12 neighbors and 22 nonneighbors in G. For each
possible degree d in {5,6,7}, enumerate all choices of d neighbors and 7-d
nonneighbors and maximize the induced edge count. This is only 204072 exact
integer cases.
"""
from itertools import combinations
from math import comb

SUPPORTS = tuple(combinations(range(7), 4))
assert len(SUPPORTS) == 35

ADJ = [[False] * 35 for _ in range(35)]
for i, a in enumerate(SUPPORTS):
    sa = set(a)
    for j in range(i + 1, 35):
        hit = len(sa.intersection(SUPPORTS[j])) == 3
        ADJ[i][j] = ADJ[j][i] = hit

CENTER = 0
NEIGHBORS = tuple(i for i in range(1, 35) if ADJ[CENTER][i])
NONNEIGHBORS = tuple(i for i in range(1, 35) if not ADJ[CENTER][i])
assert (len(NEIGHBORS), len(NONNEIGHBORS)) == (12, 22)

def edge_count(family):
    return sum(ADJ[u][v] for u, v in combinations(family, 2))

maxima = {}
case_count = 0
for d in (5, 6, 7):
    best = -1
    local_cases = 0
    for ns in combinations(NEIGHBORS, d):
        for xs in combinations(NONNEIGHBORS, 7 - d):
            local_cases += 1
            best = max(best, edge_count((CENTER,) + ns + xs))
    expected = comb(12, d) * comb(22, 7 - d)
    assert local_cases == expected
    maxima[d] = best
    case_count += local_cases

assert case_count == 204072, case_count
assert maxima == {5: 19, 6: 19, 7: 19}, maxima
assert 8 * 4 // 2 < 19

print("PASS: every eight distinct K7 tetrahedra have at most 19 shared-face pairs")
print("local_cases", case_count)
print("max_edges_by_fixed_center_degree", maxima)
