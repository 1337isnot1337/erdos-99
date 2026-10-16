#!/usr/bin/env python3
"""Exact full-pair finite checks for the accompanying unreviewed report."""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as F
from itertools import combinations

import sympy as sp


def axial_squared(p, q):
    a, b = (x - y for x, y in zip(p, q))
    return a * a + a * b + b * b


def no_triangles(n, edges):
    edges = {tuple(sorted(e)) for e in edges}
    return all(not all(e in edges for e in combinations(triple, 2))
               for triple in combinations(range(n), 3))


def gram_check(name, distance_matrix):
    n = distance_matrix.rows
    j = sp.eye(n) - sp.ones(n) / n
    gram = -j * distance_matrix * j / 2
    assert gram.rank() == 2
    old_diameter_squared = max(distance_matrix[i, k] for i, k in combinations(range(n), 2))
    for t in (sp.Rational(1, 10), sp.Rational(1, 2), sp.Rational(1)):
        new_gram = (1 - t) * gram + t * j / 2
        assert new_gram.rank() == n - 1
        for i, k in combinations(range(n), 2):
            actual = new_gram[i, i] + new_gram[k, k] - 2 * new_gram[i, k]
            expected = (1 - t) * distance_matrix[i, k] + t
            assert actual == expected
            assert 1 <= actual < old_diameter_squared
    return f"{name}: rank {n - 1} at all 3 parameters, all pairs checked"


def sign_qsqrt5(expression):
    """Exact sign in Q(sqrt(5)), reducing magnitude comparison to rationals."""
    expr = sp.expand(expression)
    b = expr.coeff(sp.sqrt(5))
    a = sp.simplify(expr - b * sp.sqrt(5))
    assert a.is_Rational and b.is_Rational
    if not b:
        return int(bool(a > 0)) - int(bool(a < 0))
    if not a:
        return int(bool(b > 0)) - int(bool(b < 0))
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    comparison = sp.simplify(a * a - 5 * b * b)
    if not comparison:
        return 0
    return (1 if a > 0 else -1) * (1 if comparison > 0 else -1)


def verify_hexagon_and_endpoint():
    old = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(1)),
           (F(-1), F(0)), (F(0), F(-1)), (F(1), F(-1))]
    pairs = list(combinations(range(6), 2))
    old_squared = {(i, k): axial_squared(old[i], old[k]) for i, k in pairs}
    assert min(old_squared.values()) == 1 and max(old_squared.values()) == 4
    contacts = [e for e, length in old_squared.items() if length == 1]
    assert len(contacts) == 6 and no_triangles(6, contacts)
    assert len([length for length in old_squared.values() if length == 4]) == 3
    # Endpoint labels 0,...,4 are the regular pentagon; label 5 is its center.
    endpoint_squared = {}
    for i, k in pairs:
        if k == 5:
            squared = sp.Integer(1)
        else:
            difference = min(k - i, 5 - (k - i))
            squared = (5 + (-1 if difference == 1 else 1) * sp.sqrt(5)) / 2
        endpoint_squared[i, k] = squared
        assert sign_qsqrt5(squared - 1) >= 0
        assert sign_qsqrt5(4 - squared) > 0
    endpoint_contacts = [e for e, squared in endpoint_squared.items() if squared == 1]
    assert len(endpoint_contacts) == 5 and no_triangles(6, endpoint_contacts)
    endpoint_max = (5 + sp.sqrt(5)) / 2
    assert sum(squared == endpoint_max for squared in endpoint_squared.values()) == 5
    matrix = sp.Matrix(6, 6, lambda i, k: 0 if i == k else old_squared[tuple(sorted((i, k)))])
    return matrix, len(pairs)


def main():
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    square_distances = sp.Matrix(4, 4, lambda i, k: sum(
        (square[i][axis] - square[k][axis]) ** 2 for axis in (0, 1)))
    hex_distances, pair_count = verify_hexagon_and_endpoint()
    print("PASS:", gram_check("square", square_distances))
    print("PASS:", gram_check("hexagon", hex_distances))
    print(f"PASS: all {pair_count} old and {pair_count} endpoint pairs; "
          "both contact graphs triangle-free; endpoint diameter strictly below 2")
    print("Scope: finite exact rank and pair certificates, not Level I closure.")


if __name__ == "__main__":
    main()
