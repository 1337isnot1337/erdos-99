#!/usr/bin/env python3
"""Regression checks for the FREE-MODULE rigid-translation gate lemma.

This certificate checks the fixed constants and the asymptotic exponent comparisons
used in the proof note. It does not promote the proof-only result to canonical state.
"""

from fractions import Fraction
import math

h = math.sqrt(303) / 52
C_A = 2 * 3 ** (5 / 8) + 4 * 3 ** (1 / 8) + 1
C_N = 2 * C_A

assert 0 < h < 0.335 < 0.5
assert C_A < 9.563
assert C_N < 19.126

# Clearance choice epsilon_D=D^(-1/3).
# The negative radial term has scale D*epsilon=D^(2/3), while the angular
# correction from phi=O(D^-1/4) has scale D*phi^2=D^(1/2).
assert Fraction(2, 3) > Fraction(1, 2)

# Support depth of every blocker relative to the canonical farthest-head normal:
# D * phi^2 = O(D^(1/2)).
assert 1 + 2 * (-Fraction(1, 4)) == Fraction(1, 2)

# A cap of depth O(D^(1/2)) in a radius D/2+O(D^(1/2)) disk has transverse
# scale sqrt(D * D^(1/2)) = D^(3/4), hence is subdiametral.
assert (1 + Fraction(1, 2)) / 2 == Fraction(3, 4)
assert Fraction(3, 4) < 1

# Finite numerical sanity check of the conservative blocker-clearance bound.
# We evaluate the cancellation-free margin
#   2 D eps - eps^2 - (D+h)(h+eps) C_N^2 / sqrt(D).
# Asymptotics, not this threshold, prove the theorem.
D = 10**12
eps = D ** (-1 / 3)
t = h + eps
clearance_margin = (
    2 * D * eps
    - eps**2
    - (D + h) * t * C_N**2 / math.sqrt(D)
)
assert clearance_margin > 0

# Conservative cap-diameter sanity check at the same D.
eta = 3 ** 0.25 * math.sqrt(D)
B = h + (C_N**2 / 2) * (math.sqrt(D) + h / math.sqrt(D))
R = D / 2 + eta
x_min = D / 2 - eta - h - B - 0.5
transverse = math.sqrt(R * R - x_min * x_min)
cap_pair_plus_translation = 2 * transverse + (B + 0.5) + 1
assert cap_pair_plus_translation < D

# Gate length: original |z-v| <= 1+s_* < 1+delta+D^(-1/3), with delta<h<1/2.
assert 1 + h < 1.5

print("PASS: free-module rigid near-contact gate certificate")
print(f"h_*={h:.15f}")
print(f"C_A={C_A:.15f}")
print(f"C_N={C_N:.15f}")
print(f"clearance margin at D=1e12: {clearance_margin:.6e}")
print(f"cap pair ratio at D=1e12: {cap_pair_plus_translation / D:.6e}")
