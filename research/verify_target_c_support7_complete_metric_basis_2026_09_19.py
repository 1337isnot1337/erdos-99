#!/usr/bin/env python3
"""Exact cycle-space certificate for the universal support-seven metric basis.

For every labelled 2-regular missing graph on seven non-ground vertices, the
14-edge present relation graph is connected.  A spanning tree gives eight
present-edge fundamental cycles.  Adding one fundamental cycle for each of the
seven missing chords produces a rank-15 basis of the complete K7 cycle space.
"""
from fractions import Fraction
from itertools import combinations, permutations
from collections import deque

V = tuple(range(1, 8))
EDGES = tuple(combinations(V, 2))
EIDX = {e: i for i, e in enumerate(EDGES)}
ALL = set(EDGES)


def edge(a, b):
    return (a, b) if a < b else (b, a)


def cyc_edges(cycle):
    return frozenset(edge(cycle[i], cycle[(i + 1) % len(cycle)])
                     for i in range(len(cycle)))


def missing_graphs():
    out = set()
    for tail in permutations(V[1:]):
        out.add(cyc_edges((V[0],) + tail))
    for tri_tuple in combinations(V, 3):
        tri = set(tri_tuple)
        quad = set(V) - tri
        te = cyc_edges(tuple(sorted(tri)))
        q0 = min(quad)
        for tail in permutations(sorted(quad - {q0})):
            qe = cyc_edges((q0,) + tail)
            out.add(frozenset(set(te) | set(qe)))
    return tuple(out)


def spanning_tree(edges):
    adj = {v: [] for v in V}
    for a, b in sorted(edges):
        adj[a].append(b)
        adj[b].append(a)
    for v in V:
        adj[v].sort()
    root = V[0]
    parent = {root: None}
    q = deque([root])
    tree = set()
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w in parent:
                continue
            parent[w] = u
            tree.add(edge(u, w))
            q.append(w)
    assert len(parent) == len(V)
    assert len(tree) == len(V) - 1
    return tree


def tree_path(tree, start, end):
    adj = {v: [] for v in V}
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    parent = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        if u == end:
            break
        for w in adj[u]:
            if w not in parent:
                parent[w] = u
                q.append(w)
    assert end in parent
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def oriented_add(row, a, b, amount=Fraction(1)):
    e = edge(a, b)
    row[EIDX[e]] += amount if a < b else -amount


def fundamental_cycle_row(tree, chord):
    a, b = chord
    # chord a->b, then unique tree path b->a
    row = [Fraction(0) for _ in EDGES]
    oriented_add(row, a, b)
    path = tree_path(tree, b, a)
    for u, v in zip(path, path[1:]):
        oriented_add(row, u, v)
    return row


def rank(rows):
    a = [r[:] for r in rows]
    r = 0
    for c in range(len(EDGES)):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(len(a)):
            if i == r or not a[i][c]:
                continue
            z = a[i][c]
            a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


MISSING = missing_graphs()
assert len(MISSING) == 465
c7 = c34 = 0
for missing in MISSING:
    present = ALL - set(missing)
    assert len(present) == 14
    tree = spanning_tree(present)
    present_chords = sorted(present - tree)
    missing_chords = sorted(missing)
    assert len(present_chords) == 8
    assert len(missing_chords) == 7

    relation_rows = [fundamental_cycle_row(tree, e) for e in present_chords]
    missing_rows = [fundamental_cycle_row(tree, e) for e in missing_chords]
    assert rank(relation_rows) == 8
    assert rank(relation_rows + missing_rows) == 15

    # Classify the 2-regular missing graph by connectivity.
    adj = {v: set() for v in V}
    for a, b in missing:
        adj[a].add(b); adj[b].add(a)
    seen = set(); sizes = []
    for s in V:
        if s in seen:
            continue
        stack = [s]; seen.add(s); n = 0
        while stack:
            u = stack.pop(); n += 1
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        sizes.append(n)
    sizes = tuple(sorted(sizes))
    if sizes == (7,): c7 += 1
    elif sizes == (3, 4): c34 += 1
    else: raise AssertionError(sizes)

assert (c7, c34) == (360, 105)
print("PASS")
print("labelled missing graphs: 465 = 360 C7 + 105 C3+C4")
print("present-relation metric cycle basis: rank 8")
print("one missing-chord cycle per absent edge: +7 independent")
print("complete K7 metric cycle basis: rank 15")
