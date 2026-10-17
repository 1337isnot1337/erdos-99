"""Directed rational intervals for the independent global E-99 certificates.

Machin's arctangent identity bounds pi; Taylor remainders bound sin and cos.
No floating point participates in a decision. Endpoints use a fixed grid.
"""

from fractions import Fraction as Q
from math import factorial, isqrt

SCALE = 10**50


def ceil_div(a, b):
    assert b > 0
    return -((-a) // b)


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = int(lo), int(lo if hi is None else hi)
        assert self.lo <= self.hi

    @classmethod
    def rational(cls, value):
        value = Q(value)
        return cls(value.numerator * SCALE // value.denominator,
                   ceil_div(value.numerator * SCALE, value.denominator))

    def __add__(self, other):
        other = other if isinstance(other, I) else I.rational(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        other = other if isinstance(other, I) else I.rational(other)
        return self + -other

    def __mul__(self, other):
        other = other if isinstance(other, I) else I.rational(other)
        products = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(products) // SCALE, ceil_div(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I.rational(other)
        assert other.lo > 0
        values = [Q(a * SCALE, b) for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        low, high = min(values), max(values)
        return I(low.numerator // low.denominator,
                 ceil_div(high.numerator, high.denominator))

    def square(self):
        lower = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(lower // SCALE, ceil_div(max(self.lo**2, self.hi**2), SCALE))

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo * SCALE)
        high = isqrt(self.hi * SCALE)
        if high * high < self.hi * SCALE:
            high += 1
        return I(low, high)

    def contains(self, value):
        value = Q(value)
        return (self.lo * value.denominator <= value.numerator * SCALE
                <= self.hi * value.denominator)

    def lower_fraction(self):
        return Q(self.lo, SCALE)

    def upper_fraction(self):
        return Q(self.hi, SCALE)


def atan_bounds(x, terms=80):
    x = Q(x)
    assert 0 < x < 1
    total = sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(terms)), Q())
    next_term = (-1)**terms * x**(2*terms+1) / (2*terms+1)
    return min(total, total + next_term), max(total, total + next_term)


def pi_bounds():
    a_lo, a_hi = atan_bounds(Q(1, 5))
    b_lo, b_hi = atan_bounds(Q(1, 239))
    low, high = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
    assert Q(3) < low < high < Q(22, 7)
    return I(I.rational(low).lo, I.rational(high).hi)


PI = pi_bounds()


def trig_pi(multiplier, sine):
    # Exact periodic reduction keeps the Taylor argument in [0,2*pi]<7.
    multiplier = Q(multiplier) % 2
    x = PI * multiplier
    assert 0 <= x.lo and x.hi < 7 * SCALE
    xx = x.square()
    term = x if sine else I.rational(1)
    total = term
    for k in range(1, 60):
        term = term * xx / ((2*k) * (2*k+1) if sine else (2*k-1) * (2*k))
        total = total - term if k % 2 else total + term
    # Lagrange's derivative bound |f^(j)|<=1. This common bound covers
    # the degree-119 sine and degree-118 cosine truncations.
    remainder = I.rational(Q(7**119, factorial(119))).hi
    return I(total.lo - remainder, total.hi + remainder)


def sin_pi(multiplier):
    return trig_pi(multiplier, True)


def cos_pi(multiplier):
    return trig_pi(multiplier, False)


def check_exact_special_values():
    for t, sine, cosine in [(Q(0), 0, 1), (Q(1, 2), 1, 0),
                             (Q(1), 0, -1), (Q(3, 2), -1, 0), (Q(2), 0, 1)]:
        assert sin_pi(t).contains(sine)
        assert cos_pi(t).contains(cosine)
    assert I.rational(3).sqrt().square().contains(3)


if __name__ == "__main__":
    check_exact_special_values()
    print("PASS directed Machin/Taylor special-value checks; no floating decisions")
