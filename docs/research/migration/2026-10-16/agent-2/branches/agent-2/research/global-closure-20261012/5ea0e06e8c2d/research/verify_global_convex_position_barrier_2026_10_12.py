#!/usr/bin/env python3
"""Exact controls for an analytical global convex-position barrier.

No globality oracle. Rational orientation signs certify convex subsets; the
heptagon replacement uses rational x and rational coefficients of sqrt(3).
"""

from fractions import Fraction as F
from itertools import combinations
import json
import sympy as sp


def sub(p, q):
    return tuple(x-y for x, y in zip(p, q))


def det(p, q):
    return p[0]*q[1]-p[1]*q[0]


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower, upper = [], []
    for bank, sequence in ((lower, points), (upper, points[::-1])):
        for p in sequence:
            while len(bank) >= 2 and det(sub(bank[-1], bank[-2]),
                                         sub(p, bank[-1])) <= 0:
                bank.pop()
            bank.append(p)
    return lower[:-1]+upper[:-1]


def perimeter(points):
    edges = [sub(points[(i+1) % len(points)], p) for i, p in enumerate(points)]
    return sum(sp.sqrt(sp.Rational(e[0])**2+sp.Rational(e[1])**2) for e in edges)


def difference_body_controls():
    polygons = [[(0, 0), (1, 0), (1, 1), (0, 1)],
                [(0, 0), (2, 0), (3, 1), (2, 3), (0, 2)],
                [(-2, 0), (-1, -1), (1, -1), (3, 0), (2, 2), (-1, 2)]]
    results = []
    for raw in polygons:
        p = hull([tuple(map(F, v)) for v in raw])
        k = hull([sub(a, b) for a in p for b in p])
        assert len(k) <= 2*len(p)
        assert set(k) == {tuple(-x for x in v) for v in k}
        assert sp.simplify(perimeter(k)-2*perimeter(p)) == 0
        d2 = max(sum(x*x for x in sub(a, b)) for a, b in combinations(p, 2))
        assert all(sum(x*x for x in v) <= d2 for v in k)
        results.append({"polygon_vertices": len(p), "difference_body_vertices": len(k),
                        "diameter_squared": str(d2), "perimeter_doubling": True})
    return results


def heptagon_escape():
    # Coordinates are (x, y/sqrt(3)); positive scaling preserves orientations.
    points = [(F(0), F(0)), (F(1), F(0)), (F(1, 2), F(1, 2)),
              (F(-1, 2), F(1, 2)), (F(-1), F(0)),
              (F(-1, 2), F(-1, 2)), (F(1, 2), F(-1, 2))]
    distances = {(i, j): (points[i][0]-points[j][0])**2
                 +3*(points[i][1]-points[j][1])**2
                 for i, j in combinations(range(7), 2)}
    assert len(distances) == 21 and min(distances.values()) == 1
    assert max(distances.values()) == 4
    assert all(distances[tuple(sorted((i, (i+1) % 7)))] == 1 for i in range(7))
    assert all(sum(points[i][a] for i in (1, 3, 5)) == 0 for a in (0, 1))
    assert len(hull(points)) == 6 and points[0] not in hull(points)
    convex_capacity = max(len(subset) for size in range(2, 8)
                          for subset in combinations(points, size)
                          if len(hull(subset)) == size)
    assert convex_capacity == 6
    # pi<22/7 and sin(x)<x imply D_7>1/(2*(11/49))>2.
    assert F(1, 2*F(11, 49)) > 2
    return {"retained_labels": 7, "checked_pairs": 21, "old_contacts_preserved": 7,
            "squared_diameter": 4, "convex_capacity": convex_capacity,
            "center_positive_barycenter": [1, 3, 5]}


def main():
    x = sp.symbols("x", positive=True)
    assert sp.trigsimp((1-sp.cos(2*x))/(2*sp.sin(x))-sp.sin(x)) == 0
    print(json.dumps({"classification": "exact finite controls; analytical universal proof",
                      "radial_support_gap_identity": "passed",
                      "difference_bodies": difference_body_controls(),
                      "canonical_heptagon_escape": heptagon_escape(),
                      "global_optimality_certified": False,
                      "level_i_resolved": False}, indent=2))


if __name__ == "__main__":
    main()
