#!/usr/bin/env python3
"""Exact graph checks for the support-seven reciprocal collinearity classification."""

from itertools import combinations


def edge(a, b):
    return tuple(sorted((a, b)))


def graph_from_cycles(cycles):
    missing = set()
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            missing.add(edge(a, b))
    relation = set(combinations(range(7), 2)) - missing
    return relation, missing


TYPES = {
    "C7": [list(range(7))],
    "C3+C4": [[0, 1, 2], [3, 4, 5, 6]],
}

expected = {
    "C7": {3: 7, 4: 0, 5: 0},
    "C3+C4": {3: 5, 4: 1, 5: 0},
}

for name, cycles in TYPES.items():
    relation, missing = graph_from_cycles(cycles)
    assert len(relation) == 14
    assert len(missing) == 7

    good = {}
    for size in (3, 4, 5):
        sets = []
        for vertices in combinations(range(7), size):
            max_relation_degree = max(
                sum(edge(v, w) in relation for w in vertices if w != v)
                for v in vertices
            )
            if max_relation_degree <= 1:
                sets.append(vertices)
        good[size] = sets
        assert len(sets) == expected[name][size], (name, size, sets)

    if name == "C7":
        canonical = {
            tuple(sorted(((i - 1) % 7, i, (i + 1) % 7)))
            for i in range(7)
        }
        assert set(good[3]) == canonical
    else:
        assert (0, 1, 2) in good[3]
        c4_triples = {
            tuple(sorted(s))
            for s in ((3, 4, 5), (4, 5, 6), (5, 6, 3), (6, 3, 4))
        }
        assert set(good[3]) == {(0, 1, 2)} | c4_triples
        assert good[4] == [(3, 4, 5, 6)]

    # A non-ground set collinear with y_0 must be relation-independent, so its
    # induced missing graph is complete.
    radial = {}
    for size in (2, 3, 4):
        sets = []
        for vertices in combinations(range(7), size):
            if all(edge(a, b) in missing for a, b in combinations(vertices, 2)):
                sets.append(vertices)
        radial[size] = sets

    assert len(radial[4]) == 0
    if name == "C7":
        assert len(radial[3]) == 0
        assert len(radial[2]) == 7
    else:
        assert radial[3] == [(0, 1, 2)]
        assert len(radial[2]) == 7

print("PASS: support-seven reciprocal collinearity classification")
print("C7: 7 possible non-ground collinear triples, no collinear four-set")
print("C3+C4: 5 possible triples, unique possible four-set = missing C4")
print("radial through ground: size <= 3; size 3 only on missing C3")
