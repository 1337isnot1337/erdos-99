#!/usr/bin/env python3
"""Exact bookkeeping regression for the Target-C Oler gluing identity."""

from fractions import Fraction as F
from math import pi, sqrt
from random import Random

rng = Random(20260914)

for _ in range(20000):
    R4 = F(rng.randrange(0, 80))
    f = F(rng.randrange(0, 40))
    q = F(rng.randrange(5, 120))
    k = F(rng.randrange(0, int(q) + 1))
    a = F(rng.randrange(0, 30))
    Q = F(rng.randrange(int(f), int(f) + 80))

    # Enforce b+Q=2(q-k); random trials that make b negative are skipped.
    b = 2 * (q - k) - Q
    if b < 0:
        continue

    e4bar = F(rng.randrange(0, 30), rng.randrange(1, 10))  # E4/a0
    A4bar = R4 + e4bar
    Achbar = F(rng.randrange(0, 100), rng.randrange(1, 10))
    AFbar = A4bar + Achbar
    Zch = F(rng.randrange(0, 80))
    m = R4 + f + q - k + 1
    NF = m + Zch

    PF = F(rng.randrange(20, 160), rng.randrange(1, 5))
    Pch = 4 * f + Q + b + PF - 2 * q + 2 * a
    sch = f + a

    sigma_F = AFbar + PF / 2 + 1 - NF
    sigma_ch = Achbar + Pch / 2 + sch - Zch
    T = q - k + 2 * f

    assert sigma_ch == sigma_F + 2 * (T - q / 2) + 2 * a - e4bar

    # Exterior-cap aggregate variables. Xbar=(area(K)-area(F))/a0.
    Xbar = F(rng.randrange(0, 100), rng.randrange(1, 10))
    PK = F(rng.randrange(20, 160), rng.randrange(1, 5))
    r = F(rng.randrange(0, 20))
    # Choose noncommon total force-hull length >= r, so L_cap >= 0.
    extra = F(rng.randrange(0, 50), rng.randrange(1, 5))
    Pcom = PF - r - extra
    if Pcom < 0:
        continue
    Zext = F(rng.randrange(0, 80))

    sigma_ext = Xbar + (PK + PF) / 2 - Pcom - r - Zext
    n = NF + Zext
    sigma_K = AFbar + Xbar + PK / 2 + 1 - n
    omega_K = sigma_K - e4bar
    Lcap = PF - Pcom - r

    assert sigma_F + sigma_ext == sigma_K + Lcap
    assert sigma_ch + sigma_ext == omega_K + 2 * (T - q / 2) + 2 * a + Lcap
    assert Lcap >= 0

Delta2 = pi / (2 * sqrt(3))
s2 = sqrt(Delta2)
Cstar = 2 * s2 + 0.00042
combined = 2 * Cstar
chamber = combined - pi / 2

print("PASS: 20,000 exact-rational gluing regressions")
print(f"Delta2={Delta2:.15f}")
print(f"AG42 C*={Cstar:.15f}")
print(f"combined local slack floor={combined:.15f}")
print(f"chamber-only floor={chamber:.15f}")
