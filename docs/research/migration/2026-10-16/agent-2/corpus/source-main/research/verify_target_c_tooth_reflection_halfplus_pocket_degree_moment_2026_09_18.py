#!/usr/bin/env python3
"""Arithmetic/regression checks for half-plus outer-pocket degree moment."""
from __future__ import annotations

import math
import random

SQ3 = math.sqrt(3.0)
PI = math.pi
h = math.sqrt(303.0) / 52.0
c_star = 0.129220199818177
Delta = 2.0 * (1.0 - math.cos(c_star / 2.0))


def nu(K: float) -> float:
    return 1.0 + Delta * (1.0 - h / K) / 4.0


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for mask in range(1 << (n - 1)):
        parts = []
        last = 0
        for i in range(n - 1):
            if mask & (1 << i):
                parts.append(i + 1 - last)
                last = i + 1
        parts.append(n - last)
        yield tuple(parts)


# Triangular pockets have strict subunit Oler capacity.
assert 4.0 / (PI * SQ3) < 1.0

# Exact composition maximum in (2.6), exhaustively for a useful finite range.
for d in range(1, 15):
    vals = [sum((r + 2) ** 2 for r in comp) for comp in compositions(d)]
    exact = max(vals)
    claimed = max((d + 2) ** 2, 9 * d)
    assert exact == claimed, (d, exact, claimed)

# Randomized check of moment and scalar bounds for positive pocket excess vectors.
rng = random.Random(20260918)
for _ in range(200_000):
    t = rng.randint(0, 20)
    rs = [rng.randint(1, 25) for _ in range(t)]
    d = sum(rs)
    if d == 0:
        continue
    S2 = sum(r * r for r in rs)
    ell2 = sum((r + 2) ** 2 for r in rs)
    assert ell2 == S2 + 4 * d + 4 * t
    assert t <= d
    assert ell2 <= S2 + 8 * d
    assert ell2 <= max((d + 2) ** 2, 9 * d)
    assert S2 <= d * d

# Report and verify the truncation-free K=400 constants.
nu400 = nu(400.0)
coef400 = math.sqrt(PI * SQ3 * nu400)
assert abs(nu400 - 1.001042380190805) < 5e-15
assert abs(coef400 - 2.333895905623207) < 5e-15

nu_inf = 1.0 + Delta / 4.0
coef_inf = math.sqrt(PI * SQ3 * nu_inf)
second_inf = PI * SQ3 * nu_inf
detour_inf = (1.0 - 2.0 / PI) * coef_inf
assert abs(nu_inf - 1.0010432532581182) < 5e-15
assert abs(coef_inf - 2.333896923386203) < 5e-15
assert abs(second_inf - 5.447074848991583) < 5e-15
assert abs(detour_inf - 0.8480919952906798) < 5e-15

# Finite scalar implication: if d>=4 and internal population N fits the pocket
# bound, then d >= sqrt(pi*sqrt(3)*N)-2.
for _ in range(100_000):
    d = rng.randint(4, 100_000)
    capacity = (d + 2) ** 2 / (PI * SQ3)
    N = rng.random() * capacity
    assert d + 1e-12 >= math.sqrt(PI * SQ3 * N) - 2.0

# Dido coefficient has its unique numerical maximum at theta=pi/2.
def dido_f(theta: float) -> float:
    return (theta - math.sin(theta) * math.cos(theta)) / (4.0 * theta * theta)

fm = dido_f(PI / 2.0)
assert abs(fm - 1.0 / (2.0 * PI)) < 1e-15
for i in range(1, 10000):
    theta = PI * i / 10000.0
    assert dido_f(theta) <= fm + 1e-14

# Equality-scale constant identity used in (5.4).
for K in [10.0, 50.0, 400.0, 1e8]:
    m = nu(K)
    assert m > 0
    cc = math.sqrt(PI * SQ3 * m)
    lhs = cc * cc / (2.0 * PI)
    rhs = SQ3 * m / 2.0
    assert abs(lhs - rhs) <= 1e-12 * max(1.0, abs(rhs))

print("PASS half-plus pocket degree-moment certificate")
print(f"h_*={h:.15f}")
print(f"delta_*={Delta:.15f}")
print(f"nu_400={nu400:.15f}")
print(f"sqrt(pi*sqrt(3)*nu_400)={coef400:.15f}")
print(f"nu_inf={nu_inf:.15f}")
print(f"sqrt(pi*sqrt(3)*nu_inf)={coef_inf:.15f}")
print(f"pi*sqrt(3)*nu_inf={second_inf:.15f}")
print(f"critical detour coefficient={detour_inf:.15f}")
