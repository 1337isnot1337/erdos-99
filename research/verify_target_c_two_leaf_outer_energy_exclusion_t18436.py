#!/usr/bin/env python3
"""Exact certificate: the two-leaf O-O/center-energy package excludes t<=1.8436.

Inputs already proved at this scope:
  * g=.0077 residual stability and t<=1.8436 localization h<.00013;
  * both leaf train masses U,V<.513;
  * the common-center low-degree O-O weight bound BAD<.03405;
  * phasewise one-well bathtub energy and the cross-phase endpoint-alternation cost.

New exact steps certified here:
  1. total retained dominant outer mass z>2.2196;
  2. every phase retains >.7179 outer-occurrence mass;
  3. hence each leaf has >.2049 O-O pair weight;
  4. the two leaf pair-energy lower bound plus center one-well energy exceeds the
     complete outer-detour budget by more than .01D.
"""

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
    b = isqrt((hi.numerator * scale * scale) // hi.denominator)
    return Q(a, scale), Q(b + 1, scale)


def sin_bounds(x, n=28):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    """F(z)=z-6 sin(z/6)."""
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


def phase_energy_bounds(z):
    """f(z)=z-2 sin(z/2)."""
    slo, shi = sin_bounds(z / 2)
    return z - 2 * shi, z - 2 * slo


# Exact pi / sqrt(3) / Delta_2 enclosures.
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10**100
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)

# Use the already hostile-audited g=.0077 residual localization.
C77_lo = 2 * s_lo + Q(77, 10000)
C77_hi = 2 * s_hi + Q(77, 10000)
T = Q(4609, 2500)       # 1.8436
c = Q(21, 20)           # 1.05
H = Q(13, 100000)       # certified h<.00013

Rt_lo = Q(9, 2) * T - 2 * pi_hi - C77_hi
Rt_hi = Q(9, 2) * T - 2 * pi_lo - C77_lo
delta_max_hi = Rt_hi / 2
assert delta_max_hi < Q(51, 1000)

# ---------------------------------------------------------------------------
# 1. Tighten total retained dominant mass to z>2.2196.
# ---------------------------------------------------------------------------
Z = Q(5549, 2500)       # 2.2196
FZ_lo, FZ_hi = F_bounds(Z)

# Under the cap z<=Z, the worst retention point occurs on the energy boundary
# delta=F(Z), with x=0 and h=Rt-2F(Z).  The parent Q_x,Q_h monotonicity handles
# the delta<F(Z) side; on delta>=F(Z), direct differentiation moves x to the
# boundary.  Check that this boundary lies inside the certified h-window.
hstar_lo = Rt_lo - 2 * FZ_hi
hstar_hi = Rt_hi - 2 * FZ_lo
assert hstar_lo > 0
assert hstar_hi < H

# The capped retention excess is
#   Z + c^2 h^2/[2(1-F(Z))] - [pi-T/2-c h].
# An upper bound is still strictly negative.
capped_retention_hi = (
    Z
    + c * c * hstar_hi * hstar_hi / (2 * (1 - FZ_hi))
    - pi_lo + T / 2 + c * hstar_hi
)
assert capped_retention_hi < Q(-5, 100000)  # <-5e-5

# The direct x derivative on the delta>=F(Z) branch has sign
# 1-B/2, B=(1+c^2h^2-F(Z))/(2(1-delta)^2); certify it positive.
B_hi = (
    1 + c * c * H * H - FZ_lo
) / (2 * (1 - delta_max_hi) * (1 - delta_max_hi))
assert B_hi < 1

# ---------------------------------------------------------------------------
# 2. Phasewise convexity forces every z_i>.7179.
# ---------------------------------------------------------------------------
A = Q(7179, 10000)      # .7179
OTHER = (Z - A) / 2
fA_lo, _ = phase_energy_bounds(A)
fO_lo, _ = phase_energy_bounds(OTHER)
phase_imbalance_energy_lo = fA_lo + 2 * fO_lo
assert phase_imbalance_energy_lo - delta_max_hi > Q(8, 10_000_000)

# ---------------------------------------------------------------------------
# 3. Both leaves then have >.2049 O-O pair weight.
# ---------------------------------------------------------------------------
LEAF_MASS_MAX = Q(513, 1000)
PAIR = A - LEAF_MASS_MAX
assert PAIR == Q(2049, 10000)

# ---------------------------------------------------------------------------
# 4. Common-center two-leaf energy + center energy closes the branch.
# ---------------------------------------------------------------------------
# Reproduce the exact low-center-degree certificate already used by the
# two-leaf common-center bridge.
W = Q(239057, 125000)        # 1.912456
E = Q(90689967, 100000000)   # .90689967
BAD = Q(681, 20000)          # .03405
assert LEAF_MASS_MAX * (W - LEAF_MASS_MAX) < E

disc = (BAD - 2 * W) ** 2 - 8 * (2 * E - BAD * LEAF_MASS_MAX)
assert disc < 0

GOOD = PAIR - BAD
assert GOOD > Q(1708, 10000)  # >.1708 in each leaf

# sqrt(3)<1.7321, so the nonalternating-endpoint cost is >.2679.
SQRT3_UP = Q(17321, 10000)
assert SQRT3_UP * SQRT3_UP > 3
ALT_COST_LO = 2 - SQRT3_UP
leaf_pair_energy_lo = ALT_COST_LO * GOOD

# Center selected occurrences are physically disjoint from the two leaf
# terminal-edge populations, so these payments add.
total_outer_energy_lo = leaf_pair_energy_lo + fA_lo
assert total_outer_energy_lo - delta_max_hi > Q(1, 100)  # >.01

print("PASS: no full-core Type-II survivor with t<=1.8436")
print("delta budget upper =", float(delta_max_hi))
print("h* interval =", float(hstar_lo), float(hstar_hi))
print("capped-retention excess upper =", float(capped_retention_hi))
print("phase-imbalance margin =", float(phase_imbalance_energy_lo - delta_max_hi))
print("leaf O-O pair weight lower =", float(PAIR))
print("good high-center-degree pair weight lower =", float(GOOD))
print("two-leaf pair-energy lower =", float(leaf_pair_energy_lo))
print("center one-well energy lower =", float(fA_lo))
print("final energy contradiction margin =", float(total_outer_energy_lo - delta_max_hi))
