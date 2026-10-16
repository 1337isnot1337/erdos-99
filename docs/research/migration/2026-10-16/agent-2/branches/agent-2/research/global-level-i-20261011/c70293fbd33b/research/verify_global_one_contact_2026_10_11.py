#!/usr/bin/env python3
"""Exact finite checks for the whole-source one-contact approximation.

Uses rational squared distances; does not certify global optimality or Level I.
The universal statements are proved in the associated report.
"""

from fractions import Fraction as F
from itertools import combinations


def qadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def qsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def qmul(a, b):
    """Multiply in Q(sqrt(5)); coefficients are rational throughout."""
    return (a[0] * b[0] + 5 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def check_pentagon():
    # Represent (x, h*y), with x,y in Q(sqrt(5)) and h=sin(pi/5).
    zero, one = (F(0), F(0)), (F(1), F(0))
    phi = (F(1, 2), F(1, 2))
    h_squared = (F(5, 8), F(-1, 8))
    points = [(zero, zero), (one, zero),
              ((F(3, 4), F(1, 4)), phi),
              ((F(1, 2), F(0)), qadd(phi, one)),
              ((F(1, 4), F(-1, 4)), phi)]
    phi_squared = (F(3, 2), F(1, 2))
    assert qmul(phi, phi) == phi_squared
    contacts = []
    for i, j in combinations(range(5), 2):
        dx, dy = qsub(points[i][0], points[j][0]), qsub(points[i][1], points[j][1])
        distance = qadd(qmul(dx, dx), qmul(h_squared, qmul(dy, dy)))
        if j - i in (1, 4):
            assert distance == one
            contacts.append((i, j))
        else:
            assert distance == phi_squared
    assert len(contacts) == 5
    assert all(not all(tuple(sorted(pair)) in contacts
                       for pair in combinations(triple, 2))
               for triple in combinations(range(5), 3))


def squared_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def ledger(points):
    return {pair: squared_distance(points[pair[0]], points[pair[1]])
            for pair in combinations(range(len(points)), 2)}


def approximate(points, pair, t):
    a, b = pair
    middle = tuple((x + y) / 2 for x, y in zip(points[a], points[b]))
    direction = tuple(y - x for x, y in zip(points[a], points[b]))
    moved = list(points)
    moved[a] = tuple(x + t * u for x, u in zip(points[a], direction))
    moved[b] = tuple(x - t * u for x, u in zip(points[b], direction))
    return [tuple(m + (x - m) / (1 - 2 * t) for x, m in zip(p, middle))
            for p in moved]


def descend(points, pair):
    """Choose a common finite rational contraction by exact feasibility checks."""
    a, b = pair
    middle = tuple((x + y) / 2 for x, y in zip(points[a], points[b]))
    before = ledger(points)
    for exponent in range(1, 100):
        s = F(1, 2 ** exponent)
        after_points = [p if i in pair else
                        tuple(m + (1 - s) * (x - m) for x, m in zip(p, middle))
                        for i, p in enumerate(points)]
        after = ledger(after_points)
        if min(after.values()) < 1:
            continue
        assert after[pair] == 1
        if all(after[edge] < value for edge, value in before.items() if edge != pair):
            assert max(after.values()) < max(before.values())
            return s
    raise AssertionError("No certified descent in bounded finite check")


def main():
    check_pentagon()
    sources = [
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(i, j) for i in range(5) for j in range(4)],
        [(0, 0), (1, 0), (F(1, 2), F(9, 10)), (F(-5, 4), F(3, 2))],
        [(i, 0) for i in range(8)] + [(F(5, 2), 3)],
    ]
    cases = 0
    for raw in sources:
        points = [tuple(F(x) for x in p) for p in raw]
        before = ledger(points)
        assert min(before.values()) == 1
        pair = next(edge for edge, value in before.items() if value == 1)
        for t in (F(1, 1000), F(1, 10), F(1, 4), F(49, 100)):
            after_points = approximate(points, pair, t)
            after = ledger(after_points)
            assert [edge for edge, value in after.items() if value == 1] == [pair]
            assert min(after.values()) == 1
            assert max(after.values()) <= max(before.values()) / (1 - 2 * t) ** 2
            assert after_points[pair[0]] == points[pair[0]]
            assert after_points[pair[1]] == points[pair[1]]
            descend(after_points, pair)
            cases += 1
    # Equilateral triangle: the common radicals cancel from squared distances.
    for t in (F(1, 1000), F(1, 10), F(1, 4), F(49, 100)):
        numerator = (F(1, 2) - t) ** 2 + F(3, 4)
        assert numerator == 1 - t + t * t
        normalized = numerator / (1 - 2 * t) ** 2
        assert normalized - 1 == 3 * t * (1 - t) / (1 - 2 * t) ** 2 > 0
        assert normalized <= 1 / (1 - 2 * t) ** 2
    print(f"PASS: {cases} rational whole-source transformations and descents; "
          "4 exact equilateral checks; all 10 pentagon pairs in Q(sqrt(5)). "
          "No Level I claim.")


if __name__ == "__main__":
    main()
