#!/usr/bin/env python3
"""Exact integer pinning checks for every one-vacancy hexagonal chart.

The universal proof is in the companion report. Finite checks do not classify
arbitrary one-deficit clouds, prove the curved-wall endpoint, or global optimality.
"""
from collections import defaultdict, deque
import json

DIRECTIONS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def radius(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))


def hexagon(m):
    return {(i, j) for i in range(-m, m + 1)
            for j in range(-m, m + 1) if abs(i + j) <= m}


def triangles(points):
    result = set()
    for p in points:
        for k in range(6):
            q, r = add(p, DIRECTIONS[k]), add(p, DIRECTIONS[(k + 1) % 6])
            if q in points and r in points:
                result.add(tuple(sorted((p, q, r))))
    return sorted(result)


def case(m):
    full = hexagon(m)
    wall = {p for p in full if radius(p) == m}
    interior = full - wall
    assert len(wall) == 6 * m
    assert len(interior) == 3 * m * m - 3 * m + 1
    full_triangles = triangles(full)
    assert len(full_triangles) == 6 * m * m
    equilibrium_checks = weighted_rows = propagated_vertices = triangle_checks = 0
    for hole in sorted(interior):
        moving = interior - {hole}
        neighbours = {add(hole, d) for d in DIRECTIONS}
        assert neighbours <= full
        for p in moving:
            force = [0, 0]
            for d in DIRECTIONS:
                q = add(p, d)
                assert q in full
                if q == hole:
                    continue
                weight = 1 + int(p in neighbours and q in neighbours)
                force[0] -= weight * d[0]
                force[1] -= weight * d[1]
                weighted_rows += 1
            assert force == [0, 0], (m, hole, p, force)
            equilibrium_checks += 1
        faces = [tri for tri in full_triangles if hole not in tri]
        incident = defaultdict(list)
        known = set(wall)
        remaining = []
        queue = deque()
        for index, tri in enumerate(faces):
            a, b, c = tri
            determinant = ((b[0] - a[0]) * (c[1] - a[1])
                           - (b[1] - a[1]) * (c[0] - a[0]))
            assert abs(determinant) == 1
            triangle_checks += 1
            remaining.append(set(tri) - known)
            if len(remaining[-1]) == 1:
                queue.append(index)
            for p in tri:
                incident[p].append(index)
        while queue:
            index = queue.popleft()
            unknown = remaining[index]
            if len(unknown) != 1:
                continue
            p = next(iter(unknown))
            assert p in moving and p not in known
            known.add(p)
            propagated_vertices += 1
            for j in incident[p]:
                remaining[j].discard(p)
                if len(remaining[j]) == 1:
                    queue.append(j)
        assert moving <= known, (m, hole, sorted(moving - known))
    return {'M': m, 'vacancies_checked': len(interior),
            'moving_equilibria': equilibrium_checks,
            'positive_row_incidences': weighted_rows,
            'exact_triangle_determinants': triangle_checks,
            'vertices_pinned_by_triangle_propagation': propagated_vertices}


def main():
    cases = [case(m) for m in range(2, 11)]
    print(json.dumps({'classification': 'exact finite certificate',
                      'arithmetic': 'integers',
                      'scope': 'flat lattice-vacancy charts only',
                      'cases': cases,
                      'total_vacancies': sum(c['vacancies_checked'] for c in cases),
                      'total_equilibria': sum(c['moving_equilibria'] for c in cases)},
                     sort_keys=True))


if __name__ == '__main__':
    main()
