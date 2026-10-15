#!/usr/bin/env python3
"""Exact finite regressions for the monotone cap-route report.

Checks all pairs in finite rational grids, pinned positive equilibrium, greedy
ascent and overlap accounting, an attachment-triangle slow vertex, and exact
Pell-family sharpness arithmetic. Does not certify global optimality, canonical
source status, the analytic universal theorem, or a source competitor.
"""

from collections import Counter
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def cross(x, y):
    return x[0] * y[1] - x[1] * y[0]


def face_walks(points, adjacency):
    """Exact half-edge face enumeration, with counterclockwise bounded faces."""
    rotation = {}
    for x, ns in adjacency.items():
        def compare(y, z):
            vy, vz = sub(points[y], points[x]), sub(points[z], points[x])
            hy = 0 if vy[1] > 0 or (vy[1] == 0 and vy[0] >= 0) else 1
            hz = 0 if vz[1] > 0 or (vz[1] == 0 and vz[0] >= 0) else 1
            if hy != hz:
                return -1 if hy < hz else 1
            cr = cross(vy, vz)
            if cr:
                return -1 if cr > 0 else 1
            return (dot(vy, vy) > dot(vz, vz)) - (dot(vy, vy) < dot(vz, vz))
        rotation[x] = sorted(ns, key=cmp_to_key(compare))
    visited, bounded = set(), []
    outer_count = 0
    for x in adjacency:
        for y in adjacency[x]:
            if (x, y) in visited:
                continue
            start, edge, walk = (x, y), (x, y), []
            while True:
                assert edge not in visited
                visited.add(edge)
                a, b = edge
                walk.append(a)
                ns = rotation[b]
                edge = b, ns[(ns.index(a) - 1) % len(ns)]
                if edge == start:
                    break
            area2 = sum(cross(points[a], points[b])
                        for a, b in zip(walk, walk[1:] + walk[:1]))
            assert area2 != 0
            if area2 > 0:
                bounded.append(walk)
            else:
                outer_count += 1
    assert outer_count == 1
    return bounded


def pocket_payment(points, neighbors, size):
    # All noncorner boundary grid vertices are pins incident with the connected
    # interior. Collinear pins make this a local framework, not a canonical one.
    interior = {x for x in points if 0 < x[0] < size and 0 < x[1] < size}
    pins = ([(i, 0) for i in range(1, size)]
            + [(size, j) for j in range(1, size)]
            + [(i, size) for i in range(size - 1, 0, -1)]
            + [(0, j) for j in range(size - 1, 0, -1)])
    vertices = interior | set(pins)
    adjacency = {x: {y for y in neighbors[x]
                     if y in vertices and (x in interior or y in interior)}
                 for x in vertices}
    base_edges = sum(map(len, adjacency.values())) // 2
    assert base_edges == 2 * size * (size - 1)
    polygon = set()
    for a, b in zip(pins, pins[1:] + pins[:1]):
        assert b not in adjacency[a]
        adjacency[a].add(b)
        adjacency[b].add(a)
        polygon.add(frozenset((a, b)))
    faces = face_walks(points, adjacency)
    assert len(faces) == base_edges + len(pins) - len(vertices) + 1
    pockets = {}
    for walk in faces:
        poly_edges = [frozenset((a, b)) for a, b in zip(walk, walk[1:] + walk[:1])
                      if frozenset((a, b)) in polygon]
        if poly_edges:
            assert len(poly_edges) == 1
            pockets[poly_edges[0]] = walk
    assert len(pockets) == len(pins)
    defect = sum(max(0, len(walk) - 4) for walk in faces)
    assert defect == 0
    triangles = sum(len(walk) == 3 for walk in faces)
    nonunit_sides = sum(dot(sub(points[b], points[a]), sub(points[b], points[a])) > 1
                        for a, b in zip(pins, pins[1:] + pins[:1]))
    assert triangles == nonunit_sides == 4
    route_bank = 2 * nonunit_sides - triangles + 5 * defect
    assert route_bank == 4
    # The local form of the exact joint-bank algebra.
    attachment_slack = len(pins) - triangles
    unit_sides = len(pins) - nonunit_sides
    assert route_bank == (len(pins) + 5 * (attachment_slack + defect)
                          - 4 * attachment_slack - 2 * unit_sides)
    for a, b in zip(pins, pins[1:] + pins[:1]):
        walk = pockets[frozenset((a, b))]
        length = len(walk) - 1
        r = sub(points[b], points[a])
        assert dot(r, r) <= length * length
        for x, y in zip(walk, walk[1:] + walk[:1]):
            if frozenset((x, y)) not in polygon:
                assert dot(sub(points[y], points[x]), sub(points[y], points[x])) == 1
    # Check the clipped-height demand with a certified rational diameter bound.
    s = points[(0, 1)][1]
    line_height = (size // 2) * s
    area = (size - 2) * (size - size // 2 - 2) * s
    diam_upper = F(2 * size)
    height = max(points[b][1] - line_height for b in pins)
    cutoff = height - area / (2 * diam_upper)
    assert cutoff >= area / (2 * diam_upper) > 0
    clipped = {b: max(F(0), points[b][1] - line_height - cutoff) for b in pins}
    variation = sum(abs(clipped[b] - clipped[a])
                    for a, b in zip(pins, pins[1:] + pins[:1]))
    assert variation == area / diam_upper
    deep = {b for b in pins if clipped[b] > 0}
    touched = [(a, b) for a, b in zip(pins, pins[1:] + pins[:1])
               if a in deep or b in deep]
    assert len(touched) <= 2 * len(deep)
    assert 6 * len(deep) + defect >= area / diam_upper
    return len(pockets)


def grid(p, q, size):
    assert q * q - 3 * p * p == -2
    c, s = F(p * p - 1, 2 * p * p - 1), F(p * q, 2 * p * p - 1)
    assert c * c + s * s == 1 and 0 < c < F(1, 2)
    points = {(i, j): (F(i) + j * c, j * s)
              for i in range(size + 1) for j in range(size + 1)}
    neighbors = {v: [] for v in points}
    pairs = 0
    diam2 = F(0)
    for x, y in combinations(points, 2):
        r = sub(points[y], points[x])
        d2 = dot(r, r)
        pairs += 1
        assert d2 >= 1
        diam2 = max(diam2, d2)
        axis = abs(x[0] - y[0]) + abs(x[1] - y[1]) == 1
        assert (d2 == 1) == axis
        if d2 == 1:
            neighbors[x].append(y)
            neighbors[y].append(x)
    assert diam2 == size * size * (2 + 2 * c)
    edges = sum(map(len, neighbors.values())) // 2
    assert edges == 2 * size * (size + 1)
    # Every bounded face is one strict rhombus, so Q^+=0 for this pinned patch.
    assert edges - len(points) + 1 == size * size
    for x, ns in neighbors.items():
        assert not any(y in neighbors[z] for y, z in combinations(ns, 2))
        if 0 < x[0] < size and 0 < x[1] < size:
            force = (F(0), F(0))
            for y in ns:
                force = add(force, sub(points[y], points[x]))
            assert force == (0, 0)
            assert len(ns) == 4
    return points, neighbors, pairs


def routes(points, neighbors, size):
    # Rational unit direction. The v step is uniquely best at each interior
    # vertex; paths starting in one column overlap and end at one pinned root.
    n = F(3, 5), F(4, 5)
    assert dot(n, n) == 1
    interior = {x for x in points if 0 < x[0] < size and 0 < x[1] < size}
    successor, gain, debit = {}, {}, {}
    for x in interior:
        successor[x] = max(neighbors[x], key=lambda y: dot(n, sub(points[y], points[x])))
        gain[x] = dot(n, sub(points[successor[x]], points[x]))
        assert gain[x] > 0
        debit[x] = max(F(0), 1 - 2 * gain[x])
        assert debit[x] == 0  # Complete interior rhombus stars.
    paths = []
    for start in sorted(interior):
        path = [start]
        while path[-1] in interior:
            nxt = successor[path[-1]]
            assert nxt not in path
            path.append(nxt)
        tails = path[:-1]
        height = dot(n, sub(points[path[-1]], points[start]))
        assert height == sum(gain[x] for x in tails)
        excess = len(tails) - 2 * height
        assert excess == sum(1 - 2 * gain[x] for x in tails)
        assert max(F(0), excess) <= sum(debit[x] for x in tails)
        paths.append((tails, path[-1], height))
    multiplicity = Counter(x for tails, _, _ in paths for x in tails)
    excess_sum = sum(max(F(0), len(tails) - 2 * h) for tails, _, h in paths)
    assert excess_sum <= sum(multiplicity[x] * debit[x] for x in interior)
    assert max(multiplicity.values()) == size - 1
    assert len({root for _, root, _ in paths}) == size - 1
    # One start per column gives disjoint unloaded tails, as required by (8).
    disjoint = [item for item in paths if item[0][0][1] == 1]
    seen = set()
    for tails, _, _ in disjoint:
        assert seen.isdisjoint(tails)
        seen.update(tails)
    return len(paths), max(multiplicity.values())


def attachment_triangle():
    # Exact positive equilibrium with an arbitrarily small uphill projection.
    # Its augmented graph has three triangular bounded faces, Q^+=0.
    eps, c = F(20, 101), F(99, 101)
    assert eps * eps + c * c == 1
    center = (F(0), F(0))
    terminals = [(c, eps), (-c, eps), (F(0), F(-1))]
    points = [center] + terminals
    contacts = []
    for i, j in combinations(range(4), 2):
        r = sub(points[j], points[i])
        assert dot(r, r) >= 1
        if dot(r, r) == 1:
            contacts.append((i, j))
    assert contacts == [(0, 1), (0, 2), (0, 3)]
    augmented = {i: {j for a, b in contacts for j in ([b] if a == i else [a] if b == i else [])}
                 for i in range(4)}
    for a, b in [(1, 2), (2, 3), (3, 1)]:
        augmented[a].add(b)
        augmented[b].add(a)
    faces = face_walks(dict(enumerate(points)), augmented)
    assert len(faces) == 3 and all(len(walk) == 3 for walk in faces)
    assert sum(max(0, len(walk) - 4) for walk in faces) == 0
    weights = [1 / (2 * eps), 1 / (2 * eps), F(1)]
    force = (F(0), F(0))
    for w, z in zip(weights, terminals):
        force = add(force, (w * z[0], w * z[1]))
    assert force == (0, 0) and all(w > 0 for w in weights)
    assert max(z[1] for z in terminals) == eps < F(1, 2)
    debit = 1 - 2 * eps
    assert debit == F(61, 101) > 0
    # An uphill route of one edge realizes the debit exactly. Thus Q^+ alone
    # cannot pay this local route; attachment-triangle occurrences are necessary.
    assert F(1) - 2 * eps == debit
    return debit


def pell_arithmetic():
    p, q = 1, 1
    previous_ratio2 = F(0)
    for _ in range(10):
        p, q = 2 * p + q, 3 * p + 2 * q
        assert q * q - 3 * p * p == -2
        c, s = F(p * p - 1, 2 * p * p - 1), F(p * q, 2 * p * p - 1)
        assert c * c + s * s == 1 and 0 < c < F(1, 2)
        size = p * p
        length = 2 * (size - 2)
        height2 = (size - 2) ** 2 * (2 - 2 * c)
        ratio2 = length * length / height2
        assert ratio2 == 4 - F(2, p * p)
        assert previous_ratio2 < ratio2 < 4
        previous_ratio2 = ratio2
        # -1/2 < length - 2*height < 0, using exact square comparisons.
        assert height2 > F(length * length, 4)
        assert height2 < (F(length, 2) + F(1, 4)) ** 2
        diam2 = size * size * (2 + 2 * c)
        assert F(length * length) > diam2 / 2
        assert (1 - c) / 2 > F(1, 4)  # Every chosen upward tail is nonslow.
    return 10


def main():
    pair_count = path_count = 0
    pocket_count = 0
    max_visit = 0
    for p, q, size in [(3, 5, 9), (11, 19, 7)]:
        points, neighbors, pairs = grid(p, q, size)
        paths, visits = routes(points, neighbors, size)
        pocket_count += pocket_payment(points, neighbors, size)
        pair_count += pairs
        path_count += paths
        max_visit = max(max_visit, visits)
    debit = attachment_triangle()
    family_count = pell_arithmetic()
    print(f"PASS: {pair_count} exact source pairs; {path_count} greedy routes; "
          f"overlap multiplicity {max_visit}; triangle debit {debit}; "
          f"{family_count} Pell sharpness identities; {pocket_count} exact "
          "attachment-pocket faces and clipped-height demands.")
    print("Scope: finite local regressions and rational arithmetic only; "
          "no global-optimality or C-II certificate.")


if __name__ == "__main__":
    main()
