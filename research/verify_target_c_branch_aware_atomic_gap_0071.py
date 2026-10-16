#!/usr/bin/env python3
"""Exact outward certificate for the branch-aware Target C-II atomic gap g=0.0071.

All assertions use Fraction arithmetic and outward square-root enclosures.  Printed
floating-point values are diagnostics only.
"""

from fractions import Fraction as F
from math import isqrt


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


def sqrt_bounds(lo: F, hi: F, digits: int = 45):
    """Outward decimal-grid enclosure for sqrt([lo,hi])."""
    assert 0 <= lo <= hi
    scale = 10**digits

    q = (lo.numerator * scale * scale) // lo.denominator
    r = isqrt(q)
    slo = F(r, scale)
    assert slo * slo <= lo

    num = hi.numerator * scale * scale
    q = (num + hi.denominator - 1) // hi.denominator
    r = isqrt(q)
    if r * r * hi.denominator < num:
        r += 1
    shi = F(r, scale)
    assert shi * shi >= hi
    return slo, shi


def sqrt_upper(x: F, digits: int = 40) -> F:
    """Outward upper enclosure for sqrt(x)."""
    assert x >= 0
    scale = 10**digits
    num = x.numerator * scale * scale
    q = (num + x.denominator - 1) // x.denominator
    r = isqrt(q)
    if r * r * x.denominator < num:
        r += 1
    out = F(r, scale)
    assert out * out >= x
    return out


# High-precision rational enclosures.  These are the same constants used by the
# hostile-audited g=0.0050 certificate.
PI_LO = dec("3.141592653589793238462643383279502884197169399375105820974944")
PI_HI = PI_LO + F(1, 10**60)
SQ3_LO = dec("1.732050807568877293527446341505872366942805253810380628055806")
SQ3_HI = SQ3_LO + F(1, 10**60)
assert SQ3_LO * SQ3_LO < 3 < SQ3_HI * SQ3_HI

DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO, S_HI = sqrt_bounds(DELTA_LO, DELTA_HI)

# r=sqrt(20/29), strong coefficient sqrt(10), and unconditional coefficient
# sqrt(29/2).
R_LO, R_HI = sqrt_bounds(F(20, 29), F(20, 29))
LAM1_LO, LAM1_HI = sqrt_bounds(F(10), F(10))
LAM0_LO, LAM0_HI = sqrt_bounds(F(29, 2), F(29, 2))

CAP_LO = 2 / SQ3_HI
CAP_HI = 2 / SQ3_LO

G = dec("0.0071")

# Under A<=2s+g, the dominant orbit satisfies W>=4s^2/(2s+g).  The
# function 4s^2/(2s+g) is increasing in s, so S_LO gives a lower bound.
W_LO = 4 * S_LO * S_LO / (2 * S_LO + G)
A_HI = 2 * S_HI + G
D_HI = S_HI * G + G * G / 4

# The strong-branch sufficient condition is
#   (1-r/2) A + r z <= K.
# Therefore z <= z_*=(K-A)/r + A/2.  This expression increases with K and r
# and decreases with A in the present range, so the following is an outward
# lower bound for z_*.
ZSTR_LO = (CAP_LO - A_HI) / R_LO + A_HI / 2

# Verify that all three phase families remain below K throughout the contradiction
# domain.  C<=A/2+sqrt(d0).
SQD_HI = sqrt_upper(D_HI)
C_MAX = A_HI / 2 + SQD_HI
assert C_MAX < CAP_LO

# Cover a fixed interval strictly wider than |z|<=sqrt(d0).
Z = dec("0.083")
STEP = dec("0.00001")
assert Z * Z > D_HI
assert W_LO - 6 * Z > 0
assert ZSTR_LO > dec("0.04428")

best = None
arg = None
count = 0
x = -Z
while x < Z:
    y = min(x + STEP, Z)

    # The raw term 3W/4+z/2 increases in W and z.
    raw = 3 * W_LO / 4 + x / 2

    # h<=d0-z^2.  On [x,y], maximize this at the point closest to zero.
    if x <= 0 <= y:
        h = D_HI
    elif y < 0:
        h = D_HI - y * y
    else:
        h = D_HI - x * x
    if h < 0:
        h = F(0)

    # R(W,z)=(W+2z)/(W+6z).  For z<0 it decreases in both W and z,
    # hence its interval maximum is at (W_LO,x).  For z>=0, R<=1.
    if x < 0:
        den = W_LO + 6 * x
        assert den > 0
        ratio = (W_LO + 2 * x) / den
        if ratio < 1:
            ratio = F(1)
    else:
        ratio = F(1)

    # Use sqrt(10) only when the whole z interval lies below the outward lower
    # bound for z_*.  Otherwise fall back to the unconditional sqrt(29/2).
    lam_hi = LAM1_HI if y <= ZSTR_LO else LAM0_HI
    loss = lam_hi * sqrt_upper(h * ratio)
    lb = raw - loss

    if best is None or lb < best:
        best = lb
        arg = (x, y, h, ratio, lam_hi, loss)

    x = y
    count += 1

margin = best - CAP_HI
assert margin > dec("0.00036")

print("PASS branch-aware atomic gap g=0.0071")
print("intervals=", count)
print("s bracket=", float(S_LO), float(S_HI))
print("W_lower=", float(W_LO))
print("d_upper=", float(D_HI))
print("center_max=", float(C_MAX), "cap_lower=", float(CAP_LO))
print("strong_z_threshold_lower=", float(ZSTR_LO))
print("sqrt(10) bracket=", float(LAM1_LO), float(LAM1_HI))
print("sqrt(29/2) bracket=", float(LAM0_LO), float(LAM0_HI))
print("best_leaf_lower=", float(best))
print("cap_upper=", float(CAP_HI))
print("margin_lower=", float(margin))
print("worst=", tuple(float(v) for v in arg))
