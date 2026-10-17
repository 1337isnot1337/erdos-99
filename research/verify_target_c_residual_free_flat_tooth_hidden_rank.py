#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C0 = D(2) * s2 + D('0.0050')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = x
    n = 1
    sign = -1
    while True:
        term = term * x * x / D((2 * n) * (2 * n + 1))
        old = total
        total = total + term if sign > 0 else total - term
        if total == old:
            return total
        sign *= -1
        n += 1


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    n = 1
    sign = -1
    while True:
        term = term * x * x / D((2 * n - 1) * (2 * n))
        old = total
        total = total + term if sign > 0 else total - term
        if total == old:
            return total
        sign *= -1
        n += 1


def L(a: Decimal) -> Decimal:
    return ((D(1) + sin_decimal(a)) / cos_decimal(a)).ln()


def psi(delta: Decimal) -> Decimal:
    # Phi(6L(a)) = 6(L(a)-a). Solve in a on [0,pi/6].
    lo = D(0)
    hi = pi / D(6)
    for _ in range(280):
        mid = (lo + hi) / D(2)
        if D(6) * (L(mid) - mid) < delta:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / D(2)
    return D(6) * L(a)


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def K0(t: Decimal) -> Decimal:
    return pi + R(t) / D(2) - t - D(2) * C0 + D(8) * Delta2 / C0


def nondominant_cap(t: Decimal) -> Decimal:
    return psi(R(t) / D(2)) - K0(t)


def pure_pentagon_floor(t: Decimal) -> Decimal:
    return pi + C0 - D('2.5') * t - nondominant_cap(t)


def hidden_rank_floor(t: Decimal) -> Decimal:
    p = pure_pentagon_floor(t)
    return D(7) * p / D(3) - D(4) * t + D(2) * pi


for t in map(D, ['1.82530', '1.82550', '1.82570', '1.825705', '1.82571']):
    print(
        't =', t,
        'nondominant cap =', nondominant_cap(t),
        'pure pentagon floor =', pure_pentagon_floor(t),
        'hidden rank floor =', hidden_rank_floor(t),
    )

assert pure_pentagon_floor(D('1.82570')) > D('0.43744312')
assert hidden_rank_floor(D('1.82570')) > D('0.0010859')
assert hidden_rank_floor(D('1.825705')) > 0
assert hidden_rank_floor(D('1.82571')) < 0

# Regression-only root bracket.
lo = D('1.82570')
hi = D('1.82571')
for _ in range(180):
    mid = (lo + hi) / D(2)
    if hidden_rank_floor(mid) > 0:
        lo = mid
    else:
        hi = mid

assert lo > D('1.8257050')
assert hi < D('1.8257051')

print('rank-zero bracket =', lo, hi)
print('PASS: residual-free flat-tooth hidden derivative rank')
