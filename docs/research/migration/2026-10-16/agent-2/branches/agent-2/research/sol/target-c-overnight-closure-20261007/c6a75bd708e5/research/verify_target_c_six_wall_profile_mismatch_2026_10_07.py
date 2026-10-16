#!/usr/bin/env python3
"""Exact opposed-profile walls and first-profile variance certificates.

The analytic subsequence argument, not these examples, excludes maximal
population. This script does not search arbitrary clouds or optimality.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def case(name, triples):
    profiles=triples+triples
    m=len(profiles[0]);assert all(len(a)==m for a in profiles)
    for a in profiles:
        assert sum(a)==0 and all(x<y for x,y in zip(a,a[1:]))
    energy=[sum(x*x for x in a) for a in profiles]
    distances={(k,l):sum((x-y)**2 for x,y in zip(profiles[k],profiles[l]))
               for k,l in combinations(range(6),2)}
    mismatch=max(distances.values());assert mismatch>0
    t=F(1,100000)
    base=((1-t*t)/(1+t*t),2*t/(1+t*t))
    sixth=(g.Q(F(1,2)),g.Q(0,F(1,2)))
    origin=(g.Q(),g.Q()); position=(g.Q(m),g.Q());wall=[];edges=[];corners=[]
    direction=g.mul(sixth,sixth)
    for profile in profiles:
        corners.append(position)
        for rate in profile:
            wall.append(position)
            z=tuple(g.Q(x) for x in g.power(base,rate))
            edge=g.mul(direction,z);assert g.distance(edge,origin)==g.Q(1)
            edges.append(edge);position=g.add(position,edge)
        direction=g.mul(direction,sixth)
    assert position==wall[0]
    def cross(p,q):return p[0]*q[1]-p[1]*q[0]
    def dot(p,q):return p[0]*q[0]+p[1]*q[1]
    supports=0
    for i,p in enumerate(wall):
        for j,q in enumerate(wall):
            if j not in (i,(i+1)%len(wall)):
                assert cross(edges[i],g.sub(q,p)).sign()>0
                supports+=1
    lower=0
    for i,j in combinations(range(len(wall)),2):
        d=g.distance(wall[i],wall[j]);adj=(j==i+1 or (i==0 and j==len(wall)-1))
        assert d==g.Q(1) if adj else (d-1).sign()>0
        lower+=1
    area=sum((cross(wall[i],wall[(i+1)%len(wall)]) for i in range(len(wall))),g.Q())*F(1,2)
    olerrhs=g.Q(2*area.b,F(2,3)*area.a)+3*m+1
    n=3*m*m-3*m+1
    assert (olerrhs-(n+6*m+1)).sign()<0
    # Telescoping finite wall work checked in the actual fixed flat frame.
    e=(g.Q(1),g.Q());radialwork=g.Q();edgework=g.Q()
    direction=g.mul(sixth,sixth)
    for k in range(6):
        radialwork+=dot(e,g.sub(corners[k],g.scale(e,F(m))))
        for j in range(m):edgework+=dot(direction,edges[k*m+j])-1
        e=g.mul(e,sixth);direction=g.mul(direction,sixth)
    assert radialwork==edgework and radialwork.sign()<0
    return {'name':name,'M':m,'opposed_profiles':profiles,'energies':energy,
        'max_pair_sorted_distance_squared':mismatch,
        'positive_variance_obstruction':str(F(mismatch,2)),
        'energy_minimum_gap':str(F(sum(energy),6)-min(energy)),
        'half_angle_tangent':str(t),'unit_edges':len(edges),
        'wall_lower_pairs':lower,'strict_support_tests':supports,
        'finite_corner_work':[str(radialwork.a),str(radialwork.b)],
        'population_cap':n,'source_realization_claim':False}


if __name__=='__main__':
    out=[case('unequal energies',[[-3,-1,1,3],[-4,-1,1,4],[-5,-2,2,5]]),
         case('equal energies distinct multisets',[[-65,-13,13,65],[-55,-37,37,55],[-65,-13,13,65]])]
    print(json.dumps({'classification':'exact boundary and mismatch certificates',
      'scope':'listed walls; universal profile necessity is analytic; no global source claim',
      'cases':out},sort_keys=True))
