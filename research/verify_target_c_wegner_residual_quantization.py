#!/usr/bin/env python3
"""Arithmetic checks for Wegner residual quantization."""

from decimal import Decimal, getcontext
from math import ceil, floor, sqrt

getcontext().prec = 60
sqrt3 = Decimal(3).sqrt()
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
a0 = sqrt3 / 2
kappa = 1 / sqrt3 - Decimal(1) / 2

assert Decimal('0.0773502') < kappa < Decimal('0.0773504')

# Algebraic coefficient identity from scaling Wegner.
cw = (Decimal(2) - sqrt3) / 4
assert abs(cw / a0 - kappa) < Decimal('1e-55')
assert abs(Decimal(1) / 2 - Decimal(1) / (2 * a0) + kappa) < Decimal('1e-55')


def L(N: int) -> int:
    return ceil(sqrt(12 * N - 3) - 3 - 1e-12)


def zmax(d: int) -> int:
    return floor((d * d - 6 * d + 12) / 12)

# First-jump equivalence: L_N <= d iff N <= floor(((d+3)^2+3)/12).
for d in range(5, 200):
    nmax = floor(((d + 3) ** 2 + 3) / 12)
    assert nmax - d == zmax(d)
    for N in range(d, nmax + 3):
        assert (L(N) <= d) == (N <= nmax), (d, N, L(N), nmax)

assert zmax(5) == 0
assert zmax(6) == 1
assert zmax(7) == 1
assert zmax(8) == 2
assert zmax(22) == 30
assert zmax(42) == 127
assert floor(((42 + 3) ** 2 + 3) / 12) == 169

# General m-jump implication: L_N-d <= m-1 iff the corresponding quadratic bound holds.
for d in range(5, 60):
    for m in range(1, 8):
        nmax = floor(((d + m + 2) ** 2 + 3) / 12)
        for N in range(d, nmax + 3):
            assert (L(N) - d <= m - 1) == (N <= nmax), (d, m, N)

# Recompute the linear degree<=42 population coefficient used by the note.
delta2 = pi / (2 * sqrt3)
s = delta2.sqrt()
f_star = s - pi / 4 + Decimal('0.00021')
ell42 = f_star - pi / Decimal(39)
assert Decimal('0.0865708') < ell42 < Decimal('0.0865712')

print('kappa =', kappa)
print('zmax(42) =', zmax(42))
print('Nmax(42) =', 42 + zmax(42))
print('ell_42 =', ell42)
print('Wegner residual quantization checks: PASS')
