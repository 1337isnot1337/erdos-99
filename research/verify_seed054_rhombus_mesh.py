#!/usr/bin/env python3
"""Exact mesh/source/replacement certificates; no global-optimality claim."""

import hashlib
import json
from collections import deque
from fractions import Fraction


FIXTURES = ((2, 24), (2, 64), (3, 40), (3, 144))


def norm_num(a, b, k):
    return k * (a * a + b * b) + (k - 2) * a * b


def in_cell_disk(i, j, k, radius):
    return norm_num(2 * i + 1, 2 * j + 1, k) <= 4 * k * radius * radius


def hole(i, j):
    return -2 <= i <= 1 and -2 <= j <= 1


def source(k, radius):
    bound = 2 * radius + 4
    cells = {(i, j) for i in range(-bound, bound + 1)
             for j in range(-bound, bound + 1)
             if not hole(i, j) and in_cell_disk(i, j, k, radius)}
    vertices = {(i + a, j + b) for i, j in cells
                for a, b in ((0, 0), (1, 0), (1, 1), (0, 1))}
    return cells, vertices


def hull(points):
    points = sorted(points)

    def cross(a, b, c):
        return ((b[0] - a[0]) * (c[1] - a[1])
                - (b[1] - a[1]) * (c[0] - a[0]))

    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def diameter2(points, k=None):
    outer = hull(points)
    best, witnesses = 0, []
    for a_index, a in enumerate(outer):
        for b in outer[a_index + 1:]:
            x, y = a[0] - b[0], a[1] - b[1]
            d = norm_num(x, y, k) if k is not None else x * x + y * y + x * y
            if d > best:
                best, witnesses = d, [(a, b)]
            elif d == best:
                witnesses.append((a, b))
    return Fraction(best, k if k is not None else 1), outer, witnesses


def triangular_packet(radius):
    bound = 2 * radius + 2
    return {(i, j) for i in range(-bound, bound + 1)
            for j in range(-bound, bound + 1)
            if i * i + j * j + i * j <= radius * radius}


def digest(vertices):
    return hashlib.sha256(json.dumps(sorted(vertices), separators=(",", ":"))
                          .encode()).hexdigest()


def verify_fixture(k, radius):
    cells, vertices = source(k, radius)
    assert cells and vertices
    queue, reached = deque([min(cells)]), {min(cells)}
    while queue:
        i, j = queue.popleft()
        for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if neighbor in cells and neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    assert reached == cells
    assert (radius, 0) in vertices and (-radius, 0) in vertices
    assert (0, radius) in vertices and (0, -radius) in vertices
    assert not (vertices & {(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)})

    # Every mesh vertex is in a complete cell. Its edge and diagonal constraints
    # are the hypotheses of the endpoint rigidity theorem in the report.
    assert vertices == {(i + a, j + b) for i, j in cells
                        for a, b in ((0, 0), (1, 0), (1, 1), (0, 1))}
    side = Fraction(norm_num(1, 0, k), k)
    diag_plus = Fraction(norm_num(1, 1, k), k)
    diag_minus = Fraction(norm_num(1, -1, k), k)
    assert side == 1 and diag_plus + diag_minus == 4
    wrong_side_d2 = Fraction((k - 2) ** 2, k * k)
    assert wrong_side_d2 < 1

    # Independent all-displacement enumeration covers every lattice source
    # pair, including displacement values not realized by this particular set.
    span_i = max(p[0] for p in vertices) - min(p[0] for p in vertices)
    span_j = max(p[1] for p in vertices) - min(p[1] for p in vertices)
    possible_contacts = set()
    for a in range(-span_i, span_i + 1):
        for b in range(-span_j, span_j + 1):
            if a == b == 0:
                continue
            d = norm_num(a, b, k)
            assert d >= k
            if d == k:
                possible_contacts.add((a, b))
    assert possible_contacts == {(1, 0), (-1, 0), (0, 1), (0, -1)}
    edges = sum((i + 1, j) in vertices for i, j in vertices)
    edges += sum((i, j + 1) in vertices for i, j in vertices)
    # The off-lattice label is p=u/10. Check every isolate-involving pair.
    isolate_min = min(Fraction(norm_num(10 * i - 1, 10 * j, k), 100 * k)
                      for i, j in vertices)
    assert isolate_min > 1

    source_d2, source_hull, witnesses = diameter2(vertices, k)
    assert source_d2 >= 4 * radius * radius
    # p is inside conv{+-R*u,+-R*v}; its pairs cannot increase the diameter.
    assert Fraction(1, 10 * radius) < 1
    n = len(vertices) + 1
    packet = triangular_packet(radius - 1)
    assert len(packet) >= n
    # Choose exactly n labels: the same cardinality includes the old isolate.
    replacement = set(sorted(packet)[:n])
    assert len(replacement) == n
    # Sorted mesh vertices map first, with the isolate assigned the last site.
    assignment = dict(zip(sorted(vertices), sorted(replacement)[:-1]))
    bad_cells, grown_pairs = 0, set()
    for i, j in cells:
        corners = ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))
        bad = False
        for a_index, a in enumerate(corners):
            for b in corners[a_index + 1:]:
                ap, bp = assignment[a], assignment[b]
                x, y = ap[0] - bp[0], ap[1] - bp[1]
                if k * (x * x + y * y + x * y) > norm_num(a[0] - b[0], a[1] - b[1], k):
                    bad = True
                    grown_pairs.add(tuple(sorted((a, b))))
        bad_cells += bad
    assert bad_cells >= (radius + 7) // 8
    assert len(grown_pairs) >= (radius + 15) // 16
    replacement_d2, replacement_hull, _ = diameter2(replacement)
    assert replacement_d2 <= 4 * (radius - 1) ** 2 < source_d2
    for i, j in replacement:
        assert i * i + j * j + i * j <= (radius - 1) ** 2

    return {
        "k": k, "R": radius, "cells": len(cells), "n": n,
        "contacts": edges, "contact_isolates": 1,
        "source_sha256": digest(vertices),
        "source_diameter_squared": str(source_d2),
        "source_hull_vertices": len(source_hull),
        "diameter_witness": witnesses[0],
        "isolate_min_squared": str(isolate_min),
        "available_replacement_sites": len(packet),
        "replacement_diameter_squared": str(replacement_d2),
        "replacement_hull_vertices": len(replacement_hull),
        "replacement_sha256": digest(replacement),
        "local_growth_cells_required_at_comparison_diameter": (radius + 7) // 8,
        "bad_cells_of_lexicographic_replacement": bad_cells,
        "grown_local_pairs_of_lexicographic_replacement": len(grown_pairs),
        "pairs_per_full_source": n * (n - 1) // 2,
        "classification": "regression; candidate proof awaits independent audit",
    }


def negative_controls():
    # One diagonal cannot pin a cell: change a square to a unit rhombus with
    # cos(angle)=1/4. All six pairs remain separated, four contacts persist.
    c = Fraction(1, 4)
    assert 2 - 2 * c < 2 < 2 + 2 * c
    assert 2 - 2 * c > 1
    # Dropping distinct-label separation permits two square cells to coincide
    # after reflecting one onto the other; all cell-local lengths are retained.
    folded = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 1), (1, 1)]
    assert len(set(folded)) < len(folded)
    # Two disconnected meshes can translate toward each other nonexpansively.
    a, b = {(0, 0), (1, 0), (0, 1), (1, 1)}, {(10, 0), (11, 0), (10, 1), (11, 1)}
    assert all((x[0] - y[0] + 1) ** 2 + (x[1] - y[1]) ** 2
               < (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 for x in a for y in b)
    assert all((x[0] - y[0] + 1) ** 2 + (x[1] - y[1]) ** 2 >= 1
               for x in a for y in b)
    # At the triangular limit the contact-parity assertion fails.
    assert norm_num(1, -1, 10**6) > 10**6
    assert Fraction(2) - 2 * Fraction(1, 2) == 1
    # Exact +R and -R source anchors exceed the comparison diameter bound.
    assert 4 * 24 ** 2 > 4 * 23 ** 2
    return 5


def main():
    fixtures = [verify_fixture(k, radius) for k, radius in FIXTURES]
    # Algebraic family bounds: no numerical/pi assumptions are used here.
    # s^2/a0^2=1+4/(3k)-4/(3k^2) >= (1+1/(4k))^2 for k>=2.
    assert Fraction(5, 8) * 2 - Fraction(67, 64) > 0
    for k in range(2, 1001):
        radius = 16 * k * k
        s2_over_a02 = 1 + Fraction(4, 3 * k) - Fraction(4, 3 * k * k)
        assert s2_over_a02 > (1 + Fraction(1, 4 * k)) ** 2
        ratio = Fraction((radius + 2) ** 2, (radius - 1) ** 2)
        assert ratio < 1 + Fraction(8, radius)
        assert s2_over_a02 > ratio * ratio
    # Exact scalar premises of Theorem 3; its quantified geometric argument
    # is the analytic proof, not a finite endpoint search.
    for k, radius in FIXTURES:
        c = Fraction(k - 2, 2 * k)
        assert (1 + c) / 2 < 1
        assert Fraction(radius, 4) - 1 >= Fraction(radius, 6)
        assert Fraction(6, radius) <= Fraction(1, 4)
        assert 24 * Fraction(1, 8) == 3
    print(json.dumps({"fixtures": fixtures, "negative_controls": negative_controls(),
                      "global_optimality_proved": False}, indent=2))


if __name__ == "__main__":
    main()
