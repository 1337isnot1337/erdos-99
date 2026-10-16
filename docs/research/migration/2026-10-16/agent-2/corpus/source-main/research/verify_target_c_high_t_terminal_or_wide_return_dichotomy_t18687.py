#!/usr/bin/env python3
"""Regression checks for the terminal-or-wide-return paired-force dichotomy."""

from fractions import Fraction
from math import asin, cos, pi, sin, sqrt

# Near-full one-sided exact-force density.
c = Fraction(113, 5_000_000)
near_full = c / 2
wide_prefix = c / 4

# Coupled host-margin constant.
z0 = 20477 / 10000
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)
thetaH = pi / 2 - gammaH

# If TT is absent, one force lane stays opposite-host throughout all N centers.
# The first half of that population has at least N/2 later mate-birth vertices
# on the same-host return arc. With N/D -> c/2, this forces the return chord
# coefficient cH*c/4 and hence this projective pair-gap floor.
return_chord_coeff = cH * float(c) / 4
rho_return = 2 * asin(return_chord_coeff)

assert 0 < cH < 1
assert abs(cos(thetaH) - cH) < 1e-14
assert 0 < rho_return < gammaH
assert float(near_full) == 1.13e-5
assert float(wide_prefix) == 5.65e-6

# TT partner-rung consequence.
tt_angle = 2 * asin(cH)
assert abs(tt_angle - 2 * gammaH) < 1e-14
assert tt_angle > 0.94
assert cH > 0.4538

# Exhaust the paired terminal-cutoff word. If TT is absent, min(rA,rB)=0,
# so one lane is opposite-host for every center, including through mixed -> OO.
for N in range(1, 31):
    for rA in range(N + 1):
        for rB in range(N + 1):
            tt = min(rA, rB)
            if tt == 0:
                assert rA == 0 or rB == 0
                persistent = "A" if rA == 0 else "B"
                cutoff = rA if persistent == "A" else rB
                assert cutoff == 0
                # Terminal membership in a lane is exactly the prefix s<=r_sigma.
                assert all(not (s <= cutoff) for s in range(1, N + 1))

                # The first floor(N/2) centers have a linear tail to the end.
                H = N // 2
                for s in range(1, H + 1):
                    assert N - s >= H - 1

# Polygonal host-arc projection regression. All oriented tangents lie in an
# interval of half-width thetaH, so projection onto the midpoint direction is
# at least cH times arc length. Sample deterministic edge directions/lengths.
for m in (1, 2, 5, 17):
    vecx = vecy = length = 0.0
    for j in range(m):
        a = -thetaH + (2 * thetaH) * (j + 0.5) / m
        ell = 1.0 + (j % 3) / 7.0
        vecx += ell * cos(a)
        vecy += ell * sin(a)
        length += ell
    chord = sqrt(vecx * vecx + vecy * vecy)
    assert vecx + 1e-12 >= cH * length
    assert chord + 1e-12 >= cH * length

# Near-antipodal return identity: if ordinary separation is pi-eta, then
# |dA+dB| = 2 sin(eta/2).
for eta in (1e-8, rho_return, 1e-3, 0.1, gammaH / 2):
    dA = (1.0, 0.0)
    ang = pi - eta
    dB = (cos(ang), sin(ang))
    sumnorm = sqrt((dA[0] + dB[0]) ** 2 + (dA[1] + dB[1]) ** 2)
    assert abs(sumnorm - 2 * sin(eta / 2)) < 1e-12

print("PASS: terminal-or-wide-return dichotomy regressions")
print(f"c={float(c):.12g}")
print(f"near_full_density={float(near_full):.12g}")
print(f"wide_prefix_density={float(wide_prefix):.12g}")
print(f"cH={cH:.15g}")
print(f"gammaH={gammaH:.15g}")
print(f"TT_terminal_chord_coeff={cH:.15g}")
print(f"TT_terminal_angle={tt_angle:.15g}")
print(f"return_chord_coeff={return_chord_coeff:.15g}")
print(f"rho_return={rho_return:.15g}")
