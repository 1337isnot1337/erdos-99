#!/usr/bin/env python3
"""Outward rational certificate for TC109 propagated through audited Target C §171."""
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

G = dec('0.00109')
EPS = dec('0.0015157')
D0 = (F(9, 2) * EPS - G) / 2
assert D0 == dec('0.002865325')

C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS

# Positive affine part of the §171 endpoint function.
B_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0

# Outward upper bound for the cube-root term.
K_RAD_HI = 81 * (PI_HI + D0) ** 2 * D0
K_HI = dec('1.319017')
assert K_HI ** 3 > K_RAD_HI

# At the feasible right endpoint the denominator equals 2*s+g.
# 8*s^2/(2*s+g) is increasing for s>0.
RHS_LO = 8 * S_LO * S_LO / (2 * S_LO + G)
MARGIN = RHS_LO - (B_HI + K_HI)
assert MARGIN > dec('0.000052')

# Uniform positivity of dF/ddelta on 0<delta<=D0.
C81_LO = dec('4.326')
ROOT_PI_D_HI = dec('1.466')
ROOT_D_HI = dec('0.143')
assert C81_LO ** 3 < 81
assert ROOT_PI_D_HI ** 3 > PI_HI + D0
assert ROOT_D_HI ** 3 > D0
KPRIME_LO = (C81_LO / 3) * dec('3.1415') / ROOT_PI_D_HI / (ROOT_D_HI ** 2)
NEG_HI = 16 * dec('0.907') / (dec('1.905') ** 2)
DERIV_LO = KPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec('142')

# Downstream coefficient transcription guards.
C109_LO = 2 * S_LO + G
C109_HI = 2 * S_HI + G
F109_LO = S_LO - PI_HI / 4 + G / 2
F109_HI = S_HI - PI_LO / 4 + G / 2
J109_LO = T0_LO + 2 * C109_LO - PI_HI
J109_HI = T0_HI + 2 * C109_HI - PI_LO
H109_LO = J109_LO / 2 + T0_LO - PI_HI / 2
H109_HI = J109_HI / 2 + T0_HI - PI_LO / 2
RESCAP_HI = 3 * PI_HI / 2 - T0_LO
P109_LO = PI_LO + C109_LO - F(5, 2) * T0_HI
P109_HI = PI_HI + C109_HI - F(5, 2) * T0_LO

assert T0_LO > dec('1.82102923795')
assert F109_LO > dec('0.1674595')
assert J109_LO > dec('2.4908673')
assert H109_LO > dec('1.4956663')
assert RESCAP_HI < dec('2.8913598')
assert P109_LO > dec('0.4947348')

print('PASS: TC109 -> §171/chamber exact-rational propagation')
print('delta endpoint =', float(D0))
print('t109 bracket =', float(T0_LO), float(T0_HI))
print('endpoint negativity margin >', float(MARGIN))
print('delta-derivative lower >', float(DERIV_LO))
print('f109 bracket =', float(F109_LO), float(F109_HI))
print('j109 bracket =', float(J109_LO), float(J109_HI))
print('h109 bracket =', float(H109_LO), float(H109_HI))
print('residual cap upper =', float(RESCAP_HI))
print('low-t pentagon P109 bracket =', float(P109_LO), float(P109_HI))
