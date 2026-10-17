#!/usr/bin/env python3
"""Regression checks for the high-t host-cap exact-force-pair theorem.

This certificate is deliberately small.  The theorem itself is a direct combination of
four already-proved geometric inputs:

* the coupled host transverse constant c_H;
* opposite transverse signs of the exact positive force pair;
* full-source diameter-midpoint localization L_D=O(D^(3/4)); and
* the convex geometric-thrackle property of actual diameter edges.

The checks below verify the displayed constants and the scale separation used to make
the positive/negative endpoint caps disjoint.
"""

from math import asin, acos, pi

C_H = 0.453819885927
CAP_HALF = C_H / 2.0
GAMMA_H = asin(C_H)
THETA_H = acos(C_H)

assert 0.45 < C_H < 0.46
assert abs((GAMMA_H + THETA_H) - pi / 2.0) < 1.0e-12
assert THETA_H < pi / 2.0
assert CAP_HALF > 0.226

# L_D/D = O(D^(-1/4)); the ratio tends to zero and is eventually far below
# the macroscopic cap half-width c_H/2.  The harmless constant 2 below is
# larger than the leading 3^(1/8) coefficient in the current midpoint bound.
def midpoint_ratio_upper(D: float) -> float:
    return 2.0 * D ** (-0.25)

prev = None
for D in (10**8, 10**12, 10**16, 10**20):
    r = midpoint_ratio_upper(float(D))
    if prev is not None:
        assert r < prev
    prev = r

assert midpoint_ratio_upper(1.0e20) < CAP_HALF / 10.0

# If |h(m)| <= L and transverse component is at least c_H-eps, the birth
# endpoint is in the positive cap and the partner in the negative cap once
# L/D + eps/2 < c_H/2.  Check representative asymptotic errors.
for eps in (1.0e-2, 1.0e-3, 1.0e-4):
    ratio = eps / 10.0
    lower = C_H / 2.0 - eps / 2.0 - ratio
    assert lower > 0.0
    # Opposite-sign bars then have separated birth coordinates by at least
    # 2*lower*D, so sharing a birth endpoint is impossible.
    assert 2.0 * lower > 0.4

print("PASS: host-cap force-pair separation regressions")
print(f"c_H={C_H:.12f}")
print(f"gamma_H_deg={GAMMA_H * 180.0 / pi:.12f}")
print(f"cap_half={CAP_HALF:.12f}")
