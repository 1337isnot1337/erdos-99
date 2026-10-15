#!/usr/bin/env python3
"""Exact source-realized fan path congestion and cap-safety samples.

The report proves the all-q family and universal cap lemma analytically.
Samples certify nonglobal configurations, not canonical KKT sources.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g

Q = g.Q


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def scale(p, s):
    return p[0]*s, p[1]*s


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def norm(p):
    return dot(p, p)


def dist2(a, b):
    return norm(sub(a, b))


def sqrt_upper(r, denominator):
    assert r > 0
    squared = r.numerator*denominator**2
    n = isqrt(squared//r.denominator)
    if n*n*r.denominator == squared:
        return F(n, denominator)
    return F(n+1, denominator)


def family(q):
    k = 3*q
    m = 64*k*k
    sigma = F(1, 4*m)
    diameter = F(m)+F(1, 16*m)
    delta = 1/diameter
    w = (1-sigma*sigma)/(1+sigma*sigma)
    rotation = 1-delta*delta/2, delta*w
    assert norm(rotation) == 1 and w*w == 1-delta*delta/4
    rho = 1+delta*delta/100
    stretch = 1+F(1, k)
    denominator = 10**6*m**6
    a = F(0), F(0)
    wall = {
        j: scale(g.power(rotation, j), diameter)
        for j in range(-1, k+2)
    }
    row = {
        j: (diameter-3+stretch*(diameter-wall[j][0]), wall[j][1])
        for j in range(k+1)
    }
    points, names = [a], ["carrier"]
    labels = {}

    def put(name, point):
        assert name not in labels
        labels[name] = len(points)
        points.append(point)
        names.append(name)
        return labels[name]

    wall_labels = {j: put(f"wall:{j}", wall[j]) for j in wall}
    row_labels = {j: put(f"row:{j}", row[j]) for j in row}
    connectors = {}
    roots = list(range(0, k+1, 3))
    construction_checks = 0
    for i in roots:
        u = scale(wall[i], 1/diameter)
        first = sub(wall[i], scale(u, rho))
        entry = row[i]
        v = sub(entry, first)
        squared = norm(v)
        radicand = (rho*rho-squared/4)/squared
        lam = sqrt_upper(radicand, denominator)
        midpoint = scale(add(first, entry), F(1, 2))
        middle = add(midpoint, scale((-v[1], v[0]), lam))
        assert rho*rho <= dist2(first, middle)
        assert rho*rho <= dist2(middle, entry)
        assert dist2(first, middle) < (1+delta*delta/50)**2
        assert dist2(middle, entry) < (1+delta*delta/50)**2
        assert F(198, 100) <= diameter-middle[0] <= F(202, 100)
        assert abs(middle[1]-wall[i][1]) < F(17, 100)
        first_label = put(f"first:{i}", first)
        middle_label = put(f"middle:{i}", middle)
        connectors[i] = first_label, middle_label
        construction_checks += 6

    trunk_count = (diameter/7).__ceil__()
    trunk = [
        put(f"trunk:{j}", (diameter-3-j*rho, F(0)))
        for j in range(1, trunk_count+1)
    ]
    assert len(points) == 8*q+7+trunk_count
    assert len(points) < diameter
    assert len(set(points)) == len(points)
    expected_contacts = {
        tuple(sorted((wall_labels[j], wall_labels[j+1])))
        for j in range(-1, k+1)
    }
    expected_diameters = {(0, wall_labels[j]) for j in wall}
    contacts, diameters, near_pairs = set(), set(), set()
    pair_checks = 0
    inner_diameter_squared = F(0)
    for i, j in combinations(range(len(points)), 2):
        squared = dist2(points[i], points[j])
        assert 1 <= squared <= diameter*diameter, (q, names[i], names[j])
        if squared == 1:
            contacts.add((i, j))
        if squared == diameter*diameter:
            diameters.add((i, j))
        if squared <= (1+delta)**2:
            near_pairs.add((i, j))
        if i != 0:
            inner_diameter_squared = max(inner_diameter_squared, squared)
        pair_checks += 1
    assert contacts == expected_contacts
    assert diameters == expected_diameters
    assert inner_diameter_squared < diameter*diameter
    translated_diameter_squared = inner_diameter_squared
    for point in points[1:]:
        moved = point[0]-delta, point[1]
        squared = norm(moved)
        assert 1 < squared < diameter*diameter
        translated_diameter_squared = max(translated_diameter_squared, squared)
    # All noncarrier pairs retain their previously checked distances.
    assert translated_diameter_squared < diameter*diameter
    expected_near = set(expected_contacts)
    for i in roots:
        first, middle = connectors[i]
        expected_near.update(
            tuple(sorted(pair)) for pair in (
                (wall_labels[i], first), (first, middle),
                (middle, row_labels[i]),
            )
        )
    expected_near.update(
        tuple(sorted((row_labels[j], row_labels[j+1]))) for j in range(k)
    )
    expected_near.add(tuple(sorted((row_labels[0], trunk[0]))))
    expected_near.update(
        tuple(sorted((x, y))) for x, y in zip(trunk, trunk[1:])
    )
    assert near_pairs == expected_near
    near_adjacency = [set() for _ in points]
    for i, j in near_pairs:
        near_adjacency[i].add(j)
        near_adjacency[j].add(i)
    adjacency = [set() for _ in points]
    for i, j in contacts:
        adjacency[i].add(j)
        adjacency[j].add(i)
    triangles = sum(len(adjacency[i] & adjacency[j]) for i, j in contacts)//3
    assert triangles == 0
    assert not adjacency[0]  # Actual loaded carrier is contact-isolated.
    for i in roots:
        assert adjacency[wall_labels[i]] == {
            wall_labels[i-1], wall_labels[i+1],
        }
    for label in row_labels.values():
        assert not adjacency[label]
    for label in trunk:
        assert not adjacency[label]
    for first, middle in connectors.values():
        assert not adjacency[first] and not adjacency[middle]
    assert all(wall[j][0] > 0 for j in wall)
    # The isolated carrier cannot balance any normalized nonnegative H load.

    kappa = Q(F(1), F(-1, 2))
    height = kappa*diameter-delta/4
    shared_prefix = int(diameter/8)
    paths = []
    arrows = 0
    all_outgoing_tests = 0
    fan_reflection_checks = 0
    for i in roots:
        u = scale(wall[i], 1/diameter)
        reflected = sub(wall[i], scale(u, delta))
        for neighbor in (i-1, i+1):
            assert dist2(reflected, wall[neighbor]) == 1
            fan_reflection_checks += 1
        first, middle = connectors[i]
        path = [wall_labels[i], first, middle]
        path.extend(row_labels[j] for j in range(i, -1, -1))
        path.extend(trunk)
        depths = [dot(u, sub(wall[i], points[label])) for label in path]
        crossing = next(
            t for t, depth in enumerate(depths) if (Q(depth)-height).sign() >= 0
        )
        path, depths = path[:crossing+1], depths[:crossing+1]
        assert len(set(path)) == len(path)
        assert all((Q(depth)-height).sign() < 0 for depth in depths[:-1])
        gap_upper = F(0)
        for parent, child, depth0, depth1 in zip(path, path[1:], depths, depths[1:]):
            old = dist2(points[parent], points[child])
            new = dist2(sub(points[parent], scale(u, delta)), points[child])
            assert 1 < old <= (1+delta)**2
            assert new < 1
            assert depth1-depth0 > delta/2
            gap_upper += (old-1)/2
            outgoing = set()
            for candidate in near_adjacency[parent]:
                old_pair = dist2(points[parent], points[candidate])
                new_pair = dist2(
                    sub(points[parent], scale(u, delta)), points[candidate],
                )
                if new_pair < 1 or (old_pair > 1 and new_pair == 1):
                    outgoing.add(candidate)
                all_outgoing_tests += 1
            assert outgoing == {child}
            arrows += 1
        assert set(trunk[:shared_prefix]).issubset(path)
        assert len(path)-1 >= diameter/8
        assert gap_upper < 1/(100*diameter)
        paths.append({
            "root": i, "edges": len(path)-1,
            "first_depth": str(depths[1]),
            "last_depth": str(depths[-1]),
            "common_trunk_nodes": shared_prefix,
            "total_gap_rational_upper": str(gap_upper),
        })

    n = len(points)
    width = isqrt(n-1)+1
    competitor = [(i % width, i // width) for i in range(n)]
    competitor_checks = 0
    competitor_diameter = 0
    for i, j in combinations(range(n), 2):
        squared = dist2(competitor[i], competitor[j])
        assert squared >= 1
        competitor_diameter = max(competitor_diameter, squared)
        competitor_checks += 1
    assert competitor_diameter < 2*n < diameter*diameter
    return {
        "q": q, "D": str(diameter), "fan_roots": len(roots),
        "source_points": n, "source_pair_checks": pair_checks,
        "competitor_pair_checks": competitor_checks,
        "actual_contacts": len(contacts),
        "actual_diameters": len(diameters),
        "contact_isolates": sum(not neighbors for neighbors in adjacency),
        "unit_triangles": triangles, "arrow_checks": arrows,
        "construction_checks": construction_checks,
        "finite_translation_cross_pair_checks": len(points)-1,
        "actual_near_unit_pairs": len(near_pairs),
        "all_outgoing_arrow_tests": all_outgoing_tests,
        "fan_reflection_checks": fan_reflection_checks,
        "common_isolate_trunk_nodes": shared_prefix,
        "path_congestion_on_common_trunk": len(roots),
        "competitor_diameter_squared": competitor_diameter,
        "paths": paths,
        "scope": "nonglobal; all H form a star at an isolated carrier; no KKT",
    }


def cap_tests():
    checks, increased = 0, 0
    for diameter in (10, 20, 40):
        delta = F(1, diameter)
        height = Q(diameter)-Q(F(0), F(diameter, 2))-delta/4
        p = F(diameter), F(0)
        candidates = []
        for numerator in range(-15, 16):
            parameter = F(numerator, 30)
            direction = (
                (1-parameter*parameter)/(1+parameter*parameter),
                2*parameter/(1+parameter*parameter),
            )
            for radius_fraction in (F(1), F(999, 1000), F(99, 100), F(19, 20)):
                point = scale(direction, diameter*radius_fraction)
                if 1 <= norm(point) <= diameter*diameter:
                    if 1 <= dist2(p, point) <= diameter*diameter:
                        candidates.append(point)
        for x in candidates:
            sx = diameter-x[0]
            if (height-Q(sx)).sign() <= 0:
                continue
            moved = x[0]-delta, x[1]
            for y in candidates:
                old = dist2(x, y)
                if not 1 <= old <= diameter*diameter:
                    continue
                new = dist2(moved, y)
                if new > old:
                    assert new < diameter*diameter
                    increased += 1
                checks += 1
        # The leading height constant cannot exceed 1-sqrt(3)/2.
        x = Q(F(0), F(diameter, 2)), Q(F(diameter, 2))
        y = x[0], -x[1]
        assert g.norm(x) == Q(diameter*diameter)
        assert g.norm(y) == Q(diameter*diameter)
        assert g.distance(x, y) == Q(diameter*diameter)
        moved = x[0]-delta, x[1]
        assert g.distance(moved, y) == Q(diameter*diameter+delta*delta)
        assert (g.distance((Q(diameter), Q()), x)-1).sign() > 0
        assert (Q(diameter*diameter)-g.distance((Q(diameter), Q()), x)).sign() > 0
    return {
        "valid_source_cross_pair_samples": checks,
        "increased_pairs_strictly_below_D": increased,
        "sharp_leading_height_regressions": 3,
    }


def main():
    cases = [family(q) for q in (1, 2, 3)]
    print(json.dumps({
        "status": "PASS", "exact_source_field": "Q",
        "threshold_field": "Q(sqrt(3))",
        "classification": "regression; canonical=false",
        "cases": cases, "cap_tests": cap_tests(),
        "totals": {
            key: sum(case[key] for case in cases)
            for key in (
                "source_pair_checks", "competitor_pair_checks",
                "arrow_checks", "construction_checks",
                "all_outgoing_arrow_tests", "fan_reflection_checks",
                "finite_translation_cross_pair_checks",
            )
        },
        "not_proved": [
            "canonical global minimizers realize this star family",
            "canonical stress permits unbounded path congestion",
            "the universal cap or all-q proofs from finite samples",
            "a shallow closed set exists in a canonical source",
            "C-II or Level I closure",
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
