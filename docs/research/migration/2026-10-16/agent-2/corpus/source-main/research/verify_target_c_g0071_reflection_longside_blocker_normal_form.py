#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
C71 = D(2) * Delta2.sqrt() + D('0.0071')
beta = pi / D(6) - D('0.0001')
t_floor = D('1.84323')


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    n = 1
    while True:
        term = -term * x * x / D((2 * n - 1) * (2 * n))
        old = total
        total += term
        if total == old:
            return total
        n += 1
        assert n < 300


c = cos_decimal(beta)
A = D(1) / (D(1) - c) + D(1) / (D(2) * c)


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C71


def loss(delta: Decimal) -> Decimal:
    return A * delta + (delta * (delta + D(2) * pi)).sqrt()


def loss_prime(delta: Decimal) -> Decimal:
    return A + (delta + pi) / (delta * (delta + D(2) * pi)).sqrt()


def G(t: Decimal) -> Decimal:
    delta = R(t) / D(2)
    return pi + delta - t - loss(delta)


R0 = R(t_floor)
delta0 = R0 / D(2)
G0 = G(t_floor)
blocker = G0 / D(2)
long_side = blocker - delta0
physical_tails = blocker / D(4)

assert R0 > 0
assert delta0 < D('0.05')
assert G0 > D('0.3858186')
assert blocker > D('0.1929093')
assert long_side > D('0.1430972')
assert physical_tails > D('0.0482273')

# After maximizing kappa, the bound decreases in delta once loss'(delta)>5.
assert loss_prime(delta0) > D(5)
assert D(5) - loss_prime(delta0) < 0
# Boundary G'(t)=5/4-(9/4) loss'(delta).
assert D('1.25') - D('2.25') * loss_prime(delta0) < 0

root_lo = D('1.8569406450521027102')
root_hi = D('1.8569406450521027103')
assert G(root_lo) > 0
assert G(root_hi) < 0
assert G(D('1.8569')) > 0
assert G(D('1.8585')) < 0

print('Delta2 =', Delta2)
print('C71 =', C71)
print('beta =', beta)
print('cos(beta) =', c)
print('linear loss coefficient =', A)
print('R71(t_floor) =', R0)
print('delta0 =', delta0)
print('G0 =', G0)
print('blocker alternative =', blocker)
print('long-side alternative =', long_side)
print('distinct physical tail floor =', physical_tails)
print("loss'(delta0) =", loss_prime(delta0))
print('G(1.8569) =', G(D('1.8569')))
print('G(1.8585) =', G(D('1.8585')))
print('root bracket =', root_lo, root_hi)
print('root signs =', G(root_lo), G(root_hi))
print('PASS: g=0.0071 reflection/long-side/blocker normal form')
