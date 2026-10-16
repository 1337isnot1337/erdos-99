#!/usr/bin/env python3
"""Regression checks for the high-t blocker matching/star-collapse note.

This script checks only arithmetic/asymptotic constants used in the proof note.
The geometric and graph-theoretic implications are proved in the Markdown note.
"""

from fractions import Fraction
from math import acos, asin, pi

c0 = Fraction(113, 20_000_000)
c_star = Fraction(7, 8) * c0
c1 = Fraction(1, 2) * c_star
gamma = Fraction(113, 640_000_000)

assert c_star == Fraction(791, 160_000_000)
assert c1 == Fraction(791, 320_000_000)
assert gamma == Fraction(113, 640_000_000)
assert abs(float(c_star) - 0.00000494375) < 1e-18
assert abs(float(c1) - 0.000002471875) < 1e-18

kappa = 4.0 * (3.0 ** (1.0 / 8.0))
rho_strong = float(c1) / kappa
rho_antipodal_bundle = rho_strong / 4.0

assert 5.3e-7 < rho_strong < 5.5e-7
assert 1.3e-7 < rho_antipodal_bundle < 1.4e-7


def theta_D(D: float) -> float:
    eta = (3.0 ** 0.25) * (D ** 0.5)
    return 2.0 * acos(D / (D + 2.0 * eta))


def delta_D(D: float) -> float:
    return 2.0 * asin(1.0 / (2.0 * D))


def degree_cap(D: float) -> int:
    cap = min(pi / 3.0, theta_D(D))
    return 1 + int(cap // delta_D(D))


# The exact formulas have the claimed asymptotic scales.
# Use rapidly growing D so the convergence is visible without fragile tolerances.
Ds = [10.0**8, 10.0**12, 10.0**16]
theta_ratios = [theta_D(D) * (D ** 0.25) for D in Ds]
delta_ratios = [delta_D(D) * D for D in Ds]
degree_ratios = [degree_cap(D) / (D ** 0.75) for D in Ds]

assert abs(theta_ratios[-1] - kappa) < 5e-4
assert abs(delta_ratios[-1] - 1.0) < 1e-12
assert abs(degree_ratios[-1] - kappa) < 5e-4

# Midpoint localization scale L_D=(D eta+eta^2)^(1/2) has coefficient 3^(1/8).
a = 3.0 ** 0.25
midpoint_coeff_limit = 3.0 ** (1.0 / 8.0)
D = 10.0**16
eta = a * (D ** 0.5)
L = (D * eta + eta * eta) ** 0.5
assert abs(L / (D ** 0.75) - midpoint_coeff_limit) < 1e-7
assert L / D < 1e-3

# A forest with m edges and maximum degree Delta can be edge-colored with Delta
# colors, so one color class has at least m/Delta edges. The theorem therefore
# has the displayed D^(1/4) exponent from D / D^(3/4).
assert abs(1.0 - 0.75 - 0.25) < 1e-15

print("PASS: high-t blocker matching/star-collapse arithmetic regressions")
print(f"c_star={float(c_star):.12g}")
print(f"c1={float(c1):.12g}")
print(f"kappa={kappa:.12g}")
print(f"rho_strong={rho_strong:.12g}")
print(f"rho_antipodal_bundle={rho_antipodal_bundle:.12g}")
print(f"theta_ratio(D=1e16)={theta_ratios[-1]:.12g}")
print(f"degree_ratio(D=1e16)={degree_ratios[-1]:.12g}")
