#!/usr/bin/env python3
"""Exact Fraction certificate for the eta_grid=0.00042 scalar inequalities.

The only transcendental inputs are certified decimal brackets for pi and sqrt(3),
with their ordering verified using rational arithmetic. Everything after that is
an outward rational interval calculation.
"""
from fractions import Fraction as F


def dec(s: str) -> F:
    neg = s.startswith('-')
    if neg:
        s = s[1:]
    a, b = (s.split('.') + [''])[:2] if '.' in s else (s, '')
    x = F(int((a or '0') + b), 10 ** len(b))
    return -x if neg else x

PI_LO = dec('3.14159265358979323846264338327950288419716939937510')
PI_HI = PI_LO + F(1, 10**50)
SQ3_LO = dec('1.73205080756887729352744634150587236694280525381038')
SQ3_HI = SQ3_LO + F(1, 10**50)
ETA = dec('0.00042')

# Verify sqrt(3) bracket exactly. The pi bracket uses the standard printed decimal
# enclosure; all downstream use is outward, so widening it by 1e-50 is harmless.
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI

DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S2_LO = dec('0.9523128068')
S2_HI = dec('0.9523128069')
assert S2_LO * S2_LO < DELTA_LO
assert S2_HI * S2_HI > DELTA_HI

ABAR_LO = 2 * S2_LO + ETA
ABAR_HI = 2 * S2_HI + ETA
M0_LO = 4 * S2_LO * S2_LO / ABAR_HI
M0_HI = 4 * S2_HI * S2_HI / ABAR_LO
R0_HI = ABAR_HI - M0_LO

# d0 = Abar^2/4 - s2^2 + R0^2/4. This is a safe outward upper bound.
D0_HI = ABAR_HI * ABAR_HI / 4 - S2_LO * S2_LO + R0_HI * R0_HI / 4
SQD0_HI = dec('0.020005')
SQ6D0_HI = dec('0.049003')
P0_HI = dec('0.028292')
assert SQD0_HI * SQD0_HI > D0_HI
assert SQ6D0_HI * SQ6D0_HI > 6 * D0_HI
assert P0_HI * P0_HI > 2 * D0_HI

S0_LO = M0_LO / 2 - SQD0_HI - SQ6D0_HI
EFFECTIVE_LO = F(3, 2) * S0_LO - 6 * P0_HI
GRID_CAP_HI = 2 / SQ3_LO

# This is exactly the strict opposite-corner diameter inequality required by §168.4.
assert EFFECTIVE_LO > GRID_CAP_HI

# The retained smaller shore still clears the triple-neighbor threshold with huge room.
B_KEEP_LO = S0_LO / 2 - 2 * P0_HI
TRIPLE_HI = 3 * P0_HI
assert B_KEEP_LO > TRIPLE_HI

# Rhombic-only consequences of eta=0.00042.
SIGMA_GAP = 2 * ETA
MANTEL_GAP_LO = SIGMA_GAP * (4 * S2_LO + ETA) / 8
MU_GAIN = SIGMA_GAP / 10
assert SIGMA_GAP == dec('0.00084')
assert MANTEL_GAP_LO > dec('0.0004')
assert MU_GAIN == dec('0.000084')

print('S2 bracket:', float(S2_LO), float(S2_HI))
print('D0 upper:', float(D0_HI))
print('S0 lower:', float(S0_LO))
print('effective lower:', float(EFFECTIVE_LO))
print('grid-cap upper:', float(GRID_CAP_HI))
print('effective margin lower:', float(EFFECTIVE_LO-GRID_CAP_HI))
print('B_keep lower:', float(B_KEEP_LO), 'triple upper:', float(TRIPLE_HI))
print('Mantel-gap lower:', float(MANTEL_GAP_LO))
print('PASS: exact rational eta_grid=0.00042 certificate')
