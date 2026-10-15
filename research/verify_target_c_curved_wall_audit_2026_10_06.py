#!/usr/bin/env python3
"""Exact full-source checks of curved unit-wall inward release.

The infinite sufficiently-small-angle construction is proved in the report.
This script certifies finite rational instances, including every retained
interior isolate and every old/new pair. The wall need not be the full
source hull in the conditional theorem; exterior protection is analytic.
No actual globally optimal source or general chamber chart is asserted.
"""
from fractions import Fraction as F
from itertools import combinations
import json


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, c):
    return a[0] * c, a[1] * c


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def turn(a):
    return -a[1], a[0]


def power(a, n):
    if n < 0:
        a, n = (a[0], -a[1]), -n
    result = F(1), F(0)
    while n:
        if n % 2:
            result = mul(result, a)
        a, n = mul(a, a), n // 2
    return result


def squared(a, b):
    d = sub(a, b)
    return dot(d, d)


def packet(m, tangent):
    assert m >= 4
    c, s = (1-tangent*tangent)/(1+tangent*tangent), 2*tangent/(1+tangent*tangent)
    assert 0 < c < F(1, 2) and s > 0 and c*c+s*s == 1
    u, v = (F(1), F(0)), (c, s)
    t = (1-2*c)/ (10**6*m**4)
    rotation = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    assert dot(rotation, rotation) == 1
    offsets = [power(rotation, 2*j-m+1) for j in range(m)]
    bases = [u, v, scale(u, -1), scale(v, -1)]
    edges = [mul(a, base) for base in bases for a in offsets]
    wall = [(F(0), F(0))]
    for e in edges[:-1]:
        wall.append(add(wall[-1], e))
    assert add(wall[-1], edges[-1]) == (F(0), F(0))
    length = sum(a[0] for a in offsets)
    assert sum(a[1] for a in offsets) == 0 and 0 < length < m
    center = scale(add(u, v), length/2)
    spacing = 1+t/(50*m)
    isolates = [add(center, scale(add(scale(u, F(i)-F(m, 2)),
                                     scale(v, F(j)-F(m, 2))), spacing))
                for i in range(1,m) for j in range(1,m)]
    bank = [side*m+i for side in range(4) for i in range(2,m-1,3)]
    assert len(bank) == 4*((m-1)//3)
    moved = list(wall)
    for index in bank:
        side, i = divmod(index, m)
        normal = turn(mul(power(rotation, 2*i-m), bases[side]))
        moved[index] = add(wall[index], scale(normal, 3*rotation[1]))
    source, target = wall+isolates, moved+isolates
    wall_count, old_contacts = len(wall), set()
    for i in range(wall_count):
        old_contacts.add(tuple(sorted((i,(i+1)%wall_count))))
    new_contacts = {p for p in old_contacts if not (set(p)&set(bank))}
    assert len(new_contacts) == wall_count-2*len(bank)
    convex_checks, interior_checks = 0, 0
    for i, e in enumerate(edges):
        assert dot(e,e) == 1
        for j, p in enumerate(wall):
            if j not in (i,(i+1)%wall_count):
                assert cross(e,sub(p,wall[i])) > 0
                convex_checks += 1
        for p in isolates+[moved[j] for j in bank]:
            assert cross(e,sub(p,wall[i])) > 0
            interior_checks += 1
    for i,j in combinations(bank,2):
        assert squared(wall[i],wall[j]) > 4
    old_diameter = max(squared(source[i],source[j])
                       for i,j in combinations(range(len(source)),2))
    source_pairs, target_pairs, root_upper_checks = 0, 0, 0
    min_old_slack, min_new_slack = None, None
    for i,j in combinations(range(len(source)),2):
        old_d, new_d = squared(source[i],source[j]), squared(target[i],target[j])
        if (i,j) in old_contacts:
            assert old_d == 1
        else:
            assert old_d > 1
            min_old_slack = old_d-1 if min_old_slack is None else min(min_old_slack,old_d-1)
        if (i,j) in new_contacts:
            assert new_d == 1
        else:
            assert new_d > 1
            min_new_slack = new_d-1 if min_new_slack is None else min(min_new_slack,new_d-1)
        assert new_d <= old_diameter
        if i in bank or j in bank:
            assert new_d < old_diameter
            root_upper_checks += 1
        source_pairs += 1
        target_pairs += 1
    # The old neighboring unit contacts open by this exact amount.
    for index in bank:
        for neighbor in ((index-1)%wall_count,(index+1)%wall_count):
            assert squared(moved[index],moved[neighbor])-1 == 3*rotation[1]**2
    return {'M':m,'base_half_angle_tangent':str(tangent),'curvature_half_angle_tangent':str(t),
            'source_points':len(source),'retained_contact_isolates':len(isolates),
            'wall_vertices':wall_count,'moved_wall_vertices':len(bank),
            'old_contacts':len(old_contacts),'new_contacts':len(new_contacts),
            'old_pair_checks':source_pairs,'new_pair_checks':target_pairs,
            'strict_moved_pair_upper_checks':root_upper_checks,
            'strict_convexity_checks':convex_checks,'strict_interior_checks':interior_checks,
            'positive_old_inactive_lower_margin':min_old_slack > 0,
            'positive_new_inactive_lower_margin':min_new_slack > 0,
            'neighbor_squared_contact_release':'3 sin(theta)^2',
            'scope':'feasible rational geometry; not global optimality'}


def contact_blocker_regression():
    """An interior point contacting the deleted vertex blocks the inward root."""
    m, tangent = 4, F(3, 5)
    c, s = (1-tangent*tangent)/(1+tangent*tangent), 2*tangent/(1+tangent*tangent)
    u, v = (F(1), F(0)), (c, s)
    curvature = (1-2*c)/(10**6*m**4)
    rotation = ((1-curvature*curvature)/(1+curvature*curvature),
                2*curvature/(1+curvature*curvature))
    offsets = [power(rotation, 2*j-m+1) for j in range(m)]
    bases = [u, v, scale(u, -1), scale(v, -1)]
    edges = [mul(a, base) for base in bases for a in offsets]
    wall = [(F(0), F(0))]
    for edge in edges[:-1]:
        wall.append(add(wall[-1], edge))
    assert add(wall[-1], edges[-1]) == (F(0), F(0))

    index = 2
    q = wall[index]
    tangent_at_q = mul(power(rotation, 2*index-m), u)
    inward = turn(tangent_at_q)
    z = add(q, add(scale(tangent_at_q, F(7, 25)),
                   scale(inward, F(24, 25))))
    root = add(q, scale(inward, 3*rotation[1]))

    # z is an actual interior source point with a unit contact to deleted q.
    assert squared(z, q) == 1
    source_distances = [squared(z, p) for p in wall]
    assert min(source_distances) == 1
    assert [i for i, d in enumerate(source_distances) if d == 1] == [index]
    assert min(cross(edge, sub(z, wall[i]))
               for i, edge in enumerate(edges)) > 0
    assert all(squared(wall[i], wall[j]) >= 1
               for i, j in combinations(range(len(wall)), 2))

    # The proposed root remains clear of every other wall vertex, yet overlaps z.
    root_wall = [squared(root, p) for i, p in enumerate(wall) if i != index]
    assert min(root_wall) > 1
    overlap = squared(root, z)
    assert overlap < 1
    assert all(d >= 1 for d in source_distances)
    return {'M': m, 'deleted_wall_vertex': index,
            'interior_point_old_wall_contacts': [index],
            'interior_point_squared_distance_to_deleted_vertex': '1',
            'minimum_squared_distance_to_other_old_wall_vertices':
                str(min(d for i, d in enumerate(source_distances) if i != index)),
            'strictly_inside_wall': True,
            'root_strictly_clear_of_other_wall_vertices': True,
            'root_point_squared_distance': str(overlap),
            'root_point_distance_is_less_than_one': True,
            'classification': 'exact local regression; blocker is not a contact isolate'}


def main():
    cases=[packet(m,t) for m,t in [(4,F(3,5)),(6,F(3,4)),(8,F(3,5)),(12,F(3,5))]]
    opening_checks = 0
    for numerator in range(1, 101):
        sine = F(numerator, 1000)
        assert 3-58*sine*sine-45*sine**4 >= F(4831, 2000) > 0
        opening_checks += 1
    print(json.dumps({'classification':'exact finite full-source non-repacking endpoints',
        'cases':cases,'old_pair_checks':sum(c['old_pair_checks'] for c in cases),
        'new_pair_checks':sum(c['new_pair_checks'] for c in cases),
        'all_isolates_retained':True,
        'contact_blocker_regression':contact_blocker_regression(),
        'weak_site_contact_opening_inequality_checks': opening_checks,
        'omitted':['universal chamber chart','uniform analytic curvature threshold',
                   'globally optimal source','Target C-II or Level I closure']},sort_keys=True))


if __name__ == '__main__':
    main()
