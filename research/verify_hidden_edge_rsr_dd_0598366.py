#!/usr/bin/env python3
"""Exact-Fraction certificate for the HE/RSR/DD generic >0.598366 theorem."""

from fractions import Fraction as F
import math


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
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs)
    )
    upper = sum(
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs + 1)
    )
    return lower, upper


# Tight rational interval for pi from Machin's identity.
a5_l, a5_u = atan_bounds_inv(5, 9)
a239_l, a239_u = atan_bounds_inv(239, 3)
PI_L = 16 * a5_l - 4 * a239_u
PI_U = 16 * a5_u - 4 * a239_l
assert PI_L < PI_U

# Exact arithmetic for the hidden-edge coefficient itself.
X0 = F(51, 1000)
assert 1 - 6 * X0 + X0 * X0 - F(3, 5) * (1 + X0) ** 3 > 0
R_EDGE = F(69363, 200000)
S0 = R_EDGE**4 / 64
HIDDEN_LOSS = X0**2 / 4 + S0 / 2 - S0**2 / 12
assert HIDDEN_LOSS > F(3, 4000)

# Rational point left of the HE transition.
Y = F(190566, 125000)  # 1.524528
SIN_L, SIN_U = sin_bounds(Y, 6)
A_L = (Y + SIN_L) / 4
A_U = (Y + SIN_U) / 4


def c_r(x: F) -> F:
    return x / (x - 2) ** 2


C_R_L = c_r(PI_U)
C_R_U = c_r(PI_L)
RATIO_L = A_L / C_R_U
RATIO_U = A_U / C_R_L

ROOT_L = F(5115690450, 10**10)
ROOT_U = F(5115690451, 10**10)
assert ROOT_L**2 < RATIO_L
assert ROOT_U**2 > RATIO_U

P_L = 2 + 2 * ROOT_L
P_U = 2 + 2 * ROOT_U
M_L = P_L - Y
M_U = P_U - Y
U_U = 2 * Y - P_L

C_HE_L = PI_L / 4 - F(3, 4000)
C_HE_U = PI_U / 4 - F(3, 4000)


def jc_upper(lam: F) -> F:
    return C_HE_U * lam**2 + (lam + M_U) ** 2 / (4 * PI_L) - A_L


def jc_lower(lam: F) -> F:
    return C_HE_L * lam**2 + (lam + M_L) ** 2 / (4 * PI_U) - A_U


LAM_598366 = F(299183, 500000)
LAM_598367 = F(598367, 10**6)
assert jc_upper(LAM_598366) < 0
assert jc_lower(LAM_598367) > 0

# DD root at Y is above 0.598367.
SQRT3_L = F(1732050807, 10**9)
SQRTY_U = F(123471779, 10**8)
SQRTU_U = F(160990404, 10**9)
assert SQRT3_L**2 < 3
assert SQRTY_U**2 > Y
assert SQRTU_U**2 > U_U

DELTA_U = (F(2) / SQRT3_L) * Y * SQRTY_U * SQRTU_U
E_L = A_L - DELTA_U
assert E_L > C_HE_U * LAM_598367**2

print("Exact HE/RSR/DD certificate passed.")
print("hidden-edge coefficient margin:", float(HIDDEN_LOSS - F(3, 4000)))
print("p_e lower sqrt margin:", float(RATIO_L - ROOT_L**2))
print("p_e upper sqrt margin:", float(ROOT_U**2 - RATIO_U))
print("JC residual at 0.598366:", float(jc_upper(LAM_598366)))
print("JC residual at 0.598367:", float(jc_lower(LAM_598367)))
print("DD margin at 0.598367:", float(E_L - C_HE_U * LAM_598367**2))
