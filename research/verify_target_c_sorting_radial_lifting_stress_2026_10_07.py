#!/usr/bin/env python3
"""Audit replay of exact finite r^2 lifting stresses for sorting packets.

All listed pair, face-gradient and equilibrium checks are exact. This
finite verifier does not establish all-M/all-permutation positivity. The
geometry constructor is pinned locally to the frozen source version because
the main helper's API changed after that snapshot. The universal radial-lifting
argument is an exploratory continuation lead.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
DIRECTIONS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
Z=(g.Q(),g.Q())


def rotate(p):
    return -p[1],p[0]+p[1]


def geometry(m,order,half_angle_tangent):
    """Pinned copy of the frozen sorting geometry at the requested tangent."""
    assert sorted(order)==list(range(-m+1,m,2))
    t=F(half_angle_tangent)
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
            for _ in range(6):
                if p in actual:
                    assert actual[p]==value and first[p]==velocity
                actual[p]=value
                first[p]=velocity
                p=rotate(p)
                velocity=rotate(velocity)
                value=g.mul(value,sixth)
    return actual,first


def rad(p):return max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def J(p):return (-p[1],p[0])
def div(p,q):
    den=q.a*q.a-3*q.b*q.b;assert den
    return (p*g.Q(q.a,-q.b))*F(1,den)
def flatnorm(p):return p[0]*p[0]+p[0]*p[1]+p[1]*p[1]


def case(order):
    m=len(order);t=F(1,200*m*m)
    actual,_=geometry(m,list(order),t)
    triangles=set()
    for p in actual:
        neighbours=[(p[0]+d[0],p[1]+d[1]) for d in DIRECTIONS]
        neighbours=[q for q in neighbours if q in actual]
        for q,r in combinations(neighbours,2):
            if flatnorm((q[0]-r[0],q[1]-r[1]))==1:
                triangles.add(frozenset((p,q,r)))
    assert len(triangles)==6*m*m
    incidence={};gradients={}
    for idx,triangle in enumerate(sorted(triangles,key=lambda x:sorted(x))):
        p,q,r=sorted(triangle)
        v,w=g.sub(actual[q],actual[p]),g.sub(actual[r],actual[p])
        det=g.cross(v,w)
        if det.sign()<0:q,r=r,q;v,w=w,v;det=-det
        assert det.sign()>0
        hq,hr=g.Q(rad(q)**2-rad(p)**2),g.Q(rad(r)**2-rad(p)**2)
        grad=(div(hq*w[1]-hr*v[1],det),div(v[0]*hr-w[0]*hq,det))
        assert dot(grad,v)==hq and dot(grad,w)==hr
        gradients[idx]=grad
        for a,b in combinations((p,q,r),2):
            edge=tuple(sorted((a,b)))
            third=next(x for x in (p,q,r) if x not in edge)
            side=g.cross(g.sub(actual[edge[1]],actual[edge[0]]),g.sub(actual[third],actual[edge[0]])).sign()
            assert side in (-1,1)
            incidence.setdefault(edge,[]).append((idx,side))
    forces={p:Z for p in actual if rad(p)<m}
    weights=[];counts={'ring':0,'radial':0,'weak':0,'nonunit_zero':0}
    total=g.Q();pairs=0
    for p,q in combinations(actual,2):
        assert (g.distance(actual[p],actual[q])-1).sign()>=0;pairs+=1
    for (p,q),adjacent in incidence.items():
        if len(adjacent)==1:
            assert rad(p)==rad(q)==m
            continue
        assert len(adjacent)==2 and {side for idx,side in adjacent}=={-1,1}
        left=next(idx for idx,side in adjacent if side==1)
        right=next(idx for idx,side in adjacent if side==-1)
        jump=g.sub(gradients[left],gradients[right]);edge=g.sub(actual[q],actual[p])
        value=div(dot(jump,J(edge)),g.norm(edge))
        assert jump==g.scale(J(edge),value.a) if value.b==0 else \
            jump==(value*J(edge)[0],value*J(edge)[1])
        if g.norm(edge)!=g.Q(1):
            assert value==g.Q();counts['nonunit_zero']+=1;continue
        assert value.sign()>0
        same_ray=any(p==(rad(p)*d[0],rad(p)*d[1]) and q==(rad(q)*d[0],rad(q)*d[1]) for d in DIRECTIONS)
        # A center edge is radial even though center lies on every ray.
        if rad(p)==rad(q):kind='ring';assert (value-2).sign()>=0 and (3-value).sign()>=0
        elif same_ray:kind='radial';assert (value-1).sign()>=0
        else:kind='weak';assert (value-g.Q(t)).sign()>0
        counts[kind]+=1;total+=value;weights.append(value)
        force=(value*edge[0],value*edge[1])
        if p in forces:forces[p]=g.add(forces[p],force)
        if q in forces:forces[q]=g.sub(forces[q],force)
    assert all(force==Z for force in forces.values())
    assert len(weights)==6*m*m and counts['nonunit_zero']==3*m*(m-1)
    assert (g.Q(30*m*m)-total).sign()>0
    return {'M':m,'order':order,'half_angle_tangent':str(t),'triangles':len(triangles),
       'gradient_compatibility_checks':len(incidence)-6*m,'all_pair_checks':pairs,
       'positive_unit_rows':len(weights),'row_classes':counts,
       'exact_moving_vertex_equilibria':len(forces),'total_weight_bound':30*m*m,
       'height':'ring radius squared'}


if __name__=='__main__':
    orders=list(permutations((3,1,-1,-3)))
    for m in (6,8,10):
        a=list(range(m-1,-m,-2));orders.extend((tuple(a),tuple(reversed(a)),tuple(a[::2]+a[1::2])))
    out=[case(order) for order in orders]
    print(json.dumps({'classification':'exact finite radial-lifting stress certificates',
      'scope':'33 listed permutations at t=1/(200M^2); no universal positivity claim',
      'cases':out},sort_keys=True))
