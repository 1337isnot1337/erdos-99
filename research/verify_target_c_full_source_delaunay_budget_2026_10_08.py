#!/usr/bin/env python3
"""Exact finite full-source Delaunay ledger and local blocker fixtures.

The report proves universal claims analytically. Every fixture is nonglobal.
No KKT support, full-source replacement or global optimality is certified.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_voronoi_spacing_debit_2026_10_08 as geom

Q = geom.Q
add, sub, scale = geom.add, geom.sub, geom.scale
dot, norm, cross = geom.dot, geom.norm, geom.cross
qdiv, area = geom.qdiv, geom.area
A = geom.A0*F(1, 2)
A0 = geom.A0


def circumcircle(p, q, r):
    v, w = sub(q, p), sub(r, p)
    denominator = 2*cross(v, w)
    assert denominator.sign() > 0
    relative = (
        qdiv(norm(v)*w[1]-norm(w)*v[1], denominator),
        qdiv(v[0]*norm(w)-w[0]*norm(v), denominator),
    )
    return add(p, relative), norm(relative)


def boundary_labels(points, hull):
    cells = geom.full_clipped_cells(points, hull)
    labels = set()
    covering_checks = 0
    for i, (p, cell) in enumerate(zip(points, cells)):
        for relative in cell:
            assert (1-norm(relative)).sign() >= 0
            covering_checks += 1
            z = add(p, relative)
            for a, b in zip(hull, hull[1:]+hull[:1]):
                value = cross(sub(b, a), sub(z, a))
                assert value.sign() >= 0
                if value == Q():
                    labels.add(i)
    assert sum(area(cell) for cell in cells) == area(hull)
    return labels, covering_checks


def pair_ledger(points, diameter2):
    contacts = set()
    count = 0
    for i, j in combinations(range(len(points)), 2):
        d2 = norm(sub(points[i], points[j]))
        assert (d2-1).sign() >= 0 and (diameter2-d2).sign() >= 0
        if d2 == Q(1):
            contacts.add((i, j))
        count += 1
    neighbors = {i: set() for i in range(len(points))}
    for i, j in contacts:
        neighbors[i].add(j)
        neighbors[j].add(i)
    assert all(not (neighbors[i] & neighbors[j]) for i, j in contacts)
    return contacts, count



def convex_hull_indices(points, labels):
    from functools import cmp_to_key
    def compare(i, j):
        x = (points[i][0]-points[j][0]).sign()
        return x if x else (points[i][1]-points[j][1]).sign()
    ordered = sorted(labels, key=cmp_to_key(compare))
    def chain(sequence):
        result = []
        for i in sequence:
            while len(result) >= 2 and cross(
                sub(points[result[-1]], points[result[-2]]),
                sub(points[i], points[result[-1]])
            ).sign() <= 0:
                result.pop()
            result.append(i)
        return result
    if len(ordered) <= 1:
        return ordered
    return chain(ordered)[:-1]+chain(list(reversed(ordered)))[:-1]


def lower_closed_front_checks(points, delta, directions, exceptions):
    arrow_pair_checks = closure_checks = front_support_checks = 0
    roots = [0, len(points)-1, len(points)//2]
    for direction in directions:
        arrows = {i: [] for i in range(len(points))}
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                if i == j:
                    continue
                relative = sub(x, y)
                if (1-norm(sub(relative, scale(direction, delta)))).sign() > 0:
                    assert dot(direction, relative).sign() > 0
                    arrows[i].append(j)
                arrow_pair_checks += 1
        for root in roots:
            selected = {root}
            pending = [root]
            while pending:
                i = pending.pop()
                for j in arrows[i]:
                    if j not in selected:
                        selected.add(j)
                        pending.append(j)
            assert all(set(arrows[i]) <= selected for i in selected)
            hull = convex_hull_indices(points, selected)
            if len(hull) < 3:
                assert selected <= exceptions
            else:
                for i, j in zip(hull, hull[1:]+hull[:1]):
                    side = sub(points[j], points[i])
                    outward = (side[1], -side[0])
                    if dot(outward, direction).sign() <= 0:
                        on_side = [
                            k for k in selected
                            if cross(side, sub(points[k], points[i])) == Q()
                        ]
                        assert set(on_side) <= exceptions
                        front_support_checks += len(on_side)
            closure_checks += 1
    return arrow_pair_checks, closure_checks, front_support_checks

def grid_case(m, enlarged):
    t = F(1, 100*m*m)
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    cosine = Q(c/2)-A0*s
    sine = A0*c+Q(s/2)
    lam = 1+F(1, 100*m*m) if enlarged else F(1)
    u, v = (Q(lam), Q()), (cosine*lam, sine*lam)
    points = [add(scale(u, i), scale(v, j))
              for j in range(m+1) for i in range(m+1)]
    diameter2 = norm(scale(add(u, v), m))
    hull = [(Q(), Q()), scale(u, m), scale(add(u, v), m), scale(v, m)]
    contacts, source_pairs = pair_ledger(points, diameter2)
    expected = set()
    if not enlarged:
        for j in range(m+1):
            for i in range(m+1):
                x = j*(m+1)+i
                if i < m:
                    expected.add((x, x+1))
                if j < m:
                    expected.add((x, x+m+1))
    assert contacts == expected
    boundary, covering_checks = boundary_labels(points, hull)
    expected_boundary = {
        j*(m+1)+i for j in range(m+1) for i in range(m+1)
        if i in (0, m) or j in (0, m)
    }
    assert boundary == expected_boundary
    hull_labels = len(boundary)
    triangles = []
    for j in range(m):
        for i in range(m):
            p = j*(m+1)+i
            triangles.extend([(p, p+1, p+m+1),
                              (p+m+2, p+m+1, p+1)])
    assert len(triangles) == 2*len(points)-hull_labels-2
    edges = {}
    incident = {i: [] for i in range(len(points))}
    neighbors = {i: set() for i in range(len(points))}
    boundary_faces, mixed_faces, good_faces = [], [], []
    empty_circle_checks = 0
    surplus = Q()
    for index, triangle in enumerate(triangles):
        p, q, r = [points[i] for i in triangle]
        center, radius2 = circumcircle(p, q, r)
        assert (1-radius2).sign() >= 0
        for z in points:
            assert (norm(sub(z, center))-radius2).sign() >= 0
            empty_circle_checks += 1
        face_area = cross(sub(q, p), sub(r, p))*F(1, 2)
        assert face_area == lam*lam*sine*F(1, 2)
        sigma = face_area-A
        assert sigma.sign() > 0 and (F(1, 100)-sigma).sign() > 0
        for a, b, c in [(p, q, r), (q, r, p), (r, p, q)]:
            assert dot(sub(b, a), sub(c, a)).sign() > 0
        for a, b in combinations(triangle, 2):
            edge = tuple(sorted((a, b)))
            edges.setdefault(edge, []).append(index)
            neighbors[a].add(b)
            neighbors[b].add(a)
            assert (F(121, 100)-norm(sub(points[a], points[b]))).sign() > 0
            assert ((1+5*sigma)*(1+5*sigma)
                    -norm(sub(points[a], points[b]))).sign() >= 0
        for a in triangle:
            incident[a].append(index)
        in_boundary = sum(i in boundary for i in triangle)
        if in_boundary == 3:
            boundary_faces.append(triangle)
        else:
            good_faces.append(triangle)
            surplus += sigma
            if in_boundary:
                mixed_faces.append(triangle)
    assert len(boundary_faces) == 2
    assert len(boundary_faces) <= 2*len(boundary)-hull_labels-2
    mixed_edges = {
        e for e in edges if (e[0] in boundary) != (e[1] in boundary)
    }
    assert all(len(edges[e]) == 2 for e in mixed_edges)
    assert len(mixed_faces) == len(mixed_edges)
    assert len(mixed_edges) <= 24*len(boundary)
    wall = set(boundary)
    for i in boundary:
        wall.update(neighbors[i])
    assert len(wall) <= 25*len(boundary)
    regular = set(range(len(points)))-wall
    assert len(regular) == (m-3)**2
    assert all(len(neighbors[i]) == len(incident[i]) == 6 for i in regular)
    total_area = area(hull)
    boundary_area = sum(
        cross(sub(points[q], points[p]), sub(points[r], points[p]))*F(1, 2)
        for p, q, r in boundary_faces
    )
    assert surplus+boundary_area+A*len(good_faces) == total_area
    assert (surplus+boundary_area-total_area+A0*(len(points)-1)
            == A*(hull_labels+len(boundary_faces)))
    assert (A0*(len(boundary)-1)
            -A*(hull_labels+len(boundary_faces))).sign() >= 0
    delta = F(1, m*m)
    epsilon = delta/20
    assert delta <= F(1, 10)
    directions = []
    for tangent in [F(0), F(1, 4), F(-1, 4), F(1, 2), F(-1, 2),
                    F(1), F(-1), F(2), F(-2), F(4), F(-4)]:
        directions.append((Q((1-tangent*tangent)/(1+tangent*tangent)),
                           Q(2*tangent/(1+tangent*tangent))))
    blocker_direction_checks = blocker_pair_checks = 0
    for i in regular:
        for j in neighbors[i]:
            assert ((1+epsilon)**2-norm(sub(points[i], points[j]))).sign() >= 0
        for direction in directions:
            assert norm(direction) == Q(1)
            blockers = []
            for j in neighbors[i]:
                relative = sub(points[i], points[j])
                new_relative = sub(relative, scale(direction, delta))
                if (1-norm(new_relative)).sign() > 0:
                    blockers.append(relative)
                blocker_pair_checks += 1
            assert len(blockers) >= 2
            assert any(
                cross(direction, r).sign() <= 0
                and cross(direction, s).sign() >= 0
                for r, s in combinations(blockers, 2)
            ) or any(
                cross(direction, s).sign() <= 0
                and cross(direction, r).sign() >= 0
                for r, s in combinations(blockers, 2)
            )
            blocker_direction_checks += 1
    arrow_pairs, closures, front_supports = lower_closed_front_checks(
        points, delta, [directions[i] for i in (0, 3, 5)], wall)
    square = [(Q(i), Q(j)) for j in range(m+1) for i in range(m+1)]
    competitor_pairs = 0
    for p, q in combinations(square, 2):
        d2 = norm(sub(p, q))
        assert (d2-1).sign() >= 0 and (diameter2-d2).sign() > 0
        competitor_pairs += 1
    return {
        "M": m, "enlarged": enlarged, "source_labels": len(points),
        "source_pairs": source_pairs, "competitor_pairs": competitor_pairs,
        "boundary_labels": len(boundary), "clipped_cells": len(points),
        "covering_vertex_checks": covering_checks,
        "triangular_faces": len(triangles),
        "empty_circumcircle_checks": empty_circle_checks,
        "all_boundary_faces": len(boundary_faces),
        "mixed_edges": len(mixed_edges), "mixed_faces": len(mixed_faces),
        "boundary_neighbor_labels": len(wall),
        "regular_six_neighbor_labels": len(regular),
        "blocker_direction_checks": blocker_direction_checks,
        "blocker_pair_checks": blocker_pair_checks,
        "complete_lower_arrow_pair_checks": arrow_pairs,
        "lower_closed_sets": closures,
        "exceptional_front_support_checks": front_supports,
        "contact_isolated_labels": len(points) if enlarged else 0,
    }


def thin_triangle():
    points = [(Q(), Q()), (Q(1), Q()), (Q(2), Q(F(1, 10)))]
    diameter2 = Q(F(401, 100))
    contacts, pairs = pair_ledger(points, diameter2)
    assert contacts == {(0, 1)}
    boundary, vertex_checks = boundary_labels(points, points)
    assert boundary == {0, 1, 2}
    center, radius2 = circumcircle(*points)
    assert (radius2-1).sign() > 0
    assert (A-area(points)).sign() > 0
    assert all(norm(sub(p, center)) == radius2 for p in points)
    competitor = [(Q(), Q()), (Q(1), Q()), (Q(F(1, 2)), A0)]
    count = 0
    for p, q in combinations(competitor, 2):
        assert norm(sub(p, q)) == Q(1)
        assert (diameter2-norm(sub(p, q))).sign() > 0
        count += 1
    return {
        "source_pairs": pairs, "competitor_pairs": count,
        "clipped_cells": 3, "covering_vertex_checks": vertex_checks,
        "boundary_labels": 3, "all_boundary_faces": 1,
        "circumradius_exceeds_one": True, "area_below_sqrt3_over_four": True,
        "competitor_has_unit_triangle": True,
    }


if __name__ == "__main__":
    result = {
        "status": "PASS",
        "grids": [grid_case(m, enlarged) for m in (4, 6, 8)
                  for enlarged in (False, True)],
        "thin_boundary_triangle": thin_triangle(),
        "does_not_prove": [
            "universal analytic assertions by finite enumeration",
            "global optimality of any fixture",
            "stress or KKT support on isolated labels",
            "a common source-wide phase or defect-localized strain",
            "compatible full-source finite motion or integer payment",
            "C-II or Level I closure",
        ],
    }
    print(json.dumps(result, indent=2))
