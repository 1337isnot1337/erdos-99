#!/usr/bin/env python3
"""Exact finite scope checks for pinned stress and nonconstant-face arc stars.

The fixtures omit global optimality and normalized full diameter stress.
Universal persistence is proved analytically in the companion report.
"""

from fractions import Fraction as F
from itertools import product
import json
import verify_target_c_quarter_fold_face_obstructions_2026_10_10 as g
import verify_target_c_deep_face_transport_2026_10_10 as transport


def determinant(matrix):
    a = [[F(x) for x in row] for row in matrix]
    value = F(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value *= -1
        p = a[k][k]
        value *= p
        for j in range(k, len(a)):
            a[k][j] /= p
        for i in range(k+1, len(a)):
            coefficient = a[i][k]
            for j in range(k, len(a)):
                a[i][j] -= coefficient*a[k][j]
    return value


def pinned_grid():
    u, v = g.point(1, 0), g.point(F(5, 13), F(12, 13))
    labels = [(i, j) for i in range(4) for j in range(4)]
    points = [g.add(g.scale(u, i), g.scale(v, j)) for i, j in labels]
    distances, contacts, diameter = g.ledger(points)
    expected = {(i, j) for i in range(16) for j in range(i+1, 16)
                if sum(abs(a-b) for a, b in zip(labels[i], labels[j])) == 1}
    assert contacts == expected and len(contacts) == 24
    assert diameter == g.Q(F(324, 13))
    interior = [i for i, (a, b) in enumerate(labels) if 0 < a < 3 and 0 < b < 3]
    matrix = [[0 for _ in interior] for _ in interior]
    for row, i in enumerate(interior):
        neighbors = [j if i == k else k for k, j in contacts if i in (k, j)]
        assert len(neighbors) == 4
        force = g.point(0, 0)
        for j in neighbors:
            force = g.add(force, g.sub(points[i], points[j]))
        assert force == g.point(0, 0)
        matrix[row][row] = len(neighbors)
        for column, j in enumerate(interior):
            if j in neighbors:
                matrix[row][column] = -1
    assert determinant(matrix) == 192
    # Arbitrary test displacement, with the entire boundary pinned at zero.
    displacement = [g.point(0, 0) for _ in labels]
    for k, i in enumerate(interior):
        displacement[i] = g.point(F(k+1, 7), F(2*k-3, 11))
    edge_energy = sum((g.distance(displacement[i], displacement[j])
                       for i, j in contacts if i in interior or j in interior), g.Q.of(0))
    matrix_energy = g.Q.of(0)
    for row, i in enumerate(interior):
        for column, j in enumerate(interior):
            dot = (displacement[i][0]*displacement[j][0] +
                   displacement[i][1]*displacement[j][1])
            matrix_energy += dot*matrix[row][column]
    assert edge_energy == matrix_energy and edge_energy.sign() > 0
    return {'source_labels': len(points), 'full_pair_checks': len(distances),
            'contacts': len(contacts), 'interior_labels': [labels[i] for i in interior],
            'positive_interior_equilibria': len(interior),
            'grounded_contact_laplacian': matrix, 'grounded_determinant': '192',
            'displacement_energy': edge_energy.encode(),
            'scope': 'pinned contact net; globality and full diameter stress omitted'}


def arc_stars():
    boundary = [g.point(F(5,13), -F(12,13)), g.point(F(5,13), F(12,13))]
    fixtures = {
        'degree_three': (boundary + [g.point(-1, 0)], [13, 13, 10]),
        'degree_four': (boundary + [g.point(-F(4,5), F(3,5)),
                                   g.point(-F(4,5), -F(3,5))], [52, 52, 25, 25])}
    result = {}
    for name, (neighbors, weights) in fixtures.items():
        old, c, _ = g.ledger([g.point(0,0)] + neighbors)
        assert c == {(0, i) for i in range(1, len(neighbors)+1)}
        force = g.point(0,0)
        for p, weight in zip(neighbors, weights):
            force = g.add(force, g.scale(p, weight))
        assert force == g.point(0,0)
        assert (g.distance(boundary[0], boundary[1])-3).sign() > 0
        lower_patterns = []
        surrounded_patterns = []
        collision_count = 0
        pair_checks = len(old)
        for signs in product((-1,1), repeat=len(neighbors)):
            image = [g.point(0,0)] + [g.J(g.scale(p,s)) for p, s in zip(neighbors, signs)]
            pairs = {e: g.distance(image[e[0]], image[e[1]]) for e in old}
            pair_checks += len(pairs)
            if any((d-1).sign() <= 0 for e, d in pairs.items() if 0 not in e):
                collision_count += 1
                continue
            lower_patterns.append(signs)
            if len(set(signs)) == 1:
                image_force = g.point(0,0)
                for p, weight in zip(image[1:], weights):
                    image_force = g.add(image_force, g.scale(p, weight))
                assert image_force == g.point(0,0)
                surrounded_patterns.append(signs)
            else:
                assert name == 'degree_three' and signs[0] == signs[1] != signs[2]
                # All folded unit rays are strictly on one side of y=0.
                assert all((p[1]*signs[0]).sign() > 0 for p in image[1:])
        assert len(surrounded_patterns) == 2
        assert len(lower_patterns) == (4 if name == 'degree_three' else 2)
        result[name] = {'old_positive_equilibrium_weights': weights,
                        'lower_feasible_sign_patterns': lower_patterns,
                        'strictly_surrounded_patterns': surrounded_patterns,
                        'lower_failure_patterns': collision_count,
                        'full_pair_checks': pair_checks,
                        'scope': 'local ray geometry; no actual global minimizer modeled'}
    return result


def main():
    print(json.dumps({'pinned_unit_grid': pinned_grid(), 'internal_arc_stars': arc_stars(),
                      'missing_endpoint_equilibrium_guardrail': transport.intrusion(),
                      'scope': 'exact finite checks; universal theorem remains analytic'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
