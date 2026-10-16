#!/usr/bin/env python3
"""Exact finite checks for Steiner packing-capacity loss.

The capacity conclusions use canonical Oler and the analytical four-point
diameter bound, not a numerical packing search. No large global minimizer
or Level I counterexample is certified.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as F
from itertools import combinations, product


def area(vertices):
    return abs(sum(p[0] * q[1] - q[0] * p[1]
                   for p, q in zip(vertices, vertices[1:] + vertices[:1]))) / 2


def distance_sq(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def section_width(vertices, y):
    crossings = set()
    for p, q in zip(vertices, vertices[1:] + vertices[:1]):
        if min(p[1], q[1]) <= y <= max(p[1], q[1]) and p[1] != q[1]:
            crossings.add(p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1]))
    return max(crossings) - min(crossings)


def square_global_minimizer_regression():
    original = [(F(-7, 10), F(-1, 10)), (F(-1, 10), F(7, 10)),
                (F(7, 10), F(1, 10)), (F(1, 10), F(-7, 10))]
    symmetrized = [(F(0), F(-7, 10)), (F(5, 8), F(-1, 10)),
                  (F(5, 8), F(1, 10)), (F(0), F(7, 10)),
                  (F(-5, 8), F(1, 10)), (F(-5, 8), F(-1, 10))]
    assert area(original) == area(symmetrized) == 1
    for y in [F(-7, 10), F(-1, 10), F(1, 10), F(7, 10)]:
        assert section_width(original, y) == section_width(symmetrized, y)
    assert min(distance_sq(p, q) for p, q in combinations(original, 2)) == 1
    assert max(distance_sq(p, q) for p, q in combinations(original, 2)) == 2
    assert max(distance_sq(p, q) for p, q in combinations(symmetrized, 2)) == F(49, 25) < 2
    three_sites = [(F(0), F(7, 10)), (F(-5, 8), F(-1, 10)), (F(5, 8), F(-1, 10))]
    assert min(distance_sq(p, q) for p, q in combinations(three_sites, 2)) > 1
    print("four-point global minimizer: Steiner diameter squared 2 -> 49/25; capacity 4 -> 3")


def rhombus_capacity_regression():
    for m in [20, 40, 100]:
        t = F(1, 2) - F(1, m * m)
        h_sq = 1 - t * t
        assert 0 < t < F(1, 2)
        # h/(2 v_y)<=9/20 is equivalent to 14h<=27t.
        assert 196 * h_sq <= 729 * t * t
        # h/a0 <= 1+2/(3m^2), checked by squaring positive quantities.
        area_factor_bound = 1 + F(2, 3 * m * m)
        assert F(4, 3) * h_sq <= area_factor_bound * area_factor_bound
        n = (m + 1) ** 2
        original_oler_upper = area_factor_bound * m * m + 2 * m + 1
        assert original_oler_upper.numerator // original_oler_upper.denominator == n
        symmetrized_oler_upper = area_factor_bound * m * m + F(19, 10) * m + 1
        capacity_upper = symmetrized_oler_upper.numerator // symmetrized_oler_upper.denominator
        assert n - symmetrized_oler_upper == F(m, 10) - F(2, 3)
        assert capacity_upper < n
        # The explicit source is far from global minimum diameter; a standard
        # translated-lattice disk bound is <(6/5)n in squared diameter.
        assert F(6, 5) * n < 2 * m * m * (1 + t)
        print(f"m={m}: original capacity exactly {n}, Steiner capacity <= {capacity_upper}; loss >= {n-capacity_upper}")
    m = 20
    t = F(1, 2) - F(1, m * m)
    labels = list(product(range(m + 1), repeat=2))
    minimum = None
    contacts = 0
    for (i, j), (k, ell) in combinations(labels, 2):
        a, b = i - k, j - ell
        d = a * a + b * b + 2 * t * a * b
        assert d >= 1
        if d == 1:
            assert abs(a) + abs(b) == 1
            contacts += 1
        minimum = d if minimum is None else min(minimum, d)
    assert minimum == 1 and contacts == 2 * m * (m + 1)
    print(f"m=20: all {len(labels)*(len(labels)-1)//2} source pairs and {contacts} exact contacts checked")


if __name__ == "__main__":
    square_global_minimizer_regression()
    rhombus_capacity_regression()
    print("PASS: packing-capacity loss only; no eventual Level I conclusion")
