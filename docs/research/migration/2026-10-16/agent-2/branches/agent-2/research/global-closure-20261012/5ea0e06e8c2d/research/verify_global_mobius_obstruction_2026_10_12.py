#!/usr/bin/env python3
"""Exact finite checks for inversion; the all-pole theorem is analytical.

No global-optimality or Level I oracle. All input/image coordinates and every
pair distance are rational. No finite source label is discarded.
"""

from fractions import Fraction as F
from itertools import combinations
import json
import sympy as sp


def norm2(point):
    return sum(x * x for x in point)


def sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def ledger(points):
    return {edge: norm2(sub(points[edge[0]], points[edge[1]]))
            for edge in combinations(range(len(points)), 2)}


def invert(points, pole):
    radii = [norm2(sub(p, pole)) for p in points]
    assert all(radii), "pole is a source label"
    image = [tuple(x / radius for x in sub(p, pole))
             for p, radius in zip(points, radii)]
    original, transformed = ledger(points), ledger(image)
    assert len(image) == len(set(image)) == len(points)
    for (i, j), old in original.items():
        assert transformed[i, j] == old / (radii[i] * radii[j])
    return original, transformed, radii


def check_grid(m, pole):
    radius = F(m - 1, 2)
    points = [(F(i) - radius, F(j) - radius)
              for i in range(m) for j in range(m)]
    if pole in points:
        return None
    old, new, radii = invert(points, pole)
    old_d2 = 8 * radius * radius
    assert min(old.values()) == 1 and max(old.values()) == old_d2
    ratio = max(new.values()) / min(new.values())
    assert ratio >= old_d2

    # Reflect and swap to the proof's r >= s >= 0 symmetry chamber.
    r, s = sorted(map(abs, pole), reverse=True)
    q_f = 2 * radius**2 + r*r + s*s + 2 * radius * (r+s)
    q_o = 2 * radius**2 + r*r + s*s - 2 * radius * (r+s)
    q_n = q_f - 2 * radius + 1 - 2 * s
    if m == 2 or r+s >= F(1, 2):
        assert q_n >= q_o > 0
        assert ratio >= old_d2 * q_n / q_o
        regime = "diameter_and_far_unit_pair"
    else:
        if m % 2:
            product = (r*r+s*s) * (1+r*r+s*s-2*r)
        else:
            b = F(1, 2) + r*r + s*s - r
            assert 0 < b <= F(1, 2)
            product = b*b - s*s
        assert 0 < product <= F(1, 4)
        assert max(new.values()) >= 4
        assert q_f >= 2 * radius**2
        assert q_n >= 2 * radius**2 - 2 * radius + 1
        assert ratio >= 4 * q_f * q_n >= old_d2
        regime = "new_pair_in_central_diamond"
    return regime, ratio


def symbolic_checks():
    x, y, a, b = sp.symbols("x y a b", real=True)
    p = sp.Matrix([x, y])
    q = sp.Matrix([a, b])
    p2, q2 = p.dot(p), q.dot(q)
    assert sp.factor((p/p2-q/q2).dot(p/p2-q/q2) * p2*q2
                     - (p-q).dot(p-q)) == 0
    R, r, s = sp.symbols("R r s", real=True)
    q_f = 2*R**2+r*r+s*s+2*R*(r+s)
    q_o = 2*R**2+r*r+s*s-2*R*(r+s)
    q_n = q_f-2*R+1-2*s
    assert sp.expand(q_n-q_o-(4*R*(r+s)-2*s-2*R+1)) == 0
    b_even = sp.Rational(1, 2)+r*r+s*s-r
    qa = (r-sp.Rational(1, 2))**2+(s-sp.Rational(1, 2))**2
    qb = (r-sp.Rational(1, 2))**2+(s+sp.Rational(1, 2))**2
    assert sp.expand(qa*qb-(b_even*b_even-s*s)) == 0


def inactive_pair_control():
    points = [(F(i), F(j)) for i in (-1, 0, 1)
              for j in (-1, 0, 1) if (i, j) != (0, 0)]
    old, new, _ = invert(points, (F(0), F(0)))
    contacts = {e for e, value in old.items() if value == 1}
    diameters = {e for e, value in old.items() if value == 8}
    assert len(old) == 28 and min(new.values()) == F(1, 2)
    assert max(new[e] for e in diameters) == 2
    assert max(new.values()) == 4
    assert max(new.values()) / min(new.values()) == 8
    assert max(new[e] for e in diameters) / min(new[e] for e in contacts) == 4
    return {"labels": 8, "pairs": 28, "old_active_pair_prediction_d2": 4,
            "actual_normalized_d2": 8}


def replacement_control():
    labels = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0),
              (0, -1), (1, -1), (1, 1), (2, -1)]
    points = [(F(a) + F(8, 17)*b, F(15, 17)*b) for a, b in labels]
    pairs = ledger(points)
    assert len(points) == len(set(points)) == 9 and len(pairs) == 36
    assert min(pairs.values()) == 1 and max(pairs.values()) == F(125, 17)
    contacts = {e for e, value in pairs.items() if value == 1}
    assert all((sum(labels[i])-sum(labels[j])) % 2 for i, j in contacts)
    assert max(pairs.values()) < 8
    return {"labels": 9, "pairs": 36, "squared_diameter": "125/17",
            "strict_squared_margin_against_grid": "11/17",
            "triangle_free": True}


def augmented_source_control():
    radius = F(7, 2)
    grid = [(F(i)-radius, F(j)-radius) for i in range(8) for j in range(8)]
    # Its non-half-integral x coordinate is outside the grid's lattice. This
    # added label is an actual contact isolate inside the full diameter lenses.
    points = grid + [(F(1, 7), F(5))]
    old = ledger(points)
    assert min(old.values()) == 1 and max(old.values()) == 98
    isolate_pairs = {e: d for e, d in old.items() if len(grid) in e}
    assert len(isolate_pairs) == 64
    assert all(1 < d < 98 for d in isolate_pairs.values())
    for pole in [(F(0), F(0)), (F(1, 4), F(1, 8)),
                 (F(3), F(-2)), (F(4000), F(0))]:
        _, grid_image, _ = invert(grid, pole)
        _, full_image, _ = invert(points, pole)
        assert max(full_image.values()) >= max(grid_image.values())
        assert min(full_image.values()) <= min(grid_image.values())
        assert max(full_image.values()) / min(full_image.values()) >= 98
    return {"labels": len(points), "pairs": len(old), "contact_isolates_added": 1,
            "squared_diameter": 98, "poles_checked": 4}


def main():
    symbolic_checks()
    poles = [(F(a, 8), F(b, 8)) for a, b in
             [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 0),
              (3, 1), (4, 0), (4, 4), (7, 2), (11, -9), (20, 40),
              (-24, 40), (80, 8), (8000, -4000)]]
    summaries = []
    for m in (2, 3, 4, 5, 6, 8):
        regimes, tested = set(), 0
        for pole in poles:
            result = check_grid(m, pole)
            if result is not None:
                regimes.add(result[0])
                tested += 1
        if m >= 3:
            assert len(regimes) == 2
        summaries.append({"grid_side": m, "labels": m*m,
                          "pairs": m*m*(m*m-1)//2,
                          "admissible_poles_tested": tested,
                          "proof_regimes_checked": sorted(regimes)})
    print(json.dumps({"classification": "exact finite certificate; no globality oracle",
                      "symbolic_identities": "passed", "grids": summaries,
                      "augmented_full_source": augmented_source_control(),
                      "inactive_pair_control": inactive_pair_control(),
                      "whole_source_replacement": replacement_control()}, indent=2))


if __name__ == "__main__":
    main()
