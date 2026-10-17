#!/usr/bin/env python3
"""Exact interval certificate for the six-pair atomic gap eta_grid=0.001625."""
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
sqrt2 = sqrt_i(I(2))
Delta2 = pi / (2 * sqrt3)
s2 = sqrt_i(Delta2)

eta = I(F(1625, 10**6))
Abar = 2 * s2 + eta
M0 = 4 * s2 * s2 / Abar
R0 = Abar - M0
d0 = Abar * Abar / 4 - s2 * s2 + R0 * R0 / 4
assert d0.lo > 0

# Equal trimming of the two dominant-orbit Mantel shores.
s0 = M0 / 2 - sqrt_i(d0)
K = 2 / sqrt3
L = 4 + sqrt2

# Every original atom family is below the per-pair lemma cutoff K.
shoremax = Abar / 2 + sqrt_i(d0)
assert shoremax.hi < K.lo

# Range required by the analytic six-pair minimization lemma.
assert F(2, 3) * K.hi < s0.lo
assert s0.hi < K.lo

# Exact minimum of the six-pair lower-payment functional is
# 2 * ((3*s0/2-K)/L)^2.  The total missing budget is at most 2*d0,
# so it is enough to certify one half-payment > d0.
gap = F(3, 2) * s0 - K
assert gap.lo > 0
payment = (gap / L) * (gap / L)
assert payment.lo > d0.hi
assert payment.lo - d0.hi > F(3, 10**6)

# Curvature conditions used in the analytic minimization proof.
# c=1/L^2; anti-diagonal concavity needs 12c<2, and the
# one-common-label two-exclusive case uses 16c<2.
assert L.lo * L.lo > 6
assert L.lo * L.lo > 8

print("PASS: six-pair atomic gap eta_grid=0.001625")
print("Abar interval =", float(Abar.lo), float(Abar.hi))
print("M0 interval =", float(M0.lo), float(M0.hi))
print("R0 interval =", float(R0.lo), float(R0.hi))
print("d0 interval =", float(d0.lo), float(d0.hi))
print("s0 interval =", float(s0.lo), float(s0.hi))
print("K interval =", float(K.lo), float(K.hi))
print("shoremax upper =", float(shoremax.hi))
print("half-payment interval =", float(payment.lo), float(payment.hi))
print("half-payment-d0 lower =", float(payment.lo - d0.hi))
