"""Exact activation-forest/monomer-scaffold regression.

The construction in this module is deliberately finite and rational. It combines
three structures on one point set:

* a fixed diameter pair;
* a one-point-at-a-time activation sequence whose new unit edges form many paths;
* a degree-three monomer conflict presentation with a matching saturating every
  activated point.

It is not a global best-packing construction. Its purpose is to test claims that
activation-forest rank plus local scaffold geometry alone forces Hall nullity.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import floor
from typing import Iterator


Coord = tuple[Fraction, Fraction]
Label = tuple[str, int, int]

ALPHA = Fraction(1, 20)
ETA = Fraction(1, 100)


def qnorm2(vector: Coord) -> Fraction:
    """Squared Euclidean norm in the 60-degree lattice basis."""

    x, y = vector
    return x * x + x * y + y * y


def distance2(first: Coord, second: Coord) -> Fraction:
    return qnorm2((first[0] - second[0], first[1] - second[1]))


def activation_order(side: int) -> tuple[Label, ...]:
    """Move each row from left to right, omitting its stationary first point."""

    if side < 2:
        raise ValueError("side must be at least two")
    return tuple(("p", i, j) for j in range(side) for i in range(1, side))


def points_at_step(side: int, completed_steps: int) -> dict[Label, Coord]:
    """Return the exact configuration after ``completed_steps`` activations."""

    order = activation_order(side)
    if not 0 <= completed_steps <= len(order):
        raise ValueError("completed_steps is outside the activation sequence")
    activated = set(order[:completed_steps])
    scale = Fraction(1) + ALPHA / side
    points: dict[Label, Coord] = {
        ("anchor", -1, 0): (Fraction(-4 * side), Fraction(0)),
        ("anchor", 1, 0): (Fraction(4 * side), Fraction(0)),
    }
    for j in range(side):
        for i in range(side):
            label = ("p", i, j)
            shift = Fraction(0)
            if i > 0 and label not in activated:
                shift = ETA * i / (side * side)
            points[label] = (
                Fraction(i) + Fraction(1, 3) + shift,
                scale * j + Fraction(1, 3),
            )
    return points


def active_pairs(points: dict[Label, Coord], side: int) -> frozenset[tuple[Label, Label]]:
    """Return all unit and fixed-diameter pairs in a sequence state."""

    diameter2 = Fraction(64 * side * side)
    out: set[tuple[Label, Label]] = set()
    for first, second in combinations(sorted(points), 2):
        d2 = distance2(points[first], points[second])
        if d2 == 1 or d2 == diameter2:
            out.add((first, second))
    return frozenset(out)


def unit_pairs(points: dict[Label, Coord]) -> frozenset[tuple[Label, Label]]:
    out: set[tuple[Label, Label]] = set()
    for first, second in combinations(sorted(points), 2):
        if distance2(points[first], points[second]) == 1:
            out.add((first, second))
    return frozenset(out)


def declared_monomer_vertices(i: int, j: int) -> frozenset[tuple[int, int]]:
    return frozenset({(i, j), (i + 1, j), (i, j + 1)})


def lattice_conflict_neighborhood(point: Coord) -> frozenset[tuple[int, int]]:
    """Enumerate all triangular-lattice sites strictly within unit distance."""

    x0, y0 = point
    # A unit conflict must lie within two coefficient units in both coordinates.
    x_floor = floor(x0)
    y_floor = floor(y0)
    return frozenset(
        (i, j)
        for i in range(x_floor - 2, x_floor + 3)
        for j in range(y_floor - 2, y_floor + 3)
        if qnorm2((x0 - i, y0 - j)) < 1
    )


def final_patch(side: int) -> dict[Label, Coord]:
    return points_at_step(side, len(activation_order(side)))


def natural_scaffold_matching(side: int) -> dict[Label, tuple[int, int]]:
    """Match every patch point to the lower-left vertex of its monomer cell."""

    return {("p", i, j): (i, j) for j in range(side) for i in range(side)}


def sequence_states(side: int) -> Iterator[dict[Label, Coord]]:
    for completed in range(len(activation_order(side)) + 1):
        yield points_at_step(side, completed)


if __name__ == "__main__":
    for side in (2, 4, 8, 16):
        final = final_patch(side)
        print(
            f"side={side} diameter={8 * side} "
            f"activation_edges={len(unit_pairs(final))} "
            f"matched={len(natural_scaffold_matching(side))}"
        )
