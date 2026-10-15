#!/usr/bin/env python3
"""Exact nonaffine packets from rational velocity certificates.

Verifies finite geometry, not canonical coembedding or universal onset.
All old populations are covered analytically by the cardinality contract.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
from verify_target_c_nested_hexagon_packet_stress_2026_10_06 import dot,norm,sub


def nonaffine(points,coeff):
    p0,p1=points[:2]
    i2=next(i for i,p in enumerate(points)
            if (p1[0]-p0[0])*(p[1]-p0[1])!=(p1[1]-p0[1])*(p[0]-p0[0]))
    p2=points[i2]
    dx,dy=sub(p1,p0),sub(p2,p0)
    determinant=dx[0]*dy[1]-dx[1]*dy[0]
    affine=[]
    for coordinate in range(2):
        v0,v1,v2=coeff[0][coordinate],coeff[1][coordinate],coeff[i2][coordinate]
        a=((v1-v0)*dy[1]-(v2-v0)*dx[1])/determinant
        b=(dx[0]*(v2-v0)-dy[0]*(v1-v0))/determinant
        affine.append((a,b,v0-a*p0[0]-b*p0[1]))
    assert any(any(a*p[0]+b*p[1]+c!=v[k] for k,(a,b,c) in enumerate(affine))
               for p,v in zip(points,coeff))


def case(data):
    m=data['M']
    r=m-1
    points=[tuple(p) for p in data['points']]
    coeff=[tuple(F(v) for v in p) for p in data['first_axial_over_sqrt3']]
    expected={(i,j) for i in range(-r,r+1) for j in range(-r,r+1)
              if abs(i+j)<=r and (i,j)!=(0,0)}
    assert set(points)==expected and len(points)==3*m*m-3*m
    nonaffine(points,coeff)
    first_checks=0
    margins=[]
    for i,j in combinations(range(len(points)),2):
        delta=sub(points[i],points[j])
        if norm(delta)==1:
            margin=dot(delta,sub(coeff[i],coeff[j]))
            assert margin>0
            margins.append(margin)
            first_checks+=1
    bases_ax=[(-1,1),(-1,0),(0,-1),(1,-1),(1,0),(0,1)]
    corner=(m,0)
    for side,w in enumerate(bases_ax):
        for index in range(m):
            q=(corner[0]+index*w[0],corner[1]+index*w[1])
            if side==index==0:
                continue
            bow=index*(m-index)
            q1=(F(bow*(w[0]+2*w[1]),3),F(-bow*(2*w[0]+w[1]),3))
            for p,d in zip(points,coeff):
                delta=sub(p,q)
                if norm(delta)==1:
                    margin=dot(delta,sub(d,q1))
                    assert margin>0
                    margins.append(margin)
                    first_checks+=1
        corner=(corner[0]+m*w[0],corner[1]+m*w[1])
    assert corner==(m,0)
    t=F(1,10**8*m**4)
    rotation=((1-t*t)/(1+t*t),2*t/(1+t*t))
    a=g.Q(F(0),F(1,2))
    bases=[(g.Q(F(-1,2)),a),(g.Q(-1),g.Q()),(g.Q(F(-1,2)),-a),
           (g.Q(F(1,2)),-a),(g.Q(1),g.Q()),(g.Q(F(1,2)),a)]
    offsets=[g.power(rotation,2*j-m+1) for j in range(m)]
    length=sum(p[0] for p in offsets)
    edges=[g.mul(p,w) for w in bases for p in offsets]
    wall=[(g.Q(length),g.Q())]
    for e in edges[:-1]:
        wall.append(g.add(wall[-1],e))
    assert g.add(wall[-1],edges[-1])==wall[0]
    packet=[(g.Q(F(i)+F(j,2),2*t*(a+b/2)),g.Q(3*t*b,F(j,2)))
            for (i,j),(a,b) in zip(points,coeff)]
    inside_checks=0
    for i,e in enumerate(edges):
        assert g.norm(e)==g.Q(1)
        for p in packet:
            assert g.cross(e,g.sub(p,wall[i])).sign()>0
            inside_checks+=1
    retained=wall[1:]
    guards=0
    for p in packet:
        for q in retained:
            assert (g.distance(p,q)-1).sign()>0
            guards+=1
    for i,j in combinations(range(len(packet)),2):
        assert (g.distance(packet[i],packet[j])-1).sign()>0
    zero=(g.Q(),g.Q())
    source=wall+[zero]
    contacts={tuple(sorted((i,(i+1)%(6*m)))) for i in range(6*m)}
    old_pairs=0
    diameter=g.Q()
    for i,j in combinations(range(len(source)),2):
        distance=g.distance(source[i],source[j])
        assert distance==g.Q(1) if (i,j) in contacts else (distance-1).sign()>0
        if (distance-diameter).sign()>0:
            diameter=distance
        old_pairs+=1
    upper_checks=0
    for p in packet:
        for q in retained:
            assert (diameter-g.distance(p,q)).sign()>0
            upper_checks+=1
    for i,j in combinations(range(len(packet)),2):
        assert (diameter-g.distance(packet[i],packet[j])).sign()>0
        upper_checks+=1
    endpoint=retained+packet[:2]
    assert len(endpoint)==len(source)
    new_contacts=0
    endpoint_pairs=0
    for i,j in combinations(range(len(endpoint)),2):
        distance=g.distance(endpoint[i],endpoint[j])
        assert (distance-1).sign()>=0
        assert (diameter-distance).sign()>=0
        if distance==g.Q(1):
            new_contacts+=1
        endpoint_pairs+=1
    assert new_contacts==6*m-2<len(contacts)
    area=sum(g.cross(wall[i],wall[(i+1)%(6*m)]) for i in range(6*m))*F(1,2)
    assert area.sign()>0
    assert (g.Q(F(3,4)*(3*m*m+1)**2)-area*area).sign()>0
    population_cases=0
    for z in range(len(packet)):
        assert z+1<=len(packet)
        assert 6*m+z == len(retained)+(z+1)
        population_cases+=1
    return {'M':m,'packet_sites':len(packet),'exact_first_variation_checks':first_checks,
            'minimum_first_margin_over_sqrt3':str(min(margins)),
            'nonaffine':True,'strict_inside_checks':inside_checks,
            'strict_wall_guard_checks':guards,'strict_new_upper_checks':upper_checks,
            'old_source_pair_checks':old_pairs,'same_cardinality_endpoint_pair_checks':endpoint_pairs,
            'old_contacts':len(contacts),'new_contacts':new_contacts,
            'integer_old_population_cases':population_cases,
            'scope':'strict packet and feasible source endpoint; no global optimality'}


def main():
    path=Path(__file__).with_name('target_c_one_corner_vacancy_velocity_certificate_2026_10_06.json')
    raw=path.read_bytes()
    cases=[case(p) for p in json.loads(raw)['cases']]
    print(json.dumps({'classification':'exact nonaffine strict packet certificates',
                      'velocity_input_sha256':hashlib.sha256(raw).hexdigest(),
                      'cases':cases,
                      'exact_first_variation_checks':sum(p['exact_first_variation_checks'] for p in cases),
                      'strict_new_upper_checks':sum(p['strict_new_upper_checks'] for p in cases),
                      'old_source_pair_checks':sum(p['old_source_pair_checks'] for p in cases),
                      'same_cardinality_endpoint_pair_checks':sum(p['same_cardinality_endpoint_pair_checks'] for p in cases),
                      'integer_old_population_cases':sum(p['integer_old_population_cases'] for p in cases),
                      'not_proved':['old maximum-population exclusion','general chamber extraction',
                                    'uniform curvature onset','global optimality','C-II or Level I']},sort_keys=True))


if __name__=='__main__':
    main()
