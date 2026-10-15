#!/usr/bin/env python3
"""Exact triangle covers; the analytic report proves arbitrary-point capacity.

No optimizer output is a certificate. The checked frames are packing
containers with fixed wall pins, not global minimum-diameter sources.
"""
from fractions import Fraction as F
from itertools import combinations
from verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05 import (
    V0, grid_point, rational, squared,
)


def cover(m, n):
    wall = {(i, j) for i in range(m+1) for j in range(n+1)
            if i in (0, m) or j in (0, n)}-{(1, 0), (2, 0)}
    triangles = []
    for i in range(m):
        for j in range(n):
            triangles.extend([((i, j), (i+1, j), (i, j+1)),
                              ((i+1, j), (i, j+1), (i+1, j+1))])
    for triangle in triangles:
        assert all(squared(grid_point(*x, V0), grid_point(*y, V0)) == rational(1)
                   for x, y in combinations(triangle, 2))
    admissible = [t for t in triangles if not wall.intersection(t)]
    assert len(triangles) == 2*m*n
    if m == 3:
        assert len(admissible) == 2*(n-1) == (m-1)*(n-1)
    if (m, n) == (4, 4):
        assert len(admissible) == 10
        center = (2, 2)
        star = [t for t in admissible if center in t]
        assert len(star) == 6
        for triangle in star:
            for x in triangle:
                assert squared(grid_point(*x, V0), grid_point(*center, V0)) in (rational(0), rational(1))
    return len(triangles), len(admissible)


if __name__ == "__main__":
    cases = [(3, n) for n in (3, 4, 7, 20, 80)]+[(4, 4)]
    results = [cover(m, n) for m, n in cases]
    print(f"PASS: {sum(r[0] for r in results)} exact elementary unit triangles")
    print(f"PASS: {sum(r[1] for r in results)} admissible triangles after deleting two adjacent wall pins")
    print("PASS: m=3 cover has exactly K triangles for every checked n")
    print("PASS: 4-by-4 has ten admissible triangles and one exact six-triangle unit-disk star")
    print("SCOPE: arbitrary-point upper bounds use convexity/angular arguments in the report, not finite sampling")
