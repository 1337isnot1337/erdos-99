#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C50 = D(2) * s2 + D('0.0050')
t_safe = D('1.82890')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = x
    for n in range(1, 120):
        term = -term * x * x / D((2 * n) * (2 * n + 1))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('sin series did not converge')


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    for n in range(1, 120):
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
    for _ in range(210):
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


def R50(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C50


def boundary_values(t: Decimal):
    delta = R50(t) / D(2)
    z = pi - t - D(2) * C50 + D(8) * Delta2 / C50
    qinv = phi_inverse(delta)
    ncomp = C50 + t / D(2) - D(4) * Delta2 / C50
    p = pi - qinv - ncomp
    e_dom = F(z)
    e_comp = J(p)
    margin = e_dom + e_comp - delta
    return delta, z, e_dom, qinv, ncomp, p, e_comp, margin


# Advertised safe endpoint.
delta, z, e_dom, qinv, ncomp, p, e_comp, margin = boundary_values(t_safe)
assert margin > D('0.0000622')
assert D('0.617') < p < D(1)
assert qinv < D('1.600')
assert z < D('1.30')

# An even tighter value still has positive margin, but is not claimed.
assert boundary_values(D('1.82891'))[-1] > D('0.0000118')

# Root bracket.
root_lo = D('1.8289123539')
root_hi = D('1.8289123540')
assert boundary_values(root_lo)[-1] > 0
assert boundary_values(root_hi)[-1] < 0

# Uniform derivative regime. Stronger C50 makes the U-denominator bounds at
# least as good as in the audited g=0.00042 complement theorem.
Fprime_130 = D(1) - cos_decimal(D('1.30') / D(6))
# Phi'(q)=1-sech(q/6)=1-cos(a), q=6L(a).
q_cap = D('1.61')
lo = D(0)
hi = pi / D(6)
for _ in range(210):
    mid = (lo + hi) / D(2)
    if D(6) * L(mid) < q_cap:
        lo = mid
    else:
        hi = mid
phase_a = (lo + hi) / D(2)
Phiprime_161 = D(1) - cos_decimal(phase_a)
Jprime_061 = D(2) - D(2) * cos_decimal(D('0.61') / D(3))

dz_ddelta_max = D(4) + D(16) * Delta2 / (C50 * C50)
minus_dN_ddelta_max = D(2) * (D(1) + D(4) * Delta2 / (C50 * C50))

assert Fprime_130 < D('0.024')
assert dz_ddelta_max < D(8)
assert Phiprime_161 < D('0.04')
assert D(1) / Phiprime_161 > D(25)
assert minus_dN_ddelta_max < D(4)
assert Jprime_061 > D('0.041')

# Coarse derivative upper bound for dM/ddelta.
coarse_margin_derivative_upper = (
    D('0.024') * D(8)
    - D(21) * D('0.041')
    - D(1)
)
assert coarse_margin_derivative_upper < D('-1.66')

# Three-sector Jensen fallback remains valid for all p<=1.
sector_cap_cost = pi / D(3) - D(1)
assert J(D(1)) < sector_cap_cost

print('Delta2 =', Delta2)
print('C50 =', C50)
print('t_safe =', t_safe)
print('delta50 =', delta)
print('z50 =', z)
print('F(z50) =', e_dom)
print('Phi^{-1}(delta50) =', qinv)
print('Ncomp upper =', ncomp)
print('retained complement pair floor p50 =', p)
print('J(p50) =', e_comp)
print('margin at 1.82890 =', margin)
print('margin at 1.82891 =', boundary_values(D('1.82891'))[-1])
print('root bracket =', root_lo, root_hi)
print('margin(root_lo) =', boundary_values(root_lo)[-1])
print('margin(root_hi) =', boundary_values(root_hi)[-1])
print('Fprime(1.30) =', Fprime_130)
print('Phiprime(1.61) =', Phiprime_161)
print('Jprime(0.61) =', Jprime_061)
print('coarse dmargin/ddelta upper =', coarse_margin_derivative_upper)
print('PASS: g=0.0050 complement-bracing floor t >= 1.82890')
