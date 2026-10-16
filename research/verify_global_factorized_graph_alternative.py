#!/usr/bin/env python3
"""Finite graph certificates plus a nonplanar improvement of an actual source."""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

from global_factorized_graph_alternative import graph_alternative
from verify_global_planarity_and_radius_barriers import sign_qsqrt5


def check_certificate(n, contacts, diameters, result):
    if result["kind"] == "abstract_improvement":
        z = result["z"]
        assert len(z) == n
        assert all(z[i] + z[j] >= 1 for i, j in contacts)
        assert all(z[i] + z[j] <= -1 for i, j in diameters)
    else:
        assert result["kind"] == "factorized_barrier"
        a, b = result["a"], result["b"]
        assert set(a) <= set(contacts) and set(b) <= set(diameters)
        assert all(w > 0 for w in list(a.values()) + list(b.values()))
        assert sum(a.values()) == sum(b.values()) == 1
        for i in range(n):
            assert sum(w for edge, w in a.items() if i in edge) == sum(
                w for edge, w in b.items() if i in edge)
        # Replay the supplied walk independently of the graph search.
        cycle = result["cycle"]
        assert cycle and len(cycle) % 2 == 0
        assert len(set(cycle)) == len(cycle)
        assert all(isinstance(s, int) and 0 <= s < 2 * n for s in cycle)
        occurrences = [Counter(), Counter()]
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            assert u % 2 != v % 2
            color = u % 2
            edge = tuple(sorted((u // 2, v // 2)))
            assert edge in (contacts if color == 0 else diameters)
            occurrences[color][edge] += 1
        length = len(cycle) // 2
        assert a == {e: F(k, length) for e, k in occurrences[0].items()}
        assert b == {e: F(k, length) for e, k in occurrences[1].items()}


def verify_corruption_controls():
    contacts = [(0, 1), (0, 3), (1, 2), (2, 3)]
    diameters = [(0, 2), (1, 3)]
    witness = graph_alternative(4, contacts, diameters)
    check_certificate(4, contacts, diameters, witness)
    bad_weight = deepcopy(witness)
    bad_weight["a"][next(iter(bad_weight["a"]))] += F(1, 2)
    bad_cycle = deepcopy(witness)
    bad_cycle["cycle"][0] = 8
    bad_kind = deepcopy(witness)
    bad_kind["kind"] = "unknown"
    directions = graph_alternative(3, [(0, 1)], [(1, 2)])
    check_certificate(3, [(0, 1)], [(1, 2)], directions)
    directions["z"] = [F(0)] * 3
    cases = [(4, contacts, diameters, bad) for bad in
             (bad_weight, bad_cycle, bad_kind)]
    cases.append((3, [(0, 1)], [(1, 2)], directions))
    for args in cases:
        try:
            check_certificate(*args)
        except AssertionError:
            continue
        raise AssertionError("Corrupted graph certificate was accepted")
    return len(cases)


def verify_graphs():
    counts = {"abstract_improvement": 0, "factorized_barrier": 0}
    # Every disjoint three-state edge labeling through five vertices.
    for n in range(2, 6):
        edges = list(combinations(range(n), 2))
        for labels in product(range(3), repeat=len(edges)):
            contacts = [e for e, label in zip(edges, labels) if label == 1]
            diameters = [e for e, label in zip(edges, labels) if label == 2]
            if not contacts or not diameters:
                continue
            result = graph_alternative(n, contacts, diameters)
            check_certificate(n, contacts, diameters, result)
            counts[result["kind"]] += 1
    return counts


def verify_actual_pentagon_center():
    pairs = list(combinations(range(6), 2))
    contacts = [(i, 5) for i in range(5)]
    diameters = sorted({tuple(sorted((i, (i + 2) % 5))) for i in range(5)})
    result = graph_alternative(6, contacts, diameters)
    check_certificate(6, contacts, diameters, result)
    assert result["kind"] == "abstract_improvement"
    assert result["z"] == [F(-1, 2)] * 5 + [F(3, 2)]
    # exp(lambda)=21/20. After unit normalization, the rim scales by (20/21)^2.
    rim_scale = sp.Rational(400, 441)
    old, new = {}, {}
    old_diameter_squared = (5 + sp.sqrt(5)) / 2
    for i, j in pairs:
        if j == 5:
            old[i, j] = new[i, j] = sp.Integer(1)
        else:
            difference = min(j - i, 5 - (j - i))
            old[i, j] = (5 + (-1 if difference == 1 else 1) * sp.sqrt(5)) / 2
            new[i, j] = sp.expand(rim_scale ** 2 * old[i, j])
        assert sign_qsqrt5(new[i, j] - 1) >= 0
        assert sign_qsqrt5(old_diameter_squared - new[i, j]) > 0
    old_d = sp.Matrix(6, 6, lambda i, j: 0 if i == j else old[tuple(sorted((i, j)))])
    new_d = sp.Matrix(6, 6, lambda i, j: 0 if i == j else new[tuple(sorted((i, j)))])
    centered = sp.eye(6) - sp.ones(6) / 6
    old_gram = -centered * old_d * centered / 2
    new_gram = -centered * new_d * centered / 2
    assert old_gram.rank() == 2
    assert new_gram.rank() == 3
    # The apex construction proves Euclidean realization in three dimensions.
    height_squared = 1 - rim_scale ** 2
    assert height_squared > 0
    assert height_squared + rim_scale ** 2 == 1
    return len(pairs)


def main():
    print(f"PASS: {verify_corruption_controls()} corrupted graph certificates rejected")
    counts = verify_graphs()
    print("PASS: exhaustive abstract graph certificates through 5 labels:", counts)
    pair_count = verify_actual_pentagon_center()
    print(f"PASS: all {pair_count} abstract endpoint pairs improve the actual "
          "pentagon-center source; centered Gram rank increases from 2 to 3")
    print("Scope: graph alternative and a planar-realizability regression, not Level I.")


if __name__ == "__main__":
    main()
