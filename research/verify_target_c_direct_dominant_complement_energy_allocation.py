#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
g = D('0.0050')
C0 = D(2) * s2 + g

t_safe = D('1.83236')
t_fail = D('1.83237')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = term
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
        assert n < 300


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
        assert n < 300


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def F_prime(z: Decimal) -> Decimal:
    return D(1) - cos_decimal(z / D(6))


def J(p: Decimal) -> Decimal:
    return D(2) * p - D(6) * sin_decimal(p / D(3))


def J_prime(p: Decimal) -> Decimal:
    return D(2) - D(2) * cos_decimal(p / D(3))


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def W_boundary(t: Decimal) -> Decimal:
    delta = R(t) / D(2)
    return pi - delta - C0 - t / D(2) + D(4) * Delta2 / C0


def allocation(W: Decimal):
    # Minimize F(z)+J(p) with z+p=W.  The derivative condition is
    # F'(W-p)=J'(p); its left-minus-right side is strictly decreasing in p.
    lo = D(0)
    hi = W
    for _ in range(180):
        p = (lo + hi) / D(2)
        derivative_gap = F_prime(W - p) - J_prime(p)
        if derivative_gap > 0:
            lo = p
        else:
            hi = p
    p = (lo + hi) / D(2)
    z = W - p
    return F(z) + J(p), z, p


def H(t: Decimal):
    W = W_boundary(t)
    energy, z, p = allocation(W)
    return energy - R(t) / D(2), energy, z, p, W


safe_margin, safe_energy, safe_z, safe_p, safe_W = H(t_safe)
fail_margin, _, _, _, _ = H(t_fail)

assert safe_margin > D('0.0000179')
assert fail_margin < D('-0.0000055')
assert D(0) < safe_p < D(1)
assert D(0) < safe_z < safe_W < pi
assert abs(F_prime(safe_z) - J_prime(safe_p)) < D('1e-50')

# Tight scalar-root bracket.
root_lo = D('1.83236762774382989752')
root_hi = D('1.83236762774382989753')
assert H(root_lo)[0] > 0
assert H(root_hi)[0] < 0

# Feasible-triangle monotonicity in delta.  For U>=C0,
# dW/ddelta <= 1+8 Delta2/C0^2.  The allocation marginal is at most
# F'(W)<=F'(pi)=1-sqrt(3)/2, so d(E(W)-delta)/ddelta<0.
dW_ddelta_max = D(1) + D(8) * Delta2 / (C0 * C0)
F_prime_pi = D(1) - sqrt3 / D(2)
derivative_product = dW_ddelta_max * F_prime_pi
assert dW_ddelta_max < D('2.99')
assert derivative_product < D('0.401') < D(1)

# Kappa monotonicity is exact: dW/dkappa=2 Delta2/U^2>0.
dW_dkappa_at_C0 = D(2) * Delta2 / (C0 * C0)
assert dW_dkappa_at_C0 > 0

print('Delta2 =', Delta2)
print('g =', g)
print('C0 =', C0)
print('t_safe =', t_safe)
print('W(t_safe) =', safe_W)
print('allocation z =', safe_z)
print('allocation p =', safe_p)
print('allocation energy =', safe_energy)
print('delta(t_safe) =', R(t_safe) / D(2))
print('H(t_safe) =', safe_margin)
print('H(t_fail) =', fail_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', H(root_lo)[0])
print('H(root_hi) =', H(root_hi)[0])
print('dW/ddelta max =', dW_ddelta_max)
print("F'(pi) =", F_prime_pi)
print('derivative product =', derivative_product)
print('PASS: direct dominant/complement allocation floor t >= 1.83236')
