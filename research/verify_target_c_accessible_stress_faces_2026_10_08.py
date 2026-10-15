#!/usr/bin/env python3
"""Exact stress-face certificates; no canonical grid/refill extraction.

The seven-site source contains unit triangles. Abstract simplex/cube checks
are not source models. Analytic Helly and canonical extreme-circuit input
prove the report's conditional dichotomy, not these finite samples.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def divide(a, b):
    denominator = b.a*b.a-3*b.b*b.b
    assert denominator
    return a*g.Q(b.a, -b.b)*F(1, denominator)


def qrank(matrix):
    work = [[g.Q.of(x) for x in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(row, len(work))
                      if work[i][column] != g.Q()), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][column]
        work[row] = [divide(x, scale) for x in work[row]]
        for i in range(row+1, len(work)):
            factor = work[i][column]
            if factor != g.Q():
                work[i] = [a-factor*b for a, b in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def psd_rank(matrix):
    work = [row[:] for row in matrix]
    rank = 0
    while work:
        assert all(work[i][i] >= 0 for i in range(len(work)))
        pivot = next((i for i in range(len(work)) if work[i][i] > 0), None)
        if pivot is None:
            assert all(x == 0 for row in work for x in row)
            return rank
        indices = [i for i in range(len(work)) if i != pivot]
        diagonal = work[pivot][pivot]
        work = [[work[i][j]-work[i][pivot]*work[pivot][j]/diagonal
                 for j in indices] for i in indices]
        rank += 1
    return rank


def stress_matrix(contacts, diameters, alpha, beta):
    matrix = [[F(0) for _ in range(7)] for _ in range(7)]
    for edges, weights, sign in ((contacts, alpha, 1), (diameters, beta, -1)):
        for (i, j), weight in zip(edges, weights):
            value = sign*weight
            matrix[i][i] += value
            matrix[j][j] += value
            matrix[i][j] -= value
            matrix[j][i] -= value
    return matrix


def polytope_face_checks(values, dimension):
    count, covered, largest = 0, 0, 0
    for size in range(len(values)+1):
        for chosen in combinations(range(len(values)), size):
            count += 1
            covers = all(any(values[i][j] > 0 for i in chosen)
                         for j in range(len(values[0])))
            if not covers:
                continue
            covered += 1
            minimum = None
            for number in range(min(len(chosen), dimension+1)+1):
                for subset in combinations(chosen, number):
                    if all(any(values[i][j] > 0 for i in subset)
                           for j in range(len(values[0]))):
                        minimum = number
                        break
                if minimum is not None:
                    break
            assert minimum is not None and minimum <= dimension+1
            largest = max(largest, minimum)
    return {"tagged_subsets": count, "empty_exceptional_faces": covered,
            "largest_minimum_transversal": largest}


def source_case():
    a0 = g.Q(F(0), F(1, 2))
    points = [(g.Q(1), g.Q()), (g.Q(F(1, 2)), a0),
              (g.Q(F(-1, 2)), a0), (g.Q(-1), g.Q()),
              (g.Q(F(-1, 2)), -a0), (g.Q(F(1, 2)), -a0),
              (g.Q(), g.Q())]
    contacts, diameters = [], []
    for i, j in combinations(range(7), 2):
        value = g.distance(points[i], points[j])
        assert (value-1).sign() >= 0 and (g.Q(4)-value).sign() >= 0
        if value == g.Q(1):
            contacts.append((i, j))
        if value == g.Q(4):
            diameters.append((i, j))
    assert len(contacts) == 12 and diameters == [(0, 3), (1, 4), (2, 5)]
    triangles = [triple for triple in combinations(range(7), 3)
                 if all(tuple(sorted(edge)) in contacts
                        for edge in combinations(triple, 2))]
    assert len(triangles) == 6
    rigidity = []
    for i, j in contacts+diameters:
        vector = g.sub(points[i], points[j])
        row = [g.Q() for _ in range(14)]
        row[2*i:2*i+2] = vector
        row[2*j:2*j+2] = tuple(-x for x in vector)
        rigidity.append(row)
    assert qrank(rigidity) == 11
    vertices = []
    ranks = []
    for index in range(4):
        beta = [F(int(j == index)) for j in range(3)] if index < 3 else [F(1, 3)]*3
        common = F(0) if index < 3 else F(2, 3)
        alpha = [2*beta[i % 3]-common if j == 6 else common for i, j in contacts]
        assert all(x >= 0 for x in alpha+beta) and sum(beta) == 1
        omega = stress_matrix(contacts, diameters, alpha, beta)
        for coordinate in range(2):
            assert all(sum((g.Q.of(omega[i][j])*points[j][coordinate]
                            for j in range(7)), g.Q()) == g.Q() for i in range(7))
        assert all(sum(row) == 0 for row in omega)
        ranks.append(psd_rank(omega))
        vertices.append((alpha, beta, omega))
    assert ranks == [1, 1, 1, 3]
    assert qrank([[v[0][i] for v in vertices] for i in range(12)]+
                 [[v[1][i] for v in vertices] for i in range(3)]) == 4
    samples = []
    for epsilon in (F(1, 10), F(1, 100), F(1, 1000), F(1, 10**6)):
        coefficients = [1-3*epsilon, epsilon, epsilon, epsilon]
        alpha = [sum(w*v[0][i] for w, v in zip(coefficients, vertices)) for i in range(12)]
        beta = [sum(w*v[1][i] for w, v in zip(coefficients, vertices)) for i in range(3)]
        assert all(x > 0 for x in alpha+beta)
        common = F(2, 3)*epsilon
        assert all(beta[i]-common/2 == coefficients[i] for i in range(3))
        omega = stress_matrix(contacts, diameters, alpha, beta)
        assert psd_rank(omega) == 4
        assert beta[0] == 1-F(8, 3)*epsilon
        samples.append({"epsilon": str(epsilon), "untagged_mass": str(beta[0])})
    tagged = {1, 2, 4, 5}
    missed = vertices[0]
    assert sum(missed[1][j] for j, edge in enumerate(diameters)
               if tagged.intersection(edge)) == 0
    faces = polytope_face_checks(
        [[sum(v[1][j] for j, edge in enumerate(diameters) if b in edge)
          for v in vertices] for b in range(6)], 3)
    support = [rigidity[i] for i, weight in enumerate(missed[0]+missed[1]) if weight > 0]
    assert len(support) == 3 and qrank(support) == 2
    sigma = 2*3-2-len(support)
    assert sigma == 1 == 2-1
    return {"source_pairs": 21, "unit_contacts": 12, "diameter_pairs": 3,
            "unit_triangles": 6, "global_optimality_certified": False,
            "mixed_rank": 11, "stress_polytope_dimension": 3,
            "vertex_psd_ranks": ranks, "relative_interior_rank": 4,
            "selected_sigma": sigma, "relative_interior_mass_samples": samples,
            "accessible_face_checks": faces}


def abstract_faces():
    cases = []
    for dimension in range(1, 7):
        size = dimension+1
        values = [[F(int(i == j)) for j in range(size)] for i in range(size)]
        result = polytope_face_checks(values, dimension)
        assert result["largest_minimum_transversal"] == dimension+1
        cases.append({"kind": "simplex", "dimension": dimension, **result})
    for dimension in range(1, 5):
        vertices = list(product((F(0), F(1)), repeat=dimension))
        values = [[vertex[i] if sign else 1-vertex[i] for vertex in vertices]
                  for i in range(dimension) for sign in (0, 1)]
        result = polytope_face_checks(values, dimension)
        assert result["largest_minimum_transversal"] == 2
        cases.append({"kind": "cube", "dimension": dimension, **result})
    return cases


def rational_bounds():
    cases = []
    for diameter in (10, 100, 1000):
        for bad in sorted({1, 2, diameter//10, diameter//5}):
            bound = F(diameter)-F((bad-1)**2, 2*diameter)-F(bad+1, 2)
            assert bound > 0
            if bad == 1:
                assert bound == diameter-1
            cases.append({"D": diameter, "bad_edge_bound": bad,
                          "rational_sigma_lower": str(bound)})
    return cases


if __name__ == "__main__":
    print(json.dumps({"classification": "exact finite stress-face certificates",
                      "scope": "triangle-containing source and abstract polytopes only; no grid/refill extraction",
                      "seven_site_source": source_case(),
                      "abstract_face_checks": abstract_faces(),
                      "rational_defect_bounds": rational_bounds()}, sort_keys=True))
