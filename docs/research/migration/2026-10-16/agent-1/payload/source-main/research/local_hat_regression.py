"""Exact regression against a tempting but invalid fractional matching rule.

The standard piecewise-linear hat functions of the triangular lattice are not a
fractional matching certificate for unit-separated points.  This is a local
geometry warning: the conflict graph of the points below is still matchable, but
the naive rule that assigns barycentric mass to the vertices of a single chosen
triangle overloads the central vertex.
"""

from __future__ import annotations

from fractions import Fraction
from math import sqrt


def alternating_ray_radius() -> Fraction:
    """Return an exact radius in the strict counterexample interval."""

    # 3/5 lies strictly between 1/sqrt(3) and 2/3.  The comparisons
    # are checked by squaring positive quantities in the tests.
    return Fraction(3, 5)


def pairwise_distance(radius: Fraction) -> float:
    """Distance between alternating 120-degree points of the given radius."""

    return sqrt(3.0) * float(radius)


def pairwise_distance_squared(radius: Fraction) -> Fraction:
    """Exact squared distance between alternating 120-degree points."""

    return 3 * radius * radius


def central_hat_mass(radius: Fraction) -> Fraction:
    """Total central barycentric mass for the three alternating ray points."""

    return 3 * (1 - radius)


def is_triangle_free(radius: Fraction) -> bool:
    """The three-point configuration has no unit equilateral triangle."""

    # Its only three pairwise distances are sqrt(3)*radius, and the chosen
    # interval is strict above 1/sqrt(3), so all three distances exceed one.
    return pairwise_distance_squared(radius) > 1


def regression_summary() -> dict[str, Fraction | float | bool]:
    radius = alternating_ray_radius()
    return {
        "radius": radius,
        "pairwise_distance": pairwise_distance(radius),
        "central_hat_mass": central_hat_mass(radius),
        "unit_separated": is_triangle_free(radius),
        "triangle_free": is_triangle_free(radius),
        "hat_overload": central_hat_mass(radius) > 1,
    }


if __name__ == "__main__":
    print(regression_summary())
