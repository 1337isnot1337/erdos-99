#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 85
D = Decimal

pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
C0 = D(2) * Delta2.sqrt() + D('0.0050')
t_safe = D('1.83279')
t_prev = D('1.83236')


def sin_decimal(x: Decimal) -> Decimal:
    term = x
    total = x
    for n in range(1, 180):
        term = -term * x * x / D((2 * n) * (2 * n + 1))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('sin series did not converge')


def cos_decimal(x: Decimal) -> Decimal:
    term = D(1)
    total = term
    for n in range(1, 180):
        term = -term * x * x / D((2 * n - 1) * (2 * n))
        new = total + term
        if new == total:
            return total
        total = new
    raise AssertionError('cos series did not converge')


def F(z: Decimal) -> Decimal:
    return z - D(6) * sin_decimal(z / D(6))


def J(p: Decimal) -> Decimal:
    return D(2) * p - D(6) * sin_decimal(p / D(3))


def Fprime(z: Decimal) -> Decimal:
    return D(1) - cos_decimal(z / D(6))


def Jprime(p: Decimal) -> Decimal:
    return D(2) - D(2) * cos_decimal(p / D(3))


def boundary_values(t: Decimal):
    delta = (D('4.5') * t - D(2) * pi - C0) / D(2)
    ncomp = C0 + t / D(2) - D(4) * Delta2 / C0
    total = pi - ncomp

    # Unique minimizer of F(total-p)+J(p), p in [0,1].
    lo = D(0)
    hi = min(D(1), total)
    for _ in range(280):
        p = (lo + hi) / D(2)
        z = total - p
        if Jprime(p) < Fprime(z):
            lo = p
        else:
            hi = p
    p = (lo + hi) / D(2)
    z = total - p

    e_dom = F(z)
    e_comp = J(p)
    margin = e_dom + e_comp - delta
    return delta, ncomp, total, z, p, e_dom, e_comp, margin, Fprime(z), Jprime(p)


safe = boundary_values(t_safe)
prev = boundary_values(t_prev)

# Advertised round endpoint.
assert safe[7] > D('0.0000080')
assert D('1.63') < safe[3] < D('1.65')
assert D('0.57') < safe[4] < D('0.59')
assert safe[9] == safe[8]

# Previous direct-tradeoff endpoint is excluded with much larger margin.
assert prev[7] > D('0.00098')

# Tight root bracket; the theorem deliberately stops at 1.83279.
root_lo = D('1.83279356481905')
root_hi = D('1.83279356481906')
assert boundary_values(root_lo)[7] > 0
assert boundary_values(root_hi)[7] < 0

# Uniform smooth-regime and feasible-triangle bounds.
assert Jprime(D('0.72')) < D('0.058')
assert safe[1] > D('0.9225')
assert J(D(1)) > D('0.0368')
assert safe[0] < D('0.028')

# Since U>=C0>2sqrt(Delta2), dS/ddelta<4.  With p<.72,
# d(H(S)-delta)/ddelta < 4 J'(.72)-1 < 0.
assert C0 > D(2) * Delta2.sqrt()
assert D(4) * Jprime(D('0.72')) - D(1) < D('-0.76')

# Boundary monotonicity is exact:
# S0'(t)=-1/2, delta0'(t)=9/4, H'(S)>0.
assert safe[8] > 0

print('Delta2 =', Delta2)
print('C0 =', C0)
print('t_safe =', t_safe)
print('delta0 =', safe[0])
print('Ncomp upper =', safe[1])
print('retained total S0 =', safe[2])
print('z0 =', safe[3])
print('p0 =', safe[4])
print('F(z0) =', safe[5])
print('J(p0) =', safe[6])
print('margin =', safe[7])
print('common marginal =', safe[8])
print('root bracket =', root_lo, root_hi)
print('H(root_lo) =', boundary_values(root_lo)[7])
print('H(root_hi) =', boundary_values(root_hi)[7])
print("J'(0.72) =", Jprime(D('0.72')))
print('PASS: joint endpoint retention floor t >= 1.83279')
