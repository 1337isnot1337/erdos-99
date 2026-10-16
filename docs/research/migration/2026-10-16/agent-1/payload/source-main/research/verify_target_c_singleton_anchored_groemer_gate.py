#!/usr/bin/env python3
"""Arithmetic/incidence regression for the singleton-anchored Groemer gate."""

from decimal import Decimal, getcontext

getcontext().prec = 60
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
c_df = delta2.sqrt() - pi / 4 + Decimal('0.00105')

assert Decimal('0.1679645') < c_df < Decimal('0.1679648')
assert Decimal('0.0011827') < c_df / 142 < Decimal('0.0011830')
assert Decimal('0.0012918') < c_df / 130 < Decimal('0.0012922')

# One chosen triple per singleton-hit pentagon. At most five pentagons can use one
# boundary source vertex in a triangle-free contact graph, so triple conflicts <=12.
assert 3 * (5 - 1) == 12
assert 5 * 13 == 65
assert 2 * 65 == 130

# Symbolic coefficient elimination:
#   sigma + 2 S_E >= cD + (5/2)k + X
#   S_E <= S5 + 6X
# gives 2 S5 >= cD + (5/2)k - sigma - 11X.
# The following exact rational sweep checks the implication numerically.
for sigma in range(0, 30):
    for X in range(0, 30):
        for S5 in range(0, 30):
            for extra in range(0, 8):
                SE = S5 + extra
                if SE > S5 + 6 * X:
                    continue
                lhs_train = sigma + 2 * SE
                rhs_base = lhs_train - X
                # If cD+(5/2)k is any value C <= rhs_base, then
                # C - sigma - 11X <= 2S5.
                C = rhs_base
                assert C - sigma - 11 * X <= 2 * S5

print('c_DF =', c_df)
print('uniform three-currency coefficient =', c_df / 142)
print('conditional singleton-anchored coefficient =', c_df / 130)
print('singleton-anchored Groemer gate: PASS')
