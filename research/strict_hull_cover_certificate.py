"""Exact strict covering certificates for nonuniform triangular cells.

For a cell with side gaps a and b in two unit directions making 60 degrees,
the short diagonal has squared length a*a - a*b + b*b. When this value is
strictly below three, both triangles obtained by cutting along that diagonal
are covered by open unit disks at their vertices. The strictness is strong
enough to cover the closed cell, including its boundary.

This module is deliberately independent of the capacity module. It records the
quantifier upgrade as a small exact research certificate.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable


Scalar = int | Fraction


def short_diagonal_squared(first_gap: Scalar, second_gap: Scalar) -> Fraction:
    """Return the squared short diagonal in the 60-degree coordinate metric."""

    first = Fraction(first_gap)
    second = Fraction(second_gap)
    if first < 1 or second < 1:
        raise ValueError("cell side gaps must be at least one")
    return first * first - first * second + second * second


def strict_cell_cover_margin(first_gap: Scalar, second_gap: Scalar) -> Fraction:
    """Return the exact margin in the sufficient strict-cover threshold."""

    return Fraction(3) - short_diagonal_squared(first_gap, second_gap)


def strictly_covers_closed_cell(first_gap: Scalar, second_gap: Scalar) -> bool:
    """Whether the open unit disks at the four corners cover the closed cell."""

    return strict_cell_cover_margin(first_gap, second_gap) > 0


def strictly_covers_closed_product_hull(
    first_chain: Iterable[Scalar], second_chain: Iterable[Scalar]
) -> bool:
    """Check strict open-disk coverage of a complete closed product hull.

    The chains describe a finite coordinate parallelogram. Every consecutive
    gap must be at least one. The exact threshold is checked independently on
    every cell, so nonuniform strain is allowed.
    """

    first = tuple(Fraction(value) for value in first_chain)
    second = tuple(Fraction(value) for value in second_chain)
    if len(first) < 2 or len(second) < 2:
        raise ValueError("each coordinate chain needs at least two entries")
    if any(next_value <= value for value, next_value in zip(first, first[1:])):
        raise ValueError("coordinate chains must be increasing")
    if any(next_value <= value for value, next_value in zip(second, second[1:])):
        raise ValueError("coordinate chains must be increasing")
    if any(
        next_value - value < 1 for value, next_value in zip(first, first[1:])
    ):
        raise ValueError("first coordinate gaps must be at least one")
    if any(
        next_value - value < 1 for value, next_value in zip(second, second[1:])
    ):
        raise ValueError("second coordinate gaps must be at least one")
    return all(
        strictly_covers_closed_cell(first_gap, second_gap)
        for first_gap in (
            first[index + 1] - first[index] for index in range(len(first) - 1)
        )
        for second_gap in (
            second[index + 1] - second[index]
            for index in range(len(second) - 1)
        )
    )
