#!/usr/bin/env python3
"""Regression checks for the near-diametrical-terminal / uniform-corridor dichotomy."""

from fractions import Fraction
from math import asin, cos, pi, sin

c = Fraction(113, 5_000_000)
nu = c / 2

z0 = 20477 / 10000
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)

nu_f = float(nu)
terminal_coeff = cos(nu_f / 2)
terminal_angle = pi - nu_f
diamond_coeff = 0.5 * sin(nu_f / 2)

# The parent threshold is safely inside the host-margin near-antipodal regime.
assert nu == Fraction(113, 10_000_000)
assert nu_f == 1.13e-5
assert nu_f < gammaH / 1000
assert 2 * (gammaH - gammaH / 4) > nu_f

# A TT pair with projective gap eta < nu cannot use the ordinary-small lift.
# In the surviving lift Delta=pi-eta, the ideal terminal rung has length
# D*sin(Delta/2)=D*cos(eta/2), minimized as eta approaches nu.
for k in range(1001):
    eta = nu_f * k / 1001
    Delta = pi - eta
    assert Delta > pi - nu_f
    assert abs(sin(Delta / 2) - cos(eta / 2)) < 2e-15
    assert cos(eta / 2) >= terminal_coeff

assert 0.99999999998 < terminal_coeff < 1
assert 1.5e-11 < 1 - terminal_coeff < 1.7e-11
assert 179.9993 < terminal_angle * 180 / pi < 180
assert 2.824e-6 < diamond_coeff < 2.826e-6

# Hole-free block packing used after the TT obstruction is removed.
# If P good indices and H holes occupy one physical interval, at most H+1
# runs occur and K disjoint m-blocks satisfy
#     K*m >= P-(H+1)(m-1).
def run_lengths(mask, n):
    out = []
    q = 0
    for i in range(n):
        if (mask >> i) & 1:
            q += 1
        elif q:
            out.append(q)
            q = 0
    if q:
        out.append(q)
    return out

for n in range(1, 13):
    for mask in range(1 << n):
        P = mask.bit_count()
        H = n - P
        runs = run_lengths(mask, n)
        for m in range(1, n + 2):
            K = sum(q // m for q in runs)
            assert K * m >= P - (H + 1) * (m - 1)

# Once no TT pair is below nu, TT pairs have gap >=nu exactly while the
# full-parent theorem gives non-TT pairs >=nu-o(1).  A safe uniform finite
# aperture nu/2 is therefore eventually available to the whole population.
rho_safe = nu_f / 2
assert 0 < rho_safe < nu_f < gammaH
compression_factor = 2 / sin(rho_safe)
assert 353_000 < compression_factor < 355_000

# The same fixed safe aperture makes the central-diamond crossing-point bound
# uniform over every separator in the selected corridor:
# |p_i-o| < (1+2/sin(rho_safe))*L_D.
# Unlike a shrinking-aperture estimate, the coefficient is source-independent.
crossing_localization_factor = 1 + compression_factor
assert 353_000 < crossing_localization_factor < 355_000

print("PASS: near-diametrical terminal / uniform fixed-aperture corridor regressions")
print(f"nu={nu_f:.15g}")
print(f"cH={cH:.15g}")
print(f"gammaH={gammaH:.15g}")
print(f"terminal_diameter_coeff={terminal_coeff:.18g}")
print(f"terminal_diameter_deficit={1-terminal_coeff:.18g}")
print(f"terminal_angle_floor_rad={terminal_angle:.15g}")
print(f"terminal_angle_floor_deg={terminal_angle*180/pi:.15g}")
print(f"uniform_diamond_radius_coeff={diamond_coeff:.15g}")
print(f"safe_compression_factor={compression_factor:.15g}")
print(f"uniform_crossing_localization_factor={crossing_localization_factor:.15g}")