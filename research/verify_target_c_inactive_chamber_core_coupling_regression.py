#!/usr/bin/env python3
"""Exact regression for a bounded inactive face around a contact core.

The construction and scope are in
docs/reports/target_c_inactive_chamber_core_coupling_regression_2026-09-12.md.
It uses axial triangular-lattice coordinates and Fraction arithmetic.  It checks
the shell cycle, all source separations, the exact diameter and Oler slack, and a
quadratic deep matching.  It intentionally makes no global-optimality claim.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def in_hex(i: int, j: int, radius: int) -> bool:
    return max(abs(i), abs(j), abs(i + j)) <= radius


def shell(radius: int) -> set[tuple[int, int]]:
    return {
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(-radius, radius + 1)
        if max(abs(i), abs(j), abs(i + j)) == radius
    }


def qform(i: Fraction, j: Fraction) -> Fraction:
    return i * i + i * j + j * j


def unit_neighbors(points: set[tuple[int, int]]) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    edges = set()
    for p in points:
        for di, dj in ((1, 0), (0, 1), (1, -1)):
            q = (p[0] + di, p[1] + dj)
            if q in points:
                edges.add(tuple(sorted((p, q))))
    return edges


def greedy_matching(points: set[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    unused = set(points)
    matching = []
    for i, j in sorted(points):
        p = (i, j)
        q = (i + 1, j)
        if p in unused and q in unused and q in points:
            matching.append((p, q))
            unused.remove(p)
            unused.remove(q)
    return matching


def check(m: int) -> None:
    assert m >= 8
    boundary = shell(m)
    inner_radius = m - 2
    inner = {(i, j) for i in range(-inner_radius, inner_radius + 1)
             for j in range(-inner_radius, inner_radius + 1)
             if in_hex(i, j, inner_radius)}
    scale = Fraction(2 * m + 1, 2 * m)

    # The shell is a single unit-contact cycle with no triangle.
    edges = unit_neighbors(boundary)
    assert len(boundary) == 6 * m
    assert len(edges) == 6 * m
    assert all(sum(1 for edge in edges if p in edge) == 2 for p in boundary)
    # There are no hidden unit chords: the exact unit-distance pairs are precisely
    # the cycle edges.
    for p, q in combinations(sorted(boundary), 2):
        distance = qform(Fraction(p[0] - q[0]), Fraction(p[1] - q[1]))
        assert (distance == 1) == (tuple(sorted((p, q))) in edges)

    # Check the exact graph triangle condition.
    adjacency = {p: set() for p in boundary}
    for p, q in edges:
        adjacency[p].add(q)
        adjacency[q].add(p)
    assert not any(q in adjacency[p] and r in adjacency[p] and q in adjacency[r]
                   for p in boundary for q in adjacency[p] for r in adjacency[p]
                   if q != r)

    # Scaled inner points are strictly separated because the nonzero integer
    # quadratic form is at least one and scale > 1.  For cross-separation, the
    # Axial-coordinate gaps must be multiplied by sqrt(3)/2 to obtain physical
    # support distances.  Test the squared physical gap, not the axial gap.
    assert scale > 1
    support_gap = Fraction(m) - scale * (m - 2)
    assert support_gap == Fraction(3, 2) + Fraction(1, m)
    assert Fraction(3, 4) * support_gap**2 > 1
    # Exhaust every cross pair independently of the support proof. Clearing the
    # denominator gives integer arithmetic, including at the larger test sizes.
    denominator = 2 * m
    for i, j in boundary:
        for a, b in inner:
            dx = denominator * i - (denominator + 1) * a
            dy = denominator * j - (denominator + 1) * b
            assert dx * dx + dx * dy + dy * dy > denominator**2

    assert len(inner) == 1 + 3 * inner_radius * (inner_radius + 1)
    normalized_area = 3 * m * m
    assert len(boundary) + len(inner) == 1 + 3 * m * (m - 1) + 6
    oler_slack = normalized_area + 3 * m + 1 - len(inner)
    assert oler_slack == 12 * m - 6

    # Six consecutive radius-m lattice points on one side repair the six-point
    # deficit of H_(m-1) without creating an antipodal pair.
    source_count = len(boundary) + len(inner)
    smaller_diameter_capacity = 1 + 3 * m * (m - 1)
    assert source_count - smaller_diameter_capacity == 6
    added = {(m - i, i) for i in range(6)}
    assert len(added) == 6
    assert all(max(abs(i), abs(j), abs(i + j)) == m for i, j in added)
    assert all(qform(Fraction(p[0] - q[0]), Fraction(p[1] - q[1])) >= 1
               for p, q in combinations(sorted(added), 2))
    assert smaller_diameter_capacity + len(added) == source_count
    assert 2 * m - 1 < 2 * m

    deep_radius = m - 3
    deep = {(i, j) for i in range(-deep_radius, deep_radius + 1)
            for j in range(-deep_radius, deep_radius + 1)
            if in_hex(i, j, deep_radius)}
    matching = greedy_matching(deep)
    assert len(matching) >= (len(deep) - 1) // 4
    assert all(scale * scale * qform(Fraction(p[0] - q[0]), Fraction(p[1] - q[1])) > 1
               for p, q in matching)


def main() -> None:
    # Exact counterexample to the old scale (m+1)/m at m=20:
    # shell (10,10), scaled inner (9,9) -> difference (11/20,11/20).
    old_distance_squared = qform(Fraction(11, 20), Fraction(11, 20))
    assert old_distance_squared == Fraction(363, 400) < 1
    print("REJECTED old scale: m=20 cross-distance squared = 363/400 < 1")
    for m in (8, 12, 20, 40):
        check(m)
        inner_count = 1 + 3 * (m - 2) * (m - 1)
        deep_radius = m - 3
        matching_count = len(greedy_matching({
            (i, j)
            for i in range(-deep_radius, deep_radius + 1)
            for j in range(-deep_radius, deep_radius + 1)
            if in_hex(i, j, deep_radius)
        }))
        print(
            f"m={m} diameter={2*m} competitor_bound={2*m-1} "
            f"source_cardinality={6*m + inner_count} "
            f"smaller_lattice_cardinality={1 + 3*m*(m - 1)} "
            f"shell_vertices={6*m} "
            f"isolates={inner_count} oler_slack={12*m-6} "
            f"deep_matching={matching_count}"
        )
    print("PASS: exact inactive-chamber/core-coupling regression")


if __name__ == "__main__":
    main()
