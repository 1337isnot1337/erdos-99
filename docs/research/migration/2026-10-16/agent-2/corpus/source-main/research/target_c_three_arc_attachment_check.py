from fractions import Fraction as F
from math import isqrt, pi, sqrt, asin

# Exact sign certificate for the three-arc attachment theorem.
#
# The adjacent report proves the geometric envelope analytically. This script
# certifies only the quoted rational lower barrier mu_3 > 0.8995. Every sign
# assertion uses Fraction/integer arithmetic; floating-point values are printed
# only as diagnostics.

PI_LO = F(6283, 2000)       # PI_LO < pi
PI_HI = F(3927, 1250)       # pi < PI_HI
SQRT3_HI = F(97, 56)        # sqrt(3) < 97/56
PHI_LO = F(154451, 250000)  # canonical lower bound for Phi(2 rho)
M = F(8995, 10000)
DEN = 10**9


def floor_sqrt_fraction(x: F, den: int = DEN) -> F:
    target = (x.numerator * den * den) // x.denominator
    k = isqrt(target)
    while F(k + 1, den) ** 2 <= x:
        k += 1
    while F(k, den) ** 2 > x:
        k -= 1
    return F(k, den)


def ceil_sqrt_fraction(x: F, den: int = DEN) -> F:
    lo = floor_sqrt_fraction(x, den)
    if lo * lo == x:
        return lo
    return lo + F(1, den)


def atan_lower(t: F, pairs: int = 8) -> F:
    # atan(t)=t-t^3/3+t^5/5-... for 0<t<1.  An even number of
    # alternating terms ends with a negative term and is a strict lower bound.
    out = F(0)
    for k in range(2 * pairs):
        term = t ** (2 * k + 1) / F(2 * k + 1)
        out += term if k % 2 == 0 else -term
    return out


assert PI_LO < PI_HI
assert SQRT3_HI * SQRT3_HI > 3
assert M > F(866, 1000)
assert M < F(9, 10)

s2 = 1 - M * M
sqrt_lo = floor_sqrt_fraction(s2)
sqrt_hi = ceil_sqrt_fraction(s2)
assert sqrt_lo * sqrt_lo <= s2 <= sqrt_hi * sqrt_hi

t_lo = sqrt_lo / M
assert 0 < t_lo < 1
atan_lo = atan_lower(t_lo)

# asin(M)=pi/2-atan(sqrt(1-M^2)/M).
# Use pi upper and atan lower for an upper bound.
asin_hi = PI_HI / 2 - atan_lo

# sin(4pi/3-2asin M)
# = (sqrt(3)/2)(2M^2-1)+M sqrt(1-M^2).
sin_g_hi = SQRT3_HI / 2 * (2 * M * M - 1) + M * sqrt_hi

# W3(M)=-pi/4+(3/4)asin(M)+(3/8)sin(g).
w3_hi = -PI_LO / 4 + F(3, 4) * asin_hi + F(3, 8) * sin_g_hi

# Cavity term (2M+pi)^2/(36pi).  Numerator increases with pi and
# denominator decreases when pi is replaced by PI_LO, so this is an upper bound.
cavity_hi = (2 * M + PI_HI) ** 2 / (36 * PI_LO)

total_hi = w3_hi + cavity_hi
margin = PHI_LO - total_hi
assert margin > 0

# Coarse exact check that the three-component regime continues past M:
# sin^2(2pi/5)=(5+sqrt(5))/8 > 0.95^2, using sqrt(5)>20/9.
assert F(20, 9) ** 2 < 5
assert (F(5, 1) + F(20, 9)) / 8 > F(95, 100) ** 2
assert M < F(95, 100)

print("PASS: exact three-arc attachment threshold check")
print("candidate mu =", M, float(M))
print("W3 upper =", w3_hi, float(w3_hi))
print("cavity upper =", cavity_hi, float(cavity_hi))
print("total upper =", total_hi, float(total_hi))
print("FSDB lower =", PHI_LO, float(PHI_LO))
print("exact margin =", margin, float(margin))

rho_diag = 0.7390851332151607
phi_diag = (2 * rho_diag + __import__('math').sin(2 * rho_diag)) / 4

def w3_diag(z: float) -> float:
    theta = 2 * asin(z)
    g = 4 * pi / 3 - theta
    return pi / 4 - 3 * (g - __import__('math').sin(g)) / 8

# Diagnostic bisection only; not a proof input.
lo, hi = sqrt(3) / 2, __import__('math').sin(2 * pi / 5)
for _ in range(100):
    mid = (lo + hi) / 2
    val = w3_diag(mid) + (2 * mid + pi) ** 2 / (36 * pi)
    if val < phi_diag:
        lo = mid
    else:
        hi = mid
print("diagnostic root =", (lo + hi) / 2)
