#!/usr/bin/env python3
"""Regression certificate for the shallow-tooth reflection perimeter collapse.

The proof is in target_c_tooth_reflection_perimeter_collapse_2026-09-15.md.
This script checks the exact constants, foot-interiority/depth geometry, and the
uniform cap-perimeter increment used there.
"""

from math import acos, cos, pi, sin, sqrt

ETA = 4 / 15
N2 = 0.4363893718701161781
DOUT = 0.002883975

c_eta = 13 / 15
h_eta = 2 * sqrt(14) / 15
alpha_eta = acos(c_eta)
Y = (13 * sqrt(3) - 2 * sqrt(14)) / 30
Y_plus = (13 * sqrt(3) + 2 * sqrt(14)) / 30
g = 2 * (sqrt(1 + Y * Y) - 1)
triangle_area = (13 / 15) * Y
nsh = N2 - DOUT / ETA

assert alpha_eta < pi / 6
assert abs(c_eta * c_eta + h_eta * h_eta - 1) < 1e-14
assert abs(sin(pi / 3 - alpha_eta) - Y) < 1e-14
assert abs(sin(pi / 3 + alpha_eta) - Y_plus) < 1e-14
assert abs(nsh - 0.4255744656201161781) < 2e-15
assert g > 0.2370630385
assert triangle_area > 0.4342966542

# Foot-interiority and depth regressions across the entire alpha-range used by
# the theorem.  We sample u>=0 only, by symmetry.
for frac in [0.15, 0.35, 0.6, 0.8, 1.0]:
    alpha = alpha_eta * frac
    c, h = cos(alpha), sin(alpha)
    y_floor = sin(pi / 3 - alpha)
    exact_floor = sin(pi / 3 + alpha)
    lower_hits = 0
    exact_hits = 0

    for ir in range(1, 1300):
        r = ir / 1000
        for iu in range(0, 1401):
            u = iu / 1000
            reflected = u * u + (r - h) ** 2
            old = u * u + (r + h) ** 2
            da = (u + c) ** 2 + r * r
            db = (u - c) ** 2 + r * r
            if (
                reflected < 1 - 1e-7
                and old > 1 + 1e-7
                and da > 1 + 1e-7
                and db > 1 + 1e-7
            ):
                lower_hits += 1
                assert u < c + 1e-12
                assert r > y_floor - 0.0015
                increment = (
                    sqrt((c + u) ** 2 + r * r)
                    + sqrt((c - u) ** 2 + r * r)
                    - 2 * c
                )
                assert increment > g - 0.002
    assert lower_hits > 0

    # Points on the reflected unit circle that become exact new contacts.
    for k in range(36000):
        theta = 2 * pi * k / 36000
        u = cos(theta)
        yy = -h + sin(theta)
        r = -yy
        if r <= 0:
            continue
        old = u * u + (yy - h) ** 2
        da = (u + c) ** 2 + yy * yy
        db = (u - c) ** 2 + yy * yy
        if old > 1 + 1e-8 and da > 1 + 1e-8 and db > 1 + 1e-8:
            exact_hits += 1
            assert abs(u) < c + 2e-4
            assert r > exact_floor - 2e-4
    assert exact_hits > 0

# Uniform cap-perimeter cost on a deterministic parameter grid.
for ia in range(1, 101):
    alpha = alpha_eta * ia / 100
    c = cos(alpha)
    y_floor = sin(pi / 3 - alpha)
    for jr in range(0, 21):
        r = y_floor + jr * (1.2 - y_floor) / 20
        for ku in range(0, 21):
            u = c * ku / 21
            increment = (
                sqrt((c + u) ** 2 + r * r)
                + sqrt((c - u) ** 2 + r * r)
                - 2 * c
            )
            assert increment >= g - 1e-12

print(f"eta={ETA}")
print(f"alpha_eta={alpha_eta:.15f} < pi/6")
print(f"h_eta={h_eta:.15f}; 2h={2*h_eta:.15f}")
print(f"Y_minus={Y:.15f}; Y_plus={Y_plus:.15f}")
print(f"perimeter cost g_eta={g:.15f}")
print(f"triangle area floor={triangle_area:.15f}")
print(f"N_sh/D >= {nsh:.15f}")
print(f"upper cone tan(alpha_eta)={h_eta/c_eta:.15f}")
print("PASS: perimeter-collapse geometry/constants")
