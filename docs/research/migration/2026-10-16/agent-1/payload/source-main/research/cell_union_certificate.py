"""Exact metric certificates for the triangular-lattice cell union.

The scaffold cells are convex hulls of lattice vertices lying at strict distance
less than one from their blocker.  This module isolates the small convexity
calculation behind the resulting cell-union interpretation.  Coordinates are in
the 60-degree lattice basis, so the squared Euclidean norm is

    |a e1 + b e2|^2 = a^2 + a*b + b^2.

The code is intentionally a certificate helper rather than a point-placement
optimizer.  It does not infer that an arbitrary point lies in a cell; it checks
the vertex-clearance hypothesis from which strict cell coverage follows.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, floor
from typing import Iterable, Sequence


ObliquePoint = tuple[Fraction, Fraction]
LatticeCoord = tuple[int, int]


def _point(value: Iterable[int | Fraction]) -> ObliquePoint:
    first, second = value
    return Fraction(first), Fraction(second)


def triangular_distance_squared(
    first: ObliquePoint, second: ObliquePoint
) -> Fraction:
    """Return the exact squared Euclidean distance in the 60-degree basis."""

    first_delta = first[0] - second[0]
    second_delta = first[1] - second[1]
    return (
        first_delta * first_delta
        + first_delta * second_delta
        + second_delta * second_delta
    )


def maximum_vertex_distance_squared(
    point: ObliquePoint, vertices: Sequence[ObliquePoint]
) -> Fraction:
    """Return the largest squared distance from ``point`` to a cell vertex."""

    if not vertices:
        raise ValueError("a cell must have at least one vertex")
    return max(triangular_distance_squared(point, vertex) for vertex in vertices)


def strict_cell_cover_margin_squared(
    point: ObliquePoint, vertices: Sequence[ObliquePoint]
) -> Fraction:
    """Return the strict unit-disk margin certified at all cell vertices.

    If this is positive and ``point`` lies anywhere in the convex hull of
    ``vertices``, the open unit disk centered at ``point`` contains the whole
    convex cell by convexity of the norm.
    """

    return Fraction(1) - maximum_vertex_distance_squared(point, vertices)


def strictly_covers_convex_cell(
    point: ObliquePoint, vertices: Sequence[ObliquePoint]
) -> bool:
    """Whether the vertex-clearance certificate proves strict cell coverage."""

    return strict_cell_cover_margin_squared(point, vertices) > 0


def _cross(
    first: ObliquePoint, second: ObliquePoint, third: ObliquePoint
) -> Fraction:
    """Return the oriented coordinate cross product of three points."""

    first_x = second[0] - first[0]
    first_y = second[1] - first[1]
    second_x = third[0] - first[0]
    second_y = third[1] - first[1]
    return first_x * second_y - first_y * second_x


def _convex_hull(vertices: Sequence[ObliquePoint]) -> tuple[ObliquePoint, ...]:
    """Return the vertices of the closed convex hull in cyclic order."""

    points = sorted(set(vertices))
    if len(points) < 3:
        raise ValueError("a cell hull must have at least three distinct vertices")

    lower: list[ObliquePoint] = []
    for point in points:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper: list[ObliquePoint] = []
    for point in reversed(points):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    hull = tuple(lower[:-1] + upper[:-1])
    if len(hull) < 3:
        raise ValueError("cell hull must have nonzero area")
    return hull


def _in_closed_convex_polygon(
    point: ObliquePoint, polygon: Sequence[ObliquePoint]
) -> bool:
    """Return whether a point lies in a cyclically ordered closed convex polygon."""

    signs = [
        _cross(polygon[index], polygon[(index + 1) % len(polygon)], point)
        for index in range(len(polygon))
    ]
    return all(sign >= 0 for sign in signs) or all(sign <= 0 for sign in signs)


def lattice_points_in_convex_hull(
    vertices: Sequence[ObliquePoint],
) -> tuple[ObliquePoint, ...]:
    """Enumerate all integer-coordinate lattice points in a closed cell hull.

    The enumeration is exact because the hull coordinates and the point-in-polygon
    test are rational.  It is intended for the small monomer--dimer cells used by
    the scaffold certificate, not for large-scale optimization.
    """

    hull = _convex_hull(vertices)
    first_min = ceil(min(point[0] for point in hull))
    first_max = floor(max(point[0] for point in hull))
    second_min = ceil(min(point[1] for point in hull))
    second_max = floor(max(point[1] for point in hull))
    points = [
        (Fraction(first), Fraction(second))
        for first in range(first_min, first_max + 1)
        for second in range(second_min, second_max + 1)
        if _in_closed_convex_polygon(
            (Fraction(first), Fraction(second)), hull
        )
    ]
    return tuple(points)


def cell_union_lattice_points(
    cells: Iterable[Sequence[ObliquePoint]],
) -> tuple[ObliquePoint, ...]:
    """Return lattice points in the union of closed convex cell hulls."""

    points: set[ObliquePoint] = set()
    for cell in cells:
        points.update(lattice_points_in_convex_hull(cell))
    return tuple(sorted(points))


def free_lattice_sinks(
    inner_lattice: Iterable[ObliquePoint],
    cells: Iterable[Sequence[ObliquePoint]],
) -> tuple[ObliquePoint, ...]:
    """Return inner lattice sites outside the union of the supplied cell hulls."""

    inner = {_point(point) for point in inner_lattice}
    occupied = set(cell_union_lattice_points(cells))
    return tuple(sorted(inner - occupied))


def monomer_centroid_certificate() -> Fraction:
    """Return the exact strict margin for a unit-triangle centroid."""

    point = _point((Fraction(1, 3), Fraction(1, 3)))
    vertices = tuple(_point(vertex) for vertex in ((0, 0), (1, 0), (0, 1)))
    return strict_cell_cover_margin_squared(point, vertices)


def dimer_center_certificate() -> Fraction:
    """Return the exact strict margin for a unit-lozenge center."""

    point = _point((Fraction(1, 2), Fraction(1, 2)))
    vertices = tuple(_point(vertex) for vertex in ((0, 0), (1, 0), (0, 1), (1, 1)))
    return strict_cell_cover_margin_squared(point, vertices)


def cell_union_lattice_sites(cells: Iterable[object]) -> frozenset[LatticeCoord]:
    """Return every triangular-lattice site lying in a scaffold cell union.

    A monomer triangle and a dimer lozenge have no lattice sites other than their
    displayed vertices. Consequently the lattice trace of a union of such cells is
    exactly the union of their vertex sets. The loose object annotation is
    deliberate: this helper accepts Cell objects from scaffold_cells without
    importing that research module and creating a dependency cycle.
    """

    sites: set[LatticeCoord] = set()
    for cell in cells:
        sites.update(getattr(cell, "vertices"))
    return frozenset(sites)


def free_lattice_sites(
    cells: Iterable[object], lattice_sites: Iterable[LatticeCoord]
) -> frozenset[LatticeCoord]:
    """Return lattice sites outside the cell union.

    For the scaffold conflict graph, these are right-side vertices with no edge
    from any selected blocker. They are therefore an immediate Hall witness.
    """

    ambient = frozenset(lattice_sites)
    return frozenset(ambient.difference(cell_union_lattice_sites(cells)))


def free_sink_hall_lower_bound(
    cells: Iterable[object], lattice_sites: Iterable[LatticeCoord]
) -> int:
    """Return the exact Hall-deficiency lower bound from free right vertices."""

    return len(free_lattice_sites(cells, lattice_sites))


if __name__ == "__main__":
    print(
        {
            "monomer_margin_squared": monomer_centroid_certificate(),
            "dimer_margin_squared": dimer_center_certificate(),
        }
    )
