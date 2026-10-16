#!/usr/bin/env python3
"""Exact regression for collective activation of a macroscopic inactive chamber.

The construction and scope are in
docs/reports/target_c_inactive_chamber_activation_grid_regression_2026-09-12.md.
All lattice distance tests use Fraction arithmetic. The family is not a
global-minimality certificate and does not address C-II closure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import math


def qform(p: Fraction, q: Fraction, c: Fraction) -> Fraction:
    return p * p + 2 * c * p * q + q * q


def frame_points(M: int) -> set[tuple[int, int]]:
    return {
        (i, j)
        for i in range(M + 1)
        for j in range(M + 1)
        if i in (0, M) or j in (0, M)
    }


def inner_indices(M: int) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(3, M - 2)
        for j in range(3, M - 2)
    ]


def initial_point(i: int, j: int, M: int) -> tuple[Fraction, Fraction]:
    center = Fraction(M, 2)
    scale = Fraction(M + 1, M)
    return (
        center + scale * (i - center),
        center + scale * (j - center),
    )


def terminal_point(i: int, j: int) -> tuple[Fraction, Fraction]:
    return Fraction(i), Fraction(j)


def contact_edges(
    points: list[tuple[Fraction, Fraction]], c: Fraction
) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for u, v in combinations(range(len(points)), 2):
        dx = points[u][0] - points[v][0]
        dy = points[u][1] - points[v][1]
        if qform(dx, dy, c) == 1:
            edges.add((u, v))
    return edges


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
    a = math.floor(M / math.sqrt(3.0)) + 1
    denominator = M * M + a * a
    c = Fraction(M * M - a * a, denominator)
    sine = Fraction(2 * M * a, denominator)
    assert 0 < c < Fraction(1, 2)
    assert c * c + sine * sine == 1
    assert 3 * a * a > M * M

    frame = sorted(frame_points(M))
    indices = inner_indices(M)
    initial = [initial_point(i, j, M) for i, j in indices]
    terminal = [terminal_point(i, j) for i, j in indices]
    assert len(frame) == 4 * M
    assert len(indices) == (M - 5) ** 2

    # Every endpoint of the homotopy remains in a coefficient buffer around the
    # parallelogram boundary. The whole homotopy lies between these endpoints.
    for point in initial + terminal:
        assert Fraction(5, 2) < point[0] < M - Fraction(5, 2)
        assert Fraction(5, 2) < point[1] < M - Fraction(5, 2)
        assert point[0] * point[0] * (1 - c * c) > 1
        assert point[1] * point[1] * (1 - c * c) > 1

    # The initial source is the frame plus the scaled, contact-free chamber.
    initial_source = [(Fraction(i), Fraction(j)) for i, j in frame] + initial
    initial_edges = contact_edges(initial_source, c)
    assert len(initial_edges) == 4 * M
    assert triangle_free(len(initial_source), initial_edges)

    for p, q in combinations(initial, 2):
        dx = p[0] - q[0]
        dy = p[1] - q[1]
        assert qform(dx, dy, c) > 1
    for p in initial:
        for q in frame:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            assert qform(dx, dy, c) > 1

    # The terminal source has an exact rhombic-grid contact component. Check
    # that its only unit differences are the two lattice generators.
    terminal_source = [(Fraction(i), Fraction(j)) for i, j in frame] + terminal
    terminal_edges = contact_edges(terminal_source, c)
    expected_frame = {
        (u, v)
        for u, v in combinations(range(4 * M), 2)
        if abs(frame[u][0] - frame[v][0]) + abs(frame[u][1] - frame[v][1]) == 1
    }
    offset = 4 * M
    expected_grid = set()
    index_position = {point: k for k, point in enumerate(indices)}
    index_set = set(indices)
    for k, (i, j) in enumerate(indices):
        for di, dj in ((1, 0), (0, 1)):
            q = (i + di, j + dj)
            if q in index_set:
                expected_grid.add((offset + k, offset + index_position[q]))
    assert terminal_edges == expected_frame | expected_grid
    assert triangle_free(len(terminal_source), terminal_edges)
    assert len(terminal_edges) == 4 * M + 2 * (M - 5) * (M - 6)

    # The frame's opposite corners fix the source diameter. The inner patch is
    # inside the frame, so no point can exceed the frame diameter.
    diameter_squared = Fraction(M * M) * (2 + 2 * c)
    assert qform(Fraction(M), Fraction(M), c) == diameter_squared
    assert qform(Fraction(M), Fraction(-M), c) < diameter_squared

    # Oler slack of the actual initial chamber, evaluated diagnostically with
    # sqrt(3); the proof uses the rational buffer and the elementary O(M) bound.
    area_over_a0 = float(sine) * M * M / (math.sqrt(3.0) / 2.0)
    slack = area_over_a0 + 2 * M + 1 - len(indices)
    assert 0 <= slack <= 16 * M

    matching = []
    for j in range(3, M - 2):
        for i in range(3, M - 3, 2):
            matching.append(((i, j), (i + 1, j)))
    assert len(matching) == ((M - 5) // 2) * (M - 5)
    assert len(matching) >= (M - 5) ** 2 // 3
    for p, q in matching:
        pp = initial_point(*p, M)
        qq = initial_point(*q, M)
        assert qform(pp[0] - qq[0], pp[1] - qq[1], c) > 1


def main() -> None:
    for M in (8, 12, 20, 32):
        check(M)
        inner = (M - 5) ** 2
        matching = ((M - 5) // 2) * (M - 5)
        print(
            f"M={M} diameter_squared_scale={M*M} frame={4*M} "
            f"isolates={inner} deep_matching={matching}"
        )
    print("PASS: exact inactive-chamber activation regression")


if __name__ == "__main__":
    main()
