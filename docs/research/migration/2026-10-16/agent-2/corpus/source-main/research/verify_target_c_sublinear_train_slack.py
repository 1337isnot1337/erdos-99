#!/usr/bin/env python3
"""Non-load-bearing arithmetic checks for sublinear train-slack exclusion."""

from decimal import Decimal, getcontext

getcontext().prec = 80
pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
coefficient = Decimal(3) * sqrt3 * delta2.sqrt() / Decimal(4)
margin = coefficient - 1
assert delta2 > Decimal(16) / Decimal(27)
assert margin > Decimal("0.2")

# Exact rationalization identity on integer examples.
for T in range(2, 300):
    max_r = T * T // 4
    for R in {1, max_r, max(1, max_r // 2)}:
        sqrt_r = Decimal(R).sqrt()
        sigma = 2 * Decimal(T) - 4 * sqrt_r
        mantel = Decimal(T * T) / 4 - Decimal(R)
        rhs = 8 * mantel / (Decimal(T) + 2 * sqrt_r)
        assert abs(sigma - rhs) < Decimal("1e-70")

print("Delta_2 =", delta2)
print("Section-76 leading coefficient =", coefficient)
print("fixed contradiction margin =", margin)
print("sublinear train-slack arithmetic: PASS")
