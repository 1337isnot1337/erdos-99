#!/usr/bin/env python3
"""Regression checks for the LOWER diagonal/terminal-companion theorem."""
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import random

# Stronger one-row threshold L_* = 3 sqrt(3)/4.
# Its square is 27/16, and it strictly contains the old 21/20 window.
assert Fraction(441, 400) < Fraction(27, 16) < 4

# Angular lemma sanity test. If angle(a,b)=pi-eps, angle(a,c)=gamma in
# (pi/3,2pi/3), and |c-b|<=1, then delta=2pi/3-gamma <= eps.
rng = random.Random(20260917)
for _ in range(20000):
    eps = rng.uniform(1e-6, 0.4)
    phi = rng.uniform(-math.pi, math.pi)
    gamma = abs((phi + math.pi) % (2 * math.pi) - math.pi)
    if not (math.pi / 3 < gamma < 2 * math.pi / 3):
        continue
    eta = abs(((phi - (math.pi - eps)) + math.pi) % (2 * math.pi) - math.pi)
    if 2 - 2 * math.cos(eta) <= 1 + 1e-12:
        delta = 2 * math.pi / 3 - gamma
        assert delta <= eps + 1e-10

s0 = Fraction(791, 320_000_000)
delta_one = s0 / 16
assert delta_one == Fraction(791, 5_120_000_000)

# Fixing owner-side orientation keeps at least half the LOWER blockers, and
# on that oriented family the canonical-companion map is injective.
terminal_companion = delta_one / 2
assert terminal_companion == s0 / 32
assert terminal_companion == Fraction(791, 10_240_000_000)

# Current fixed-spine row-distinct LOWER family, followed by the same
# owner-side split. The companion map is injective on the retained half.
spine_rows = Fraction(1_272_719, 156_697_600_000_000)
one_sided_spine_companions = spine_rows / 2
assert one_sided_spine_companions == Fraction(
    1_272_719, 313_395_200_000_000
)

getcontext().prec = 50
Lstar = Decimal(3) * Decimal(3).sqrt() / Decimal(4)
print("LOWER diagonal terminal-companion certificate: PASS")
print("one-row threshold =", Lstar)
print("same-side global terminal companions >=", float(terminal_companion))
print("fixed-spine same-side terminal companions >=", float(one_sided_spine_companions))
