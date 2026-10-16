#!/usr/bin/env python3
"""Arithmetic regression for the shallow outer-tooth four-currency reduction.

This is non-load-bearing arithmetic only.  The geometric proof is in
`target_c_shallow_outer_tooth_four_currency_2026-09-14.md`.
"""
from decimal import Decimal, getcontext

getcontext().prec = 90
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
SQ2 = D(2).sqrt()
SQ3 = D(3).sqrt()
SQ6 = D(6).sqrt()
DELTA2 = PI / (D(2) * SQ3)
RHO = DELTA2.sqrt()

# Hostile-audited committed atomic gap and its safe Section-171 propagation.
g = D('0.0021')
eps_t = D('0.0017279')
C146 = D(4) * (PI + RHO) / D(9)
t21 = C146 + eps_t
Cg = D(2) * RHO + g
R = D(9) * t21 / D(2) - D(2) * PI - Cg
# Algebraically R=(9/2)eps_t-g=0.00567555.  The explicit Decimal evaluation
# passes through a rounded division by nine, so compare outward rather than by ==.
assert abs(R - D('0.00567555')) < D('1e-80')

# epsilon = pi/12.  d_epsilon = 2(1-cos(pi/24)).
cos_pi_12 = (SQ6 + SQ2) / D(4)
cos_pi_24 = ((D(1) + cos_pi_12) / D(2)).sqrt()
d = D(2) * (D(1) - cos_pi_24)
assert D('0.01711027') < d < D('0.01711029')

A = D(3) + D(1) / d
F = D(2) * t21 - PI - A * R / D(2)
assert D('0.3265248') < F < D('0.3265249')

# The four left coefficients are 1, 2/3, 1, 1, so their sum is 11/3.
unweighted = D(3) * F / D(11)
assert D('0.0890522') < unweighted < D('0.0890523')

# Local degree-three multiplier ratio at epsilon=pi/12.
ratio = (SQ3 - D(1)) / D(2)
assert D('0.3660254') < ratio < D('0.3660255')

# Local degree-four hidden-pair distance cap 2 sin(5 pi/24).
cos_5pi_12 = (SQ6 - SQ2) / D(4)  # cos(75 degrees)
sin_5pi_24 = ((D(1) - cos_5pi_12) / D(2)).sqrt()
hcap = D(2) * sin_5pi_24
assert D('1.2175228') < hcap < D('1.2175230')

# Vanishing-detour consequence.
vanishing_rhs = D(2) * t21 - PI
vanishing_unweighted = D(3) * vanishing_rhs / D(11)
assert D('0.5008902') < vanishing_rhs < D('0.5008903')
assert D('0.1366064') < vanishing_unweighted < D('0.1366065')

# Check the low-t minimization direction used in OT.19.
# With 2 delta + kappa/2 <= R, substituting maximal delta gives
#   2 kappa - A delta >= -A R/2 + (2+A/4) kappa,
# whose kappa coefficient is positive.
assert D(2) + A / D(4) > 0

print('PASS shallow outer-tooth four-currency arithmetic')
print('Delta2 =', DELTA2)
print('rho =', RHO)
print('t21 =', t21)
print('R_g(t21) =', R)
print('d(pi/12) =', d)
print('F_g(t21,pi/12) =', F)
print('unweighted four-way coefficient =', unweighted)
print('degree-three ratio cap =', ratio)
print('degree-four hidden-pair distance cap =', hcap)
print('vanishing-detour weighted rhs =', vanishing_rhs)
print('vanishing-detour four-way coefficient =', vanishing_unweighted)
