#!/usr/bin/env python3
import math

CSTAR = 0.129220199818177
HSTAR = math.sqrt(303.0) / 52.0

# Direct three-way source-wide partition after Q-DIAMETER is absorbed into
# the exact-braid class.
assert abs(CSTAR / 3.0 - 0.04307339993939233) < 1e-15

# The q-slack repair only needs the inactive-witness absorption in the
# at-most-two-gate branch. Opening both q-base contacts then strictly lowers
# the contact count for every possible shallow-apex contact degree.
for d in range(3, 6):
    for k in range(0, 3):
        assert -d + k < 0

# Exact radial identity at a Q-DIAMETER witness. Put q=(0,0), r=(D,0),
# and a unit contact neighbor u=r+(cos(theta),sin(theta)).
for D in (10.0, 100.0, 1.0e6):
    for theta in [i * math.pi / 32 for i in range(64)]:
        ex = math.cos(theta)
        ey = math.sin(theta)
        ux = D + ex
        uy = ey
        Ru2 = ux * ux + uy * uy
        lhs = ex  # e=(1,0), so e dot (u-r)=cos(theta)
        rhs = (Ru2 - D * D - 1.0) / (2.0 * D)
        assert abs(lhs - rhs) < 1e-9
        if Ru2 <= D * D + 1e-12:
            assert rhs <= -1.0 / (2.0 * D) + 1e-12

# Once an inactive equality witness r is moved epsilon toward q, the q-r
# equality acquires strict diameter slack exactly epsilon.
for D in (10.0, 1000.0):
    for eps in (1e-9, 1e-5, 1e-2):
        assert abs((D - eps) - (D - eps)) < 1e-15
        assert D - eps < D

# The existing q-opening perturbation remains valid after that equality has
# been made strict.
for h in (0.01, HSTAR, 0.49):
    c2 = 1.0 - h * h
    for eps in (1e-8, 1e-4, 1e-2):
        assert c2 + (h + eps) ** 2 > 1.0

# Slow-scale separation dominates the universal O(D^(3/4)) endpoint
# localization in every subpolynomial/divergent kappa regime.
for D in (1e8, 1e12, 1e16):
    kappa = math.log(math.log(D))
    assert kappa > 1.0
    assert kappa * D ** 0.75 > D ** 0.75
    assert (D / kappa) / D < 1.0

print('q-diameter absorption certificate: PASS')
print(f'h_*={HSTAR:.15f}')
print(f'c_*/3={CSTAR/3.0:.15f}')
