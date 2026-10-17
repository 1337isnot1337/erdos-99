#!/usr/bin/env python3
"""Exact rational certificate for the corrected Target C-II phase-star gap 0.0053."""

from fractions import Fraction as F
from math import isqrt


def atan_inv_bounds(q: int, n: int):
    s = F(0)
    for k in range(n):
        term = F(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = F(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(x_lo: F, x_hi: F, scale: int):
    lo_n = isqrt((x_lo.numerator * scale * scale) // x_lo.denominator)
    hi_n = isqrt((x_hi.numerator * scale * scale) // x_hi.denominator)
    return F(lo_n, scale), F(hi_n + 1, scale)


def dec(x: F) -> str:
    return f"{float(x):.16g}"


# Machin enclosure for pi.
a5_lo, a5_hi = atan_inv_bounds(5, 80)
a239_lo, a239_hi = atan_inv_bounds(239, 20)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

DIGITS = 70
SCALE = 10 ** DIGITS
sqrt3_n = isqrt(3 * SCALE * SCALE)
sqrt3_lo = F(sqrt3_n, SCALE)
sqrt3_hi = F(sqrt3_n + 1, SCALE)
K_lo = F(2) / sqrt3_hi
K_hi = F(2) / sqrt3_lo
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)

alpha = F(2, 29)
g = F(53, 10000)
A_lo = 2 * s_lo + g
A_hi = 2 * s_hi + g
M0_lo = 4 * Delta_lo / A_hi
residual_slope_hi = (A_hi - M0_lo) / 2

# Scope repair. The pair theorem assumes every selected phase class has mass <=K.
# If the dominant center C>K, use only the generic crossing bound E<=C(W-C).
# Since K>A0/2, this branch is decreasing in C and maximized at C=K.
assert A_hi / 2 < K_lo
high_center_derivative_lo = K_lo - residual_slope_hi
assert high_center_derivative_lo > F(1)
high_center_capacity_hi = K_lo * (A_hi - K_lo)
assert high_center_capacity_hi < Delta_lo - F(3, 100)

# Low-center branch C<=K. The physical pair theorem is valid here. The optimizer is
# in (W/3,W/2), and W/2<K, so it remains strictly inside the theorem's scope.
r_left_lo = F(2, 3) * M0_lo - K_hi
assert r_left_lo > 0
r_less_c_margin = 2 * K_lo - F(2, 3) * A_hi
assert r_less_c_margin > 0
r_edge_hi = F(2, 3) * A_hi - K_lo
left_derivative_lo = (
    M0_lo / 3
    - alpha * (F(9) / M0_lo) * r_edge_hi * r_edge_hi
)
assert left_derivative_lo > F(3, 5)

# Envelope monotonicity in dominant-orbit mass M.
r_slope_hi = F(3, 4) * A_hi - K_lo
psi_slope_lo = M0_lo / 3 - alpha * r_slope_hi
net_slope_lo = psi_slope_lo - residual_slope_hi
assert net_slope_lo > F(3, 5)

# Strong-concavity tangent certificate for the low-center endpoint A0.
c0 = F(94047, 100000)
assert A_hi / 3 < c0 < A_lo / 2 < K_lo
q_lo = 3 - A_hi / c0
q_hi = 3 - A_lo / c0
r_lo = (A_lo + c0) / 2 - K_hi
r_hi = (A_hi + c0) / 2 - K_lo
assert q_lo > 0 and r_lo > 0

term1_hi = c0 * (A_hi - c0)
penalty_lo = alpha * q_lo * r_lo * r_lo
phi_hi = term1_hi - penalty_lo

part1_lo = A_lo / (c0 * c0) * r_lo * r_lo
part1_hi = A_hi / (c0 * c0) * r_hi * r_hi
part2_lo = q_lo * r_lo
part2_hi = q_hi * r_hi
phi_c_lo = A_lo - 2 * c0 - alpha * (part1_hi + part2_hi)
phi_c_hi = A_hi - 2 * c0 - alpha * (part1_lo + part2_lo)
phi_c_abs_hi = max(abs(phi_c_lo), abs(phi_c_hi))

# Phi_CC<=-2, hence max Phi <= Phi(c0)+Phi_C(c0)^2/4.
psi_A0_hi = phi_hi + phi_c_abs_hi * phi_c_abs_hi / 4
capacity_margin_lo = Delta_lo - psi_A0_hi
assert capacity_margin_lo > F(463, 10_000_000)

print("PASS: corrected phase-star orbit-capacity gap g=0.0053")
print("A0 upper =", dec(A_hi))
print("M0 lower =", dec(M0_lo))
print("K lower =", dec(K_lo))
print("high-center total capacity upper =", dec(high_center_capacity_hi))
print("high-center margin =", dec(Delta_lo - high_center_capacity_hi))
print("left derivative lower =", dec(left_derivative_lo))
print("net M slope lower =", dec(net_slope_lo))
print("Phi endpoint upper =", dec(phi_hi))
print("|Phi_C| upper =", dec(phi_c_abs_hi))
print("Psi(A0) upper =", dec(psi_A0_hi))
print("capacity margin lower =", dec(capacity_margin_lo))
