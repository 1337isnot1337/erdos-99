#!/usr/bin/env python3
"""Exact regression for geometric impossibility of a circulating gap multigraph.

Encoded: actual Euclidean diameter pairs, strictly convex diameter endpoints,
ordered topological layers, exact-phase interval rows, full column rank, positive
transverse circulation, positive axial cut resultants, nonzero two-bar reactions,
a common full-support diameter-star witness pair, and arbitrarily round hulls.
Omitted: actual unit-contact crosscuts, vertex KKT equilibrium, a positive contact
core, its scalar stress PSD/affine kernel, a transverse rhombus grid, quadratic
packing population, and global optimality. The positive diameter weights below
are cut-balance labels; they are NOT a KKT stress on these contact-free sets.
All certificates use integers/Fraction. Roundness is proved in the report.
"""

from fractions import Fraction as F
from itertools import combinations
from math import lcm


def distance2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def rank(rows):
    a = [list(map(F, row)) for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        ix = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if ix is None:
            continue
        a[pivot], a[ix] = a[ix], a[pivot]
        factor = a[pivot][col]
        a[pivot] = [x / factor for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def certify(points, layers, expected, m, weights=None):
    names = list(points)
    diam = max(distance2(points[a], points[b]) for a, b in combinations(names, 2))
    actual = {frozenset((a, b)) for a, b in combinations(names, 2)
              if distance2(points[a], points[b]) == diam}
    assert actual == {frozenset(e) for e in expected}
    # Make every coordinate an even integer. Distinct points are >=2 apart.
    scale = 2 * lcm(*(F(x).denominator for p in points.values() for x in p))
    minimum = min(distance2(points[a], points[b]) for a, b in combinations(names, 2))
    assert minimum * scale * scale >= 4
    assert len(set(points.values())) == len(points)
    rows, axial, gap, flux = [], [F(0)] * m, [], [F(0)] * (m + 1)
    weights = weights or [F(1)] * len(expected)
    for (a, b), beta in zip(expected, weights):
        if layers[a] > layers[b]:
            a, b = b, a
        p, q = layers[a], layers[b]
        assert p < q and beta > 0
        rx, ry = (points[b][i] - points[a][i] for i in (0, 1))
        assert ry
        row = [ry if p < i <= q else F(0) for i in range(1, m + 1)]
        rows.append(row)
        for i in range(m):
            axial[i] += beta * rx * (p < i + 1 <= q)
        flux[p] += beta * ry
        flux[q] -= beta * ry
        gap.append((p, q))
    assert not any(flux)
    assert rank(rows) == m
    assert all(x > 0 for x in axial)
    assert all(axial[i] != axial[i + 1] for i in range(m - 1))
    for pair in set(gap):
        signs = [rows[i][pair[0]] for i, e in enumerate(gap) if e == pair]
        assert min(signs) < 0 < max(signs)
    # Each expected diameter endpoint is uniquely exposed in its diameter direction.
    for a, b in expected:
        d = tuple(points[b][i] - points[a][i] for i in (0, 1))
        for z in names:
            if z != a:
                assert sum((points[z][i] - points[a][i]) * d[i] for i in (0, 1)) > 0
            if z != b:
                assert sum((points[z][i] - points[b][i]) * d[i] for i in (0, 1)) < 0
    return len(actual), scale.bit_length(), axial


def seven_point():
    p = {"v": (-33, 0), "x+": (30, 16), "x-": (30, -16),
         "l+": (-10, 30), "l-": (-10, -30),
         "r+": (15, 30), "r-": (15, -30)}
    p = {k: tuple(map(F, v)) for k, v in p.items()}
    layers = {k: (0 if k == "v" else 1 if k.startswith("l") else 2) for k in p}
    edges = [("v", "x+"), ("v", "x-"), ("l+", "r-"), ("l-", "r+")]
    count, _, axial = certify(p, layers, edges, 2)
    assert count == 4 and axial == [126, 176]
    print("PASS: seven-point actual-diameter regression; rank=2; axial=[126,176]")


def family(j):
    t = F(1, 100 * j)
    m = j + 1
    p = {"v": (F(-1), F(0))}
    layers = {"v": 0}
    for sign, tag in [(1, "+"), (-1, "-")]:
        p["X" + tag] = ((1 - 3 * t * t) / (1 + t * t),
                        sign * 4 * t / (1 + t * t))
        layers["X" + tag] = m
    edges = [("v", "X+"), ("v", "X-")]
    for k in range(1, j + 1):
        z = 5 * t + (1 - 5 * t) * F(k, j + 1)
        assert 5 * t < z < 1
        c, s = (1 - z * z) / (1 + z * z), 2 * z / (1 + z * z)
        for prefix, x, layer in [("L", -c, k), ("R", c, m)]:
            for sign, tag in [(1, "+"), (-1, "-")]:
                name = f"{prefix}{k}{tag}"
                p[name] = (x, sign * s)
                layers[name] = layer
        edges += [(f"L{k}+", f"R{k}-"), (f"L{k}-", f"R{k}+")]
        # Matching directions are strictly outside the common V witness cell.
        assert 2 * z / (1 - z * z) > 2 * t / (1 - t * t)
    count, scale_bits, _ = certify(p, layers, edges, m)
    assert count == 2 * m
    assert all(distance2(p[a], p[b]) == 4 for a, b in edges)
    print(f"PASS: J={j}; points={len(p)}; gap_vertices={m+1}; "
          f"diameters={count}; rank={m}; integer_scale_bits={scale_bits}")


if __name__ == "__main__":
    seven_point()
    for j in (1, 2, 4, 8, 16):
        family(j)
