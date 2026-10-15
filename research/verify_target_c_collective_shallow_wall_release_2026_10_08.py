#!/usr/bin/env python3
"""Exact shallow-wall packet release and collective-translation regression.

Certifies two nonglobal fixtures, including every source pair and endpoint
pair. It does not prove the analytic wall theorem, canonical packet extraction,
full pinned rank, global optimality, or a same-cardinality strict-D competitor.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def qpoint(x, y):
    return g.Q.of(x), g.Q.of(y)


def interior(point, polygon):
    return all(g.cross(g.sub(b, a), g.sub(point, a)).sign() > 0
               for a, b in zip(polygon, polygon[1:] + polygon[:1]))


def small_triangle_packet():
    left = [(F(12*i, 13), F(5) - F(5*i, 13)) for i in range(14)]
    bottom = [(F(12+i), F(0)) for i in range(1, 11)]
    right = [(F(22) + F(12*i, 13), F(5*i, 13)) for i in range(1, 14)]
    wall = [qpoint(*p) for p in left + bottom + right]
    outside_isolate = qpoint(17, -2)
    old = wall + [outside_isolate]
    packet = [qpoint(i, 1) for i in range(13, 22)]
    packet.append((g.Q(F(33, 2)), g.Q(F(1), F(1, 2))))
    polygon = [wall[0], wall[13], wall[23], wall[-1]]
    assert all(interior(p, polygon) for p in packet)
    # Total turn = 2 acos(12/13) < 120 degrees.
    assert F(12, 13) > F(1, 2)
    source = old + packet
    initial_contacts = []
    initial_checks = 0
    for i, j in combinations(range(len(source)), 2):
        value = g.distance(source[i], source[j])
        assert (value - 1).sign() >= 0
        assert (g.Q(34**2) - value).sign() >= 0
        if value == g.Q(1):
            initial_contacts.append((i, j))
        initial_checks += 1
    start = len(old)
    assert g.distance(packet[3], packet[4]) == g.Q(1)
    assert g.distance(packet[3], packet[-1]) == g.Q(1)
    assert g.distance(packet[4], packet[-1]) == g.Q(1)
    for i, point in enumerate(packet):
        for j, anchor in enumerate(wall):
            if g.distance(point, anchor) == g.Q(1):
                assert j not in (0, len(wall)-1)
                inward = g.sub(point, anchor)
                assert inward[1].sign() > 0
    shift = qpoint(0, F(1, 100))
    center = qpoint(17, F(101, 100))
    translated = [g.add(p, shift) for p in packet]
    endpoint = [g.add(center, g.scale(g.sub(p, center), F(1001, 1000)))
                for p in translated]
    assert all(interior(p, polygon) for p in endpoint)
    after = old + endpoint
    final_checks = 0
    for i, j in combinations(range(len(after)), 2):
        value = g.distance(after[i], after[j])
        assert (value - 1).sign() >= 0
        assert (g.Q(34**2) - value).sign() >= 0
        if j >= start:
            assert (value - 1).sign() > 0
            assert (g.Q(34**2) - value).sign() > 0
        final_checks += 1
    assert (g.distance(outside_isolate, packet[4])-1).sign() > 0
    # The source is nonglobal: 48 sites fit a 7-by-7 unit grid, diameter^2=72.
    assert len(source) <= 49 and 72 < 34**2
    return {"source_pair_checks": initial_checks,
            "endpoint_pair_checks": final_checks,
            "packet_sites": len(packet), "initial_packet_triangle": True,
            "retained_outside_isolates": 1,
            "new_endpoint_contacts": 0, "nonglobal": True}


def integer_points(points):
    denominator = lcm(*(v.denominator for p in points for v in p))
    return [(int(p[0]*denominator), int(p[1]*denominator)) for p in points], denominator


def rational_packet_regression():
    p, q, length = 264, 23, 265
    assert p*p + q*q == length*length
    wall = [(F(7*i, 25), F(24) - F(24*i, 25)) for i in range(26)]
    wall += [(F(7+i), F(0)) for i in range(1, 515)]
    wall += [(F(521) + F(7*i, 25), F(24*i, 25)) for i in range(1, 26)]
    wall = [(F(-16, 65), F(24)+F(63, 65))] + wall + [
        (F(2*p)+F(16, 65), F(24)+F(63, 65))]
    diameter = F(2*p)+F(32, 65)
    root = (F(p), F(1))
    packet = [(F(p*j, length), F(24) - F(q*j, length))
              for j in range(1, length+1)]
    packet += [(F(2*p) - F(p*j, length), F(24) - F(q*j, length))
               for j in range(1, length)]
    old_count = len(wall)
    source = wall + packet
    scaled, den = integer_points(source)
    adjacency = [set() for _ in source]
    initial_checks = 0
    contacts = []
    for i, j in combinations(range(len(source)), 2):
        x = scaled[i][0] - scaled[j][0]
        y = scaled[i][1] - scaled[j][1]
        norm = x*x + y*y
        assert den*den <= norm <= int(diameter*den)**2
        if norm == den*den:
            adjacency[i].add(j)
            adjacency[j].add(i)
            contacts.append((i, j))
        initial_checks += 1
    assert not any(adjacency[i] & adjacency[j] for i, j in contacts)
    moving_rows = [(i, j) for i, j in contacts if j >= old_count]
    assert len(packet) == 529 and len(moving_rows) == 531
    assert len(contacts) == 1097
    bottom_pin = wall.index((F(p), F(0)))
    root_index = source.index(root)
    forces = {i: (F(0), F(0)) for i in range(old_count, len(source))}
    wall_normals = []
    for i, j in moving_rows:
        weight = F(2*q, length) if {i, j} == {bottom_pin, root_index} else F(1)
        vector = (source[j][0] - source[i][0], source[j][1] - source[i][1])
        if i in forces:
            forces[i] = (forces[i][0] + weight*vector[0],
                         forces[i][1] + weight*vector[1])
        if j in forces:
            forces[j] = (forces[j][0] - weight*vector[0],
                         forces[j][1] - weight*vector[1])
        if i < old_count:
            assert i not in (0, old_count-1)
            wall_normals.append((vector, weight))
    assert all(force == (0, 0) for force in forces.values())
    assert len(wall_normals) == 3
    assert tuple(sum(w*v[k] for v, w in wall_normals) for k in (0, 1)) == (0, 0)
    assert all(w > 0 for v, w in wall_normals)
    assert g.cross(wall_normals[0][0], wall_normals[1][0]) != 0
    # 120 < total turn = 2 acos(16/65) < 180 degrees.
    assert F(0) < F(16, 65) < F(1, 2)
    # Pinned full rank is absent, independent of an actual rank computation.
    assert len(moving_rows) < 2*len(packet)
    tangent = F(1, 10**7)
    cosine = (1-tangent*tangent)/(1+tangent*tangent)
    sine = 2*tangent/(1+tangent*tangent)
    extra = tangent*tangent
    endpoint = []
    for x, y in packet:
        dx, dy = x-root[0], y-root[1]
        endpoint.append((root[0]+(1+extra)*(cosine*dx-sine*dy),
                         root[1]+extra+(1+extra)*(sine*dx+cosine*dy)))
    polygon = [wall[0], wall[1], wall[26], wall[540], wall[-2], wall[-1]]
    for point in packet + endpoint:
        assert all(g.cross(g.sub(b, a), g.sub(point, a)) > 0
                   for a, b in zip(polygon, polygon[1:] + polygon[:1]))
    after = wall + endpoint
    scaled, den = integer_points(after)
    final_checks = 0
    for i, j in combinations(range(len(after)), 2):
        x = scaled[i][0]-scaled[j][0]
        y = scaled[i][1]-scaled[j][1]
        norm = x*x+y*y
        assert den*den <= norm <= int(diameter*den)**2
        if j >= old_count:
            assert den*den < norm < int(diameter*den)**2
        final_checks += 1
    # All 1096 source labels fit a 34-by-33 grid of smaller diameter.
    assert len(source) <= 34*33 and 33**2+32**2 < diameter**2
    return {"source_pair_checks": initial_checks,
            "endpoint_pair_checks": final_checks,
            "packet_sites": len(packet),
            "positive_packet_equilibrium_rows": len(moving_rows),
            "exact_packet_equilibria": len(forces),
            "wall_contact_vectors": len(wall_normals),
            "source_unit_rows": len(contacts),
            "source_triangle_free": True,
            "no_nonzero_common_translation": True,
            "finite_rotation_translation_dilation_release": True,
            "new_endpoint_contacts": 0,
            "full_pinned_rank": False, "nonglobal": True}


if __name__ == "__main__":
    print(json.dumps({"classification": "exact finite certificates and regression",
                      "scope": "nonglobal fixtures only; no canonical packet extraction",
                      "shallow_wall": small_triangle_packet(),
                      "larger_turn": rational_packet_regression()}, sort_keys=True))
