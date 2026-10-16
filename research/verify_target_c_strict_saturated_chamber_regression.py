#!/usr/bin/env python3
"""Exact certificate for a strict, one-point-saturated chamber regression.

For an integer R >= 8, C_R is the regular triangular-lattice hexagon of
axial radius R and Z_R is the homothetic copy of the radius-(R-1) lattice
hexagon with factor h_R = 1 + R^{-2}.  The points of Z_R are all strictly
more than one apart, but their unit disks cover the one-unit erosion of C_R.

The script checks the algebraic parts of the construction with Fraction
arithmetic.  The continuum covering implication is proved in the companion
dated report using the triangular-lattice covering radius h_R/sqrt(3) < 1.
No global-minimum-diameter claim is made.
"""

from __future__ import annotations

from fractions import Fraction


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


def qform(delta: Index) -> int:
    i, j = delta
    return i * i + i * j + j * j


def pair_count(radius: int) -> int:
    """A disjoint axial (1,0)-matching in a central rectangle."""
    m = (radius - 1) // 2
    return m * (2 * m + 1)


def certificate(radius: int) -> dict[str, object]:
    if radius < 8:
        raise ValueError("need radius >= 8")

    chamber = hex_window(radius)
    source_indices = hex_window(radius - 1)
    h = Fraction(radius * radius + 1, radius * radius)

    if len(chamber) != 1 + 3 * radius * (radius + 1):
        raise AssertionError("hexagon cardinality failed")
    if len(source_indices) != 1 + 3 * (radius - 1) * radius:
        raise AssertionError("source cardinality failed")
    if not (h > 1 and h * h < 3):
        raise AssertionError("strict separation/covering-radius margin failed")

    # Every nonzero triangular-lattice difference has squared norm at least 1;
    # after the homothety every source pair is therefore strictly farther than 1.
    minimum_index_norm = min(qform((i, j)) for i, j in source_indices if (i, j) != (0, 0))
    if minimum_index_norm != 1:
        raise AssertionError("unexpected lattice minimum")
    minimum_source_squared_distance = h * h * minimum_index_norm
    if minimum_source_squared_distance <= 1:
        raise AssertionError("source is not strictly separated")

    # The homothetic radius-(R-1) hexagon lies in the radius-R chamber.
    if h * (radius - 1) >= radius:
        raise AssertionError("source escaped the chamber")

    # With a0=sqrt(3)/2, area(C_R)/a0 = 3R^2 and perimeter(C_R)/2 = 3R.
    # This is the ordinary Oler expression A/a0 + P/2 + 1 - |Z_R|.
    normalized_area = 3 * radius * radius
    half_perimeter = 3 * radius
    source_count = len(source_indices)
    oler_slack = normalized_area + half_perimeter + 1 - source_count
    if oler_slack != 6 * radius:
        raise AssertionError("Oler slack identity failed")

    # A central rectangle supplies an exact quadratic number of disjoint
    # nearest-neighbor pairs at distance h=1+R^-2.
    matching = pair_count(radius)
    if matching <= radius * radius // 16:
        raise AssertionError("matching is not quadratic")
    if h * h <= 1:
        raise AssertionError("near-pair distance is not strictly above one")

    # The triangular lattice covering radius is h/sqrt(3); the squared margin
    # below one is exact and positive.
    covering_radius_squared = h * h / 3
    if covering_radius_squared >= 1:
        raise AssertionError("one-unit erosion is not covered")

    return {
        "radius": radius,
        "scale": h,
        "source_count": source_count,
        "normalized_area": normalized_area,
        "oler_slack": oler_slack,
        "matching_count": matching,
        "covering_radius_squared": covering_radius_squared,
    }


def main() -> None:
    for radius in (8, 16, 32, 64, 128):
        result = certificate(radius)
        print(
            "PASS R={radius} h={scale} z={source_count} sigma={oler_slack} "
            "matching={matching_count} cover_radius^2={covering_radius_squared}".format(**result)
        )
    print("PASS: exact strict one-point-saturated chamber regression")
    print("Scope: fixed convex container and feasible source only; no global-optimality claim")


if __name__ == "__main__":
    main()
