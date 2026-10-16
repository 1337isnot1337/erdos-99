#!/usr/bin/env python3
"""Exact certificate for the modern high-t pentagon-face staircase.

For the canonical full-core Type-II contact embedding let f be the number of bounded
nonquadrilateral faces, Q=sum(deg P-4), and f5 the number of bounded degree-5 faces.
Every nonquadrilateral face has degree >=5, so
  Q-f = sum(deg P-5) >= number of degree>=6 faces,
and hence f5 >= f-(Q-f).

Using the exact post-endpoint identities and the modern train-slack floor
  liminf tau_D/D >= rho+0.007707,
one gets, whenever t=(q-k)/D <= T,
  f5/D >= rho+0.007707 - 3T + pi + 2sqrt(Delta_2) - o(1).

This script certifies the safe staircase 0.243, 0.228, 0.213 at T=1.850,1.855,1.860.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

# Modern train-slack inputs.
g = Q(7707, 10**6)
rho_lo = Q(7390851, 10**7)
cos_lo = sum(
    (-1) ** k * rho_lo ** (2 * k) / factorial(2 * k)
    for k in range(8)
)
assert cos_lo > rho_lo
# cos(x)-x strictly decreases for x>=0, hence the Dottie number rho exceeds rho_lo.
tau_lo = rho_lo + g

# Lower bounds for pi and sqrt(Delta_2), Delta_2=pi/(2sqrt(3)).
pi_lo = Q(103993, 33102)
s3_up = Q(1732050808, 10**9)
assert s3_up * s3_up > 3
Delta_lo = pi_lo / (2 * s3_up)
S = 10**12
root = isqrt((Delta_lo.numerator * S * S) // Delta_lo.denominator)
sqrtDelta_lo = Q(root, S)
assert sqrtDelta_lo * sqrtDelta_lo <= Delta_lo

CASES = [
    (Q(37, 20), Q(243, 1000)),   # 1.850 -> 0.243
    (Q(371, 200), Q(228, 1000)), # 1.855 -> 0.228
    (Q(93, 50), Q(213, 1000)),   # 1.860 -> 0.213
]

for T, safe_p5 in CASES:
    # 2f = tau_D - tD + 2sqrt(R4).
    f_lo = (tau_lo - T + 2 * sqrtDelta_lo) / 2

    # X=(Q-f)+(b-p) from the exact post-endpoint identity:
    # X/D = (5/2)t - p/D - sqrt(R4)/D - tau_D/(2D).
    X_hi = Q(5, 2) * T - pi_lo - sqrtDelta_lo - tau_lo / 2

    # f5 >= f-(Q-f) >= f-X since b-p>=0.
    p5_lo = f_lo - X_hi
    # Equivalent simplified coefficient: tau-3T+pi+2sqrt(Delta_2).
    assert p5_lo == tau_lo - 3 * T + pi_lo + 2 * sqrtDelta_lo
    assert p5_lo > safe_p5
    assert p5_lo - safe_p5 > Q(1, 100000)

    print(f"T={float(T):.3f}")
    print("  f/D lower  =", float(f_lo))
    print("  X/D upper  =", float(X_hi))
    print("  f5/D lower =", float(p5_lo))
    print("  safe f5/D  =", float(safe_p5))
    print("  margin      =", float(p5_lo - safe_p5))

print("PASS modern high-t pentagon-face staircase")
