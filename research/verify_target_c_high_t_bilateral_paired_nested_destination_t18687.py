#!/usr/bin/env python3
"""Regression checks for the bilateral paired nested-destination theorem.

This script certifies only finite combinatorics and displayed scalar arithmetic.
The geometric inputs are theorem dependencies named in the companion Markdown note.
"""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import asin, pi, sin, sqrt

c0 = Fraction(113, 20_000_000)
lam = Fraction(9, 10) * c0
theta = lam / 3

assert lam == Fraction(1017, 200_000_000)
assert theta == Fraction(339, 200_000_000)
assert float(lam) == 5.085e-6
assert float(theta) == 1.695e-6
assert float(2 * theta) == 3.39e-6
assert abs(sin(float(theta)) - float(theta)) < 1e-17

# If terminal membership in each nested lane is a prefix, the paired destination
# word has at most the three ordered runs TT -> MIX -> OO.  Exhaust all cutoff
# pairs through N=60 and verify the N/3 pigeonhole exactly.
for N in range(1, 61):
    for rA in range(N + 1):
        for rB in range(N + 1):
            patterns = []
            for s in range(1, N + 1):
                a_terminal = s <= rA
                b_terminal = s <= rB
                if a_terminal and b_terminal:
                    pattern = "TT"
                elif a_terminal or b_terminal:
                    pattern = "MIX"
                else:
                    pattern = "OO"
                patterns.append(pattern)

            runs = []
            for pattern in patterns:
                if not runs or runs[-1][0] != pattern:
                    runs.append([pattern, 1])
                else:
                    runs[-1][1] += 1

            assert len(runs) <= 3
            order = [run[0] for run in runs]
            assert order == [x for x in ("TT", "MIX", "OO") if x in order]
            assert max(run[1] for run in runs) * 3 >= N

# Independently nonincreasing support-end sequences in the two birth lanes make
# each lane, their union envelope, and their common-support intersection strictly
# nested because the common birth index increases.  Exhaust small finite models.
for N in range(1, 6):
    k = N + 1
    m = k + 3
    sequences = [
        tuple(reversed(seq))
        for seq in combinations_with_replacement(range(k, m + 1), N)
    ]
    starts = list(range(1, N + 1))

    for a_ends in sequences:
        for b_ends in sequences:
            lane_a = [
                set(range(starts[s], a_ends[s] + 1)) for s in range(N)
            ]
            lane_b = [
                set(range(starts[s], b_ends[s] + 1)) for s in range(N)
            ]
            envelope = [lane_a[s] | lane_b[s] for s in range(N)]
            common = [lane_a[s] & lane_b[s] for s in range(N)]

            for family in (lane_a, lane_b, envelope, common):
                for s in range(N - 1):
                    assert family[s + 1] < family[s]

# Large-D numerical regression for the factor-two TT direction-packing bound.
# A 0.999 density factor models an arbitrary finite -o(D) margin; the theorem's
# asymptotic limit removes that factor.
def midpoint_radius(D: float) -> float:
    eta = 3 ** 0.25 * sqrt(D)
    return sqrt(D * eta + eta * eta)


def radial_error(D: float) -> float:
    L = midpoint_radius(D)
    return asin(L / (D / 2 - L))


th = float(theta)
ratios = []
for D in (1e28, 1e32, 1e36):
    M = 0.999 * th * D
    delta = 2 * asin(1 / (2 * D))
    angle_bound = min(pi / 3, (2 * M - 1) * delta) - 2 * radial_error(D)
    assert 0 < angle_bound < 2 * th
    ratios.append(angle_bound / (2 * th))

    chord_bound = sin(angle_bound / 2) - 2 * midpoint_radius(D) / D
    assert chord_bound > 0

assert ratios[0] > 0.86
assert ratios[1] > 0.985
assert ratios[2] > 0.997
assert ratios[0] < ratios[1] < ratios[2]

print("PASS: bilateral paired nested-destination regressions")
print(f"c0={float(c0):.12g}")
print(f"lambda90={float(lam):.12g}")
print(f"largest_regime_density90={float(theta):.12g}")
print(f"TT_angle_limit90={float(2 * theta):.12g}")
print(f"TT_chord_limit90=sin(theta)={sin(th):.12g}")
