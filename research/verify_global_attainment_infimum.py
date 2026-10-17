#!/usr/bin/env python3
"""Exact finite fixtures for the global-attainment report, not an optimality test."""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def squared_distance(p, q):
    return sum((a - b) * (a - b) for a, b in zip(p, q))


def pair_squares(points):
    return {pair: squared_distance(points[pair[0]], points[pair[1]])
            for pair in combinations(range(len(points)), 2)}


def check_three_point_sequence():
    cases = (3, 10, 100, 1000, 10**6, 10**12)
    for m in cases:
        k = isqrt(m * m // 3) + 1
        assert 3 * (k - 1) * (k - 1) <= m * m < 3 * k * k
        u = F(k, m)
        third = ((1 - u * u) / (1 + u * u), 2 * u / (1 + u * u))
        points = ((F(0), F(0)), (F(1), F(0)), third)
        distances = pair_squares(points)
        assert distances[(0, 1)] == distances[(0, 2)] == 1
        diameter_sq = distances[(1, 2)]
        excess = F(3 * k * k - m * m, m * m + k * k)
        assert diameter_sq == 4 * u * u / (1 + u * u)
        assert diameter_sq - 1 == excess > 0
        assert excess <= F(5, m)
    return len(cases)


def check_distinct_velocity_coefficients(n):
    differences = [3**j - 3**i for i, j in combinations(range(n), 2)]
    assert len(differences) == len(set(differences))
    assert len({d * d for d in differences}) == len(differences)


def check_grid_perturbation(n):
    width = isqrt(n - 1) + 1
    points = [(F(i % width), F(i // width)) for i in range(n)]
    original = pair_squares(points)
    assert min(original.values()) == 1
    # A rational sequence tending to zero eventually avoids every finite root set.
    t = F(1, 1000 * n * 3**n)
    for _ in range(100):
        perturbed = [(x + t * 3**i, y) for i, (x, y) in enumerate(points)]
        distances = pair_squares(perturbed)
        if len(set(distances.values())) == len(distances):
            break
        t /= 2
    else:
        raise AssertionError("fixture failed to avoid pair-distance equalities")
    smallest = min(distances.values())
    normalized_squares = {pair: s / smallest for pair, s in distances.items()}
    assert smallest > 0
    assert sum(s == 1 for s in normalized_squares.values()) == 1
    assert all(s >= 1 for s in normalized_squares.values())
    assert all(not all(normalized_squares[pair] == 1
                       for pair in combinations(triple, 2))
               for triple in combinations(range(n), 3))
    # The actual raw displacements obey the report's finite-source bound.
    e = t * 3**(n - 1)
    assert e < F(1, 2)
    assert all(squared_distance(p, q) <= e * e
               for p, q in zip(points, perturbed))
    assert smallest >= (1 - 2 * e) * (1 - 2 * e)
    return n * (n - 1) // 2


def main():
    triangle_cases = check_three_point_sequence()
    total_pairs = 0
    sizes = (3, 4, 9, 16, 25, 49)
    for n in sizes:
        check_distinct_velocity_coefficients(n)
        total_pairs += check_grid_perturbation(n)
    print(f"PASS: {triangle_cases} exact three-point cases; "
          f"{len(sizes)} one-contact grid fixtures; {total_pairs} pairs checked")
    print("Scope: finite approximation regressions; no global optimality or Level I closure")


if __name__ == "__main__":
    main()
