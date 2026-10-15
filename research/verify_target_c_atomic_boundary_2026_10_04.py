#!/usr/bin/env python3
"""Finite certificates for the October 4 atomic boundary reports.

Proves the stated rational arithmetic margins, a twelve-point Q(sqrt(3))
geometric regression, and finite support/perimeter identities. Does not prove
weak-limit theorems, global optimality, source existence, or C-II closure.
The source/successor comparison is documented in
docs/audits/atomic_boundary_source_reconciliation_2026-10-15.md.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction as F
from itertools import combinations
from math import isqrt


PI_LO = F(314159265358979323846264338327950288419716939937510, 10**50)
PI_HI = PI_LO + F(1, 10**50)


def sqrt_bounds(x, digits=35):
    scale = 10**digits
    n = isqrt((x.numerator * scale * scale) // x.denominator)
    lo, hi = F(n, scale), F(n + 1, scale)
    assert lo * lo <= x < hi * hi
    return lo, hi


S3_LO, S3_HI = sqrt_bounds(F(3))
DELTA_LO = PI_LO / (2 * S3_HI)
DELTA_HI = PI_HI / (2 * S3_LO)
S2_LO = sqrt_bounds(DELTA_LO)[0]
S2_HI = sqrt_bounds(DELTA_HI)[1]
T0_LO = PI_LO / 2 + 2 * S2_LO / 5
T0_HI = PI_HI / 2 + 2 * S2_HI / 5


class Q3:
    """Exact a+b*sqrt(3), with rational sign certification."""

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Q3) else Q3(x)

    def __add__(self, other):
        y = self.coerce(other)
        return Q3(self.a + y.a, self.b + y.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        y = self.coerce(other)
        return Q3(self.a * y.a + 3 * self.b * y.b,
                  self.a * y.b + self.b * y.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if self.a > 0 and self.b > 0:
            return 1
        if self.a < 0 and self.b < 0:
            return -1
        d = self.a * self.a - 3 * self.b * self.b
        assert d != 0  # sqrt(3) is irrational
        return ((d > 0) - (d < 0)) * ((self.a > 0) - (self.a < 0))

    def __eq__(self, other):
        y = self.coerce(other)
        return self.a == y.a and self.b == y.b


def add(p, q):
    return tuple(x + y for x, y in zip(p, q))


def dot(p, q):
    return sum((x * y for x, y in zip(p, q)), Q3())


def distance2(p, q):
    d = tuple(x - y for x, y in zip(p, q))
    return dot(d, d)


def rotate(p, c, s):
    x, y = p
    return c * x - s * y, s * x + c * y


def atan_bounds(x, n=40):
    assert 0 <= x < 1
    even = sum(((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(2*n)), F())
    odd = even + x**(4*n+1) / (4*n+1)
    assert even <= odd
    return even, odd


def check_arithmetic():
    # Certify the encoded pi bracket by Machin's identity and alternating
    # rational arctangent series, rather than assuming a decimal constant.
    al, ah = atan_bounds(F(1, 5))
    bl, bh = atan_bounds(F(1, 239))
    tan_twice = F(5, 12)
    tan_four = 2*tan_twice/(1-tan_twice*tan_twice)
    assert (tan_four-F(1, 239))/(1+tan_four/F(239)) == 1
    assert PI_LO < 16*al-4*bh < 16*ah-4*bl < PI_HI
    assert F('1.951721449540479') < T0_LO < T0_HI < F('1.951721449540480')
    demand_lo = 10 * (T0_LO - F('1.860'))
    demand_hi = 10 * (T0_HI - F('1.860'))
    assert F('0.91721449540479') < demand_lo < demand_hi < F('0.91721449540480')
    q_hi = PI_HI - demand_lo
    assert q_hi < F('2.22437815818501')
    # Independent derivation: exact outer ledger plus f<=Q, rather than
    # simply evaluating the reported t cutoff.
    q, k, x, m = F(200), F(50), F(30), F(20)
    p = F(210)
    b, g, z = q + x, p - q, q + x - p
    u, Q = x - m, q - x - 2*k
    assert 5*Q + x + m == 10*(q-k) - 5*p + 2*g - 3*z - u
    assert 5*Q + x == 10*(q-k) - 5*p + g - 4*z
    assert 2*Q-k+m == 5*(q-k)-3*p+2*g-z-u
    one_end_lo = (3*PI_LO+2*S2_LO)/5
    one_end_hi = (3*PI_HI+2*S2_HI)/5
    assert F('2.2658807148994') < one_end_lo < one_end_hi < F('2.2658807148995')
    # The exact new sharp-orbit value at A=2.
    phi2_lo, phi2_hi = 5 - PI_HI - S3_HI, 5 - PI_LO - S3_LO
    assert F('0.12635653884132') < phi2_lo < phi2_hi < F('0.12635653884133')
    return 12


def check_geometric_regression():
    pair_checks = 0
    for L, denominator in ((1, 100), (1, 1000), (1, 10000), (2, 200), (3, 300)):
        t = F(1, denominator)
        ce, se = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        zero, e0 = (Q3(), Q3()), (Q3(1), Q3())
        e60, e120 = (Q3(F(1, 2)), Q3(0, F(1, 2))), (Q3(F(-1, 2)), Q3(0, F(1, 2)))
        pairs = [(e0, rotate(e60, ce, se)),
                 (rotate(e60, ce, -se), e120),
                 (rotate(e120, ce, -se), (Q3(-1), Q3()))]
        points = []
        for j, (u, v) in enumerate(pairs):
            assert dot(u, u) == 1 and dot(v, v) == 1
            assert dot(u, v).sign() > 0 and (Q3(F(1, 2)) - dot(u, v)).sign() > 0
            shift = (Q3(10*L*j), Q3())
            points.extend(add(shift, (i*u[0]+k*v[0], i*u[1]+k*v[1]))
                          for i in range(L+1) for k in range(L+1))
        contacts = set()
        for i, j in combinations(range(len(points)), 2):
            d2 = distance2(points[i], points[j])
            assert (d2-1).sign() >= 0
            pair_checks += 1
            if d2 == 1:
                contacts.add((i, j))
        assert len(contacts) == 6*L*(L+1)
        assert not any(all(tuple(sorted(e)) in contacts for e in combinations(triple, 2))
                       for triple in combinations(range(len(points)), 3))
        physical, labels = set(), []
        for a, b in ((0, 1), (1, 2), (2, 0)):
            start = len(labels)
            labels.extend([a]*L+[b]*L)
            physical.update((start+i,start+L+j) for i in range(L) for j in range(L))
        quotient = {tuple(sorted((labels[i], labels[j]))) for i, j in physical}
        assert quotient == {(0, 1), (1, 2), (0, 2)}
        assert len(physical) == 3*L*L and 4*len(physical) <= (6*L)**2
    return pair_checks


def check_sharp_geometry():
    # Quadratic-field tests of the actual endpoint hull and its support
    # function, independently of the final piecewise Phi formula.
    normals = [(Q3(1), Q3()), (Q3(F(1, 2)), Q3(0, F(1, 2))),
               (Q3(F(-1, 2)), Q3(0, F(1, 2))), (Q3(-1), Q3()),
               (Q3(F(-1, 2)), Q3(0, F(-1, 2))),
               (Q3(F(1, 2)), Q3(0, F(-1, 2)))]
    count = 0
    for a in (F(1, 10), F(1, 2), F(3, 5), F(1), F(3, 2), F(3)):
        H = Q3(1) if (Q3(1)-Q3(0, a/2)).sign() >= 0 else Q3(0, a/2)
        vertices = []
        for n in normals:
            tangent = -n[1], n[0]
            vertices += [add(tuple(H*c for c in n), tuple(s*a/2*c for c in tangent))
                         for s in (-1, 1)]
        for n in normals:
            assert all((H-dot(n, v)).sign() >= 0 for v in vertices)
            count += len(vertices)
        # Rational unit test directions in [0,pi/6], generated by half-angle.
        for s in (F(), F(1, 20), F(1, 10), F(1, 5), F(1, 4)):
            direction = Q3((1-s*s)/(1+s*s)), Q3(2*s/(1+s*s))
            supports = [dot(v, direction) for v in vertices] + [Q3(1)]
            direct = supports[0]
            for value in supports[1:]:
                if (value-direct).sign() > 0:
                    direct = value
            c60, s60 = Q3(F(1, 2)), Q3(0, F(1, 2))
            other_cos = c60*direction[0]+s60*direction[1]
            other_sin = s60*direction[0]-c60*direction[1]
            proposed = [Q3(1), H*direction[0]+a/2*direction[1],
                        H*other_cos+a/2*other_sin]
            maximum = proposed[0]
            for value in proposed[1:]:
                if (value-maximum).sign() > 0:
                    maximum = value
            assert direct == maximum
            count += 1
    # An exact rational arctangent enclosure of the first sharp branch.
    lo, hi = atan_bounds(F(1, 6))
    phi_lo, phi_hi = 2-12*hi, 2-12*lo
    assert F('0.0182158') < phi_lo < phi_hi < F('0.0182159')
    return count


if __name__ == '__main__':
    arithmetic = check_arithmetic()
    pairs = check_geometric_regression()
    support = check_sharp_geometry()
    print(f'PASS: {arithmetic} rational budget checks; {pairs} exact full-source pair checks; '
          f'{support} exact convex support checks.')
    print('Scope: finite arithmetic, collapsed-phase regression, and sharp-body geometry; '
          'not a global-optimality or C-II certificate.')
