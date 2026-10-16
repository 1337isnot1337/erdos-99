#!/usr/bin/env python3
"""Outward rational certificate for coefficient-27 Section-171 with g=0.0035."""
from fractions import Fraction as F


def dec(s: str) -> F:
    neg = s.startswith("-")
    if neg:
        s = s[1:]
    if "." in s:
        a, b = s.split(".", 1)
    else:
        a, b = s, ""
    x = F(int((a or "0") + b), 10 ** len(b))
    return -x if neg else x


PI_LO = dec("3.14159265358979323846264338327950288419716939937510")
PI_HI = PI_LO + F(1, 10**50)
SQ3_LO = dec("1.73205080756887729352744634150587236694280525381038")
SQ3_HI = SQ3_LO + F(1, 10**50)
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI
DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO = dec("0.9523128068")
S_HI = dec("0.9523128069")
assert S_LO * S_LO < DELTA_LO
assert S_HI * S_HI > DELTA_HI

G = dec("0.0035")
EPS = dec("0.00452")
D0 = (F(9, 2) * EPS - G) / 2
assert D0 == dec("0.00842")

C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS

# At the feasible right endpoint, the Section-171 denominator is 2*s_2+g.
B_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0
CUSP_RAD_HI = 27 * (PI_HI + D0) ** 2 * D0
CUSP_RAD_LO = 27 * (PI_LO + D0) ** 2 * D0
CUSP_HI = dec("1.3116")
CUSP_LO = dec("1.3114")
assert CUSP_HI**3 > CUSP_RAD_HI
assert CUSP_LO**3 < CUSP_RAD_LO
RHS_LO = 8 * DELTA_LO / (2 * S_HI + G)
MARGIN = RHS_LO - (B_HI + CUSP_HI)
assert MARGIN > dec("0.00038")

# The entire feasible detour interval lies in the disjoint-three-cusp regime.
RATIO_HI = D0 / (PI_LO + D0)
CUSP_REGIME_LO = PI_LO**3 / F(5184)
assert RATIO_HI < CUSP_REGIME_LO

# Delta monotonicity. For q(d)=(27(pi+d)^2 d)^(1/3),
# q'(d)=q(d)/3*(1/d+2/(pi+d)); q' decreases with d>0.
QPRIME_LO = CUSP_LO / F(3) * (1 / D0 + 2 / (PI_HI + D0))
NEG_HI = 16 * DELTA_HI / (2 * S_LO + G) ** 2
DERIV_LO = QPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec("43")

print("PASS: coefficient-27 Section-171 with g=0.0035")
print("delta endpoint =", float(D0))
print("t floor bracket =", float(T0_LO), float(T0_HI))
print("endpoint negativity margin >", float(MARGIN))
print("detour ratio upper =", float(RATIO_HI))
print("three-cusp threshold lower =", float(CUSP_REGIME_LO))
print("delta derivative lower >", float(DERIV_LO))
