#!/usr/bin/env python3
"""Complete exact finite sign universes and source pair-ledger regressions.

Canonical arbitrary-source endpoint existence is not established here.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
Z=(g.Q(),g.Q())


def J(p):return (-p[1],p[0])
def dot(p,q):return p[0]*q[0]+p[1]*q[1]
def encode(q):return [str(q.a),str(q.b)]


def ledger(points):
    pairs={e:g.distance(points[e[0]],points[e[1]])
           for e in combinations(range(len(points)),2)}
    maximum=max(pairs.values(),key=lambda q:float(q.a)+float(q.b)*3**.5)
    assert all((maximum-q).sign()>=0 for q in pairs.values())
    contacts={e for e,q in pairs.items() if q==g.Q(1)}
    diameters={e for e,q in pairs.items() if q==maximum}
    failures={e for e,q in pairs.items() if (q-1).sign()<0}
    triangles=[t for t in combinations(range(len(points)),3)
               if all(tuple(e) in contacts for e in combinations(t,2))]
    return pairs,maximum,contacts,diameters,failures,triangles


def compatibility(points,edges,ntrains):
    adjacent={i:[] for i in range(len(points))}
    for i,j,t in edges:
        adjacent[i].append((j,t));adjacent[j].append((i,t))
    relations=set()
    for j,rows in adjacent.items():
        for (i,t),(k,s) in combinations(rows,2):
            if (g.distance(points[i],points[k])-3).sign()>=0:
                relations.add(tuple(sorted((t,s))))
    graph={i:set() for i in range(ntrains)}
    for t,s in relations:graph[t].add(s);graph[s].add(t)
    unseen=set(graph);components=[]
    while unseen:
        seed=next(iter(unseen));unseen.remove(seed);todo=[seed];found={seed}
        while todo:
            for k in graph[todo.pop()]:
                if k in unseen:unseen.remove(k);found.add(k);todo.append(k)
        components.append(sorted(found))
    return relations,components


def hexagon():
    sixth=(g.Q(F(1,2)),g.Q(0,F(1,2)))
    points=[];p=(g.Q(1),g.Q())
    for _ in range(6):points.append(p);p=g.mul(p,sixth)
    old,D,C,H,_,tri=ledger(points);assert D==g.Q(4) and len(C)==6 and len(H)==3 and not tri
    A=[[0]*6 for _ in range(6)]
    for i,j in C:
        A[i][i]+=2;A[j][j]+=2;A[i][j]-=2;A[j][i]-=2
    for i,j in H:
        A[i][i]-=1;A[j][j]-=1;A[i][j]+=1;A[j][i]+=1
    for i in range(6):
        assert sum(A[i])==0
        assert sum((points[j][0]*A[i][j] for j in range(6)),g.Q())==g.Q()
        assert sum((points[j][1]*A[i][j] for j in range(6)),g.Q())==g.Q()
        for j in range(6):assert sum(A[i][k]*A[k][j] for k in range(6))==6*A[i][j]
    assert sum(A[i][i] for i in range(6))==18
    edges=[(i,(i+1)%6,i) for i in range(6)]
    relations,components=compatibility(points,edges,6)
    assert len(components)==1
    states=[];closed=0;mean_strict=0;pair_checks=0
    for signs in product((-1,1),repeat=6):
        image=[Z];current=Z
        for i,s in enumerate(signs):
            current=g.add(current,g.scale(J(g.sub(points[(i+1)%6],points[i])),F(s)))
            if i<5:image.append(current)
        if current!=Z:continue
        closed+=1
        new,DD,CC,HH,low,triangles=ledger(image);pair_checks+=len(new)
        mean=sum((new[h] for h in H),g.Q())*F(1,3)
        assert all((D-new[h]).sign()>=0 for h in H)
        nonconstant=len(set(signs))>1
        if nonconstant:
            assert (D-mean).sign()>0 and any(q==g.Q() for q in new.values())
            assert any(signs[t]!=signs[s] for t,s in relations)
            mean_strict+=1
        else:
            assert not low and CC==C and len(HH)==3 and DD==D
        states.append({'signs':signs,'weighted_old_diameter_square':encode(mean),
                      'lower_failures':sorted(low),
                      'collisions':[e for e,q in new.items() if q==g.Q()],
                      'new_unit_triangles':triangles})
    assert closed==10 and mean_strict==8
    return {'source':'unit regular hexagon','sign_universe':64,'face_closed_states':closed,
            'nonconstant_strict_mean_states':mean_strict,'full_pair_checks':pair_checks,
            'Gamma_components':components,'stress_matrix':A,'states':states,
            'nonglobal_competitor':'center plus unit-radius regular pentagon, D^2=(5+sqrt(5))/2<4'}


def grid(m):
    u=(g.Q(1),g.Q());v=(g.Q(F(5,13)),g.Q(F(12,13)))
    labels=[(i,j) for i in range(m+1) for j in range(m+1)]
    idx={p:k for k,p in enumerate(labels)}
    points=[g.add(g.scale(u,F(i)),g.scale(v,F(j))) for i,j in labels]
    old,D,C,H,low,tri=ledger(points);assert not low and not tri and len(H)==1
    edges=[]
    for i,j in labels:
        if i<m:edges.append((idx[i,j],idx[i+1,j],i))
        if j<m:edges.append((idx[i,j],idx[i,j+1],m+j))
    assert {tuple(sorted((i,j))) for i,j,t in edges}==C
    relations,components=compatibility(points,edges,2*m)
    assert len(components)==2
    feasible=[];pair_checks=0
    for signs in product((-1,1),repeat=2*m):
        a=[0];b=[0]
        for k in range(m):a.append(a[-1]+signs[k]);b.append(b[-1]+signs[m+k])
        image=[J(g.add(g.scale(u,F(a[i])),g.scale(v,F(b[j])))) for i,j in labels]
        for i,j,t in edges:
            assert g.sub(image[j],image[i])==g.scale(J(g.sub(points[j],points[i])),F(signs[t]))
        new,DD,CC,HH,fail,tr=ledger(image);pair_checks+=len(new)
        if fail:continue
        assert not tr and CC==C and DD==D and len(HH)==len(H)==1
        assert all(signs[t]==signs[s] for t,s in relations)
        if signs[0]!=signs[m]:
            assert all((D-new[h]).sign()>0 for h in H)
            assert HH.isdisjoint(H) and all(old[h]!=D for h in HH)
        feasible.append({'signs':signs,'old_diameters':sorted(H),'new_diameters':sorted(HH),
            'old_diameter_shortened':all((D-new[h]).sign()>0 for h in H),
            'new_inactive_diameters':len(HH-H),'new_contacts':len(CC-C),
            'diameter_square':encode(DD),'triangle_count':len(tr)})
    assert len(feasible)==4
    return {'source':'unit rhombic grid','M':m,'labels':len(points),'trains':2*m,
       'sign_universe':2**(2*m),'full_pair_checks':pair_checks,
       'Gamma_components':components,'fully_lower_feasible_states':feasible}


def rectangular_face():
    labels=[(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,1)]
    points=[(g.Q(i),g.Q(j)) for i,j in labels]
    old,D,C,H,low,tri=ledger(points);assert not low and not tri
    edges=[(i,(i+1)%8,i) for i in range(8)]
    relations,components=compatibility(points,edges,8)
    assert len(components)==4
    eligible={i for i in range(8) if (old[tuple(sorted(((i-1)%8,(i+1)%8)))]-3).sign()<0}
    assert eligible=={0,2,4,6}
    closed=0;feasible=[];checks=0
    for signs in product((-1,1),repeat=8):
        image=[Z];current=Z
        for i,sign in enumerate(signs):
            current=g.add(current,g.scale(J(g.sub(points[(i+1)%8],points[i])),F(sign)))
            if i<7:image.append(current)
        if current!=Z:continue
        closed+=1
        new,DD,CC,HH,fail,tr=ledger(image);checks+=len(new)
        if fail or tr:continue
        transitions=[i for i in range(8) if signs[i]!=signs[(i-1)%8]]
        assert set(transitions)<=eligible
        if transitions:
            assert len(transitions)==4
            a,b,c,d=transitions
            assert g.add(points[a],points[c])==g.add(points[b],points[d])
        assert CC==C and DD==D and len(HH)==len(H)
        feasible.append({'signs':signs,'transition_vertices':transitions,
                         'new_contacts':len(CC-C),'new_diameter_pairs':len(HH-H)})
    assert closed==36 and len(feasible)==4
    return {'source':'rectangular eight-site unit face','sign_universe':256,
       'face_closed_states':closed,'full_pair_checks':checks,
       'eligible_high_turn_vertices':sorted(eligible),'Gamma_components':components,
       'fully_feasible_states':feasible}


if __name__=='__main__':
    print(json.dumps({'classification':'exact finite exhaustive sign regressions',
        'scope':'hexagon and listed rhombic grids; no canonical arbitrary-source sign existence',
        'cases':[hexagon(),rectangular_face()]+[grid(m) for m in (2,3,4)]},sort_keys=True))
