#!/usr/bin/env python3
"""Exact finite regressions for loaded-collar face payment.

Encodes unit separation, circle containment, actual antipodal diameter pairs,
contact alphabets, and the stated finite move. Square roots have rational
outward enclosures; no floating-point acceptance is used. Constructed equalities
are checked through their rational defining identities. The analytic convex
face, pocket, turning, and saturation arguments are not computational claims.
No global optimality, full KKT/PSD, quadratic population, or full-core hypotheses
are encoded. See the associated report and research/README.md.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import isqrt


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    @staticmethod
    def exact(q):
        q = F(q)
        return I(q, q)

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) + (-self)

    def __mul__(self, other):
        other = as_i(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return I(min(products), max(products))

    __rmul__ = __mul__

    def sq(self):
        if self.lo <= 0 <= self.hi:
            return I(F(0), max(self.lo ** 2, self.hi ** 2))
        return I(min(self.lo ** 2, self.hi ** 2),
                 max(self.lo ** 2, self.hi ** 2))


def as_i(q):
    return q if isinstance(q, I) else I.exact(q)


def root(q, bits=100):
    q = F(q)
    assert q >= 0
    scale = 1 << bits
    k = isqrt((q.numerator * scale * scale) // q.denominator)
    assert F(k * k, scale * scale) <= q < F((k + 1) ** 2, scale * scale)
    return I(F(k, scale), F(k + 1, scale))


def point(x, y):
    return as_i(x), as_i(y)


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def mul(t, p):
    return t * p[0], t * p[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def norm2(p):
    return p[0].sq() + p[1].sq()


def dist2(p, q):
    return norm2(sub(p, q))


def edge(a, b):
    return tuple(sorted((a, b)))


def certify_source(points, contacts, diameters, D, center, boundary):
    """Known equalities are constructor identities, strict inequalities enclosed."""
    checks = 0
    for name, p in points.items():
        radius = dist2(p, center)
        if name in boundary:
            assert radius.lo <= D * D / 4 <= radius.hi
        else:
            assert radius.hi < D * D / 4, (name, radius)
    for a, b in combinations(points, 2):
        e = edge(a, b)
        value = dist2(points[a], points[b])
        if e in contacts:
            assert value.lo <= 1 <= value.hi, (e, value)
        else:
            assert value.lo > 1, (e, value)
        if e in diameters:
            assert value.lo <= D * D <= value.hi, (e, value)
        else:
            assert value.hi < D * D, (e, value, D)
        checks += 1
    for a, b, c in combinations(points, 3):
        assert not all(edge(x, y) in contacts for x, y in ((a, b), (b, c), (a, c)))
    return checks


def two_edge_pentagon(t):
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    assert c*c + s*s == 1
    h2 = 1 - (c-F(1, 2)) ** 2
    h = root(h2)
    D = 1/s
    center = point(0, -D/2)
    points = {
        'p0': point(-c, -s), 'p1': point(0, 0), 'p2': point(c, -s),
        'x': point(F(1, 2), -s-h), 'y': point(-F(1, 2), -s-h),
    }
    # Unit anchor identities; all six antipodal endpoints have squared radius R^2.
    assert (c-F(1, 2)) ** 2 + h2 == 1
    assert 2*(D/2)*s == 1
    for i in range(3):
        points['q'+str(i)] = sub(mul(2, center), points['p'+str(i)])
    contacts = {edge(a, b) for a, b in (
        ('p0','p1'), ('p1','p2'), ('p2','x'), ('x','y'), ('y','p0'),
        ('q0','q1'), ('q1','q2'))}
    diameters = {edge('p'+str(i), 'q'+str(i)) for i in range(3)}
    boundary = {'p0','p1','p2','q0','q1','q2'}
    checks = certify_source(points, contacts, diameters, D, center, boundary)
    near = dist2(points['p1'], points['x'])
    assert near.lo > 1 and near.hi <= 1 + 8*s
    reflected = point(0, -2*s)
    assert dist2(reflected, points['x']).hi < 1
    assert dist2(reflected, points['y']).hi < 1
    moved = dict(points)
    moved['p1'] = reflected
    moved['x'] = add(points['x'], point(0, -2*s))
    moved['y'] = add(points['y'], point(0, -2*s))
    new_contacts = contacts - {edge('p2','x'), edge('p0','y')}
    new_diameters = diameters - {edge('p1','q1')}
    checks += certify_source(moved, new_contacts, new_diameters, D,
                             center, boundary - {'p1'})
    assert len(contacts) == 7 and len(new_contacts) == 5
    assert len(diameters) == 3 and len(new_diameters) == 2
    return checks


def one_edge_pentagon(n, angular_parameter):
    # a approaches sqrt(3)/2 strictly from below; angle excess O(2^-n).
    a = F(isqrt(3 * (1 << (2*n-2))), 1 << n)
    assert F(1, 2) < a*a < F(3, 4)
    b2 = 1-a*a
    b = root(b2)
    t = angular_parameter
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    assert c*c+s*s == 1
    d = point(c, s)
    wx, wy = 2*a-c, -s
    L2 = wx*wx+wy*wy
    assert 0 < L2 < 4
    lam2 = (1-L2/4)/L2
    lam = root(lam2)
    # P=-d/2+lambda Jw, Q=P+d. Constructor checks of all three top lengths.
    # P-A=-w/2+lambda Jw; Q-C=w/2+lambda Jw.
    assert L2/4 + lam2*L2 == 1
    midpoint = point(-wy*lam, wx*lam)
    P, Q = sub(midpoint, mul(F(1, 2), d)), add(midpoint, mul(F(1, 2), d))
    D = F(1 << n)
    R = D/2
    depth2 = R*R-F(1, 4)
    depth = root(depth2)
    normal = point(-s, c)
    center = sub(midpoint, mul(depth, normal))
    assert depth2+F(1, 4) == R*R
    points = {'A': point(-a, 0), 'B': point(0, -b), 'C': point(a, 0),
              'P': P, 'Q': Q,
              'p_ant': sub(mul(2, center), P), 'q_ant': sub(mul(2, center), Q)}
    assert a*a+b2 == 1
    contacts = {edge(x,y) for x,y in (
        ('A','B'), ('B','C'), ('C','Q'), ('Q','P'), ('P','A'), ('p_ant','q_ant'))}
    diameters = {edge('P','p_ant'), edge('Q','q_ant')}
    checks = certify_source(points, contacts, diameters, D, center,
                             {'P','Q','p_ant','q_ant'})
    # Loaded direction differs from either unit chart direction.
    assert a*as_i(s) != b*as_i(c)  # reinforced by disjoint interval determinants
    assert (a*s-b*c).hi < 0 and (a*s+b*c).lo > 0
    return checks


def main():
    pairs = 0
    for den in (64, 128, 256, 1024, 4096, 16384, 65536):
        pairs += two_edge_pentagon(F(1, den))
    for n in (12, 18, 24):
        for t in (F(0), F(1,100), F(-1,100), F(1,50), F(-1,50)):
            pairs += one_edge_pentagon(n, t)
    # Projection bounds used in CD.4: L*(1+4/5)<j.
    for j, allowed in ((5,2), (6,3), (7,3)):
        survivors = [L for L in range(j+1) if F(9,5)*L < j]
        assert max(survivors) == allowed
    for j in range(8, 1001):
        assert j <= 2*(j-4)
    print(f'PASS: {pairs} exact source-pair checks; 7 failed reflections and')
    print('7 certified companion moves; 15 changing-direction one-edge pentagons;')
    print('all 993 large-face payment integers. No global optimality claim.')


if __name__ == '__main__':
    main()
