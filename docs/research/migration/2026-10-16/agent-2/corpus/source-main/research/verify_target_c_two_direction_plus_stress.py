#!/usr/bin/env python3
"""Exact audit of the five-square two-direction positive-stress regression.

This verifies the finite source, its contact/diameter equilibrium stress, and the
same-cardinality triangular-lattice competitor used in
docs/reports/target_c_two_direction_boundary_force_regression_2026-09-14.md.
It is a regression only: it does not claim global optimality of the plus source.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations


Point = tuple[F, F]
Edge = tuple[Point, Point]


PLUS: tuple[Point, ...] = (
    (F(1), F(3)),
    (F(1), F(2)),
    (F(0), F(2)),
    (F(0), F(1)),
    (F(1), F(1)),
    (F(1), F(0)),
    (F(2), F(0)),
    (F(2), F(1)),
    (F(3), F(1)),
    (F(3), F(2)),
    (F(2), F(2)),
    (F(2), F(3)),
)

BOUNDARY: tuple[tuple[int, int], ...] = (
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 0),
)

CENTRAL: tuple[tuple[int, int], ...] = ((4, 1), (1, 10), (10, 7), (7, 4))

# The four diameter pairs in the report, in the displayed vertex indexing.
DIAMETERS: tuple[tuple[int, int], ...] = ((2, 8), (3, 9), (0, 6), (11, 5))


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


def scale(c: F, a: Point) -> Point:
    return (c * a[0], c * a[1])


def norm2(a: Point) -> F:
    return a[0] * a[0] + a[1] * a[1]


def edge(a: Point, b: Point) -> Edge:
    return (a, b)


def main() -> None:
    contacts = BOUNDARY + CENTRAL

    distances = {(i, j): norm2(sub(PLUS[i], PLUS[j]))
                 for i, j in combinations(range(len(PLUS)), 2)}
    assert min(distances.values()) >= 1
    assert max(distances.values()) == 10
    assert {pair for pair, value in distances.items() if value == 1} == {
        tuple(sorted(pair)) for pair in contacts
    }
    assert {pair for pair, value in distances.items() if value == 10} == {
        tuple(sorted(pair)) for pair in DIAMETERS
    }

    # Boundary contact weights in cyclic order, followed by weight 3 on the
    # four central-square edges.  Diameter multipliers are all one.
    boundary_weights = (F(3), F(3), F(1), F(3), F(3), F(1),
                        F(3), F(3), F(1), F(3), F(3), F(1))
    contact_weights = dict(zip(contacts, boundary_weights + (F(3),) * 4))
    diameter_weight = {pair: F(1) for pair in DIAMETERS}

    force = {point: (F(0), F(0)) for point in PLUS}
    for (i, j), weight in contact_weights.items():
        delta_ij = sub(PLUS[j], PLUS[i])
        delta_ji = sub(PLUS[i], PLUS[j])
        force[PLUS[i]] = add(force[PLUS[i]], scale(weight, delta_ij))
        force[PLUS[j]] = add(force[PLUS[j]], scale(weight, delta_ji))
    for (i, j), weight in diameter_weight.items():
        # The convention is alpha(y-x)+beta(x-z)=0 at x, so the two
        # diameter endpoints receive opposite force contributions.
        delta_i = sub(PLUS[i], PLUS[j])
        delta_j = sub(PLUS[j], PLUS[i])
        force[PLUS[i]] = add(force[PLUS[i]], scale(weight, delta_i))
        force[PLUS[j]] = add(force[PLUS[j]], scale(weight, delta_j))

    assert all(value == (F(0), F(0)) for value in force.values())

    # The report's same-cardinality triangular-lattice competitor.  In axial
    # coordinates (a,b), squared Euclidean distance is a^2+ab+b^2.
    competitor_axial = (
        (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 1),
    )

    def axial_norm2(a: tuple[int, int], b: tuple[int, int]) -> int:
        x, y = a[0] - b[0], a[1] - b[1]
        return x * x + x * y + y * y

    competitor_distances = [axial_norm2(a, b)
                            for a, b in combinations(competitor_axial, 2)]
    assert min(competitor_distances) >= 1
    assert max(competitor_distances) == 9

    print("PASS: plus source has 12 points, min squared distance 1, max squared distance 10")
    print("PASS: its unit contacts are exactly the 16 listed two-direction edges")
    print("PASS: all listed contact and diameter multipliers are strictly positive")
    print("PASS: exact mixed equilibrium holds at every source vertex")
    print("PASS: 12-point triangular-lattice competitor has min squared distance 1 and diameter 3")
    print("Scope: finite stress/globality regression; no Level-I claim")


if __name__ == "__main__":
    main()
