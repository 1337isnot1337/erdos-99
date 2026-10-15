#!/usr/bin/env python3
"""Finite Voronoi geometry and exact spacing-debit arithmetic.

Universal statements are analytic in the report. Grid fixtures have explicit
same-cardinality strict competitors. The hexagon equality fixture contains
unit triangles and has no global-optimality certificate here.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as field

Q = field.Q
A0 = Q(F(0), F(1, 2))


def qdiv(a, b):
    a, b = Q.of(a), Q.of(b)
    denominator = b.a*b.a-3*b.b*b.b
    assert denominator
    conjugate = Q(b.a, -b.b)
    numerator = a*conjugate
    return Q(numerator.a/denominator, numerator.b/denominator)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def scale(a, t):
    return a[0]*t, a[1]*t


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def norm(a):
    return dot(a, a)


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def area(polygon):
    return sum(cross(a, b) for a, b in zip(polygon, polygon[1:]+polygon[:1]))*F(1, 2)


def clip(polygon, normal, threshold):
    result = []
    for a, b in zip(polygon, polygon[1:]+polygon[:1]):
        da, db = dot(a, normal)-threshold, dot(b, normal)-threshold
        inside_a, inside_b = da.sign() <= 0, db.sign() <= 0
        if inside_a:
            result.append(a)
        if inside_a != inside_b:
            result.append(add(a, scale(sub(b, a), qdiv(da, da-db))))
    compact = []
    for p in result:
        if not compact or compact[-1] != p:
            compact.append(p)
    if len(compact) > 1 and compact[0] == compact[-1]:
        compact.pop()
    return compact


def full_clipped_cells(points, hull):
    cells = []
    for x in points:
        relative = [sub(p, x) for p in hull]
        for y in points:
            if y == x:
                continue
            normal = sub(y, x)
            relative = clip(relative, normal, norm(normal)*F(1, 2))
            assert len(relative) >= 3
        cells.append(relative)
    return cells


def grid_case(m, enlarged):
    delta = F(1, 10*m)
    lam = 1+delta+delta*delta if enlarged else F(1)
    t = F(1, 100*m*m)
    rotation = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    cos = Q(rotation[0]/2)-A0*rotation[1]
    sin = A0*rotation[0]+Q(rotation[1]/2)
    assert cos*cos+sin*sin == Q(1)
    assert cos.sign() > 0 and (Q(F(1, 2))-cos).sign() > 0
    assert (sin-A0).sign() > 0
    u, v = (Q(lam), Q()), (cos*lam, sin*lam)
    points = [add(scale(u, i), scale(v, j))
              for j in range(m+1) for i in range(m+1)]
    diameter2 = norm(scale(add(u, v), m))
    contacts, diameters = set(), set()
    source_pairs = 0
    minimum2 = None
    for i, j in combinations(range(len(points)), 2):
        d2 = norm(sub(points[i], points[j]))
        assert (d2-1).sign() >= 0 and (diameter2-d2).sign() >= 0
        if d2 == Q(1):
            contacts.add((i, j))
        if d2 == diameter2:
            diameters.add((i, j))
        if minimum2 is None or (minimum2-d2).sign() > 0:
            minimum2 = d2
        source_pairs += 1
    assert minimum2 == Q(lam*lam)
    assert diameters == {(0, len(points)-1)}
    expected_contacts = set()
    if not enlarged:
        for j in range(m+1):
            for i in range(m+1):
                index = j*(m+1)+i
                if i < m:
                    expected_contacts.add((index, index+1))
                if j < m:
                    expected_contacts.add((index, index+m+1))
    assert contacts == expected_contacts
    neighbors = {i: set() for i in range(len(points))}
    for i, j in contacts:
        neighbors[i].add(j)
        neighbors[j].add(i)
    assert all(not (neighbors[i] & neighbors[j]) for i, j in contacts)
    near_isolated = []
    for i, x in enumerate(points):
        if all(i == j or (norm(sub(x, y))-(1+delta)**2).sign() > 0
               for j, y in enumerate(points)):
            near_isolated.append(i)
    assert len(near_isolated) == (len(points) if enlarged else 0)
    hull = [(Q(), Q()), scale(u, m), scale(add(u, v), m), scale(v, m)]
    cells = full_clipped_cells(points, hull)
    total_area = Q()
    boundary_area = Q()
    surplus = Q()
    boundary_count = full_count = vertex_checks = 0
    for i, (x, cell) in enumerate(zip(points, cells)):
        cell_area = area(cell)
        assert cell_area.sign() > 0
        total_area += cell_area
        touches = False
        for relative in cell:
            assert (1-norm(relative)).sign() >= 0
            vertex_checks += 1
            absolute = add(x, relative)
            for a, b in zip(hull, hull[1:]+hull[:1]):
                side = cross(sub(b, a), sub(absolute, a))
                assert side.sign() >= 0
                if side == Q():
                    touches = True
        if touches:
            boundary_count += 1
            boundary_area += cell_area
        else:
            full_count += 1
            assert cell_area == sin*lam*lam
            assert (cell_area-A0).sign() > 0
            assert all((norm(r)-F(1, 3)).sign() >= 0 for r in cell)
            if enlarged:
                assert (cell_area-A0-delta).sign() >= 0
            surplus += cell_area-A0
    assert boundary_count == 4*m
    assert full_count == (m-1)**2
    hull_area = area(hull)
    assert total_area == hull_area == m*m*lam*lam*sin
    assert surplus+boundary_area == hull_area-A0*full_count
    assert (64*diameter2-(boundary_count-1)**2).sign() >= 0
    square = [(Q(i), Q(j)) for j in range(m+1) for i in range(m+1)]
    competitor_pairs = 0
    for a, b in combinations(square, 2):
        d2 = norm(sub(a, b))
        assert (d2-1).sign() >= 0 and (diameter2-d2).sign() > 0
        competitor_pairs += 1
    return {
        "M": m, "enlarged": enlarged, "source_labels": len(points),
        "source_pairs": source_pairs, "competitor_pairs": competitor_pairs,
        "clipped_cells": len(cells), "full_cells": full_count,
        "boundary_cells": boundary_count, "covering_vertex_checks": vertex_checks,
        "delta_near_isolated_labels": len(near_isolated),
    }


def equality_cell():
    neighbors = [
        (Q(1), Q()), (Q(F(1, 2)), A0), (Q(F(-1, 2)), A0),
        (Q(-1), Q()), (Q(F(-1, 2)), -A0), (Q(F(1, 2)), -A0),
    ]
    points = [(Q(), Q())]+neighbors
    cell = [(-Q(2), -Q(2)), (Q(2), -Q(2)), (Q(2), Q(2)), (-Q(2), Q(2))]
    for p in neighbors:
        cell = clip(cell, p, norm(p)*F(1, 2))
    assert len(cell) == 6 and area(cell) == A0
    contacts = set()
    pairs = 0
    for i, j in combinations(range(7), 2):
        d2 = norm(sub(points[i], points[j]))
        assert (d2-1).sign() >= 0 and (4-d2).sign() >= 0
        if d2 == Q(1):
            contacts.add((i, j))
        pairs += 1
    triangles = [
        (i, j, k) for i, j, k in combinations(range(7), 3)
        if {(i, j), (i, k), (j, k)} <= contacts
    ]
    assert len(triangles) == 6
    return {"source_pairs": pairs, "cell_vertices": len(cell), "unit_triangles": len(triangles)}


def atan_bounds(x, terms):
    value = sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms))
    next_term = (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(value, value+next_term), max(value, value+next_term)


def arithmetic():
    tangent = F(1, 5)
    twice = 2*tangent/(1-tangent*tangent)
    four = 2*twice/(1-twice*twice)
    assert (four-F(1, 239))/(1+four/239) == 1
    low5, high5 = atan_bounds(F(1, 5), 16)
    low239, high239 = atan_bounds(F(1, 239), 4)
    pi_low, pi_high = 16*low5-4*high239, 16*high5-4*low239
    assert F(157, 50) < pi_low < pi_high < F(22, 7)
    assert F(26, 15)**2 > 3
    delta_low = F(471, 520)
    assert pi_low/(2*F(26, 15)) > delta_low
    margin = F(191, 48)*delta_low-F(11, 7)-2
    assert margin == F(5727, 174720) > 0
    base_checks = 0
    for q in range(1, 1001):
        m = 576*q*q
        diameter = F(m)+F(1, 16*m)
        base = 8*q+7+(diameter/7).__ceil__()
        assert base < diameter/5
        assert diameter*diameter*(diameter+1)/(diameter+2)**2 >= diameter-3
        lam = 1+2/diameter
        upper = diameter/5+pi_high*diameter/(2*lam)-delta_low*diameter**2*(1-1/(lam*lam))
        assert upper < -F(9, 5)*diameter
        base_checks += 1
    return {"pi_bounds_certified": True, "all_q_arithmetic_samples": base_checks,
            "rational_margin": f"{margin.numerator}/{margin.denominator}"}


def main():
    result = {
        "status": "PASS",
        "grid_fixtures": [grid_case(m, enlarged) for m in (4, 6, 8)
                          for enlarged in (False, True)],
        "triangular_equality_fixture": equality_cell(),
        "spacing_debit_arithmetic": arithmetic(),
        "does_not_prove": [
            "universal assertions by finite sampling",
            "global optimality of any fixture",
            "an upper bound on all contact-isolated source labels",
            "canonical shallow closure or high-degree merger control",
            "C-II or Level I closure",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
