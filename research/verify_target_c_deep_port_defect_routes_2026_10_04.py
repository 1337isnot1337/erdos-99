#!/usr/bin/env python3
"""Exact finite regressions for the deep-port route report.

All coordinates, squared distances, convexity and barycentric identities use
Fraction arithmetic. These checks do not prove the topological route theorem,
Type-II asymptotics, KKT feasibility, or global optimality of any fixture.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from collections import deque
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def scale(t, p):
    return t * p[0], t * p[1]


def cross(p, q):
    return p[0] * q[1] - p[1] * q[0]


def norm2(p):
    return p[0] ** 2 + p[1] ** 2


def edge(a, b):
    return tuple(sorted((a, b)))


def direction_cmp(p, q):
    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1

    hp, hq = half(p), half(q)
    if hp != hq:
        return hp - hq
    c = cross(p, q)
    assert c != 0, "fixture has coincident directions"
    return -1 if c > 0 else 1


def faces(points, edges):
    neighbors = {p: [] for p in points}
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    for a in neighbors:
        neighbors[a].sort(
            key=cmp_to_key(lambda b, c: direction_cmp(sub(points[b], points[a]),
                                                     sub(points[c], points[a])))
        )
    seen, bounded = set(), []
    for a, b in ((a, b) for e in edges for a, b in (e, e[::-1])):
        if (a, b) in seen:
            continue
        walk, start = [], (a, b)
        while (a, b) not in seen:
            seen.add((a, b))
            walk.append(a)
            at_b = neighbors[b]
            c = at_b[(at_b.index(a) - 1) % len(at_b)]
            a, b = b, c
        assert (a, b) == start
        area2 = sum(cross(points[u], points[v])
                    for u, v in zip(walk, walk[1:] + walk[:1]))
        if area2 > 0:
            bounded.append(walk)
    return bounded


def connected(vertices, edges):
    seen = {next(iter(vertices))}
    todo = deque(seen)
    while todo:
        a = todo.popleft()
        for e in edges:
            if a in e:
                b = e[1] if e[0] == a else e[0]
                if b in vertices and b not in seen:
                    seen.add(b)
                    todo.append(b)
    return seen == set(vertices)


def check_fixture(points, attachments, interior, weights):
    contacts = {edge(a, b) for a, b in combinations(points, 2)
                if norm2(sub(points[a], points[b])) == 1}
    assert contacts == set(weights)
    assert all(norm2(sub(points[a], points[b])) >= 1
               for a, b in combinations(points, 2))
    assert not any(edge(a, b) in contacts and edge(a, c) in contacts
                   and edge(b, c) in contacts
                   for a, b, c in combinations(points, 3))
    assert connected(interior, contacts)
    for a in interior:
        equilibrium = (F(0), F(0))
        for e, w in weights.items():
            assert w > 0
            if a in e:
                b = e[1] if e[0] == a else e[0]
                equilibrium = add(equilibrium, scale(w, sub(points[b], points[a])))
        assert equilibrium == (0, 0)
    a_cycle = attachments[1:] + attachments[:1]
    sides = {edge(a, b) for a, b in zip(attachments, a_cycle)}
    assert sides.isdisjoint(contacts)
    for a, b in zip(attachments, a_cycle):
        assert all(cross(sub(points[b], points[a]), sub(points[x], points[a])) > 0
                   for x in points if x not in (a, b))
    augmented_faces = faces(points, contacts | sides)
    assert len(augmented_faces) == len(contacts | sides) - len(points) + 1
    hull_face_count = 0
    for walk in augmented_faces:
        assert len(set(walk)) == len(walk)
        assert all(cross(sub(points[walk[(i + 1) % len(walk)]], points[walk[i]]),
                         sub(points[walk[(i + 2) % len(walk)]],
                             points[walk[(i + 1) % len(walk)]])) > 0
                   for i in range(len(walk)))
        face_edges = {edge(a, b) for a, b in zip(walk, walk[1:] + walk[:1])}
        polygon_sides = face_edges & sides
        loaded = set(walk) & set(attachments)
        if polygon_sides:
            hull_face_count += 1
            assert len(polygon_sides) == 1
            assert loaded == set(next(iter(polygon_sides)))
        else:
            assert len(loaded) <= 1
    assert hull_face_count == len(attachments)
    return len(augmented_faces)


def fixture_checks():
    points = {
        "00": (F(0), F(0)), "10": (F(1), F(0)),
        "11": (F(1), F(1)), "01": (F(0), F(1)),
        "a00": (F(-3, 5), F(-4, 5)), "a10": (F(8, 5), F(-4, 5)),
        "a11": (F(8, 5), F(9, 5)), "a01": (F(-3, 5), F(9, 5)),
    }
    weights = {edge("00", "10"): F(3, 5), edge("01", "11"): F(3, 5),
               edge("00", "01"): F(4, 5), edge("10", "11"): F(4, 5)}
    weights.update({edge(p, "a" + p): F(1) for p in ("00", "10", "11", "01")})
    n = check_fixture(points, ["a00", "a10", "a11", "a01"],
                      {"00", "10", "11", "01"}, weights)
    points.pop("a00")
    weights.pop(edge("00", "a00"))
    n += check_fixture(points, ["00", "a10", "a11", "a01"],
                       {"10", "11", "01"}, weights)
    points = {"x": (F(0), F(0)), "y": (F(1), F(0)),
              "a": (F(-3, 5), F(-4, 5)), "b": (F(8, 5), F(-4, 5)),
              "c": (F(8, 5), F(4, 5)), "d": (F(-3, 5), F(4, 5))}
    weights = {edge("x", "y"): F(6, 5), edge("a", "x"): F(1),
               edge("d", "x"): F(1), edge("b", "y"): F(1), edge("c", "y"): F(1)}
    n += check_fixture(points, ["a", "b", "c", "d"], {"x", "y"}, weights)
    return n


def boundary_point(t, v):
    u = (F(1), F(0))
    if t <= 1:
        return scale(t, u)
    if t <= 2:
        return add(u, scale(t - 1, v))
    if t <= 3:
        return add(v, scale(3 - t, u))
    return scale(4 - t, v)


def rhombus_checks():
    directions = set()
    for q in range(2, 18):
        for p in range(1, 2 * q):
            t = F(p, q)
            c, s = (1 - t*t)/(1 + t*t), 2*t/(1 + t*t)
            if abs(c) < F(1, 2):
                directions.add((c, s))
    parameters = [F(i, 4) for i in range(16)]
    count = 0
    for v in sorted(directions):
        assert norm2(v) == 1
        for a, b in combinations(parameters, 2):
            d = b - a
            shorter_arc = min(d, 4 - d)
            chord2 = norm2(sub(boundary_point(b, v), boundary_point(a, v)))
            assert 3 * shorter_arc**2 <= 16 * chord2
            count += 1
    v = (F(5, 13), F(12, 13))
    # Opposite top edge has reverse boundary parameter.
    a, b = F(9, 13), 3 - F(4, 13)
    shorter_arc = min(b - a, 4 - (b - a))
    chord2 = norm2(sub(boundary_point(b, v), boundary_point(a, v)))
    assert shorter_arc == 2 and chord2 == F(144, 169)
    assert shorter_arc**2 > 4 * chord2
    assert norm2(add((F(1), F(0)), v)) == F(36, 13)
    assert norm2(sub((F(1), F(0)), v)) == F(16, 13)
    return len(directions), count


def grid_regression():
    # This lattice fixture omits the canonical loaded-hull, KKT and ZF hypotheses.
    # It refutes charging raw macroscopic contact distance to interior defect.
    count = 0
    for m in (4, 8, 12):
        sites = {(i, j): (F(i) + F(5*j, 13), F(12*j, 13))
                 for i in range(m + 1) for j in range(m + 1)}
        contacts = set()
        for a, b in combinations(sites, 2):
            d2 = norm2(sub(sites[a], sites[b]))
            assert d2 >= 1
            if d2 == 1:
                assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
                contacts.add((a, b))
            count += 1
        assert len(contacts) == 2*m*(m + 1)
        assert norm2(sub(sites[(m, m)], sites[(0, 0)])) == F(36*m*m, 13)
        assert all(norm2(sub(p, q)) <= F(36*m*m, 13)
                   for p, q in combinations(sites.values(), 2))
        # Manhattan distance is 2m; all bounded faces are strict rhombi, Q=0.
        assert (2*m)**2 > F(36*m*m, 13)
    return count


def thin_face_regression():
    count = 0
    for length in (4, 8, 16, 32):
        bottom = [(F(0), F(-3, 5))]
        for i in range(1, length + 1):
            t = F(2*i - length - 1, 100*length*length)
            u = ((1-t*t)/(1+t*t), 2*t/(1+t*t))
            assert norm2(u) == 1
            bottom.append(add(bottom[-1], u))
        width = bottom[-1][0]
        assert bottom[-1][1] == F(-3, 5)
        assert F(length) - F(1, 5000*length) <= width <= length
        assert all(F(-31, 50) <= y <= F(-3, 5) for x, y in bottom)
        top = [(x, -y) for x, y in reversed(bottom)]
        right, left = (width + F(4, 5), F(0)), (F(-4, 5), F(0))
        polygon = bottom + [right] + top + [left]
        size = len(polygon)
        assert size == 2*length + 4
        assert all(norm2(sub(polygon[(i + 1) % size], polygon[i])) == 1
                   for i in range(size))
        assert all(cross(sub(polygon[(i + 1) % size], polygon[i]),
                         sub(polygon[(i + 2) % size], polygon[(i + 1) % size])) > 0
                   for i in range(size))
        for i, j in combinations(range(size), 2):
            d2 = norm2(sub(polygon[i], polygon[j]))
            expected_contact = (j-i == 1 or j-i == size-1)
            assert d2 == 1 if expected_contact else d2 > 1
            assert d2 <= (width + F(8, 5))**2
            count += 1
        area2 = sum(cross(polygon[i], polygon[(i+1) % size]) for i in range(size))
        assert 0 < area2/2 <= F(31, 25)*(length + F(8, 5))
        assert width + F(8, 5) <= length + 3
        assert size - 4 == 2*length
    return count


if __name__ == "__main__":
    face_count = fixture_checks()
    direction_count, rhombus_count = rhombus_checks()
    pair_count = grid_regression()
    thin_pair_count = thin_face_regression()
    print(f"PASS: {face_count} exact harmonic-fixture augmented faces; "
          f"{direction_count} rational rhombi / {rhombus_count} boundary pairs; "
          f"{pair_count} lattice source-pair checks; "
          f"{thin_pair_count} thin-face source-pair checks; three exact regressions")
    print("Scope: finite geometry and arithmetic only; no C-II or global-optimality certificate.")
