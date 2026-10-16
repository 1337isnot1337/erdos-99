#!/usr/bin/env python3
"""Exact-rational certificate for the degree-weighted pentagon-seed tradeoff.

This script certifies only the scalar composition in
`target_c_free_terminal_degree_weighted_pentagon_seed_tradeoff_2026-09-18.md`.
The finite graph/rank argument is proved in that note.
"""

from fractions import Fraction as F


# Safe live constants imported from already-certified proof-only terminal notes.
f_upper = F(76152405, 100000000)       # f/D < 0.76152405 + o(1)
r_upper = F(141, 1000000)              # (Q-f)/D < 0.000141 + o(1)
C0 = F(11988388040, 10000000000)       # m/D baseline > 1.1988388040
K0 = F(11812298040, 10000000000)       # k/D > 1.1812298040
A0 = F(14941462550, 10000000000)       # old quarter line constant > 1.4941462550


# WS.3: degree-weighted seed threshold.
B0 = F(2, 5) * f_upper + F(8, 5) * r_upper
assert B0 == F(15241761, 50000000)
assert B0 == F(30483522, 100000000)


# Random-order exclusion probabilities for degrees 0,...,5.
# A vertex is retained when at most three neighbors precede it.
seed_prob = {
    d: max(F(0), F(1) - F(4, d + 1))
    for d in range(6)
}
assert seed_prob == {
    0: F(0),
    1: F(0),
    2: F(0),
    3: F(0),
    4: F(1, 5),
    5: F(1, 3),
}
assert seed_prob[5] - seed_prob[4] == F(2, 15)


# WS.7: weighted flex/topology-stress conservation law.
lam = F(15, 8)
weighted_floor = C0 + lam * (K0 - B0)
assert weighted_floor == F(2842078649, 1000000000)
assert weighted_floor > F(2842078648, 1000000000)


# WS.6: crossover between sigma/4 and (15/8)(sigma-B0).
sigma_cross = F(15, 13) * B0
assert sigma_cross == F(45725283, 130000000)
assert sigma_cross > F(351732946, 1000000000)


# WS.9: intersection of the new 15/8 line with the old 1/4 line.
x_cross = (weighted_floor - A0) / (lam - F(1, 4))
m_cross = A0 - F(1, 4) * x_cross
assert x_cross == F(673966197, 812500000)
assert m_cross == F(16728036527, 13000000000)
assert x_cross > F(829496857, 1000000000)
assert m_cross > F(1286772040, 1000000000)


# Useful defect remainder at the degree-weighted threshold.
defect_remainder = K0 - B0
assert defect_remainder == F(109549323, 125000000)
assert defect_remainder > F(876394583, 1000000000)


print("degree-weighted pentagon-seed certificate: PASS")
print("B0 =", float(B0), B0)
print("lambda =", float(lam), lam)
print("weighted floor =", float(weighted_floor), weighted_floor)
print("sigma crossover =", float(sigma_cross), sigma_cross)
print("intersection x =", float(x_cross), x_cross)
print("intersection m =", float(m_cross), m_cross)
print("K0-B0 =", float(defect_remainder), defect_remainder)
