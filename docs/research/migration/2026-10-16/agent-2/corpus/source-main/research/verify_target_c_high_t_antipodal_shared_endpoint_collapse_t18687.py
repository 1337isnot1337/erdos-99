#!/usr/bin/env python3
"""Arithmetic/asymptotic regressions for antipodal shared-endpoint collapse."""

from fractions import Fraction
from math import acos, asin

c1 = Fraction(791, 320_000_000)
kappa = 4.0 * (3.0 ** (1.0 / 8.0))
rho_bundle = float(c1) / (4.0 * kappa)

assert abs(float(c1) - 0.000002471875) < 1e-18
assert 1.3e-7 < rho_bundle < 1.4e-7


def theta_D(D: float) -> float:
    eta = (3.0 ** 0.25) * (D ** 0.5)
    return 2.0 * acos(D / (D + 2.0 * eta))


def delta_D(D: float) -> float:
    return 2.0 * asin(1.0 / (2.0 * D))


# Verify the two scales used in the packing argument:
# shared-endpoint angle O(D^-1/4), C67 spacing ~ D^-1.
for D in (1e8, 1e12, 1e16):
    assert theta_D(D) > 0.0
    assert delta_D(D) > 0.0

D = 1e16
assert abs(theta_D(D) * D**0.25 - kappa) < 5e-4
assert abs(delta_D(D) * D - 1.0) < 1e-12

# A representative shrinking row window demonstrates the exact capacity scaling:
# ell_D=o(1) and delta_D~1/D imply ell_D/delta_D=o(D).
# The proof itself permits any omega_D=o(1); this is only a regression example.
for D in (1e8, 1e12, 1e16):
    omega = D ** (-0.05)
    ell = omega + 2.0 * theta_D(D)
    capacity_ratio = (1.0 + ell / delta_D(D)) / D
    assert capacity_ratio < omega + 2.0 * theta_D(D) + 1e-3

assert (1.0 + (D**(-0.05) + 2.0 * theta_D(D)) / delta_D(D)) / D < 0.2

print("PASS: antipodal shared-endpoint collapse arithmetic regressions")
print(f"c1={float(c1):.12g}")
print(f"kappa={kappa:.12g}")
print(f"rho_bundle={rho_bundle:.12g}")
print(f"Ddelta(D=1e16)={delta_D(D)*D:.12g}")
print(f"D^1/4 Theta(D=1e16)={theta_D(D)*D**0.25:.12g}")
