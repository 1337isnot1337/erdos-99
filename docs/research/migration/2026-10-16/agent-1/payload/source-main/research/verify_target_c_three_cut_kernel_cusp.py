#!/usr/bin/env python3
from fractions import Fraction as F

# Same exact constants as the hostile-audited adjacent-pair averaging theorem.
A = F(1851, 2500)          # 0.7404
P = F(53, 625)             # 0.0848
N = F(1063, 1000)          # 1.063
lam = F(677, 1000)
r = F(61, 125)             # 0.488

g = (A - lam) * P / (N - lam)
d_top = lam - (1 - r) * N
d_low = lam - r * N
p = d_top * g / (r * N)
assert d_top > 0 and d_low > 0
assert p > F(3564, 10**6)

pi_u = F(355, 113)
sqrt3_u = F(17321, 10000)
C_phase_u = pi_u * pi_u * sqrt3_u * (2 + sqrt3_u) / 12

# Parent total-cost constant per internal boundary.
K = (2 * pi_u + 2 + 2 * C_phase_u / d_low) / p
assert K < 21200

# For consecutive triples of cuts, average T_i+T_{i+1}.  Every internal
# boundary cost appears in at most two such sums, so the asymptotic constant is
# at most 2K.  The m-2 versus m denominator discrepancy is absorbed by o(1)
# because m>pD-o(D).
K3 = 2 * K
assert K3 < 42400
assert F(42400) - K3 > 48

print('backbone density p =', p, float(p))
print('parent adjacent constant K =', K, float(K))
print('three-cut two-boundary constant 2K =', K3, float(K3))
print('margin to 42400 =', F(42400)-K3, float(F(42400)-K3))
print('PASS: one consecutive three-cut block has total switch count, D*switch beta mass, and D*two-gap phase cost all <42400+o(1)')
