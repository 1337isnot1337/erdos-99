#!/usr/bin/env python3
"""Exact regression and finite checks for the signed gap-circulation reduction.

Encodes interval rows, positive row dependence, full rank, cut orientations,
and an actual rational five-point diameter star.  The star has assigned gap
labels, not a realized contact/train system.  Neither the checks nor the star
assert a global minimizer, a full source KKT stress, or C-II closure.
"""

from fractions import Fraction as F
from itertools import combinations, product


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        hit = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if hit is None:
            continue
        a[pivot], a[hit] = a[hit], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def check_packet(m, edges, flow):
    """edges are (gap p, gap q, nonzero coefficient c), p < q."""
    rows = [[c if p <= i < q else F(0) for i in range(m)] for p, q, c in edges]
    weights = [f / abs(c) for (_, _, c), f in zip(edges, flow)]
    assert all(w > 0 for w in weights)
    assert all(sum(w * row[i] for w, row in zip(weights, rows)) == 0 for i in range(m))
    assert rank(rows) == m
    for mask in range(1, (1 << (m + 1)) - 1):
        crossing = []
        for p, q, c in edges:
            ip, iq = bool(mask & (1 << p)), bool(mask & (1 << q))
            if ip != iq:
                crossing.append((1 if ip else -1) * c)
        assert any(x > 0 for x in crossing)
        assert any(x < 0 for x in crossing)
    assert len(edges) >= m + 1
    return (1 << (m + 1)) - 2


def main():
    packets = cuts = 0
    # Connected positive circuits with every possible cyclic vertex order.
    # A doubled path and doubled star also test multigraph two-cycles.
    from itertools import permutations

    for m in range(1, 6):
        for order in permutations(range(1, m + 1)):
            cycle = (0,) + order + (0,)
            edges = []
            for k, (tail, head) in enumerate(zip(cycle, cycle[1:])):
                p, q = sorted((tail, head))
                c = F(k + 1) * (1 if tail < head else -1)
                edges.append((p, q, c))
            cuts += check_packet(m, edges, [F(1)] * len(edges))
            packets += 1
        for base in [[(j - 1, j) for j in range(1, m + 1)], [(0, j) for j in range(1, m + 1)]]:
            edges = [(p, q, F(sign * (k + 1))) for k, (p, q) in enumerate(base) for sign in [-1, 1]]
            cuts += check_packet(m, edges, [F(1)] * len(edges))
            packets += 1

    # A diameter-13 geometric thrackle: all four actual diameter bars share 0.
    pts = [(F(0), F(0)), (F(12), F(5)), (F(12), F(-5)), (F(63, 5), F(16, 5)), (F(63, 5), F(-16, 5))]
    distances = {(i, j): sum((x - y) ** 2 for x, y in zip(pts[i], pts[j])) for i, j in combinations(range(5), 2)}
    assert min(distances.values()) == F(18, 5) > 1
    assert max(distances.values()) == 169
    actual = {ij for ij, d2 in distances.items() if d2 == 169}
    assert actual == {(0, j) for j in range(1, 5)}
    # Labels: root in 0, first symmetric leaf pair in 1, second in 2.
    edges = [(0, 1, F(5)), (0, 1, F(-5)), (0, 2, F(16, 5)), (0, 2, F(-16, 5))]
    cuts += check_packet(2, edges, [F(5, 4), F(5, 4), F(4, 5), F(4, 5)])
    packets += 1
    rows = [[c if p <= i < q else F(0) for i in range(2)] for p, q, c in edges]
    assert rank(rows) == 2
    # A_1 = 123/10, A_2 = 63/10, so the internal axial reaction is 6u.
    a1 = sum(pts[j][0] / 4 for j in range(1, 5))
    a2 = sum(pts[j][0] / 4 for j in range(3, 5))
    assert (a1, a2, a1 - a2) == (F(123, 10), F(63, 10), F(6))
    # The basis rows +5*[1,0] and +(16/5)*[1,1] have private leaf 1.
    # Shortening its basis edge necessarily lengthens the opposite parallel row.
    theta = (F(-1), F(1))
    derivatives = [sum(x * y for x, y in zip(row, theta)) for row in rows]
    assert derivatives == [F(-5), F(5), F(0), F(0)]
    for theta in product(range(-3, 4), repeat=2):
        if theta != (0, 0):
            assert max(sum(x * y for x, y in zip(row, theta)) for row in rows) > 0
    print(f"PASS: {packets} exact positive-circulation packets; {cuts} proper cuts")
    print("PASS: rational diameter star, full row rank, positive axial reaction, leaf-release obstruction")
    print("Scope: assigned interval labels only; no contact/train embedding or global-optimality certificate")


if __name__ == "__main__":
    main()
