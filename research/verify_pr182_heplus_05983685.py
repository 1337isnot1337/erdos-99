#!/usr/bin/env python3
"""Exact-Fraction certificate for the PR #182 HE+ audit strengthening.

The HE proof itself yields the stronger attachment coefficient
    c_plus = pi/4 - 121/160000
rather than only pi/4 - 3/4000.

This script certifies a safe resulting scalar floor > 0.5983685. All theorem-sign
checks use fractions.Fraction. Floating-point output is diagnostic only after every
exact assertion has passed.
"""

from fractions import Fraction as F
from math import factorial, isqrt


def atan_bounds_inv(n: int, pairs: int) -> tuple[F, F]:
    x = F(1, n)
    lower = sum(
        ((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
        for k in range(2 * pairs)
    )
    upper = sum(
        ((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
        for k in range(2 * pairs + 1)
    )
    return lower, upper


def sin_bounds(x: F, pairs: int) -> tuple[F, F]:
    lower = sum(
        ((-1) ** k) * x ** (2 * k + 1) / factorial(2 * k + 1)
        for k in range(2 * pairs)
    )
    upper = sum(
        ((-1) ** k) * x ** (2 * k + 1) / factorial(2 * k + 1)
        for k in range(2 * pairs + 1)
    )
    return lower, upper


def floor_sqrt_fraction(x: F, den: int) -> F:
    """Largest k/den whose square is <= x, computed exactly."""
    target = x.numerator * den * den
    d = x.denominator
    k = isqrt(target // d)
    while (k + 1) * (k + 1) * d <= target:
        k += 1
    while k * k * d > target:
        k -= 1
    out = F(k, den)
    assert out * out <= x
    return out


def ceil_sqrt_fraction(x: F, den: int) -> F:
    """Least k/den whose square is >= x, computed exactly."""
    target = x.numerator * den * den
    d = x.denominator
    q = (target + d - 1) // d
    k = isqrt(q)
    while k * k * d < target:
        k += 1
    while k > 0 and (k - 1) * (k - 1) * d >= target:
        k -= 1
    out = F(k, den)
    assert out * out >= x
    return out


# Self-contained pi interval from Machin's identity.
a5_l, a5_u = atan_bounds_inv(5, 9)
a239_l, a239_u = atan_bounds_inv(239, 3)
PI_L = 16 * a5_l - 4 * a239_u
PI_U = 16 * a5_u - 4 * a239_l
assert PI_L < PI_U

# First certify the stronger HE geometric coefficient.
X0 = F(51, 1000)
R_EDGE = F(69363, 200000)
S0 = R_EDGE**4 / 64
HARD_CASE_LOSS = X0**2 / 4 + S0 / 2 - S0**2 / 12
LOSS_PLUS = F(121, 160000)
assert HARD_CASE_LOSS > LOSS_PLUS
# The easy HE case x>=11/200 has x^2/4 >= exactly LOSS_PLUS.
assert (F(11, 200) ** 2) / 4 == LOSS_PLUS

# Rational y point strictly before the strengthened transition.
Y = F(15245283, 10**7)  # 1.5245283
SIN_L, SIN_U = sin_bounds(Y, 6)
A_L = (Y + SIN_L) / 4
A_U = (Y + SIN_U) / 4


def c_r(x: F) -> F:
    return x / (x - 2) ** 2


# c_R(pi) is decreasing for pi>2.
C_R_L = c_r(PI_U)
C_R_U = c_r(PI_L)
RATIO_L = A_L / C_R_U
RATIO_U = A_U / C_R_L

ROOT_L = F(5115690768, 10**10)
ROOT_U = F(5115690769, 10**10)
assert ROOT_L**2 < RATIO_L
assert ROOT_U**2 > RATIO_U

P_L = 2 + 2 * ROOT_L
P_U = 2 + 2 * ROOT_U
M_L = P_L - Y
M_U = P_U - Y
U_U = 2 * Y - P_L

C_PLUS_L = PI_L / 4 - LOSS_PLUS
C_PLUS_U = PI_U / 4 - LOSS_PLUS


def jc_upper(lam: F) -> F:
    return C_PLUS_U * lam**2 + (lam + M_U) ** 2 / (4 * PI_L) - A_L


def jc_lower(lam: F) -> F:
    return C_PLUS_L * lam**2 + (lam + M_L) ** 2 / (4 * PI_U) - A_U


LAM_LO = F(5983685, 10**7)
LAM_HI = F(5983686, 10**7)
assert jc_upper(LAM_LO) < 0
assert jc_lower(LAM_HI) > 0

# DD crossover is still strictly above the JC root at this y.
SQRT3_L = floor_sqrt_fraction(F(3), 10**10)
SQRTY_U = ceil_sqrt_fraction(Y, 10**10)
SQRTU_U = ceil_sqrt_fraction(U_U, 10**10)
DELTA_U = (F(2) / SQRT3_L) * Y * SQRTY_U * SQRTU_U
E_L = A_L - DELTA_U
LAM_DD = F(598369, 10**6)
DD_MARGIN = E_L - C_PLUS_U * LAM_DD**2
assert DD_MARGIN > 0

print("PASS: PR182 HE+ exact certificate")
print("HE+ hard-case margin =", float(HARD_CASE_LOSS - LOSS_PLUS))
print("JC upper residual at 0.5983685 =", float(jc_upper(LAM_LO)))
print("JC lower residual at 0.5983686 =", float(jc_lower(LAM_HI)))
print("DD margin at 0.598369 =", float(DD_MARGIN))
