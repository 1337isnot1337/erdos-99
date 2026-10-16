#!/usr/bin/env python3
"""Outward certificate for LA90 (g=0.0009) propagation through Section 171."""
from decimal import Decimal, getcontext
from fractions import Fraction as F


def dec_frac(s: str) -> F:
    neg = s.startswith("-")
    if neg:
        s = s[1:]
    if "." in s:
        a, b = s.split(".", 1)
    else:
        a, b = s, ""
    x = F(int((a or "0") + b), 10 ** len(b))
    return -x if neg else x


PI_LO = dec_frac("3.14159265358979323846264338327950288419716939937510")
PI_HI = PI_LO + F(1, 10**50)
SQ3_LO = dec_frac("1.73205080756887729352744634150587236694280525381038")
SQ3_HI = SQ3_LO + F(1, 10**50)
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI

DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO = dec_frac("0.9523128068")
S_HI = dec_frac("0.9523128069")
assert S_LO * S_LO < DELTA_LO
assert S_HI * S_HI > DELTA_HI

G = dec_frac("0.0009")
EPS = dec_frac("0.0014758")
D0 = (F(9, 2) * EPS - G) / 2
assert D0 == dec_frac("0.00287055")

C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS

# Section 171 endpoint:
# F_t(delta)=B(delta)+K(delta)-8 Delta_2 / denom.
B_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0
K_RAD_HI = 81 * (PI_HI + D0) ** 2 * D0
K_HI = dec_frac("1.31983")
assert K_HI**3 > K_RAD_HI

# At the right endpoint denom = 2*s_2 + g.
RHS_LO = 8 * S_LO * S_LO / (2 * S_LO + G)
MARGIN = RHS_LO - (B_HI + K_HI)
assert MARGIN > dec_frac("0.00004")

# Coarse positive derivative certificate on 0 <= delta <= D0.
C81_LO = dec_frac("4.326")
ROOT_PI_D_HI = dec_frac("1.466")
ROOT_D_HI = dec_frac("0.143")
assert C81_LO**3 < 81
assert ROOT_PI_D_HI**3 > PI_HI + D0
assert ROOT_D_HI**3 > D0
KPRIME_LO = (
    (C81_LO / 3)
    * dec_frac("3.1415")
    / ROOT_PI_D_HI
    / (ROOT_D_HI**2)
)
assert KPRIME_LO > dec_frac("151.1")
NEG_HI = 16 * dec_frac("0.907") / (dec_frac("1.905") ** 2)
DERIV_LO = KPRIME_LO - 5 - NEG_HI
assert DERIV_LO > dec_frac("142")

# Downstream constants used in the companion note.
getcontext().prec = 70
D = Decimal
pi = D("3.14159265358979323846264338327950288419716939937510")
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
g = D("0.0009")
eps = D("0.0014758")
C146 = D(4) * (pi + s2) / D(9)
t = C146 + eps
R = D("4.5") * eps - g
delta_max = R / D(2)
C0 = D(2) * s2 + g
j = t + D(4) * s2 + D(2) * g - pi
h = j / D(2) + t - pi / D(2)
p5 = pi + C0 - D("2.5") * t
loo = D(3) * pi - D(5) * t
tooth_coupled = D(5) * pi + D(2) * C0 - D(10) * t

assert D("1.82098933") < t < D("1.82098935")
assert delta_max == D("0.00287055")
assert p5 > D("0.49464")
assert loo > D("0.3198")
assert tooth_coupled / D(3) > D("0.43637")

print("PASS: LA90 g=0.0009 -> Section 171 propagation")
print("delta90 =", float(D0))
print("t90 bracket =", float(T0_LO), float(T0_HI))
print("endpoint negativity margin >", float(MARGIN))
print("delta derivative lower >", float(DERIV_LO))
print("safe q-k floor >", float(T0_LO))
print("C0 =", C0)
print("R(t90) =", R)
print("p5/D floor =", p5)
print("L_OO/D floor =", loo)
print("max(N2,L_>2)/D floor =", tooth_coupled / D(3))
print("J/D floor =", j)
print("H/D floor =", h)
