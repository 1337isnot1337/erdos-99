#!/usr/bin/env python3
"""Non-load-bearing regression for flat-center KKT stress leakage."""
from decimal import Decimal, getcontext
from math import cos, pi, sin

getcontext().prec = 60
D = Decimal

# Local coefficients must vanish at the flat endpoint and give a positive
# chain-comparability denominator on the range used by the proof.
for eps in (1e-7, 1e-5, 1e-3, 1e-2, 5e-2, 1e-1):
    lam = sin(eps) / sin(pi / 3 - eps)
    mismatch = 1 - cos(eps) + lam
    kappa = cos(eps) - lam
    assert lam > 0
    assert mismatch > 0
    assert kappa > 0
    assert lam / kappa < 2 * eps
    assert mismatch < 2 * eps

# A representative degree-four equilibrium.  The three complementary angular
# gaps are pi/3 + e_i with e_1+e_2+e_3=delta.
eps = 0.04
delta = 0.03
A = pi - delta
e1, e2, e3 = 0.008, 0.009, delta - 0.008 - 0.009
assert e3 > 0
phi1 = A + pi / 3 + e1
phi2 = phi1 + pi / 3 + e2
assert abs((2 * pi - phi2) - (pi / 3 + e3)) < 1e-12
# Choose positive exterior weights and solve y- then x-equilibrium for the face
# weights.  The solution should be positive and obey the theorem bounds.
g1, g2 = 0.2, 0.13
alpha_l = -(g1 * sin(phi1) + g2 * sin(phi2)) / sin(A)
alpha_r = -(alpha_l * cos(A) + g1 * cos(phi1) + g2 * cos(phi2))
assert alpha_l > 0 and alpha_r > 0
Gamma = g1 + g2
lam = sin(eps) / sin(pi / 3 - eps)
mismatch = 1 - cos(eps) + lam
assert Gamma <= lam * alpha_l + 1e-12
assert abs(alpha_r - alpha_l) <= mismatch * alpha_l + 1e-12

# Low-t binary coefficients.
P42 = D('0.4944166723690961')
P18585 = D('0.4003882673177079')
assert D('0.2472083361') < P42 / 2 < D('0.2472083363')
assert D('0.2001941335') < P18585 / 2 < D('0.2001941338')

print('PASS flat-center KKT stress leakage regression')
print('lambda(0.01)=', sin(0.01) / sin(pi / 3 - 0.01))
print('kappa(0.01)=', cos(0.01) - sin(0.01) / sin(pi / 3 - 0.01))
print('binary_floor_t42=', P42 / 2)
print('binary_floor_t_le_1.8585=', P18585 / 2)
