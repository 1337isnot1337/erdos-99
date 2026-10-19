#!/usr/bin/env python3
"""Exact endpoint check for the conditional g=0.0071 propagation."""

from fractions import Fraction as F
from math import isqrt


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dec(s: str) -> F:
    neg = s.startswith("-")
    s = s[1:] if neg else s
    a, b = s.split(".", 1) if "." in s else (s, "")
    value = F(int((a or "0") + b), 10 ** len(b))
    return -value if neg else value


def atan_bounds(inv: int, terms: int = 60):
    x = F(1, inv)
    x2 = x * x
    power = x
    partial = F(0)
    for n in range(terms):
        term = power / (2 * n + 1)
        partial += term if n % 2 == 0 else -term
        power *= x2
    next_term = power / (2 * terms + 1)
    other = partial + (next_term if terms % 2 == 0 else -next_term)
    return min(partial, other), max(partial, other)


def sqrt_bounds(x: F, digits: int = 70):
    require(x >= 0, "square-root input must be nonnegative")
    scale = 10**digits
    q = (x.numerator * scale * scale) // x.denominator
    lo = F(isqrt(q), scale)
    hi = lo + F(1, scale)
    require(lo * lo <= x < hi * hi, "rational square-root enclosure failed")
    return lo, hi


# Independent Machin enclosure for pi; all subsequent checks are rational.
PI_LO = dec("3.141592653589793238462643383279502884197169399375105820974944")
PI_HI = PI_LO + F(1, 10**60)
a5_lo, a5_hi = atan_bounds(5)
a239_lo, a239_hi = atan_bounds(239)
machin_lo = 16 * a5_lo - 4 * a239_hi
machin_hi = 16 * a5_hi - 4 * a239_lo
require(PI_LO < machin_lo < machin_hi < PI_HI, "Machin pi enclosure failed")

SQ3_LO = dec("1.73205080756887729352744634150587236694280525381038")
SQ3_HI = SQ3_LO + F(1, 10**50)
require(SQ3_LO**2 < 3 < SQ3_HI**2, "sqrt(3) enclosure failed")
DELTA_LO = PI_LO / (2 * SQ3_HI)
DELTA_HI = PI_HI / (2 * SQ3_LO)
S_LO = dec("0.9523128068")
S_HI = dec("0.9523128069")
require(S_LO**2 < DELTA_LO < DELTA_HI < S_HI**2, "s enclosure failed")

# Section 171 endpoint, with g changed and every outward endpoint recomputed.
G = dec("0.0071")
EPS = dec("0.0023374")
D0 = (F(9, 2) * EPS - G) / 2
require(D0 == dec("0.00170915") and D0 > 0, "g=0.0071 residual endpoint changed")
C146_LO = F(4, 9) * (PI_LO + S_LO)
C146_HI = F(4, 9) * (PI_HI + S_HI)
T0_LO = C146_LO + EPS
T0_HI = C146_HI + EPS

# The Section 171 endpoint expression is 8s^2/(2s+g) - B - K.
B171_HI = 10 * T0_HI - 5 * PI_LO - 5 * D0
K_RAD_HI = 81 * (PI_HI + D0) ** 2 * D0
K_HI = dec("1.111")
require(K_HI**3 > K_RAD_HI, "cube-root upper endpoint failed")
RHS_LO = 8 * S_LO**2 / (2 * S_LO + G)
MARGIN = RHS_LO - B171_HI - K_HI
require(MARGIN > dec("0.18"), "Section 171 endpoint margin is not positive")

# Negative control: the predecessor's coarse K bound is not valid at this input.
OLD_COARSE_K_HI = dec("1.3025")
OLD_COARSE_MARGIN = RHS_LO - B171_HI - OLD_COARSE_K_HI
require(OLD_COARSE_MARGIN < dec("-0.009"), "stale cube-root control no longer detects the failed transfer")

# Recheck the positive derivative on the complete Section 171 endpoint interval.
C81_LO = dec("4.326")
ROOT_PI_D_HI = dec("1.466")
ROOT_D_HI = dec("0.143")
require(C81_LO**3 < 81, "cube-root 81 lower endpoint failed")
require(ROOT_PI_D_HI**3 > PI_HI + D0, "pi-plus-delta root upper endpoint failed")
require(ROOT_D_HI**3 > D0, "delta root upper endpoint failed")
KPRIME_LO = (C81_LO / 3) * dec("3.1415") / ROOT_PI_D_HI / ROOT_D_HI**2
require(KPRIME_LO > dec("151.1"), "cube-root derivative lower bound failed")
require(S_HI**2 < dec("0.907") and 2 * S_LO + G > dec("1.905"), "negative derivative term enclosure failed")
NEG_HI = 16 * dec("0.907") / dec("1.905") ** 2
DERIV_LO = KPRIME_LO - 5 - NEG_HI
require(DERIV_LO > dec("142"), "Section 171 derivative sign failed")

# Exact outer-tooth / long-side endpoint functions, evaluated at t=t0.
# Algebra: [5pi+2(2s+g)-10t0]/3 = 5pi/27-4s/27+2g/3-10eps/3.
BORDER_LO = F(5, 27) * PI_LO - F(4, 27) * S_HI + F(2, 3) * G - F(10, 3) * EPS
require(BORDER_LO > dec("0.4376350385"), "outer boundary lower bound failed")

ETA15 = F(1, 15)
ETA6 = F(3, 50)
SQ2_LO, SQ2_HI = sqrt_bounds(F(2))
SQ6_LO, SQ6_HI = sqrt_bounds(F(6))
ETA_LIMIT_LO = 2 - (SQ2_HI + SQ6_HI) / 2  # 2(1-cos(pi/12))
require(0 < ETA6 < ETA15 < ETA_LIMIT_LO, "tooth penetration parameter is outside its allowed interval")


def tooth_direction_lower(eta: F) -> F:
    root_hi = sqrt_bounds(eta - eta * eta / 4)[1]
    return SQ3_LO / 2 * (1 - eta / 2) - root_hi / 2


PEN15_LO = (BORDER_LO - D0 / ETA15) / 2
PEN6_LO = (BORDER_LO - D0 / ETA6) / 2
Y6_LO = tooth_direction_lower(ETA6)
require(PEN15_LO > dec("0.20599889"), "eta=1/15 tooth count floor failed")
require(PEN6_LO > dec("0.20457460"), "eta=3/50 tooth count floor failed")
require(Y6_LO > dec("0.71849218"), "inward direction floor failed")
INWARD_MASS_LO = PEN6_LO * Y6_LO
require(INWARD_MASS_LO > dec("0.14698525"), "inward projection sum floor failed")

TAN_DEN_LO = 1 - SQ3_HI / 2
require(TAN_DEN_LO > 0, "long-side direction denominator is not positive")
TAN_LO = (BORDER_LO - D0 / TAN_DEN_LO) / 2
TAN_MASS_LO = TAN_LO * SQ3_LO / 2
require(TAN_LO > dec("0.21243888"), "long-side contact count floor failed")
require(TAN_MASS_LO > dec("0.18397747"), "tangent projection sum floor failed")

# For x=t-t0, both branch floors decrease by their displayed positive slopes.
PEN15_X_SLOPE = F(5, 3) + F(9, 8) / ETA15
PEN6_X_SLOPE = F(5, 3) + F(9, 8) / ETA6
require(PEN15_X_SLOPE == F(445, 24), "eta=1/15 branch slope changed")
require(PEN6_X_SLOPE == F(245, 12), "eta=3/50 branch slope changed")
TAN_X_SLOPE_HI = F(5, 3) + F(9, 8) / TAN_DEN_LO
PEN15_AT_X01_LO = PEN15_LO - PEN15_X_SLOPE / 100
TAN_AT_X01_LO = TAN_LO - TAN_X_SLOPE_HI / 100
require(PEN15_AT_X01_LO > dec("0.0205"), "tooth floor at x=0.01 failed")
require(TAN_AT_X01_LO > dec("0.111"), "long-side floor at x=0.01 failed")

print("PASS conditional g=0.0071 -> Section 171 and both outer-energy branches")
print("delta_71 =", float(D0))
print("t0 bracket =", float(T0_LO), float(T0_HI))
print("cube-root upper =", float(K_HI), "endpoint margin >", float(MARGIN))
print("old coarse-cube-root margin <", float(OLD_COARSE_MARGIN))
print("delta derivative lower >", float(DERIV_LO))
print("outer B lower >", float(BORDER_LO))
print("tooth eta=1/15 contacts >", float(PEN15_LO))
print("tooth eta=3/50 contacts >", float(PEN6_LO), "inward mass >", float(INWARD_MASS_LO))
print("long-side contacts >", float(TAN_LO), "tangent mass >", float(TAN_MASS_LO))
print("endpoint x-slopes =", float(PEN15_X_SLOPE), float(PEN6_X_SLOPE))
print("at x<=0.01: tooth contacts >", float(PEN15_AT_X01_LO), "long-side contacts >", float(TAN_AT_X01_LO))
