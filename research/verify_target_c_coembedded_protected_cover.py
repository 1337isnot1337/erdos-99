#!/usr/bin/env python3
"""Exact checks for the co-embedded shell/strict-interior regression.

The companion report proves that a unit-contact shell can surround a dense
strict triangular-lattice interior whose unit disks cover the full inner
window, while the shell covers the outer band of the fixed chamber.  This
script checks the finite combinatorial identities and the exact rational
inequality equivalent to the inner-window covering margin.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Index = tuple[int, int]


def axial_norm(p: Index) -> int:
    i, j = p
    return max(abs(i), abs(j), abs(i + j))


def hex_window(radius: int) -> set[Index]:
    return {
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(-radius, radius + 1)
        if axial_norm((i, j)) <= radius
    }


def shell(radius: int) -> set[Index]:
    return {
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(-radius, radius + 1)
        if axial_norm((i, j)) == radius
    }


def qform(delta: Index) -> int:
    i, j = delta
    return i * i + i * j + j * j


def certificate(radius: int) -> dict[str, object]:
    if radius < 10:
        raise ValueError("need radius >= 10")

    boundary = shell(radius)
    inner = hex_window(radius - 2)
    h = Fraction(2 * radius + 1, 2 * radius)

    if len(boundary) != 6 * radius:
        raise AssertionError("shell cardinality failed")
    if len(inner) != 1 + 3 * (radius - 2) * (radius - 1):
        raise AssertionError("inner cardinality failed")
    if not (h > 1 and h * h < 3):
        raise AssertionError("strict lattice scale failed")

    # Exact shell contact graph check.  It is a single triangle-free cycle in
    # the standard axial triangular lattice.
    shell_edges = set()
    for p, q in combinations(sorted(boundary), 2):
        if qform((p[0] - q[0], p[1] - q[1])) == 1:
            shell_edges.add((p, q))
    if len(shell_edges) != 6 * radius:
        raise AssertionError("shell contact cycle count failed")
    degree = {p: 0 for p in boundary}
    for p, q in shell_edges:
        degree[p] += 1
        degree[q] += 1
    if set(degree.values()) != {2}:
        raise AssertionError("shell is not a cycle")
    adjacency = {p: set() for p in boundary}
    for p, q in shell_edges:
        adjacency[p].add(q)
        adjacency[q].add(p)
    reached = {next(iter(boundary))}
    frontier = list(reached)
    while frontier:
        p = frontier.pop()
        for q in adjacency[p]:
            if q not in reached:
                reached.add(q)
                frontier.append(q)
    if len(reached) != len(boundary):
        raise AssertionError("shell contact graph is disconnected")

    # Every nonzero source difference is a triangular-lattice difference and
    # is therefore strictly longer than one after scaling by h.
    if h * h <= 1:
        raise AssertionError("inner source is not strict")

    # A shell point lies on the boundary of C_R.  The minimum distance from a
    # scaled inner point to the six boundary lines is
    # sqrt(3)/2 * (3/2 + 1/R), which is strictly above one.  Squaring removes
    # the only irrational quantity in this exact check.
    support_gap = Fraction(3, 2) + Fraction(1, radius)
    if 3 * support_gap * support_gap <= 4:
        raise AssertionError("core/interior separation margin failed")

    # C_R,-1 is a regular hexagon of parameter R-2/sqrt(3).  The same
    # projection argument actually covers the larger hexagon H_(R-1).  Its
    # parameter gap over the scaled inner hull is delta_1=1/2+1/R <= 3/5.
    # A side projection is within sqrt(3 delta_1^2/4+h^2/4) of a source
    # point on that side; a vertex projection is within delta_1 of that
    # source vertex.  The report proves the projection/corner dichotomy;
    # this rational check certifies its uniform margin.
    delta_upper = Fraction(3, 5)
    h_upper = Fraction(21, 20)
    if h > h_upper:
        raise AssertionError("scale rational upper bound failed")
    if Fraction(1, 2) + Fraction(1, radius) > delta_upper:
        raise AssertionError("inner-window delta upper bound failed")
    inner_window_bound_squared = (
        Fraction(3, 4) * delta_upper * delta_upper
        + Fraction(1, 4) * h_upper * h_upper
    )
    if inner_window_bound_squared >= 1:
        raise AssertionError("inner-window covering margin failed")

    # Quadratic explicit matching in the strict inner lattice.
    m = (radius - 3) // 2
    matching = m * (2 * m + 1)
    if matching <= radius * radius // 16:
        raise AssertionError("near-unit matching is not quadratic")
    matching_vertices: set[Index] = set()
    for j in range(-m, m + 1):
        for k in range(m):
            left = (-m + 2 * k, j)
            right = (-m + 2 * k + 1, j)
            if axial_norm(left) > radius - 2 or axial_norm(right) > radius - 2:
                raise AssertionError("matching escaped the strict interior")
            if left in matching_vertices or right in matching_vertices:
                raise AssertionError("matching is not vertex-disjoint")
            matching_vertices.add(left)
            matching_vertices.add(right)
    if len(matching_vertices) != 2 * matching:
        raise AssertionError("matching cardinality failed")

    oler_slack = 3 * radius * radius + 3 * radius + 1 - len(inner)
    if oler_slack != 12 * radius - 6:
        raise AssertionError("chamber Oler expression failed")
    total_capacity_slack = 3 * radius * radius + 3 * radius + 1 - (
        len(boundary) + len(inner)
    )
    if total_capacity_slack != 6 * radius - 6:
        raise AssertionError("full-source container capacity slack failed")

    return {
        "radius": radius,
        "scale": h,
        "core_vertices": len(boundary),
        "isolates": len(inner),
        "source_count": len(boundary) + len(inner),
        "oler_slack": oler_slack,
        "matching_count": matching,
        "inner_window_bound_squared": inner_window_bound_squared,
        "total_capacity_slack": total_capacity_slack,
    }


def main() -> None:
    for radius in (10, 20, 40, 80, 160):
        result = certificate(radius)
        print(
            "PASS R={radius} h={scale} core={core_vertices} isolates={isolates} "
            "n={source_count} sigma={oler_slack} matching={matching_count} "
            "inner_window_bound_squared={inner_window_bound_squared} "
            "total_capacity_slack={total_capacity_slack}".format(**result)
        )
    print("PASS: exact co-embedded protected-erosion regression")
    print("Scope: shell/core plus feasible strict interior; no global-optimality claim")


if __name__ == "__main__":
    main()
