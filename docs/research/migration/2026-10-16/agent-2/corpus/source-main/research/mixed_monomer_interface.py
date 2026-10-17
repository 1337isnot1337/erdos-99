"""Exact local compatibility certificate for opposite monomer cells.

The triangular-lattice scaffold has two orientations of elementary monomer
triangle.  This module records an explicit one-parameter family of blockers in
two edge-sharing triangles.  It is a small but useful no-go test: cell
interior-disjointness and unit separation of the blockers do not, by
themselves, force a single orientation at a mixed interface.

Coordinates use a 60-degree lattice basis, so

    |a e1 + b e2|^2 = a^2 + a*b + b^2.

All calculations are exact.  The finite lattice shell used below is certified
to be complete by the reverse-triangle estimate in the accompanying report:
for a point at oblique distance less than ``sqrt(3)/2`` from a lattice site,
every other lattice site of squared norm at least four is more than one away.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from typing import Iterable


ObliquePoint = tuple[Fraction, Fraction]
LatticePoint = tuple[int, int]
TaggedBlocker = tuple[str, int, int, ObliquePoint]


def _point(value: Iterable[int | Fraction]) -> ObliquePoint:
    first, second = value
    return Fraction(first), Fraction(second)


def triangular_distance_squared(
    first: ObliquePoint, second: ObliquePoint
) -> Fraction:
    """Return exact squared Euclidean distance in the triangular basis."""

    first_delta = first[0] - second[0]
    second_delta = first[1] - second[1]
    return (
        first_delta * first_delta
        + first_delta * second_delta
        + second_delta * second_delta
    )


def plus_triangle() -> tuple[ObliquePoint, ...]:
    """Return the lower-left elementary triangle."""

    return tuple(_point(vertex) for vertex in ((0, 0), (1, 0), (0, 1)))


def minus_triangle() -> tuple[ObliquePoint, ...]:
    """Return the edge-sharing opposite-orientation triangle."""

    return tuple(_point(vertex) for vertex in ((1, 0), (0, 1), (1, 1)))


def mixed_blocker_pair(parameter: Fraction) -> tuple[ObliquePoint, ObliquePoint]:
    """Return the exact pair ``p_t=((t,t), (1-t,1-t))``."""

    t = Fraction(parameter)
    if not (0 < t < Fraction(1, 2)):
        raise ValueError("the parameter must lie strictly between zero and one-half")
    return _point((t, t)), _point((1 - t, 1 - t))


def monomer_vertex_maximum_squared(parameter: Fraction) -> Fraction:
    """Return the largest own-cell vertex distance squared for the pair."""

    t = Fraction(parameter)
    if not (0 < t < Fraction(1, 2)):
        raise ValueError("the parameter must lie strictly between zero and one-half")
    return 1 - 3 * t + 3 * t * t


def mixed_blocker_separation_squared(parameter: Fraction) -> Fraction:
    """Return the squared distance between the two mixed blockers."""

    t = Fraction(parameter)
    if not (0 < t < Fraction(1, 2)):
        raise ValueError("the parameter must lie strictly between zero and one-half")
    return 3 * (1 - 2 * t) ** 2


def _lattice_shell(maximum_squared_norm: int = 3) -> tuple[LatticePoint, ...]:
    """Enumerate lattice vectors with squared norm at most the shell bound."""

    if maximum_squared_norm < 0:
        raise ValueError("the shell bound must be nonnegative")
    # The displayed range contains every vector with Q <= 3.  Keeping the
    # bound explicit makes the exact finite certificate easy to audit.
    return tuple(
        (first, second)
        for first in range(-3, 4)
        for second in range(-3, 4)
        if (
            first * first + first * second + second * second
            <= maximum_squared_norm
        )
    )


def certified_conflict_neighborhood(
    point: ObliquePoint, anchor: LatticePoint
) -> frozenset[LatticePoint]:
    """Return the complete strict unit neighborhood of a certified point.

    The caller supplies one lattice anchor.  This routine is used for the
    points ``(t,t)`` near ``(0,0)`` and ``(1-t,1-t)`` near ``(1,1)``.  For the
    admissible parameter range, the reverse-triangle estimate proves that no
    lattice vector outside the Q <= 3 shell can be a strict conflict.
    """

    anchor_point = _point(anchor)
    anchor_offset_squared = triangular_distance_squared(point, anchor_point)
    if not anchor_offset_squared < Fraction(3, 4):
        raise ValueError("the point is outside the certified shell regime")
    return frozenset(
        (anchor[0] + first, anchor[1] + second)
        for first, second in _lattice_shell()
        if triangular_distance_squared(
            point,
            _point((anchor[0] + first, anchor[1] + second)),
        )
        < 1
    )


def mixed_monomer_certificate(parameter: Fraction) -> dict[str, object]:
    """Return exact checks for the adjacent mixed-monomer configuration."""

    t = Fraction(parameter)
    plus_blocker, minus_blocker = mixed_blocker_pair(t)
    plus_neighborhood = certified_conflict_neighborhood(plus_blocker, (0, 0))
    minus_neighborhood = certified_conflict_neighborhood(minus_blocker, (1, 1))
    return {
        "parameter": t,
        "plus_blocker": plus_blocker,
        "minus_blocker": minus_blocker,
        "plus_neighborhood": plus_neighborhood,
        "minus_neighborhood": minus_neighborhood,
        "plus_is_strictly_inside": all(
            triangular_distance_squared(plus_blocker, vertex) < 1
            for vertex in plus_triangle()
        ),
        "minus_is_strictly_inside": all(
            triangular_distance_squared(minus_blocker, vertex) < 1
            for vertex in minus_triangle()
        ),
        "own_vertex_maximum_squared": monomer_vertex_maximum_squared(t),
        "blocker_separation_squared": mixed_blocker_separation_squared(t),
        "blockers_unit_separated": (
            mixed_blocker_separation_squared(t) >= 1
        ),
    }


def diagonal_interface_blockers(
    side: int, parameter: Fraction
) -> tuple[TaggedBlocker, ...]:
    """Return a length-``side`` diagonal interface of mixed monomers.

    The plus blockers occupy the lower-left triangular index region
    ``i + j <= side - 1`` and sit near the lower-left corner of their cells.
    The minus blockers occupy the complementary upper-right region of the
    ``side`` by ``side`` index square and sit near their upper-right corners.
    The two regions share the diagonal of cells, where both orientations are
    present in different elementary triangles.
    """

    if side < 1:
        raise ValueError("the side must be positive")
    t = Fraction(parameter)
    # Validate the parameter through the pair constructor before translating
    # the local pattern across the lattice.
    mixed_blocker_pair(t)
    blockers: list[TaggedBlocker] = []
    for i in range(side):
        for j in range(side - i):
            blockers.append(("+", i, j, _point((i + t, j + t))))
    for i in range(side):
        for j in range(side):
            if i + j >= side - 1:
                blockers.append(("-", i, j, _point((i + 1 - t, j + 1 - t))))
    return tuple(blockers)


def diagonal_interface_expected_neighborhood(
    blocker: TaggedBlocker,
) -> frozenset[LatticePoint]:
    """Return the declared three-site neighborhood of an interface blocker."""

    orientation, i, j, _ = blocker
    if orientation == "+":
        return frozenset({(i, j), (i + 1, j), (i, j + 1)})
    if orientation == "-":
        return frozenset({(i + 1, j), (i, j + 1), (i + 1, j + 1)})
    raise ValueError("orientation must be '+' or '-'")


def diagonal_interface_matching_vertices(
    side: int, parameter: Fraction
) -> tuple[tuple[TaggedBlocker, LatticePoint], ...]:
    """Return an explicit injective cell-to-vertex matching.

    A plus cell is matched to its lower-left vertex and a minus cell to its
    upper-right vertex.  The coordinate-sum separation of these two vertex
    classes makes injectivity immediate.
    """

    blockers = diagonal_interface_blockers(side, parameter)
    return tuple(
        (
            blocker,
            (blocker[1], blocker[2])
            if blocker[0] == "+"
            else (blocker[1] + 1, blocker[2] + 1),
        )
        for blocker in blockers
    )


def diagonal_interface_matching_is_injective(
    side: int, parameter: Fraction
) -> bool:
    """Check that the explicit matching saturates every selected cell."""

    assignments = diagonal_interface_matching_vertices(side, parameter)
    return (
        len({vertex for _, vertex in assignments}) == len(assignments)
        and all(
            vertex in diagonal_interface_expected_neighborhood(blocker)
            for blocker, vertex in assignments
        )
    )


def subhalf_anchor_hall_bound(
    blockers: Iterable[tuple[ObliquePoint, Iterable[LatticePoint]]],
) -> dict[str, object]:
    """Bound left Hall deficiency by blockers without a sub-half anchor.

    The supplied lattice neighborhoods must be complete strict conflict
    neighborhoods. A blocker with a neighborhood site at squared distance
    below 1/4 is assigned that site. Unit separation makes all such
    assignments injective, so only the remaining blockers can contribute to
    a positive Hall deficiency.
    """

    normalized = tuple(
        (point, tuple(sorted(set(neighborhood))))
        for point, neighborhood in blockers
    )
    if any(
        triangular_distance_squared(first[0], second[0]) < 1
        for first, second in combinations(normalized, 2)
    ):
        raise ValueError("blockers must be unit-separated")
    short_anchors = tuple(
        tuple(
            vertex
            for vertex in neighborhood
            if triangular_distance_squared(point, _point(vertex))
            < Fraction(1, 4)
        )
        for point, neighborhood in normalized
    )
    if any(len(anchors) > 1 for anchors in short_anchors):
        raise AssertionError("a point has two lattice sites within one-half")
    selected_anchors = tuple(
        anchors[0] for anchors in short_anchors if anchors
    )
    if len(set(selected_anchors)) != len(selected_anchors):
        raise AssertionError("unit-separated blockers share a sub-half anchor")
    central_count = sum(not anchors for anchors in short_anchors)
    return {
        "blocker_count": len(normalized),
        "noncentral_count": len(selected_anchors),
        "central_count": central_count,
        "anchor_assignment_injective": True,
        "hall_deficiency_upper_bound": central_count,
        "short_anchors": short_anchors,
    }


def diagonal_interface_is_unit_separated(
    side: int, parameter: Fraction
) -> bool:
    """Check exact pairwise unit separation for the diagonal interface."""

    blockers = diagonal_interface_blockers(side, parameter)
    return all(
        triangular_distance_squared(first[3], second[3]) >= 1
        for first, second in combinations(blockers, 2)
    )


def diagonal_interface_certificate(
    side: int, parameter: Fraction
) -> dict[str, object]:
    """Return exact checks for the arbitrary-length mixed interface."""

    blockers = diagonal_interface_blockers(side, parameter)
    neighborhoods = tuple(
        certified_conflict_neighborhood(
            blocker[3],
            (blocker[1], blocker[2])
            if blocker[0] == "+"
            else (blocker[1] + 1, blocker[2] + 1),
        )
        for blocker in blockers
    )
    expected = tuple(
        diagonal_interface_expected_neighborhood(blocker)
        for blocker in blockers
    )
    anchor_bound = subhalf_anchor_hall_bound(
        tuple(
            (blocker[3], neighborhood)
            for blocker, neighborhood in zip(blockers, neighborhoods)
        )
    )
    matching = diagonal_interface_matching_vertices(side, parameter)
    return {
        "side": side,
        "parameter": Fraction(parameter),
        "blocker_count": len(blockers),
        "expected_blocker_count": side * (side + 1),
        "lattice_vertex_count": (side + 1) ** 2,
        "raw_incidence_deficiency": len(blockers) - (side + 1) ** 2,
        "unit_separated": diagonal_interface_is_unit_separated(side, parameter),
        "complete_neighborhoods": neighborhoods == expected,
        "matching_saturates_cells": diagonal_interface_matching_is_injective(
            side, parameter
        ),
        "subhalf_anchor_bound": anchor_bound,
        "matching": matching,
        "blockers": blockers,
        "neighborhoods": neighborhoods,
    }


if __name__ == "__main__":
    print(mixed_monomer_certificate(Fraction(1, 10)))
