#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C0 = D(2) * s2 + D('0.00042')
C146 = D(4) * (pi + s2) / D(9)
t42 = C146 + D('0.0013751')
t_safe = D('1.82806')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = x
    for n in range(1, 100):
        term = -term * x * x / D((2 * n) * (2 * n + 1))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('sin series did not converge')


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    for n in range(1, 100):
        term = -term * x * x / D((2 * n - 1) * (2 * n))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('cos series did not converge')


def L(a: Decimal) -> Decimal:
    # log(sec a + tan a)
    return ((D(1) + sin_decimal(a)) / cos_decimal(a)).ln()


def phi_inverse(delta: Decimal) -> Decimal:
    # Phi(z)=delta, with z=6 L(a), Phi=6(L(a)-a).
    lo = D(0)
    hi = pi / D(6)
    target = delta / D(6)
    for _ in range(170):
        mid = (lo + hi) / D(2)
        if L(mid) - mid < target:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / D(2)
    return D(6) * L(a)


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def J(p: Decimal) -> Decimal:
    return D(2) * p - D(6) * sin_decimal(p / D(3))


def R(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C0


def boundary_values(t: Decimal):
    delta = R(t) / D(2)
    z = pi - t - D(2) * C0 + D(8) * Delta2 / C0
    qinv = phi_inverse(delta)
    ncomp = C0 + t / D(2) - D(4) * Delta2 / C0
    p = pi - qinv - ncomp
    e_dom = F(z)
    e_comp = J(p)
    margin = e_dom + e_comp - delta
    return delta, z, e_dom, qinv, ncomp, p, e_comp, margin


# Safe theorem endpoint.
delta, z, e_dom, qinv, ncomp, p, e_comp, margin = boundary_values(t_safe)
assert margin > D('0.0000295')
assert D('0.615') < p < D(1)
assert qinv < D('1.62')
assert z < D('1.33')

# Root regression.  The safe theorem stays comfortably below this crossing.
assert boundary_values(D('1.8280659'))[-1] > D('0.00000007')
assert boundary_values(D('1.828066'))[-1] < 0

# Uniform derivative bounds used to reduce the feasible triangle to its
# maximum-detour, kappa=0 endpoint.
Fprime_133 = D(1) - cos_decimal(D('1.33') / D(6))
# Phi'(q)=1-sech(q/6)=1-cos(a), where q=6L(a).
a_162 = D('1.62') / D(6)
# sech(q/6)=cos(gd(q/6)); gd(x)=a with L(a)=x.
lo = D(0)
hi = pi / D(6)
for _ in range(170):
    mid = (lo + hi) / D(2)
    if L(mid) < a_162:
        lo = mid
    else:
        hi = mid
phase_a = (lo + hi) / D(2)
Phiprime_162 = D(1) - cos_decimal(phase_a)
Jprime_061 = D(2) - D(2) * cos_decimal(D('0.61') / D(3))

dz_ddelta_max = D(4) + D(16) * Delta2 / (C0 * C0)
minus_dN_ddelta_max = D(2) * (D(1) + D(4) * Delta2 / (C0 * C0))

assert Fprime_133 < D('0.025')
assert dz_ddelta_max < D(8)
assert Phiprime_162 < D('0.04')
assert minus_dN_ddelta_max < D(4)
assert Jprime_061 > D('0.041')

# dp/ddelta = -1/Phi'(Q) - dN/ddelta < -25 + 4 < -21.
assert D(1) / Phiprime_162 > D(25)
# Total margin derivative is strictly negative with large slack.
coarse_margin_derivative_upper = (
    D('0.025') * D(8)
    - D(21) * D('0.041')
    - D(1)
)
assert coarse_margin_derivative_upper < D('-1.6')

# Sector Jensen regime: the fallback one-sector cost at pi/6 dominates
# the three-sector bound for every p<=1.
sector_cap_cost = pi / D(3) - D(1)
J_one = J(D(1))
assert sector_cap_cost > D('0.047')
assert J_one < sector_cap_cost

print('Delta2 =', Delta2)
print('C0 =', C0)
print('t42 =', t42)
print('t_safe =', t_safe)
print('delta0 =', delta)
print('z0 =', z)
print('F(z0) =', e_dom)
print('Phi^{-1}(delta0) =', qinv)
print('Ncomp upper =', ncomp)
print('retained complement pair floor p0 =', p)
print('J(p0) =', e_comp)
print('margin =', margin)
print('margin at 1.8280659 =', boundary_values(D('1.8280659'))[-1])
print('margin at 1.828066 =', boundary_values(D('1.828066'))[-1])
print('Fprime(1.33) =', Fprime_133)
print('Phiprime(1.62) =', Phiprime_162)
print('Jprime(0.61) =', Jprime_061)
print('coarse dmargin/ddelta upper =', coarse_margin_derivative_upper)
print('sector cap cost =', sector_cap_cost)
print('J(1) =', J_one)
print('PASS: complement outer-train bracing floor t >= 1.82806')
