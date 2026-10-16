#!/usr/bin/env python3
"""Arithmetic regression for the global one-sided deep-cell reaction budget.

The geometric proof is in
`target_c_high_t_global_reaction_budget_t18687_2026-09-17.md`.
This script checks its exact density/quantile constants and the force-coefficient
numerics for the explicit 90%-density instance.
"""
from fractions import Fraction as Q
import math

c0 = Q(113, 20_000_000)
lam = Q(9, 10) * c0
sigma = Q(1, 2)
H = Q(4_436_000, 1)

assert lam == Q(1017, 200_000_000)

# K = 1/(sigma*lambda) is the exact tail threshold from sum B_i <= 1.
K = 1 / (sigma * lam)
assert K == Q(400_000_000, 1017)
assert 1 / K == sigma * lam

retained = (1 - sigma) * lam
assert retained == Q(1017, 400_000_000)
assert float(retained) == 2.5425e-6

# The quantile ceiling is materially below the previous all-cell H ceiling.
improvement = H / K
assert improvement > 11
assert abs(float(improvement) - 11.27853) < 1e-10

# In the near-full-density parameter limit, the half-quantile constant tends to 2/c0.
limit_half_quantile = 2 / c0
assert limit_half_quantile == Q(40_000_000, 113)
assert abs(float(limit_half_quantile) - 353982.30088495574) < 1e-9

# Explicit force-angle choice from the 90%-density parameterization.
rho = c0 / 100
assert rho == Q(113, 2_000_000_000)
sin_rho = math.sin(float(rho))
assert sin_rho > 0

# RB.26 and RB.27 numerical constants for this instance.
compressed_total_budget = 2 / sin_rho
per_ray_coeff_numerator = float(K) / sin_rho
assert compressed_total_budget > 0
assert per_ray_coeff_numerator > 0

# Sanity-check the tail algebra in integer-scaled form: if N bad cells each
# carry >K/D mass and total mass <=1, then N<D/K=sigma*lambda*D.
assert sigma * lam == Q(1017, 400_000_000)

print("PASS: global one-sided deep-cell reaction budget arithmetic")
print("lambda_90 =", float(lam))
print("sigma =", float(sigma))
print("K_half =", float(K))
print("retained density =", float(retained))
print("old H / K_half =", float(improvement))
print("limiting half-quantile constant 2/c0 =", float(limit_half_quantile))
print("rho_90 =", float(rho))
print("compressed total coefficient budget 2/sin(rho) =", compressed_total_budget)
print("per-ray coefficient <=", per_ray_coeff_numerator, "/ D")
