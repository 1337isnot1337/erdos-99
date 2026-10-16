#!/usr/bin/env python3
"""Exact certificate for the D6-symmetric affine-window comparison.

For c in (-1/2,1/2), let q_c(i,j)=i^2+j^2+2*c*i*j.  The map
(i,j) -> i*u+j*v with u.v=c is unit-separated.  If a finite index set S has
S-S invariant under r(i,j)=(-j,i+j), then the equilateral metric q_{1/2}
on the same indices has strictly smaller diameter.  The certificate checks
the six-orbit averaging identity and several finite orbit-closed windows with
exact Fraction arithmetic.

This is a restricted source-level comparison only.  It is not a theorem that
arbitrary C-II sources have affine D6-symmetric index sets.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Index = tuple[int, int]


def rotate(p: Index) -> Index:
    i, j = p
    return (-j, i + j)


def orbit(p: Index) -> set[Index]:
    out: set[Index] = set()
    q = p
    for _ in range(6):
        out.add(q)
        q = rotate(q)
    if q != p:
        raise AssertionError("the index rotation does not have order six")
    return out


def qform(p: Index, c: Fraction) -> Fraction:
    i, j = p
    return i * i + j * j + 2 * c * i * j


def difference_set(points: set[Index]) -> set[Index]:
    return {
        (p[0] - q[0], p[1] - q[1])
        for p in points
        for q in points
        if p != q
    }


def orbit_window(seeds: tuple[Index, ...]) -> set[Index]:
    points = {(0, 0)}
    for seed in seeds:
        points.update(orbit(seed))
    return points


def check_average_identity() -> None:
    for i, j in product(range(-7, 8), repeat=2):
        p = (i, j)
        for c in (Fraction(-49, 100), Fraction(0), Fraction(49, 100)):
            lhs = sum(qform(p, c) for p in orbit(p))
            rhs = 6 * Fraction(4 - 2 * c, 3) * qform(p, Fraction(1, 2))
            if lhs != rhs:
                raise AssertionError((p, c, lhs, rhs))


def check_window(points: set[Index], c: Fraction) -> dict[str, Fraction | int]:
    if len(points) < 2:
        raise AssertionError("comparison needs at least two points")
    if not (-Fraction(1, 2) < c < Fraction(1, 2)):
        raise ValueError("the strict triangle-free affine range is required")
    differences = difference_set(points)
    if difference_set({rotate(p) for p in points}) != differences:
        raise AssertionError("the difference set is not rotation invariant")
    minimum = min(qform(p, c) for p in differences)
    if minimum < 1:
        raise AssertionError(("unit separation", c, minimum))
    sheared = max(qform(p, c) for p in differences)
    equilateral = max(qform(p, Fraction(1, 2)) for p in differences)
    lam = Fraction(4 - 2 * c, 3)
    if sheared < lam * equilateral:
        raise AssertionError(("averaged diameter bound", c, sheared, lam, equilateral))
    if not equilateral < sheared:
        raise AssertionError(("strict comparison", c, sheared, equilateral))
    return {
        "points": len(points),
        "minimum": minimum,
        "sheared": sheared,
        "equilateral": equilateral,
        "lambda": lam,
    }


def main() -> None:
    check_average_identity()
    windows = (
        orbit_window(((1, 0),)),
        orbit_window(((1, 0), (2, 1))),
        orbit_window(((2, -1), (3, 1))),
    )
    for idx, points in enumerate(windows, start=1):
        for c in (Fraction(-49, 100), Fraction(0), Fraction(49, 100)):
            result = check_window(points, c)
            print(
                "PASS window={idx} c={c} n={points} min_q={minimum} "
                "D_shear^2={sheared} D_equilateral^2={equilateral} lambda={lambda}".format(
                    idx=idx, c=c, **result
                )
            )
    print("PASS: six-orbit average and strict same-cardinality comparison")
    print("Scope: finite D6-symmetric affine windows; no Level-I closure.")


if __name__ == "__main__":
    main()
