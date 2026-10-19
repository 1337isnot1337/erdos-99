#!/usr/bin/env python3
"""Finite exact falsification screens for the PR958 affine flattening lemma.

This is a regression check on small rational source sets, not a proof of the
universal rank criterion or a test of global optimality. The three color
vertices use barycentric coordinates: an invertible affine change sends any
three regular-simplex vertices to these coordinates and preserves affine rank.
"""

from fractions import Fraction
from itertools import combinations, product
import json


GRID = tuple(product(range(3), repeat=2))
THREE_SIMPLEX_AFFINE_COORDS = ((0, 0), (1, 0), (0, 1))


def require(condition, context):
    if not condition:
        raise AssertionError(context)


def matrix_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    cols = len(a[0])
    pivot = 0
    for col in range(cols):
        found = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][col]:
                scale = a[r][col]
                a[r] = [x - scale*y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def center(rows):
    n = len(rows)
    width = len(rows[0])
    means = [Fraction(sum(row[j] for row in rows), n) for j in range(width)]
    return [[Fraction(row[j]) - means[j] for j in range(width)] for row in rows]


def joined(left, right):
    return [a + b for a, b in zip(left, right)]


def centered_source(points):
    P0 = center(points)
    require(matrix_rank(P0) == 2, "source points are collinear")
    return P0


def screen_two_colours():
    total = flattenable = 0
    for points in combinations(GRID, 4):
        try:
            P0 = centered_source(points)
        except AssertionError:
            continue
        for colours in product(range(2), repeat=4):
            if len(set(colours)) != 2:
                continue
            Z0 = center([(-1 if c == 0 else 1,) for c in colours])
            rank_flat = matrix_rank(joined(P0, Z0)) == 2
            within_class_differences = [
                (points[j][0] - points[i][0], points[j][1] - points[i][1])
                for i, j in combinations(range(4), 2) if colours[i] == colours[j]
            ]
            require(bool(within_class_differences), "both colors must be used")
            parallel_level_lines = matrix_rank(within_class_differences) == 1
            require(rank_flat == parallel_level_lines,
                    f"two-color criterion mismatch: {points}, {colours}")
            total += 1
            flattenable += int(rank_flat)
    require((total, flattenable) == (1764, 240), "two-color count changed")
    return {"assignments": total, "flattenable": flattenable,
            "rank_iff_parallel_level_lines": True}


def screen_three_colours():
    three_point_cases = three_point_flat = 0
    four_point_cases = four_point_flat = 0

    for points in combinations(GRID, 3):
        try:
            P0 = centered_source(points)
        except AssertionError:
            continue
        for colours in product(range(3), repeat=3):
            if set(colours) != {0, 1, 2}:
                continue
            Z0 = center([THREE_SIMPLEX_AFFINE_COORDS[c] for c in colours])
            flat = matrix_rank(joined(P0, Z0)) == 2
            require(flat, f"three-color triangle did not flatten: {points}, {colours}")
            three_point_cases += 1
            three_point_flat += int(flat)

    for points in combinations(GRID, 4):
        try:
            P0 = centered_source(points)
        except AssertionError:
            continue
        for colours in product(range(3), repeat=4):
            if set(colours) != {0, 1, 2}:
                continue
            Z0 = center([THREE_SIMPLEX_AFFINE_COORDS[c] for c in colours])
            flat = matrix_rank(joined(P0, Z0)) == 2
            require(not flat, f"three-color four-point lift flattened: {points}, {colours}")
            four_point_cases += 1
            four_point_flat += int(flat)

    require((three_point_cases, three_point_flat) == (456, 456),
            "three-point count or flattening boundary changed")
    require((four_point_cases, four_point_flat) == (4536, 0),
            "four-point count or flattening boundary changed")
    return {
        "noncollinear_three_point_assignments": three_point_cases,
        "flattenable_at_n3": three_point_flat,
        "noncollinear_four_point_assignments": four_point_cases,
        "flattenable_at_n4": four_point_flat,
    }


def main():
    print(json.dumps({
        "grid": "3x3 integer points",
        "two_colour": screen_two_colours(),
        "three_colour": screen_three_colours(),
        "arithmetic": "exact fractions; barycentric color coordinates",
        "scope": "finite regression only; no global minimizer conclusion",
    }, sort_keys=True))


main()
