#!/usr/bin/env python3
"""Small exact-in-the-combinatorics capacity-flag regression harness.

This file deliberately separates the metric input from the matroid calculation
used in Target A.  A *left* shore is a capacity-endpoint set X and a *right*
shore is a smaller packing B.  A cross edge means strict conflict (distance < 1).
The script computes a maximum matching, fundamental circuits of the non-basis
left vertices, and the adjacent-cardinality exchange flag

    P_i = (B \\ W_i) union U_i.

The geometric checks are numerical diagnostics only; the matching and cardinality
identities are integer-exact once the strict-conflict graph has been supplied.
It is intended as a compact regression tool for the v1.7 source-capacity lemmas,
not as a global optimizer or a proof of Erdős Problem #99.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import itertools
import json
import math
from typing import Iterable, Sequence


Point = tuple[float, float]


def dist2(a: Point, b: Point) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def unit_separated(points: Sequence[Point], tol: float = 1e-9) -> bool:
    return all(dist2(a, b) >= 1.0 - tol for a, b in itertools.combinations(points, 2))


def unit_triangles(points: Sequence[Point], tol: float = 1e-8) -> list[tuple[int, int, int]]:
    triangles: list[tuple[int, int, int]] = []
    for i, j, k in itertools.combinations(range(len(points)), 3):
        sides = (dist2(points[i], points[j]), dist2(points[i], points[k]), dist2(points[j], points[k]))
        if max(abs(side - 1.0) for side in sides) <= tol:
            triangles.append((i, j, k))
    return triangles


def regular_hexagon(radius: float = 1.0) -> list[Point]:
    return [
        (radius * math.cos(k * math.pi / 3.0), radius * math.sin(k * math.pi / 3.0))
        for k in range(6)
    ]


def one_point_escape_vectors(
    index: int,
    points: Sequence[Point],
    diameter: float | None = None,
    tol: float = 1e-8,
) -> list[Point]:
    """Active one-point vectors for the strict escape test.

    For a unit contact xy, the vector x-y points toward increasing separation
    when x is moved.  For a diameter pair xy, the vector y-x points toward
    decreasing separation.  A common strict positive dot product with all
    returned vectors is exactly the one-point perturbation criterion.
    """
    x = points[index]
    vectors: list[Point] = []
    for j, y in enumerate(points):
        if j == index:
            continue
        squared = dist2(x, y)
        if abs(squared - 1.0) <= tol:
            vectors.append((x[0] - y[0], x[1] - y[1]))
        elif diameter is not None and abs(math.sqrt(squared) - diameter) <= tol:
            vectors.append((y[0] - x[0], y[1] - x[1]))
    return vectors


def fits_open_semicircle(vectors: Sequence[Point], tol: float = 1e-8) -> bool:
    """Whether some direction has positive dot product with every vector."""
    if not vectors:
        return True
    angles = sorted(math.atan2(y, x) % (2.0 * math.pi) for x, y in vectors)
    gaps = [
        (angles[(i + 1) % len(angles)] - angles[i]) % (2.0 * math.pi)
        for i in range(len(angles))
    ]
    # The vectors fit in an open semicircle iff the complementary circular gap
    # is strictly larger than pi.
    return max(gaps) > math.pi + tol


def strict_conflicts(left: Sequence[Point], right: Sequence[Point], tol: float = 1e-9) -> list[list[int]]:
    """Return right-neighbor indices for every left vertex."""
    threshold = 1.0 - tol
    return [
        [j for j, q in enumerate(right) if dist2(p, q) < threshold * threshold]
        for p in left
    ]


@dataclass(frozen=True)
class Matching:
    """A left-to-right matching, represented by matched right indices."""

    left_to_right: tuple[int | None, ...]

    @property
    def size(self) -> int:
        return sum(value is not None for value in self.left_to_right)


def maximum_matching(neighbors: Sequence[Sequence[int]], right_size: int) -> Matching:
    """Kuhn augmenting-path algorithm, deterministic under ordered neighbors."""
    right_to_left: list[int | None] = [None] * right_size

    def augment(left: int, seen: list[bool]) -> bool:
        for right in neighbors[left]:
            if seen[right]:
                continue
            seen[right] = True
            owner = right_to_left[right]
            if owner is None or augment(owner, seen):
                right_to_left[right] = left
                return True
        return False

    for left in range(len(neighbors)):
        augment(left, [False] * right_size)

    left_to_right: list[int | None] = [None] * len(neighbors)
    for right, left in enumerate(right_to_left):
        if left is not None:
            left_to_right[left] = right
    return Matching(tuple(left_to_right))


def neighborhood(left_indices: Iterable[int], neighbors: Sequence[Sequence[int]]) -> set[int]:
    result: set[int] = set()
    for left in left_indices:
        result.update(neighbors[left])
    return result


def fundamental_circuit(
    nonbasis_left: int,
    neighbors: Sequence[Sequence[int]],
    matching: Matching,
) -> tuple[int, ...]:
    """Compute the fundamental circuit of a nonbasis left vertex.

    The alternating search starts at the nonbasis vertex, follows every edge to a
    right vertex, and then follows the chosen matching edge back to its basis
    owner.  For a nonbasis vertex in a maximum basis, the reachable left set is
    the unique fundamental circuit support.
    """
    right_to_left = {
        right: left
        for left, right in enumerate(matching.left_to_right)
        if right is not None
    }
    seen_left = {nonbasis_left}
    seen_right: set[int] = set()
    frontier = [nonbasis_left]
    while frontier:
        left = frontier.pop()
        for right in neighbors[left]:
            if right in seen_right:
                continue
            seen_right.add(right)
            owner = right_to_left.get(right)
            if owner is not None and owner not in seen_left:
                seen_left.add(owner)
                frontier.append(owner)
    return tuple(sorted(seen_left))


def exchange_flag(
    basis_points: Sequence[Point],
    capacity_points: Sequence[Point],
    tol: float = 1e-9,
) -> dict:
    """Build the capacity flag from a basis of the capacity endpoint.

    ``basis_points`` is the right shore B. ``capacity_points`` is X.  The maximum
    matching is computed from X to B.  The matched capacity vertices form the
    basis, and the unmatched vertices are ordered by index.
    """
    neighbors = strict_conflicts(capacity_points, basis_points, tol=tol)
    matching = maximum_matching(neighbors, len(basis_points))
    if matching.size < len(basis_points):
        raise ValueError("capacity endpoint does not match the supplied basis shore")

    matched = [i for i, right in enumerate(matching.left_to_right) if right is not None]
    nonbasis = [i for i, right in enumerate(matching.left_to_right) if right is None]
    circuits = {
        left: fundamental_circuit(
            nonbasis_left=left,
            neighbors=neighbors,
            matching=matching,
        )
        for left in nonbasis
    }

    flags = []
    U: set[int] = set()
    previous_W: set[int] = set()
    previous_U: set[int] = set()
    for step, left in enumerate(nonbasis, start=1):
        # U is represented in the disjoint union X: capacity vertices are the
        # nonbasis vertices plus the matched basis vertices in the circuit.
        circuit = set(circuits[left])
        U.update(circuit)
        W = neighborhood(U, neighbors)
        # The exchanged packing is the unconflicted part of B plus U.
        P_right = sorted(set(range(len(basis_points))) - W)
        P_points = [basis_points[i] for i in P_right] + [capacity_points[i] for i in U]
        flags.append(
            {
                "step": step,
                "nonbasis_vertex": left,
                "circuit": sorted(circuit),
                "U_size": len(U),
                "W_size": len(W),
                "net_surplus": len(U) - len(W),
                "new_U": len(U - previous_U),
                "new_W": len(W - previous_W),
                "right_indices": P_right,
                "left_indices": sorted(U),
                "configuration_size": len(P_points),
                "unit_separated": unit_separated(P_points, tol=tol),
                "unit_triangles": unit_triangles(P_points, tol=tol),
            }
        )
        previous_W = W
        previous_U = set(U)

    return {
        "left_size": len(capacity_points),
        "right_size": len(basis_points),
        "matching_size": matching.size,
        "matched_left": matched,
        "nonbasis_left": nonbasis,
        "circuits": {str(k): list(v) for k, v in circuits.items()},
        "flags": flags,
    }


def assert_flag_invariants(
    basis_points: Sequence[Point],
    capacity_points: Sequence[Point],
    flag: dict,
) -> None:
    """Assert the cardinality and packing identities used by the regression.

    These checks deliberately stay finite and exact once the conflict graph is
    fixed: every appended fundamental circuit contributes one more left vertex
    than its newly exposed right neighborhood in the examples below.
    """
    right_size = len(basis_points)
    assert flag["right_size"] == right_size
    assert flag["matching_size"] == right_size
    assert len(flag["nonbasis_left"]) == len(capacity_points) - right_size
    for expected_step, record in enumerate(flag["flags"], start=1):
        assert record["step"] == expected_step
        assert record["net_surplus"] == expected_step
        assert record["configuration_size"] == right_size + expected_step
        assert record["unit_separated"]


def square_grid(side: int) -> list[Point]:
    return [(float(i), float(j)) for i in range(side + 1) for j in range(side + 1)]


def triangular_points_in_box(width: float, height: float) -> list[Point]:
    """Unit triangular-lattice points in [0,width] x [0,height]."""
    h = math.sqrt(3.0) / 2.0
    points: list[Point] = []
    for j in range(math.floor(height / h) + 1):
        y = j * h
        offset = 0.5 * (j % 2)
        for i in range(math.floor(width - offset) + 1):
            x = i + offset
            if x <= width + 1e-9:
                points.append((x, y))
    return points


def triangular_lattice_coordinate(i: int, j: int) -> Point:
    return (float(i) + 0.5 * float(j), math.sqrt(3.0) * 0.5 * float(j))


def strained_patch(side: int, alpha: float) -> tuple[list[Point], list[Point]]:
    """Return a scaled triangle-lattice patch and its unscaled comparison patch."""
    scale = 1.0 + alpha / side
    sites = [triangular_lattice_coordinate(i, j) for i in range(side) for j in range(side)]
    strained = [(scale * x, scale * y) for x, y in sites]
    return strained, sites


def strain_regression(side: int = 8, alpha: float = 0.25) -> dict:
    """Measure the exact identity matching in a distributed-strain patch.

    The identity pairing is a strict-conflict matching whenever the scaled point
    remains within distance one of its unscaled counterpart.  The returned Hall
    deficiency is the left-shore deficiency ``|X|-nu``.  This is a local scaffold
    regression, not a finite-container capacity or global-optimality certificate.
    """
    strained, lattice = strained_patch(side, alpha)
    equal_flag = exchange_flag(strained, lattice)
    assert_flag_invariants(strained, lattice, equal_flag)
    extra_lattice = lattice + [triangular_lattice_coordinate(side, 0)]
    extra_flag = exchange_flag(strained, extra_lattice)
    assert_flag_invariants(strained, extra_lattice, extra_flag)
    return {
        "side": side,
        "alpha": alpha,
        "scale": 1.0 + alpha / side,
        "strained_points": len(strained),
        "lattice_points": len(lattice),
        "strained_unit_triangles": len(unit_triangles(strained)),
        "lattice_unit_triangles": len(unit_triangles(lattice)),
        "equal_shore_matching": equal_flag["matching_size"],
        "equal_shore_hall_deficiency": len(lattice) - equal_flag["matching_size"],
        "one_extra_shore_matching": extra_flag["matching_size"],
        "one_extra_shore_hall_deficiency": len(extra_lattice) - extra_flag["matching_size"],
    }


def demo() -> dict:
    """Return two small regression cases.

    Case ``square`` has no unit triangles on either shore.  Case ``mixed`` uses a
    triangle-free subconfiguration of a small triangular-lattice comparison shore,
    so the flag exposes a first triangle transition.  The second shore is
    deliberately called a comparison shore: its container capacity is not
    certified here.  These are finite-container diagnostics, not claims about D(n).
    """
    source = square_grid(2)
    comparison = triangular_points_in_box(2.0, 2.0)
    mixed_source = [comparison[i] for i in (0, 2, 3, 4, 5, 7)]
    mixed_capacity = comparison
    mixed_flag = exchange_flag(mixed_source, mixed_capacity)
    assert_flag_invariants(mixed_source, mixed_capacity, mixed_flag)
    hexagon = regular_hexagon()
    hex_endpoint = [(0.0, 0.0)] + hexagon
    hex_flag = exchange_flag(hexagon, hex_endpoint)
    assert_flag_invariants(hexagon, hex_endpoint, hex_flag)
    center_vectors = one_point_escape_vectors(0, hex_endpoint, diameter=2.0)
    return {
        "square": {
            "source_points": len(source),
            "source_unit_separated": unit_separated(source),
            "source_unit_triangles": unit_triangles(source),
            "comparison_points": len(source),
            "comparison_unit_triangles": unit_triangles(source),
        },
        "mixed": {
            "source_points": len(mixed_source),
            "source_unit_separated": unit_separated(mixed_source),
            "source_unit_triangles": unit_triangles(mixed_source),
            "comparison_points": len(mixed_capacity),
            "comparison_unit_separated": unit_separated(mixed_capacity),
            "comparison_unit_triangles": unit_triangles(mixed_capacity),
            "flag": mixed_flag,
        },
        "hexagon_center": {
            "source_points": len(hexagon),
            "source_unit_separated": unit_separated(hexagon),
            "source_unit_triangles": unit_triangles(hexagon),
            "capacity_points": len(hex_endpoint),
            "capacity_unit_separated": unit_separated(hex_endpoint),
            "capacity_unit_triangles": unit_triangles(hex_endpoint),
            "flag": hex_flag,
            "center_active_vector_count": len(center_vectors),
            "center_has_strict_one_point_escape": fits_open_semicircle(center_vectors),
        },
        "distributed_strain": strain_regression(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="print finite geometry regressions as JSON")
    args = parser.parse_args()
    if args.demo:
        print(json.dumps(demo(), indent=2, sort_keys=True))
    else:
        parser.error("pass --demo")


if __name__ == "__main__":
    main()
