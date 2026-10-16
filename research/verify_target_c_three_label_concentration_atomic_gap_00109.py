#!/usr/bin/env python3
"""Exact outward-interval certificate for the TC109 atomic train gap."""
from fractions import Fraction as F
from math import isqrt

SCALE = 10**36
PI = (
    F(3141592653589793238462643383279502884, SCALE),
    F(3141592653589793238462643383279502885, SCALE),
)


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)

    def __add__(self, other):
        other = iv(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __sub__(self, other):
        other = iv(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __rsub__(self, other):
        return iv(other).__sub__(self)

    def __mul__(self, other):
        other = iv(other)
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = iv(other)
        assert other.lo > 0
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return iv(other).__truediv__(self)


def iv(x):
    return x if isinstance(x, I) else I(x)


def sqrt_frac(x, digits=44):
    assert x >= 0
    scale = 10**digits
    m = isqrt((x.numerator * scale * scale) // x.denominator)
    while F((m + 1) * (m + 1), scale * scale) <= x:
        m += 1
    while F(m * m, scale * scale) > x:
        m -= 1
    return F(m, scale), F(m + 1, scale)


def sqrt_i(x):
    lo, _ = sqrt_frac(x.lo)
    _, hi = sqrt_frac(x.hi)
    return I(lo, hi)


pi = I(*PI)
sqrt3 = sqrt_i(I(3))
sqrt2 = sqrt_i(I(2))
Delta = pi / (2 * sqrt3)
s = sqrt_i(Delta)
eta = I(F(109, 100000))
A = 2 * s + eta
M0 = 4 * s * s / A
R0 = A - M0
d0 = A * A / 4 - s * s + R0 * R0 / 4
assert d0.lo > 0
sqrt_d = sqrt_i(d0)
u0 = M0 / 2 - sqrt_d
v0 = A / 2 + sqrt_d
m0 = 2 * d0

# Same-label overlap ratio is safely below the 1/4 concentration threshold.
overlap_ratio = m0 / (u0 * u0)
assert overlap_ratio.hi < F(1, 4)

# Uniform center-label lower bound from Corollary TC109.2.
a0 = u0 - sqrt_i(m0 * v0 / u0)
assert a0.lo > 0

# Opposite-shore mass in the other two labels.
B0 = u0 - m0 / a0
assert B0.lo > 0

K = 2 / sqrt3
L = 4 + sqrt2

# Every atom family fits below the per-pair TL69 size cutoff.
assert v0.hi < K.lo

# Two disjoint leaf payments exceed the whole missing cross-shore budget.
z = a0 + B0 / 2 - K
assert z.lo > 0
payment = (z / L) * (z / L)
assert payment.lo > d0.hi
assert payment.lo - d0.hi > F(19, 10**6)

# Human-readable sanity brackets, deliberately weaker than the exact intervals.
assert A.lo > F(1905715, 10**6)
assert A.hi < F(1905716, 10**6)
assert d0.lo > F(1039, 10**6)
assert d0.hi < F(1040, 10**6)
assert a0.lo > F(8723, 10**4)
assert B0.lo > F(9171, 10**4)

print('PASS: TC109 exact interval certificate')
print('Abar interval =', float(A.lo), float(A.hi))
print('M0 interval =', float(M0.lo), float(M0.hi))
print('d0 interval =', float(d0.lo), float(d0.hi))
print('u0 interval =', float(u0.lo), float(u0.hi))
print('v0 interval =', float(v0.lo), float(v0.hi))
print('same-label overlap ratio upper =', float(overlap_ratio.hi))
print('center mass interval =', float(a0.lo), float(a0.hi))
print('leaf-total interval =', float(B0.lo), float(B0.hi))
print('payment interval =', float(payment.lo), float(payment.hi))
print('payment-d0 lower =', float(payment.lo - d0.hi))
