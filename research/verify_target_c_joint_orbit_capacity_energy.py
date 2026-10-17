#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C0 = D(2) * s2 + D('0.00042')
C146 = D(4) * (pi + s2) / D(9)
t42 = C146 + D('0.0013751')
t_safe = D('1.82434')


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
    # log(sec(a)+tan(a)) = log((1+sin(a))/cos(a))
    return ((D(1) + sin_decimal(a)) / cos_decimal(a)).ln()


def a_from_mass(z: Decimal) -> Decimal:
    # Solve 6 L(a)=z on [0,pi/6] by monotone bisection.
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
    # kappa=0, delta=R(t)/2, U=C0
    return pi + R(t) / D(2) - t - D(2) * C0 + D(8) * Delta2 / C0


def H_boundary(t: Decimal) -> Decimal:
    return Phi(K_boundary(t)) - R(t) / D(2)


# The old AG42 endpoint is excluded with substantial margin.
assert H_boundary(t42) > D('0.00768')

# Safe new round floor.
safe_margin = H_boundary(t_safe)
assert safe_margin > D('0.0000196')

# Tight scalar root bracket, retained as regression only.
root_lo = D('1.82434886920262333')
root_hi = D('1.82434886920262334')
assert H_boundary(root_lo) > 0
assert H_boundary(root_hi) < 0

# The dual optimizer remains in the interior K<3 log 3.
assert K_boundary(t_safe) < D(3) * D(3).ln()

# Positivity of K throughout the excluded region: K is minimized at
# delta=kappa=0 and the largest t under consideration.
U_zero = D('4.5') * t_safe - D(2) * pi
K_min = pi - t_safe - D(2) * U_zero + D(8) * Delta2 / U_zero
assert K_min > D('1.23')

# Delta monotonicity: dK/ddelta <9 and Phi'(K)<0.025 for K<1.33.
a_133 = a_from_mass(D('1.33'))
Phi_prime_133 = D(1) - cos_decimal(a_133)
dK_ddelta_max = D(5) + D(16) * Delta2 / (C0 * C0)
assert dK_ddelta_max < D(9)
assert Phi_prime_133 < D('0.025')
assert Phi_prime_133 * dK_ddelta_max < D('0.225') < D(1)

# Kappa monotonicity is exact and positive.
dK_dkappa_at_C0 = D(4) * Delta2 / (C0 * C0)
assert dK_dkappa_at_C0 > 0

# H_boundary is decreasing: K_boundary'=5/4 and Phi'<0.025.
assert D('1.25') * Phi_prime_133 < D('0.04') < D('2.25')

print('Delta2 =', Delta2)
print('C0 =', C0)
print('t42 =', t42)
print('H_joint(t42) =', H_boundary(t42))
print('t_safe =', t_safe)
print('K_boundary(t_safe) =', K_boundary(t_safe))
print('R(t_safe)/2 =', R(t_safe) / D(2))
print('Phi(K_boundary(t_safe)) =', Phi(K_boundary(t_safe)))
print('H_joint(t_safe) =', safe_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', H_boundary(root_lo))
print('H(root_hi) =', H_boundary(root_hi))
print('K_min on excluded rectangle =', K_min)
print('Phi_prime(1.33) =', Phi_prime_133)
print('dK/ddelta max =', dK_ddelta_max)
print('derivative product =', Phi_prime_133 * dK_ddelta_max)
print('PASS: joint dominant-orbit floor t >= 1.82434')
