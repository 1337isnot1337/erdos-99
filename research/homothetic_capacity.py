"""Exact finite capacity calculations for a strained triangular-lattice patch.

The geometric statement audited in canonical Section 141 only uses the quadratic
form of the triangular lattice. Keeping the strain as a Fraction makes the
number of extra lattice layers exact and avoids a floating-point floor error.
"""

from __future__ import annotations

from fractions import Fraction


def extra_layers(side: int, strain: Fraction) -> int:
    """Return the number of complete lattice layers exposed by the strain.

    The original patch has lattice indices 0 through side - 1. Its homothetic
    hull has coordinate extent (1 + strain) * (side - 1). Therefore the
    largest new integer index is side - 1 + floor(strain * (side - 1)).
    """

    if side < 2:
        raise ValueError("side must be at least 2")
    if strain <= 0:
        raise ValueError("strain must be positive")
    return int(strain * (side - 1))


def original_size(side: int) -> int:
    """Return the number of points in the unstrained square-index patch."""

    if side < 2:
        raise ValueError("side must be at least 2")
    return side * side


def candidate_size(side: int, strain: Fraction) -> int:
    """Return the size of the maximal square-index lattice candidate."""

    return (side + extra_layers(side, strain)) ** 2


def candidate_diameter_squared(side: int, strain: Fraction) -> Fraction:
    """Return the squared diameter of the square-index candidate."""

    layers = extra_layers(side, strain)
    return Fraction(3 * (side + layers - 1) ** 2)


def strained_diameter_squared(side: int, strain: Fraction) -> Fraction:
    """Return the squared diameter of the homothetically strained patch."""

    if side < 2:
        raise ValueError("side must be at least 2")
    if strain <= 0:
        raise ValueError("strain must be positive")
    return 3 * (1 + strain) ** 2 * (side - 1) ** 2


def candidate_fits(side: int, strain: Fraction) -> bool:
    """Check the exact hull containment inequality for the candidate."""

    return candidate_diameter_squared(side, strain) <= strained_diameter_squared(
        side, strain
    )
