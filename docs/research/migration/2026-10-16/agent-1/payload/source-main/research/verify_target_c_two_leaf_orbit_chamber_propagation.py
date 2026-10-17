#!/usr/bin/env python3
"""Outward rational certificate for TL69 propagated through audited Target C §171."""
from fractions import Fraction as F


def dec(s: str) -> F:
    neg = s.startswith('-')
    if neg:
        s = s[1:]
    if '.' in s:
        a, b = s.split('.', 1)
    else:
        a, b = s, ''
    x = F(int((a or '0') + b), 10 ** len(b))
    return -x if neg else x

# Wide, exact decimal enclosures.
PI_LO = dec('3.14159265358979323846264338327950288419716939937510')
PI_HI = PI_LO + F(1, 10**50)
SQ3_LO = dec('1.73205080756887729352744634150587236694280525381038')
SQ3_HI = SQ3_LO + F(1, 10**50)
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI

DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO = dec('0.9523128068')
S_HI = dec('0.9523128069')
assert S_LO * S_LO < DELTA_LO
assert S_HI * S_HI > DELTA_HI

# TL69 train gain and safe §171 epsilon.
G = dec('0.000698')
EPS = dec('0.0014334')
D0 = (F(9, 2) * EPS - G) / 2
assert D0 == dec('0.00287615')

C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS

# Positive affine part at the feasible right endpoint.
B_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0

# Cube-root term: explicit outward rational bound.
K_RAD_HI = 81 * (PI_HI + D0) ** 2 * D0
K_HI = dec('1.320679')
assert K_HI ** 3 > K_RAD_HI

# At the endpoint the §171 denominator simplifies to 2*s+g.
# 8*s^2/(2*s+g) is increasing in s>0.
RHS_LO = 8 * S_LO * S_LO / (2 * S_LO + G)
MARGIN = RHS_LO - (B_HI + K_HI)
assert MARGIN > dec('0.00005')

# Certify F_t(delta) is increasing throughout the feasible interval.
C81_LO = dec('4.326')
ROOT_PI_D_HI = dec('1.466')
ROOT_D_HI = dec('0.143')
assert C81_LO ** 3 < 81
assert ROOT_PI_D_HI ** 3 > PI_HI + D0
assert ROOT_D_HI ** 3 > D0
KPRIME_LO = (C81_LO / 3) * dec('3.1415') / ROOT_PI_D_HI / (ROOT_D_HI ** 2)

# Along the feasible interval the last denominator is >=2*s+g.
# Deliberately retain the older coarse numerical enclosure.
NEG_HI = 16 * dec('0.907') / (dec('1.905') ** 2)
DERIV_LO = KPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec('142')

# Downstream numerical brackets used by the companion note.
# These are not needed for the §171 contradiction, but guard transcription.
C69_LO = 2 * S_LO + G
C69_HI = 2 * S_HI + G
F69_LO = S_LO - PI_HI / 4 + G / 2
F69_HI = S_HI - PI_LO / 4 + G / 2
J69_LO = T0_LO + 2 * C69_LO - PI_HI
J69_HI = T0_HI + 2 * C69_HI - PI_LO
H69_LO = J69_LO / 2 + T0_LO - PI_HI / 2
H69_HI = J69_HI / 2 + T0_HI - PI_LO / 2
RESCAP_HI = 3 * PI_HI / 2 - T0_LO

assert F69_LO > dec('0.1672635')
assert J69_LO > dec('2.4900010')
assert H69_LO > dec('1.4951509')
assert RESCAP_HI < dec('2.8914421')

print('PASS: TL69 -> §171/chamber exact-rational propagation')
print('delta endpoint =', float(D0))
print('t69 bracket =', float(T0_LO), float(T0_HI))
print('endpoint negativity margin >', float(MARGIN))
print('delta-derivative lower >', float(DERIV_LO))
print('f69 bracket =', float(F69_LO), float(F69_HI))
print('j69 bracket =', float(J69_LO), float(J69_HI))
print('h69 bracket =', float(H69_LO), float(H69_HI))
print('residual cap upper =', float(RESCAP_HI))
