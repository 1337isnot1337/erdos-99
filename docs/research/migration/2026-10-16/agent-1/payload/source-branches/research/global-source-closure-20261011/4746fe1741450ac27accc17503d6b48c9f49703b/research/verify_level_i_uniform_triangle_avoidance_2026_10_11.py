#!/usr/bin/env python3
"""Exact finite checks of source-uniform normalized triangle avoidance.

Coordinates are (x, y) with physical height sqrt(vertical_factor)*y.
All squared distances, forbidden intervals, normalization factors, and
triangle slacks are rational. This checks the listed fixtures, including a
new-triangle trap; it certifies no global minimum or Level I conclusion.
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb


def edge_data(points, vertical_factor):
    return {
        (i, j): (
            (points[i][0] - points[j][0]) ** 2
            + vertical_factor * (points[i][1] - points[j][1]) ** 2,
            vertical_factor * (points[i][1] - points[j][1]) ** 2,
        )
        for i, j in combinations(range(len(points)), 2)
    }


def avoid_intervals(data, n, t):
    if n < 3 or not F(0) < t <= F(1, 32):
        raise ValueError("need n>=3 and 0<t<=1/32")
    if min(a for a, _ in data.values()) != 1:
        raise ValueError("minimum original separation must equal one")
    tau = t / (16 * comb(n, 3))
    left, right = t / 2, t
    intervals = []
    raw_total_length = F(0)
    short_count = 0
    for triple in combinations(range(n), 3):
        edges = list(combinations(triple, 2))
        if max(data[e][0] for e in edges) > F(9, 8):
            continue
        short_count += 1
        low = min(edges, key=lambda e: data[e][1])
        high = max(edges, key=lambda e: data[e][1])
        slope = data[high][1] - data[low][1]
        assert slope >= F(1, 2), (triple, slope)
        intercept = data[high][0] - data[low][0]
        root = -intercept / slope
        radius = (1 + t) * tau / slope
        raw_total_length += 2 * radius
        start, end = max(left, root - radius), min(right, root + radius)
        if start <= end:
            intervals.append((start, end))

    assert raw_total_length <= 4 * (1 + t) * comb(n, 3) * tau
    assert raw_total_length < right - left
    cursor = left
    for start, end in sorted(intervals):
        if cursor < start:
            return (cursor + start) / 2, tau, short_count
        cursor = max(cursor, end)
    assert cursor < right
    return (cursor + right) / 2, tau, short_count


def verify_fixture(name, points, vertical_factor=F(1), t=F(1, 32)):
    data = edge_data(points, vertical_factor)
    n = len(points)
    s, tau, short_count = avoid_intervals(data, n, t)
    assert t / 2 <= s <= t
    transformed = {e: a + s * b for e, (a, b) in data.items()}
    normalization2 = min(transformed.values())
    assert 1 <= normalization2 <= 1 + s <= 1 + t
    normalized = {e: d / normalization2 for e, d in transformed.items()}
    assert min(normalized.values()) == 1
    assert max(normalized.values()) <= (1 + t) * max(a for a, _ in data.values())
    original_triangle_count = 0
    for triple in combinations(range(n), 3):
        edges = tuple(combinations(triple, 2))
        original_triangle_count += all(data[e][0] == 1 for e in edges)
        slack = sum(normalized[e] for e in edges) - 3
        assert slack >= tau, (name, triple, slack, tau)
    print(
        f"{name}: n={n}, pairs={len(data)}, triples={comb(n, 3)}, "
        f"short={short_count}, old-unit-triangles={original_triangle_count}; "
        "all normalized pair bounds and triangle slack certified"
    )
    return len(data), comb(n, 3)


def triangular_patch(m):
    return tuple((F(i) + F(j, 2), F(j, 2)) for i in range(m) for j in range(m))


def verify():
    totals = [0, 0]
    fixtures = [
        ("equilateral", ((F(0), F(0)), (F(1), F(0)), (F(1, 2), F(1, 2))), F(3)),
        ("triangular-5x5", triangular_patch(5), F(3)),
        ("triangular-7x7", triangular_patch(7), F(3)),
        ("collinear", tuple((F(i), F(0)) for i in range(9)), F(1)),
        (
            "rotated-square-4x4",
            tuple((F(3 * i - 4 * j, 5), F(4 * i + 3 * j, 5))
                  for i in range(4) for j in range(4)),
            F(1),
        ),
    ]

    # All three normalized lengths become exactly one at s=trap_s.
    # The input itself is unit-separated and has no unit triangle.
    r = F(50, 151)
    x = (1 - 3 * r * r) / (1 + 3 * r * r)
    y = 2 * r / (1 + 3 * r * r)
    assert x * x + 3 * y * y == 1
    trap = ((F(0), F(0)), (2 * x, F(0)), (x, y))
    trap_s = x * x / (y * y) - 1
    assert F(1, 64) < trap_s < F(1, 32)
    trap_data = edge_data(trap, F(3))
    trap_lengths = [a + trap_s * b for a, b in trap_data.values()]
    assert len(set(trap_lengths)) == 1
    assert all(d / min(trap_lengths) == 1 for d in trap_lengths)
    s, _, _ = avoid_intervals(trap_data, 3, F(1, 32))
    assert s != trap_s
    fixtures.append(("new-triangle-trap", trap, F(3)))
    print("Hostile trap: a naive interior parameter creates a unit triangle; avoidance excludes it")

    for name, points, factor in fixtures:
        counts = verify_fixture(name, points, factor)
        totals = [a + b for a, b in zip(totals, counts)]

    for bad_t in (F(0), F(-1), F(1, 16)):
        try:
            avoid_intervals(trap_data, 3, bad_t)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid parameter accepted")
    try:
        avoid_intervals(edge_data(((F(0), F(0)), (F(2), F(0)), (F(4), F(0))), F(1)), 3, F(1, 32))
    except ValueError:
        pass
    else:
        raise AssertionError("nonnormalized source accepted")

    print(f"PASS: {totals[0]} exact pair checks and {totals[1]} exact triple checks; "
          "no global optimality or Level I closure asserted")


if __name__ == "__main__":
    verify()
