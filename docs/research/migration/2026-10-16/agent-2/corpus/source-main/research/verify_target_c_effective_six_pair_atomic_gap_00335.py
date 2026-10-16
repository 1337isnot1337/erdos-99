#!/usr/bin/env python3
"""Exact interval certificate for effective-coefficient six-pair atomic gap eta=0.00335."""
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


def sqrt_frac(x, digits=42):
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
s3 = sqrt_i(I(3))
Delta = pi / (2 * s3)
s2 = sqrt_i(Delta)
eta = I(F(335, 100000))

A = 2 * s2 + eta
M0 = 4 * s2 * s2 / A
R0 = A - M0
d0 = A * A / 4 - s2 * s2 + R0 * R0 / 4
sd = sqrt_i(d0)
s0 = M0 / 2 - sd
K = 2 / s3

# Safe cap for every retained atom family: no family can exceed its Mantel shore.
S = A / 2 + sd

# Iterative-pruning pair theorem: rho >= min(g^2/10, 2m^2/29).
# For a,b <= S and g=(a+b-K)_+ > 0,
# g/m <= 2-K/S.  Therefore rho >= c_eff*g^2 with
# c_eff=min(1/10, 2/(29*(2-K/S)^2)).
ratio = 2 - K / S
c2 = 2 / (29 * ratio * ratio)
c_eff = I(c2.lo, c2.hi)

gap = F(3, 2) * s0 - K
payment = c_eff * gap * gap
margin = payment - d0

assert d0.lo > 0
assert S.hi < K.lo
assert s0.lo > 2 * K.hi / 3
assert s0.hi < K.lo
assert ratio.lo > 0
assert c2.hi < F(1, 10)
assert c2.lo > F(93, 1000)
assert c2.hi < F(1, 8)
assert gap.lo > 0
assert margin.lo > F(5, 100000)

print("PASS: effective six-pair eta=0.00335")
print("Abar interval =", float(A.lo), float(A.hi))
print("M0 interval =", float(M0.lo), float(M0.hi))
print("R0 interval =", float(R0.lo), float(R0.hi))
print("d0 interval =", float(d0.lo), float(d0.hi))
print("s0 interval =", float(s0.lo), float(s0.hi))
print("family cap S interval =", float(S.lo), float(S.hi))
print("K interval =", float(K.lo), float(K.hi))
print("ratio cap interval =", float(ratio.lo), float(ratio.hi))
print("c_eff interval =", float(c2.lo), float(c2.hi))
print("gap interval =", float(gap.lo), float(gap.hi))
print("payment interval =", float(payment.lo), float(payment.hi))
print("payment-d0 lower =", float(margin.lo))
