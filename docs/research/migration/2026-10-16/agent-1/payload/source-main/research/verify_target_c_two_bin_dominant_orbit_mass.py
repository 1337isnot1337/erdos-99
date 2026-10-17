#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 90
D = Decimal

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C50 = D(2) * s2 + D('0.0050')
t_safe = D('1.83287')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = x
    for n in range(1, 140):
        term = -term * x * x / D((2 * n) * (2 * n + 1))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('sin series did not converge')


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    for n in range(1, 140):
        term = -term * x * x / D((2 * n - 1) * (2 * n))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('cos series did not converge')


def m2(A: Decimal) -> Decimal:
    rad = D(8) * Delta2 - A * A
    assert rad > 0
    return (A + rad.sqrt()) / D(2)


def m2prime(A: Decimal) -> Decimal:
    rad = D(8) * Delta2 - A * A
    assert rad > 0
    return (D(1) - A / rad.sqrt()) / D(2)


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def Fprime(z: Decimal) -> Decimal:
    return D(1) - cos_decimal(z / D(6))


def J(p: Decimal) -> Decimal:
    return D(2) * p - D(6) * sin_decimal(p / D(3))


def Jprime(p: Decimal) -> Decimal:
    return D(2) - D(2) * cos_decimal(p / D(3))


def R50(t: Decimal) -> Decimal:
    return D('4.5') * t - D(2) * pi - C50


def allocation(S: Decimal):
    # In the certified range the complement coordinate is <1.
    lo = max(D(0), S - D(1))
    hi = S

    def derivative(z: Decimal) -> Decimal:
        return Fprime(z) - Jprime(S - z)

    assert derivative(lo) < 0
    assert derivative(hi) > 0
    a = lo
    b = hi
    for _ in range(230):
        mid = (a + b) / D(2)
        if derivative(mid) < 0:
            a = mid
        else:
            b = mid
    z = (a + b) / D(2)
    p = S - z
    assert D(0) < p < D(1)
    return F(z) + J(p), z, p, derivative(z)


M50 = m2(C50)
old_M50 = D(4) * Delta2 / C50
gain = M50 - old_M50


def boundary_values(t: Decimal):
    delta = R50(t) / D(2)
    Ncomp = C50 + t / D(2) - M50
    S = pi - Ncomp
    energy, z, p, stationarity = allocation(S)
    margin = energy - delta
    return delta, Ncomp, S, energy, z, p, margin, stationarity


safe = boundary_values(t_safe)
delta, Ncomp, S, energy, z, p, margin, stationarity = safe
assert gain > D('0.0049803')
assert margin > D('0.0000112')
assert D('1.64') < z < D('1.65')
assert D('0.57') < p < D('0.59')
assert abs(stationarity) < D('1e-70')

# Root bracket.
root_lo = D('1.8328749746')
root_hi = D('1.8328749747')
assert boundary_values(root_lo)[6] > 0
assert boundary_values(root_hi)[6] < 0

# Domain and feasible-triangle monotonicity.
# At fixed t, U is maximized by delta=kappa=0.
Umax = D('4.5') * t_safe - D(2) * pi
assert Umax < D(2)
assert C50 > D(2) * s2

# m2' is decreasing in A; checking A=2 controls the whole C50<=U<2 interval.
mp2 = m2prime(D(2))
assert mp2 > -D(1) / D(8)
assert m2prime(C50) < 0

# Hence dS/ddelta=2(1-m2')<9/4.
Sdelta_cap = D('2.25')
Fprime_pi = D(1) - sqrt3 / D(2)
assert Sdelta_cap * Fprime_pi < D('0.31') < D(1)

# At the boundary S decreases with t while delta grows, so margin decreases.
assert boundary_values(root_hi)[2] < boundary_values(root_lo)[2]
assert boundary_values(root_hi)[0] > boundary_values(root_lo)[0]

# Quadratic upper-root selection: throughout A<=Umax<2 we have A^2<8Delta2.
assert Umax * Umax < D(8) * Delta2
assert D(4) * Delta2 / Umax > Umax / D(2)

print('Delta2 =', Delta2)
print('C50 =', C50)
print('old dominant mass at C50 =', old_M50)
print('two-bin dominant mass M50 =', M50)
print('dominant mass gain =', gain)
print('t_safe =', t_safe)
print('delta0 =', delta)
print('complement train ceiling N0 =', Ncomp)
print('required shared retained mass S0 =', S)
print('optimal dominant retained z =', z)
print('optimal complement retained p =', p)
print('shared energy =', energy)
print('margin at 1.83287 =', margin)
print('root bracket =', root_lo, root_hi)
print('margin(root_lo) =', boundary_values(root_lo)[6])
print('margin(root_hi) =', boundary_values(root_hi)[6])
print('Umax =', Umax)
print("m2'(2) =", mp2)
print('detour derivative energy cap =', Sdelta_cap * Fprime_pi)
print('PASS: two-bin dominant-orbit floor t >= 1.83287')
