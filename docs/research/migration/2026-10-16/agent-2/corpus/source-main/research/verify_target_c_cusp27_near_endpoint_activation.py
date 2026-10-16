#!/usr/bin/env python3
"""Exact certificate for the cusp27 near-endpoint activation band."""
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
DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO = dec("0.9523128068")
S_HI = dec("0.9523128069")
assert S_LO * S_LO < DELTA_LO
assert S_HI * S_HI > DELTA_HI

G = dec("0.0035")
EPS_MAX = dec("0.0046")
DELTA_MIN = dec("0.00839")
DELTA_MAX = (F(9, 2) * EPS_MAX - G) / 2
assert DELTA_MAX == dec("0.0086")

C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
TMAX_HI = C146_HI + EPS_MAX

# At t=tmax and delta=0.00839 the scalar inequality is still negative.
B_HI = 10 * TMAX_HI - 5 * PI_LO - 5 * DELTA_MIN
CUSP_HI = dec("1.30994")
assert CUSP_HI**3 > 27 * (PI_HI + DELTA_MIN) ** 2 * DELTA_MIN
DEN_HI = 2 * S_HI + F(9, 2) * EPS_MAX - 2 * DELTA_MIN
RHS_LO = 8 * DELTA_LO / DEN_HI
MARGIN = RHS_LO - (B_HI + CUSP_HI)
assert MARGIN > dec("0.00025")

# F is increasing in delta throughout the larger feasible band [0,0.0086].
CUSP_DMAX_LO = dec("1.3207")
assert CUSP_DMAX_LO**3 < 27 * (PI_LO + DELTA_MAX) ** 2 * DELTA_MAX
QPRIME_LO = CUSP_DMAX_LO / F(3) * (1 / DELTA_MAX + 2 / (PI_HI + DELTA_MAX))
NEG_HI = 16 * DELTA_HI / (2 * S_LO + G) ** 2
DERIV_LO = QPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec("42")

# Three-cusp hypothesis remains valid throughout the band.
assert DELTA_MAX / (PI_LO + DELTA_MAX) < PI_LO**3 / F(5184)

# Topology slack consequences.
RMAX = F(9, 2) * EPS_MAX - G
KAPPA_MAX = 2 * RMAX - 4 * DELTA_MIN
assert KAPPA_MAX == dec("0.00084")
QMF_HI = (
    F(9, 4) * (C146_HI + EPS_MAX)
    - PI_LO
    - (2 * S_LO + G) / 2
    - DELTA_MIN
)
assert QMF_HI < dec("0.000211")

print("PASS: cusp27 near-endpoint activation")
print("scalar negativity margin >", float(MARGIN))
print("delta derivative lower >", float(DERIV_LO))
print("delta max =", float(DELTA_MAX))
print("kappa max =", float(KAPPA_MAX))
print("Q-f upper <", float(QMF_HI))
