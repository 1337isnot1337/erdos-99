#!/usr/bin/env python3
"""Finite parity regression for the odd-face two-projective-window lemma."""

from __future__ import annotations

import math


def coefficient_patterns(d: int):
    """All ideal signed coefficients a,b from assigning d edges to two lines."""
    out = set()
    for n_u in range(d + 1):
        n_v = d - n_u
        for p_u in range(n_u + 1):
            a = 2 * p_u - n_u
            for p_v in range(n_v + 1):
                b = 2 * p_v - n_v
                out.add((a, b, n_u, n_v))
    return out


for d in range(3, 52, 2):
    for a, b, n_u, n_v in coefficient_patterns(d):
        assert (a - n_u) % 2 == 0
        assert (b - n_v) % 2 == 0
        assert (n_u + n_v) % 2 == 1
        # Hence a,b have opposite parity.  If one vanishes, the other is a
        # nonzero odd integer.  If both are nonzero, |a| and |b| are unequal
        # integers.  In either case min_{unit u,v}|a u+b v| >= 1.
        if a == 0:
            assert abs(b) >= 1
        elif b == 0:
            assert abs(a) >= 1
        else:
            assert abs(abs(a) - abs(b)) >= 1

for d in (3, 5, 7, 9, 11, 13, 15):
    eps = 2.0 * math.asin(1.0 / (2.0 * d))
    print(f"d={d:2d} epsilon_d={eps:.15f} rad = {eps*180/math.pi:.12f} deg")

EPS5 = 2.0 * math.asin(0.1)
assert 0.20033 < EPS5 < 0.20034
assert 11.4783 < EPS5 * 180.0 / math.pi < 11.4784

DELTA2 = math.pi / (2.0 * math.sqrt(3.0))
S2 = math.sqrt(DELTA2)
P5_MIN_INTERFACE = 2.0 * S2 - (math.pi - 2.0)
OFF_TRAIN_MIN = P5_MIN_INTERFACE / 2.0
assert 0.76302 < P5_MIN_INTERFACE < 0.76304
assert 0.38151 < OFF_TRAIN_MIN < 0.38153

print(f"pentagon radius epsilon_5={EPS5:.15f} rad")
print(f"minimal-interface p5/D floor={P5_MIN_INTERFACE:.15f}")
print(f"off-two-window train/D floor={OFF_TRAIN_MIN:.15f}")
print("odd-face two-window parity regression: PASS")
