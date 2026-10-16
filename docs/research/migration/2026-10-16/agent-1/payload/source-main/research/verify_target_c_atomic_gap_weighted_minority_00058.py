#!/usr/bin/env python3
"""Exact rational interval certificate for the AG58 weighted-minority constants."""
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

    def __add__(self, o):
        o = iv(o)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __sub__(self, o):
        o = iv(o)
        return I(self.lo - o.hi, self.hi - o.lo)

    def __rsub__(self, o):
        return iv(o).__sub__(self)

    def __mul__(self, o):
        o = iv(o)
        vals = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = iv(o)
        assert o.lo > 0
        return self * I(1 / o.hi, 1 / o.lo)

    def __rtruediv__(self, o):
        return iv(o).__truediv__(self)


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
rt2 = sqrt_i(I(2))
Delta = pi / (2 * s3)
s2 = sqrt_i(Delta)
eta = I(F(58, 100000))
A = 2 * s2 + eta
M0 = 4 * s2 * s2 / A
R0 = A - M0
d0 = A * A / 4 - s2 * s2 + R0 * R0 / 4
assert d0.lo > 0

# Shore mass before atom-window minority deletion.
S = M0 / 2 - sqrt_i(d0)
minority = sqrt_i(6 * d0)
p0 = sqrt_i(2 * d0)

# AG58.1: the 1+2 label support uses the total minority loss once.
pair_mass = F(3, 2) * S - minority
selected_degree = pair_mass - (4 + rt2) * p0
projection = s3 * selected_degree / 2

# Worst individual family after chain-cover and degree pruning, minus 3*p0
# required for a triple common neighbor.
common_neighbor_margin = (S - minority) / 2 - (4 + rt2) * p0

assert projection.lo > F(10003, 10000)
assert common_neighbor_margin.lo > F(1, 4)

print("PASS: AG58 exact interval certificate")
print("projection lower =", float(projection.lo))
print("common-neighbor margin lower =", float(common_neighbor_margin.lo))
print("M0 interval =", float(M0.lo), float(M0.hi))
print("d0 interval =", float(d0.lo), float(d0.hi))
print("S interval =", float(S.lo), float(S.hi))
print("minority-loss interval =", float(minority.lo), float(minority.hi))
print("p0 interval =", float(p0.lo), float(p0.hi))
print("selected-pair lower =", float(pair_mass.lo))
