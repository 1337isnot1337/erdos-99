#!/usr/bin/env python3
"""Arithmetic/bookkeeping regression for loaded-slack source externalization."""
from decimal import Decimal as D, getcontext

getcontext().prec = 90
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406')
SQRT3 = D(3).sqrt()
DELTA2 = PI / (D(2) * SQRT3)
S = DELTA2.sqrt()
G = D('0.002123')
C = D(2) * S + G
C146 = D(4) * (PI + S) / D(9)
T23 = C146 + D('0.0017327')
ETA = D('0.06')


def A(t):
    return D(11) * PI + D(6) * C - D(24) * t


def R(t):
    return D('4.5') * t - D(2) * PI - C


def B(t, eta):
    return A(t) + (D(9) - D(1) / eta) * R(t) / D(2)


# Normalized algebra behind LS.2.
t, kappa, delta = D('1.83'), D('0.004'), D('0.001')
xcap = D(9) * t / D(4) - PI - C / D(2) - delta - kappa / D(4)
rhs = D(3) * t + D(3) * kappa - PI - delta - D(2) * delta - D(12) * xcap
closed = D(11) * PI + D(6) * C - D(24) * t + D(9) * delta + D(6) * kappa
assert abs(rhs - closed) < D('1e-80')

# Deficient-degree finite payment: if J >= B1+B2-C2 and C2 <= B2,
# then 2J+C2 >= 2B1+B2=s_B. Exhaust a small integer box.
for b1 in range(8):
    for b2 in range(8):
        for c2 in range(b2 + 1):
            j = b1 + b2 - c2
            assert D(2) * j + c2 >= D(2) * b1 + b2

A23 = A(T23)
R23 = R(T23)
B23 = B(T23, ETA)
assert D('2.27') < A23 < D('2.30')
assert D('0.0056') < R23 < D('0.0058')
assert D('2.24') < B23 < D('2.28')
assert A23 / D(7) > D('0.32')
assert B23 / D(10) > D('0.22')

# For eta<1/9, minimizing (9-1/eta)delta+6kappa under
# 2delta+kappa/2 <= R occurs at delta=R/2, kappa=0.
a = D(9) - D(1) / ETA
assert a < 0
# objective per unit of topology budget: delta costs a/2 per R,
# kappa costs 12 per R, so the negative delta endpoint is minimal.
assert a / D(2) < D(12)



def loaded_cap(t, delta=D(0)):
    return D('2.5') * t - PI - delta - S - G / D(2)


def contact_sum_floor(t, eta):
    # LS.30 after eliminating L_flat and minimizing topology.
    base = D(13) * PI + D(7) * C - D(29) * t
    coeff = D(11) - D(1) / eta
    return base + coeff * R(t) / D(2)


# LS.26 algebra before the topology minimization.
tx, dx, kx = D('1.83'), D('0.001'), D('0.004')
ls6 = A(tx) + (D(9) - D(1) / ETA) * dx + D(6) * kx
subtract_loaded = D(2) * loaded_cap(tx, dx)
ls26_direct = ls6 - subtract_loaded
ls26_closed = (
    D(13) * PI + D(7) * C - D(29) * tx
    + (D(11) - D(1) / ETA) * dx + D(6) * kx
)
assert abs(ls26_direct - ls26_closed) < D('1e-80')

C23 = contact_sum_floor(T23, ETA)
assert D('1.35') < C23 < D('1.36')
assert D('0.16946') < C23 / D(8) < D('0.16948')

# Historical hostile-audited g=.0021 comparison.
G21 = D('0.0021')
C21 = D(2) * S + G21
T21 = C146 + D('0.0017279')
R21 = D('4.5') * T21 - D(2) * PI - C21
base21 = D(13) * PI + D(7) * C21 - D(29) * T21
contact21 = base21 + (D(11) - D(1) / ETA) * R21 / D(2)
assert D('0.16945') < contact21 / D(8) < D('0.16947')

print('sqrt(Delta2) =', S)
print('C_23 =', C)
print('t_23 =', T23)
print('A_23 =', A23)
print('A_23/7 =', A23 / D(7))
print('R_23 =', R23)
print('delta_max =', R23 / D(2))
print('B_23(eta=.06) =', B23)
print('B_23/10 =', B23 / D(10))
print('all-contact burden g=.002123 =', C23)
print('all-contact union floor g=.002123 =', C23 / D(8))
print('historical all-contact union floor g=.0021 =', contact21 / D(8))
print('A positive through t <', (D(11) * PI + D(6) * C) / D(24))
print('PASS loaded-slack source externalization regression')
