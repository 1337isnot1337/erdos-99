#!/usr/bin/env python3
"""Exact certificate: extend the two-leaf outer-energy exclusion to t<=1.84362."""

from fractions import Fraction as Q
from math import factorial, isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator * scale * scale) // lo.denominator)
    b = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    return Q(a, scale), Q(b, scale)


def sin_bounds(x, n=30):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_lower(x):
    _, shi = sin_bounds(x / 6)
    return x - 6 * shi


def F_bounds(x):
    slo, shi = sin_bounds(x / 6)
    return x - 6 * shi, x - 6 * slo


def phase_energy_bounds(x):
    slo, shi = sin_bounds(x / 2)
    return x - 2 * shi, x - 2 * slo


SCALE = 10**100
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
K_lo = Q(2) / sqrt3_hi
K_hi = Q(2) / sqrt3_lo
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C77_lo = 2 * s_lo + Q(77, 10000)
C77_hi = 2 * s_hi + Q(77, 10000)

# ---------------------------------------------------------------------------
# 1. Residual localization at the new endpoint t=1.84362.
# ---------------------------------------------------------------------------
T = Q(92181, 50000)      # 1.84362
c = Q(21, 20)            # 1.05
H = Q(7, 25000)          # 0.00028
Rt_lo = Q(9, 2) * T - 2 * pi_hi - C77_hi
Rt_hi = Q(9, 2) * T - 2 * pi_lo - C77_lo

delta_at_H = (Rt_hi - H) / 2
B_hi = c * c * H * H / (2 * (1 - delta_at_H))
A_lo = pi_lo - T / 2 - c * H - B_hi
localization_margin = F_lower(A_lo) - delta_at_H
assert localization_margin > Q(2, 100000)  # >2e-5

# The parent residual-capacity monotonicity remains strict on this slightly larger box.
Fprime_cap = Q(67, 500)
Qh_upper = (
    -1 / (2 * Fprime_cap)
    + c
    + c * c * Q(101, 1000) / (1 - Q(52, 1000))
)
Qx_upper = -1 / (2 * Fprime_cap) + 1
assert Qh_upper < Q(-5, 2)
assert Qx_upper < Q(-27, 10)

# ---------------------------------------------------------------------------
# 2. Dominant three-phase mass box and U,V<0.525.
# ---------------------------------------------------------------------------
W = Q(956303, 500000)    # 1.912606
assert C77_hi + H < W
RMAX = c * H
E = Q(1813799, 2000000)  # 0.9068995
assert Delta_lo - RMAX * RMAX / 4 > E

U0 = Q(21, 40)           # 0.525
CLOW = W - 2 * U0
CHI = Q(261, 250)        # 1.044
alpha = Q(1, 10)
rcrit_lo, _ = sqrt_bounds(Q(20, 29), Q(20, 29), SCALE)

# Generic center capacity excludes both C<=U0 and C>=CHI.
assert U0 * (W - U0) < E
assert CHI * (W - CHI) < E

# Low-center branch: the strong aggregate phase-star capacity is increasing up to CLOW.
def phi(C):
    q = 3 - W / C
    r = (W + C) / 2 - K_hi
    return C * (W - C) - alpha * q * r * r


def phi_prime(C):
    r = (W + C) / 2 - K_hi
    q = 3 - W / C
    return W - 2 * C - alpha * (W * r * r / (C * C) + q * r)


assert phi_prime(CLOW) > 0
assert phi(CLOW) < E - Q(5, 1000)

# Main interval: the strong physical 1/10 branch is valid for U=U0 and hence for V<=U.
ratio_hi = (CHI + U0 - K_lo) / U0
assert ratio_hi < rcrit_lo


def cap(C):
    V = W - C - U0
    A = 1 - V / C
    B = 1 - U0 / C
    x = alpha * (C + U0 - K_hi) ** 2
    y = alpha * (C + V - K_hi) ** 2
    return C * (U0 + V) - A * x - B * y


def cap_prime(C):
    V = W - C - U0
    A = 1 - V / C
    B = 1 - U0 / C
    eU = C + U0 - K_hi
    eV = C + V - K_hi
    x = alpha * eU * eU
    y = alpha * eV * eV
    Ap = (W - U0) / (C * C)
    Bp = U0 / (C * C)
    return W - 2 * C - Ap * x - A * (2 * alpha * eU) - Bp * y


# cap''<-2 throughout the interval. The left side below increases with C.
Dconst = (
    K_hi * K_hi * W
    + 4 * K_hi * U0 * U0
    - 4 * K_hi * U0 * W
    - U0 * U0 * W
    + U0 * W * W
)
assert (1 + 2 * alpha) * CLOW**3 - alpha * Dconst > CLOW**3

c0 = Q(465961, 500000)   # 0.931922
assert CLOW < c0 < CHI
f0 = cap(c0)
fp0 = cap_prime(c0)
cap_upper = f0 + fp0 * fp0 / 4
assert cap_upper < E - Q(1, 100000)

# ---------------------------------------------------------------------------
# 3. Tightened retained dominant outer mass z>2.2195.
# ---------------------------------------------------------------------------
Z = Q(4439, 2000)        # 2.2195
FZ_lo, FZ_hi = F_bounds(Z)
hstar_lo = Rt_lo - 2 * FZ_hi
hstar_hi = Rt_hi - 2 * FZ_lo
assert hstar_lo > 0
assert hstar_hi < H

# At delta=F(Z), the capped retention excess is maximized at x=0, h=hstar.
capped_retention_hi = (
    Z
    + c * c * hstar_hi * hstar_hi / (2 * (1 - FZ_hi))
    - pi_lo + T / 2 + c * hstar_hi
)
assert capped_retention_hi < Q(-3, 100000)

# The direct x derivative on the delta>=F(Z) side is positive throughout the box.
Bder_hi = (
    1 + c * c * H * H - FZ_lo
) / (2 * (1 - Rt_hi / 2) ** 2)
assert Bder_hi < 1

# ---------------------------------------------------------------------------
# 4. Phasewise convexity: every retained exact phase has mass >0.7100.
# ---------------------------------------------------------------------------
PHASE = Q(71, 100)       # 0.7100
OTHER = (Z - PHASE) / 2
f_phase_lo, _ = phase_energy_bounds(PHASE)
f_other_lo, _ = phase_energy_bounds(OTHER)
delta_max_hi = Rt_hi / 2
phase_imbalance_margin = f_phase_lo + 2 * f_other_lo - delta_max_hi
assert phase_imbalance_margin > Q(3, 1000000)

# ---------------------------------------------------------------------------
# 5. Both leaves carry >0.185 retained O-O pair weight; bad weight <0.036 total.
# ---------------------------------------------------------------------------
PAIR = PHASE - U0
assert PAIR == Q(37, 200)   # 0.185
BAD = Q(9, 250)             # 0.036

# BAD(C-U0)-2[C(W-C)-E] is positive for all real C by negative discriminant.
disc = (BAD - 2 * W) ** 2 - 8 * (2 * E - BAD * U0)
assert disc < 0

GOOD = PAIR - BAD
assert GOOD == Q(149, 1000)  # 0.149

# ---------------------------------------------------------------------------
# 6. Cross-leaf noncrossing energy + disjoint center one-well energy closes the branch.
# ---------------------------------------------------------------------------
SQRT3_UP = Q(17321, 10000)
assert SQRT3_UP * SQRT3_UP > 3
ALT_COST_LO = 2 - SQRT3_UP
leaf_pair_energy_lo = ALT_COST_LO * GOOD

total_outer_energy_lo = leaf_pair_energy_lo + f_phase_lo
final_margin = total_outer_energy_lo - delta_max_hi
assert final_margin > Q(4, 1000)

print("PASS: no full-core Type-II survivor with t<=1.84362")
print("residual localization margin =", float(localization_margin))
print("dominant mass-box slack =", float(W - C77_hi - H))
print("dominant crossing slack =", float(Delta_lo - RMAX * RMAX / 4 - E))
print("low-center capacity margin =", float(E - phi(CLOW)))
print("strong-branch ratio slack =", float(rcrit_lo - ratio_hi))
print("main-interval capacity margin =", float(E - cap_upper))
print("hstar upper =", float(hstar_hi))
print("capped-retention excess upper =", float(capped_retention_hi))
print("phase-imbalance margin =", float(phase_imbalance_margin))
print("leaf O-O pair weight lower =", float(PAIR))
print("bad-weight discriminant =", float(disc))
print("good pair weight per leaf =", float(GOOD))
print("final outer-energy contradiction margin =", float(final_margin))
