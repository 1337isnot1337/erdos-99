#!/usr/bin/env python3
"""Exact antitone-circulation certificates and a nonembedded finite regression.

No contact/train embedding, global optimality, or Level I conclusion is encoded.
The general proofs are in the associated report; enumeration is a regression.
"""

from fractions import Fraction as F
from itertools import combinations, product


def connected(edges, n):
    reached = {0}
    while True:
        nxt = reached | {v for e in edges if any(u in reached for u in e) for v in e}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


def antitone(edges):
    return not any(p < r and q < s for p, q in edges for r, s in edges)


def eliminate(edges, n):
    while n > 1:
        assert connected(edges, n)
        assert antitone(edges | {(q, p) for p, q in edges})
        p, q = next(e for e in sorted(edges) if e[1] == e[0] + 1)
        image = lambda j: j if j <= p else j - 1
        edges = {tuple(sorted((image(a), image(b)))) for a, b in edges if image(a) != image(b)}
        n -= 1


def main():
    couplings = trees = 0
    for n in range(2, 7):
        for masses in product(range(1, 4), repeat=n):
            prefix = [0]
            for mass in masses:
                prefix.append(prefix[-1] + mass)
            w = prefix[-1]
            a = [[max(0, min(prefix[p + 1], w - prefix[q]) - max(prefix[p], w - prefix[q + 1])) for q in range(n)] for p in range(n)]
            assert all(sum(row) == mass for row, mass in zip(a, masses))
            assert all(sum(a[p][q] for p in range(n)) == masses[q] for q in range(n))
            assert all(a[p][q] == a[q][p] for p in range(n) for q in range(n))
            assert antitone({(p, q) for p in range(n) for q in range(n) if a[p][q]})
            couplings += 1

        pairs = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(pairs)):
            edges = {e for k, e in enumerate(pairs) if mask & (1 << k)}
            if not antitone(edges | {(q, p) for p, q in edges}) or not connected(edges, n):
                continue
            assert len(edges) == n - 1
            eliminate(edges, n)
            trees += 1

    # Actual diameter packet with a coherent but nonembedded gap labelling.
    t = F(1, 10000)
    d = F(1000000)
    unit = lambda z: ((1 - z * z) / (1 + z * z), 2 * z / (1 + z * z))
    ratios = [F(6, 5), F(-13, 10), F(7, 5), F(-3, 2)]
    supports = [(0, 3), (1, 3), (1, 2), (0, 2)]
    r = [tuple(d * x for x in unit(q * t)) for q in ratios]
    pts, labels = [], []
    for vector, (p, q) in zip(r, supports):
        pts.extend([tuple(-x / 2 for x in vector), tuple(x / 2 for x in vector)])
        labels.extend([p, q])
    sq = lambda p, q: sum((x - y) ** 2 for x, y in zip(p, q))
    old = {(i, j): sq(pts[i], pts[j]) for i, j in combinations(range(8), 2)}
    assert min(old.values()) > 399
    assert max(old.values()) == d * d
    assert {ij for ij, value in old.items() if value == d * d} == {(2 * k, 2 * k + 1) for k in range(4)}
    coeffs = [vector[1] for vector in r]
    rows = [[c if p <= j < q else F(0) for j in range(3)] for (p, q), c in zip(supports, coeffs)]
    weight = [1 / abs(c) for c in coeffs]
    assert all(sum(w * row[j] for w, row in zip(weight, rows)) == 0 for j in range(3))
    # The determinant of the first three actual rows is nonzero.
    determinant = rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
    assert determinant != 0
    arrows = {(p, q) if c > 0 else (q, p) for (p, q), c in zip(supports, coeffs)}
    assert arrows == {(0, 3), (3, 1), (1, 2), (2, 0)}
    assert not antitone(arrows)
    changes = [(x - 1, y) for x, y in [unit(t), unit(-t), unit(t)]]
    displacements = [(F(0), F(0))]
    for x, y in changes:
        displacements.append((displacements[-1][0] + x, displacements[-1][1] + y))
    moved = [tuple(x + y for x, y in zip(p, displacements[j])) for p, j in zip(pts, labels)]
    new = {(i, j): sq(moved[i], moved[j]) for i, j in old}
    assert min(new.values()) > 399
    assert max(new.values()) < d * d
    margin = d * d - max(new.values())
    assert margin > F(239, 10000)
    # All new phases +/-2 arctan(t) lie between nearest original diameter
    # phases -2 arctan(13t/10) and +2 arctan(6t/5).
    assert F(-13, 10) < -1 < 0 < 1 < F(6, 5)
    # Circular order follows the exact rational angle parameters and antipodes.
    order = [1, 5, 6, 2, 0, 4, 7, 3]
    for a, b in zip(order, order[1:] + order[:1]):
        for v in range(8):
            cross = (pts[b][0] - pts[a][0]) * (pts[v][1] - pts[a][1]) - (pts[b][1] - pts[a][1]) * (pts[v][0] - pts[a][0])
            assert cross >= 0
    circular_labels = [labels[j] for j in order]
    assert circular_labels == [3, 2, 0, 1, 0, 1, 2, 3]
    mask = [label == 0 for label in circular_labels]
    assert sum(a != b for a, b in zip(mask, mask[1:] + mask[:1])) == 4
    print(f"PASS: {couplings} exact antitone couplings; {trees} connected support trees with complete adjacent elimination")
    print("PASS: 8-point rational diameter packet and strictly smaller moved diameter")
    print("Certified squared-diameter decrease > 239/10000; all squared pair distances > 399")
    print("Failure isolated: gap-0 vertices occupy two boundary arcs; no proper nested-cut embedding")

    geometric_pairs = 0
    for m in range(2, 9):
        for threshold in [False, True]:
            labels = list(range(m + 1)) + list(range(m - 1, 0, -1)) if threshold else list(range(m + 1)) + list(range(m, 0, -1))
            roles = [None if j == 0 or (threshold and j == m) else ("P" if i <= m else "N") for i, j in enumerate(labels)]
            edges = []
            for a, b in combinations(range(len(labels)), 2):
                if roles[a] is None and roles[b] is None:
                    continue
                if roles[a] is None:
                    tail, head = (a, b) if roles[b] == "P" else (b, a)
                elif roles[b] is None:
                    tail, head = (b, a) if roles[a] == "P" else (a, b)
                elif roles[a] == roles[b]:
                    continue
                else:
                    tail, head = (a, b) if roles[a] == "N" else (b, a)
                if labels[tail] != labels[head]:
                    edges.append((a, b, labels[tail], labels[head]))
            for a, b, p, q in edges:
                for c, e, r0, s in edges:
                    crosses = (a < c < b) != (a < e < b)
                    if len({a, b, c, e}) == 4 and not crosses:
                        continue
                    assert not (p < r0 and q < s)
                    geometric_pairs += 1
    print(f"PASS: {geometric_pairs} crossing/shared-endpoint ordered chord pairs, including one and two extreme mixed vertices")

    empty_pairs = 0
    for m in range(1, 7):
        # Duplicated labels test chords within one arc as well as across arcs.
        labels = [j for j in range(m + 1) for _ in range(2)] + [j for j in range(m, -1, -1) for _ in range(2)]
        empty = [(a, b, labels[a]) for a, b in combinations(range(len(labels)), 2) if labels[a] == labels[b]]
        for a, b, j in empty:
            for c, d0, k in empty:
                if j == k:
                    continue
                assert len({a, b, c, d0}) == 4
                assert (a < c < b) == (a < d0 < b)
                empty_pairs += 1
    print(f"PASS: {empty_pairs} distinct-layer empty-support chord pairs are disjoint and noncrossing")
    cos0, sin0 = unit(F(1, 5))
    parallel_change = (F(13) + cos0 - 1) ** 2 + sin0 ** 2 - F(13) ** 2
    assert parallel_change == 2 * (1 - 13) * (1 - cos0) < 0
    print("PASS: parallel zero-derivative diameter is not intrinsically stationary in the finite chart")


if __name__ == "__main__":
    main()
