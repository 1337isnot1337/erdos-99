#!/usr/bin/env python3
"""Arithmetic/algebra regression for singleton/hole incidence coupling.

The incidence theorem itself is combinatorial; this script checks only the displayed
constant arithmetic and the rearrangements in SH.6--SH.7.
"""
import math

pi = math.pi
sqrt3 = math.sqrt(3.0)
Delta2 = pi / (2.0 * sqrt3)
s0 = math.sqrt(Delta2)
f_star = s0 - pi / 4.0 + 0.00021
c_df = s0 - pi / 4.0 + 0.00105

assert abs(f_star - 0.167124643466509) < 1e-15
assert abs(c_df - 0.167964643466509) < 1e-15

# Generic positive test values for the exact rearrangements.
sqrtR = 123.4
sigma = 7.8
S_E = 5.6
f = 11.2
X = 3.4
k = 2.1
D = 100.0
T_R = 2.0 * sqrtR + sigma / 2.0
Q = f + X
G = sigma + 2.0 * S_E

raw_flex = T_R - (2.0 / 5.0) * (4.0 * f + Q - S_E)
rearranged_flex = 2.0 * sqrtR - 2.0 * f - (2.0 / 5.0) * X + (3.0 / 10.0) * sigma + G / 5.0
assert abs(raw_flex - rearranged_flex) < 1e-12

raw_noo = T_R - (4.0 * f + Q) + S_E
rearranged_noo = 2.0 * sqrtR - 5.0 * f - X + G / 2.0
assert abs(raw_noo - rearranged_noo) < 1e-12

# If SH.5 is saturated, SH.6--SH.7 agree exactly with substitution.
G_floor = c_df * D + 2.5 * k + X
flex_floor = 2.0 * sqrtR - 2.0 * f - (2.0 / 5.0) * X + (3.0 / 10.0) * sigma + G_floor / 5.0
flex_display = 2.0 * sqrtR + c_df * D / 5.0 + k / 2.0 - 2.0 * f - X / 5.0 + 3.0 * sigma / 10.0
assert abs(flex_floor - flex_display) < 1e-12

noo_floor = 2.0 * sqrtR - 5.0 * f - X + G_floor / 2.0
noo_display = 2.0 * sqrtR + c_df * D / 2.0 + 1.25 * k - 5.0 * f - X / 2.0
assert abs(noo_floor - noo_display) < 1e-12

endpoint_noo = 2.0 * s0 + c_df / 2.0 - 5.0 * f_star
endpoint_flex = 2.0 * s0 + c_df / 5.0 - 2.0 * f_star
assert endpoint_noo > 1.15
assert endpoint_flex > 1.60

print(f"f_star={f_star:.15f}")
print(f"c_DF={c_df:.15f}")
print(f"formal endpoint N_oo coefficient={endpoint_noo:.15f}")
print(f"formal endpoint train-flex coefficient={endpoint_flex:.15f}")
print("singleton/hole incidence coupling arithmetic: PASS")
