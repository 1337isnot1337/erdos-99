#!/usr/bin/env python3
"""Outward rational certificate for the AG42 refinement of audited Target C §171.

This checks the safe endpoint eps=0.0013751 using Fraction arithmetic.  It relies on
§171's already-audited symbolic reduction and on the proof-only AG42 input g=0.00042;
it does not re-prove either geometric theorem.
"""
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

# Standard decimal enclosures, deliberately wider than needed.
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

G = dec('0.00042')
EPS = dec('0.0013751')
D0 = (F(9, 2) * EPS - G) / 2
assert D0 == dec('0.002883975')

# t0 = C146 + EPS, C146=(4/9)(pi+s).  Bound the positive B endpoint term.
C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS
B_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0

# Upper-bound K=(81(pi+d0)^2 d0)^(1/3) by an explicit rational cube root.
K_RAD_HI = 81 * (PI_HI + D0) ** 2 * D0
K_HI = dec('1.321878')
assert K_HI ** 3 > K_RAD_HI

# RHS=8*s^2/(2s+g) is increasing in s>0, so S_LO gives a lower bound.
RHS_LO = 8 * S_LO * S_LO / (2 * S_LO + G)
MARGIN = RHS_LO - (B_HI + K_HI)
assert MARGIN > dec('0.000029')

# Certify F_{t0}(delta) is increasing for 0<delta<=d0 using coarse rational bounds.
# K'(delta) >= (cuberoot(81)/3)*pi*(pi+d0)^(-1/3)*d0^(-2/3).
# The following rational bounds are intentionally crude but exact.
C81_LO = dec('4.326')
ROOT_PI_D_HI = dec('1.466')
ROOT_D_HI = dec('0.143')
assert C81_LO ** 3 < 81
assert ROOT_PI_D_HI ** 3 > PI_HI + D0
assert ROOT_D_HI ** 3 > D0
KPRIME_LO = (C81_LO / 3) * dec('3.1415') / ROOT_PI_D_HI / (ROOT_D_HI ** 2)
assert KPRIME_LO > dec('151.1')

# Along the feasible interval the denominator in §171.21 is >=2s+g.
# Use Delta2<0.907 and 2s+g>1.905 for a simple exact upper bound.
NEG_HI = 16 * dec('0.907') / (dec('1.905') ** 2)
DERIV_LO = KPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec('142')

# Since §171 also proves strict monotonicity in t, endpoint negativity excludes t<=t0.
print('D0 =', float(D0))
print('t0 bracket =', float(T0_LO), float(T0_HI))
print('B upper =', float(B_HI))
print('K upper =', float(K_HI))
print('RHS lower =', float(RHS_LO))
print('endpoint negativity margin >', float(MARGIN))
print('delta-derivative lower >', float(DERIV_LO))
print('safe all-Type-II t floor >', float(T0_LO))
print('PASS: AG42 -> §171 safe endpoint eps=0.0013751')
