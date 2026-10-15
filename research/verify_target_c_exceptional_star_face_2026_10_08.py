#!/usr/bin/env python3
"""Exact star-face and two-stage codimension fixtures, not E99 closure.

The report proves the universal star classification analytically.
These finite nonglobal sources verify its sharpness and limits.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
from verify_target_c_accessible_stress_faces_2026_10_08 import qrank, psd_rank


def census(points, diameter_squared):
    contacts, diameters = [], []
    for i, j in combinations(range(len(points)), 2):
        distance = g.distance(points[i], points[j])
        assert (distance-1).sign() >= 0
        assert (g.Q.of(diameter_squared)-distance).sign() >= 0
        if distance == g.Q(1):
            contacts.append((i, j))
        if distance == g.Q.of(diameter_squared):
            diameters.append((i, j))
    contact_set = set(contacts)
    triangles = [triple for triple in combinations(range(len(points)), 3)
                 if all(tuple(sorted(edge)) in contact_set
                        for edge in combinations(triple, 2))]
    return contacts, diameters, triangles


def equilibrium_and_ranks(points, contacts, diameters, alpha, beta):
    size = len(points)
    assert all(x >= 0 for x in alpha+beta) and sum(beta) == 1
    omega = [[F(0) for _ in points] for _ in points]
    rigidity = []
    for edges, weights, sign in ((contacts, alpha, 1), (diameters, beta, -1)):
        for (i, j), weight in zip(edges, weights):
            difference = g.sub(points[i], points[j])
            row = [g.Q() for _ in range(2*size)]
            row[2*i:2*i+2] = difference
            row[2*j:2*j+2] = tuple(-x for x in difference)
            rigidity.append(row)
            omega[i][i] += sign*weight
            omega[j][j] += sign*weight
            omega[i][j] -= sign*weight
            omega[j][i] -= sign*weight
    assert all(sum(row) == 0 for row in omega)
    for coordinate in range(2):
        assert all(sum((g.Q.of(omega[i][j])*points[j][coordinate]
                        for j in range(size)), g.Q()) == g.Q()
                   for i in range(size))
    return qrank(rigidity), psd_rank(omega), qrank(rigidity[:len(contacts)])


def competitor(size, old_diameter_squared):
    width = 1
    while width*width < size:
        width += 1
    points = [(g.Q(i % width), g.Q(i//width)) for i in range(size)]
    values = [g.distance(a, b) for a, b in combinations(points, 2)]
    assert all((value-1).sign() >= 0 for value in values)
    maximum = max(value.a for value in values)
    assert all(value.b == 0 for value in values)
    assert (g.Q.of(old_diameter_squared)-maximum).sign() > 0
    return str(maximum)


def straight_chains():
    cases = []
    for length in (10, 11, 12):
        points = [(g.Q(j), g.Q()) for j in range(length+1)]
        points.append((g.Q(F(length, 2)), g.Q(2)))
        contacts, diameters, triangles = census(points, length*length)
        assert contacts == [(j, j+1) for j in range(length)]
        assert diameters == [(0, length)] and not triangles
        rank, psd, contact_rank = equilibrium_and_ranks(
            points, contacts, diameters, [F(length)]*length, [F(1)])
        assert rank == contact_rank == length and psd == length-1
        chain_vertices = length+1
        sigma = 2*chain_vertices-2-(length+1)
        assert sigma == length-1
        cases.append({"D": length, "source_points": len(points),
                      "source_pairs": len(points)*(len(points)-1)//2,
                      "contact_isolates": 1, "unit_triangles": 0,
                      "rigidity_rank": rank, "psd_rank": psd,
                      "contact_row_rank": contact_rank,
                      "selected_sigma": sigma,
                      "smaller_competitor_diameter_squared":
                          competitor(len(points), length*length)})
    return cases


def arms_at_sixty_degrees():
    length = 10
    u = (g.Q(1), g.Q())
    v = (g.Q(F(1, 2)), g.Q(F(0), F(1, 2)))
    points = [(g.Q(), g.Q())]
    points += [g.scale(u, j) for j in range(1, length+1)]
    points += [g.scale(v, j) for j in range(1, length+1)]
    contacts, diameters, triangles = census(points, length*length)
    assert len(contacts) == 2*length+1
    assert diameters == [(0, length), (0, 2*length), (length, 2*length)]
    assert triangles == [(0, 1, length+1)]
    cross = (1, length+1)
    alpha = [F(0) if edge == cross else F(length, 2) for edge in contacts]
    beta = [F(1, 2), F(1, 2), F(0)]
    rank, psd, contact_rank = equilibrium_and_ranks(
        points, contacts, diameters, alpha, beta)
    assert rank == 2*length+2 and psd == 2*(length-1)
    assert contact_rank == len(contacts)
    x = (g.Q(1), g.Q())
    y = (g.Q(F(3, 5)), g.Q(F(4, 5)))
    short = g.distance(x, y)
    assert short == g.Q(F(4, 5))
    return {"source_points": len(points),
            "source_pairs": len(points)*(len(points)-1)//2,
            "unit_triangles": 1, "positive_diameter_edges": 2,
            "shared_hub": 0, "psd_rank": psd,
            "rigidity_rank": rank, "contact_row_rank": contact_rank,
            "smaller_competitor_diameter_squared":
                competitor(len(points), length*length),
            "below_sixty_first_neighbor_squared_distance": str(short.a),
            "below_sixty_unit_separation_fails": True}


def y_cycles():
    directions = [(g.Q(1), g.Q()),
                  (g.Q(F(-1, 2)), g.Q(F(0), F(1, 2))),
                  (g.Q(F(-1, 2)), g.Q(F(0), F(-1, 2)))]
    cases = []
    for length in (6, 8, 10):
        points = [(g.Q(), g.Q())]
        endpoints = []
        for direction in directions:
            points += [g.scale(direction, j) for j in range(1, length+1)]
            endpoints.append(len(points)-1)
        contacts, diameters, triangles = census(points, 3*length*length)
        assert len(contacts) == 3*length and not triangles
        assert diameters == list(combinations(endpoints, 2))
        rank, psd, contact_rank = equilibrium_and_ranks(
            points, contacts, diameters, [F(length)]*len(contacts),
            [F(1, 3)]*3)
        assert rank == 3*length+2 and psd == len(points)-3
        assert contact_rank == len(contacts)
        sigma = 2*len(points)-2-(len(contacts)+len(diameters))
        assert sigma == 3*length-3
        assert rank < 2*len(points)-3
        cases.append({"arm_length": length, "source_points": len(points),
                      "source_pairs": len(points)*(len(points)-1)//2,
                      "unit_triangles": 0, "diameter_cycle_edges": 3,
                      "rigidity_rank": rank, "psd_rank": psd,
                      "contact_row_rank": contact_rank,
                      "affine_scalar_kernel_dimension": 3,
                      "selected_sigma": sigma,
                      "canonical_mixed_rigidity": False,
                      "smaller_competitor_diameter_squared":
                          competitor(len(points), 3*length*length)})
    return cases


def affine_dimension(vertices):
    if len(vertices) <= 1:
        return len(vertices)-1
    origin = vertices[0]
    return qrank([[x-y for x, y in zip(vertex, origin)]
                  for vertex in vertices[1:]])


def minimum_cover(values, selected_vertices):
    for size in range(len(values)+1):
        for chosen in combinations(range(len(values)), size):
            if all(any(values[i][j] > 0 for i in chosen)
                   for j in selected_vertices):
                return chosen
    raise AssertionError("uncovered face")


def two_stage_check(vertices, accessible, contacts):
    assert all(value >= 0 for row in accessible+contacts for value in row)
    dimension = affine_dimension(vertices)
    exceptional = [j for j in range(len(vertices))
                   if all(row[j] == 0 for row in accessible)]
    assert exceptional
    face_dimension = affine_dimension([vertices[j] for j in exceptional])
    exceptions = minimum_cover(contacts, exceptional)
    count = len(exceptions)
    assert count <= face_dimension+1
    witnesses = []
    for chosen in exceptions:
        witness = next(j for j in exceptional if contacts[chosen][j] > 0
                       and all(contacts[i][j] == 0 for i in exceptions
                               if i != chosen))
        witnesses.append(vertices[witness])
    assert affine_dimension(witnesses) == count-1
    surviving = [j for j in range(len(vertices))
                 if all(contacts[i][j] == 0 for i in exceptions)]
    surviving_dimension = affine_dimension([vertices[j] for j in surviving])
    if surviving:
        assert surviving_dimension <= dimension-count
        selected = minimum_cover(accessible, surviving)
        assert len(selected) <= surviving_dimension+1
    else:
        selected = ()
    assert len(selected)+count <= dimension+1
    assert all(any(contacts[i][j] > 0 for i in exceptions)
               or any(accessible[i][j] > 0 for i in selected)
               for j in range(len(vertices)))
    return {"abstract_dimension": dimension,
            "exceptional_face_dimension": face_dimension,
            "unloaded_exceptions": count,
            "surviving_face_dimension": surviving_dimension,
            "accessible_deletions": len(selected),
            "total_deletions": count+len(selected),
            "total_bound": dimension+1,
            "planar_source_model": False}


def two_stage_faces():
    from itertools import product
    cases = []
    for dimension in range(1, 8):
        for face_dimension in range(dimension):
            vertices = [[F(int(i == j)) for i in range(dimension+1)]
                        for j in range(dimension+1)]
            contacts = [[vertex[i] for vertex in vertices]
                        for i in range(face_dimension+1)]
            accessible = [[vertex[i] for vertex in vertices]
                          for i in range(face_dimension+1, dimension+1)]
            result = two_stage_check(vertices, accessible, contacts)
            assert result["unloaded_exceptions"] == face_dimension+1
            assert result["total_deletions"] == dimension+1
            cases.append({"kind": "simplex", **result})
    for dimension in range(2, 8):
        for face_dimension in range(1, dimension):
            apices = dimension-face_dimension
            vertices = [list(x)+[F(0)]*apices for x in
                        product((F(0), F(1)), repeat=face_dimension)]
            vertices += [[F(0)]*face_dimension+
                         [F(int(i == j)) for i in range(apices)]
                         for j in range(apices)]
            accessible = [[vertex[face_dimension+i] for vertex in vertices]
                          for i in range(apices)]
            # Both functions are affine and nonnegative on every vertex
            # of the join. Their common zero face is the apex simplex.
            contacts = [[vertex[0] for vertex in vertices],
                        [1-sum(vertex[face_dimension:])-vertex[0]
                         for vertex in vertices]]
            result = two_stage_check(vertices, accessible, contacts)
            assert result["unloaded_exceptions"] == 2
            assert result["surviving_face_dimension"] == apices-1
            cases.append({"kind": "cube-simplex join", **result})
    for dimension in range(8):
        vertices = [[F(int(i == j)) for i in range(dimension+1)]
                    for j in range(dimension+1)]
        contacts = [[vertex[i] for vertex in vertices]
                    for i in range(dimension+1)]
        result = two_stage_check(vertices, [], contacts)
        assert result["surviving_face_dimension"] == -1
        assert result["total_deletions"] == dimension+1
        cases.append({"kind": "full simplex empty remainder", **result})
    for dimension in range(1, 8):
        vertices = [list(x) for x in product((F(0), F(1)), repeat=dimension)]
        contacts = [[vertex[0] for vertex in vertices],
                    [1-vertex[0] for vertex in vertices]]
        result = two_stage_check(vertices, [], contacts)
        assert result["surviving_face_dimension"] == -1
        assert result["total_deletions"] == 2
        cases.append({"kind": "full cube empty remainder", **result})
    assert len(cases) == 64
    return cases


if __name__ == "__main__":
    print(json.dumps({"classification": "exact finite star-face certificates",
                      "scope": "nonglobal fixtures and abstract faces; no star extraction or refill",
                      "integer_chains_with_isolates": straight_chains(),
                      "triangle_free_hypothesis_test": arms_at_sixty_degrees(),
                      "nonstar_cycle_limits": y_cycles(),
                      "two_stage_face_codimension": two_stage_faces()},
                     sort_keys=True))
