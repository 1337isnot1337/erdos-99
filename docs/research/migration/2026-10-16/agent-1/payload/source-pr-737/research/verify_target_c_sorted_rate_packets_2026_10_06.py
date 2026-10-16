#!/usr/bin/env python3
"""Exact sorting packets and radial equality regressions.

Finite arithmetic only; analytic compactness and pinned stress continuation
are in the companion report and require independent review.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
from verify_target_c_nested_hexagon_packet_stress_2026_10_06 import dot,norm,sub


def rotate(p):
    return -p[1],p[0]+p[1]


def rank_mod(rows,cols,prime=1000000007):
    pivots={}
    for original in rows:
        row=[v%prime for v in original]
        for col in range(cols):
            if not row[col]:continue
            if col in pivots:
                factor=row[col]
                old=pivots[col]
                for j in range(col,cols):row[j]=(row[j]-factor*old[j])%prime
            else:
                inverse=pow(row[col],prime-2,prime)
                row=[v*inverse%prime for v in row]
                pivots[col]=row
                break
        if len(pivots)==cols:break
    return len(pivots)


def geometry(m,order,half_angle_tangent=None):
    assert sorted(order)==list(range(-m+1,m,2))
    t=F(1,10**6*m**4) if half_angle_tangent is None else F(half_angle_tangent)
    base=((1-t*t)/(1+t*t),2*t/(1+t*t))
    sixth=(g.Q(F(1,2)),g.Q(F(0),F(1,2)))
    w=g.sub(sixth,(g.Q(1),g.Q()))
    z=[tuple(g.Q(x) for x in g.power(base,k)) for k in order]
    actual={(0,0):(g.Q(),g.Q())}
    first={(0,0):(F(0),F(0))}
    for r in range(1,m+1):
        total=(sum(q[0] for q in z[:r]),sum(q[1] for q in z[:r]))
        chosen=sorted(range(r),key=lambda h:order[h])
        prefix=(g.Q(),g.Q())
        alpha=sum(order[:r])
        for j in range(r+1):
            if j:prefix=g.add(prefix,z[chosen[j-1]])
            value=g.add(total,g.mul(prefix,w))
            s=-sum(sorted(order[:r])[:j])
            velocity=(F(s-alpha,3),F(s+2*alpha,3))
            p=(r-j,j)
            for k in range(6):
                if p in actual:assert actual[p]==value and first[p]==velocity
                actual[p]=value;first[p]=velocity
                p=rotate(p);velocity=rotate(velocity);value=g.mul(value,sixth)
    return actual,first


def case(m,order):
    actual,first=geometry(m,order)
    rad=lambda p:max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))
    moving=sorted(p for p in actual if rad(p)<m)
    assert len(moving)==3*m*m-3*m+1
    wall=[p for p in actual if rad(p)==m]
    assert len(wall)==6*m
    contacts=set();pair_checks=0;first_checks=0;active=[]
    for p,q in combinations(actual,2):
        dist=g.distance(actual[p],actual[q]);assert (dist-1).sign()>=0
        pair_checks+=1
        delta=sub(p,q)
        if norm(delta)==1:
            margin=dot(delta,sub(first[p],first[q]));assert margin>=0
            first_checks+=1
            assert (dist==g.Q(1))==(margin==0)
        if dist==g.Q(1):
            contacts.add(frozenset((p,q)))
            if p in moving or q in moving:active.append((p,q))
    assert len(contacts)==6*m*(m+1)
    assert len(active)==6*m*m
    triangles=[]
    adj={p:set() for p in actual}
    for pair in contacts:
        p,q=pair;adj[p].add(q);adj[q].add(p)
    for p in actual:
        for q,r in combinations(adj[p],2):
            if q in adj[r]:triangles.append(frozenset((p,q,r)))
    triangles=set(triangles)
    assert len(triangles)==6*m
    interior_tri=[tri for tri in triangles if all(rad(p)<m for p in tri)]
    assert len(interior_tri)==6*(m-1)
    centerless=[tri for tri in interior_tri if (0,0) not in tri]
    assert len(centerless)==6*(m-2)>0
    columns={p:i for i,p in enumerate(moving)};rows=[]
    for p,q in active:
        r=sub(p,q);coeff=(2*r[0]+r[1],r[0]+2*r[1]);row=[0]*(2*len(moving))
        if p in columns:
            k=2*columns[p];row[k]+=coeff[0];row[k+1]+=coeff[1]
        if q in columns:
            k=2*columns[q];row[k]-=coeff[0];row[k+1]-=coeff[1]
        rows.append(row)
    rank=rank_mod(rows,2*len(moving));assert rank==2*len(moving)
    # Delete the central columns and all central contact rows, rather than
    # treating the vacancy as a silently retained fixed source point.
    cindex=columns[(0,0)]*2
    vacancy_rows=[row[:cindex]+row[cindex+2:] for pair,row in zip(active,rows)
                  if (0,0) not in pair]
    vacancy_rank=rank_mod(vacancy_rows,2*len(moving)-2)
    assert vacancy_rank==2*len(moving)-2
    energy=[]
    rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
    unit_pairs=[(p,q) for p,q in combinations(moving,2) if norm(sub(p,q))==1]
    for ring in range(m):
        value=F(0)
        for p,q in unit_pairs:
            if rad(p)==rad(q)==ring:value+=3*norm(sub(first[p],first[q]))
        for e in rays:
            for r in range(ring,m):
                p=(r*e[0],r*e[1]);q=((r+1)*e[0],(r+1)*e[1])
                value+=3*norm(sub(first[p],first[q]))
        assert value==2*m*(m*m-1)
        energy.append(str(value))
    return {'M':m,'rate_order':order,'complete_packet_sites':len(moving),
            'all_pair_checks':pair_checks,'first_row_checks':first_checks,
            'unit_contacts':len(contacts),'actual_unit_triangles':len(triangles),
            'interior_unit_triangles':len(interior_tri),
            'center_vacancy_interior_triangles':len(centerless),
            'limiting_pinned_rank_mod_prime':rank,'center_vacancy_rank':vacancy_rank,
            'all_ring_energies':energy,'classification':'feasible triangle-containing packet, not global optimality'}


def main():
    orders=[(3,list(p)) for p in permutations((2,0,-2))]
    orders+=[(m,list(p)) for m in (4,5,6) for p in
             (tuple(range(m-1,-m,-2)),tuple(range(-m+1,m,2)))]
    orders+=[(4,[-3,3,1,-1]),(5,[-4,-2,2,0,4])]
    cases=[case(m,order) for m,order in orders]
    subset_checks=0
    for m in range(3,10):
        order=list(range(m-1,-m,-2))
        assert sum(order)==0
        for k in range(m+1):
            for subset in combinations(order,k):
                assert abs(sum(subset))<=k*(m-k);subset_checks+=1
    print(json.dumps({'classification':'exact sorting packets and equality regression',
        'cases':cases,'all_pair_checks':sum(c['all_pair_checks'] for c in cases),
        'first_row_checks':sum(c['first_row_checks'] for c in cases),
        'subset_checks':subset_checks,
        'not_proved':['arbitrary-cloud compactness','uniform onset',
        'general one-deficit classification','global optimality','C-II or Level I']},sort_keys=True))

if __name__=='__main__':main()
