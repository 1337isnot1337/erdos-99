#!/usr/bin/env python3
"""Exact arithmetic certificate for the correlated low-energy O-O path through t<=1.860."""

from fractions import Fraction as Q
from math import factorial


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sin_bounds(x, n=20):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


a5_lo, a5_hi = atan_inv_bounds(5, 80)
a239_lo, a239_hi = atan_inv_bounds(239, 20)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

# Parent exact bootstrap theorem supplies z>2.0783 uniformly through t<=1.860.
T = Q(93, 50)
z0 = Q(20783, 10000)
lam = Q(9, 10)

# U = 9t/2 - 2pi - 2delta - kappa/2.
# For low-energy pair weight, keep the same delta instead of independently maximizing it:
#   P_low >= (z-U) - delta/lam
#         >= z-Umax + (2-1/lam) delta
#         >= z0-Umax + (2-1/lam) F(z0).
Umax_hi = Q(9, 2) * T - 2 * pi_lo
Flo, _ = F_bounds(z0)
coeff = 2 - 1 / lam
assert coeff > 0

low_total = z0 - Umax_hi + coeff * Flo
assert low_total > Q(281, 10000)  # >0.0281

low_phase = low_total / 3
assert low_phase > Q(93, 10000)  # >0.0093

# e_tau<=0.9 gives terminal-arc gap
# pi - 2 arccos(0.1) = 2 asin(0.1) > 0.2.

# A path of density >0.0093 has, after discarding the one hub boundary,
# one nonhub boundary with at most 675 switching rows.
pi_up = Q(355, 113)
avg_switch_up = 2 * pi_up / Q(93, 10000)
assert avg_switch_up < 676

print("F(2.0783) lower =", float(Flo))
print("Umax upper =", float(Umax_hi))
print("correlated low-energy total pair weight >", float(low_total))
print("one-phase low-energy path density >", float(low_phase))
print("2*pi_up/0.0093 =", float(avg_switch_up), "< 676")
print("PASS correlated low-energy dual path through t<=1.860")
