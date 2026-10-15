#!/usr/bin/env python3
"""Exact finite checks for the bulk separator / disjoint-return report.

The examples are grounded square grids, not canonical E99 sources: boundary
pins are not all actual diameter endpoints. Checks prove the stated finite
ranks, equilibrium, cuts, integral flows and rational capacity bounds only.
The general analytic theorem is proved in the report, not by this script.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from collections import deque
from fractions import Fraction
from itertools import combinations
from math import isqrt


def board(side):
    vertices = [(x, y) for x in range(side + 1) for y in range(side + 1)]
    pins = {p for p in vertices if 0 in p or side in p}
    adjacency = {p: set() for p in vertices}
    for x, y in vertices:
        for q in ((x + 1, y), (x, y + 1)):
            if q in adjacency:
                adjacency[x, y].add(q)
                adjacency[q].add((x, y))
    return vertices, pins, adjacency


def rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(rows[0])):
        found = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        divisor = rows[pivot][column]
        rows[pivot] = [x / divisor for x in rows[pivot]]
        for i in range(pivot + 1, len(rows)):
            factor = rows[i][column]
            if factor:
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def check_pinned_minor(side, oblique=False):
    vertices, pins, adjacency = board(side)
    interior = [p for p in vertices if p not in pins]
    index = {p: i for i, p in enumerate(interior)}
    if oblique:
        denominator = side ** 2
        numerator = isqrt(denominator ** 2 // 3) + 1
        assert 3 * numerator ** 2 > denominator ** 2
        divisor = denominator ** 2 + numerator ** 2
        cosine = Fraction(denominator ** 2 - numerator ** 2, divisor)
        sine = Fraction(2 * denominator * numerator, divisor)
        assert 0 < cosine < Fraction(1, 2)
        assert cosine ** 2 + sine ** 2 == 1
    else:
        cosine, sine = Fraction(0), Fraction(1)
    basis = ((Fraction(1), Fraction(0)), (cosine, sine))

    def point(p):
        return p[0] + cosine * p[1], sine * p[1]

    rows = []
    # Horizontal edges toward the left pin, vertical edges toward the bottom
    # pin: a square 2|I|-row minor of the actual pinned rigidity matrix.
    for p in interior:
        for coordinate in (0, 1):
            q = list(p)
            q[coordinate] -= 1
            q = tuple(q)
            assert q in adjacency[p]
            row = [0] * (2 * len(interior))
            for axis, value in enumerate(basis[coordinate]):
                row[2 * index[p] + axis] = value
                if q in index:
                    row[2 * index[q] + axis] = -value
            rows.append(row)
    assert rank(rows) == 2 * len(interior)
    for p in interior:
        # All four contact multipliers equal one: exact positive equilibrium.
        assert len(adjacency[p]) == 4
        assert all(sum(point(p)[j] - point(q)[j] for q in adjacency[p]) == 0 for j in (0, 1))
    largest, actual_loaded = Fraction(0), set()
    for i, p in enumerate(vertices):
        for q in vertices[i + 1:]:
            squared = sum((a - b) ** 2 for a, b in zip(point(p), point(q)))
            assert squared >= 1
            assert (squared == 1) == (q in adjacency[p])
            if squared > largest:
                largest, actual_loaded = squared, {p, q}
            elif squared == largest:
                actual_loaded.update((p, q))
    assert all(len(adjacency[p]) <= 3 for p in pins)
    # The remaining pins deliberately fail actual diameter loading.
    expected = {(0, 0), (side, side)} if oblique else {
        p for p in vertices if all(c in (0, side) for c in p)}
    assert actual_loaded == expected
    assert actual_loaded < pins
    assert largest >= 2 * side ** 2
    assert Fraction(7, 6) * (side ** 2 + 2 * side) < 2 * side ** 2


def cells(lo, hi):
    return [{(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)}
            for x in range(lo, hi) for y in range(lo, hi)]


def components(adjacency, removed):
    unseen = set(adjacency) - removed
    result = []
    while unseen:
        seed = min(unseen)
        component = {seed}
        queue = deque([seed])
        unseen.remove(seed)
        while queue:
            p = queue.popleft()
            for q in adjacency[p] & unseen:
                unseen.remove(q)
                component.add(q)
                queue.append(q)
        result.append(component)
    return result


def diameter(adjacency, component):
    answer = 0
    for seed in component:
        distances = {seed: 0}
        queue = deque([seed])
        while queue:
            p = queue.popleft()
            for q in adjacency[p] & component:
                if q not in distances:
                    distances[q] = distances[p] + 1
                    queue.append(q)
        assert len(distances) == len(component)
        answer = max(answer, max(distances.values()))
    return answer


def check_separator(pins, adjacency, rhombi, removed, minimal=False):
    bulk = set().union(*rhombi)
    pieces = components(adjacency, removed)
    if any(piece & bulk and piece & pins for piece in pieces):
        return False
    surviving = [face for face in rhombi if not face & removed]
    selected = [piece for piece in pieces if any(face <= piece for face in surviving)]
    k_i, k_b = len(removed - pins), len(removed & pins)
    w = 5 * k_i + 3 * k_b
    assert len(rhombi) - len(surviving) <= 5 * k_i
    sum_delta, sum_t = 0, 0
    for piece in selected:
        assert not piece & pins
        boundary_edges = [(p, q) for p in piece for q in adjacency[p] - piece]
        assert all(q in removed for _, q in boundary_edges)
        delta = diameter(adjacency, piece)
        e = sum(len(adjacency[p] & piece) for p in piece) // 2
        t = len(boundary_edges)
        assert e + t >= 2 * len(piece) + 1
        assert e <= 2 * len(piece) - delta - 2
        assert t >= delta + 3
        sum_delta += delta
        sum_t += t
    assert sum_t <= w
    assert sum_delta <= w - 3 * len(selected)
    if surviving:
        # Exact rational relaxation: a0>6/7 and pi/4<11/14.
        assert Fraction(6, 7) * len(surviving) <= Fraction(11, 14) * sum_delta ** 2
    assert len(rhombi) <= 5 * k_i + Fraction(11, 12) * w ** 2
    if minimal:
        for s in removed:
            restored = components(adjacency, removed - {s})
            assert any(piece & bulk and piece & pins for piece in restored)
            if s not in pins:
                loaded_side = set().union(*(piece for piece in pieces if piece & pins))
                assert adjacency[s] & loaded_side
        w_min = 4 * k_i + 3 * k_b
        assert sum_t <= w_min
        assert len(rhombi) <= 5 * k_i + Fraction(11, 12) * w_min ** 2
    return True


def vertex_flow(vertices, pins, adjacency, bulk):
    index = {p: i for i, p in enumerate(vertices)}
    source, sink = 2 * len(vertices), 2 * len(vertices) + 1
    residual = [dict() for _ in range(sink + 1)]
    original = {}
    high = len(vertices) + 1

    def edge(a, b, capacity):
        assert (a, b) not in original
        original[a, b] = capacity
        residual[a][b] = capacity
        residual[b].setdefault(a, 0)

    for p in vertices:
        i = index[p]
        edge(2 * i, 2 * i + 1, 1)
        for q in adjacency[p]:
            edge(2 * i + 1, 2 * index[q], high)
        if p in bulk:
            edge(source, 2 * i, high)
        if p in pins:
            edge(2 * i + 1, sink, high)

    def search(graph, start, end):
        parent = {start: None}
        queue = deque([start])
        while queue and end not in parent:
            a = queue.popleft()
            for b, capacity in graph[a].items():
                if capacity > 0 and b not in parent:
                    parent[b] = a
                    queue.append(b)
        return parent

    value = 0
    while True:
        parent = search(residual, source, sink)
        if sink not in parent:
            break
        b = sink
        while b != source:
            a = parent[b]
            residual[a][b] -= 1
            residual[b][a] += 1
            b = a
        value += 1
    cut = {p for p in vertices if 2 * index[p] in parent and 2 * index[p] + 1 not in parent}
    assert len(cut) == value

    flow = [dict() for _ in residual]
    for (a, b), capacity in original.items():
        amount = capacity - residual[a][b]
        if amount > 0:
            flow[a][b] = amount
    paths = []
    for _ in range(value):
        parent_flow = search(flow, source, sink)
        assert sink in parent_flow
        steps, b = [], sink
        while b != source:
            a = parent_flow[b]
            steps.append((a, b))
            flow[a][b] -= 1
            b = a
        steps.reverse()
        path = [vertices[a // 2] for a, b in steps if a < source and a % 2 == 0 and b == a + 1]
        last = next(i for i, p in enumerate(path) if p in pins)
        first = max(i for i, p in enumerate(path[:last]) if p in bulk)
        path = path[first:last + 1]
        assert path[0] in bulk and path[-1] in pins
        assert not set(path[1:]) & bulk and not set(path[:-1]) & pins
        assert all(q in adjacency[p] for p, q in zip(path, path[1:]))
        paths.append(path)
    used = set()
    for path in paths:
        assert not used & set(path)
        used.update(path)
    return value, cut, paths


def main():
    for side in range(3, 9):
        check_pinned_minor(side)
        check_pinned_minor(side, oblique=True)
    vertices, pins, adjacency = board(3)
    rhombi = cells(1, 2)
    checked, valid = 0, 0
    for size in range(5):
        for subset in combinations(vertices, size):
            checked += 1
            valid += check_separator(pins, adjacency, rhombi, set(subset))
    assert valid > 0
    flow_cases = []
    for side in (6, 12, 18, 24):
        vertices, pins, adjacency = board(side)
        lo, hi = side // 3, 2 * side // 3
        rhombi = cells(lo, hi)
        bulk = set().union(*rhombi)
        value, cut, paths = vertex_flow(vertices, pins, adjacency, bulk)
        assert check_separator(pins, adjacency, rhombi, cut, minimal=True)
        ring = {p for p in bulk if any(q not in bulk for q in adjacency[p])}
        assert check_separator(pins, adjacency, rhombi, ring, minimal=True)
        assert value == len(ring) == 4 * (hi - lo)
        assert all(len(path) - 1 >= lo for path in paths)
        flow_cases.append((side, len(rhombi), value, sum(len(path) - 2 for path in paths)))
    assert Fraction(4, 3) ** 4 > 3  # 3^(1/4)/256 < 1/192.
    assert Fraction(7, 4) ** 2 > 3  # With pi>3, Delta_2>6/7.
    print('pinned_rank_and_positive_equilibrium_cases=12 (six square, six near-triangular oblique)')
    print(f'exhaustive_small_separator_sets={checked}; valid_separators={valid}')
    print('integral_flow_cases=(side,rhombi,disjoint_returns,external_internal_vertices)')
    print(flow_cases)
    print('PASS: exact finite pinned-grid checks; no global optimality or C-II closure certified')


if __name__ == '__main__':
    main()
