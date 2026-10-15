#!/usr/bin/env python3
"""Exhaustively compute small triangular-lattice diameter minima with integers."""

from __future__ import annotations

import argparse
from itertools import combinations
import json

Point = tuple[int, int]
ORIGIN: Point = (0, 0)


def distance_squared(p: Point, q: Point) -> int:
    """Squared Euclidean distance in the basis (1,0), (1/2,sqrt(3)/2)."""
    da = p[0] - q[0]
    db = p[1] - q[1]
    return da * da + da * db + db * db


def lattice_disk(radius: int) -> list[Point]:
    """Return all nonzero lattice points at distance at most radius from 0."""
    bound = 2 * radius  # A safe integer-coordinate bound; the quadratic test is exact.
    points = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            point = (a, b)
            if point != ORIGIN and distance_squared(point, ORIGIN) <= radius * radius:
                points.append(point)
    return sorted(points, key=lambda p: (distance_squared(p, ORIGIN), p[0], p[1]))


def diameter_squared(points: tuple[Point, ...]) -> int:
    return max(distance_squared(p, q) for p, q in combinations(points, 2))


def enumerate_minimum(n: int) -> dict[str, object]:
    """Enumerate every origin-anchored candidate with diameter <= n-1."""
    if n < 2:
        raise ValueError("n must be at least 2")

    radius = n - 1
    sites = lattice_disk(radius)
    best: int | None = None
    witness: tuple[Point, ...] | None = None
    examined = 0

    for chosen in combinations(sites, n - 1):
        candidate = (ORIGIN,) + chosen
        examined += 1
        candidate_diameter = diameter_squared(candidate)
        if best is None or candidate_diameter < best:
            best = candidate_diameter
            witness = candidate

    if best is None or witness is None:
        raise RuntimeError(f"no candidate found for n={n}")

    return {
        "n": n,
        "lattice_optimum_squared": best,
        "witness": [list(point) for point in witness],
        "anchored_subsets_examined": examined,
        "radius_bound": radius,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-n", type=int, default=5,
        help="compute every size from 2 through this value (default: 5; 6 may be expensive)",
    )
    args = parser.parse_args()
    if not 2 <= args.max_n <= 6:
        parser.error("--max-n must be between 2 and 6")
    print(json.dumps([enumerate_minimum(n) for n in range(2, args.max_n + 1)], indent=2))


if __name__ == "__main__":
    main()
