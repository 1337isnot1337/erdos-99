#!/usr/bin/env python3
"""Exact source regressions for the harmonic rail endpoint theorem.

Encoded: every pair distance, actual contacts/diameters, exact positive KKT
for the square, PSD affine-kernel stress, genuine horizontal cuts and rails.
The 2-by-1 grid has no positive-support stress: an unloaded middle rail vertex
forces its sole vertical contact weight to zero. No large-source enumeration,
global optimality, route promotion, or Level I conclusion is encoded.
"""

from fractions import Fraction as F
from itertools import combinations


def pair_sq(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def packet(points):
    distances = {e: pair_sq(points[e[0]], points[e[1]]) for e in combinations(range(len(points)), 2)}
    assert min(distances.values()) >= 1
    contacts = {e for e, d in distances.items() if d == 1}
    diameter_sq = max(distances.values())
    diameters = {e for e, d in distances.items() if d == diameter_sq}
    return contacts, diameters, diameter_sq


def components(n, edges):
    remaining, out = set(range(n)), []
    while remaining:
        reached = {min(remaining)}
        while True:
            nxt = reached | {v for e in edges if reached.intersection(e) for v in e}
            if nxt == reached:
                break
            reached = nxt
        out.append(reached)
        remaining -= reached
    return out


def main():
    square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    c, h, d2 = packet(square)
    assert c == {(0, 1), (1, 2), (2, 3), (0, 3)}
    assert h == {(0, 2), (1, 3)} and d2 == 2
    alpha, beta = {e: F(1, 2) for e in c}, {e: F(1, 2) for e in h}
    assert sum(beta.values()) == 1 and sum(alpha.values()) == d2
    omega = [[F(0) for _ in square] for _ in square]
    for edges, sign in ((alpha, 1), (beta, -1)):
        for (i, j), weight in edges.items():
            omega[i][i] += sign * weight
            omega[j][j] += sign * weight
            omega[i][j] -= sign * weight
            omega[j][i] -= sign * weight
    z = [1, -1, 1, -1]
    assert omega == [[F(1, 2) * a * b for b in z] for a in z]
    for values in ([F(1)] * 4, [p[0] for p in square], [p[1] for p in square]):
        assert all(sum(a * b for a, b in zip(row, values)) == 0 for row in omega)
    # Explicit PSD rank-one factor and independent 1,x,y prove kernel dimension 3.
    assert len({(p[0], p[1]) for p in square}) == 4
    cut = {(0, 1), (2, 3)}
    rails = components(4, c - cut)
    assert rails == [{0, 3}, {1, 2}]
    loaded = {i for e in h for i in e}
    reactions = [[F(0), F(0)] for _ in square]
    for (i, j), weight in beta.items():
        for k in range(2):
            force = weight * (square[i][k] - square[j][k])
            reactions[i][k] += force
            reactions[j][k] -= force
    for s in rails:
        ys = [square[i][1] for i in s]
        assert s <= loaded and max(ys) - min(ys) == 1
        assert sum(reactions[i][1] for i in s) == 0
        moment = sum(square[i][1] * reactions[i][1] for i in s)
        energy = sum(weight * (square[i][1] - square[j][1]) ** 2 for (i, j), weight in alpha.items() if i in s and j in s)
        assert moment == energy == F(1, 2)
    assert len(loaded) == 4 == 2 * (1 + 1)
    deficiency = len(loaded) - len(h)
    assert len(h) == 2 * 1 + 2 - deficiency

    rectangle = [(F(x), F(y)) for x in range(3) for y in range(2)]
    c, h, d2 = packet(rectangle)
    assert len(c) == 7 and d2 == 5
    assert h == {(0, 5), (1, 4)}
    horizontal = {e for e in c if rectangle[e[0]][1] == rectangle[e[1]][1]}
    rails = components(6, c - horizontal)
    assert rails == [{0, 1}, {2, 3}, {4, 5}]
    loaded = {i for e in h for i in e}
    assert not loaded.intersection(rails[1])
    for i in rails[1]:
        nonzero_y = [(e, rectangle[i][1] - rectangle[e[1] if e[0] == i else e[0]][1]) for e in c if i in e and rectangle[e[0]][1] != rectangle[e[1]][1]]
        assert len(nonzero_y) == 1 and abs(nonzero_y[0][1]) == 1
        assert nonzero_y[0][0] == (2, 3)
    print("PASS: square actual KKT, PSD stress, both rail widths and component moments; 2-by-1 grid forces a zero vertical multiplier")


if __name__ == "__main__":
    main()
