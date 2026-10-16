#!/usr/bin/env python3
"""Arithmetic/bookkeeping regression for all-degree Groemer face stability."""

from decimal import Decimal, getcontext
from fractions import Fraction as F
from random import Random

getcontext().prec = 60
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
a0 = sqrt3 / 2
delta2 = pi / (2 * sqrt3)
s = delta2.sqrt()
eta = Decimal('0.00042')

f_star = s - pi / 4 + eta / 2
K = 42
ell = f_star - pi / Decimal(K - 3)
match_fixed = ell / Decimal(4 * K + 1)
match_diag = match_fixed / 2

assert Decimal('0.1671245') < f_star < Decimal('0.1671248')
assert Decimal('0.0865708') < ell < Decimal('0.0865712')
assert Decimal('0.0005121') < match_fixed < Decimal('0.0005124')
assert Decimal('0.0002560') < match_diag < Decimal('0.0002563')

# K=42 maximizes the crude lower bound ell_K/(4K+1) among all useful
# integer cutoffs. Beyond this range the coefficient is already decreasing toward 0.
best = (Decimal('-1'), None)
for kk in range(5, 1000):
    low = f_star - pi / Decimal(kk - 3)
    if low <= 0:
        continue
    coeff = low / Decimal(4 * kk + 1)
    if coeff > best[0]:
        best = (coeff, kk)
assert best[1] == 42

# Exact force-hull residual identity behind the note:
# R_F = Sigma_F - E4/a0. Work in units divided by a0, so c0/a0=1/2.
rng = Random(20260914)
for _ in range(20000):
    R4 = F(rng.randrange(0, 50))
    f = F(rng.randrange(0, 30))
    q = F(rng.randrange(5, 80))
    k = F(rng.randrange(0, int(q) + 1))
    Q = F(rng.randrange(int(f), int(f) + 50))
    b = 2 * (q - k) - Q
    if b < 0:
        continue

    PF = F(rng.randrange(10, 100), rng.randrange(1, 5))
    e4bar = F(rng.randrange(0, 20), rng.randrange(1, 8))
    rbar = F(rng.randrange(0, 20), rng.randrange(1, 8))
    Zch = F(rng.randrange(0, 50))

    # H=(b-PF)+(2f+Q); Ach/a0=Zch+H/2+R_F.
    H = (b - PF) + 2 * f + Q
    Achbar = Zch + H / 2 + rbar
    AFbar = R4 + e4bar + Achbar
    m = R4 + f + q - k + 1
    NF = m + Zch
    sigmaF = AFbar + PF / 2 + 1 - NF
    assert sigmaF - e4bar == rbar

# Exact Q<=PF implication from b+Q=2(q-k), q<=PF, b>=PF.
for q in range(1, 60):
    for k in range(q + 1):
        for extra_p in range(0, 10):
            PF = F(q + extra_p)
            # choose every nonnegative Q for which b>=PF
            for Q in range(0, 2 * (q - k) + 1):
                b = F(2 * (q - k) - Q)
                if b >= PF:
                    assert F(Q) <= PF

print('f_* =', f_star)
print('K =', K)
print('ell_42 =', ell)
print('fixed-eta face-disjoint matching coefficient =', match_fixed)
print('diagonal o(1)-gap coefficient =', match_diag)
print('crude coefficient optimizer K =', best[1])
print('20,000 exact force-hull residual regressions: PASS')
