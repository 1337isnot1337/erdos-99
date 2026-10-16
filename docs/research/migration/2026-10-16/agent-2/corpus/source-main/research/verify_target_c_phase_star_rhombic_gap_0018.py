#!/usr/bin/env python3
"""Outward arithmetic checks for the 0.0018 phase-star rhombic gap."""
from decimal import Decimal, getcontext
getcontext().prec = 70
D = Decimal
S = D('0.0018')
R_LO = D('0.9523128068')
R_HI = D('0.9523128069')
SQRT3_LO = D('1.7320508075')
W_LO = 4 * R_LO * R_LO / (2 * R_LO + S / 2)
d_HI = S * R_HI / 2 + S * S / 16
z_HI = d_HI.sqrt()
q_LO = (W_LO / 2 - 3 * z_HI) / (W_LO - 2 * z_HI)
m_HI = d_HI / q_LO
p_HI = m_HI.sqrt()
C_LO = W_LO / 2 - z_HI
U_LO = W_LO / 4 - z_HI / 2
RAW_SUM_LO = 3 * W_LO / 4 - z_HI / 2
E_LO = RAW_SUM_LO - 6 * p_HI
CAP_HI = D(2) / SQRT3_LO
PROJECTED_LO = SQRT3_LO * E_LO / 2
MANTEL_LO = S * R_LO / 2 + S * S / 16
assert q_LO > D('0.46')
assert U_LO > 5 * p_HI
assert C_LO > 5 * p_HI
assert E_LO > CAP_HI + D('0.0017')
assert PROJECTED_LO > D('1.00149')
assert MANTEL_LO > D('0.000857')
print('PASS phase-star rhombic gap 0.0018 arithmetic')
print('sigma_safe=', S)
print('dominant_orbit_mass_lower=', W_LO)
print('orbit_deficit_upper=', d_HI)
print('sqrt_deficit_upper=', z_HI)
print('center_leaf_denominator_lower=', q_LO)
print('center_large_leaf_missing_upper=', m_HI)
print('pruning_threshold_upper=', p_HI)
print('center_mass_lower=', C_LO)
print('large_leaf_mass_lower=', U_LO)
print('large_leaf_common_neighbor_margin=', U_LO - 5 * p_HI)
print('raw_center_leaf_sum_lower=', RAW_SUM_LO)
print('opposite_corner_degree_sum_lower=', E_LO)
print('2/sqrt3_upper=', CAP_HI)
print('degree_sum_margin_lower=', E_LO - CAP_HI)
print('projected_diameter_coefficient_lower=', PROJECTED_LO)
print('projected_margin_lower=', PROJECTED_LO - D(1))
print('Mantel_deficit_coefficient_lower=', MANTEL_LO)
