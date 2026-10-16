#!/usr/bin/env python3
"""Exact certificate for the centrally symmetric oblique-hexagon shear test.

For R >= 1 put

    H_R = {(i,j) in Z^2 : max(|i|, |j|, |i+j|) <= R}.

Map (i,j) to i*u+j*v, where |u|=|v|=1 and u.v=c with
0 <= c < 1/2.  The contact graph is bipartite, so the oblique image is
triangle-free.  Its exact diameter is

    diam(H_R)^2 = 8 R^2 (1-c).

At c=1/2 the same index window is the triangular-lattice hexagon, has the
same cardinality, diameter 2R, and contains unit equilateral triangles.

The script checks the finite integer identities with Fraction arithmetic.  It
does not claim that arbitrary triangle-free sources have hexagonal index
windows or that the restricted comparison solves Erdos #99.
"""

from __future__ import annotations

from fractions import Fraction


Index = tuple[int, int]


def hnorm(p: Index) -> int:
    i, j = p
    return max(abs(i), abs(j), abs(i + j))


def hex_window(radius: int) -> tuple[Index, ...]:
    return tuple(
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(-radius, radius + 1)
        if hnorm((i, j)) <= radius
    )


def qform(delta: Index, cosine: Fraction) -> Fraction:
    i, j = delta
    return i * i + j * j + 2 * cosine * i * j


def certificate(radius: int, cosine: Fraction) -> dict[str, object]:
    if radius < 1 or not (Fraction(0) <= cosine < Fraction(1, 2)):
        raise ValueError("need radius >= 1 and 0 <= cosine < 1/2")

    points = hex_window(radius)
    differences = {
        (p[0] - q[0], p[1] - q[1])
        for p in points
        for q in points
        if p != q
    }
    minimum = min(qform(delta, cosine) for delta in differences)
    maximum = max(qform(delta, cosine) for delta in differences)
    predicted = 8 * radius * radius * (1 - cosine)

    if len(points) != 1 + 3 * radius * (radius + 1):
        raise AssertionError("hexagonal cardinality identity failed")
    if minimum < 1:
        raise AssertionError("unit separation failed")
    if maximum != predicted:
        raise AssertionError((radius, cosine, maximum, predicted))

    unit_differences = {
        delta for delta in differences if qform(delta, cosine) == 1
    }
    if unit_differences != {(1, 0), (-1, 0), (0, 1), (0, -1)}:
        raise AssertionError(f"unexpected unit differences: {unit_differences}")

    equilateral_diameter_squared = 4 * radius * radius
    if predicted <= equilateral_diameter_squared:
        raise AssertionError("strict shear comparison failed")

    return {
        "radius": radius,
        "points": len(points),
        "cosine": cosine,
        "minimum_squared_distance": minimum,
        "sheared_diameter_squared": maximum,
        "equilateral_competitor_squared_diameter": equilateral_diameter_squared,
        "unit_differences": tuple(sorted(unit_differences)),
        "triangle_free": True,
    }


def main() -> None:
    cosine = Fraction(499, 1000)
    for radius in (1, 2, 3, 5, 9, 17):
        result = certificate(radius, cosine)
        print(
            "PASS R={radius} n={points} c={cosine} D_shear^2={sheared_diameter_squared} "
            "D_tri^2={equilateral_competitor_squared_diameter}".format(**result)
        )
    print("PASS: the restricted oblique-hexagon shear is globally beaten at equal cardinality")
    print("Scope: exact finite affine-window comparison only; no Level-I closure.")


if __name__ == "__main__":
    main()
