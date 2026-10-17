#!/usr/bin/env python3
"""Exact certificate for the 0.7404-fan dual-tree rectangle profile."""

from fractions import Fraction as Q

F = Q(1851, 2500)       # 0.7404 weighted average center degree
P = Q(53, 625)          # 0.0848 retained pair-weight density
C = Q(1063, 1000)       # center-train density ceiling


def good_density(lam):
    return (F - lam) * P / (C - lam)


def backbone_density(lam):
    return lam * good_density(lam) / C


def penalty_slope(lam):
    return C / backbone_density(lam)


def common_center_density(lam, rho):
    return lam - penalty_slope(lam) * rho


# Balanced square choice.
lam_bal = Q(561, 1000)
rho_bal = Q(831, 100000)  # 0.00831
g_bal = good_density(lam_bal)
s_bal = backbone_density(lam_bal)
a_bal = penalty_slope(lam_bal)
c_bal = common_center_density(lam_bal, rho_bal)

assert g_bal == Q(47541, 1568750)
assert g_bal > Q(303, 10000)
assert s_bal == Q(26670501, 1667581250)
assert a_bal == Q(7090555475, 106682004)
assert rho_bal < s_bal
assert c_bal == Q(1234784329, 142242672000)
assert c_bal > rho_bal
assert c_bal - rho_bal > Q(37, 100000)  # > 0.00037

# High-product choice.
lam_prod = Q(3, 5)
rho_prod = Q(409, 100000)  # 0.00409
g_prod = good_density(lam_prod)
s_prod = backbone_density(lam_prod)
a_prod = penalty_slope(lam_prod)
c_prod = common_center_density(lam_prod, rho_prod)

assert g_prod == Q(37206, 1446875)
assert g_prod > Q(257, 10000)
assert s_prod == Q(892944, 61521125)
assert a_prod == Q(523175647, 7143552)
assert rho_prod < s_prod
assert c_prod == Q(214634280377, 714355200000)
assert c_prod > Q(3004, 10000)
assert rho_prod * c_prod > Q(12288, 10_000_000)  # > 0.0012288

# Both choices strictly improve the previously merged profile constants.
assert rho_bal > Q(779, 100000)           # old balanced leaf shore 0.00779
assert Q(3004, 10000) > Q(285, 1000)      # old product center shore 0.285
assert rho_prod > Q(395, 100000)           # old simple product leaf shore 0.00395

print("PASS: 0.7404-fan rectangle profile")
print("balanced lambda =", float(lam_bal))
print("balanced good density =", float(g_bal))
print("balanced backbone density =", float(s_bal))
print("balanced penalty slope =", float(a_bal))
print("balanced leaf density =", float(rho_bal))
print("balanced center density lower =", float(c_bal))
print("balanced center-minus-leaf margin =", float(c_bal - rho_bal))
print("product lambda =", float(lam_prod))
print("product good density =", float(g_prod))
print("product backbone density =", float(s_prod))
print("product leaf density =", float(rho_prod))
print("product center density lower =", float(c_prod))
print("product crossing density lower =", float(rho_prod * c_prod))
