#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 90
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
C0 = D(2) * Delta2.sqrt() + D('0.0050')


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
        assert n < 400


def m2(U: Decimal) -> Decimal:
    return (U + (D(8) * Delta2 - U * U).sqrt()) / D(2)


def m2_prime(U: Decimal) -> Decimal:
    return (D(1) - U / (D(8) * Delta2 - U * U).sqrt()) / D(2)


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def boundary(t: Decimal):
    delta = R(t) / D(2)
    U = C0
    M = m2(U)
    r = U - M
    S = pi - U - t / D(2) + M
    P = (delta + r * r) / (D(2) * (D(1) - delta))
    Z = S - P
    return F(Z) - delta, delta, S, P, Z, M, r


t_safe = D('1.84209')
t_fail = D('1.84210')

safe_margin, delta_safe, S_safe, P_safe, Z_safe, M0, r0 = boundary(t_safe)
fail_margin = boundary(t_fail)[0]

assert safe_margin > D('0.0000173')
assert fail_margin < D('-0.0000063')

root_lo = D('1.84209732935')
root_hi = D('1.84209732937')
assert boundary(root_lo)[0] > 0
assert boundary(root_hi)[0] < 0

# Conservative derivative bounds used to reduce the whole feasible triangle to
# kappa=0 and maximal detour.  On t<=1.84210 one has U<2.007, delta<0.049,
# r(U)<0.11, and -0.06<m2'(U)<0.
U_max = D('4.5') * t_fail - D(2) * pi
delta_max = R(t_fail) / D(2)
r_max = U_max - m2(U_max)
m2p_min = m2_prime(U_max)
m2p_at_C0 = m2_prime(C0)

assert U_max < D('2.007')
assert delta_max < D('0.049')
assert r_max < D('0.11')
assert m2p_min > D('-0.06')
assert m2p_at_C0 < 0

# S_delta<2.12.  Dropping the positive first term in P_delta gives
# P_delta > -2*r*(1-m2')/(1-delta), hence Z_delta<the bound below.
z_delta_bound = (
    D('2.12')
    + D(2) * D('0.11') * D('1.06') / (D(1) - D('0.049'))
)
F_prime_pi = D(1) - sqrt3 / D(2)
derivative_product = z_delta_bound * F_prime_pi

assert z_delta_bound < D('2.37')
assert F_prime_pi < D('0.134')
assert derivative_product < D('0.318') < D(1)

print('Delta2 =', Delta2)
print('C0 =', C0)
print('M0 =', M0)
print('residual orbit mass r0 =', r0)
print('t_safe =', t_safe)
print('delta_safe =', delta_safe)
print('S_safe =', S_safe)
print('P_safe =', P_safe)
print('Z_safe =', Z_safe)
print('H(t_safe) =', safe_margin)
print('H(t_fail) =', fail_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', boundary(root_lo)[0])
print('H(root_hi) =', boundary(root_hi)[0])
print('U_max =', U_max)
print('delta_max =', delta_max)
print('r_max =', r_max)
print("m2'(U_max) =", m2p_min)
print('Z_delta bound =', z_delta_bound)
print("F'(pi) =", F_prime_pi)
print('derivative product =', derivative_product)
print('PASS: complement rhombus-incidence floor t >= 1.84209')
