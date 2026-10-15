#!/usr/bin/env python3
"""Exact-Fraction certificate for the BV/RSR/DD generic >0.5983 theorem.

All sign checks use fractions.Fraction.  Binary floating point is used only when
printing human-readable margins after every exact assertion has passed.
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
    """Alternating-series bounds for sin(x) on the positive argument used here."""
    lower = sum(
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs)
    )
    upper = sum(
        ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
        for k in range(2 * pairs + 1)
    )
    return lower, upper


# Self-contained pi interval from Machin's identity
#     pi = 16 atan(1/5) - 4 atan(1/239).
a5_l, a5_u = atan_bounds_inv(5, 8)
a239_l, a239_u = atan_bounds_inv(239, 3)
PI_L = 16 * a5_l - 4 * a239_u
PI_U = 16 * a5_u - 4 * a239_l
assert PI_L < PI_U

# Rational test point left of the true BV/RSR/DD transition.
Y = F(3049, 2000)  # 1.5245
SIN_L, SIN_U = sin_bounds(Y, 5)
A_L = (Y + SIN_L) / 4
A_U = (Y + SIN_U) / 4


# c_R(pi)=pi/(pi-2)^2 is decreasing on the relevant pi interval.
def c_r(x: F) -> F:
    return x / (x - 2) ** 2


C_L = c_r(PI_U)
C_U = c_r(PI_L)

# p_e=2+2 sqrt(Phi/c_R).
ratio_l = A_L / C_U
ratio_u = A_U / C_L
ROOT_L = F(51156607, 100000000)
ROOT_U = F(51156608, 100000000)
assert ROOT_L ** 2 < ratio_l
assert ROOT_U ** 2 > ratio_u

P_L = 2 + 2 * ROOT_L
P_U = 2 + 2 * ROOT_U
M_L = P_L - Y
M_U = P_U - Y
U_U = 2 * Y - P_L


# With c_BV=pi/4-1/1600, the JC root is the positive root of
#   (pi^2+1-pi/400) lambda^2 + 2m lambda + m^2 - 4pi Phi = 0.
def jc_coeff(x: F) -> F:
    return x * x + 1 - x / F(400)


def q_upper(lam: F) -> F:
    return (
        jc_coeff(PI_U) * lam ** 2
        + 2 * M_U * lam
        + M_U ** 2
        - 4 * PI_L * A_L
    )


def q_lower(lam: F) -> F:
    return (
        jc_coeff(PI_L) * lam ** 2
        + 2 * M_L * lam
        + M_L ** 2
        - 4 * PI_U * A_U
    )


LAM_5983 = F(5983, 10000)
LAM_59832 = F(59832, 100000)
assert q_upper(LAM_5983) < 0
assert q_lower(LAM_59832) > 0

# Therefore r_BV(Y) is in (0.5983,0.59832).

# Bound the DD value from below.  At p=p_e,
#   Delta=(2/sqrt(3)) Y^(3/2) sqrt(2Y-p_e).
# Upper-bound Delta and upper-bound c_BV to prove
#   Phi-Delta > c_BV * 0.5986^2.
SQRT3_L = F(17320508, 10000000)
SQRTY_U = F(123471, 100000)
SQRTU_U = F(160835, 1000000)
assert SQRT3_L ** 2 < 3
assert SQRTY_U ** 2 > Y
assert SQRTU_U ** 2 > U_U

DELTA_U = (F(2) / SQRT3_L) * Y * SQRTY_U * SQRTU_U
E_L = A_L - DELTA_U
C_BV_U = PI_U / 4 - F(1, 1600)
LAM_5986 = F(2993, 5000)
assert E_L > C_BV_U * LAM_5986 ** 2

# Thus d_BV(Y)>0.5986>r_BV(Y), so Y lies strictly before the unique
# d_BV=r_BV transition.  Since r_BV is strictly increasing there,
# lambda_BRD>r_BV(Y)>0.5983.

print("Exact BV/RSR/DD certificate passed.")
print("JC upper polynomial at 0.5983:", float(q_upper(LAM_5983)))
print("JC lower polynomial at 0.59832:", float(q_lower(LAM_59832)))
print(
    "DD margin above c_BV*0.5986^2:",
    float(E_L - C_BV_U * LAM_5986 ** 2),
)
