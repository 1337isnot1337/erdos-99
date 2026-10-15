#!/usr/bin/env python3
"""Exact finite N-site one-deficit replacement packets in Q(sqrt(3)).

The finite cases certify no arbitrary-M or zero-curvature onset theorem.
All old source labels are counted in the companion analytic exchange.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))


def geometry(m, order, t):
    """Rebuild the exact sorting chart at the supplied half-angle tangent."""
    assert sorted(order) == list(range(-m + 1, m, 2))
    base = ((1 - t*t)/(1 + t*t), 2*t/(1 + t*t))
    sixth = (g.Q(F(1, 2)), g.Q(F(0), F(1, 2)))
    w = g.sub(sixth, (g.Q(1), g.Q()))
    z = [tuple(g.Q(x) for x in g.power(base, k)) for k in order]
    actual = {(0, 0): (g.Q(), g.Q())}
    for r in range(1, m + 1):
        total = (sum((q[0] for q in z[:r]), g.Q()),
                 sum((q[1] for q in z[:r]), g.Q()))
        chosen = sorted(range(r), key=lambda h: order[h])
        prefix = (g.Q(), g.Q())
        for j in range(r + 1):
            if j:
                prefix = g.add(prefix, z[chosen[j - 1]])
            value = g.add(total, g.mul(prefix, w))
            p = (r - j, j)
            for _ in range(6):
                if p in actual:
                    assert actual[p] == value
                actual[p] = value
                p = (-p[1], p[0] + p[1])
                value = g.mul(value, sixth)
    return actual


def case(data):
    m = data['M']
    t = F(data['half_angle_tangent'])
    eps = F(data['finite_amplitude'])
    actual = geometry(m, list(range(m - 1, -m, -2)), t)
    hole = tuple(data['hole'])
    deleted = tuple(data['deleted_wall_vertex'])
    assert hole == (1, m - 2) and deleted == (1, m - 1)
    del actual[hole]
    moving = sorted(p for p in actual if rad(p) < m)
    assert moving == [tuple(p) for p in data['moving']]
    field_value = lambda x: (g.Q(F(x[0]), F(x[1])) if isinstance(x, list)
                             else g.Q(F(x)))
    coeff = {p: tuple(field_value(x) for x in row)
             for p, row in zip(moving, data['velocities'])}
    first_checks = 0
    for p, q in combinations(actual, 2):
        if p not in coeff and q not in coeff:
            continue
        if g.distance(actual[p], actual[q]) != g.Q(1):
            continue
        a = g.sub(actual[p], actual[q])
        d = g.sub(coeff.get(p, (g.Q(), g.Q())),
                  coeff.get(q, (g.Q(), g.Q())))
        margin = a[0] * d[0] + a[1] * d[1]
        assert margin.sign() > 0
        first_checks += 1
    rotation = ((1 - t*t)/(1 + t*t), 2*t/(1 + t*t))
    w = (g.Q(F(-1, 2)), g.Q(0, F(1, 2)))
    tangent = g.mul(g.power(rotation, m - 2), w)
    inward = (-tangent[1], tangent[0])
    root = g.add(actual[deleted], g.scale(inward, 3*rotation[1]))
    inserted = [g.add(actual[p], g.scale(coeff[p], eps)) for p in moving]
    inserted.append(root)
    n = 3*m*m - 3*m + 1
    assert len(inserted) == n
    wall = [(m, 0)]
    for _ in range(6*m - 1):
        # Wall index order follows the six sector sides.
        k = len(wall) // m
        j = len(wall) % m
        rays = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
        e, e1 = rays[k], rays[(k+1) % 6]
        wall.append(((m-j)*e[0]+j*e1[0], (m-j)*e[1]+j*e1[1]))
    assert len(set(wall)) == 6*m
    wall_positions = [actual[p] for p in wall]
    retained = [actual[p] for p in wall if p != deleted]
    wall_diameter_squared = max((g.distance(p, q) for p, q in combinations(wall_positions, 2)),
                                key=lambda x: float(x.a)+1.7320508075688772*float(x.b))
    # Certify that the chosen maximum is an exact maximum, rather than relying on the key.
    for p, q in combinations(wall_positions, 2):
        assert (wall_diameter_squared-g.distance(p, q)).sign() >= 0
    lower_checks = upper_checks = containment_checks = 0
    for p in inserted:
        for k, a in enumerate(wall_positions):
            b = wall_positions[(k+1) % len(wall_positions)]
            assert g.cross(g.sub(b, a), g.sub(p, a)).sign() > 0
            containment_checks += 1
        for q in retained:
            d = g.distance(p, q)
            assert (d-1).sign() > 0
            assert (wall_diameter_squared-d).sign() > 0
            lower_checks += 1
            upper_checks += 1
    for p, q in combinations(inserted, 2):
        d = g.distance(p, q)
        assert (d-1).sign() > 0
        assert (wall_diameter_squared-d).sign() > 0
        lower_checks += 1
        upper_checks += 1
    # Old and retained walls have exactly their cyclic contacts and no triangles.
    wall_contacts = set()
    for i, p in enumerate(wall):
        for j in range(i+1, len(wall)):
            d = g.distance(actual[p], actual[wall[j]])
            adjacent = j == i+1 or (i == 0 and j == len(wall)-1)
            assert d == g.Q(1) if adjacent else (d-1).sign() > 0
            if adjacent:
                wall_contacts.add(frozenset((p, wall[j])))
    removed_wall_contacts = sum(deleted in e for e in wall_contacts)
    assert removed_wall_contacts == 2
    assert len(retained)+len(inserted) == 6*m+(n-1)
    return {'M': m, 'half_angle_tangent': str(t), 'amplitude': str(eps),
            'old_interior_population_paid': n-1, 'inserted_sites': n,
            'exact_opening_rows': first_checks, 'strict_new_lower_pairs': lower_checks,
            'strict_new_upper_pairs': upper_checks, 'strict_containment_tests': containment_checks,
            'new_contacts': 0, 'removed_wall_contacts_at_least': 2,
            'new_involving_triangles': 0}


def main():
    path = Path(__file__).with_name('target_c_one_deficit_strict_root_velocity_certificate_2026_10_07.json')
    raw = path.read_bytes()
    result = {'classification': 'exact finite packet certificate',
              'arithmetic': 'Q(sqrt(3)) with rational amplitudes',
              'input_sha256': hashlib.sha256(raw).hexdigest(),
              'scope': 'listed M and positive rational curvatures; no universal onset claimed',
              'cases': [case(d) for d in json.loads(raw)['cases']]}
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
