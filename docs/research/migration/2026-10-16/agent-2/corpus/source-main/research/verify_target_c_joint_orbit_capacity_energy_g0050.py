#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
g = D('0.0050')
C0 = D(2) * s2 + g
C146 = D(4) * (pi + s2) / D(9)
t_base = C146 + D('0.0023374')
t_safe = D('1.82515')


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


def L(a: Decimal) -> Decimal:
    return ((D(1) + sin_decimal(a)) / cos_decimal(a)).ln()


def a_from_mass(z: Decimal) -> Decimal:
    lo = D(0)
    hi = pi / D(6)
    target = z / D(6)
    for _ in range(360):
        mid = (lo + hi) / D(2)
        if L(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / D(2)


def Phi(z: Decimal) -> Decimal:
    return z - D(6) * a_from_mass(z)


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def K_boundary(t: Decimal) -> Decimal:
    # Worst feasible endpoint: kappa=0, delta=R(t)/2, U=C0.
    return pi + R(t) / D(2) - t - D(2) * C0 + D(8) * Delta2 / C0


def H_boundary(t: Decimal) -> Decimal:
    return Phi(K_boundary(t)) - R(t) / D(2)


# The independently audited g=0.0050 Section-171 endpoint is excluded strongly.
expected_R_base = D('0.0055183')
assert abs(R(t_base) - expected_R_base) < D('1e-95')
assert H_boundary(t_base) > D('0.00735')

# Safe strengthened floor and nearby sign change.
safe_margin = H_boundary(t_safe)
assert safe_margin > D('0.000025')
assert H_boundary(D('1.82516')) > D('0.000003')
assert H_boundary(D('1.82517')) < D('-0.000019')

# Tight root bracket, retained only as a regression target.
root_lo = D('1.82516142463113334')
root_hi = D('1.82516142463113335')
assert H_boundary(root_lo) > 0
assert H_boundary(root_hi) < 0

# The dual optimizer remains in the interior K < 3 log 3.
assert K_boundary(t_safe) < D(3) * D(3).ln()

# Positivity of K on the excluded region.
U_zero = D('4.5') * t_safe - D(2) * pi
K_min = pi - t_safe - D(2) * U_zero + D(8) * Delta2 / U_zero
assert K_min > D('1.23')

# Delta monotonicity. The stronger C0 only improves the derivative bound relative
# to the symbolic proof: dK/ddelta < 9 and Phi'(K)<0.025 for K<1.33.
a_133 = a_from_mass(D('1.33'))
Phi_prime_133 = D(1) - cos_decimal(a_133)
dK_ddelta_max = D(5) + D(16) * Delta2 / (C0 * C0)
assert dK_ddelta_max < D(9)
assert Phi_prime_133 < D('0.025')
assert Phi_prime_133 * dK_ddelta_max < D('0.217') < D(1)

# Kappa monotonicity and one-variable monotonicity.
dK_dkappa_at_C0 = D(4) * Delta2 / (C0 * C0)
assert dK_dkappa_at_C0 > 0
assert D('1.25') * Phi_prime_133 < D('0.04') < D('2.25')

print('Delta2 =', Delta2)
print('g =', g)
print('C0 =', C0)
print('C146 =', C146)
print('t_base =', t_base)
print('H_joint(t_base) =', H_boundary(t_base))
print('t_safe =', t_safe)
print('K_boundary(t_safe) =', K_boundary(t_safe))
print('R(t_safe)/2 =', R(t_safe) / D(2))
print('Phi(K_boundary(t_safe)) =', Phi(K_boundary(t_safe)))
print('H_joint(t_safe) =', safe_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', H_boundary(root_lo))
print('H(root_hi) =', H_boundary(root_hi))
print('Phi_prime(1.33) =', Phi_prime_133)
print('dK/ddelta max =', dK_ddelta_max)
print('derivative product =', Phi_prime_133 * dK_ddelta_max)
print('PASS: g=0.0050 joint dominant-orbit floor t >= 1.82515')
