#!/usr/bin/env python3
"""Exact irredundancy witnesses for cross-root cycles in L(K8).

Each witness is eight strict total orders, one on the seven segments incident
to each reciprocal root.  Thus every root-star triangle is automatically
transitive.  The verifier checks that all 56 triangle-side triples are also
acyclic, while among all 7,962 simple K8 cycles of lengths 4..8 exactly one is
directed.  Representatives are supplied for lengths 4,5,6,7,8.

By relabelling K8, this proves individual irredundancy of every one of the
7,962 cross-root chordless-cycle templates under only local rooted total-order
consistency plus triangle-side acyclicity.
"""
from collections import Counter
from itertools import combinations, permutations

V = tuple(range(8))

# Orders are shortest-to-longest among the seven segments incident to root r;
# an entry a denotes segment {r,a}.  These were found by finite search, but the
# certificate below uses only the explicit orders and exact combinatorics.
WITNESSES = {
    4: {
        0: (7, 6, 5, 4, 2, 3, 1),
        1: (7, 6, 5, 4, 3, 0, 2),
        2: (7, 6, 5, 4, 0, 1, 3),
        3: (7, 6, 5, 4, 1, 2, 0),
        4: (7, 6, 5, 3, 2, 1, 0),
        5: (7, 6, 4, 3, 2, 1, 0),
        6: (7, 5, 4, 3, 2, 1, 0),
        7: (6, 5, 4, 3, 2, 1, 0),
    },
    5: {
        0: (7, 6, 5, 3, 2, 4, 1),
        1: (7, 6, 5, 4, 3, 0, 2),
        2: (7, 6, 5, 4, 0, 1, 3),
        3: (7, 6, 5, 1, 0, 2, 4),
        4: (7, 6, 5, 2, 1, 3, 0),
        5: (7, 6, 4, 3, 2, 1, 0),
        6: (7, 5, 4, 3, 2, 1, 0),
        7: (6, 5, 4, 3, 2, 1, 0),
    },
    6: {
        0: (7, 6, 4, 5, 1, 3, 2),
        1: (7, 6, 5, 4, 0, 2, 3),
        2: (7, 6, 5, 4, 1, 3, 0),
        3: (7, 6, 5, 2, 4, 1, 0),
        4: (7, 6, 2, 1, 0, 3, 5),
        5: (7, 6, 3, 2, 1, 4, 0),
        6: (7, 5, 4, 3, 2, 1, 0),
        7: (6, 5, 4, 3, 2, 1, 0),
    },
    7: {
        0: (7, 5, 4, 6, 1, 3, 2),
        1: (7, 6, 5, 4, 3, 0, 2),
        2: (7, 6, 5, 4, 1, 3, 0),
        3: (7, 6, 5, 1, 2, 4, 0),
        4: (7, 6, 2, 1, 0, 3, 5),
        5: (7, 3, 2, 1, 0, 4, 6),
        6: (7, 4, 3, 2, 1, 5, 0),
        7: (6, 5, 4, 3, 2, 1, 0),
    },
    8: {
        0: (6, 5, 4, 7, 1, 3, 2),
        1: (7, 6, 5, 4, 3, 0, 2),
        2: (7, 6, 5, 4, 1, 3, 0),
        3: (7, 6, 5, 1, 2, 4, 0),
        4: (7, 6, 2, 1, 0, 3, 5),
        5: (7, 3, 2, 1, 0, 4, 6),
        6: (4, 3, 2, 1, 0, 5, 7),
        7: (5, 4, 3, 2, 1, 6, 0),
    },
}


def shorter(orders, root, a, b):
    """Whether segment {root,a} precedes {root,b} in the root order."""
    return orders[root].index(a) < orders[root].index(b)


def directed_cycle_sign(orders, cyc):
    """Return +1/-1 for either directed orientation, else 0."""
    k = len(cyc)
    forward = all(
        shorter(orders, cyc[i], cyc[i - 1], cyc[(i + 1) % k])
        for i in range(k)
    )
    reverse = all(
        shorter(orders, cyc[i], cyc[(i + 1) % k], cyc[i - 1])
        for i in range(k)
    )
    assert not (forward and reverse)
    return 1 if forward else -1 if reverse else 0


def canonical_cycles(k):
    """All undirected labelled simple k-cycles of K8, once each."""
    out = set()
    for subset in combinations(V, k):
        anchor = min(subset)
        rest = tuple(v for v in subset if v != anchor)
        for perm in permutations(rest):
            seq = (anchor,) + perm
            rev = (anchor,) + tuple(reversed(perm))
            out.add(min(seq, rev))
    return tuple(sorted(out))


def edge_set(cyc):
    k = len(cyc)
    return frozenset(
        tuple(sorted((cyc[i], cyc[(i + 1) % k])))
        for i in range(k)
    )


CYCLES = {k: canonical_cycles(k) for k in range(4, 9)}
assert {k: len(v) for k, v in CYCLES.items()} == {
    4: 210,
    5: 672,
    6: 1680,
    7: 2880,
    8: 2520,
}
assert sum(map(len, CYCLES.values())) == 7962

summary = Counter()
for target_k, orders in sorted(WITNESSES.items()):
    # Each root really carries a strict total order on exactly the other seven
    # vertices.  Hence all 280 root-star triangles are automatically acyclic.
    for root in V:
        assert len(orders[root]) == 7
        assert set(orders[root]) == set(V) - {root}

    # Triangle-side triples correspond to the three segments ab,bc,ca.  Their
    # comparison cycle is exactly the K8 vertex cycle (a,b,c).
    directed_side = 0
    for a, b, c in combinations(V, 3):
        directed_side += bool(directed_cycle_sign(orders, (a, b, c)))
    assert directed_side == 0

    directed = []
    by_length = Counter()
    for k in range(4, 9):
        for cyc in CYCLES[k]:
            sign = directed_cycle_sign(orders, cyc)
            if sign:
                directed.append((k, cyc, sign))
                by_length[k] += 1

    assert len(directed) == 1, (target_k, directed)
    k, cyc, sign = directed[0]
    assert k == target_k
    assert sign == 1
    assert edge_set(cyc) == edge_set(tuple(range(target_k)))
    assert by_length == Counter({target_k: 1})
    summary[target_k] = 1

assert summary == Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1})

print("PASS: cross-root L(K8) cycle templates are individually irredundant")
print("simple cycle counts:", {k: len(CYCLES[k]) for k in range(4, 9)})
print("total cross-root templates:", sum(len(CYCLES[k]) for k in range(4, 9)))
print("representative unique directed cycles:", dict(sorted(summary.items())))
print("all witnesses: 280 root-star triangles transitive, 56 side triangles acyclic")
