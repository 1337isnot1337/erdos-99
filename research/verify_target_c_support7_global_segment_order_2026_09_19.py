#!/usr/bin/env python3
"""Exact finite certificate for the support-seven global segment-order layer.

The analytic distance/angle sign identity is proved in the companion note.
This verifier checks the K8 / line-graph bookkeeping with exact integer graph
combinatorics only. No floating-point arithmetic is used.
"""
from itertools import combinations
from collections import Counter, deque

V = tuple(range(8))
SEGMENTS = tuple(combinations(V, 2))
assert len(SEGMENTS) == 28
seg_index = {e: i for i, e in enumerate(SEGMENTS)}


def common_endpoint(e, f):
    inter = set(e) & set(f)
    return next(iter(inter)) if len(inter) == 1 else None


# L(K8): vertices are the 28 reciprocal segments, with adjacency precisely
# when two segments share one reciprocal endpoint.
ADJ = []
neighbors = {e: set() for e in SEGMENTS}
root_hist = Counter()
for e, f in combinations(SEGMENTS, 2):
    r = common_endpoint(e, f)
    if r is None:
        continue
    ADJ.append((e, f, r))
    neighbors[e].add(f)
    neighbors[f].add(e)
    root_hist[r] += 1

assert len(ADJ) == 168
assert root_hist == Counter({r: 21 for r in V})
assert all(len(neighbors[e]) == 12 for e in SEGMENTS)
assert sum(len(neighbors[e]) for e in SEGMENTS) // 2 == 168

# Connectedness and cycle rank.
seen = {SEGMENTS[0]}
q = deque([SEGMENTS[0]])
while q:
    e = q.popleft()
    for f in neighbors[e]:
        if f not in seen:
            seen.add(f)
            q.append(f)
assert len(seen) == 28
assert len(ADJ) - len(SEGMENTS) + 1 == 141

# Every adjacency is equivalently one root and one unordered pair among the
# seven other reciprocal points.
rooted = set()
for r in V:
    others = [v for v in V if v != r]
    for i, j in combinations(others, 2):
        e = tuple(sorted((r, i)))
        f = tuple(sorted((r, j)))
        rooted.add(tuple(sorted((e, f))))
assert len(rooted) == 8 * 21 == 168
assert rooted == {tuple(sorted((e, f))) for e, f, _ in ADJ}

# Triangles in L(K8) have exactly two forms: three K8 edges through one common
# vertex (star triangles), or the three sides of one K8 triangle.
line_triangles = []
for a, b, c in combinations(SEGMENTS, 3):
    if b in neighbors[a] and c in neighbors[a] and c in neighbors[b]:
        line_triangles.append((a, b, c))
assert len(line_triangles) == 336

star = 0
cycle = 0
for tri in line_triangles:
    common = set(tri[0]) & set(tri[1]) & set(tri[2])
    if common:
        star += 1
    else:
        vertices = set().union(*map(set, tri))
        assert len(vertices) == 3
        cycle += 1
assert star == 8 * 35 == 280
assert cycle == 56
assert star + cycle == 336

# The induced four-cycles are exactly the simple K8 four-cycles. A four-set
# has three cyclic orders up to reversal, hence 3*C(8,4)=210.
induced_c4 = []
for subset in combinations(SEGMENTS, 4):
    degree = {
        e: sum(f in neighbors[e] for f in subset if f != e)
        for e in subset
    }
    if all(d == 2 for d in degree.values()):
        induced_c4.append(subset)
assert len(induced_c4) == 3 * 70 == 210

# One explicit genuinely cross-root 4-cycle in the line graph. Consecutive
# comparisons occur at roots 0,2,3,1 respectively.
C4 = ((0, 1), (0, 2), (2, 3), (1, 3))
for e, f in zip(C4, C4[1:] + C4[:1]):
    assert f in neighbors[e]
assert [common_endpoint(e, f) for e, f in zip(C4, C4[1:] + C4[:1])] == [0, 2, 3, 1]

# Generic distinct segment lengths orient every L(K8) edge from shorter to
# longer, which is necessarily acyclic. Check the elementary topological fact
# on deterministic rank assignments: arbitrary global strict ranks induce no
# directed cycle. We use several algebraically distinct rankings rather than a
# numerical geometry sample.
def induced_digraph(rank):
    out = {e: set() for e in SEGMENTS}
    indeg = {e: 0 for e in SEGMENTS}
    for e, f, _ in ADJ:
        lo, hi = (e, f) if rank[e] < rank[f] else (f, e)
        out[lo].add(hi)
        indeg[hi] += 1
    return out, indeg


def acyclic(out, indeg):
    indeg = dict(indeg)
    q = deque([v for v in SEGMENTS if indeg[v] == 0])
    n = 0
    while q:
        v = q.popleft()
        n += 1
        for w in out[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    return n == len(SEGMENTS)

rankings = []
rankings.append({e: k for k, e in enumerate(SEGMENTS)})
rankings.append({e: 27 - k for k, e in enumerate(SEGMENTS)})
rankings.append({e: ((17 * k + 5) % 29) for k, e in enumerate(SEGMENTS)})
# The last modular map is injective on k=0,...,27 because 29 is prime.
assert all(len(set(r.values())) == 28 for r in rankings)
for rank in rankings:
    assert acyclic(*induced_digraph(rank))

print("PASS: support-seven global segment-order finite certificate")
print("reciprocal points / segments:", len(V), len(SEGMENTS))
print("L(K8) comparison edges / degree / cycle rank:", len(ADJ), 12, 141)
print("rooted comparisons:", len(rooted), "= 8 * C(7,2)")
print("line-graph triangles: 336 = 280 star + 56 K8-triangle")
print("induced cross-root four-cycles:", len(induced_c4))
print("explicit cross-root 4-cycle roots: 0,2,3,1")
