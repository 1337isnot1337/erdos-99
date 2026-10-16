#!/usr/bin/env python3
"""Regression certificate for the matching/reflection coupled Type-II floor.

The proof is in target_c_matching_reflection_coupled_floor_2026-09-15.md.
This checks the high-precision coupled constant, exact eta=15/56 reflection geometry,
and sampled upper-blocker near-common-antipode inequalities.
"""

from decimal import Decimal, getcontext
from math import acos, cos, pi, sin, sqrt

getcontext().prec = 70

ETA_D = Decimal(15) / Decimal(56)
T42 = Decimal("1.8208886379794447")
R42 = Decimal("0.00576795")
PI_D = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
SQ3_D = Decimal(3).sqrt()

K_D = Decimal(3) + Decimal(1) / ETA_D + Decimal(8) * (Decimal(2) + SQ3_D)
FLOOR_NEW = (PI_D - T42 - (K_D / 2) * R42) / Decimal(5)
FLOOR_OLD = (PI_D - T42 - (K_D / 2) * R42) / Decimal(6)

assert abs(FLOOR_NEW / FLOOR_OLD - Decimal(6) / Decimal(5)) < Decimal("1e-60")
assert FLOOR_NEW > Decimal("0.24303602415")

eta = 15 / 56
c = 97 / 112
h = sqrt(3135) / 112
alpha = acos(c)
y_minus = sin(pi / 3 - alpha)
y_plus = sin(pi / 3 + alpha)
cos2 = c * c - h * h
perimeter_cost = 2 * (sqrt(1 + y_minus * y_minus) - 1)

assert alpha < pi / 6
assert abs(c * c + h * h - 1) < 1e-14
assert abs(y_minus - (97 * sqrt(3) - sqrt(3135)) / 224) < 1e-14
assert abs(y_plus - (97 * sqrt(3) + sqrt(3135)) / 224) < 1e-14
assert abs(2 * cos2 - 3137 / 3136) < 1e-14
assert 2 * cos2 > 1
assert abs(h / c - sqrt(3135) / 97) < 1e-14
assert perimeter_cost > 0.236

# Sample upper blockers at several diameter scales.  For every tuple satisfying the
# original diameter constraints and the reflected violation, verify the normal-cone
# inequality and the exact near-common-antipode strengthening CMR.23-CMR.26.
upper_hits = 0
for diameter in [5.0, 10.0, 30.0, 100.0]:
    for ip in range(-160, 161):
        p = ip * diameter / 800
        for iq in range(1, 801):
            q = iq * diameter / 800
            reflected2 = p * p + (q + h) ** 2
            da2 = (p + c) ** 2 + q * q
            db2 = (p - c) ** 2 + q * q
            if (
                reflected2 > diameter * diameter + 1e-10
                and da2 <= diameter * diameter + 1e-10
                and db2 <= diameter * diameter + 1e-10
            ):
                upper_hits += 1
                dx2 = p * p + (q - h) ** 2
                assert 2 * h * q - 2 * c * abs(p) > cos2 - 1e-9
                assert abs(p) / q < h / c + 1e-9
                assert min(da2, db2) > dx2 + 2 * cos2 - 1e-9
                assert dx2 > diameter * diameter - 4 * h * q - 1e-9
                assert q <= diameter + 1e-9
                assert min(da2, db2) > (
                    diameter * diameter - 4 * h * diameter + 2 * cos2 - 1e-8
                )

assert upper_hits > 0

print(f"eta=15/56={eta:.15f}")
print(f"K={K_D}")
print(f"matching/reflection coupled floor={FLOOR_NEW}")
print(f"previous factor-1/2 coupled floor={FLOOR_OLD}")
print("improvement factor=6/5")
print(f"alpha_eta={alpha:.15f}")
print(f"h_eta={h:.15f}; 2h={2*h:.15f}")
print(f"Y_minus={y_minus:.15f}; Y_plus={y_plus:.15f}")
print(f"perimeter cap cost={perimeter_cost:.15f}")
print(f"cone tan(alpha_eta)={h/c:.15f}")
print(f"2 cos(2 alpha_eta)={2*cos2:.15f}=3137/3136")
print(f"sampled upper blockers={upper_hits}")
print("PASS: matching/reflection coupled floor certificate")
