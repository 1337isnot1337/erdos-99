#!/usr/bin/env python3
"""Exact finite checks for slot 02 quarter-fold face obstructions.

Arithmetic is Q(sqrt(15)); rational cases have zero radical coefficient.
The analytic universal proofs are in the companion report. These examples
certify pair ledgers and scope boundaries, not global source optimality.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json


@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(F(x))

    def __add__(self, other):
        other = Q.of(other)
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + -Q.of(other)

    def __rsub__(self, other):
        return Q.of(other) + -self

    def __mul__(self, other):
        other = Q.of(other)
        return Q(self.a * other.a + 15 * self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if (self.a > 0) == (self.b > 0):
            return 1 if self.a > 0 else -1
        d = self.a * self.a - 15 * self.b * self.b
        assert d != 0  # sqrt(15) is irrational.
        return ((self.a > 0) - (self.a < 0)) * (1 if d > 0 else -1)

    def encode(self):
        return [str(self.a), str(self.b)]


def point(x, y):
    return Q.of(x), Q.of(y)


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(p, k):
    return p[0] * k, p[1] * k


def J(p):
    return -p[1], p[0]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def distance(p, q):
    d = sub(p, q)
    return d[0] * d[0] + d[1] * d[1]


def exact_min(values):
    winner = values[0]
    for q in values[1:]:
        if (q - winner).sign() < 0:
            winner = q
    return winner


def exact_max(values):
    winner = values[0]
    for q in values[1:]:
        if (q - winner).sign() > 0:
            winner = q
    return winner


def ledger(points):
    pairs = {e: distance(points[e[0]], points[e[1]])
             for e in combinations(range(len(points)), 2)}
    assert all((d - 1).sign() >= 0 for d in pairs.values())
    contacts = {e for e, d in pairs.items() if d == Q.of(1)}
    triangles = [t for t in combinations(range(len(points)), 3)
                 if all(e in contacts for e in combinations(t, 2))]
    assert not triangles
    diameter = exact_max(list(pairs.values()))
    return pairs, contacts, diameter


def cycle_edges(n):
    return {tuple(sorted((i, (i + 1) % n))) for i in range(n)}


def area(points):
    return sum((cross(a, b) for a, b in
                zip(points, points[1:] + points[:1])), Q()) * F(1, 2)


def turns(points):
    n = len(points)
    return [cross(sub(points[i], points[i - 1]),
                  sub(points[(i + 1) % n], points[i])).sign()
            for i in range(n)]


def verify_fold(points, signs, z):
    """z is the image after undoing the common proper quarter-turn."""
    n = len(points)
    assert len(signs) == len(z) == n
    for i in range(n):
        j = (i + 1) % n
        assert sub(z[j], z[i]) == scale(sub(points[j], points[i]), signs[i])
    u = [J(p) for p in z]
    for i in range(n):
        j = (i + 1) % n
        assert sub(u[j], u[i]) == scale(J(sub(points[j], points[i])), signs[i])
    return u


def bowed_eight():
    p = [point(F(x, 41), F(y, 41)) for x, y in
         [(0, 0), (40, -9), (80, 0), (89, 40),
          (80, 80), (40, 89), (0, 80), (-9, 40)]]
    z = [point(F(x, 41), F(y, 41)) for x, y in
         [(0, 0), (40, -9), (80, 0), (71, -40),
          (80, -80), (40, -71), (0, -80), (9, -40)]]
    u = verify_fold(p, [1, 1, -1, -1, 1, 1, -1, -1], z)
    old, contacts, d2 = ledger(p)
    new, new_contacts, new_d2 = ledger(u)
    assert contacts == new_contacts == cycle_edges(8)
    assert d2 == new_d2 == Q(F(12800, 1681))
    assert turns(p) == [1] * 8
    assert turns(z) == [-1, 1] * 4
    assert area(p) == Q(F(7840, 1681))
    assert area(z) == Q(F(-4960, 1681))

    # A complete finite contact-loss endpoint, in the z coordinate frame.
    released = list(z)
    released[1] = add(z[1], point(0, -F(1, 100)))
    final, final_contacts, final_d2 = ledger(released)
    assert final_contacts == cycle_edges(8) - {(0, 1), (1, 2)}
    assert final_d2 == d2
    assert all((d2 - d).sign() >= 0 for d in final.values())

    # Retaining an old strict isolate at the center fails at the quarter-turn.
    center = point(F(40, 41), F(40, 41))
    _, contacts9, _ = ledger(p + [center])
    assert contacts9 == contacts
    collisions = [i for i, v in enumerate(u)
                  if (distance(center, v) - 1).sign() < 0]
    assert collisions == [1, 3, 5, 7]
    return {
        'old_area': area(p).encode(),
        'folded_signed_area': area(z).encode(),
        'diameter_squared': d2.encode(),
        'full_pair_checks': len(old) + len(new) + len(final) + 36,
        'release_amplitude': '1/100',
        'released_contacts': [[0, 1], [1, 2]],
        'fixed_center_lower_collisions': collisions,
    }


def flat_eight():
    a, b = point(1, 0), point(F(5, 13), F(12, 13))
    labels = [(0, 0), (1, 0), (2, 0), (2, 1),
              (2, 2), (1, 2), (0, 2), (0, 1)]
    p = [add(scale(a, i), scale(b, j)) for i, j in labels]
    z = [sub(scale(a, i), scale(b, j)) for i, j in labels]
    u = verify_fold(p, [1, 1, -1, -1, 1, 1, -1, -1], z)
    old, c, d = ledger(p)
    new, cc, dd = ledger(u)
    assert c == cc == cycle_edges(8)
    assert d == dd == Q(F(144, 13))
    assert turns(p) == [1, 0] * 4
    assert turns(z) == [-1, 0] * 4
    assert area(p) == -area(z) == Q(F(48, 13))
    old_h = {e for e, v in old.items() if v == d}
    new_h = {e for e, v in new.items() if v == dd}
    assert old_h == {(0, 4)} and new_h == {(2, 6)}
    return {'full_pair_checks': len(old) + len(new),
            'diameter_squared': d.encode(),
            'old_diameter_pairs': sorted(old_h),
            'new_diameter_pairs': sorted(new_h)}


def odd_twenty_one():
    # Bottom arc: four copies of (7,-sqrt(15))/8, then four
    # copies of (7,+sqrt(15))/8. The remaining arcs have 3,7,3 edges.
    p = [point(F(7*k, 8), Q(0, F(-k, 8))) for k in range(5)]
    p += [point(F(7*k, 8), Q(0, F(-(8-k), 8))) for k in range(5, 9)]
    p += [point(7, k) for k in range(1, 4)]
    p += [point(k, 3) for k in range(6, -1, -1)]
    p += [point(0, k) for k in range(2, 0, -1)]
    assert len(p) == 21
    z = [(x, y) if i <= 8 else (x, -y) for i, (x, y) in enumerate(p)]
    u = verify_fold(p, [1]*8 + [-1]*3 + [1]*7 + [-1]*3, z)
    old, c, d = ledger(p)
    new, cc, dd = ledger(u)
    assert c == cc == cycle_edges(21)
    assert d == dd == Q.of(58)
    assert all(v >= 0 for v in turns(p))
    assert 1 in turns(z) and -1 in turns(z)
    assert area(p) == Q(21, F(7, 4))
    assert area(z) == Q(-21, F(7, 4))
    # A five-by-five square grid contains a 21-point competitor of D^2<=32.
    grid = [point(i, j) for i in range(5) for j in range(5)][:21]
    grid_d = exact_max([distance(a, b) for a, b in combinations(grid, 2)])
    assert (Q.of(32) - grid_d).sign() >= 0 and (d - grid_d).sign() > 0
    return {'arc_lengths': [8, 3, 7, 3],
            'old_area': area(p).encode(),
            'folded_signed_area': area(z).encode(),
            'diameter_squared': d.encode(),
            'old_min_noncontact_squared': exact_min(
                [v for e, v in old.items() if e not in c]).encode(),
            'folded_min_noncontact_squared': exact_min(
                [v for e, v in new.items() if e not in cc]).encode(),
            'full_pair_checks': len(old) + len(new),
            'nonglobal_competitor_diameter_squared': grid_d.encode()}


def small_arc_counts():
    # Exact comparisons with 2/sqrt(3), without floating square roots.
    assert all(3*(k+1)**2 >= 4*k*k for k in range(1, 7))
    assert 3*8**2 < 4*7**2
    feasible_counts = []
    for m in range(8, 19):
        for a in range(2, m):
            for b in range(2, m-a):
                for c in range(2, m-a-b):
                    d = m-a-b-c
                    if d < 2:
                        continue
                    if (3*max(a, c)**2 < 4*min(a, c)**2 and
                            3*max(b, d)**2 < 4*min(b, d)**2):
                        assert a == c and b == d and m % 2 == 0
                        feasible_counts.append([a, b, c, d])
    return {'cutoff': 18, 'admissible_count_vectors': feasible_counts,
            'first_unequal_pair_allowed_by_ratio': [7, 8],
            'scope': 'count inequality only; not geometric realization'}


def main():
    result = {
        'arithmetic': 'Q(sqrt(15)), exact sign comparisons',
        'bowed_eight': bowed_eight(),
        'flat_eight_guardrail': flat_eight(),
        'odd_twenty_one_guardrail': odd_twenty_one(),
        'small_arc_count_reduction': small_arc_counts(),
        'scope': 'finite regressions; no global optimality or universal endpoint existence',
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
