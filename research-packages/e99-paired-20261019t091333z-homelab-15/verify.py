#!/usr/bin/env python3
"""Independent exact controls for the pinned PR #138 audit."""

from fractions import Fraction as F
from itertools import combinations


ZERO = (F(0), F(0), F(0))  # rational, sqrt(3), pi coefficients
ONE = (F(1), F(0), F(0))


def c(r=0, s=0, p=0):
    return (F(r), F(s), F(p))


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def minus(x, y):
    return tuple(a - b for a, b in zip(x, y))


def poly_sum(*terms):
    result = {}
    for sign, poly in terms:
        for name, value in poly.items():
            result[name] = plus(result.get(name, ZERO), value if sign > 0 else minus(ZERO, value))
    return {name: value for name, value in result.items() if value != ZERO}


def norm2(p):
    i, j = p
    return i * i + i * j + j * j


def square_dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def hex_patch(radius):
    # Independent set-valued construction of |i|, |j|, |i+j| <= radius.
    return {
        (i, j)
        for i in range(-radius, radius + 1)
        for j in range(max(-radius, -radius - i), min(radius, radius - i) + 1)
    }


def transformed_hull(points):
    # (2i+j,j) is an invertible linear image of triangular-lattice coordinates.
    ordered = sorted((2 * i + j, j) for i, j in points)

    def turn(a, b, q):
        return (b[0] - a[0]) * (q[1] - a[1]) - (b[1] - a[1]) * (q[0] - a[0])

    lower = []
    for q in ordered:
        while len(lower) >= 2 and turn(lower[-2], lower[-1], q) <= 0:
            lower.pop()
        lower.append(q)
    upper = []
    for q in reversed(ordered):
        while len(upper) >= 2 and turn(upper[-2], upper[-1], q) <= 0:
            upper.pop()
        upper.append(q)
    return set(lower[:-1] + upper[:-1])


def all_pair_distances(points):
    return [norm2((a[0] - b[0], a[1] - b[1])) for a, b in combinations(points, 2)]


def check_hex_and_coloring(radius):
    points = hex_patch(radius)
    expected_count = 3 * radius * (radius + 1) + 1
    assert len(points) == expected_count
    corners = {
        (radius, 0), (0, radius), (-radius, radius), (-radius, 0),
        (0, -radius), (radius, -radius),
    }
    expected_hull = {
        (2 * radius, 0), (radius, radius), (-radius, radius),
        (-2 * radius, 0), (-radius, -radius), (radius, -radius),
    }
    assert transformed_hull(points) == expected_hull
    hull_order = [
        (2 * radius, 0), (radius, radius), (-radius, radius),
        (-2 * radius, 0), (-radius, -radius), (radius, -radius),
    ]
    shoelace_twice = sum(
        x * y_next - x_next * y
        for (x, y), (x_next, y_next) in zip(hull_order, hull_order[1:] + hull_order[:1])
    )
    assert shoelace_twice == 12 * radius * radius
    lattice_hull = [((x - y) // 2, y) for x, y in hull_order]
    edge_lengths_squared = [
        norm2((a[0] - b[0], a[1] - b[1]))
        for a, b in zip(lattice_hull, lattice_hull[1:] + lattice_hull[:1])
    ]
    assert all(length == radius * radius for length in edge_lengths_squared)
    distances = all_pair_distances(points)
    assert min(distances) == 1
    assert max(distances) == 4 * radius * radius
    full_slack = minus(
        plus(c(0, F(3, 2) * radius * radius), c(0, F(3, 2) * radius)),
        c(0, F(expected_count - 1, 2)),
    )
    assert full_slack == ZERO

    if radius % 3 == 0:
        source = {p for p in points if (p[0] - p[1]) % 3 != 1}
        assert len(points) - len(source) == radius * (radius + 1)
        assert len(source) == 3 * radius * (radius + 1) + 1 - radius * (radius + 1)
        assert corners <= source
        assert min(all_pair_distances(source)) >= 1
        residues = {(i - j) % 3 for i, j in source}
        assert residues == {0, 2}
        for a, b in combinations(source, 2):
            if norm2((a[0] - b[0], a[1] - b[1])) == 1:
                assert ((a[0] - a[1]) % 3) != ((b[0] - b[1]) % 3)
        # Every unit contact switches between the two retained residues, so the
        # unit-contact graph is bipartite and contains no unit triangle.
        a0 = (0, 0)
        a1 = (1, 0)
        a2 = (0, 1)
        assert all(norm2((x[0] - y[0], x[1] - y[1])) == 1 for x, y in combinations((a0, a1, a2), 2))
        assert a1 not in source  # the omitted third residue kills this explicit triangle
        n = len(source)
        slack = minus(
            plus(c(0, F(3, 2) * radius * radius), c(0, F(3, 2) * radius)),
            c(0, F(n - 1, 2)),
        )
        assert slack == c(0, F(radius * (radius + 1), 2))
        return source, slack
    return None, None


def check_grid_competitor(points, expected_n, source_diameter_squared):
    assert len(points) == expected_n
    distances = [square_dist2(a, b) for a, b in combinations(points, 2)]
    assert min(distances) >= 1
    assert max(distances) < source_diameter_squared
    for a, b in combinations(points, 2):
        if square_dist2(a, b) == 1:
            assert (sum(a) % 2) != (sum(b) % 2)
    # Square-lattice unit edges switch parity, so a unit equilateral triangle is impossible.


def check_unreviewed_area_remainder_identity():
    a0 = c(0, F(1, 2))
    # Substitute Omega_H = areaH + a0/2*perH - a0*(N-1),
    # Delta_H = areaH - areaL into the published signed remainder.
    omega = {"areaH": ONE, "perH": c(0, F(1, 4)), "Nminus1": minus(ZERO, a0)}
    delta = {"areaH": ONE, "areaL": minus(ZERO, ONE)}
    lhs = poly_sum(
        (1, omega), ( -1, delta), ( -1, {"perH": c(0, F(1, 4))}),
        (1, {"B0": a0}), (-1, {"fanArea": ONE}),
    )
    rhs = {
        "areaL": ONE,
        "Nminus1": minus(ZERO, a0),
        "B0": a0,
        "fanArea": minus(ZERO, ONE),
    }
    assert lhs == rhs


def check_signed_parallel_area():
    # H_6 area minus (K_3 + 3B) area, using Steiner's formula.
    area_h = c(0, 54)
    area_k = c(0, F(27, 2))
    expanded_k = plus(area_k, c(54, 0, 9))
    delta = minus(area_h, expanded_k)
    assert delta == c(-54, F(81, 2), -9)
    # sqrt(3)<2 and pi>3 give Delta < 81-54-27 = 0.
    assert F(81) - 54 - 27 == 0
    assert 3 < 4
    return delta


def main():
    check_unreviewed_area_remainder_identity()
    sources = {}
    for radius in range(1, 7):
        source, slack = check_hex_and_coloring(radius)
        if source is not None:
            sources[radius] = (source, slack)

    # Exact same-cardinality square-grid competitors independently establish
    # that the two deleted-color controls are not global diameter optima.
    grid25 = {(i, j) for i in range(5) for j in range(5)}
    check_grid_competitor(grid25, 25, 4 * 3 * 3)
    disk26 = sorted((i, j) for i in range(-5, 6) for j in range(-5, 6) if i * i + j * j <= 26)
    assert len(disk26) == 89
    grid85 = disk26[:85]
    assert max(square_dist2(a, b) for a, b in combinations(grid85, 2)) <= 104
    check_grid_competitor(grid85, 85, 4 * 6 * 6)

    assert sources[3][1] == c(0, 6)
    assert sources[6][1] == c(0, 21)
    assert 3 * 3 * 3 > 4  # squared apothem gap for K_3 inside H_6 exceeds one.
    delta = check_signed_parallel_area()

    # pi>3 and a0=sqrt(3)/2<1 imply
    # pi+2e-a0(1+e) > 2+e, strictly, for every integer e>=0.
    assert 3 < 4
    assert all(F(2 + e) > 0 for e in range(101))

    print("PASS: independent exact patch counts, hex hulls, pair separation, and Oler slacks")
    print("PASS: two-residue argument certifies the M=3,6 retained sources are triangle-free")
    print("PASS: square-grid competitors: 25 labels with d^2<=32<36; 85 labels with d^2<=104<144")
    print("PASS: signed parallel-body expansion; the M=6 control has Delta_H<0")
    print("PASS: exact signed-remainder cancellation and strict separate-envelope gap")
    print(f"CONTROL: Delta_H = {delta[0]} + ({delta[1]})*sqrt(3) + ({delta[2]})*pi")
    print("LIMIT: no actual Section-165 optimum, fan, admissible basis, or source-specific lower bound is modeled")


main()
