#!/usr/bin/env python3
"""Exact arithmetic certificate for the t<=1.844 small-leaf rectangle Pareto profile."""

from fractions import Fraction as Q

s0 = Q(627, 42520)
d0 = Q(57, 100)
n0 = Q(1063, 1000)
alpha = n0 / s0

assert alpha == Q(1129969, 15675)

rho_max = d0 / alpha
rho_bal = d0 / (1 + alpha)
rho_prod = d0 / (2 * alpha)

assert rho_max == Q(35739, 4519876)
assert rho_bal == Q(35739, 4582576)
assert rho_prod == Q(35739, 9039752)
assert 0 < rho_prod < rho_bal < rho_max < s0

# Balanced safe square.
rho_sq = Q(779, 100000)
center_sq = d0 - alpha * rho_sq
assert rho_sq < rho_bal
assert center_sq == Q(696271, 82500000)
assert center_sq > rho_sq

# Product optimum and a simple nearby decimal choice.
center_prod = d0 - alpha * rho_prod
assert center_prod == Q(57, 200)
product_opt = rho_prod * center_prod
assert product_opt > Q(11267, 10_000_000)  # > 0.0011267

rho_decimal = Q(79, 20000)  # 0.00395
center_decimal = d0 - alpha * rho_decimal
assert center_decimal == Q(89427449, 313500000)
assert center_decimal > Q(285, 1000)

# The original fixed theorem point lies on the same valid tradeoff and the advertised
# 0.35 center density is safely below the exact Pareto lower bound.
rho_old = Q(3, 1000)
center_old = d0 - alpha * rho_old
assert center_old > Q(7, 20)

# Concavity/product optimization is exact: P'(rho)=d0-2 alpha rho vanishes at rho_prod.
assert d0 - 2 * alpha * rho_prod == 0
assert alpha > 0

print("s0 =", s0, float(s0))
print("alpha =", alpha, float(alpha))
print("rho_max =", rho_max, float(rho_max))
print("rho_bal =", rho_bal, float(rho_bal))
print("balanced safe rho =", rho_sq, float(rho_sq))
print("balanced center lower =", center_sq, float(center_sq))
print("balanced center margin =", float(center_sq - rho_sq))
print("rho_prod =", rho_prod, float(rho_prod))
print("center_prod =", center_prod, float(center_prod))
print("product_opt =", product_opt, float(product_opt))
print("rho=.00395 center lower =", center_decimal, float(center_decimal))
print("old rho=.003 exact center lower =", center_old, float(center_old))
print("PASS: small-leaf rectangle Pareto profile")
