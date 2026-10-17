#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C0 = Decimal(2) * s + g
C146 = Decimal(4) * (pi + s) / Decimal(9)
t42 = C146 + Decimal('0.0013751')


def bounds(t):
    phi_min = C0 / Decimal(2) - t / Decimal(4)
    qminusf_max = Decimal(9) * t / Decimal(4) - pi - C0 / Decimal(2)
    pent_min = pi + C0 - Decimal(5) * t / Decimal(2)
    loo_min = Decimal(3) * pi - Decimal(5) * t
    return phi_min, qminusf_max, pent_min, loo_min


phi, excess, pent, loo = bounds(t42)
assert phi > Decimal('0.49730064')
assert Decimal('0.00288397') < excess < Decimal('0.00288398')
assert pent > Decimal('0.49441667')
assert loo > Decimal('0.3203347')
assert excess / phi < Decimal('0.0058')

bar = Decimal('1.8585')
phi_b, excess_b, pent_b, loo_b = bounds(bar)
assert pent_b > Decimal('0.4003882')
assert loo_b > Decimal('0.1322779')

for t, kappa, delta in [
    (Decimal('1.83'), Decimal('0.01'), Decimal('0.002')),
    (Decimal('1.84'), Decimal('0'), Decimal('0.003')),
    (Decimal('1.8585'), Decimal('0.02'), Decimal('0.001')),
]:
    phi0 = C0 / Decimal(2) - t / Decimal(4) + kappa / Decimal(4)
    chi = Decimal(2) * t - pi - delta
    assert phi0 <= chi
    assert chi - phi0 == (
        Decimal(9) * t / Decimal(4)
        - pi
        - C0 / Decimal(2)
        - delta
        - kappa / Decimal(4)
    )
    assert Decimal(2) * phi0 - chi == (
        pi + C0 - Decimal(5) * t / Decimal(2) + delta + kappa / Decimal(2)
    )

print('Delta2 =', Delta2)
print('C0 =', C0)
print('C146 =', C146)
print('t42 =', t42)
print('at t42: f/D >=', phi)
print('at t42: (Q-f)/D <=', excess)
print('at t42: pentagons/D >=', pent)
print('at t42: non-pentagon fraction <=', excess / phi)
print('at t42: L_OO/D >=', loo)
print('at 1.8585: pentagons/D >=', pent_b)
print('at 1.8585: L_OO/D >=', loo_b)
print('PASS: low-t pentagon sea and outer-train floor')
