#!/usr/bin/env python3
"""Exact ingredients for uniform cells and diameter-weighted access.

All fixtures are nonglobal. Stars certify one unloaded positive pinned
equilibrium. Circle/fan sources certify actual diameter geometry but no
canonical stress. Auxiliary bodies and pin subsets are not source cells.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json
from math import isqrt

from verify_target_c_face_tail_port_multiplicity_2026_10_08 import (
    area, bodies, circle_ports, convex, cross, d2, distance_polygon2,
    dot, sqrt_upper, sub,
)


def unit(t):
    return ((1 - t*t) / (1 + t*t), 2*t / (1 + t*t))


def angle_gt_30(u, v):
    p = dot(u, v)
    return p <= 0 or 4*p*p < 3*dot(u, u)*dot(v, v)


def star(t1, t2):
    c1, s1 = unit(t1)
    c2, s2 = unit(t2)
    a, x = (F(0), F(0)), (F(1), F(0))
    y, z = (1+c1, s1), (1+c2, -s2)
    points = [a, x, y, z]
    contact_edges = set()
    for i, j in combinations(range(4), 2):
        dist = d2(points[i], points[j])
        assert dist >= 1
        if dist == 1:
            contact_edges.add((i, j))
    assert contact_edges == {(0, 1), (1, 2), (1, 3)}
    assert angle_gt_30(sub(y, a), sub(z, a))
    weights = [s2*c1+s1*c2, s2, s1]
    rays = [sub(a, x), sub(y, x), sub(z, x)]
    assert all(w > 0 for w in weights)
    assert sum(w*r[0] for w, r in zip(weights, rays)) == 0
    assert sum(w*r[1] for w, r in zip(weights, rays)) == 0
    assert cross(rays[0], rays[1]) != 0  # full pinned column rank two
    assert max(d2(p, q) for p, q in combinations(points, 2)) > 2
    return 6


def star_fan(m):
    D = F(100*m*m)
    a = (F(0), F(0))
    pts = [a]
    for j in range(-m, m+1):
        u = unit(F(j, 100*m*m))
        pts.append((D*u[0], D*u[1]))
    return pts, D, (D/2, F(0)), F(m), F(1)


def geometry_fixture(points, D, center, r, eta, with_hub):
    degree = Counter()
    diameter_edges = []
    source_pairs = 0
    for i, j in combinations(range(len(points)), 2):
        s = d2(points[i], points[j])
        assert 1 < s <= D*D  # all these sources are contact-isolated
        if s == D*D:
            diameter_edges.append((i, j))
            degree[i] += 1
            degree[j] += 1
        source_pairs += 1
    assert all(degree[i] > 0 for i in range(len(points)))
    # Exact nonglobal certificate: an n-site square grid has diameter^2 <2n.
    assert 2*len(points) < D*D

    directions = []
    for i, j in diameter_edges:
        midpoint = ((points[i][0]+points[j][0])/2,
                    (points[i][1]+points[j][1])/2)
        assert d2(midpoint, center) <= r*r
        v = sub(points[j], points[i])
        directions.append((v[0]/D, v[1]/D))
    direction_checks = 0
    for u, v in combinations(directions, 2):
        assert 1-dot(u, v)**2 >= 1/(4*D*D)
        direction_checks += 1
    for p in points:
        rad2 = d2(p, center)
        assert (D/2-eta)**2 <= rad2 <= (D/2+eta)**2

    translated_bodies = [
        [(p[0]+center[0], p[1]+center[1]) for p in poly]
        for poly in bodies(int(D/2))]
    if with_hub:
        a = points[0]
        near_hub = [(a[0]+dx, a[1]+dy) for dx, dy in [
            (F(1), F(0)), (F(5, 4), -F(1, 4)),
            (F(7, 4), -F(1, 4)), (F(2), F(0)),
            (F(7, 4), F(1, 4)), (F(5, 4), F(1, 4)),
        ]]
        translated_bodies.append(near_hub)

    weight = [len(poly)-4 for poly in translated_bodies]
    eps = []
    for poly in translated_bodies:
        convex(poly)
        eps.append(sqrt_upper(2*area(poly))/D)
    distance = [[distance_polygon2(p, poly) for p in points]
                for poly in translated_bodies]
    radii = [1/D, F(1, 128), F(1, 32), F(1, 8)]
    weighted_identities = 0
    incidence_tests = 0
    hub_witnesses = 0
    const = 256*r+16
    for rho in radii:
        phi = [0]*len(points)
        rhs = 0
        for j, poly in enumerate(translated_bodies):
            near = [i for i, s in enumerate(distance[j])
                    if s <= rho*rho*D*D]
            incidence = sum(degree[i] for i in near)
            if incidence > const:
                assert (incidence-const)**2 <= (
                    (48*D)**2*(rho+eps[j]+eta/D))
            for i in near:
                phi[i] += weight[j]
            rhs += weight[j]*incidence
            incidence_tests += len(points)
            if with_hub and rho == 1/D and j == len(translated_bodies)-1:
                assert near == [0]
                assert incidence == len(diameter_edges) > len(near)
                hub_witnesses += 1
        assert sum(degree[i]*phi[i] for i in range(len(points))) == rhs
        bank = sum(weight)
        if rhs > bank*const:
            assert (rhs-bank*const)**2 <= (
                (48*D*bank)**2*(rho+max(eps)+eta/D))
        for threshold in (1, 2, 4, 8):
            bad_degree = sum(degree[i] for i in range(len(points))
                             if phi[i] >= threshold)
            assert threshold*bad_degree <= rhs
        weighted_identities += 1

    return {
        "vertices": len(points), "source_pairs": source_pairs,
        "actual_diameter_edges": len(diameter_edges),
        "direction_pair_checks": direction_checks,
        "weighted_identities": weighted_identities,
        "port_body_radius_tests": incidence_tests,
        "high_degree_single_port_witnesses": hub_witnesses,
        "nonglobal": True, "canonical_stress_certified": False,
    }


def impossible_pin_diagnostics(m):
    ports = circle_ports(m)
    D = F(2*m)
    thin = [p for p in ports if abs(p[1]) <= 3]
    convex(thin)
    assert len(thin) == 6
    assert all(angle_gt_30(sub(thin[i-1], thin[i]),
                           sub(thin[(i+1) % len(thin)], thin[i]))
               for i in range(len(thin)))
    assert max(d2(p, q) for p, q in combinations(thin, 2)) == D*D
    assert 3*len(thin) < D+1  # violates the necessary pinned count
    arc = [p for p in ports if p[0] >= F(9*m, 10)]
    convex(arc)
    assert any(not angle_gt_30(sub(arc[i-1], arc[i]),
                              sub(arc[(i+1) % len(arc)], arc[i]))
               for i in range(len(arc)))
    return {
        "m": m, "thin_actual_endpoint_subset": len(thin),
        "thin_cell_pinned_count_rejected": True,
        "small_arc_acute_angle_rejected": True,
        "actual_source_component_certified": False,
    }


if __name__ == "__main__":
    star_pairs = 0
    for t1 in (F(27, 100), F(3, 10), F(1, 3), F(1, 2)):
        for t2 in (F(27, 100), F(3, 10), F(1, 3), F(1, 2)):
            star_pairs += star(t1, t2)
    for N in (10, 100, 1000, 10000, 100000):
        t = F(2*N-isqrt(3*N*N), N)
        assert (2-t)**2 < 3
        assert (2-t+1/F(N))**2 > 3
        star_pairs += star(t, t)

    circles = []
    diagnostics = []
    for m in (16, 32, 64):
        circles.append(geometry_fixture(
            circle_ports(m), F(2*m), (F(0), F(0)), F(0), F(0), False))
        diagnostics.append(impossible_pin_diagnostics(m))
    fans = [geometry_fixture(*star_fan(m), True) for m in (8, 16, 32)]
    print(json.dumps({
        "status": "PASS", "scope": "exact finite geometry and pinned-star ingredients",
        "positive_pinned_stars": 21, "star_pair_checks": star_pairs,
        "circles": circles, "actual_diameter_fans": fans,
        "impossible_cell_diagnostics": diagnostics,
        "global_optimality_certified": False,
        "uniform_asymptotic_cells_certified_by_script": False,
        "finite_motion_certified": False,
    }, sort_keys=True))
