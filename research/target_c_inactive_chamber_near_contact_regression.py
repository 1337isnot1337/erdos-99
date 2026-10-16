#!/usr/bin/env python3
"""Exact regression for a saturated, contact-isolated inactive chamber.

This is a local obstruction certificate.  It deliberately does not model the
positive-contact core or assert global diameter optimality.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import floor


@dataclass(frozen=True)
class Chamber:
    side: int

    @property
    def scale(self) -> Fraction:
        return Fraction(self.side + 1, self.side)

    @property
    def point_count(self) -> int:
        return (self.side + 1) ** 2

    @property
    def normalized_area(self) -> int:
        # Divide physical area by the unit equilateral-triangle area.
        # The chamber has side length m * (1 + 1/m) = m + 1.
        return (self.side + 1) ** 2

    @property
    def perimeter(self) -> Fraction:
        return 4 * self.side * self.scale

    @property
    def oler_slack(self) -> Fraction:
        # z <= area/a0 + perimeter/2 + 1.
        return self.normalized_area + self.perimeter / 2 + 1 - self.point_count

    def squared_distance(self, delta_i: int, delta_j: int) -> Fraction:
        # The two basis vectors have length scale and angle pi/3.
        return self.scale**2 * (
            delta_i * delta_i + delta_i * delta_j + delta_j * delta_j
        )

    def unit_difference_indices(self) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []
        for delta_i in range(-self.side, self.side + 1):
            for delta_j in range(-self.side, self.side + 1):
                if (delta_i, delta_j) != (0, 0) and self.squared_distance(
                    delta_i, delta_j
                ) <= 1:
                    result.append((delta_i, delta_j))
        return result

    def deep_horizontal_matching(self) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        # Every endpoint has both lattice indices in [2, m-2], so every
        # endpoint is separated from all four chamber sides by > 1.
        pairs = []
        for j in range(2, self.side - 1):
            for i in range(2, self.side - 2, 2):
                pairs.append(((i, j), (i + 1, j)))
        return pairs


def check(side: int) -> None:
    chamber = Chamber(side)
    assert chamber.side >= 8
    assert chamber.scale > 1
    assert chamber.point_count == chamber.normalized_area
    assert chamber.unit_difference_indices() == []
    assert chamber.oler_slack == 2 * (side + 1) + 1

    pairs = chamber.deep_horizontal_matching()
    expected = floor((side - 3) / 2) * (side - 3)
    assert len(pairs) == expected
    endpoints = [point for pair in pairs for point in pair]
    assert len(set(endpoints)) == len(endpoints)
    assert all(
        2 <= i <= side - 2 and 2 <= j <= side - 2 for i, j in endpoints
    )
    assert len(pairs) >= (side - 3) * (side - 3) / 3


def main() -> None:
    for side in (8, 20, 100, 400):
        check(side)
        chamber = Chamber(side)
        print(
            "side=%d points=%d normalized_area=%d perimeter=%s "
            "oler_slack=%s deep_pairs=%d"
            % (
                side,
                chamber.point_count,
                chamber.normalized_area,
                chamber.perimeter,
                chamber.oler_slack,
                len(chamber.deep_horizontal_matching()),
            )
        )
    print("PASS: exact inactive-chamber near-contact regression")


if __name__ == "__main__":
    main()
