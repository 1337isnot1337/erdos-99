#!/usr/bin/env python3
"""Reviewer-owned exact checks for PR89 and PR98; imports no submitted code.

PR89 uses rational projection onto the THREE complete fan segments and explicit
convex sector polygons, rather than half-edge traversal or per-edge tube unions.
PR98 exhausts all 32 Hall subsets and checks a separate nonglobality witness.
Run in ordinary Python; assertions below are reviewer checks, not package gates.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json


def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))


def norm2(p):
    return p[0] ** 2 + p[0] * p[1] + p[1] ** 2


def inner(p, q):
    return p[0] * q[0] + p[1] * q[1] + F(p[0] * q[1] + p[1] * q[0], 2)


def segment2(p, a, b):
    v, w = sub(b, a), sub(p, a)
    t = max(F(0), min(F(1), inner(w, v) / norm2(v)))
    return norm2(tuple(w[k] - t * v[k] for k in (0, 1)))


def area(a, b, p):
    v, w = sub(b, a), sub(p, a)
    return v[0] * w[1] - v[1] * w[0]


def polygon_contains(p, poly, strict=False):
    vals = [area(a, b, p) for a, b in zip(poly, poly[1:] + poly[:1])]
    return all(v > 0 if strict else v >= 0 for v in vals)


def addphase(z, phase):
    return tuple(F(a) + b for a, b in zip(z, phase))


PHASES = [(F(1, 1000), F(2, 1000)), (F(1, 50), F(1, 25)), (F(1, 100), F(2, 25))]


def hex_case(m, phase):
    hull = [(m, 0), (0, m), (-m, m), (-m, 0), (0, -m), (m, -m)]
    hull_edges = list(zip(hull, hull[1:] + hull[:1]))
    sources = {z for z in product(range(-m, m + 1), repeat=2)
               if max(abs(z[0]), abs(z[1]), abs(sum(z))) <= m}
    rows = set()
    physical = {}
    for z in product(range(-m - 3, m + 4), repeat=2):
        p = addphase(z, phase)
        if polygon_contains(p, hull) or min(segment2(p, a, b) for a, b in hull_edges) < 1:
            rows.add(z)
            physical[z] = p
    interior = {z for z in rows if polygon_contains(physical[z], hull, True)}
    exterior = rows - interior
    assert interior <= sources
    # A unit-distance pair has axial-coordinate gaps below 2/sqrt(3).
    # This radius-two index search therefore includes every possible neighbor.
    adjacency = {}
    for x in sources:
        candidates = {(x[0] + u, x[1] + v) for u, v in product(range(-2, 3), repeat=2)} & rows
        adjacency[x] = {z for z in candidates if norm2(sub(physical[z], x)) < 1}
    if m == 2:
        assert adjacency == {x: {z for z in rows if norm2(sub(physical[z], x)) < 1}
                             for x in sources}
    assert all(x in adjacency[x] for x in sources)
    assert all(z == x or z[0] + 2 * z[1] < x[0] + 2 * x[1]
               for x in sources for z in adjacency[x] & sources)
    fan_segments = [((-m, 0), (m, 0)), ((1, 0), (1 - m, m)), ((0, 0), (0, 1))]
    tube = {z for z in rows if min(segment2(physical[z], a, b) for a, b in fan_segments) < 1}
    fan_vertices = {x for x in sources if min(segment2(x, a, b) for a, b in fan_segments) == 0}
    sectors = [[(0, 0), (1, 0), (0, 1)],
               [(-m, 0), (0, 0), (0, 1), (1 - m, m), (-m, m)],
               [(1, 0), (m, 0), (0, m), (1 - m, m)],
               [(-m, 0), (0, -m), (m, -m), (m, 0)]]

    def sector(p):
        hits = [i for i, poly in enumerate(sectors) if polygon_contains(p, poly)]
        assert len(hits) == 1
        return hits[0]

    deep = {x for x in sources if adjacency[x] <= interior}

    def population(matching):
        basis = set(matching)
        assert set(matching.values()) == interior and len(basis) == len(interior)
        assert deep <= basis
        assert all(z in adjacency[x] for x, z in matching.items())
        removed = fan_vertices | {x for x, z in matching.items() if z in tube}
        alive = sources - removed
        csets = [{x for x in alive - basis if sector(x) == k} for k in range(4)]
        bsets = [{x for x in alive & basis if sector(x) == k} for k in range(4)]
        zsets = [{z for z in interior - tube if sector(physical[z]) == k} for k in range(4)]
        osets = [{z for x in alive if sector(x) == k for z in adjacency[x] & exterior - tube}
                 for k in range(4)]
        assert list(map(len, bsets)) == list(map(len, zsets))
        assert all(not (a & b) for a, b in combinations(osets, 2))
        isolated = exterior - tube - set().union(*osets)
        bound = len(isolated) + sum(max(0, len(o) - len(c)) for c, o in zip(csets, osets)) - len(tube & interior)
        cap = len(exterior) - len(tube) - sum(min(len(c), len(o)) for c, o in zip(csets, osets))
        assert cap == bound <= 3
        return {'C': list(map(len, csets)), 'O': list(map(len, osets)),
                'B': list(map(len, bsets)), 'Z': list(map(len, zsets)),
                'isolated': len(isolated), 'raw_bound': bound}

    matching = {z: z for z in interior}
    own = population(matching)
    assert len(rows) == 3 * m * m + 9 * m + 4
    assert len(interior) == 3 * m * m and len(exterior) == 9 * m + 4
    assert len(fan_vertices) == 3 * m + 1
    assert len(tube & interior) == 9 * m - 8 and len(tube & exterior) == 9
    assert own['C'] == [0, 1, 2 * m - 2, m]
    assert own['O'] == [0, m - 1, 2 * m - 4, 4 * m - 1]
    assert own['B'] == [0, (m - 1) * (m - 2) // 2, (m - 2) * (m - 3), (3 * m * m - 5 * m + 2) // 2]
    assert own['isolated'] == 2 * m + 1 and own['raw_bound'] == 6 - 3 * m
    no_original_neighbor = rows - set().union(*adjacency.values())
    assert len(no_original_neighbor) == 2 * m
    alternatives = []
    if m == 2:
        for terminal in sources - interior:
            for row in adjacency[terminal] & interior - deep:
                changed = dict(matching)
                del changed[row]
                changed[terminal] = row
                alternatives.append(population(changed)['raw_bound'])
    if m >= 7:
        assert 133 * len(tube & interior) - 924 * m - 792 == 273 * m - 1856 > 0
    return {'m': m, 'phase': list(map(str, phase)), 'source': len(sources),
            'collar': len(rows), 'tube_interior': len(tube & interior), 'tube_exterior': len(tube & exterior),
            'own_basis_ledger': own, 'deep_columns': len(deep),
            'single_exchange_admissible_bases': len(alternatives),
            'alternative_raw_bounds': sorted(set(alternatives))}


def cart2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def overlap_fixture():
    X = [(F(-1, 5), F(-1, 5)), (F(16, 5), F(-1, 5)), (F(3, 2), F(2))]
    Y = [(F(0), F(0)), (F(3), F(0))]
    A = [(F(-1, 2), F(-1, 5)), (F(7, 2), F(-1, 5)), (F(3, 2), F(29, 10)), (F(6), F(0)), (F(9), F(-1, 5))]
    assert all(polygon_contains(y, X, True) for y in Y)
    assert all(not polygon_contains(a, X) for a in A)
    sd = {str((i, j)): cart2(A[i], A[j]) for i, j in combinations(range(5), 2)}
    assert min(sd.values()) == F(629, 100) and max(sd.values()) == F(361, 4)
    assert max(cart2(a, b) for a, b in combinations(X, 2)) == F(289, 25)
    L = X + Y
    adj = [{j for j, a in enumerate(A) if cart2(p, a) < 1} for p in L]
    assert adj == [{0}, {1}, {2}, {0}, {1}]
    deficiencies = []
    for bits in product((0, 1), repeat=5):
        chosen = [i for i, b in enumerate(bits) if b]
        neighbors = set().union(*(adj[i] for i in chosen)) if chosen else set()
        deficiencies.append(len(chosen) - len(neighbors))
    assert max(deficiencies) == 2
    # Fully retained source has a much smaller same-cardinality packing.
    half = [tuple(a / 2 for a in p) for p in A]
    assert min(cart2(a, b) for a, b in combinations(half, 2)) > 1
    assert max(cart2(a, b) for a, b in combinations(half, 2)) == F(361, 16)
    # The selected Y is not the complete canonical response lattice.
    missing = (F(1), F(0))
    assert polygon_contains(missing, X, True)
    assert not any(cart2(missing, a) < 1 for a in A)
    return {'all_source_squared_distances': {k: str(v) for k, v in sd.items()},
            'adjacency_zero_based': [sorted(s) for s in adj], 'Hall_subsets': len(deficiencies),
            'maximum_Hall_deficiency': max(deficiencies), 'joint_matching_size': 3,
            'explicit_nonglobal_competitor': 'A/2; diameter 19/4; minimum squared distance 629/400',
            'scope_control': 'Interior lattice point (1,0) has no source neighbor, so Y is a selected subset, not Y_in.'}


def main():
    cases = [hex_case(m, phase) for m in (2, 7) for phase in PHASES]
    cases += [hex_case(m, PHASES[0]) for m in (13, 32)]
    print(json.dumps({'reviewer': '/root/merge_review_a', 'status': 'PASS',
                      'pr89_independent_cases': cases, 'pr98_independent_fixture': overlap_fixture()}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
