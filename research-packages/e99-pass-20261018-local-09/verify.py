#!/usr/bin/env python3
"""Exact rational audit of constants in the pinned twelve-arc proof."""

from fractions import Fraction as F
import json


def require(condition, label):
    if not condition:
        raise ValueError(label)


# Certified rational enclosure of sqrt(3); the integer square tests are exact.
sqrt3_lo = F(1732050807568877293, 10**18)
sqrt3_hi = F(1732050807568877294, 10**18)
require(sqrt3_lo * sqrt3_lo < 3 < sqrt3_hi * sqrt3_hi, "sqrt(3) enclosure")

a_lo, a_hi = sqrt3_lo / 2, sqrt3_hi / 2
p_lo, p_hi = 1 - a_hi, 1 - a_lo
q_lo, q_hi = F(98, 65) - a_hi, F(98, 65) - a_lo
b_lo, b_hi = a_lo - q_hi, a_hi - q_lo
h = F(56, 65)
k = F(9, 56)  # 1/h - 1: inserted count less deleted old row length
c = F(65, 28)  # 2/h
s = F(256, 16385)
beta = F(16383, 16385)

require(0 < p_lo and p_hi < q_lo and q_hi < a_lo, "height ordering")
require(b_lo > 0, "positive arc-width difference")
require(h * h + F(33, 65) ** 2 == 1, "adjacent inserted contacts")
require(F(1, 1) - p_hi == a_lo, "lower-row vertical guard")
require(F(98, 65) - 1 == F(33, 65), "alternating row offset")
require(beta * beta + s * s == 1, "arc cone identity")
require(b_lo * beta / s > 14, "packet length exceeds two")
require(beta * 8192 + a_hi < 8192, "radius-onset guard")
cross_frame_clearance = beta * (beta - sqrt3_hi * s)
require(cross_frame_clearance > F(1, 2), "different-frame angular separation")

# Net row gain is K - ell.  From K >= (ell - 2)/h this is
# (1/h - 1) ell - 2/h = k ell - c.
one_minus_beta = 1 - beta
gamma_numerator_lo = k * b_lo * s - c * one_minus_beta
gamma_numerator_hi = k * b_hi * s - c * one_minus_beta
require(gamma_numerator_lo > 0, "positive linear reserve")
gamma_lo = 6 * gamma_numerator_lo / a_hi
gamma_hi = 6 * gamma_numerator_hi / a_lo
require(F(193, 100000) < gamma_lo < gamma_hi < F(194, 100000),
        "effective gamma interval")

# The coefficient of sqrt(R) in the integrated top-edge loss is
# A = (8 sqrt(2)/a) k b^(3/2). Bound A^2 using rational endpoints.
a2_sqrt_error_hi = 128 * k * k * b_hi**3 / (a_lo * a_lo)
require(0 < a2_sqrt_error_hi < F(1, 16), "square-root error below 1/4")
wrong_net_coefficient = F(65, 56)  # 1/h, omitting deletion of the old row labels
wrong_a2_lo = 128 * wrong_net_coefficient**2 * b_lo**3 / (a_hi * a_hi)
require(wrong_a2_lo > F(1, 16), "net-gain negative control was not rejected")

# B0 = (12/a) k b (2 beta a/s + a^2/(8192 s)); cancel a
# and bound the remaining positive factors at their upper endpoints.
constant_error_hi = 12 * k * b_hi * (2 * beta / s + a_hi / (8192 * s))
require(0 < constant_error_hi < 60, "constant error below 60")

# gamma > 193/100000 implies the stated D/600 bound for x=sqrt(D)>=1000.
x = F(1000)
gap = F(193, 100000) - F(1, 600)
require(gap == F(79, 300000), "threshold coefficient")
require(gap * x * x - x / 5 - 60 == F(10, 3), "threshold value at 10^6")
require(2 * gap * x - F(1, 5) > 0, "threshold monotonicity")

print(json.dumps({
    "result": "PASS",
    "scope": "exact rational endpoint checks for the twelve-arc proof constants",
    "gamma_interval": [str(gamma_lo), str(gamma_hi)],
    "square_root_error_squared_upper": str(a2_sqrt_error_hi),
    "insertion_only_coefficient_control": "REJECTED",
    "constant_error_upper": str(constant_error_hi),
    "cross_frame_clearance_lower": str(cross_frame_clearance),
}, sort_keys=True))
