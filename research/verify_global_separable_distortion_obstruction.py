#!/usr/bin/env python3
"""Exact finite checks for the whole-source separable-distortion obstruction.

The analytic theorem is proved in the accompanying report. These checks certify
cyclic incidence balances, Mobius distance identities in cyclotomic fields, and
a formal improved distance array that has no planar realization. They do not
certify global optimality or settle Level I.
"""

from fractions import Fraction
from itertools import combinations
import sys

if not __debug__:
    raise SystemExit('Refusing optimized Python: exact assertions must execute')

import sympy as sp


def cycle_balance(m):
    """Both rim contacts and longest chords give uniform vertex marginals."""
    if type(m) is not int or m < 5 or m % 2 != 1:
        raise ValueError('odd integer m >= 5 required')
    k = (m - 1) // 2
    contact = [tuple(sorted((i, (i + 1) % m))) for i in range(m)]
    diameter = [tuple(sorted((i, (i + k) % m))) for i in range(m)]
    assert len(set(contact)) == len(set(diameter)) == m
    assert set(contact).isdisjoint(diameter)
    counts = []
    for edges in (contact, diameter):
        degree = [Fraction(0) for _ in range(m)]
        for i, j in edges:
            degree[i] += Fraction(1, m)
            degree[j] += Fraction(1, m)
        counts.append(degree)
    assert counts[0] == counts[1] == [Fraction(2, m)] * m
    return contact, diameter


def cyclotomic_mobius(m):
    """Check all source pairs exactly for z -> z/(1+b*z), b=2/7."""
    z = sp.Symbol("z")
    modulus = sp.Poly(sp.cyclotomic_poly(m, z), z, domain=sp.QQ)

    def reduce(value):
        return sp.rem(sp.Poly(value, z, domain=sp.QQ), modulus).as_expr()

    def inv(value):
        return sp.invert(sp.Poly(value, z, domain=sp.QQ), modulus).as_expr()

    def mul(a, b):
        return reduce(a * b)

    b = sp.Rational(2, 7)
    roots = [reduce(z**i) for i in range(m)]
    conjugates = [roots[(-i) % m] for i in range(m)]
    w = [reduce(1 + b * (u + v) + b**2)
         for u, v in zip(roots, conjugates)]
    transformed = [mul(u, inv(1 + b * u)) for u in roots]
    transformed_conj = [mul(u, inv(1 + b * u)) for u in conjugates]
    contact, diameter = cycle_balance(m)
    q_contact = reduce(2 - roots[1] - conjugates[1])
    k = (m - 1) // 2
    q_diameter = reduce(2 - roots[k] - conjugates[k])
    checked = 0
    for i, j in combinations(range(m), 2):
        q = mul(roots[i] - roots[j], conjugates[i] - conjugates[j])
        q_transformed = mul(transformed[i] - transformed[j],
                            transformed_conj[i] - transformed_conj[j])
        assert reduce(mul(q_transformed, mul(w[i], w[j])) - q) == 0
        if (i, j) in contact:
            assert reduce(q - q_contact) == 0
        if (i, j) in diameter:
            assert reduce(q - q_diameter) == 0
        checked += 1
    return checked


def formal_planarity_regression():
    """Vertex scaling improves a four-label ratio but breaks planar geometry."""
    positions = [0, 1, 2, 3]
    factors = [1, 2, 3, 1]
    q = sp.zeros(4)
    values = []
    for i, j in combinations(range(4), 2):
        q[i, j] = q[j, i] = (positions[i] - positions[j])**2 * factors[i] * factors[j]
        values.append(q[i, j])
    assert min(values) == 2 and max(values) == 12
    assert sp.Rational(max(values), min(values)) < 9
    # Any four planar points have zero Cayley--Menger determinant.
    cm = sp.ones(5)
    cm[0, 0] = 0
    cm[1:, 1:] = q
    determinant = cm.det()
    assert determinant == -72
    # An independent actual planar square has zero Cayley--Menger determinant.
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    for i, j in combinations(range(4), 2):
        cm[i + 1, j + 1] = cm[j + 1, i + 1] = sum(
            (square[i][axis] - square[j][axis])**2 for axis in (0, 1))
    assert cm.det() == 0
    return determinant


def main():
    for invalid in (True, 3, 4, 6, 5.0, '5'):
        try:
            cycle_balance(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid cycle domain accepted')
    for m in range(5, 1002, 2):
        cycle_balance(m)
    pair_count = sum(cyclotomic_mobius(m) for m in (5, 7, 9, 11))
    determinant = formal_planarity_regression()
    print("PASS: 499 odd-rim incidence certificates (m=5,...,1001)")
    print(f"PASS: {pair_count} exact cyclotomic all-pair Mobius identities")
    print(f"PASS: formal improved squared ratio 6 < 9; Cayley--Menger determinant {determinant}")
    print("Scope: finite identities and a nonplanarity regression; no global optimality or Level I certificate.")


if __name__ == "__main__":
    main()
