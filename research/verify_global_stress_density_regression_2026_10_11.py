#!/usr/bin/env python3
"""Finite rational-interval checks; not a global-optimality certificate.

The report proves the all-odd-q assertions analytically. This script verifies
the strict inactive chord bounds, positive nonkernel Fourier eigenvalues,
nonzero rigidity determinant factors, dense isolated interior labels, and
the scalar smaller-lattice-competitor inequality for selected q.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def point(x):
        return I(F(x), F(x))

    def __add__(self, other):
        other = other if isinstance(other, I) else I.point(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -to_i(other)

    def __rsub__(self, other):
        return to_i(other) + -self

    def __mul__(self, other):
        other = to_i(other)
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = to_i(other)
        assert other.lo * other.hi > 0
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return to_i(other) / self

    def square(self):
        if self.lo <= 0 <= self.hi:
            return I(F(0), max(self.lo * self.lo, self.hi * self.hi))
        return I(min(self.lo * self.lo, self.hi * self.hi),
                 max(self.lo * self.lo, self.hi * self.hi))


def to_i(x):
    return x if isinstance(x, I) else I.point(x)


def atan_inverse(n, terms=64):
    """Alternating-series enclosure for atan(1/n)."""
    total = sum(((-1) ** j * F(1, (2*j+1)*n**(2*j+1))
                 for j in range(terms)), F(0))
    next_term = (-1) ** terms * F(1, (2*terms+1)*n**(2*terms+1))
    return I(min(total, total + next_term), max(total, total + next_term))


PI = 16 * atan_inverse(5) - 4 * atan_inverse(239)
pi_scale = 10**60
PI = I(F((PI.lo*pi_scale).__floor__(), pi_scale),
       F((PI.hi*pi_scale).__floor__()+1, pi_scale))
scale = 10**70
root = isqrt(3 * scale**2)
SQRT3 = I(F(root, scale), F(root+1, scale))
A = PI / (2 * SQRT3)


def polynomial_division(numerator, denominator):
    """Exact integer division by a monic polynomial; coefficients ascend."""
    remainder = list(numerator)
    while remainder and remainder[-1] == 0:
        remainder.pop()
    assert denominator[-1] == 1
    quotient = [0] * max(0, len(remainder)-len(denominator)+1)
    while len(remainder) >= len(denominator):
        shift = len(remainder)-len(denominator)
        coefficient = remainder[-1]
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            remainder[shift+i] -= coefficient*value
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return tuple(quotient), tuple(remainder)


@lru_cache(None)
def cyclotomic(q):
    polynomial = (-1,) + (0,)*(q-1) + (1,)
    for d in range(1, q):
        if q % d == 0:
            polynomial, remainder = polynomial_division(polynomial, cyclotomic(d))
            assert not remainder
    return polynomial


def exact_rigidity_modes(q):
    """Independently clear the two Fourier-row denominators in Q[z].

    z is a primitive qth root. A numerator vanishes there exactly when its
    remainder modulo the irreducible cyclotomic polynomial Phi_q is zero.
    This checks the original row determinant, not its trigonometric factors.
    """
    phi = cyclotomic(q)
    m = (q-1)//2
    nonzero = 0
    for ell in range(q):
        coefficients = {}
        factors = (
            (1, ((0, -1), (1, 1)), ((0, 1), (m, 1)),
             ((0, 1), (ell, 1)), ((0, -1), (m*ell, 1))),
            (-1, ((0, 1), (1, 1)), ((0, -1), (m, 1)),
             ((0, 1), (m*ell, 1)), ((0, -1), (ell, 1))),
        )
        for sign, *product in factors:
            terms = [(0, sign)]
            for factor in product:
                terms = [((a+b) % q, c*d) for a, c in terms for b, d in factor]
            for exponent, coefficient in terms:
                coefficients[exponent] = coefficients.get(exponent, 0) + coefficient
        numerator = [coefficients.get(e, 0) for e in range(q)]
        _, remainder = polynomial_division(numerator, phi)
        zero = not remainder
        assert zero == (ell in (0, 1, q-1)), (q, ell)
        nonzero += not zero
    return nonzero


def trig(arg, cosine=False):
    """Taylor enclosure at the rational midpoint, plus a Lipschitz error."""
    midpoint = (arg.lo + arg.hi) / 2
    midpoint_scale = 10**60
    mid = F((midpoint*midpoint_scale).__floor__(), midpoint_scale)
    assert abs(mid) < 4
    terms = 48
    offset = 0 if cosine else 1
    total = sum(((-1)**j * mid**(2*j+offset) / factorial(2*j+offset)
                 for j in range(terms)), F(0))
    # Taylor's theorem to degree 2*terms+offset-1; all derivatives <=1.
    degree_next = 2 * terms + offset
    err = abs(mid)**degree_next / factorial(degree_next)
    err += max(abs(mid-arg.lo), abs(mid-arg.hi))
    return I(total-err, total+err)


def check_q(q):
    assert q >= 5 and q % 2 == 1
    x = PI / (2*q)
    sx = trig(x)
    d = 1 / (2 * sx)
    radius = 1 / (2 * trig(2*x))
    m = (q-1)//2
    chords = spectra = rigidity = 0

    # Exact chord classes k=1 and k=m are respectively contact and diameter.
    # Every other class has strict lower/upper slack.
    for k in range(2, m):
        chord = trig(2*k*x) / trig(2*x)
        assert chord.lo > 1 and chord.hi < d.lo
        chords += q

    # (3) and the independently factored determinant (6)/(7).
    for ell in range(2, q-1):
        sl = trig(ell*x)
        cl = trig(ell*x, cosine=True)
        denominator = sl if ell % 2 else cl
        spectral_gap = d.square() - 1 / (4 * denominator.square())
        assert spectral_gap.lo > 0
        spectra += 1
        determinant_factor = sx.square() - denominator.square()
        assert determinant_factor.hi < 0
        assert sl.lo > 0 and cl.lo > 0
        rigidity += 1

    assert exact_rigidity_modes(q) == rigidity

    if q < 41:
        return chords, spectra, rigidity, 0, 0

    # Freeze the integer count only after both rational endpoints agree.
    population = A * (d-4).square()
    n = population.lo.numerator // population.lo.denominator
    assert n == population.hi.numerator // population.hi.denominator
    assert n > q
    spacing = F(q*q+1, q*q)
    inner = d/2 - 2
    assert inner.lo > 0
    assert (radius-inner).lo > 2
    assert (radius * trig(2*x, cosine=True)).lo > inner.hi
    assert ((n-1) / A).hi < (d-4).square().lo

    # A fixed centered triangular lattice is sufficient in these examples;
    # the universal proof instead uses translation averaging.
    bound = int(2 * inner.hi) + 3
    sites = []
    for a in range(-bound, bound+1):
        for b in range(-bound, bound+1):
            norm2 = spacing**2 * (a*a+a*b+b*b)
            if norm2 < inner.lo**2:
                sites.append((norm2, a, b))
    assert len(sites) >= n-q
    chosen = sorted(sites)[:n-q]
    lower_pairs = 0
    for j, (_, a, b) in enumerate(chosen):
        for _, c, e in chosen[:j]:
            da, db = a-c, b-e
            pair2 = spacing**2 * (da*da+da*db+db*db)
            assert pair2 > 1
            lower_pairs += 1

    # These radial inequalities cover every inserted-involving upper pair
    # and every ring-isolate lower pair, including pairs not individually
    # enumerated. Their strictness is recorded above, not inferred by sampling.
    assert 2*inner.hi < d.lo
    assert (radius+inner).hi < d.lo
    covered_pairs = len(chosen)*q + lower_pairs
    return chords, spectra, rigidity, n, covered_pairs


def interval_controls():
    # tan(4 atan(1/5)-atan(1/239))=1; the positive angle is below
    # 4/5, fixing the branch in Machin's identity used to enclose pi.
    t = F(1, 5)
    double = 2*t/(1-t*t)
    fourfold = 2*double/(1-double*double)
    assert (fourfold-F(1, 239))/(1+fourfold/F(239)) == 1
    angle = 4*atan_inverse(5)-atan_inverse(239)
    assert 0 < angle.lo <= angle.hi < F(4, 5)
    assert 3 < PI.lo <= PI.hi < F(22, 7)
    assert SQRT3.lo**2 < 3 < SQRT3.hi**2
    for arg, cosine, exact in (
        (I.point(0), False, F(0)), (I.point(0), True, F(1)),
        (PI/6, False, F(1, 2)), (PI/3, True, F(1, 2)),
        (PI/2, False, F(1)), (PI, False, F(0)),
    ):
        value = trig(arg, cosine)
        assert value.lo <= exact <= value.hi
        assert value.hi-value.lo < F(1, 10**40)
    print("PASS: Machin branch, square-root and six exact trigonometric controls")


def main():
    interval_controls()
    totals = [0, 0, 0, 0]
    qs = (5, 7, 9, 11, 15, 21, 31, 41, 61, 81, 101)
    for q in qs:
        chords, spectra, rigidity, n, pairs = check_q(q)
        totals[0] += chords
        totals[1] += spectra
        totals[2] += rigidity
        totals[3] += pairs
        print(f"q={q}: strict chord pairs={chords}; positive modes={spectra}; "
              f"nonzero rigidity modes={rigidity}; full population={n or 'ring only'}; "
              f"isolate-involving pairs covered={pairs}")
    print("PASS: rational interval and exact lattice checks; "
          f"{totals[0]} inactive ring pairs, {totals[1]} spectral modes, "
          f"{totals[2]} rigidity modes, {totals[3]} isolate-involving pairs.")
    print("Scope: finite nonglobal regressions only. Universal proofs are analytic; "
          "no canonical-source or Level I certificate.")


if __name__ == "__main__":
    main()
