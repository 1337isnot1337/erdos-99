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


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


M0 = m2(C0)
r0 = C0 - M0


def boundary(t: Decimal):
    delta = R(t) / D(2)
    S = pi - C0 - t / D(2) + M0

    def equation(z: Decimal) -> Decimal:
        return (
            z
            + (delta - F(z) + r0 * r0) / (D(2) * (D(1) - delta))
            - S
        )

    lo = D(0)
    hi = pi
    for _ in range(300):
        mid = (lo + hi) / D(2)
        if equation(mid) < 0:
            lo = mid
        else:
            hi = mid
    z = (lo + hi) / D(2)
    p = S - z
    return F(z) - delta, delta, S, z, p, equation(z)


safe = D('1.84283')
fail = D('1.84284')
safe_margin, delta_safe, S_safe, z_safe, p_safe, residual = boundary(safe)
fail_margin = boundary(fail)[0]

assert safe_margin > D('0.0000190')
assert fail_margin < D('-0.0000046')
assert abs(residual) < D('1e-80')
assert D(0) < p_safe < D('0.000004')

root_lo = D('1.84283805523')
root_hi = D('1.84283805525')
assert boundary(root_lo)[0] > 0
assert boundary(root_hi)[0] < 0

# Conservative implicit-derivative bounds used in the proof.
delta_max = R(fail) / D(2)
F_prime_pi = D(1) - sqrt3 / D(2)
Gz_min = D(1) - F_prime_pi / (D(2) * (D(1) - delta_max))
GU_max = D('0.11') * D('1.06') / (D(1) - D('0.05'))
z_delta_bound = (D('2.12') + D(2) * GU_max) / Gz_min
derivative_product = z_delta_bound * F_prime_pi

assert delta_max < D('0.05')
assert Gz_min > D('0.929')
assert GU_max < D('0.123')
assert z_delta_bound < D('2.55')
assert derivative_product < D('0.342') < D(1)

print('Delta2 =', Delta2)
print('C0 =', C0)
print('M0 =', M0)
print('r0 =', r0)
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
print('Gz_min =', Gz_min)
print('GU_max =', GU_max)
print('z_delta_bound =', z_delta_bound)
print('derivative product =', derivative_product)
print('PASS: energy-restored complement rhombus-incidence floor t >= 1.84283')
