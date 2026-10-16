#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
C71 = D(2) * Delta2.sqrt() + D('0.0071')


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
        assert n < 500


def m2(U: Decimal) -> Decimal:
    return (U + (D(8) * Delta2 - U * U).sqrt()) / D(2)


def m2_prime(U: Decimal) -> Decimal:
    return (D(1) - U / (D(8) * Delta2 - U * U).sqrt()) / D(2)


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C71


M71 = m2(C71)
r71 = C71 - M71


def boundary(t: Decimal):
    delta = R(t) / D(2)
    S = pi - C71 - t / D(2) + M71

    def equation(z: Decimal) -> Decimal:
        return z + (delta - F(z) + r71 * r71) / (D(2) * (D(1) - delta)) - S

    lo = D(0)
    hi = pi
    for _ in range(360):
        mid = (lo + hi) / D(2)
        if equation(mid) < 0:
            lo = mid
        else:
            hi = mid
    z = (lo + hi) / D(2)
    p = S - z
    return F(z) - delta, delta, S, z, p, equation(z)


safe = D('1.84323')
fail = D('1.84324')
safe_margin, delta_safe, S_safe, z_safe, p_safe, residual = boundary(safe)
fail_margin = boundary(fail)[0]

assert safe_margin > D('0.00001267')
assert fail_margin < D('-0.00001100')
assert abs(residual) < D('1e-90')
assert D(0) < p_safe < D('0.0000200')

root_lo = D('1.84323535293446450')
root_hi = D('1.84323535293446451')
assert boundary(root_lo)[0] > 0
assert boundary(root_hi)[0] < 0

# Recheck the parent's conservative derivative box on the new interval.
top = fail
U_max = D('4.5') * top - D(2) * pi
# This is the largest feasible U when delta=kappa=0.  The proof only needs it below 2.007.
delta_max = R(top) / D(2)
r_max = U_max - m2(U_max)
m2p_min = m2_prime(U_max)
F_prime_pi = D(1) - sqrt3 / D(2)

assert U_max < D('2.007')
assert delta_max < D('0.051')
assert r_max < D('0.11')
assert m2p_min > D('-0.06')
assert m2_prime(C71) < 0
assert F_prime_pi < D('0.134')

print('Delta2 =', Delta2)
print('C71 =', C71)
print('M71 =', M71)
print('r71 =', r71)
print('safe t =', safe)
print('delta_safe =', delta_safe)
print('S_safe =', S_safe)
print('z_safe =', z_safe)
print('p_safe =', p_safe)
print('H(safe) =', safe_margin)
print('H(fail) =', fail_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', boundary(root_lo)[0])
print('H(root_hi) =', boundary(root_hi)[0])
print('U_max =', U_max)
print('delta_max =', delta_max)
print('r_max =', r_max)
print("m2'(U_max) =", m2p_min)
print('PASS: g=0.0071 propagates to t >= 1.84323')
