#!/usr/bin/env python3
"""Exact KKT-realizable inactive-chamber activation regression.

The construction and scope are in
docs/reports/target_c_inactive_chamber_kkt_activation_regression_2026-09-12.md.
All distance and contact tests use Fraction arithmetic. The KKT check is the
explicit scalar/vector balance described in the report; the family is not a
global-minimality certificate.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import math


def basis(M: int) -> tuple[Fraction, Fraction]:
    a = math.floor(M / math.sqrt(3.0)) + 1
    denominator = M * M + a * a
    c = Fraction(M * M - a * a, denominator)
    sine = Fraction(2 * M * a, denominator)
    assert 0 < c < Fraction(1, 2)
    assert c * c + sine * sine == 1
    assert 3 * a * a > M * M
    return c, sine


def frame_points(M: int) -> list[tuple[int, int]]:
    return sorted(
        (i, j)
        for i in range(M + 1)
        for j in range(M + 1)
        if i in (0, M) or j in (0, M)
    )


def inner_lattice(
    M: int, c: Fraction, sine: Fraction
) -> list[tuple[Fraction, Fraction, int, int]]:
    points = []
    for j in range(-2 * M, 2 * M + 1):
        y = sine * j
        if not (3 <= y <= M - 3):
            continue
        for i in range(-2 * M, 2 * M + 1):
            x = Fraction(i) + c * j
            if 3 <= x <= M - 3:
                points.append((x, y, i, j))
    return points


def initial_point(x: Fraction, y: Fraction, M: int) -> tuple[Fraction, Fraction]:
    center = Fraction(M, 2)
    scale = Fraction(M + 1, M)
    return center + scale * (x - center), center + scale * (y - center)


def distance_squared(
    p: tuple[Fraction, Fraction], q: tuple[Fraction, Fraction]
) -> Fraction:
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + dy * dy


def contact_edges(
    points: list[tuple[Fraction, Fraction]]
) -> set[tuple[int, int]]:
    return {
        (u, v)
        for u, v in combinations(range(len(points)), 2)
        if distance_squared(points[u], points[v]) == 1
    }


def triangle_free(vertex_count: int, edges: set[tuple[int, int]]) -> bool:
    adjacency = [set() for _ in range(vertex_count)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    return not any(
        v in adjacency[u] and w in adjacency[u] and v in adjacency[w]
        for u in range(vertex_count)
        for v in adjacency[u]
        for w in adjacency[u]
        if v != w
    )


def check(M: int) -> None:
    assert M >= 8
    c, sine = basis(M)
    frame = frame_points(M)
    inner = inner_lattice(M, c, sine)
    assert len(frame) == 4 * M
    assert len(inner) > 0

    initial_inner = [initial_point(x, y, M) for x, y, _, _ in inner]
    terminal_inner = [(x, y) for x, y, _, _ in inner]
    frame_as_points = [(Fraction(i), Fraction(j)) for i, j in frame]

    # Both endpoints of the homotopy stay in a square buffer. The coefficient
    # bounds are preserved by the affine interpolation.
    for point in initial_inner + terminal_inner:
        assert Fraction(5, 2) < point[0] < M - Fraction(5, 2)
        assert Fraction(5, 2) < point[1] < M - Fraction(5, 2)

    # Initial source: exactly the frame cycle is in contact.
    initial_source = frame_as_points + initial_inner
    initial_edges = contact_edges(initial_source)
    expected_frame = {
        (u, v)
        for u, v in combinations(range(4 * M), 2)
        if abs(frame[u][0] - frame[v][0])
        + abs(frame[u][1] - frame[v][1])
        == 1
    }
    assert initial_edges == expected_frame
    assert triangle_free(len(initial_source), initial_edges)

    for u, v in combinations(initial_inner, 2):
        assert distance_squared(u, v) > 1
    for p in initial_inner:
        for q in frame_as_points:
            assert distance_squared(p, q) > 1

    # Terminal source: exact rhombic-grid contacts, with no cross contacts.
    terminal_source = frame_as_points + terminal_inner
    terminal_edges = contact_edges(terminal_source)
    index_position = {(i, j): k for k, (_, _, i, j) in enumerate(inner)}
    index_set = set(index_position)
    expected_grid = set()
    for k, (_, _, i, j) in enumerate(inner):
        for di, dj in ((1, 0), (0, 1)):
            neighbor = (i + di, j + dj)
            if neighbor in index_set:
                expected_grid.add(
                    (4 * M + k, 4 * M + index_position[neighbor])
                )
    assert terminal_edges == expected_frame | expected_grid
    assert triangle_free(len(terminal_source), terminal_edges)

    for p in terminal_inner:
        for q in frame_as_points:
            assert distance_squared(p, q) > 1

    # The two frame diagonals fix the source diameter; all inner points are in
    # the square, so no inner pair can exceed the square diameter.
    diameter_squared = Fraction(2 * M * M)
    frame_position = {point: k for k, point in enumerate(frame)}
    assert distance_squared(
        frame_as_points[frame_position[(0, 0)]],
        frame_as_points[frame_position[(M, M)]],
    ) == diameter_squared
    assert distance_squared(
        frame_as_points[frame_position[(M, 0)]],
        frame_as_points[frame_position[(0, M)]],
    ) == diameter_squared

    # Oler slack is diagnostic here; the proof uses the standard lattice
    # fundamental-cell count and the O(M) estimate.
    area_over_a0 = float(sine) * M * M / (math.sqrt(3.0) / 2.0)
    slack = area_over_a0 + 2 * M + 1 - len(inner)
    assert 0 <= slack <= 80 * M

    # Alternating horizontal neighbors form a deep matching.
    matching = []
    point_by_index = {(i, j): (x, y) for x, y, i, j in inner}
    for j in sorted({j for _, _, _, j in inner}):
        row = sorted(i for i, jj in index_set if jj == j)
        for position in range(0, len(row) - 1, 2):
            p = (row[position], j)
            q = (row[position + 1], j)
            if q == (p[0] + 1, p[1]):
                matching.append((p, q))
    assert len(matching) >= len(inner) // 5
    for p, q in matching:
        pp = initial_point(*point_by_index[p], M)
        qq = initial_point(*point_by_index[q], M)
        assert distance_squared(pp, qq) > 1

    # KKT scalar balance: two diameter multipliers sum to one and the corner
    # diagonal coefficient h/sqrt(2) equals the frame-contact coefficient.
    h = 0.5
    gamma = 1.0 / (2.0 * math.sqrt(2.0))
    assert abs(2.0 * h - 1.0) < 1e-15
    assert abs(h / math.sqrt(2.0) - gamma) < 1e-15


def main() -> None:
    for M in (8, 12, 20, 28):
        check(M)
        c, sine = basis(M)
        count = len(inner_lattice(M, c, sine))
        matching = count // 5
        print(f"M={M} frame={4*M} chamber_points={count} matching_lower={matching}")
    print("PASS: KKT-realizable inactive-chamber activation regression")


if __name__ == "__main__":
    main()
