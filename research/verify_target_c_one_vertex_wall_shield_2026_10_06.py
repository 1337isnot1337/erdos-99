#!/usr/bin/env python3
"""Exact packets for the convex one-vertex wall shield; no optimality claim.

Certifies a six-edge wall whose five retained vertices admit one strict
interior site, and a full-source lower failure for deleting two wall
vertices without another shield. The analytic exterior shield is proved
in the companion report, not by finite sampling here.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json
from math import isqrt


RADICAND = 808669
assert isqrt(RADICAND) ** 2 != RADICAND


@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(value):
        return value if isinstance(value, Q) else Q(F(value))

    def __add__(self, other):
        other = Q.of(other)
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + -Q.of(other)

    def __rsub__(self, other):
        return Q.of(other) - self

    def __mul__(self, other):
        other = Q.of(other)
        return Q(self.a * other.a + RADICAND * self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if (self.a > 0) == (self.b > 0):
            return 1 if self.a > 0 else -1
        difference = self.a * self.a - RADICAND * self.b * self.b
        assert difference
        return ((self.a > 0) - (self.a < 0)) * (1 if difference > 0 else -1)

    def __str__(self):
        return f"{self.a}+({self.b})sqrt({RADICAND})"


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def squared(p):
    return p[0] * p[0] + p[1] * p[1]


def maximum(values):
    result = values[0]
    for value in values[1:]:
        if (value - result).sign() > 0:
            result = value
    return result


def main():
    radius = F(17, 16)
    cosine, sine = F(161, 289), F(240, 289)
    assert cosine * cosine + sine * sine == 1
    directions = [(F(1), F(0))]
    for _ in range(4):
        x, y = directions[-1]
        directions.append((cosine * x - sine * y,
                           sine * x + cosine * y))
    arc = [tuple(Q(radius * a) for a in p) for p in directions]
    bisector = tuple(-a for a in directions[2])
    center_distance = F(31679, 16 * 4913)
    half_chord = F(4830, 4913)
    height = Q(F(0), F(1, 4913))
    assert height * height == Q(1 - half_chord * half_chord)
    tip_radius = center_distance + height
    tip = tuple(tip_radius * a for a in bisector)
    wall = arc + [tip]
    zero = (Q(), Q())
    contacts = {tuple(sorted((i, (i + 1) % 6))) for i in range(6)}
    source_distances = []
    for i, j in combinations(range(6), 2):
        distance = squared(sub(wall[i], wall[j]))
        source_distances.append(distance)
        assert distance == Q(1) if (i, j) in contacts else (distance - 1).sign() > 0
    for i in range(6):
        a, b, c = wall[i], wall[(i + 1) % 6], wall[(i + 2) % 6]
        assert cross(sub(b, a), sub(c, b)).sign() > 0
        assert cross(sub(b, a), sub(zero, a)).sign() > 0
    assert (squared(tip) - 1).sign() < 0
    assert tip_radius.sign() > 0
    for p in arc:
        assert squared(p) == Q(F(289, 256))

    target = arc + [zero]
    target_distances = []
    target_contacts = set()
    for i, j in combinations(range(6), 2):
        distance = squared(sub(target[i], target[j]))
        target_distances.append(distance)
        assert (distance - 1).sign() >= 0
        if distance == Q(1):
            target_contacts.add((i, j))
    assert len(contacts) == 6 and len(target_contacts) == 4
    assert maximum(source_distances) == maximum(target_distances)

    # An outside contact isolate can enter through a gap left by two deletions.
    square = [(F(0), F(0)), (F(1), F(0)),
              (F(1), F(1)), (F(0), F(1))]
    outside = (F(1, 2), F(-9, 10))
    replacement = (F(1, 2), F(1, 20))
    source = square + [outside]
    square_contacts = set()
    for i, j in combinations(range(5), 2):
        distance = squared(sub(source[i], source[j]))
        assert distance >= 1
        if distance == 1:
            square_contacts.add((i, j))
    assert len(square_contacts) == 4
    assert all(4 not in edge for edge in square_contacts)
    assert all(squared(sub(replacement, p)) > 1 for p in square[2:])
    failure = squared(sub(replacement, outside))
    assert failure == F(361, 400) < 1
    print(json.dumps({
        'classification': 'exact finite packets; analytic shield not enumerated',
        'field': f'Q(sqrt({RADICAND}))',
        'hexagon_source_pair_checks': len(source_distances),
        'hexagon_target_pair_checks': len(target_distances),
        'hexagon_convexity_checks': 6,
        'interior_site_checks': 6,
        'retained_wall_squared_guard_margin': '33/256',
        'old_contacts': len(contacts), 'target_contacts': len(target_contacts),
        'local_packet_diameter_unchanged': True,
        'two_deletion_source_pair_checks': 10,
        'two_deletion_inactive_isolate_squared_distance': str(failure),
        'omitted': ['canonical-source realization', 'actual diameter loads',
                    'global optimality', 'capacity for every source face']
    }, sort_keys=True))


if __name__ == '__main__':
    main()
