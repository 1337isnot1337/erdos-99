#!/usr/bin/env python3
"""Regression checks for the near-full-shore growing exact-force diagonal."""

import math
from fractions import Fraction as Q

c = Q(113, 5_000_000)

# Fixed-n schedule from the theorem.
for n in [1, 2, 10, 100, 10_000]:
    m = 2 * n + 1
    eps = c / (10 * n)
    eta0 = eps / 4
    etar = eps / 4
    rho = eps / (8 * m)
    T0 = 41 * n
    Tr = 41 * m * n

    assert c / T0 < eta0
    assert m * c / Tr < etar
    assert 2 * m * rho == eps / 4

    lam = c / 2 - eta0 - etar - 2 * m * rho
    target = c / 2 - 3 * c / (40 * n)
    assert lam == target
    assert lam < c / 2
    assert c / 2 - lam == 3 * c / (40 * n)

# The density converges monotonically to c/2.
prev = None
for n in [1, 2, 5, 10, 100, 1000, 10000]:
    lam = c / 2 - 3 * c / (40 * n)
    if prev is not None:
        assert lam > prev
    prev = lam
assert float(c / 2) == 1.13e-5

# Pair gap is asymptotic to c/(160 n^2); it goes to zero while a diagonal can
# always choose D large enough that D^(1/4)*rho diverges.
for n in [10, 100, 1000]:
    m = 2 * n + 1
    rho = c / (80 * n * m)
    assert rho > 0
    assert rho < float(c) / (160 * n * n) * 1.01

    # Exhibit an algebraic D choice just for scaling: D=(n/rho)^4 makes
    # D^(1/4)*rho=n. The actual proof is free to choose still larger D after
    # the fixed-parameter theorem's source threshold.
    D = (n / float(rho)) ** 4
    assert abs(D ** 0.25 * float(rho) - n) / n < 1e-12

# Coupled host constants used by every force bar.
z0 = 2.0477
d0 = z0 - 6 * math.sin(z0 / 6)
cH = 0.4143 + d0
assert 0.45381 < cH < 0.45383
assert 0.90763 < 2 * cH < 0.90765

# A positive sequence of m reactions with total <D has at least half its terms
# below 2D/m. Verify the counting threshold combinatorially.
for m in [3, 5, 11, 101]:
    # If more than floor(m/2) terms were >=2/m of total scale 1, their sum
    # would exceed 1. Thus at least ceil(m/2) are below 2/m.
    too_large = math.floor(m / 2) + 1
    assert too_large * (2 / m) > 1

print("PASS: near-full-shore growing exact-force diagonal regressions")
print("one-sided shore density c/2 =", float(c / 2))
print("coupled host transverse floor =", cH)
print("coupled dipole slope coefficient =", 2 * cH)
