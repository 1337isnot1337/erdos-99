#!/usr/bin/env python3
"""Finite exact scope checks for deep-face persistence and isolate transport.

The universal harmonic/persistence claims are analytic in the report. The
fixtures are nonglobal and do not encode canonical full-support stresses.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt
import json
import verify_target_c_quarter_fold_face_obstructions_2026_10_10 as g


def perimeter_labels(a, b):
    return ([(i, 0) for i in range(a+1)] +
            [(a, j) for j in range(1, b+1)] +
            [(i, b) for i in range(a-1, -1, -1)] +
            [(0, j) for j in range(b-1, 0, -1)])


def transport():
    u, v = g.point(1, 0), g.point(F(5, 13), F(12, 13))
    labels = perimeter_labels(3, 3)
    wall = [g.add(g.scale(u, i), g.scale(v, j)) for i, j in labels]
    z = [g.sub(g.scale(u, i), g.scale(v, j)) for i, j in labels]
    signs = [1]*3 + [-1]*3 + [1]*3 + [-1]*3
    image = g.verify_fold(wall, signs, z)
    isolate = g.add(g.scale(u, F(11, 10)), g.scale(v, F(103, 100)))
    old, c, d = g.ledger(wall + [isolate])
    assert c == g.cycle_edges(12)
    # The correct isometry is T(x) = U_b - J(x), with b=(3,0).
    moved = g.sub(image[3], g.J(isolate))
    new, cc, dd = g.ledger(image + [moved])
    assert cc == c and d == dd == g.Q(F(324, 13))
    permutation = []
    for i, p in enumerate(wall):
        q = g.sub(image[3], g.J(p))
        j = image.index(q)
        assert labels[j] == (3-labels[i][0], labels[i][1])
        permutation.append(j)
    assert permutation != list(range(12))
    assert sorted(old.values(), key=lambda q: q.a) == sorted(new.values(), key=lambda q: q.a)
    # The naive label-affine transport collides with the boundary label (1,0).
    naive = g.J(g.sub(g.scale(u, F(11, 10)), g.scale(v, F(103, 100))))
    collision = g.distance(naive, image[1])
    assert collision == g.Q(F(128917, 130000))
    assert (collision - 1).sign() < 0
    return {'labels': 13, 'full_pair_checks': len(old)+len(new),
            'diameter_squared': d.encode(),
            'boundary_permutation': permutation,
            'naive_transport_collision_squared': collision.encode(),
            'old_min_isolate_clearance_squared': g.exact_min(
                [g.distance(isolate, p) for p in wall]).encode(),
            'correct_min_isolate_clearance_squared': g.exact_min(
                [g.distance(moved, p) for p in image]).encode()}


def intrusion():
    labels = perimeter_labels(3, 3)
    wall = [g.point(i, j) for i, j in labels]
    z = [g.point(i, -j) for i, j in labels]
    q = g.point(F(5, 13), -F(12, 13))
    old_leaf = g.add(wall[1], q)
    new_leaf = g.add(z[1], q)
    old, c, d = g.ledger(wall+[old_leaf])
    new, cc, dd = g.ledger(z+[new_leaf])
    assert c == cc == g.cycle_edges(12) | {(1, 12)}
    assert d == dd == g.Q.of(18)
    old_h = {e for e, v in old.items() if v == d}
    new_h = {e for e, v in new.items() if v == dd}
    assert (6, 12) in old_h
    assert all(12 not in e for e in new_h)
    assert 0 < new_leaf[0].a < 3 and -3 < new_leaf[1].a < 0
    assert old_leaf[1].a < 0
    # The same cycle is no longer a simple face boundary: a bridge is inside.
    released = list(z)+[g.add(new_leaf, g.scale(q, F(1, 100)))]
    final, ccc, ddd = g.ledger(released)
    assert ccc == g.cycle_edges(12) and ddd == dd
    assert all((dd-v).sign() >= 0 for v in final.values())
    return {'full_pair_checks': len(old)+len(new)+len(final),
            'old_diameter_pairs': sorted(old_h),
            'new_diameter_pairs': sorted(new_h),
            'old_loaded_intruding_label': 12,
            'intruding_component_size': 1,
            'old_loaded_distance_to_wall': '1',
            'release_amplitude': '1/100',
            'scope': 'nonglobal; old unloaded vertex 1 fails positive equilibrium'}


def atan_bounds(x, n=16):
    terms = [(-1)**k * x**(2*k+1)/F(2*k+1) for k in range(n)]
    s = sum(terms, F(0))
    next_term = (-1)**n * x**(2*n+1)/F(2*n+1)
    return min(s, s+next_term), max(s, s+next_term)


def capacities():
    # Machin identity: tan(4 atan(1/5)-atan(1/239))=1 in the first quadrant.
    x = F(1, 5)
    t2 = 2*x/(1-x*x)
    t4 = 2*t2/(1-t2*t2)
    assert (t4-F(1,239))/(1+t4*F(1,239)) == 1
    a_lo, a_hi = atan_bounds(F(1, 5))
    b_lo, b_hi = atan_bounds(F(1, 239))
    pi_lo, pi_hi = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
    denom = 10**15
    k = isqrt(3*denom*denom)
    sqrt_lo, sqrt_hi = F(k, denom), F(k+1, denom)
    assert sqrt_lo**2 < 3 < sqrt_hi**2
    assert 3 < pi_lo < pi_hi < 4
    rows = []
    for m in range(5, 33):
        lo = F(m*m)/(2*pi_hi*sqrt_hi) - F(m, 2) + 1
        hi = F(m*m)/(2*pi_lo*sqrt_lo) - F(m, 2) + 1
        floor_lo, floor_hi = lo.numerator//lo.denominator, hi.numerator//hi.denominator
        assert floor_lo == floor_hi
        rows.append({'face_degree': m, 'component_capacity': floor_lo,
                     'maximum_face_charge_per_lost_loaded_label':
                     5*(2*floor_lo+1)**2})
    return {'table': rows,
            'arithmetic': 'exact alternating-series pi enclosure; integer sqrt(3) enclosure',
            'scope': 'floor arithmetic only; Oler and face persistence are analytic'}


def nonglobal_comparator():
    # Euclidean Gram form for the unit triangular basis (1,0),(1/2,sqrt(3)/2).
    def norm(p):
        i, j = p
        return i*i+j*j+i*j
    disk = [(i, j) for i in range(-2, 3) for j in range(-2, 3)
            if norm((i, j)) <= 4]
    assert len(disk) == 19
    packet = disk[:13]
    pairs = [norm((a[0]-b[0], a[1]-b[1])) for a, b in combinations(packet, 2)]
    assert min(pairs) >= 1 and max(pairs) <= 16 < 18
    return {'labels': packet, 'pair_checks': len(pairs),
            'diameter_squared': max(pairs),
            'scope': 'explicit strict competitor to both nonglobal 13-label fixtures'}


def loaded_port_patterns():
    neighbors = [g.point(F(5,13),-F(12,13)), g.point(1,0),
                 g.point(F(5,13),F(12,13))]
    old, c, _ = g.ledger([g.point(0,0)]+neighbors)
    assert c == {(0,1),(0,2),(0,3)}
    assert (g.distance(neighbors[0],neighbors[2])-3).sign() > 0
    feasible = []
    failures = 0
    for signs in product((-1,1),repeat=3):
        image = [g.J(g.scale(p,s)) for p,s in zip(neighbors,signs)]
        pairs = [g.distance(a,b) for a,b in combinations(image,2)]
        if any((d-1).sign()<0 for d in pairs):
            failures += 1
            assert signs[0] != signs[2]
            continue
        assert signs[0] == signs[2]
        surrounding = signs[1] != signs[0]
        if surrounding:
            assert g.add(g.add(g.scale(image[0],13),g.scale(image[1],10)),
                         g.scale(image[2],13)) == g.point(0,0)
        feasible.append({'signs': signs, 'strict_surrounding': surrounding})
    assert failures == 4 and len(feasible) == 4
    assert sum(s['strict_surrounding'] for s in feasible) == 2
    return {'feasible_patterns': feasible, 'colliding_patterns': failures,
            'scope': 'local hull contact-ray universe; actual diameter load, globality, and full-source motion are not modeled'}


def main():
    result = {'permuted_wall_isolate_transport': transport(),
              'actual_loaded_leaf_intrusion_guardrail': intrusion(),
              'deep_face_component_capacity': capacities(),
              'strict_nonglobal_comparator': nonglobal_comparator(),
              'local_loaded_port_patterns': loaded_port_patterns(),
              'scope': 'finite scope checks; no canonical global minimizer modeled'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
