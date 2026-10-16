#!/usr/bin/env python3
"""Regression checks for terminal FREE route/perimeter and train-pentagon normal form."""
from __future__ import annotations

import math
import random

PI = math.pi
SQ3 = math.sqrt(3.0)
s2 = math.sqrt(PI / (2.0 * SQ3))
g = 0.007707
M = 4.0 * s2 + 2.0 * g
C = 3.0 * M / 8.0
tau = PI / 2.0 + g
mantel = tau * s2 / 2.0 + tau * tau / 16.0
p5_endpoint = M / 8.0
I5_endpoint = 5.0 * M / 8.0 - tau

# Reported constants.
assert abs(s2 - 0.9523128068639574) < 5e-15
assert abs(M - 3.8246652274558293) < 5e-15
assert abs(C - 1.4342494602959360) < 5e-15
assert abs(tau - 1.5785033267948965) < 5e-15
assert abs(tau / 2.0 - 0.7892516633974482) < 5e-15
assert abs(mantel - 0.9073440139359810) < 5e-15
assert abs(p5_endpoint - 0.47808315343197866) < 5e-15
assert abs(I5_endpoint - 0.8119124403649969) < 5e-15
assert abs(I5_endpoint / 2.0 - 0.40595622018249844) < 5e-15
assert abs(I5_endpoint / 5.0 - 0.16238248807299938) < 5e-15
assert abs(I5_endpoint / 25.0 - 0.03247649761459988) < 5e-15

# The old classwise constant is exactly 3/8 of the stronger route+perimeter floor.
assert abs(C - 3.0 * (2.0 * s2 + g) / 4.0) < 1e-15
assert abs(M - (C + 5.0 * M / 8.0)) < 1e-15
assert abs(3.0 * (5.0 * M / 8.0) / 5.0 - C) < 1e-15

# Equality point for the stable classwise endpoint.
F0 = M / 8.0
r0 = 0.0
E0 = 3.0 * F0 + r0
P0 = 5.0 * F0 + r0
L0 = C
assert abs(E0 - C) < 1e-15
assert abs(P0 - 5.0 * M / 8.0) < 1e-15
assert abs(L0 + P0 - M) < 1e-15
assert abs((F0 - r0) - M / 8.0) < 1e-15

# Randomized stability check.  Variables are normalized by D:
# E=3F+r, P=5F+r, r=Q-f>=0. Construct samples near the feasible endpoint,
# then verify the derived F, r, and pentagon-expression bounds.
rng = random.Random(2026091806)
checked = 0
for _ in range(400_000):
    eps = rng.random() * 0.04
    F = max(0.0, M / 8.0 - eps) + rng.random() * (2.0 * eps + 1e-9)
    r = rng.random() * (4.0 * eps + 1e-9)
    E = 3.0 * F + r
    P = 5.0 * F + r
    if E > C + eps + 1e-12:
        continue
    lo = max(0.0, M - P)
    hi = C + eps
    if lo > hi + 1e-12:
        continue
    L = lo + rng.random() * max(0.0, hi - lo)
    assert L + P + 1e-10 >= M
    checked += 1
    assert P + 1e-10 >= 5.0 * M / 8.0 - eps
    assert F + 1e-10 >= M / 8.0 - eps
    assert r <= 4.0 * eps + 1e-10
    # 2f-Q = F-r is a guaranteed lower bound for the pentagon density.
    assert F - r + 1e-10 >= M / 8.0 - 5.0 * eps
assert checked > 10_000

# Exact singleton/rhombic decomposition minimax. If tau_D>=tau and
# rho+sigma=2*tau_D, then rho>=tau or sigma>=tau.
for _ in range(300_000):
    tau_D = tau + rng.random() * 4.0
    rho = rng.random() * 2.0 * tau_D
    sigma = 2.0 * tau_D - rho
    assert rho >= tau - 1e-12 or sigma >= tau - 1e-12
    if rho >= tau:
        assert rho / 2.0 >= tau / 2.0 - 1e-12
    else:
        assert sigma >= tau - 1e-12

# Mantel-deficit identity and monotonicity in sigma and sqrt(R4).
for _ in range(300_000):
    rootR = s2 + rng.random() * 3.0
    sigma = tau + rng.random() * 3.0
    TR = 2.0 * rootR + sigma / 2.0
    lhs = TR * TR / 4.0 - rootR * rootR
    rhs = sigma * rootR / 2.0 + sigma * sigma / 16.0
    assert abs(lhs - rhs) <= 1e-11 * max(1.0, abs(rhs))
    assert rhs + 1e-12 >= mantel

# Rhombic-pentagon incidence floor in the stable window.
for _ in range(200_000):
    eps = rng.random() * (I5_endpoint / 25.0)
    pent_expr = M / 8.0 - 5.0 * eps
    rho = rng.random() * tau
    I5 = 5.0 * pent_expr - rho
    claimed = I5_endpoint - 25.0 * eps
    assert I5 + 1e-12 >= claimed
    assert claimed >= -1e-12

# Multi-rhombic pentagon floor: X2 >= (I5-Q)/4 and balanced Q <= M/8+3 eps.
gamma0 = 2.0 * s2 - PI / 2.0
x2_endpoint = gamma0 / 4.0
x2_eps_max = gamma0 / 28.0
assert abs(gamma0 - 0.33382928693301817) < 5e-15
assert abs(x2_endpoint - 0.08345732173325454) < 5e-15
assert abs(x2_eps_max - 0.011922474533322078) < 5e-15
for _ in range(200_000):
    eps = rng.random() * x2_eps_max
    q_cap = M / 8.0 + 3.0 * eps
    i5_floor = I5_endpoint - 25.0 * eps
    x2_floor = (i5_floor - q_cap) / 4.0
    claimed = x2_endpoint - 7.0 * eps
    assert abs(x2_floor - claimed) < 1e-12
    assert claimed >= -1e-12

print("PASS terminal FREE route/perimeter train-pentagon certificate")
print(f"s2={s2:.15f}")
print(f"M_g={M:.15f}")
print(f"C_g={C:.15f}")
print(f"tau_g={tau:.15f}")
print(f"singleton floor={tau/2:.15f}")
print(f"rhombic Mantel deficit={mantel:.15f}")
print(f"endpoint pentagon expression={p5_endpoint:.15f}")
print(f"endpoint rhombus/pentagon incidences={I5_endpoint:.15f}")
print(f"empty >=2-rhombus pentagon floor={x2_endpoint:.15f}")
print(f"X2 epsilon window={x2_eps_max:.15f}")
print(f"random stability instances={checked}")
