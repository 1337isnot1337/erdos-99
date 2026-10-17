#!/usr/bin/env python3
"""Exact certificate for the joint-feasibility opposite-branch O-O path through t<=1.860."""

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


def sin_bounds(x, n=24):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


# Outward constants.
a5_lo, a5_hi = atan_inv_bounds(5, 90)
a239_lo, a239_hi = atan_inv_bounds(239, 25)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10**100
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
sD_lo, _ = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C76_lo = 2 * sD_lo + Q(19, 2500)

T = Q(93, 50)  # 1.860
U0_lo = Q(9, 2) * T - 2 * pi_hi
U0_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (U0_hi - C76_lo) / 2

assert delta_max_hi < Q(11, 125)  # 0.088
assert U0_hi < Q(21, 10)  # 2.1

# On U>=C76=2sqrt(Delta)+.0076, m2'(U)<0 and r'(U)>1.
# Also r'(U)<=3/2 because U/sqrt(8Delta-U^2)<=2, equivalent to
# 5U^2<=32Delta; it suffices to check the largest U=U0.
assert 5 * U0_hi * U0_hi < 32 * Delta_lo

# For the relaxed feasibility function G(delta,z),
# 2(1-delta)^2 G_delta
# = 1-F(z)+r^2-4r'(1-delta)(r+1-delta).
# Use r<=U/2<1.05 and 1-delta>0.912.
rmax = Q(21, 20)
one_minus_delta = Q(114, 125)
assert 1 + rmax * rmax < 4 * one_minus_delta * one_minus_delta

# Hence G_delta<0. A coarse lower derivative bound used below is G_delta>-7.5.
Gd_lower = -6 * (1 + rmax) / (2 * one_minus_delta * one_minus_delta)
assert Gd_lower > -Q(15, 2)

z0 = Q(2107, 1000)

# F'(z)=1-cos(z/6)<=z^2/72<1/16 on [0,z0].
assert z0 * z0 / 72 < Q(1, 16)

# G_z=1-F'(z)/(2(1-delta)) >24/25.
Gz_lower = 1 - Q(1, 16) / (2 * one_minus_delta)
assert Gz_lower > Q(24, 25)

# H(z)=G(F(z),z) therefore has
# H'=G_z+G_delta F' > .96-7.5/16 >0 on [0,z0].
assert Q(24, 25) - Q(15, 2) * Q(1, 16) > 0

# Exact outward evaluation H(z0)<0.
Flo, Fhi = F_bounds(z0)
Ulo = U0_lo - 2 * Fhi
Uhi = U0_hi - 2 * Flo
xlo = 8 * Delta_lo - Uhi * Uhi
xhi = 8 * Delta_hi - Ulo * Ulo
assert xlo > 0
root_lo, _ = sqrt_bounds(xlo, xhi, SCALE)
mlo = (Ulo + root_lo) / 2
rhi = Uhi - mlo
p_hi = rhi * rhi / (2 * (1 - Fhi))
S_lo = pi_lo - Uhi - T / 2 + mlo
H_hi = z0 + p_hi - S_lo
assert H_hi < 0

# lambda=1/2: opposite-branch exclusion is uniform under delta<.088.
lam = Q(1, 2)
brace = 1 - Q(11, 125) - lam / 2
same_sq = lam - lam * lam / 4
assert brace > 0
assert brace * brace > same_sq

# At lambda=1/2 the delta term cancels exactly:
# P_low >= z-U-2delta = z-(9t/2-2pi)+kappa/2.
low_total_lo = z0 - U0_hi
assert low_total_lo > Q(201, 10000)  # >0.0201
low_phase_lo = low_total_lo / 3
assert low_phase_lo > Q(67, 10000)  # >0.0067

# One nonhub path boundary has at most 937 switching rows.
pi_up = Q(355, 113)
avg_switch_up = 2 * pi_up / Q(67, 10000)
assert avg_switch_up < 938

print("PASS joint-feasibility opposite-branch path through t<=1.860")
print("U0 upper =", float(U0_hi))
print("delta_max upper =", float(delta_max_hi))
print("G_delta crude lower =", float(Gd_lower))
print("G_z lower =", float(Gz_lower))
print("H(2.107) outward upper =", float(H_hi))
print("opposite-branch squared margin using delta<.088 =", float(brace * brace - same_sq))
print("low-energy total pair floor =", float(low_total_lo))
print("one-phase low-energy path floor =", float(low_phase_lo))
print("switch-count average upper =", float(avg_switch_up))
