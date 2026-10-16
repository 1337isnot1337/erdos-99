#!/usr/bin/env python3
"""Exact arithmetic certificate for the eta=0.06 shallow-tooth locality corollary."""
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
S2_HI = dec("0.9523128069")
SQ3_LO = dec("1.73205080756887729352744634150587236694280525381038")
SQ3_HI = SQ3_LO + F(1, 10**50)
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI

SQ591_LO = dec("24.310491562286436")
SQ591_HI = dec("24.310491562286438")
assert SQ591_LO * SQ591_LO < 591 < SQ591_HI * SQ591_HI

G = dec("0.00335")
EPS = dec("0.0019905")
DELTA = (F(9, 2) * EPS - G) / 2
assert DELTA == dec("0.002803625")

# P335.22 simplifies exactly to
# 5*pi + 2*(2*s2+g) - 10*(4/9*(pi+s2)+eps)
# = 5/9*pi - 4/9*s2 + 2g - 10eps.
BURDEN_LO = F(5, 9) * PI_LO - F(4, 9) * S2_HI + 2 * G - 10 * EPS
N2_LO = BURDEN_LO / 3

ETA = F(3, 50)  # 0.06
assert ETA < 2 - SQ3_HI
NSH_LO = N2_LO - DELTA / ETA

# For eta=3/50,
# Y_eta=(97*sqrt(3)-sqrt(591))/200.
Y_LO = (97 * SQ3_LO - SQ591_HI) / 200
PROJECTION_SUM_LO = NSH_LO * Y_LO

assert N2_LO > dec("0.4362913")
assert NSH_LO > dec("0.3895642")
assert Y_LO > dec("0.7184921")
assert PROJECTION_SUM_LO > dec("0.2798988")

print("PASS: near-disk shallow-tooth locality eta=0.06")
print("delta upper =", float(DELTA))
print("tooth-branch N2/D lower >", float(N2_LO))
print("shallow/distinct penetration count lower >", float(NSH_LO))
print("per-edge inward component lower >", float(Y_LO))
print("sum of local inward projections / D lower >", float(PROJECTION_SUM_LO))
