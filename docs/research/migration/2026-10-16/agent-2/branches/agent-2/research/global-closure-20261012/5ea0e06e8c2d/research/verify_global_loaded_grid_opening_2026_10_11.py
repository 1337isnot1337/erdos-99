#!/usr/bin/env python3
"""Exact finite contact-opening fixtures, not a Level I certificate."""

from fractions import Fraction as F
from itertools import combinations
import json


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def norm2(p):
    return sum(a * a for a in p)


def ledger(points):
    return {(i, j): norm2(sub(points[i], points[j]))
            for i, j in combinations(range(len(points)), 2)}


def components(size, edges):
    neighbors = [set() for _ in range(size)]
    for i, j in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)
    remaining, result = set(range(size)), []
    while remaining:
        root = min(remaining)
        found, stack = {root}, [root]
        while stack:
            for j in neighbors[stack.pop()] - found:
                found.add(j)
                stack.append(j)
        remaining -= found
        result.append(found)
    return result, neighbors


def check_fixture(name, points, u, v, expected_retained, expected_isolates):
    old = ledger(points)
    contacts = {edge for edge, length in old.items() if length == 1}
    d2 = max(old.values())
    diameters = {edge for edge, length in old.items() if length == d2}
    pins = {i for edge in diameters for i in edge}
    old_components, neighbors = components(len(points), contacts)
    directions = {u: (1, 0), tuple(-x for x in u): (-1, 0),
                  v: (0, 1), tuple(-x for x in v): (0, -1)}
    determinant = u[0] * v[1] - u[1] * v[0]
    assert norm2(u) == norm2(v) == 1 and determinant != 0
    velocities = [(F(0), F(0)) for _ in points]
    original_component = {}
    pin_counts = []
    isolates = 0
    for index, component in enumerate(old_components):
        for i in component:
            original_component[i] = index
        pin_counts.append(len(component & pins))
        if len(component) == 1:
            isolates += 1
            continue
        root = min(component)
        labels, stack = {root: (0, 0)}, [root]
        while stack:
            i = stack.pop()
            for j in neighbors[i]:
                step = directions[sub(points[j], points[i])]
                label = tuple(labels[i][a] + step[a] for a in range(2))
                if j in labels:
                    assert labels[j] == label
                else:
                    labels[j] = label
                    stack.append(j)
        a_pins = {labels[i][0] for i in component & pins}
        b_pins = {labels[i][1] for i in component & pins}
        free_a = sorted({labels[i][0] for i in component} - a_pins)
        free_b = sorted({labels[i][1] for i in component} - b_pins)
        g = {a: F(k + 1) for k, a in enumerate(free_a)}
        f = {b: F(k + 1) for k, b in enumerate(free_b)}
        for a in a_pins:
            g[a] = F(0)
        for b in b_pins:
            f[b] = F(0)
        for i, (a, b) in labels.items():
            velocities[i] = ((f[b] * v[1] - u[1] * g[a]) / determinant,
                             (u[0] * g[a] - f[b] * v[0]) / determinant)
    assert isolates == expected_isolates
    assert all(velocities[i] == (0, 0) for i in pins)
    retained = set()
    t = F(1, 10000)
    moved = [tuple(p[a] + t * w[a] for a in range(2))
             for p, w in zip(points, velocities)]
    new = ledger(moved)
    for i, j in contacts:
        r, dw = sub(points[i], points[j]), sub(velocities[i], velocities[j])
        assert sum(a * b for a, b in zip(r, dw)) == 0
        assert new[i, j] == 1 + t * t * norm2(dw)
        if norm2(dw) == 0:
            retained.add((i, j))
    assert min(old.values()) == 1 and min(new.values()) >= 1
    assert max(new.values()) == d2
    assert {e for e, length in new.items() if length == d2} == diameters
    assert {e for e, length in new.items() if length == 1} == retained
    assert len(retained) == expected_retained
    new_components, _ = components(len(points), retained)
    largest = F(0)
    for component in new_components:
        indices = {original_component[i] for i in component}
        assert len(indices) == 1
        original = indices.pop()
        bound = 2 * max(0, pin_counts[original] - 1)
        r2 = max((new[tuple(sorted((i, j)))]
                  for i, j in combinations(component, 2)), default=F(0))
        assert r2 <= bound * bound
        largest = max(largest, r2)
    final_d2 = None
    if not retained:
        assert min(new.values()) > 1
        contraction = F(9999999999, 10000000000)
        final = ledger([tuple(contraction * x for x in p) for p in moved])
        assert min(final.values()) > 1 and max(final.values()) < d2
        final_d2 = str(max(final.values()))
    elif name == "two_by_three":
        vertical_scale = 1 - t * t / 4
        final = ledger([(p[0], p[1] * vertical_scale) for p in moved])
        assert min(final.values()) >= 1 and max(final.values()) < d2
        final_d2 = str(max(final.values()))
    else:
        assert name == "two_by_two_control"
        assert moved == points and largest == d2
    return {"name": name, "labels": len(points), "pairs_each_stage": len(old),
            "diameter_pairs_fixed": len(diameters), "isolates_retained": isolates,
            "contacts_opened": len(contacts - retained),
            "contacts_retained": len(retained),
            "largest_new_contact_component_squared": str(largest),
            "strict_competitor_diameter_squared": final_d2}


def check_triangular_partition():
    def triangular_norm2(a, b):
        return a * a + a * b + b * b
    assert all(triangular_norm2(*r) == 1 for r in ((1, 0), (0, 1), (1, -1)))
    assert triangular_norm2(2, -1) == triangular_norm2(1, 1) == 3
    assert 2 * 1 - (-1) * 1 == 3
    checked = 0
    for a in range(-10, 11):
        for b in range(-10, 11):
            residue = (a + 2 * b) % 3
            ra, rb = ((0, 0), (1, 0), (0, 1))[residue]
            x, y = a - ra, b - rb
            assert (x - y) % 3 == 0 and (x + 2 * y) % 3 == 0
            s, t = (x - y) // 3, (x + 2 * y) // 3
            assert (a, b) == (2 * s + t + ra, -s + t + rb)
            checked += 1
    assert 128 + F(32) * 2 ** 16 < F(2 ** 24, 4)
    return checked


def main():
    square_u, square_v = (F(1), F(0)), (F(0), F(1))
    fixture_results = []
    for m, k, name, retained in ((2, 2, "two_by_two_control", 4),
                                  (2, 3, "two_by_three", 3)):
        points = [(F(a), F(b)) for a in range(m) for b in range(k)]
        fixture_results.append(check_fixture(name, points, square_u, square_v,
                                             retained, 0))
    points = [(F(a), F(b)) for a in range(7) for b in range(7)
              if not (2 <= a <= 4 and 2 <= b <= 4)]
    points.append((F(3) + F(1, 7), F(3) + F(1, 11)))
    fixture_results.append(check_fixture("hole_and_off_lattice_isolate", points,
                                         square_u, square_v, 0, 1))
    labels = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0),
              (0, -1), (1, -1), (1, 1), (2, -1)]
    v = (F(8, 17), F(15, 17))
    points = [(F(a) + b * v[0], b * v[1]) for a, b in labels]
    fixture_results.append(check_fixture("nonrectangular_oblique", points,
                                         square_u, v, 0, 0))
    print(json.dumps({"status": "PASS", "arithmetic": "rational",
                      "fixtures": fixture_results,
                      "triangular_partition_labels_checked": check_triangular_partition(),
                      "general_theorem_proved_by_finite_output": False,
                      "level_i_resolved": False}, sort_keys=True))


if __name__ == "__main__":
    main()
