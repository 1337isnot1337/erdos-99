#!/usr/bin/env python3
"""Exact finite checks of small-slack wall triangulations and constants.

The universal arbitrary-wall reconstruction is the analytic theorem in
the companion report. These finite sorting examples do not prove it or
establish a uniform finite-triangle classification.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_sorted_rate_packets_2026_10_06 as s
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


DIRECTIONS = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0]+p[1]))


def flat_norm(p):
    return p[0]*p[0]+p[0]*p[1]+p[1]*p[1]


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def incircle(a, b, c, d):
    a, b, c = g.sub(a,d), g.sub(b,d), g.sub(c,d)
    return (g.norm(a)*g.cross(b,c)-g.norm(b)*g.cross(a,c)
            +g.norm(c)*g.cross(a,b))


def case(m):
    t = F(1, 20000*m**3)
    actual, _ = s.geometry(m, list(range(m-1,-m,-2)), t)
    triangles = set()
    for p in actual:
        neighbours = [(p[0]+d[0],p[1]+d[1]) for d in DIRECTIONS]
        neighbours = [q for q in neighbours if q in actual]
        for q,r in combinations(neighbours,2):
            if flat_norm((q[0]-r[0],q[1]-r[1])) == 1:
                triangles.add(frozenset((p,q,r)))
    assert len(triangles) == 6*m*m
    incidence = {}
    valence = {p:0 for p in actual}
    area = g.Q()
    baseline = g.Q(0,F(1,4))
    checks = 0
    for triangle in sorted(triangles,key=lambda x: sorted(x)):
        p,q,r = sorted(triangle)
        cross = g.cross(g.sub(actual[q],actual[p]),g.sub(actual[r],actual[p]))
        if cross.sign() < 0:
            q,r = r,q
            cross = -cross
        excess = cross*F(1,2)-baseline
        assert excess.sign() >= 0
        area += cross*F(1,2)
        sides = [g.distance(actual[a],actual[b]) for a,b in combinations((p,q,r),2)]
        assert (4*cross*cross-sides[0]*sides[1]*sides[2]).sign() >= 0
        for a,b,c in ((p,q,r),(q,p,r),(r,p,q)):
            assert dot(g.sub(actual[b],actual[a]),g.sub(actual[c],actual[a])).sign() > 0
        for value in sides:
            assert ((1+5*excess)*(1+5*excess)-value).sign() >= 0
        for a in (p,q,r):
            valence[a] += 1
        for a,b in combinations((p,q,r),2):
            incidence.setdefault(frozenset((a,b)),[]).append((p,q,r))
        checks += 1
    internal = 0
    for edge,adjacent in incidence.items():
        assert len(adjacent) in (1,2)
        if len(adjacent) == 2:
            p,q,r = adjacent[0]
            d = next(a for a in adjacent[1] if a not in edge)
            assert incircle(actual[p],actual[q],actual[r],actual[d]).sign() <= 0
            internal += 1
        else:
            assert all(rad(p)==m for p in edge)
            p,q = tuple(edge)
            assert g.distance(actual[p],actual[q]) == g.Q(1)
    sigma = area-baseline*(6*m*m)
    assert sigma.sign() >= 0 and (g.Q(F(1,1000))-sigma).sign() > 0
    pair_checks = 0
    for p,q in combinations(actual,2):
        assert (g.distance(actual[p],actual[q])-1).sign() >= 0
        pair_checks += 1
    for p in actual:
        is_corner = p in [(m*d[0],m*d[1]) for d in DIRECTIONS]
        assert valence[p] == (6 if rad(p)<m else 2 if is_corner else 3)
        flat = (g.Q(F(2*p[0]+p[1],2)),g.Q(0,F(p[1],2)))
        assert (g.Q((1000*m**4*t)**2)-g.distance(actual[p],flat)).sign() > 0
    return {'M':m,'half_angle_tangent':str(t),'triangles':checks,
            'exact_internal_delaunay_checks':internal,'all_pair_checks':pair_checks,
            'sigma_Qsqrt3':[str(sigma.a),str(sigma.b)],
            'valence_and_displacement_checks':len(actual)}


def main():
    baseline = g.Q(0,F(1,4))
    gap = g.Q(F(1,2),F(-1,4))
    assert (gap-F(1,1000)).sign() > 0
    # f(11/10)>sqrt(3)/4+1/1000, checked by positive squares.
    threshold = baseline+F(1,1000)
    assert (g.Q(F(33759,160000))-threshold*threshold).sign() > 0
    deficit = g.Q(F(1,1000),F(1,2))
    assert (52*gap-4*deficit).sign() > 0
    assert (87-100*deficit).sign() > 0
    assert (131-150*deficit).sign() > 0
    one_deficit_constants = {'obtuse_triangles_at_most':51,
                             'high_excess_triangles_at_most':86,
                             'outside_nonhex_vertices_at_most':130,
                             'exceptional_vertices_at_most':541}
    results = [case(m) for m in (4,5,6,8,10)]
    print(json.dumps({'classification':'exact finite effective-chart checks',
                      'cases':results,'one_deficit_constants':one_deficit_constants,
                      'scope':'listed sorting packets and proof constants'},sort_keys=True))


if __name__=='__main__':
    main()
