#!/usr/bin/env python3
"""Exact finite checks for the 2026-09-05 Target B phase-cut report.

Run: python3 research/phase_cut_certificate.py
Angles are rational multiples of pi; arithmetic uses fractions.Fraction.
Checks every cut interval for a finite direction graph, the sharp five-cycle
blow-up, and all balanced tripartite graphs with two vertices per class.
Encoded: direction/gain relations and finite graph constraints. Omitted: planar
rhombus realization, unit distances, KKT, global diameter optimality. Successful
checks certify these finite models only; the general PC/CR/PS proofs are in
docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md.
"""

from fractions import Fraction as Q
from itertools import combinations, product


def acyclic(n, edges):
    adjacency = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adjacency[u].append(v)
        degree[v] += 1
    pending = [v for v in range(n) if degree[v] == 0]
    count = 0
    while pending:
        u = pending.pop()
        count += 1
        for v in adjacency[u]:
            degree[v] -= 1
            if degree[v] == 0:
                pending.append(v)
    return count == n


def phase_cuts(directions, pairs):
    length = Q(1, 3)
    edges = []
    for u, v in pairs:
        step = (directions[v] - directions[u]) % 1
        if step > Q(1, 2):
            u, v = v, u
            step = 1 - step
        assert length < step <= Q(1, 2)
        edges.append((u, v, step - length))
    phases = [phi % length for phi in directions]
    endpoints = sorted(set(phases))
    integral = Q(0)
    smallest = len(edges)
    for index, left in enumerate(endpoints):
        right = endpoints[(index + 1) % len(endpoints)]
        if index == len(endpoints) - 1:
            right += length
        cut = ((left + right) / 2) % length
        lifted = [cut + (phase - cut) % length for phase in phases]
        labels = []
        for phi, x in zip(directions, lifted):
            label = (phi - x) / length
            assert label.denominator == 1
            labels.append(int(label) % 3)
        retained = []
        deleted = 0
        for u, v, defect in edges:
            difference = lifted[v] - lifted[u]
            if difference == defect:
                assert (labels[v] - labels[u]) % 3 == 1
                retained.append((u, v))
            else:
                assert difference == defect - length
                deleted += 1
        assert acyclic(len(directions), retained)
        integral += (right - left) * deleted
        smallest = min(smallest, deleted)
    defect_sum = sum((edge[2] for edge in edges), Q(0))
    assert integral == defect_sum
    assert smallest <= defect_sum // length
    return edges, smallest, defect_sum / length


def balanced_equality():
    classes = (range(2), range(2, 4), range(4, 6))
    pairs = [(u, v) for a, b in combinations(classes, 2) for u in a for v in b]
    equalities = 0
    for mask in range(1 << len(pairs)):
        edge_set = {edge for bit, edge in enumerate(pairs) if mask & (1 << bit)}
        if any(all(tuple(sorted(edge)) in edge_set for edge in combinations(triple, 2))
               for triple in product(*classes)):
            continue
        assert len(edge_set) <= 8
        if len(edge_set) != 8:
            continue
        equalities += 1
        assert any(all((u, v) in edge_set for u in a for v in b)
                   for a, b in combinations(classes, 2))
        colourings = []
        for colours in product(range(2), repeat=6):
            if all(((u, v) in edge_set) == (colours[u] != colours[v])
                   for u, v in pairs):
                colourings.append(colours)
        assert colourings
        for colours in colourings:
            assert sum(len({colours[v] for v in group}) == 2 for group in classes) <= 1
    witness = {(u, v) for u in classes[1] for v in classes[2]}
    witness |= {(0, v) for v in classes[2]} | {(1, v) for v in classes[1]}
    # Its connected bipartition is 3+3, but one of the nine cross pairs is absent.
    assert len(witness) == 8 and (0, 1) not in witness
    print(f"balanced m=2: all 4096 graphs checked; {equalities} equality graphs; EC verified")


def sliding_interval_regression(n=12, k=6):
    """Check the exact SI model and its maximum complete crossing product."""
    edges = {(j, i) for j in range(n) for i in range(j, min(n, j + k))}
    expected = k * n - k * (k - 1) // 2
    assert len(edges) == expected
    best = 0
    for b_count in range(1, n + 1):
        for chosen in __import__('itertools').combinations(range(n), b_count):
            common = set(range(n))
            for j in chosen:
                common &= {i for jj, i in edges if jj == j}
            best = max(best, b_count * len(common))
    assert best == (k + 1) ** 2 // 4
    print(f"sliding intervals N={n}, k={k}: edges={len(edges)}, max biclique product={best}")


def main():
    directions = [Q(i, 30) for i in range(30)]
    pairs = [(u, v) for u, v in combinations(range(30), 2)
             if Q(1, 3) < (directions[v] - directions[u]) < Q(2, 3)]
    edges, minimum, mean = phase_cuts(directions, pairs)
    print(f"30-direction model: edges={len(edges)}, minimum cut={minimum}, mean={mean}")
    for size in (1, 2):
        directions = [Q(i, 5) for i in range(5) for _ in range(size)]
        pairs = [(u, v) for u, v in combinations(range(5 * size), 2)
                 if (v // size - u // size) % 5 in (2, 3)]
        edges, minimum, mean = phase_cuts(directions, pairs)
        assert minimum == mean == size * size
        # Exhaustively exclude every smaller directed feedback set.
        oriented = [(u, v) for u, v, _ in edges]
        checked = 0
        for count in range(size * size):
            for removed in combinations(range(len(edges)), count):
                removed = set(removed)
                assert not acyclic(len(directions), [e for i, e in enumerate(oriented)
                                                    if i not in removed])
                checked += 1
        print(f"C5 blow-up s={size}: optimum={minimum}; {checked} smaller deletions excluded")
    balanced_equality()
    sliding_interval_regression()


if __name__ == "__main__":
    main()
