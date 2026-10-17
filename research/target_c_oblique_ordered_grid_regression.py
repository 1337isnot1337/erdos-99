#!/usr/bin/env python3
"""Exact regression for carrier-only ordered-grid closure claims.

For an integer m >= 3 choose a rational unit-vector pair u,v whose angle is
just above 60 degrees.  The (m+1) by (m+1) patch

    p[i,j] = i*u + j*v

has m*m strict unit rhombi, two complete linear train families, and no unit
equilateral triangle.  The angle excess can be made O(1/m) by choosing the
rational circle parameter immediately above 1/sqrt(3).  All assertions in
this file are exact rational/integer checks; no floating-point geometry is
used.

This is a finite regression only.  The patches are not asserted to be global
minimum-diameter configurations.  Its purpose is to falsify any proposed
closure that uses only ordered-grid structure, inverse-diameter phase defect,
boundary-order interface, and near-triangular rhombic area without an
additional global-minimality theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


Index = tuple[int, int]


@dataclass(frozen=True)
class ObliqueGrid:
    """A finite patch in a rational oblique unit lattice."""

    side: int
    parameter_numerator: int
    parameter_denominator: int

    @classmethod
    def near_equilateral(cls, side: int) -> "ObliqueGrid":
        if side < 3:
            raise ValueError("side must be at least three")

        # p/q is the least rational immediately above 1/sqrt(3).  Thus
        # 3*p*p > q*q, while minimality gives 3*(p-1)^2 <= q^2.
        q = side
        p = isqrt((q * q) // 3) + 1
        while 3 * p * p <= q * q:
            p += 1
        while p > 0 and 3 * (p - 1) * (p - 1) > q * q:
            p -= 1
        # The smallest test denominator q=2 gives p=q=2, i.e. a right-angle
        # grid.  This remains a valid upper rational for 1/sqrt(3); the
        # strict p<q condition is only needed once q>=3.
        if not (0 < p <= q and 3 * (p - 1) * (p - 1) <= q * q < 3 * p * p):
            raise AssertionError("parameter was not the exact upper rational")
        return cls(side, p, q)

    @property
    def p(self) -> Fraction:
        return Fraction(self.parameter_numerator, self.parameter_denominator)

    @property
    def cosine(self) -> Fraction:
        t = self.p
        return (1 - t * t) / (1 + t * t)

    @property
    def sine(self) -> Fraction:
        t = self.p
        return 2 * t / (1 + t * t)

    @property
    def points(self) -> tuple[Index, ...]:
        return tuple(
            (i, j)
            for i in range(self.side + 1)
            for j in range(self.side + 1)
        )

    def squared_norm(self, delta: Index) -> Fraction:
        a, b = delta
        return a * a + 2 * self.cosine * a * b + b * b

    def unit_difference_indices(self) -> tuple[Index, ...]:
        m = self.side
        return tuple(
            (a, b)
            for a in range(-m, m + 1)
            for b in range(-m, m + 1)
            if (a, b) != (0, 0) and self.squared_norm((a, b)) == 1
        )

    def diameter_squared(self) -> Fraction:
        # c>0, so the farthest pair is (0,0)--(m,m).
        m = self.side
        return m * m * (2 + 2 * self.cosine)

    def interface_length(self) -> int:
        return 4 * self.side

    def strict_rhombus_count(self) -> int:
        return self.side * self.side

    def strict_rhombus_area(self) -> Fraction:
        return self.strict_rhombus_count() * self.sine

    def area_excess_upper_bound(self) -> Fraction:
        """Exact rational upper bound for A_4 - (sqrt(3)/2)R_4."""

        # If c=cos(theta)<1/2 and s=sin(theta), then
        # s^2 - 3/4 = (1/2-c)(1/2+c), while s+sqrt(3)/2 > 1.
        return self.strict_rhombus_count() * (Fraction(1, 2) - self.cosine)

    def check(self) -> dict[str, object]:
        unit = set(self.unit_difference_indices())
        expected = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        if unit != expected:
            raise AssertionError(f"unexpected unit differences: {sorted(unit)}")

        # The unit-contact graph is the Cartesian grid: every edge changes the
        # parity of i+j, so it is bipartite and therefore triangle-free.
        if not all(
            ((i + j) % 2) != ((i + 1 + j) % 2)
            for i, j in self.points
            if i < self.side
        ):
            raise AssertionError("horizontal parity check failed")
        if not all(
            ((i + j) % 2) != ((i + j + 1) % 2)
            for i, j in self.points
            if j < self.side
        ):
            raise AssertionError("vertical parity check failed")

        q = self.parameter_denominator
        p = self.parameter_numerator
        cosine_gap = Fraction(1, 2) - self.cosine
        # Minimality of p gives the O(1/q) defect bound without radicals.
        exact_upper = Fraction(3 * p, q * q + p * p)
        if not (cosine_gap > 0 and cosine_gap < exact_upper):
            raise AssertionError("circle-parameter defect bound failed")

        return {
            "side": self.side,
            "points": len(self.points),
            "unit_difference_indices": tuple(sorted(unit)),
            "triangle_free": True,
            "strict_rhombi": self.strict_rhombus_count(),
            "train_families": 2,
            "trains_per_family": self.side + 1,
            "boundary_occurrences": self.interface_length(),
            "cosine": self.cosine,
            "cosine_defect_upper": cosine_gap,
            "certified_cosine_defect_upper": exact_upper,
            "diameter_squared": self.diameter_squared(),
            "rhombus_area": self.strict_rhombus_area(),
            "area_excess_upper": self.area_excess_upper_bound(),
        }


def main() -> None:
    for side in (3, 5, 20, 100, 400):
        grid = ObliqueGrid.near_equilateral(side)
        summary = grid.check()
        print(
            "PASS side={side} points={points} rhombi={strict_rhombi} "
            "boundary={boundary_occurrences} cosine_defect<{defect} "
            "area_excess<{area_excess}".format(
                side=side,
                points=summary["points"],
                strict_rhombi=summary["strict_rhombi"],
                boundary_occurrences=summary["boundary_occurrences"],
                defect=summary["cosine_defect_upper"],
                area_excess=summary["area_excess_upper"],
            )
        )
    print("PASS: every certified unit-contact graph is bipartite and triangle-free")
    print("PASS: ordered linear-by-linear train grids survive O(1/D) angle defect")
    print("Finite regression only; no global-minimality claim.")


if __name__ == "__main__":
    main()
