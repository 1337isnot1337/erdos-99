#!/usr/bin/env python3
"""Exact rational certificate for the corrected uniform strong-branch gap 0.0077.

This is the same scope-corrected three-branch certificate as the hostile-audited
0.0076 theorem. The physical pair theorem is used only while the center family has
mass C<=K; the C>K branch is handled only by generic triangle-free capacity.
"""

from fractions import Fraction as F
from math import isqrt


def atan_inv_bounds(q: int, n: int):
    s = F(0)
    for k in range(n):
        term = F(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = F(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo: F, hi: F, scale: int):
    assert 0 <= lo <= hi
    lo_n = isqrt((lo.numerator * scale * scale) // lo.denominator)
    hi_n = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    out_lo = F(lo_n, scale)
    out_hi = F(hi_n, scale)
    assert out_lo * out_lo <= lo
    assert out_hi * out_hi >= hi
    return out_lo, out_hi


def diag(x: F) -> str:
    return f"{float(x):.16g}"


DIGITS = 90
SCALE = 10**DIGITS

a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

sqrt3_n = isqrt(3 * SCALE * SCALE)
sqrt3_lo = F(sqrt3_n, SCALE)
sqrt3_hi = F(sqrt3_n + 1, SCALE)
K_lo = F(2) / sqrt3_hi
K_hi = F(2) / sqrt3_lo
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
rcrit_lo, rcrit_hi = sqrt_bounds(F(20, 29), F(20, 29), SCALE)

alpha_strong = F(1, 10)
alpha_weak = F(2, 29)
g = F(77, 10000)  # 0.0077
A_lo = 2 * s_lo + g
A_hi = 2 * s_hi + g
M0_lo = 4 * Delta_lo / A_hi

# Full relevant orbit interval remains below 2K.
assert A_hi < 2 * K_lo

# On C<=W/2, the worst center/leaf excess ratio is 2-2K/W.
strong_ratio_hi = 2 - 2 * K_lo / A_hi
assert strong_ratio_hi < rcrit_lo

# Strong branch optimizer geometry.
r_left_lo = F(2, 3) * M0_lo - K_hi
assert r_left_lo > 0
assert 2 * K_lo - F(2, 3) * A_hi > 0
r_edge_hi = F(2, 3) * A_hi - K_lo
left_derivative_lo = (
    M0_lo / 3
    - alpha_strong * (F(9) / M0_lo) * r_edge_hi * r_edge_hi
)
assert left_derivative_lo > 0

r_max_hi = F(3, 4) * A_hi - K_lo
psi_slope_lo = M0_lo / 3 - alpha_strong * r_max_hi
residual_slope_hi = (A_hi - M0_lo) / 2
net_strong_slope_lo = psi_slope_lo - residual_slope_hi
assert net_strong_slope_lo > 0

# Strong/fallback boundary C_s(W)=W-(W-K)/sqrt(20/29).
cs_min_lo = A_hi - (A_hi - K_lo) / rcrit_lo
cs_max_hi = M0_lo - (M0_lo - K_hi) / rcrit_hi
assert cs_min_lo > A_hi / 2
assert cs_max_hi < K_lo

weak_phiW_lo = M0_lo / 2 - 2 * alpha_weak * (A_hi - K_lo)
net_weak_slope_lo = weak_phiW_lo - residual_slope_hi
assert net_weak_slope_lo > 0

# C>K branch: generic capacity only.
high_net_slope_lo = K_lo - residual_slope_hi
assert high_net_slope_lo > 0
high_capacity_hi = K_lo * (A_hi - K_lo)
high_margin_lo = Delta_lo - high_capacity_hi
assert high_margin_lo > F(32, 1000)

# Strong-capacity tangent certificate at W=A0. Phi_CC<=-2.
c0 = F(935386, 1_000_000)
assert A_hi / 3 < c0 < A_lo / 2
assert c0 < K_lo
q_lo = 3 - A_hi / c0
q_hi = 3 - A_lo / c0
e_lo = (A_lo + c0) / 2 - K_hi
e_hi = (A_hi + c0) / 2 - K_lo
assert q_lo > 0 and e_lo > 0

phi_hi = c0 * (A_hi - c0) - alpha_strong * q_lo * e_lo * e_lo
part1_lo = A_lo / (c0 * c0) * e_lo * e_lo
part1_hi = A_hi / (c0 * c0) * e_hi * e_hi
part2_lo = q_lo * e_lo
part2_hi = q_hi * e_hi
phi_c_lo = A_lo - 2 * c0 - alpha_strong * (part1_hi + part2_hi)
phi_c_hi = A_hi - 2 * c0 - alpha_strong * (part1_lo + part2_lo)
phi_c_abs_hi = max(abs(phi_c_lo), abs(phi_c_hi))
psi_strong_hi = phi_hi + phi_c_abs_hi * phi_c_abs_hi / 4
strong_margin_lo = Delta_lo - psi_strong_hi
assert strong_margin_lo > F(66, 10_000_000)  # >6.6e-6

# Fallback branch at C_s(A0).
q_weak_lo = 3 - A_hi / cs_min_lo
e_weak_lo = (A_lo + cs_min_lo) / 2 - K_hi
assert q_weak_lo > 0 and e_weak_lo > 0
phi_weak_hi = (
    cs_min_lo * (A_hi - cs_min_lo)
    - alpha_weak * q_weak_lo * e_weak_lo * e_weak_lo
)
weak_margin_lo = Delta_lo - phi_weak_hi
assert weak_margin_lo > F(13, 10_000)  # >1.3e-3

print("PASS corrected uniform strong-branch orbit capacity g=0.0077")
print("Delta_2 lower:", diag(Delta_lo))
print("A0 upper:", diag(A_hi))
print("M0 lower:", diag(M0_lo))
print("strong ratio upper:", diag(strong_ratio_hi))
print("rcrit lower:", diag(rcrit_lo))
print("left-center derivative lower:", diag(left_derivative_lo))
print("net strong W-slope lower:", diag(net_strong_slope_lo))
print("net fallback W-slope lower:", diag(net_weak_slope_lo))
print("net high-center W-slope lower:", diag(high_net_slope_lo))
print("strong capacity margin lower:", diag(strong_margin_lo))
print("fallback capacity margin lower:", diag(weak_margin_lo))
print("high-center capacity margin lower:", diag(high_margin_lo))
print("|Phi_C(c0)| upper:", diag(phi_c_abs_hi))
