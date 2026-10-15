#!/usr/bin/env python3
"""Exact pentagon closure rows and finite sparse-graph elimination.

Two glued unit pentagons are genuine unit-separated positive-equilibrium
boundary-pinned packets, not certified loaded optima. Sparse graphs are
abstract endpoint ledgers. No asymptotic chart radius or diameter descent
is certified.
"""
from fractions import Fraction as F
from itertools import combinations

from verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05 import (
    add, cross, dot, mul, neg, rational, sign, sub, vsub,
)


def field_rank(rows, rad):
    rows = [[tuple(x) for x in row] for row in rows]
    if not rows:
        return 0
    pivot = 0
    for c in range(len(rows[0])):
        at = next((r for r in range(pivot, len(rows)) if rows[r][c] != rational(0)), None)
        if at is None:
            continue
        rows[pivot], rows[at] = rows[at], rows[pivot]
        a, b = rows[pivot][c]
        denominator = a*a-rad*b*b
        assert denominator != 0
        inverse = (a/denominator, -b/denominator)
        rows[pivot] = [mul(x, inverse, rad) for x in rows[pivot]]
        for r in range(len(rows)):
            if r != pivot and rows[r][c] != rational(0):
                coefficient = rows[r][c]
                rows[r] = [sub(x, mul(coefficient, y, rad))
                           for x, y in zip(rows[r], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def glued_pentagons(t):
    u, v = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    cb, rad = u-F(1, 2), 1-(u-F(1, 2))**2
    root = (F(0), F(1))
    pos = [(rational(0), rational(0)),
           (rational(u), rational(-v)),
           (rational(2*u), rational(0)),
           (rational(u+F(1, 2)), root),
           (rational(u-F(1, 2)), root)]
    pos += [(pos[i][0], sub(add(root, root), pos[i][1])) for i in range(3)]
    faces = [[0, 1, 2, 3, 4], [5, 4, 3, 7, 6]]
    contacts = {tuple(sorted((w[i], w[(i+1) % 5]))) for w in faces for i in range(5)}
    assert len(pos) == 8 and len(contacts) == 9
    for i, j in combinations(range(8), 2):
        distance2 = dot(vsub(pos[j], pos[i]), vsub(pos[j], pos[i]), rad)
        assert sign(sub(distance2, rational(1)), rad) >= 0
        assert (distance2 == rational(1)) == ((i, j) in contacts)
    for w in faces:
        vectors = [vsub(pos[w[(i+1) % 5]], pos[w[i]]) for i in range(5)]
        assert all(sign(cross(vectors[i], vectors[(i+1) % 5], rad), rad) > 0
                   for i in range(5))
        assert all(cross(a, b, rad) != rational(0) for a, b in combinations(vectors, 2))
    pins, free = {0, 1, 2, 5, 6, 7}, {3, 4}
    weights = {e: rational(2*cb if e == (3, 4) else 1) for e in contacts}
    assert all(sign(alpha, rad) > 0 for alpha in weights.values())
    for i in free:
        result = [rational(0), rational(0)]
        for e in contacts:
            if i in e:
                j = e[0] if e[1] == i else e[1]
                delta = vsub(pos[j], pos[i])
                result = [add(result[c], mul(weights[e], delta[c], rad)) for c in range(2)]
        assert result == [rational(0), rational(0)]
    trains = sorted(contacts)  # all nine trains are singleton edges
    index = {e: i for i, e in enumerate(trains)}
    closure = [[rational(0)]*len(trains) for _ in range(4)]
    for f, w in enumerate(faces):
        for i in range(5):
            a, b = w[i], w[(i+1) % 5]
            dx, dy = vsub(pos[b], pos[a])
            column = index[tuple(sorted((a, b)))]
            closure[2*f][column] = neg(dy)
            closure[2*f+1][column] = dx
    assert field_rank(closure, rad) == 4
    bar_rows = []
    for a, b in trains:
        delta = vsub(pos[b], pos[a])
        row = [rational(0)]*16
        for i, sg in ((a, -1), (b, 1)):
            row[2*i:2*i+2] = [mul(rational(sg), x, rad) for x in delta]
        bar_rows.append(row)
    assert field_rank(bar_rows, rad) == len(contacts)
    assert field_rank([[row[2*i+c] for i in sorted(free) for c in range(2)]
                       for row in bar_rows], rad) == 4
    assert 2*len(faces)-field_rank(closure, rad) == len(contacts)-field_rank(bar_rows, rad) == 0
    return 28


def sparse_peeling():
    graphs, orders = 0, 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        subsets = [(mask, mask.bit_count(), sum(1 << k for k, (a, b) in enumerate(pairs)
                                               if mask >> a & 1 and mask >> b & 1))
                   for mask in range(1, 1 << n)]
        for graph in range(1 << len(pairs)):
            if n >= 2 and graph.bit_count() > 2*n-3:
                continue
            if any(size >= 2 and (graph & inside).bit_count() > 2*size-3
                   for _, size, inside in subsets):
                continue
            adjacency = [set() for _ in range(n)]
            for k, (a, b) in enumerate(pairs):
                if graph >> k & 1:
                    adjacency[a].add(b)
                    adjacency[b].add(a)
            if any(len(ns) > 5 for ns in adjacency):
                continue
            graphs += 1
            for initially_fixed in (set(), {0}, set(range(0, n, 2))):
                remaining = set(range(n))-initially_fixed
                while remaining:
                    at = next((v for v in remaining if len(adjacency[v] & remaining) <= 3), None)
                    assert at is not None
                    # Complete pentagon valence is five, including all
                    # edges to fixed/outside nodes and missing outside ports.
                    assert 5-len(adjacency[at] & remaining) >= 2
                    remaining.remove(at)
                orders += 1
    return graphs, orders


if __name__ == "__main__":
    checks = sum(glued_pentagons(F(1, n)) for n in (5, 10, 20, 50, 100, 250, 1000, 10000))
    graphs, orders = sparse_peeling()
    print(f"PASS: {checks} exact source-pair checks in eight glued unit-pentagon packets")
    print("PASS: all hidden diagonals strict, nonparallel face sides and positive unloaded equilibrium")
    print("PASS: full pentagon closure row rank, pure-contact row independence and pinned interior rank")
    print(f"PASS: {graphs} (2,3)-sparse abstract endpoint graphs and {orders} complete two-anchor orders")
    print("SCOPE: boundary-pinned geometry and abstract graph cuts; no actual loaded optimum or uniform radius")
