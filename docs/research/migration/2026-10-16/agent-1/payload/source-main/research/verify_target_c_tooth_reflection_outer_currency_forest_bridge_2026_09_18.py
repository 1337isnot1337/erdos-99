#!/usr/bin/env python3
"""Arithmetic/regression certificate for the outer-currency/forest bridge.

This script checks only the scalar and constant algebra in the proof-only theorem.
It does not certify the geometric dependency theorems.
"""

from __future__ import annotations

import math
import random

H_STAR = math.sqrt(303.0) / 52.0
C_STAR = 0.129220199818177
B_STAR = math.sin(C_STAR / 2.0)
DELTA_STAR = 2.0 * (1.0 - math.cos(C_STAR / 2.0))
RHO_STAR = 2.0 - math.sqrt(2.0)


def alpha(K: float) -> float:
    return 1.0 - H_STAR / K


def c_out(K: float) -> float:
    return math.sqrt(alpha(K) * B_STAR / 6.0)


def d_floor(theta: float, K: float, D: float) -> float:
    return max(
        0.0,
        2.0
        - 2.0
        * (1.0 + K / D)
        * max(math.cos(theta / 2.0), math.sin(theta / 2.0)),
    )


def b_axis(theta: float) -> float:
    return min(math.sin(theta / 2.0), math.cos(theta / 2.0))


# Basic constants.
assert 0.3347 < H_STAR < 0.3348
assert 0.0645 < B_STAR < 0.0647
assert 0.0041 < DELTA_STAR < 0.0043
assert abs(c_out(1.0) - 0.0846090036211229) < 2e-15
assert abs(c_out(400.0) - 0.103691147605043) < 2e-15
assert abs(math.sqrt(B_STAR / 6.0) - 0.103734562859954) < 2e-15
assert abs(1.0 + DELTA_STAR / 4.0 - 1.001043253258118) < 2e-15

# Angle-adaptive floors improve from c_* to pi/2 in the relevant interval.
last_d = -1.0
last_b = -1.0
for j in range(20001):
    theta = C_STAR + (math.pi / 2.0 - C_STAR) * j / 20000.0
    d = 2.0 - 2.0 * max(math.cos(theta / 2.0), math.sin(theta / 2.0))
    b = b_axis(theta)
    assert d + 1e-14 >= last_d
    assert b + 1e-14 >= last_b
    last_d, last_b = d, b
assert abs(last_d - RHO_STAR) < 2e-14
assert abs(last_b - 1.0 / math.sqrt(2.0)) < 2e-14

# The finite common defect floor never exceeds either orientation-specific bound.
for D in (1e5, 1e7, 1e10):
    for K in (1.0, 10.0, 400.0):
        for j in range(1001):
            theta = C_STAR + (math.pi / 2.0 - C_STAR) * j / 1000.0
            floor = d_floor(theta, K, D)
            same = 2.0 - 2.0 * (1.0 + K / D) * math.cos(theta / 2.0)
            opp = 2.0 - 2.0 * (1.0 + K / D) * math.sin(theta / 2.0)
            assert floor <= max(0.0, same) + 2e-14
            assert floor <= max(0.0, opp) + 2e-14

# Exact scalar minimax:
# max{E/s-B, B/2} >= E/(3s) for all E,s>0 and B>=0.
rng = random.Random(0xE99)
for _ in range(500_000):
    E = 10 ** rng.uniform(-3.0, 9.0)
    s = 10 ** rng.uniform(-3.0, 6.0)
    B = 10 ** rng.uniform(-5.0, 9.0) if rng.random() < 0.95 else 0.0
    lhs = max(E / s - B, B / 2.0)
    rhs = E / (3.0 * s)
    assert lhs + 2e-12 * max(1.0, abs(lhs), abs(rhs)) >= rhs

# Equality occurs at B=2E/(3s).
for E, s in ((1.0, 1.0), (17.0, 2.5), (1e8, 1234.0)):
    B = 2.0 * E / (3.0 * s)
    lhs = max(E / s - B, B / 2.0)
    rhs = E / (3.0 * s)
    assert abs(lhs - rhs) <= 1e-12 * max(1.0, rhs)

# Balancing E/(3s) against b*s gives sqrt(bE/3).
for theta in (C_STAR, 0.3, 0.7, 1.0, math.pi / 2.0):
    b = b_axis(theta)
    for E in (10.0, 1e3, 1e8):
        s = math.sqrt(E / (3.0 * b))
        target = math.sqrt(b * E / 3.0)
        assert abs(E / (3.0 * s) - target) <= 1e-12 * max(1.0, target)
        assert abs(b * s - target) <= 1e-12 * max(1.0, target)

print(f"h_*={H_STAR:.15f}")
print(f"c_*={C_STAR:.15f}")
print(f"b_*={B_STAR:.15f}")
print(f"delta_*={DELTA_STAR:.15f}")
print(f"C_out(K=1)={c_out(1.0):.15f}")
print(f"C_out(K=400)={c_out(400.0):.15f}")
print(f"C_out(envelope)={math.sqrt(B_STAR / 6.0):.15f}")
print("outer-currency/forest scalar certificate: PASS")
