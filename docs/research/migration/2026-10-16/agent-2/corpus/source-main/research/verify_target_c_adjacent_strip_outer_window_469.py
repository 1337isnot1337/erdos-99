#!/usr/bin/env python3
"""Exact certificate for the 469-edge adjacent-strip outer-window bound.

Uses the optimized live-backbone density from OP543 together with the Type-II
outer-walk identity b/D = pi + delta + o(1) and the matched g=.007707 residual
envelope at t<=1.844.
"""
from fractions import Fraction as Q
from math import isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2*k+1) * q**(2*k+1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2*n+1) * q**(2*n+1))
    return (s, s+nxt) if n % 2 == 0 else (s-nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator * scale * scale) // lo.denominator)
    b = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    return Q(a, scale), Q(b, scale)


S = 10**100
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16*a5_lo - 4*a239_hi
pi_hi = 16*a5_hi - 4*a239_lo

n3 = isqrt(3*S*S)
sqrt3_lo = Q(n3, S)
sqrt3_hi = Q(n3+1, S)
Delta_lo = pi_lo / (2*sqrt3_hi)
Delta_hi = pi_hi / (2*sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, S)
C707_lo = 2*s_lo + Q(7707, 1_000_000)

# Current t<=1.844 endpoint. The residual identity
#   2 delta + kappa/2 + h = 9t/2 - 2pi - C707
# has kappa,h>=0, so the right side/2 is an upper bound for delta.
T = Q(461, 250)
R_hi = Q(9, 2)*T - 2*pi_lo - C707_lo
delta_hi = R_hi / 2
assert 0 < delta_hi < Q(513, 10000)

# Optimized OP543 backbone density, recomputed exactly from its audited fan inputs.
A = Q(1851, 2500)      # .7404 weighted center-degree average
W = Q(53, 625)         # .0848 retained O-O pair weight
NC = Q(1063, 1000)     # 1.063 center-train upper density
lam = Q(1601, 2500)    # .6404 good-leaf threshold
d_low = Q(1, 10000)
r = (lam - d_low) / NC
d_top = lam - (1-r)*NC
g = (A-lam)*W/(NC-lam)
p = d_top*g/(r*NC)
assert p > Q(68, 10000)

# The occurrence-counted outer facial walk has b/D = pi+delta+o(1).
# Consecutive proper crosscuts on one simple dual path cut the boundary circle into
# pairwise-disjoint middle-arc intervals, so some internal strip has total middle-arc
# length at most (pi+delta)/p + o(1).
outer_density_hi = pi_hi + delta_hi
ratio = outer_density_hi / p
assert ratio < Q(469)
assert Q(469) - ratio > Q(1)

print("PASS adjacent-strip outer window <469+o(1)")
print("backbone density p =", float(p))
print("delta upper =", float(delta_hi))
print("outer-walk density upper =", float(outer_density_hi))
print("window average upper =", float(ratio))
print("margin to 469 =", float(Q(469)-ratio))
