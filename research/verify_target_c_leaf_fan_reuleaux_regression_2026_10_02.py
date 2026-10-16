#!/usr/bin/env python3
"""Certified finite members of the round Reuleaux leaf-fan regression.

Equalities/PSD/rank for the entire family are proved in the companion report.
This verifier certifies strict inactive-pair gaps using outward-rounded integer
interval arithmetic and a rational Machin-formula enclosure of pi. It never treats
an interval containing zero as proof of equality. Global optimality is omitted;
a strictly smaller same-cardinality triangular grid is certified instead.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import factorial

SCALE = 10**70


def ceildiv(a, b):
    return -((-a) // b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    @staticmethod
    def rational(x):
        x = Fraction(x)
        return Interval(x.numerator * SCALE // x.denominator,
                        ceildiv(x.numerator * SCALE, x.denominator))

    def __add__(self, y):
        y = as_interval(y)
        return Interval(self.lo + y.lo, self.hi + y.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, y):
        return self + -as_interval(y)

    def __rsub__(self, y):
        return as_interval(y) - self

    def __mul__(self, y):
        y = as_interval(y)
        products = [a * b for a in (self.lo, self.hi) for b in (y.lo, y.hi)]
        return Interval(min(products) // SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, y):
        y = as_interval(y)
        assert not (y.lo <= 0 <= y.hi), 'division interval meets zero'
        candidates = [Fraction(a * SCALE, b)
                      for a in (self.lo, self.hi) for b in (y.lo, y.hi)]
        low, high = min(candidates), max(candidates)
        return Interval(low.numerator // low.denominator,
                        ceildiv(high.numerator, high.denominator))

    def square(self):
        values = [self.lo**2, self.hi**2]
        low = 0 if self.lo <= 0 <= self.hi else min(values)
        return Interval(low // SCALE, ceildiv(max(values), SCALE))

    def positive(self):
        return self.lo > 0


def as_interval(x):
    return x if isinstance(x, Interval) else Interval.rational(x)


def arctan_enclosure(inv, terms=60):
    """Alternating series enclosure for atan(1/inv), exact rationals."""
    value = sum(((-1)**j * Fraction(1, (2*j+1)*inv**(2*j+1))
                 for j in range(terms)), Fraction(0))
    next_term = (-1)**terms * Fraction(1, (2*terms+1)*inv**(2*terms+1))
    return min(value, value + next_term), max(value, value + next_term)


a, b = arctan_enclosure(5)
c, d = arctan_enclosure(239)
pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
PI = Interval(Interval.rational(pi_lo).lo, Interval.rational(pi_hi).hi)
assert PI.lo > 3*SCALE and PI.hi < 4*SCALE


def trig_pi(coefficient):
    """sin/cos of a rational multiple of pi, with certified Taylor error."""
    coefficient = Fraction(coefficient) % 2
    if coefficient > 1:
        coefficient -= 2
    x = PI * coefficient
    x2 = x.square()
    sin_term, cos_term = x, as_interval(1)
    sine, cosine = sin_term, cos_term
    terms = 50
    for j in range(1, terms):
        sin_term = -sin_term*x2 / ((2*j)*(2*j+1))
        cos_term = -cos_term*x2 / ((2*j-1)*(2*j))
        sine, cosine = sine + sin_term, cosine + cos_term
    # |x|<4, so the alternating-series error is bounded by the first omitted
    # term. These bounds also work at negative x by odd/even symmetry.
    sin_error = ceildiv(4**(2*terms+1)*SCALE, factorial(2*terms+1))
    cos_error = ceildiv(4**(2*terms)*SCALE, factorial(2*terms))
    return (Interval(sine.lo-sin_error, sine.hi+sin_error),
            Interval(cosine.lo-cos_error, cosine.hi+cos_error))


def squared_distance(p, z):
    return (p[0]-z[0]).square() + (p[1]-z[1]).square()


def verify(q, k):
    assert q >= 5 and q % 2 == 1 and k >= 2
    n, r = q*k, (q-1)//2
    sine_half_step, _ = trig_pi(Fraction(1, 2*q*k))
    _, cosine_half_arc = trig_pi(Fraction(1, 2*q))
    diameter = as_interval(1) / (2*sine_half_step)
    radius = diameter / (2*cosine_half_arc)
    d2 = diameter.square()
    cores = []
    for i in range(q):
        si, co = trig_pi(Fraction(2*i, q))
        cores.append((radius*co, radius*si))
    points = []
    for i in range(q):
        center = cores[(i+r+1) % q]
        for j in range(k):
            si, co = trig_pi(Fraction(2*i, q)+Fraction(1, 2*q)+Fraction(j, q*k))
            points.append((center[0]+diameter*co, center[1]+diameter*si))

    contacts = {tuple(sorted((j, (j+1) % n))) for j in range(n)}
    diameters = set()
    panels = []
    for i in range(q):
        carrier = ((i+r+1) % q)*k
        arc_vertices = [i*k+j for j in range(k)] + [((i+1) % q)*k]
        bars = {tuple(sorted((carrier, p))) for p in arc_vertices}
        diameters |= bars
        panels.append(bars)
    assert len(contacts) == len(diameters) == n
    assert not (contacts & diameters)
    inactive = 0
    for i in range(n):
        for j in range(i+1, n):
            pair = i, j
            if pair in contacts or pair in diameters:
                continue  # Equalities are proved analytically in the report.
            gap2 = squared_distance(points[i], points[j])
            assert (gap2-1).positive(), ('unit gap', q, k, pair)
            assert (d2-gap2).positive(), ('diameter gap', q, k, pair)
            inactive += 1

    # A size-q cover and size-q matching certify nu=q exactly.
    cover = {i*k for i in range(q)}
    assert all(a in cover or b in cover for a, b in diameters)
    matching = [tuple(sorted((((i+r+1) % q)*k, i*k+1))) for i in range(q)]
    assert all(pair in diameters for pair in matching)
    assert len({v for pair in matching for v in pair}) == 2*q
    degrees = [sum(v in pair for pair in diameters) for v in range(n)]
    assert all(degrees[v] == (k+1 if v in cover else 1) for v in range(n))

    # Each panel is triangulated by actual bars. Shared full diameter edges
    # connect all rigid panels, which is an exact infinitesimal-rank witness.
    for i in range(q):
        carrier = ((i+r+1) % q)*k
        arc = [i*k+j for j in range(k)] + [((i+1) % q)*k]
        for a0, a1 in zip(arc, arc[1:]):
            assert tuple(sorted((a0, a1))) in contacts
            assert tuple(sorted((carrier, a0))) in diameters
            assert tuple(sorted((carrier, a1))) in diameters
    seen, todo = set(), [0]
    while todo:
        i = todo.pop()
        if i in seen:
            continue
        seen.add(i)
        todo.extend(j for j in range(q) if j not in seen and panels[i] & panels[j])
    assert len(seen) == q

    # Positive eliminated block and Schur Fourier spectrum; affine-mode
    # equalities j=0,1,q-1 are established by the symbolic proof.
    _, cos_step = trig_pi(Fraction(1, q*k))
    for j in range(1, k):
        _, cos_mode = trig_pi(Fraction(j, k))
        assert (cos_step-cos_mode).positive()
    sin_core, _ = trig_pi(Fraction(1, q))
    ratio = sin_core.square() / cosine_half_arc.square()
    for j in range(2, q-1):
        s1, _ = trig_pi(Fraction(j, q))
        s2, _ = trig_pi(Fraction(r*j, q))
        assert (s1.square()-ratio*s2.square()).positive()

    if q == k:
        assert (d2 - 3*(q-1)**2).positive(), 'strict grid competitor'
        assert (1-(radius-diameter/2)).positive(), 'roundness bound'
        assert (1-(PI*diameter-n)).positive(), 'perimeter-deficit bound'
    return inactive


def main():
    total = 0
    for q, k in [(5, 5), (7, 7), (9, 9), (5, 2), (5, 11)]:
        count = verify(q, k)
        total += count
        print(f'PASS q={q} k={k}: N=h=e={q*k}, nu={q}, '
              f'A={q*(k-2)}, x_B=0, certified inactive pairs={count}')
    print(f'PASS: {total} strict inactive-pair certificates; positive grounded '
          'and Schur modes; full-rank triangle-panel witnesses. '
          'Equalities/infinite family follow from the report, not interval overlap. '
          'No global-minimizer claim.')


if __name__ == '__main__':
    main()
