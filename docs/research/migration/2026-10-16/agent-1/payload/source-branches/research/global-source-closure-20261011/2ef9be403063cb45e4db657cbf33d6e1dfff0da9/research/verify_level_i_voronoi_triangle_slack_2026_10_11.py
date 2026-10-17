#!/usr/bin/env python3
"""Exact finite Voronoi certificates for the full-source triangle-slack budget.

The physical coordinates are (x, sqrt(vertical_factor)*y), with rational x,y
and vertical_factor in {1,3}. No floating geometry or tolerance is used.
This checks the listed cells, triples, and constant arithmetic only. It does
not certify global fixture optimality, universal saturation extraction, or
an exact unit-triangle theorem for large global minimizers.
"""

from fractions import Fraction as F
from itertools import combinations


def dot(p, q, vertical_factor):
    return p[0] * q[0] + vertical_factor * p[1] * q[1]


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def dist2(p, q, vertical_factor):
    difference = sub(p, q)
    return dot(difference, difference, vertical_factor)


def clip(poly, normal, bound):
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        dp = sum(a * b for a, b in zip(p, normal)) - bound
        dq = sum(a * b for a, b in zip(q, normal)) - bound
        if dp <= 0:
            result.append(p)
        if (dp < 0 < dq) or (dq < 0 < dp):
            parameter = -dp / (dq - dp)
            result.append(tuple(a + parameter * (b - a) for a, b in zip(p, q)))
        elif dp > 0 and dq == 0:
            result.append(q)
    clean = []
    for p in result:
        if not clean or p != clean[-1]:
            clean.append(p)
    if len(clean) > 1 and clean[0] == clean[-1]:
        clean.pop()
    return clean


def voronoi_cell(points, vertical_factor):
    assert points[0] == (F(0), F(0))
    radius = F(10)
    poly = [(-radius, -radius), (radius, -radius),
            (radius, radius), (-radius, radius)]
    for q in points[1:]:
        poly = clip(poly, (q[0], vertical_factor * q[1]), dot(q, q, vertical_factor) / 2)
        assert len(poly) >= 3
    assert all(abs(coordinate) < radius for p in poly for coordinate in p)
    return poly


def area_coordinate(poly):
    return sum(p[0] * q[1] - p[1] * q[0]
               for p, q in zip(poly, poly[1:] + poly[:1])) / 2


def area_margin(area, vertical_factor, gamma):
    """Certify area*sqrt(factor) >= sqrt(3)/2 + min(gamma,1)/36."""
    eta = min(gamma, F(1))
    if vertical_factor == 1:
        remainder = area - eta / 36
        return remainder >= 0 and 4 * remainder * remainder >= 3
    if vertical_factor == 3:
        remainder = area - F(1, 2)
        return remainder >= 0 and 3 * remainder * remainder >= (eta / 36) ** 2
    raise ValueError("unsupported exact vertical factor")


def verify_fixture(name, points, vertical_factor):
    pairs = {ij: dist2(points[ij[0]], points[ij[1]], vertical_factor)
             for ij in combinations(range(len(points)), 2)}
    assert min(pairs.values()) >= 1
    triples = {
        ijk: sum(pairs[ij] for ij in combinations(ijk, 2)) - 3
        for ijk in combinations(range(len(points)), 3)
    }
    gamma = min(triples.values())
    assert gamma >= 0
    poly = voronoi_cell(points, vertical_factor)
    area = area_coordinate(poly)
    assert area > 0 and area_margin(area, vertical_factor, gamma)
    vertex_triples = 0
    for vertex in poly:
        radius2 = dot(vertex, vertex, vertical_factor)
        distances = [dist2(vertex, p, vertical_factor) for p in points]
        assert min(distances) == radius2
        closest = [i for i, d in enumerate(distances) if d == radius2]
        assert 0 in closest and len(closest) >= 3
        noncollinear = []
        for i, j in combinations(closest[1:], 2):
            p, q = points[i], points[j]
            if p[0] * q[1] != p[1] * q[0]:
                noncollinear.append((0, i, j))
        assert noncollinear
        assert radius2 >= (3 + gamma) / 9
        for indices in noncollinear:
            vectors = [sub(points[i], vertex) for i in indices]
            vector_sum = tuple(sum(v[axis] for v in vectors) for axis in range(2))
            side_sum = sum(pairs[ij] for ij in combinations(indices, 2))
            assert side_sum == 9 * radius2 - dot(vector_sum, vector_sum, vertical_factor)
            assert side_sum >= 3 + gamma
            vertex_triples += 1
    print(f"{name}: n={len(points)}, cell-sides={len(poly)}, "
          f"gamma={gamma}, coordinate-area={area}; exact radius and area margins pass")
    return len(pairs), len(triples), vertex_triples, area


def lattice_patch(u, v):
    points = [(F(0), F(0))]
    points.extend((i * u[0] + j * v[0], i * u[1] + j * v[1])
                  for i in range(-2, 3) for j in range(-2, 3) if (i, j) != (0, 0))
    return tuple(points)


def rational_circle(parameter, radius=F(1)):
    return (radius * (1 - parameter * parameter) / (1 + parameter * parameter),
            radius * 2 * parameter / (1 + parameter * parameter))


def verify():
    zero = (F(0), F(0))
    original_star = (zero, (F(1), F(0)), (F(-1, 2), F(1, 2)), (F(-1, 2), F(-1, 2)))
    additions = ((F(1, 2), F(1, 2)), (F(-1), F(0)), (F(1, 2), F(-1, 2)))
    fixtures = (
        ("triangular-lattice", lattice_patch((F(1), F(0)), (F(1, 2), F(1, 2))), F(3)),
        ("triangle-free-oblique", lattice_patch((F(1), F(0)), (F(8, 17), F(15, 17))), F(1)),
        ("square-lattice", lattice_patch((F(1), F(0)), (F(0), F(1))), F(1)),
        ("rectangular-lattice", lattice_patch((F(1), F(0)), (F(0), F(2))), F(1)),
        ("five-unit-neighbors", (zero,) + tuple(rational_circle(t) for t in
                                               (F(0), F(3, 4), F(3), F(-3), F(-3, 4))), F(1)),
        ("seven-separated-neighbors", (zero,) + tuple(rational_circle(t, F(5, 4)) for t in
                                                      (F(0), F(1, 2), F(5, 4), F(4), F(-4), F(-5, 4), F(-1, 2))), F(1)),
        ("original-three-arm-star", original_star, F(3)),
        ("completed-unit-hexagon", original_star + additions, F(3)),
    )
    pair_count = triple_count = vertex_count = 0
    for name, points, factor in fixtures:
        pairs, triples, vertices, _ = verify_fixture(name, points, factor)
        pair_count += pairs
        triple_count += triples
        vertex_count += vertices

    original_pairs = {ij: dist2(original_star[ij[0]], original_star[ij[1]], F(3))
                      for ij in combinations(range(len(original_star)), 2)}
    original_gamma = min(sum(original_pairs[ij] for ij in combinations(ijk, 2)) - 3
                         for ijk in combinations(range(len(original_star)), 3))
    completed_area = area_coordinate(voronoi_cell(original_star + additions, F(3)))
    assert original_gamma == 2 and completed_area == F(1, 2)
    assert not area_margin(completed_area, F(3), original_gamma)
    assert all(dist2(zero, p, F(3)) < 4 for p in additions)
    print("Hostile saturation check: original positive slack cannot be assigned to a cell with added neighbors")

    # Elementary 3<pi<22/7 and sqrt(3)<2 imply a>3/4 and a0/a<1.
    diameter = F(4096)
    assert (12 * F(22, 7) + 8) * diameter + 25 < 46 * diameter
    assert 46 * diameter < F(3, 8) * diameter * diameter
    assert 72 * 46 == 3312 and F(3312, 4096) < 1
    diameter = F(8192)
    assert 46 * diameter < F(3, 16) * diameter * diameter
    assert 144 * 46 == 6624 and F(6624, 8192) < 1
    assert F(36 * 46, 6624) == F(1, 4)
    assert 3 * 25 == 75 and 2 * 75 == 150
    print(f"PASS: {pair_count} exact source pair checks, {triple_count} exact source triple checks, "
          f"{vertex_count} exact defining-triple identities; finite examples and constants only")


if __name__ == "__main__":
    verify()
