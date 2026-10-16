#!/usr/bin/env python3
"""Exact geometric tests for Type-II face-tail port multiplicity.

Circle points are actual diameter endpoints of nonglobal isolate-only
configurations. Auxiliary convex bodies and incidence masks are not
certified harmonic cells/faces. No stress, Type-II limit, source motion,
or global optimality is certified.
"""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json

PI_HI = F(22, 7)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def d2(a, b):
    t = sub(a, b)
    return dot(t, t)


def area(poly):
    return sum(cross(poly[i], poly[(i + 1) % len(poly)])
               for i in range(len(poly))) / 2


def circle_ports(m):
    points = set()
    for j in range(-m, m + 1):
        den = m * m + j * j
        p = (F(m * (m * m - j * j), den),
             F(2 * m * m * j, den))
        points.add(p)
        points.add((-p[0], -p[1]))
    # Exact angular order without floating-point trigonometry.
    def half(p):
        return 0 if p[1] > 0 or (p[1] == 0 and p[0] >= 0) else 1
    from functools import cmp_to_key
    def compare(a, b):
        ha, hb = half(a), half(b)
        if ha != hb:
            return -1 if ha < hb else 1
        c = cross(a, b)
        return -1 if c > 0 else (1 if c < 0 else 0)
    return sorted(points, key=cmp_to_key(compare))


def convex(poly):
    assert area(poly) > 0
    for i in range(len(poly)):
        assert cross(sub(poly[(i + 1) % len(poly)], poly[i]),
                     sub(poly[(i + 2) % len(poly)],
                         poly[(i + 1) % len(poly)])) > 0


def distance_segment2(p, a, b):
    v = sub(b, a)
    t = dot(sub(p, a), v) / dot(v, v)
    t = max(F(0), min(F(1), t))
    q = (a[0] + t * v[0], a[1] + t * v[1])
    return d2(p, q)


def distance_polygon2(p, poly):
    if all(cross(sub(poly[(i + 1) % len(poly)], poly[i]),
                 sub(p, poly[i])) >= 0 for i in range(len(poly))):
        return F(0)
    return min(distance_segment2(p, poly[i], poly[(i + 1) % len(poly)])
               for i in range(len(poly)))


def sqrt_upper(q, den=10**6):
    assert q >= 0
    n = isqrt(q.numerator * den * den // q.denominator)
    if F(n * n, den * den) < q:
        n += 1
    out = F(n, den)
    assert out * out >= q
    return out


def bodies(m):
    hexagon = [
        (-F(3 * m, 4), F(0)), (-F(m, 2), -F(1, 4)),
        (F(m, 2), -F(1, 4)), (F(3 * m, 4), F(0)),
        (F(m, 2), F(1, 4)), (-F(m, 2), F(1, 4)),
    ]
    vertical = [(-y, x) for x, y in hexagon]
    tangent = [
        (-F(1), F(m) - F(3, 2 * m)),
        (-F(1, 2), F(m) - F(2, m)),
        (F(1, 2), F(m) - F(2, m)),
        (F(1), F(m) - F(3, 2 * m)),
        (F(1, 2), F(m) - F(1, m)),
        (-F(1, 2), F(m) - F(1, m)),
    ]
    shifted = [(x, y + F(m, 4)) for x, y in hexagon]
    octagon = [
        (-F(3 * m, 4), -F(1, 8)), (-F(m, 2), -F(1, 4)),
        (F(m, 2), -F(1, 4)), (F(3 * m, 4), -F(1, 8)),
        (F(3 * m, 4), F(1, 8)), (F(m, 2), F(1, 4)),
        (-F(m, 2), F(1, 4)), (-F(3 * m, 4), F(1, 8)),
    ]
    diagonal = [(F(3, 5) * x - F(4, 5) * y,
                 F(4, 5) * x + F(3, 5) * y) for x, y in octagon]
    return [hexagon, vertical, tangent, shifted, diagonal]


def fixture(m):
    ports = circle_ports(m)
    n = len(ports)
    assert n == 4 * m
    D = F(2 * m)
    assert all(dot(p, p) == m * m for p in ports)
    assert all((-p[0], -p[1]) in ports for p in ports)
    convex(ports)
    pairs = 0
    for a, b in combinations(ports, 2):
        s = d2(a, b)
        assert 1 < s <= D * D  # all contacts absent
        pairs += 1
    # A square-grid placement has diameter^2 < 2n, hence beats this.
    assert 2 * n < D * D

    polys = bodies(m)
    lines, epsilons, weights = [], [], []
    body_vertex_checks = 0
    for poly in polys:
        convex(poly)
        assert all(dot(p, p) < m * m for p in poly)
        S = area(poly)
        x, y = max(combinations(poly, 2), key=lambda pair: d2(*pair))
        v = sub(y, x)
        L2 = dot(v, v)
        eps = sqrt_upper(2 * S) / D
        assert eps * eps * D * D >= 2 * S
        for z in poly:
            height_num = cross(v, sub(z, x))
            assert height_num * height_num <= 2 * S * L2
            assert abs(height_num) <= 2 * S
            body_vertex_checks += 1
        lines.append((x, v, L2))
        epsilons.append(eps)
        weights.append(len(poly) - 4)
    eps_max = max(epsilons)

    # Overlapping incidence masks deliberately count shared ports.
    masks = [set(range(n)), {i for i in range(n) if i % 2 == 0},
             {i for i in range(n) if i % 3 != 0}]
    distances = [[distance_polygon2(p, poly) for p in ports]
                 for poly in polys]
    radii = [F(1, 128), F(1, 64), F(1, 32), F(1, 16),
             F(1, 8), F(1, 4), F(1, 2)]
    incidence_tests = 0
    identities = 0
    nonempty_neighborhoods = 0
    markov_checks = 0
    for rho in radii:
        phi = {(i, g): 0 for g, mask in enumerate(masks) for i in mask}
        rhs = 0
        for j, poly in enumerate(polys):
            g = j % len(masks)
            x, v, L2 = lines[j]
            near = {i for i, s in enumerate(distances[j])
                    if s <= rho * rho * D * D}
            count = len(near)
            nonempty_neighborhoods += bool(count)
            for i in near:
                height_num = cross(v, sub(ports[i], x))
                envelope = (rho + epsilons[j]) * D
                assert height_num * height_num <= envelope * envelope * L2
            if count > 8:
                assert (count - 8)**2 <= 144 * (rho + epsilons[j]) * D * D
            for i in masks[g]:
                if i in near:
                    phi[i, g] += weights[j]
            rhs += weights[j] * len(near & masks[g])
            incidence_tests += n
        assert sum(phi.values()) == rhs
        bank = sum(weights)
        if rhs > 8 * bank:
            assert (rhs - 8 * bank)**2 <= (
                144 * (rho + eps_max) * D * D * bank * bank)
        for threshold in [1, 2, 4, 8]:
            bad = sum(value >= threshold for value in phi.values())
            assert bad * threshold <= rhs
            markov_checks += 1
        identities += 1

    strip_tests = 0
    normals = [(F(1), F(0)), (F(0), F(1)),
               (F(3, 5), F(4, 5)), (-F(5, 13), F(12, 13))]
    offsets = [F(0), F(m, 2), F(m) - F(1, m), F(m), F(m) + F(1, m)]
    for normal in normals:
        assert dot(normal, normal) == 1
        for offset in offsets:
            for rho in [F(0)] + radii:
                count = sum(abs(dot(normal, p) - offset) <= rho * D
                            for p in ports)
                if count > 8:
                    assert (count - 8)**2 <= 144 * rho * D * D
                strip_tests += 1

    # Every prescribed hull vertex supplies a uniformly large triangle.
    S = area(ports)
    triangles = 0
    for i, a in enumerate(ports):
        b = max(ports, key=lambda p: d2(a, p))
        v = sub(b, a)
        L2 = dot(v, v)
        assert S <= PI_HI * L2
        heights = [cross(v, sub(p, a)) for p in ports]
        spread = max(heights) - min(heights)
        assert S * S * L2 <= D * D * spread * spread
        c = max(ports, key=lambda p: abs(cross(v, sub(p, a))))
        A = abs(cross(v, sub(c, a))) / 2
        assert A * A >= S * S * L2 / (16 * D * D)
        assert A * A >= S**3 / (16 * PI_HI * D * D)
        base2 = d2(b, c)
        signed_num = cross(sub(c, b), sub(a, b))
        H2 = signed_num * signed_num / base2
        assert H2 >= 4 * A * A / (D * D)
        assert base2 >= 4 * A * A / (D * D)
        ib, ic = ports.index(b), ports.index(c)
        assert (ib - ic) % n not in (1, n - 1)
        assert a != b and b != c and a != c
        triangles += 1

    return {
        "m": m, "actual_diameter_ports": n, "full_source_pairs": pairs,
        "auxiliary_convex_bodies": len(polys),
        "flatness_vertex_checks": body_vertex_checks,
        "port_body_radius_tests": incidence_tests,
        "weighted_identities": identities,
        "nonempty_body_neighborhoods": nonempty_neighborhoods,
        "markov_checks": markov_checks, "strip_tests": strip_tests,
        "prescribed_port_triangles": triangles,
        "nonglobal": True, "contact_isolated": True,
        "source_augmented_faces_certified": False,
        "global_optimality_certified": False,
    }


if __name__ == "__main__":
    fixtures = [fixture(m) for m in (16, 32, 64)]
    assert sum(x["nonempty_body_neighborhoods"] for x in fixtures) > 0
    print(json.dumps({"status": "PASS", "scope": "exact geometry and counting only",
                      "fixtures": fixtures}, sort_keys=True))
