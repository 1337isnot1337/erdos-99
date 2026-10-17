#!/usr/bin/env python3
"""Exact arithmetic/regression checks for the one-anchor corank theorem.

The geometry is proved in the companion Markdown note.  This script checks:
* the exact coefficient implication sigma <= f/5 + (18/5) E_U;
* the resulting flex/corank algebra;
* the rigorous live-window upper enclosure sigma/D < 0.1558266092 when E_U=o(D).
"""

from fractions import Fraction
from math import isqrt

Q = Fraction


def atan_inv_bounds(q: int, terms: int):
    s = Q(0)
    for k in range(terms):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * terms + 1) * q ** (2 * terms + 1))
    if terms % 2 == 0:
        return s, s + nxt
    return s - nxt, s


def sqrt_ceil(x: Q, scale: int) -> Q:
    n = isqrt((x.numerator * scale * scale) // x.denominator) + 1
    y = Q(n, scale)
    assert y * y >= x
    return y


# Finite coefficient regression.  The proof is the exact identity below, not the box.
for a in range(12):
    for x_A in range(12):
        for n_0 in range(12):
            for n_1 in range(12):
                for n_2 in range(12):
                    f = a + n_0 + n_1 + n_2
                    sigma_bound = 2 * n_0 + n_2 + Q(n_1, 5)
                    E = a + Q(x_A, 2) + Q(n_0 + n_2, 2)
                    rhs = Q(f, 5) + Q(18, 5) * E
                    assert rhs - sigma_bound == Q(19 * a + 9 * x_A + 5 * n_2, 5)
                    assert sigma_bound <= rhs

# Rigorous pi and sqrt(pi/(2sqrt(3))) enclosure, matching the repository's exact style.
DIGITS = 90
SCALE = 10 ** DIGITS

a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_hi = 16 * a5_hi - 4 * a239_lo

n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
assert sqrt3_lo * sqrt3_lo < 3

delta2_hi = pi_hi / (2 * sqrt3_lo)
s2_hi = sqrt_ceil(delta2_hi, SCALE)

g = Q(7707, 10**6)
epsilon = Q(71, 10000)
Mstar_hi = 4 * s2_hi + 2 * g

# f/D <= M*/5 + 2 epsilon; at E_U=o(D), sigma/D <= (f/D)/5.
f_density_hi = Mstar_hi / 5 + 2 * epsilon
sigma_endpoint_hi = f_density_hi / 5
assert sigma_endpoint_hi < Q(1558266092, 10**10)

print("PASS: one-anchor closure-corank certificate")
print("live f-density upper enclosure <", float(f_density_hi))
print("pair-floor sigma_C density upper enclosure <", float(sigma_endpoint_hi))
