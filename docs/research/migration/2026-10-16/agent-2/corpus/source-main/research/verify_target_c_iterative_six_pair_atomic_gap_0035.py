#!/usr/bin/env python3
"""Exact interval certificate for iterative-pruning six-pair eta_grid=0.0035."""
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
        vals = [self.lo * other.lo, self.lo * other.hi,
                self.hi * other.lo, self.hi * other.hi]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = iv(other)
        assert other.lo > 0
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return iv(other).__truediv__(self)

    def __pow__(self, n):
        assert n == 2
        assert self.lo >= 0
        return I(self.lo * self.lo, self.hi * self.hi)


def iv(x):
    return x if isinstance(x, I) else I(x)


def sqrt_frac(x, digits=50):
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
Delta2 = pi / (2 * sqrt3)
s2 = sqrt_i(Delta2)
K = 2 / sqrt3

eta = I(F(35, 10000))
Abar = 2 * s2 + eta
M0 = 4 * s2 * s2 / Abar
R0 = Abar - M0
d0 = Abar * Abar / 4 - s2 * s2 + R0 * R0 / 4
assert d0.lo > 0
s0 = M0 / 2 - sqrt_i(d0)

# Six-label minimization range.
assert F(2, 3) * K.hi < s0.lo
assert s0.hi < K.lo

# Every physically trimmed label family has mass <= s0. A coarse 0.9 cap
# already lies safely inside the iterative-pruning strong-branch condition.
S = I(F(9, 10))
assert s0.hi < S.lo
ratio = 2 - K / S
assert ratio.lo > 0
assert ratio.hi * ratio.hi < F(20, 29)

# The sharp three-label minimization remains valid for c=1/10.
c = F(1, 10)
assert 12 * c < 2
assert 16 * c < 2
assert c < 1

gap = F(3, 2) * s0 - K
assert gap.lo > 0
half_payment = c * gap * gap
margin = half_payment - d0
assert margin.lo > F(4, 100000)  # visible >4e-5 safety margin

print("PASS: iterative-pruning six-pair eta_grid=0.0035")
print("Abar interval =", float(Abar.lo), float(Abar.hi))
print("M0 interval =", float(M0.lo), float(M0.hi))
print("R0 interval =", float(R0.lo), float(R0.hi))
print("d0 interval =", float(d0.lo), float(d0.hi))
print("s0 interval =", float(s0.lo), float(s0.hi))
print("K interval =", float(K.lo), float(K.hi))
print("strong-branch ratio upper =", float(ratio.hi))
print("sqrt(20/29)^2 target =", float(F(20, 29)))
print("half-payment interval =", float(half_payment.lo), float(half_payment.hi))
print("half-payment-d0 lower =", float(margin.lo))
