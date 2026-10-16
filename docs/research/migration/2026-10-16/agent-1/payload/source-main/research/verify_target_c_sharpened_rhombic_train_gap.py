#!/usr/bin/env python3
"""Outward arithmetic checks for the sharpened rhombic-train gap."""
from decimal import Decimal, getcontext
getcontext().prec = 70
D = Decimal
S = D('0.00119')
R_LO = D('0.9523128068')
R_HI = D('0.9523128069')
SQRT3_LO = D('1.7320508075')
M_LO = 4 * R_LO * R_LO / (2 * R_LO + S / 2)
d_HI = S * R_HI / 2 + S * S / 16
sqrt_d = d_HI.sqrt()
u_HI = (D(6) * d_HI).sqrt()
p_HI = (D(2) * d_HI).sqrt()
L_LO = M_LO / 2 - sqrt_d - u_HI
E_LO = 3 * M_LO / 4 - sqrt_d / 2 - u_HI - 6 * p_HI
CAP_HI = D(2) / SQRT3_LO
PROJECTED_LO = SQRT3_LO * E_LO / 2
MANTEL_LO = S / 8 * (4 * R_LO + S / 2)
B_RETAIN_LO = L_LO / 2 - 2 * p_HI
TRIPLE_NEED_HI = 3 * p_HI
assert E_LO > CAP_HI + D('0.0010')
assert PROJECTED_LO > D('1.0009')
assert B_RETAIN_LO > TRIPLE_NEED_HI
assert L_LO > 0
assert MANTEL_LO > D('0.000566')
print('PASS sharpened rhombic-train gap arithmetic')
print('sigma_safe=', S)
print('M_lower=', M_LO)
print('d_upper=', d_HI)
print('minority_loss_upper=', u_HI)
print('p_upper=', p_HI)
print('per_shore_retained_lower=', L_LO)
print('second_family_after_pruning_lower=', B_RETAIN_LO)
print('triple_common_neighbor_need_upper=', TRIPLE_NEED_HI)
print('opposite_corner_degree_sum_lower=', E_LO)
print('2/sqrt3_upper=', CAP_HI)
print('degree_sum_margin_lower=', E_LO - CAP_HI)
print('projected_diameter_coefficient_lower=', PROJECTED_LO)
print('projected_margin_lower=', PROJECTED_LO - D(1))
print('Mantel_deficit_coefficient_lower=', MANTEL_LO)
