#!/usr/bin/env python3
"""Exact finite exercises for the reflected straight-interface candidate.

The universal packing construction and density limit are analytic. These cases
check the seam, reflection, slab and counting formulas, including irrationally
related row periods and zero-gap rows. They do not extract a source interface,
bound finite junction costs, certify a global minimizer, or close Level I.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from dataclasses import dataclass
from fractions import Fraction as F
from functools import total_ordering
from itertools import combinations

from verify_global_boundary_zigzag_2026_10_11 import (
    interval_quadratic, sign_quadratic,
)


@total_ordering
@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a))
        object.__setattr__(self, "b", F(self.b))

    @staticmethod
    def of(value):
        return value if isinstance(value, Q) else Q(value)

    def __add__(self, other):
        other = Q.of(other)
        return Q(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self+-Q.of(other)

    def __rsub__(self, other):
        return Q.of(other)+-self

    def __mul__(self, other):
        other = Q.of(other)
        return Q(self.a*other.a+3*self.b*other.b,
                 self.a*other.b+self.b*other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q.of(other)
        denominator = other.a*other.a-3*other.b*other.b
        assert denominator
        return self*Q(other.a/denominator, -other.b/denominator)

    def __rtruediv__(self, other):
        return Q.of(other)/self

    def __eq__(self, other):
        other = Q.of(other)
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        # Rational Q values compare equal to Fraction/int; their hashes must
        # also agree when point sets or dictionaries mix these representations.
        return hash(self.a) if not self.b else hash((self.a, self.b))

    def __lt__(self, other):
        difference = self-Q.of(other)
        return sign_quadratic(difference.a, difference.b) < 0

    def floor(self):
        lower, _ = interval_quadratic(self.a, self.b)
        result = lower.numerator // lower.denominator
        while self >= result+1:
            result += 1
        assert result <= self < result+1
        return result

    def ceil(self):
        return -(-self).floor()


A0 = Q(0, F(1, 2))


def add(p, q):
    return p[0]+q[0], p[1]+q[1]


def sub(p, q):
    return p[0]-q[0], p[1]-q[1]


def scale(k, p):
    return k*p[0], k*p[1]


def norm2(p):
    return p[0]*p[0]+p[1]*p[1]


@dataclass(frozen=True)
class Lattice:
    s: Q
    b: Q
    h: Q

    @property
    def u(self):
        return self.s, Q(0)

    @property
    def v(self):
        return self.b, self.h

    @property
    def volume(self):
        return self.s*self.h

    def site(self, k, j):
        return k*self.s+j*self.b, j*self.h

    def integer_coordinates(self, point):
        j = point[1]/self.h
        k = (point[0]-j*self.b)/self.s
        assert j.b == k.b == 0
        assert j.a.denominator == k.a.denominator == 1
        return int(k.a), int(j.a)

    def check_unit_separated(self):
        assert self.s >= 1 and self.h > 0 and self.volume >= A0
        # All omitted rows have vertical separation >=1. In each remaining
        # row these are the two closest horizontal residues to zero.
        reach = (1/self.h).ceil()
        checked = 0
        for j in range(-reach, reach+1):
            k0 = (-j*self.b/self.s).floor()
            for k in (k0, k0+1):
                if j or k:
                    assert norm2(self.site(k, j)) >= 1
                    checked += 1
        return checked


def check_complete_seam(a, b, t):
    assert t[1] >= 0
    if t[1] >= 1:
        return "vertical guard"
    if a == b and t == a.v:
        return "one original lattice"
    assert a.s == b.s and a.h >= 1 and b.h >= 1
    k0 = (-t[0]/a.s).floor()
    # All nonfront cross-row pairs have vertical separation >=1.
    for k in (k0, k0+1):
        assert norm2((t[0]+k*a.s, t[1])) >= 1
    return "front residues and deeper-row guard"


def check_stack(name, a, b, t, n, m):
    assert n*a.h >= 1 and m*b.h >= 1
    q = add(scale(2, t), scale(m, b.v))
    period = add(q, scale(n, a.v))
    height = period[1]
    assert height == 2*t[1]+n*a.h+m*b.h
    points = []
    identities = 0
    for r in (-1, 0, 1):
        shift = scale(r, period)
        inversion_sum = add(scale(2*r, period), q)
        for k in range(-2, 3):
            for j in range(-n, 1):
                point = add(shift, a.site(k, j))
                reflected = sub(inversion_sum, point)
                coords = a.integer_coordinates(sub(reflected, scale(r+1, period)))
                assert coords == (-k, -n-j)
                points.append(point)
                identities += 1
            for j in range(m+1):
                point = add(add(shift, t), b.site(k, j))
                reflected = sub(inversion_sum, point)
                coords = b.integer_coordinates(sub(sub(reflected, shift), t))
                assert coords == (-k, m-j)
                points.append(point)
                identities += 1
    assert len(set(points)) == len(points)
    pairs = contacts = 0
    for p, qpoint in combinations(points, 2):
        distance2 = norm2(sub(p, qpoint))
        assert distance2 >= 1, (name, p, qpoint, distance2)
        pairs += 1
        contacts += distance2 == 1

    rows = (n+1)/a.s+(m+1)/b.s
    exact_payment = (2*t[1]-A0*(1/a.s+1/b.s)
                     +n*(a.volume-A0)/a.s+m*(b.volume-A0)/b.s)
    assert height-A0*rows == exact_payment >= 0
    if a.volume == b.volume == A0:
        assert t[1] >= (a.h+b.h)/2
    correction = (1+1/A0)*((a.volume-A0)+(b.volume-A0))/2
    assert t[1] >= A0*(1/a.s+1/b.s)/2-correction
    assert n/a.s <= 1/a.volume+1/a.s or n != (1/a.h).ceil()
    print(f"{name}: N={n}, M={m}, labels={len(points)}, pairs={pairs}, "
          f"contacts={contacts}, reflection identities={identities}")
    return len(points), pairs, identities


def cropped_rows(lattice, shift, first, last, left, right):
    points = []
    for j in range(first, last+1):
        offset = shift[0]+j*lattice.b
        kmin = ((left-offset)/lattice.s).ceil()
        kmax = ((right-offset)/lattice.s).floor()
        for k in range(kmin, kmax+1):
            point = add(shift, lattice.site(k, j))
            assert left <= point[0] <= right
            points.append(point)
    return points


def centered(value, period):
    result = value-(value/period+F(1, 2)).floor()*period
    assert -period/2 <= result <= period/2
    return result


def absolute(value):
    return -value if value < 0 else value


def check_finite_window(name, a, b, t, center, length):
    n, m = (1/a.h).ceil(), (1/b.h).ceil()
    # Move the A origin to its front-row site nearest the window center.
    origin = (center/a.s+F(1, 2)).floor()*a.s
    center -= origin
    t = (center+centered(t[0]-origin-center, b.s), t[1])
    assert absolute(center) <= a.s/2 and absolute(t[0]-center) <= b.s/2
    left, right = center-length/2, center+length/2
    source_a = cropped_rows(a, (Q(0), Q(0)), -n, 0, left, right)
    source_b = cropped_rows(b, t, 0, m, left, right)
    source_pairs = 0
    for p in source_a:
        for qpoint in source_b:
            assert norm2(sub(p, qpoint)) >= 1
            source_pairs += 1
    error = (A0*(1/a.s+1/b.s)-2*t[1]
             -n*(a.volume-A0)/a.s-m*(b.volume-A0)/b.s)
    ssum = a.s+b.s
    assert length*max(error, Q(0)) <= 24*ssum
    gap_lower = (A0*length*(1/a.s+1/b.s)/2
                 -(1+1/A0)*length*((a.volume-A0)+(b.volume-A0))/2
                 -12*ssum)
    assert t[1]*length >= gap_lower
    guard = 3*ssum/2
    width = length-2*guard
    if width <= 0:
        assert error > 0  # This case exercises a genuinely finite seam.
        print(f"{name}: {source_pairs} finite source cross-pairs; "
              "positive seam debt is paid by the endpoint bound")
        return source_pairs, 0, 0

    wa = (centered(n*a.b, a.s), n*a.h)
    wb = (centered(m*b.b, b.s), m*b.h)
    q = add(scale(2, t), wb)
    period = add(q, wa)
    height = period[1]
    assert absolute(period[0]) <= guard
    assert absolute(wa[0]+2*center) <= guard
    assert absolute(q[0]-2*center) <= guard
    jleft, jright = left+guard, right-guard
    base_a = cropped_rows(a, (Q(0), Q(0)), -n, 0, jleft, jright)
    base_b = cropped_rows(b, t, 0, m, jleft, jright)
    for point in base_a:
        preimage = sub(scale(-1, wa), point)
        assert left <= preimage[0] <= right
        _, row = a.integer_coordinates(preimage)
        assert -n <= row <= 0
    for point in base_b:
        preimage = sub(q, point)
        assert left <= preimage[0] <= right
        _, row = b.integer_coordinates(sub(preimage, t))
        assert 0 <= row <= m
    base = base_a+base_b
    assert len(base) >= width*((n+1)/a.s+(m+1)/b.s)-(n+m+2)
    points = [add(scale(r, period), p) for r in range(3) for p in base]
    assert len(set(points)) == len(points)
    strip_pairs = 0
    for p, qpoint in combinations(points, 2):
        assert norm2(sub(p, qpoint)) >= 1
        strip_pairs += 1
    tilted = [p[0]-(period[0]/height)*p[1] for p in points]
    assert max(tilted)-min(tilted) <= width+absolute(period[0])
    assert max(p[1] for p in points)-min(p[1] for p in points) <= 3*height
    # |T| <= H+|T_x| gives an exact upper bound without another radical.
    endpoint_bound = (height*absolute(period[0])
                      +A0*(height+absolute(period[0]))+A0*(n+m+2))
    assert width*error <= endpoint_bound
    print(f"{name}: {source_pairs} finite source cross-pairs, "
          f"{len(points)} strip labels, {strip_pairs} strip pairs")
    return source_pairs, len(points), strip_pairs


def main():
    for value in (F(-7, 3), F(0), F(1), F(19, 20)):
        exact = Q(value)
        assert exact == value and hash(exact) == hash(value)
        assert len({exact, value}) == 1
    for value in (Q(-1, F(1, 2)), Q(F(1, 2), -1), Q(0), Q(F(-3, 2))):
        result = value.floor()
        assert result <= value < result+1
        assert value.ceil() == -(-value).floor()
    print("PASS: rational equality/hash consistency and signed quadratic-field floors")
    triangular = Lattice(Q(1), Q(F(1, 2)), A0)
    rotated = Lattice(Q(0, 1), Q(0, F(1, 2)), Q(F(1, 2)))
    near = Lattice(Q(1), Q(F(1, 2)), A0+F(1, 10**6))
    square = Lattice(Q(1), Q(0), Q(1))
    sparse = Lattice(Q(3), Q(0), Q(1))
    defect = Lattice(Q(F(19, 10)), Q(0), Q(1))
    cases = [
        ("triangular equality", triangular, triangular, triangular.v),
        ("rotated triangular equality", rotated, rotated, rotated.v),
        ("incommensurate row periods", triangular, rotated, (Q(0), Q(1))),
        ("near-triangular defect", near, near, near.v),
        ("square seam", square, square, (Q(F(1, 2)), A0)),
        ("zero-gap interlaced fronts", sparse, sparse, (Q(F(3, 2)), Q(0))),
        ("defect correction is necessary", defect, defect,
         (Q(F(19, 20)), Q(F(8, 25)))),
    ]
    labels = pairs = identities = short_vectors = 0
    for name, a, b, t in cases:
        short_vectors += a.check_unit_separated()+b.check_unit_separated()
        check_complete_seam(a, b, t)
        n, m = (1/a.h).ceil(), (1/b.h).ceil()
        for dn, dm in ((0, 0), (1, 2)):
            values = check_stack(name, a, b, t, n+dn, m+dm)
            labels += values[0]
            pairs += values[1]
            identities += values[2]

    # A finite exact negative fixture: lowering a triangular seam to 4/5
    # produces a front-pair collision, so the half-plane premise fails.
    bad_front = (Q(F(1, 2)), Q(F(4, 5)))
    assert norm2(bad_front) == F(89, 100) < 1
    # The valid large-covolume seam refutes deleting the correction in (3).
    assert Q(F(8, 25)) < A0/defect.s
    assert norm2((Q(F(19, 20)), Q(F(8, 25)))) == F(10049, 10000) > 1
    finite_cases = [
        ("finite triangular seam", triangular, triangular, triangular.v,
         Q(F(11, 7)), Q(12)),
        ("finite rotated seam", rotated, rotated, rotated.v,
         Q(F(-5, 3)), Q(24)),
        ("finite incommensurate seam", triangular, rotated, (Q(0), Q(1)),
         Q(F(2, 9)), Q(18)),
        ("finite sparse seam", defect, defect, (Q(F(19, 20)), Q(F(8, 25))),
         Q(F(5, 7)), Q(24)),
        ("finite zero-gap seam", sparse, sparse, (Q(F(3, 2)), Q(0)),
         Q(F(-7, 11)), Q(30)),
        ("finite seam with invalid infinite continuation", triangular, rotated,
         (Q(F(4, 5)), Q(F(3, 5))), Q(F(9, 20)), Q(F(9, 10))),
    ]
    finite_source_pairs = strip_labels = strip_pairs = 0
    for case in finite_cases:
        counts = check_finite_window(*case)
        finite_source_pairs += counts[0]
        strip_labels += counts[1]
        strip_pairs += counts[2]
    # The final window is valid, but its infinite continuation is not:
    # A's omitted front point (1,0) collides with B's front point (4/5,3/5).
    assert norm2((Q(F(-1, 5)), Q(F(3, 5)))) == F(2, 5) < 1
    print(f"PASS: {len(cases)} seams, {2*len(cases)} stacks, {labels} labels, "
          f"{pairs} pairs, {identities} reflection identities, "
          f"{short_vectors} short lattice-vector checks, 2 negative diagnostics")
    print(f"PASS: {len(finite_cases)} finite windows, {finite_source_pairs} source "
          f"cross-pairs, {strip_labels} strip labels, {strip_pairs} strip pairs")
    print("Scope: finite formulas and fixtures; no source extraction, bound on total "
          "junction cost, global-optimality certificate, or Level I closure.")


if __name__ == "__main__":
    main()
