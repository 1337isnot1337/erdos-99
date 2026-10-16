#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
D = Decimal

pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
grid_gap = D('0.00042')
C0 = D(2) * s2 + grid_gap
C146 = D(4) * (pi + s2) / D(9)
t42 = C146 + D('0.0013751')
t_safe = D('1.82428')


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


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def k_boundary(t: Decimal) -> Decimal:
    # Weakest feasible point: kappa=0, delta=R(t)/2, U=C0.
    return pi - t - D(2) * C0 + D(8) * Delta2 / C0


def H_boundary(t: Decimal) -> Decimal:
    return F(k_boundary(t)) - R(t) / D(2)


# Old AG42 endpoint is excluded with a large margin.
old_margin = H_boundary(t42)
assert old_margin > D('0.0077')

# The advertised safe round floor remains strictly on the excluded side.
safe_margin = H_boundary(t_safe)
assert safe_margin > D('0.0000028')

# The scalar zero is tightly bracketed above the advertised safe value.
root_lo = D('1.82428123517075213')
root_hi = D('1.82428123517075215')
assert H_boundary(root_lo) > 0
assert H_boundary(root_hi) < 0

# Monotonicity in delta: throughout t>=t42 and U>=C0,
# k < pi-t42 and dk/ddelta < 8.  This numerical cap certifies
# F'(k) * dk/ddelta < 1, hence d(F(k)-delta)/ddelta < 0.
k_max = pi - t42
Fprime_max = D(1) - cos_decimal(k_max / D(6))
dk_ddelta_max = D(4) + D(16) * Delta2 / (C0 * C0)
assert dk_ddelta_max < D(8)
assert Fprime_max < D('0.024129')
assert Fprime_max * dk_ddelta_max < D('0.193')

# Monotonicity in kappa is exact and positive: 4 Delta2/U^2 > 0.
dk_dkappa_at_C0 = D(4) * Delta2 / (C0 * C0)
assert dk_dkappa_at_C0 > 0

# Bathtub argument stays in the first Voronoi cell range.
assert 0 < k_boundary(t42) < pi
assert k_boundary(t_safe) < pi

print('Delta2 =', Delta2)
print('s2 =', s2)
print('C0 =', C0)
print('t42 =', t42)
print('H(t42) =', old_margin)
print('t_safe =', t_safe)
print('k_boundary(t_safe) =', k_boundary(t_safe))
print('R(t_safe)/2 =', R(t_safe) / D(2))
print('F(k_boundary(t_safe)) =', F(k_boundary(t_safe)))
print('H(t_safe) =', safe_margin)
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', H_boundary(root_lo))
print('H(root_hi) =', H_boundary(root_hi))
print('Fprime_max =', Fprime_max)
print('dk_ddelta_max =', dk_ddelta_max)
print('derivative product =', Fprime_max * dk_ddelta_max)
print('PASS: dominant-orbit outer-energy floor t >= 1.82428')
