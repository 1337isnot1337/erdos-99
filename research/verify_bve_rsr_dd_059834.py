#!/usr/bin/env python3
"""Exact-Fraction certificate for the BVE/RSR/DD generic >0.59834 theorem.

All sign checks use fractions.Fraction. Floating-point output is printed only after
all exact assertions pass.
"""

from fractions import Fraction as F
import math


def atan_bounds_inv(n: int, pairs: int) -> tuple[F, F]:
    """Alternating-series bounds for atan(1/n)."""
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
    """Alternating-series bounds for sin(x) at the positive argument used here."""
    lower = sum(
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs)
    )
    upper = sum(
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs + 1)
    )
    return lower, upper


# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
a5_l, a5_u = atan_bounds_inv(5, 9)
a239_l, a239_u = atan_bounds_inv(239, 3)
PI_L = 16 * a5_l - 4 * a239_u
PI_U = 16 * a5_u - 4 * a239_l
assert PI_L < PI_U

# Rational test point strictly left of the true feedback transition.
Y = F(609811, 400000)  # 1.5245275
SIN_L, SIN_U = sin_bounds(Y, 6)
A_L = (Y + SIN_L) / 4
A_U = (Y + SIN_U) / 4


def c_r(x: F) -> F:
    return x / (x - 2) ** 2


# c_R(pi) decreases on the relevant pi interval.
C_R_L = c_r(PI_U)
C_R_U = c_r(PI_L)
RATIO_L = A_L / C_R_U
RATIO_U = A_U / C_R_L

# sqrt(Phi/c_R) interval.
ROOT_L = F(5115689920, 10**10)
ROOT_U = F(5115689921, 10**10)
assert ROOT_L**2 < RATIO_L
assert ROOT_U**2 > RATIO_U

P_L = 2 + 2 * ROOT_L
P_U = 2 + 2 * ROOT_U
M_L = P_L - Y
M_U = P_U - Y
U_U = 2 * Y - P_L


def h_kappa(lam: F, x: F) -> F:
    """Increasing cubic whose zero is kappa(lam)."""
    return lam * (1 + x) ** 3 - (1 - 6 * x + x * x)


LAM_59834 = F(59834, 100000)
K0_L = F(512495574, 10**10)
K0_U = F(512495575, 10**10)
assert h_kappa(LAM_59834, K0_L) < 0
assert h_kappa(LAM_59834, K0_U) > 0

LAM_598341 = F(598341, 10**6)
K1_L = F(512494100, 10**10)
K1_U = F(512494101, 10**10)
assert h_kappa(LAM_598341, K1_L) < 0
assert h_kappa(LAM_598341, K1_U) > 0


def g_upper(lam: F, kappa_lower: F) -> F:
    """Upper bound for G(lam)=(pi-kappa^2)lam^2/4."""
    return (PI_U / 4 - kappa_lower * kappa_lower / 4) * lam * lam


def g_lower(lam: F, kappa_upper: F) -> F:
    """Lower bound for G(lam)."""
    return (PI_L / 4 - kappa_upper * kappa_upper / 4) * lam * lam


# JC residual: G(lam)+(lam+m)^2/(4pi)-Phi.
# It is strictly increasing in lam.  Outward bounds prove the root is in
# (0.59834, 0.598341).
JC_59834_UPPER = (
    g_upper(LAM_59834, K0_L)
    + (LAM_59834 + M_U) ** 2 / (4 * PI_L)
    - A_L
)
JC_598341_LOWER = (
    g_lower(LAM_598341, K1_U)
    + (LAM_598341 + M_L) ** 2 / (4 * PI_U)
    - A_U
)
assert JC_59834_UPPER < 0
assert JC_598341_LOWER > 0

# DD residual on p=p_e: E(y)-G(lam), where
# E=Phi-(2/sqrt(3))*y^(3/2)*sqrt(2y-p_e).
# Upper-bound the detour term and G(0.598341); a positive remainder proves
# d_G(Y)>0.598341.
SQRT3_L = F(1732050807, 10**9)
SQRTY_U = F(123471758, 10**8)
SQRTU_U = F(160987627, 10**9)
assert SQRT3_L**2 < 3
assert SQRTY_U**2 > Y
assert SQRTU_U**2 > U_U

DELTA_U = (F(2) / SQRT3_L) * Y * SQRTY_U * SQRTU_U
E_L = A_L - DELTA_U
DD_MARGIN = E_L - g_upper(LAM_598341, K1_L)
assert DD_MARGIN > 0

print("Exact BVE/RSR/DD feedback certificate passed.")
print("pi interval width:", float(PI_U - PI_L))
print("p_e sqrt lower margin:", float(RATIO_L - ROOT_L**2))
print("p_e sqrt upper margin:", float(ROOT_U**2 - RATIO_U))
print("JC upper residual at 0.59834:", float(JC_59834_UPPER))
print("JC lower residual at 0.598341:", float(JC_598341_LOWER))
print("DD margin at 0.598341:", float(DD_MARGIN))
