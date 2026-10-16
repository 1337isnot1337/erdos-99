#!/usr/bin/env python3
"""Outward Decimal certificate for the phase-star atomic gap g=0.0009."""
from decimal import Decimal, getcontext
getcontext().prec = 70
D = Decimal
G = D('0.0009')
S_LO = D('0.9523128068')
S_HI = D('0.9523128069')
SQRT3_LO = D('1.7320508075')
W_LO = 4 * S_LO * S_LO / (2 * S_LO + G)
d_HI = S_HI * G + G * G / 4
z_HI = d_HI.sqrt()
q_LO = (W_LO / 2 - 3 * z_HI) / (W_LO - 2 * z_HI)
m_HI = d_HI / q_LO
p_HI = m_HI.sqrt()
C_LO = W_LO / 2 - z_HI
U_LO = W_LO / 4 - z_HI / 2
E_LO = 3 * W_LO / 4 - z_HI / 2 - 6 * p_HI
CAP_HI = D(2) / SQRT3_LO
PROJECTED_LO = SQRT3_LO * E_LO / 2
assert W_LO > D('1.9037')
assert q_LO > D('0.468')
assert U_LO > 5 * p_HI
assert C_LO > 5 * p_HI
assert E_LO > CAP_HI + D('0.0017')
assert PROJECTED_LO > D('1.00149')
print('PASS phase-star atomic gap g=0.0009 arithmetic')
print('g_safe=', G)
print('dominant_orbit_mass_lower=', W_LO)
print('orbit_deficit_upper=', d_HI)
print('center_leaf_denominator_lower=', q_LO)
print('center_large_leaf_missing_upper=', m_HI)
print('pruning_threshold_upper=', p_HI)
print('large_leaf_common_neighbor_margin=', U_LO - 5 * p_HI)
print('opposite_corner_degree_sum_lower=', E_LO)
print('degree_sum_margin_lower=', E_LO - CAP_HI)
print('projected_diameter_coefficient_lower=', PROJECTED_LO)
print('projected_margin_lower=', PROJECTED_LO - D(1))
