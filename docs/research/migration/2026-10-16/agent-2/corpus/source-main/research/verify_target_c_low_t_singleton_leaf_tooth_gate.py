#!/usr/bin/env python3
"""Outward arithmetic regression for the low-t singleton leaf-tooth gate."""
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406')
SQRT3 = D(3).sqrt()
DELTA2 = PI / (D(2) * SQRT3)
R = DELTA2.sqrt()
C0 = D(2) * R + D('0.00042')
TSTAR = D(4) / D(9) * (PI + R) + D('0.0013751')
LSTAR = TSTAR + D('0.00084')

def A0(t):
    return D(9) * t / D(4) - PI - C0 / D(2)

def G(t):
    direct = LSTAR - D(8) * A0(t) - D(4) * t + D(2) * PI
    expanded = LSTAR - D(22) * t + D(10) * PI + D(4) * C0
    assert abs(direct - expanded) < D('1e-70')
    return direct

xcap = A0(TSTAR)
gstar = G(TSTAR)
root = (LSTAR + D(10) * PI + D(4) * C0) / D(22)
a_floor = gstar / D(104)
uniform = gstar / D(105)
three_way = gstar / D(113)
qcap = D(2) * TSTAR - PI
assert D('0.0028839749') < xcap < D('0.0028839751')
assert D('0.7982875') < gstar < D('0.7982877')
assert D('0.0076758') < a_floor < D('0.0076760')
assert D('0.0076027') < uniform < D('0.0076030')
assert D('0.0070643') < three_way < D('0.0070646')
assert D('0.5001846') < qcap < D('0.5001847')
assert D('1.857') < root < D('1.858')
assert G(D('1.85')) > 0
assert G(D('1.8585')) < 0
# Joint bad-incidence ledger: p5 + (5*N6 + X) = Q + 4*N6 <= Q+4X.
# Extraction constants: at most four leaf-side assignments per face, then Delta<=12.
assert D(4) * D(13) == D(52)
assert D(2) * D(52) == D(104)
print('PASS low-t singleton leaf-tooth gate arithmetic')
print('Delta2=', DELTA2)
print('C0=', C0)
print('t_star=', TSTAR)
print('L_star=', LSTAR)
print('X_cap_at_tstar=', xcap)
print('Q_cap_at_tstar=', qcap)
print('G_at_tstar=', gstar)
print('A_leaf_floor_if_sigma_RF_small=', a_floor)
print('uniform_sigma_or_A_threshold=', uniform)
print('uniform_sigma_or_A_or_residual_threshold=', three_way)
print('positive_G_until_t=', root)
