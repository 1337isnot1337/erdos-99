#!/usr/bin/env python3
"""Exact regression for the false orthogonal-boundary lemma.

The point is only to verify the polygonal counterexample used in
docs/reports/target_c_two_direction_boundary_regression_2026-09-14.md.
It does not encode a KKT stress or global optimality certificate.
"""

from __future__ import annotations

from fractions import Fraction as F


Point = tuple[F, F]


P: tuple[Point, ...] = (
    (F(0), F(0)),
    (F(3), F(0)),
    (F(3), F(1)),
    (F(1), F(1)),
    (F(1), F(3)),
    (F(0), F(3)),
)


def cross(a: Point, b: Point, c: Point) -> F:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
    ordered = sorted(set(points))

    def half(items: list[Point]) -> list[Point]:
        out: list[Point] = []
        for point in items:
            while len(out) >= 2 and cross(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    lower = half(ordered)
    upper = half(list(reversed(ordered)))
    return tuple(lower[:-1] + upper[:-1])


def turn(prev: Point, point: Point, nxt: Point) -> int:
    value = cross(prev, point, nxt)
    return 1 if value > 0 else -1 if value < 0 else 0


def main() -> None:
    hull = set(convex_hull(P))
    turns = [turn(P[i - 1], P[i], P[(i + 1) % len(P)]) for i in range(len(P))]
    convex = [P[i] for i, value in enumerate(turns) if value > 0]
    reflex = [P[i] for i, value in enumerate(turns) if value < 0]
    straight = [P[i] for i, value in enumerate(turns) if value == 0]

    assert convex == [(F(0), F(0)), (F(3), F(0)), (F(3), F(1)), (F(1), F(3)), (F(0), F(3))]
    assert reflex == [(F(1), F(1))]
    assert straight == []
    assert set(convex) == hull
    assert not [point for point in convex + straight if point not in hull]

    print("PASS: L-shaped orthogonal polygon is simple and non-square")
    print(f"PASS: convex boundary vertices={len(convex)}; reflex vertices={len(reflex)}")
    print("PASS: every convex/straight boundary vertex lies on the convex hull")
    print("Scope: polygon-lemma regression only; no KKT/global-minimality claim")


if __name__ == "__main__":
    main()
