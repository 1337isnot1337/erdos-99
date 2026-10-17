#!/usr/bin/env python3
"""Exact finite check for the strict thin-corridor polygon regression.

The script certifies unit side lengths, strict convexity, pairwise unit separation
of all face vertices, a linear bounding box, and linear off-phase side count for
one rational construction. It does not construct a contact graph, a C-II source,
or a global minimizer.
"""

from fractions import Fraction as F


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def build_edges(n):
    edges = []
    for i in range(1, n + 1):
        t = F(i, n * n)
        den = 1 + t * t
        edges.append(((1 - t * t) / den, 2 * t / den))
    caps = [(F(4, 5), F(3, 5)), (F(0), F(1)), (-F(4, 5), F(3, 5))]
    return edges + caps + [(-x, -y) for x, y in edges] + [(-x, -y) for x, y in caps]


def main():
    n = 32
    edges = build_edges(n)
    size = len(edges)
    assert size == 2 * n + 6

    # Every edge is exactly unit length and the cyclic vector sum is zero.
    for x, y in edges:
        assert x * x + y * y == 1
    assert sum(x for x, _ in edges) == 0
    assert sum(y for _, y in edges) == 0

    # Closure and strict positive turns certify a strictly convex polygon.
    turns = [cross(edges[i], edges[(i + 1) % size]) for i in range(size)]
    assert min(turns) > 0

    points = [(F(0), F(0))]
    for edge in edges:
        points.append((points[-1][0] + edge[0], points[-1][1] + edge[1]))
    assert points[-1] == points[0]
    points.pop()

    # The boundary vertices themselves are unit-separated; adjacent distances equal 1.
    min_nonadjacent_sq = None
    for i in range(size):
        for j in range(i):
            gap = i - j
            if gap in (1, size - 1):
                continue
            d2 = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            min_nonadjacent_sq = d2 if min_nonadjacent_sq is None else min(min_nonadjacent_sq, d2)
    assert min_nonadjacent_sq > 1

    xmin = min(x for x, _ in points)
    xmax = max(x for x, _ in points)
    ymin = min(y for _, y in points)
    ymax = max(y for _, y in points)
    assert xmin > -1
    assert xmax < n + 1
    assert xmax - xmin < n + 2
    assert ymin == 0
    assert ymax < 5

    area2 = sum(
        points[i][0] * points[(i + 1) % size][1]
        - points[(i + 1) % size][0] * points[i][1]
        for i in range(size)
    )
    assert area2 > 0
    assert area2 / 2 < 5 * (n + 1)

    # Use horizontal and slope-one projective directions.  No listed edge has slope
    # 0 or 1, including the vertical cap edge.
    assert all(y != 0 and y != x for x, y in edges)
    assert size == 2 * n + 6

    print("strict thin-corridor regression: exact finite checks OK")
    print(f"side_occurrences={size} area={float(area2/2):.9f}")
    print(f"min_nonadjacent_distance={float(min_nonadjacent_sq) ** 0.5:.9f}")
    print(f"bounding_box=({float(xmax):.9f},{float(ymax):.9f})")


if __name__ == "__main__":
    main()
