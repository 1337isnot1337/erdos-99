#!/usr/bin/env python3
"""Arithmetic checks for the explicit rhombic-train gap note.

The proof is geometric. This script checks only displayed constants and exact finite
identities used in the write-up.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import random

getcontext().prec = 80
pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
s2 = delta2.sqrt()
eta = Decimal("0.0004")
sigma_gap = 2 * eta
mantel_gap = sigma_gap * (4 * s2 + eta) / 8
mu_gain = sigma_gap / 10
c0 = sqrt3 / 4
chamber_gain = 3 * c0 * sigma_gap / 5
oler_gain = chamber_gain / (sqrt3 / 2)

assert sigma_gap == Decimal("0.0008")
assert Decimal("0.0003809") < mantel_gap < Decimal("0.0003811")
assert mu_gain == Decimal("0.00008")
assert Decimal("0.0002078") < chamber_gain < Decimal("0.0002079")
assert oler_gain == Decimal("0.00024")

# Finite bookkeeping: full stopped trains = rhombic trains + singleton trains,
# recipient vacancy = 2 * singleton trains, and tau = S + sigma/2.
rng = random.Random(20260914)
for _ in range(10000):
    tr = rng.randint(1, 500)
    s = rng.randint(0, 500)
    # Choose a feasible rhombus count below the Mantel cap.
    r = rng.randint(1, max(1, tr * tr // 4))
    sqrt_r = Decimal(r).sqrt()
    b4 = 2 * tr
    t_full = tr + s
    capacity = 2 * t_full
    rho_rec = capacity - b4
    sigma = Decimal(b4) - 4 * sqrt_r
    tau = Decimal(t_full) - 2 * sqrt_r
    assert rho_rec == 2 * s
    assert abs(tau - (Decimal(s) + sigma / 2)) < Decimal("1e-70")

    m = Fraction(tr * tr, 4) - r
    rhs = Decimal(8) * (Decimal(m.numerator) / Decimal(m.denominator)) / (
        Decimal(tr) + 2 * sqrt_r
    )
    assert abs(sigma - rhs) < Decimal("1e-70")

print("Delta_2 =", delta2)
print("sqrt(Delta_2) =", s2)
print("explicit sigma_R/D gain =", sigma_gap)
print("explicit Mantel deficit/D^2 gain =", mantel_gap)
print("explicit mu gain =", mu_gain)
print("explicit chamber-surplus gain =", chamber_gain)
print("explicit chamber Oler-slack gain =", oler_gain)
print("explicit rhombic-train gap arithmetic: PASS")
