"""Exact geometric predicates for one-point unit-contact escape tests.

The distinction between an *open* and a *closed* semicircle matters. A strict
first-order escape exists when all active contact normals fit in an open
semicircle. A nontrivial finite one-point motion already exists when they fit in
a closed semicircle: contacts with zero first derivative open quadratically.
Consequently local isolation by unit contacts occurs only when the contact
directions do not fit in any closed semicircle.
"""

from __future__ import annotations

import math
from collections.abc import Sequence


Point = tuple[float, float]


def _angles(vectors: Sequence[Point]) -> list[float]:
    return sorted(math.atan2(y, x) % (2.0 * math.pi) for x, y in vectors)


def _largest_gap(vectors: Sequence[Point]) -> float:
    if len(vectors) <= 1:
        return 2.0 * math.pi
    angles = _angles(vectors)
    return max(
        (angles[(i + 1) % len(angles)] - angles[i]) % (2.0 * math.pi)
        for i in range(len(angles))
    )


def fits_open_semicircle(vectors: Sequence[Point], tol: float = 1e-8) -> bool:
    """Whether one direction has strictly positive dot product with every vector."""
    return _largest_gap(vectors) > math.pi + tol


def fits_closed_semicircle(vectors: Sequence[Point], tol: float = 1e-8) -> bool:
    """Whether the directions fit in some closed semicircle.

    For unit-contact vectors this is the exact local one-point feasibility test
    when all other points are fixed and no upper-diameter constraints are active.
    If the supporting direction has zero dot product with a contact normal, the
    squared distance still increases by the positive quadratic term.
    """
    return _largest_gap(vectors) >= math.pi - tol


def locally_isolated_by_unit_contacts(
    vectors: Sequence[Point], tol: float = 1e-8
) -> bool:
    """Whether the fixed-neighbor unit-contact slice is locally isolated."""
    return not fits_closed_semicircle(vectors, tol=tol)
