#!/usr/bin/env python3
"""Exact fixtures for the complete-array diameter-forest candidate.

Finite path and array checks do not prove the universal path integral or bank
argument. Global optimality and canonical positive stresses are not modeled.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as alg


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(a, t):
    return (a[0] * t, a[1] * t)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def norm(a):
    return dot(a, a)


def rot(a):
    return (-a[1], a[0])


def circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def complex_product(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def finite_paths(parameters):
    normals = [circle(t) for t in parameters]
    half_cos, half_sin = circle(max(parameters))
    even_upper = 4 * half_sin * half_sin
    odd_lower = (2 * half_cos - 1) ** 2
    triple_count, invalid_turns = 0, 0
    for i, j, k in product(range(len(normals)), repeat=3):
        if i == j or j == k:
            continue
        a, b, c = normals[i], normals[j], normals[k]
        displacement = add(sub(a, b), c)
        identity = 2 * dot(sub(a, b), sub(c, b))
        assert norm(displacement) - 1 == identity
        monotone = i < j < k or i > j > k
        assert (norm(displacement) <= 1) == monotone
        invalid_turns += not monotone
        triple_count += 1
    path_count, pair_checks = 0, 0
    endpoint_squares = {0: [], 1: []}
    for length in range(1, len(normals) + 1):
        for selected in combinations(range(len(normals)), length):
            orders = [selected] if length == 1 else [selected, selected[::-1]]
            for order in orders:
                points = [(F(0), F(0))]
                for pos, index in enumerate(order):
                    points.append(add(points[-1], scale(normals[index], (-1) ** pos)))
                pairs = [norm(sub(points[i], points[j]))
                         for i, j in combinations(range(len(points)), 2)]
                assert min(pairs) > 0 and max(pairs) == 1
                endpoint = norm(sub(points[-1], points[0]))
                if length % 2:
                    assert endpoint >= odd_lower
                else:
                    assert endpoint <= even_upper
                endpoint_squares[length % 2].append(endpoint)
                path_count += 1
                pair_checks += len(pairs)
    return {'three_edge_identities': triple_count,
            'nonmonotone_sequences_killed_by_an_actual_upper_pair': invalid_turns,
            'valid_monotone_paths': path_count,
            'complete_upper_pair_checks': pair_checks,
            'even_squared_endpoint_upper': str(even_upper),
            'odd_squared_endpoint_lower': str(odd_lower),
            'minimum_odd_endpoint_square': str(min(endpoint_squares[1])),
            'maximum_even_endpoint_square': str(max(endpoint_squares[0])),
            'scope': 'normalized diameter paths; canonical contact/stress data omitted'}


def two_windows():
    u, v = circle(F(1, 8)), circle(F(1, 10))
    half_sum = complex_product(u, v)
    assert 0 < half_sum[1] < F(1, 2) and half_sum[0] > 0
    assert 4 * half_sum[0] ** 2 > 3
    assert 4 * u[1] ** 2 < (2 * v[0] - 1) ** 2
    assert 4 * v[1] ** 2 < (2 * u[0] - 1) ** 2
    return {'half_sum_rotation': [str(x) for x in half_sum],
            'strict_full_window_sum_below_60_degrees': True,
            'both_even_odd_orders_have_strictly_disjoint_endpoint_bounds': True}


def corner_allocations():
    corners = [(0, 0), (0, 1), (1, 0), (1, 1)]
    rows = []
    for x_endpoints in combinations(corners, 2):
        y_endpoints = tuple(p for p in corners if p not in x_endpoints)
        x_parity = x_endpoints[0][1] ^ x_endpoints[1][1]
        y_parity = y_endpoints[0][0] ^ y_endpoints[1][0]
        odd = (x_parity + y_parity + 2) % 2 == 1
        x_delta = sub(x_endpoints[1], x_endpoints[0])
        y_delta = sub(y_endpoints[1], y_endpoints[0])
        if odd:
            assert norm(x_delta) == norm(y_delta) == 1
            assert x_parity != y_parity
        rows.append({'X_endpoints': x_endpoints, 'Y_endpoints': y_endpoints,
                     'X_path_parity': x_parity, 'Y_path_parity': y_parity,
                     'odd_total_parity': odd,
                     'equal_chord_in_odd_case': odd})
    assert sum(row['odd_total_parity'] for row in rows) == 4
    return rows


def qencode(a):
    return [str(a.a), str(a.b)]


def sharp_sixty():
    Q = alg.Q
    normals = [(Q(0, F(1, 2)), Q(F(-1, 2))),
               (Q(0, F(1, 2)), Q(F(1, 2)))]
    points = [(Q(), Q()), normals[0], sub(normals[0], normals[1])]
    for i, j in combinations(range(3), 2):
        assert norm(sub(points[i], points[j])) == Q(1)
    assert dot(normals[0], normals[1]) == Q(F(1, 2))
    # Scaling by thirteen separates diameter triangles from unit-contact ones.
    scaled = [scale(p, 13) for p in points]
    assert all(norm(sub(scaled[i], scaled[j])) == Q(169)
               for i, j in combinations(range(3), 2))
    return {'normalized_points': [[qencode(x) for x in p] for p in points],
            'even_path_edge_count': 2, 'odd_path_edge_count': 1,
            'equal_endpoint_square': '1', 'window_sum_degrees': 60,
            'scaled_all_pair_squares': '169',
            'scope': 'sharp diameter-path boundary; no canonical global source'}


def is_forest(edges):
    vertices = {i for e in edges for i in e}
    parent = {i: i for i in vertices}
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in sorted(edges):
        ri, rj = root(i), root(j)
        if ri == rj:
            return False
        parent[ri] = rj
    return True


def complete_arrays():
    u_options = [circle(t) for t in (F(-1, 8), F(0), F(1, 8))]
    v_options = [rot(circle(t)) for t in (F(-1, 10), F(0), F(1, 10))]
    fixtures, pairs_checked = 0, 0
    graph_counts = Counter()
    for choices in product(range(3), repeat=4):
        us = [u_options[i] for i in choices[:2]]
        vs = [v_options[i] for i in choices[2:]]
        xs, ys = [(F(0), F(0))], [(F(0), F(0))]
        for u in us:
            xs.append(add(xs[-1], u))
        for v in vs:
            ys.append(add(ys[-1], v))
        labels = list(product(range(3), repeat=2))
        index = {p: i for i, p in enumerate(labels)}
        points = [add(xs[i], ys[j]) for i, j in labels]
        pairs = {(i, j): norm(sub(points[i], points[j]))
                 for i, j in combinations(range(9), 2)}
        assert min(pairs.values()) >= 1
        expected = {tuple(sorted((index[(i, j)], index[(i + 1, j)])))
                    for i in range(2) for j in range(3)}
        expected |= {tuple(sorted((index[(i, j)], index[(i, j + 1)])))
                     for i in range(3) for j in range(2)}
        assert {e for e, d in pairs.items() if d == 1} == expected
        assert not any({(i, j), (i, k), (j, k)} <= expected
                       for i, j, k in combinations(range(9), 3))
        diameter = max(pairs.values())
        diameters = {e for e, d in pairs.items() if d == diameter}
        assert is_forest(diameters)
        loaded = {i for e in diameters for i in e}
        for i in loaded:
            assert labels[i][0] in (0, 2) or labels[i][1] in (0, 2)
        graph_counts[(len(loaded), len(diameters))] += 1
        fixtures += 1
        pairs_checked += len(pairs)
    assert fixtures == 81
    return {'complete_bent_unit_array_fixtures': fixtures,
            'full_lower_upper_pair_checks': pairs_checked,
            'diameter_graph_count_by_loaded_vertices_and_edges':
                {f'{q},{h}': count for (q, h), count in sorted(graph_counts.items())},
            'scope': 'all fixture hypotheses of Theorem 1.1; globality/KKT not assumed'}


def additive_only_odd_cycle():
    Q = alg.Q
    x = [(Q(), Q()), (Q(1), Q()), (Q(F(1, 2)), Q(0, F(1, 2)))]
    y = [scale(p, F(1, 2)) for p in x]
    points = [scale(add(a, b), 13) for a in x for b in y]
    pairs = {(i, j): norm(sub(points[i], points[j]))
             for i, j in combinations(range(9), 2)}
    diameter = Q(F(1521, 4))
    assert all((d - 1).sign() > 0 and (diameter - d).sign() >= 0
               for d in pairs.values())
    diameters = {e for e, d in pairs.items() if d == diameter}
    assert diameters == {(0, 4), (0, 8), (4, 8)}
    assert not is_forest(diameters)
    return {'full_pair_checks': len(pairs),
            'diameter_squared': qencode(diameter),
            'actual_odd_diameter_cycle': [0, 4, 8],
            'unit_contacts': 0,
            'scope': 'additive structure alone is insufficient; actual unit cells absent'}


def main():
    result = {'rational_path_bank_U': finite_paths([F(-1, 8), F(-1, 16), F(0),
                                                   F(1, 16), F(1, 8)]),
              'rational_path_bank_V': finite_paths([F(-1, 10), F(-1, 20), F(0),
                                                   F(1, 20), F(1, 10)]),
              'strict_combined_windows': two_windows(),
              'corner_parity_allocations': corner_allocations(),
              'sixty_degree_sharpness': sharp_sixty(),
              'complete_array_fixtures': complete_arrays(),
              'additive_only_odd_cycle_guardrail': additive_only_odd_cycle(),
              'scope': 'exact finite checks; universal proof and canonical application analytic'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
