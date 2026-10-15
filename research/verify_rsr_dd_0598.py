#!/usr/bin/env python3
"""Exact-Fraction certificate for target_c_rsr_dd_explicit_surplus_0598_2026-09-10.md.

All theorem-sign checks use fractions.Fraction. Floating-point values are printed only
for human-readable margins after the exact assertions have passed.
"""

from fractions import Fraction as F


def atan_bounds_inv(n: int, pairs: int) -> tuple[F, F]:
    """Alternating-series bounds for atan(1/n)."""
    x = F(1, n)
    lower = sum(((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
                for k in range(2 * pairs))
    upper = sum(((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
                for k in range(2 * pairs + 1))
    return lower, upper


def sin_bounds(x: F, pairs: int) -> tuple[F, F]:
    """Alternating-series bounds for sin(x), for the positive x used here."""
    import math
    lower = sum(((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
                for k in range(2 * pairs))
    upper = sum(((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
                for k in range(2 * pairs + 1))
    return lower, upper


# Self-contained pi bounds from Machin's identity.
a5_l, a5_u = atan_bounds_inv(5, 6)
a239_l, a239_u = atan_bounds_inv(239, 2)
machin_l = 16 * a5_l - 4 * a239_u
machin_u = 16 * a5_u - 4 * a239_l

PI_L = F(333, 106)
PI_U = F(355, 113)
assert machin_l > PI_L
assert machin_u < PI_U

# Rational test point.
Y = F(3811, 2500)

# Sine bounds at y0.
sin_l_exact, sin_u_exact = sin_bounds(Y, 4)
SIN_L = F(4994619, 5000000)  # 0.9989238
SIN_U = F(249731, 250000)    # 0.998924
assert sin_l_exact > SIN_L
assert sin_u_exact < SIN_U

A_L = (Y + SIN_L) / 4
A_U = (Y + SIN_U) / 4

# c_R(pi)=pi/(pi-2)^2 is decreasing on our pi interval.
def c_r(x: F) -> F:
    return x / (x - 2) ** 2


C_L = c_r(PI_U)
C_U = c_r(PI_L)

ratio_l = A_L / C_U
ratio_u = A_U / C_L

ROOT_L = F(51152, 100000)
ROOT_U = F(51158, 100000)
assert ROOT_L ** 2 < ratio_l
assert ROOT_U ** 2 > ratio_u

P_L = 2 + 2 * ROOT_L
P_U = 2 + 2 * ROOT_U
M_L = P_L - Y
M_U = P_U - Y
U_U = 2 * Y - P_L

# JC root r_e(y0) lies in (0.598, 0.599).
def q_upper(lam: F) -> F:
    return ((PI_U ** 2 + 1) * lam ** 2
            + 2 * M_U * lam + M_U ** 2
            - 4 * PI_L * A_L)


def q_lower(lam: F) -> F:
    return ((PI_L ** 2 + 1) * lam ** 2
            + 2 * M_L * lam + M_L ** 2
            - 4 * PI_U * A_U)


LAM_598 = F(299, 500)
LAM_599 = F(599, 1000)
assert q_upper(LAM_598) < 0
assert q_lower(LAM_599) > 0

# DD root d_e(y0) is > 0.599.
SQRT3_L = F(433, 250)
SQRTY_U = F(247, 200)
SQRTU_U = F(321, 2000)
assert SQRT3_L ** 2 < 3
assert SQRTY_U ** 2 > Y
assert SQRTU_U ** 2 > U_U

DELTA_U = (F(2) / SQRT3_L) * Y * SQRTY_U * SQRTU_U
E_L = A_L - DELTA_U
D599_THRESHOLD = PI_U * LAM_599 ** 2 / 4
assert E_L > D599_THRESHOLD

print("Exact certificate passed.")
print("Q_upper(0.598) =", float(q_upper(LAM_598)))
print("Q_lower(0.599) =", float(q_lower(LAM_599)))
print("DD E-margin over 0.599^2*pi/4 =", float(E_L - D599_THRESHOLD))
