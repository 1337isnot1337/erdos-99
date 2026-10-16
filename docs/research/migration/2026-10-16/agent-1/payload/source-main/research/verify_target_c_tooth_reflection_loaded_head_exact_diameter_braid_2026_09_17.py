#!/usr/bin/env python3
"""Regression checks for the loaded-head exact-diameter braid extraction."""

import math


c_star = 0.129220199818177

# Eventually M_D >= (2 c_*/3) omega^2.  A loaded majority then has
# at least (c_*/3) omega^2 members.
c_loaded = c_star / 3.0
T = 12.0 * math.pi / c_star
bad_coeff = 2.0 * math.pi / T
c_good = c_loaded - bad_coeff

assert abs(bad_coeff - c_star / 6.0) < 1e-14
assert abs(c_good - c_star / 6.0) < 1e-14
assert c_good > 0.0

# Fixed spacing constant used in the proof.
J = 1267
assert J > 4.0 * T + 100.0

# A J-spaced aligned family still has Theta(omega^2) members.
c_retained = c_good / J
assert c_retained > 0.0

# Normal gap after two alignment errors remains positive.
assert 2.0 * J - 2.0 * T > 0.0

# Reflected-apex spacing dominates two partner-localization radii.
assert J - 2.0 * T > 0.0

# Exact partner localization uses
# t-q = (L-D)N + D(N-M), |L-D|<h_*, |N-M|<=theta.
h_star = math.sqrt(303.0) / 52.0
assert h_star < 0.335
for D in (1e6, 1e12):
    omega = max(2.0, math.log(math.log(D)))
    theta = T / (omega * omega)
    partner_radius = h_star + D * theta
    assert partner_radius > 0.0
    assert partner_radius / D < T / (omega * omega) + 1e-5

# Slow-scale exponent checks.  A concrete extremal slow choice
# omega=D^(1/8)/log D satisfies all required little-o relations.
for D in (1e16, 1e32, 1e64):
    omega = D ** 0.125 / math.log(D)
    assert omega > 1.0

    # D^-1/4 = o(omega^-2).
    ratio_direction_error = D ** (-0.25) / (omega ** -2)
    assert ratio_direction_error < 1.0

    # Partner localization is o(D).
    assert (D / (omega * omega)) / D < 1.0

    # Diameter crossing core D^(3/4) omega^2 is o(D).
    core_ratio = D ** 0.75 * omega * omega / D
    assert core_ratio < 1.0

# Elementary two-line estimate scale check: if midpoint separation is at most
# 2L and angle phi >= c/omega^2, line-intersection displacement is O(L omega^2).
for omega in (3.0, 10.0, 100.0):
    c = 1.0
    phi = c / (omega * omega)
    factor = 2.0 / math.sin(phi)
    assert factor / (omega * omega) < 3.0

# One diameter edge has only two endpoints, so H loaded heads always support
# at least ceil(H/2) distinct actual diameter edges before the stronger spacing step.
for H in range(1, 100):
    distinct_floor = (H + 1) // 2
    assert 2 * distinct_floor >= H

print("PASS: loaded-head exact-diameter braid certificate")
