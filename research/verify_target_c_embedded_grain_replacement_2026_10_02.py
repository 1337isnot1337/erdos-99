#!/usr/bin/env python3
"""Exact finite certificates for embedded contact-wall grain replacement.

Arithmetic: Fraction pairs a+b*sqrt(3), with exact sign comparisons.
Encoded: actual square-grid walls/interiors, 38 strictly guarded sites, all
source/new pair distances, simultaneous adjacent patches, and real diameter
vertex-cover deletion/refill. The oblique area thresholds are squared rational
comparisons. Omitted: global optimality, KKT, arbitrary grid extraction, and any
claim that failure of the area test proves failure of fixed-wall repacking.
The universal wall/competitor theorems are proved in the accompanying report.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def cast(x):
        return x if isinstance(x, Q3) else Q3(F(x))

    def __add__(self, other):
        y = self.cast(other)
        return Q3(self.a + y.a, self.b + y.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        y = self.cast(other)
        return Q3(self.a*y.a + 3*self.b*y.b, self.a*y.b + self.b*y.a)

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
        diff = self.a*self.a - 3*self.b*self.b
        assert diff != 0  # irrationality of sqrt(3)
        return ((diff > 0) - (diff < 0)) * ((self.a > 0) - (self.a < 0))

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __le__(self, other):
        return (self - other).sign() <= 0

    def __gt__(self, other):
        return (self - other).sign() > 0

    def __ge__(self, other):
        return (self - other).sign() >= 0

    def __eq__(self, other):
        if not isinstance(other, (Q3, int, F)):
            return NotImplemented
        y = self.cast(other)
        return self.a == y.a and self.b == y.b

    def __hash__(self):
        return hash(self.a) if self.b == 0 else hash((self.a, self.b))


def norm2(p, q):
    dx, dy = p[0]-q[0], p[1]-q[1]
    return dx*dx + dy*dy


def grid(r, s, shift=0):
    return [(Q3(F(i+shift)), Q3(F(j)))
            for i in range(r+1) for j in range(s+1)]


def wall(r, s, shift=0):
    return [(Q3(F(i+shift)), Q3(F(j)))
            for i in range(r+1) for j in range(s+1)
            if i in (0, r) or j in (0, s)]


def packet(shift=0):
    result = []
    labels = []
    for i in range(-3, 4):
        for j in range(-8, 8):
            y = F(4) + F(i, 2) + j
            if (F(3, 2) <= y <= F(11, 2) if i % 2 else F(1) <= y <= F(6)):
                result.append((Q3(F(7, 2)+shift, F(i, 2)), Q3(y)))
                labels.append((i, j))
    assert len(result) == 38
    # A fixed exact strictification, stronger than the existential dilation proof.
    lam = F(100001, 100000)
    c = (Q3(F(7, 2)+shift), Q3(F(7, 2)))
    expanded = [(c[0]+lam*(x-c[0]), c[1]+lam*(y-c[1])) for x, y in result]
    return result, expanded, labels


def check_packet():
    old = grid(7, 7)
    boundary = wall(7, 7)
    raw, new, _ = packet()
    assert len(old) == 64 and len(boundary) == 28
    assert all(0 < x < 7 and 0 < y < 7 for x, y in new)
    assert all(norm2(p, q) >= 1 for p, q in combinations(old, 2))
    assert all(norm2(p, q) >= 1 for p, q in combinations(raw, 2))
    assert all(norm2(p, q) > 1 for p, q in combinations(new, 2))
    gaps = [norm2(p, b)-1 for p in new for b in boundary]
    margin = min(gaps)
    assert margin > F(1, 20)
    # Same cardinality and fewer contacts; diameter is unchanged by retained corners.
    contact_competitor = boundary + new[:36]
    assert len(contact_competitor) == 64
    assert all(norm2(p, q) >= 1 for p, q in combinations(contact_competitor, 2))
    old_contacts = sum(norm2(p, q) == 1 for p, q in combinations(old, 2))
    new_contacts = sum(norm2(p, q) == 1 for p, q in combinations(contact_competitor, 2))
    assert old_contacts == 112 and new_contacts == 28
    assert max(norm2(p, q) for p, q in combinations(contact_competitor, 2)) == 98
    # Delete a real two-vertex cover of the old diameter graph; use the two spare sites.
    cover = {(Q3(0), Q3(0)), (Q3(0), Q3(7))}
    old_diameters = [(p, q) for p, q in combinations(old, 2) if norm2(p, q) == 98]
    assert len(old_diameters) == 2
    assert all(p in cover or q in cover for p, q in old_diameters)
    strict_competitor = [p for p in boundary if p not in cover] + new
    assert len(strict_competitor) == 64
    assert all(norm2(p, q) >= 1 for p, q in combinations(strict_competitor, 2))
    assert max(norm2(p, q) for p, q in combinations(strict_competitor, 2)) == 85
    print("PASS: 38 exact strict sites; squared wall margin >1/20; 112->28 contacts; 98->85 diameter squared")


def check_simultaneous():
    # Two embedded seven-face squares sharing one entire old unit-contact wall.
    first = packet()[1]
    second = packet(7)[1]
    assert all(norm2(p, q) > 3 for p in first for q in second)
    original = grid(14, 7)
    interiors = {(Q3(F(i)), Q3(F(j)))
                 for i in range(1, 14) if i != 7 for j in range(1, 7)}
    assert len(original) == 120 and len(interiors) == 72
    cover = {(Q3(0), Q3(0)), (Q3(0), Q3(7))}
    retained = [p for p in original if p not in interiors and p not in cover]
    inserted = first + second[:36]
    competitor = retained + inserted
    assert len(competitor) == 120
    assert all(norm2(p, q) >= 1 for p, q in combinations(competitor, 2))
    assert all(norm2(p, q) > 1 for p in inserted for q in retained)
    diam2 = max(norm2(p, q) for p, q in combinations(competitor, 2))
    assert diam2 < 245
    print("PASS: adjacent wall packets; 1444 cross-packet gaps >3; actual 120-point strict competitor")


def check_patch_stability():
    for vx in (F(800, 160001), -F(800, 160001)):
        vy = F(159999, 160001)
        assert vx*vx + vy*vy == 1
        assert vx*vx + (vy-1)**2 < F(1, 40000)
        shift = (Q3(F(7, 2)*vx), Q3(F(7, 2)*(vy-1)))
        source = [(Q3(F(i)+j*vx), Q3(j*vy))
                  for i in range(8) for j in range(8)]
        boundary = [(Q3(F(i)+j*vx), Q3(j*vy))
                    for i in range(8) for j in range(8) if i in (0, 7) or j in (0, 7)]
        reference = [(p[0]+shift[0], p[1]+shift[1]) for p in grid(7, 7)]
        assert all(norm2(p, q) < F(1, 2500) for p, q in zip(source, reference))
        new = [(p[0]+shift[0], p[1]+shift[1]) for p in packet()[1]]
        assert all(norm2(p, b) > 1 for p in new for b in boundary)
        for x, y in new:
            beta = y*(1/vy)
            alpha = x-vx*beta
            assert 0 < alpha < 7 and 0 < beta < 7
    # Universal conservative guard estimate for any 1/50 Euclidean perturbation.
    assert (1+F(1, 50))**2 < F(21, 20)
    assert F(1, 2) < (1-F(1, 50))**2
    print("PASS: two exact oblique perturbations; universal 1/50 guard/cover inequalities")


def threshold(sin_theta):
    for k in range(3, 2001):
        if k <= 2/sin_theta:
            continue
        area = (k-2/sin_theta)**2*sin_theta
        count_minus_one = k*k-2*k
        if 4*area*area > 3*count_minus_one*count_minus_one:
            return k
    raise AssertionError("increase exact threshold bound")


def check_area_and_regressions():
    cases = [F(1), F(24, 25), F(15, 17), F(168, 193)]
    answers = {str(s): threshold(s) for s in cases}
    assert answers["1"] == 15
    # Two-face oblique patch: centre is the unique feasible site for every open
    # strict-rhombus angle. These examples check its exact boundary data; the
    # continuum uniqueness proof is in the report.
    for vx, vy in [(F(0), F(1)), (F(7, 25), F(24, 25)), (F(8, 17), F(15, 17)),
                   (F(95, 193), F(168, 193))]:
        assert vx*vx + vy*vy == 1 and abs(vx) < F(1, 2)
        b = [(Q3(F(i)+j*vx), Q3(j*vy))
             for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]
        zero = (Q3(), Q3())
        assert min(norm2(p, zero) for p in b) == 1
        assert sum(norm2(p, zero) == 1 for p in b) == 4
        assert all(norm2(p, q) >= 1 for p, q in combinations(b, 2))
    # Marked Hall surplus need not be proportional to quadratic contact population.
    r = 7
    sites = [(F(i, 1)+F(1, 2), F(j, 1)+F(1, 2))
             for i in range(r) for j in range(r)]
    src = [(F(i), F(j)) for i in range(r+1) for j in range(r+1)]
    neigh = {z for b in sites for z in src
             if (z[0]-b[0])**2+(z[1]-b[1])**2 <= 1}
    assert len(neigh) == 64 and len(sites) == 49
    assert all(sum((z[0]-b[0])**2+(z[1]-b[1])**2 <= 1 for z in src) == 4
               for b in sites)
    print("PASS: exact area thresholds", answers)
    print("PASS: four two-face boundary packets; geometric square-grid Hall regression")


if __name__ == "__main__":
    check_packet()
    check_simultaneous()
    check_patch_stability()
    check_area_and_regressions()
