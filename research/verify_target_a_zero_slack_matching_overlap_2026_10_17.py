#!/usr/bin/env python3
"""Exact rational incidence-geometry regression for independent matchings."""

from fractions import Fraction as F
from itertools import combinations


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def d2(a, b):
    dx, dy = sub(a, b)
    return dx * dx + dy * dy


def cross(a, b, c):
    ab, ac = sub(b, a), sub(c, a)
    return ab[0] * ac[1] - ab[1] * ac[0]


def point_in_triangle_strict(point, triangle):
    a, b, c = triangle
    orientation = cross(a, b, c)
    signs = (cross(a, b, point), cross(b, c, point), cross(c, a, point))
    return orientation > 0 and all(value > 0 for value in signs)


def point_outside_triangle(point, triangle):
    a, b, c = triangle
    return any(value < 0 for value in
               (cross(a, b, point), cross(b, c, point), cross(c, a, point)))


def all_matchings(left, adjacency):
    results = []

    def visit(position, used, assignment):
        if position == len(left):
            results.append(tuple(assignment))
            return
        vertex = left[position]
        for source in adjacency[vertex]:
            if source not in used:
                visit(position + 1, used | {source},
                      assignment + [(vertex, source)])

    visit(0, set(), [])
    return results


def maximum_matching_size(left, adjacency):
    best = 0

    def visit(position, used, size):
        nonlocal best
        if position == len(left):
            best = max(best, size)
            return
        vertex = left[position]
        visit(position + 1, used, size)
        for source in adjacency[vertex]:
            if source not in used:
                visit(position + 1, used | {source}, size + 1)

    visit(0, set(), 0)
    return best


def main():
    X = {
        "x1": (F(-1, 5), F(-1, 5)),
        "x2": (F(16, 5), F(-1, 5)),
        "x3": (F(3, 2), F(2)),
    }
    Y = {
        "y1": (F(0), F(0)),
        "y2": (F(3), F(0)),
    }
    A = {
        "a1": (F(-1, 2), F(-1, 5)),
        "a2": (F(7, 2), F(-1, 5)),
        "a3": (F(3, 2), F(29, 10)),
        "a4": (F(6), F(0)),
        "a5": (F(9), F(-1, 5)),
    }

    source_distances = {(i, j): d2(A[i], A[j])
                        for i, j in combinations(A, 2)}
    assert min(source_distances.values()) > 1
    source_diameter2 = max(source_distances.values())
    assert source_diameter2 == F(361, 4)
    assert [pair for pair, value in source_distances.items()
            if value == source_diameter2] == [("a1", "a5")]

    response_distances = {(i, j): d2(X[i], X[j])
                          for i, j in combinations(X, 2)}
    assert min(response_distances.values()) > 1
    assert max(response_distances.values()) == F(289, 25)
    assert response_distances["x1", "x3"] == F(773, 100)
    assert response_distances["x2", "x3"] == F(773, 100)
    assert d2(Y["y1"], Y["y2"]) == 9

    triangle = (X["x1"], X["x2"], X["x3"])
    assert cross(*triangle) > 0
    assert set(Y.values()) == {(F(0), F(0)), (F(3), F(0))}
    for point in Y.values():
        assert point_in_triangle_strict(point, triangle)
    assert all(point_outside_triangle(point, triangle)
               for point in A.values())

    source_matching_adjacency = {
        x: [a for a in A if d2(X[x], A[a]) < 1] for x in X
    }
    lattice_matching_adjacency = {
        y: [a for a in A if d2(Y[y], A[a]) < 1] for y in Y
    }
    assert source_matching_adjacency == {
        "x1": ["a1"], "x2": ["a2"], "x3": ["a3"]}
    assert lattice_matching_adjacency == {
        "y1": ["a1"], "y2": ["a2"]}
    match_x = all_matchings(list(X), source_matching_adjacency)
    match_y = all_matchings(list(Y), lattice_matching_adjacency)
    assert match_x == [(('x1', 'a1'), ('x2', 'a2'), ('x3', 'a3'))]
    assert match_y == [(('y1', 'a1'), ('y2', 'a2'))]
    image_x = {source for _, source in match_x[0]}
    image_y = {source for _, source in match_y[0]}
    assert image_x == {"a1", "a2", "a3"}
    assert image_y == {"a1", "a2"}
    assert image_x & image_y == {"a1", "a2"}
    assert len(image_x | image_y) == 3

    xy_conflicts = [(x, y) for x in X for y in Y
                    if d2(X[x], Y[y]) < 1]
    assert xy_conflicts == [("x1", "y1"), ("x2", "y2")]
    assert d2(X["x1"], Y["y1"]) == F(2, 25)
    assert d2(X["x2"], Y["y2"]) == F(2, 25)
    assert d2(A["a1"], Y["y1"]) == F(29, 100)
    assert d2(A["a2"], Y["y2"]) == F(29, 100)

    combined = list(X) + list(Y)
    combined_adjacency = {
        **source_matching_adjacency,
        **lattice_matching_adjacency,
    }
    neighborhood = {a for vertex in combined
                    for a in combined_adjacency[vertex]}
    assert neighborhood == {"a1", "a2", "a3"}
    assert len(combined) - len(neighborhood) == 2
    assert maximum_matching_size(combined, combined_adjacency) == 3
    assert len(A) == len(combined) == 5
    assert F(3) <= 12 * F(17, 5) + 9

    print("PASS: all five source labels are unit-separated; exact source diameter is 19/2")
    print("PASS: X is a nondegenerate unit-separated triangle; both lattice sites lie strictly inside")
    print("PASS: unique X-to-A and Y-to-A matchings; image intersection has size 2")
    print("PASS: combined five-target conflict graph has three source neighbors and maximum matching size 3")
    print("LIMIT: incidence geometry only; no global optimum, source-capacity premise, or Schur matrix")


if __name__ == "__main__":
    main()
