#!/usr/bin/env python3
"""Arithmetic certificate for audited-working Target C Section 166.

This script checks only the explicit scalar inequalities in Section 166. It does not
certify the geometric or measure-theoretic arguments.
"""

import math

EPS = 1.0e-4
s2 = math.sqrt(math.pi / (2.0 * math.sqrt(3.0)))
A = 2.0 * s2 + EPS
G = A * A / 4.0 - s2 * s2
M = 4.0 * s2 * s2 / A
delta = G
L = M / 2.0 - (1.0 + 3.0 * math.sqrt(2.0)) * math.sqrt(delta)

# Worst-case ratio bound using only a >= L, b >= L/2, a,b <= A.
ratio_term = math.sqrt(A / (L / 2.0)) + math.sqrt(A / L)
rho = 2.0 * delta
selected_lower = 1.5 * L
robust_upper = 2.0 / math.sqrt(3.0) + (ratio_term + 4.0) * math.sqrt(rho)

C146 = (4.0 / 9.0) * (math.pi + s2)
C166 = C146 + (2.0 / 9.0) * EPS

assert 0.95 < s2 < 0.96
assert G < 1.0e-4
assert M > 1.8999
assert L > 0.8975
assert ratio_term < 4.0
assert math.sqrt(rho) < 0.01415
assert selected_lower > 1.34625
assert robust_upper < 1.2682
assert selected_lower > robust_upper

print(f"s2 = {s2:.15f}")
print(f"G_max = {G:.15e}")
print(f"dominant_orbit_mass_min = {M:.15f}")
print(f"retained_shore_mass_min = {L:.15f}")
print(f"ratio_term_max = {ratio_term:.15f}")
print(f"rho_max = {rho:.15e}")
print(f"selected_pair_lower = {selected_lower:.15f}")
print(f"robust_grid_upper = {robust_upper:.15f}")
print(f"contradiction_margin = {selected_lower - robust_upper:.15f}")
print(f"section_166_weighted_floor = {C166:.15f}")
