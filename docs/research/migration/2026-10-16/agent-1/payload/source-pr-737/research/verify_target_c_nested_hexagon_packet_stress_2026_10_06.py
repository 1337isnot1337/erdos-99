#!/usr/bin/env python3
"""Exact selected-support stress identities; target chart, not old source.

The limiting triangular grid contains unit triangles. It is not claimed
to be a canonical triangle-free source or a feasible strict packet.
"""
from fractions import Fraction as F
from itertools import combinations
import json


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def sub(a,b):
    return a[0]-b[0],a[1]-b[1]


def scale(a,t):
    return a[0]*t,a[1]*t


def dot(a,b):
    return a[0]*b[0]+F(a[0]*b[1]+a[1]*b[0],2)+a[1]*b[1]


def norm(a):
    return dot(a,a)


def packet(m):
    radius=m-1
    points={(i,j) for i in range(-radius,radius+1)
                   for j in range(-radius,radius+1) if abs(i+j)<=radius}
    assert len(points)==3*radius*radius+3*radius+1
    rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
    guards={scale(e,m) for e in rays}
    coords=points|guards
    all_edges={tuple(sorted((a,b))) for a,b in combinations(points,2)
               if norm(sub(a,b))==1}
    assert len(all_edges)==9*radius*radius+3*radius
    selected_union=set()
    equilibrium_checks=0
    polynomial_checks=0
    c=F(m*(m*m-1),6)
    for ring in range(radius+1):
        boundary={p for p in points if max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))==ring}
        ring_edges={e for e in all_edges if all(p in boundary for p in e)}
        assert len(ring_edges)==6*ring
        selected=set(ring_edges)
        for e in rays:
            for r in range(ring,m):
                selected.add(tuple(sorted((scale(e,r),scale(e,r+1)))))
        assert len(selected)==6*m
        selected_union|=selected
        force={p:(F(0),F(0)) for p in coords}
        for a,b in selected:
            edge=sub(a,b)
            assert norm(edge)==1
            force[a]=add(force[a],edge)
            force[b]=sub(force[b],edge)
        for p in points:
            assert force[p]==(0,0)
            equilibrium_checks+=1
        for e in rays:
            assert force[scale(e,m)]==e
        for mode in (1,2,3):
            d={p:(F(mode*p[0]**2+p[1],7),F(p[0]-mode*p[1]**2,11)) for p in points}
            b={p:(F(mode*p[0]+p[1]**2,13),F(p[0]**2-mode*p[1],17)) for p in points}
            for e in rays:
                guard=scale(e,m)
                d[guard]=(F(0),F(0))
                b[guard]=scale(e,-c)
            first=F(0)
            second=F(0)
            energy=F(0)
            for a,z in selected:
                r=sub(a,z)
                velocity=sub(d[a],d[z])
                acceleration=sub(b[a],b[z])
                first+=2*dot(r,velocity)
                energy+=norm(velocity)
                second+=norm(velocity)+2*dot(r,acceleration)
            assert first==0
            assert second==energy-12*c
            polynomial_checks+=1
    assert len(selected_union)==3*m*(m+1)
    return {'M':m,'limiting_packet_sites':len(points),'positive_radius_rings':radius,
            'stresses_including_center':radius+1,
            'selected_support_union':len(selected_union),'equilibrium_checks':equilibrium_checks,
            'chosen_field_cancellation_checks':polynomial_checks,
            'corner_load':str(12*c),'strict_packet_proved':False}


def main():
    cases=[packet(m) for m in range(3,13)]
    print(json.dumps({'classification':'exact selected stress and energy identities',
                      'cases':cases,
                      'equilibrium_checks':sum(c['equilibrium_checks'] for c in cases),
                      'chosen_field_cancellation_checks':sum(c['chosen_field_cancellation_checks'] for c in cases),
                      'not_proved':['completeness of forced-zero classification',
                                    'energy upper bound','strict finite packet',
                                    'global optimality','C-II or Level I']},sort_keys=True))


if __name__=='__main__':
    main()
