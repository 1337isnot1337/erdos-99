#!/usr/bin/env python3
"""Exact pinned one-vacancy regression at arbitrarily small train variation.

Reruns companion finite arithmetic fixtures. Tests exact sources, all moving
unit-edge weights, equilibrium, anchored projections, and finite gap formulas.
Does not test a canonical global source or obstruct a moving-wall replacement.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10 import Q, fixtures, dist2, rank

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def minimum(xs):
    z=None
    for x in xs:
        if z is None or (x-z).sign()<0: z=x
    assert z is not None
    return z
def maximum(xs): return -minimum(-x for x in xs)
angles=[fixtures[0],fixtures[1],('obtuse_13_85',-fixtures[1][1],fixtures[1][2]),
        fixtures[4],('obtuse_critical',-fixtures[4][1],fixtures[4][2]),
        fixtures[7],('obtuse_8_17',-fixtures[7][1],fixtures[7][2]),fixtures[6]]
counts={x:0 for x in ('source_pairs','weighted_moving_edges','moving_equilibria',
                     'anchored_chain_rows','full_rank_small_fixtures','smaller_competitor_pairs')}
records=[]
for name,c,s in angles:
 for t in (F(1,1000),F(1,10000)):
  a=Q((1-t*t)/(1+t*t)); b=Q(2*t/(1+t*t))
  ua=(a,b); va=(a*c+b*s,a*s-b*c); u=(Q(1),Q(0)); v=(c,s)
  alpha=b/s; gamma=(a*s-b*c)/s
  assert alpha.sign()>0 and gamma.sign()>0
  assert va==(alpha+gamma*c,gamma*s)
  assert ua==(gamma+alpha*c,alpha*s)
  assert (dot(ua,va)+F(1,2)).sign()>0 and (F(1,2)-dot(ua,va)).sign()>0
  for m,n in ((3,3),(4,5),(8,6)):
    axes=[(i,j) for j in range(n+1) for i in range(m+1)]
    def point(i,j):
      U=(Q(0),Q(0)) if i==0 else (a+i-1,b)
      V=(Q(0),Q(0)) if j==0 else (va[0]+(j-1)*c,va[1]+(j-1)*s)
      return (U[0]+V[0],U[1]+V[1])
    old=[point(i,j) for i,j in axes]; index={z:k for k,z in enumerate(axes)}
    hole=index[(1,1)]
    moving={index[(i,j)] for i in range(1,m) for j in range(1,n)}-{hole}
    I=len(moving); ordered=sorted(moving); col={k:i for i,k in enumerate(ordered)}
    source_contacts=[]; weights={}
    distances=[]
    for x,y in combinations(range(len(old)),2):
      d=dist2(old[x],old[y]); assert (d-1).sign()>=0
      distances.append(d); counts['source_pairs']+=1
      expected=abs(axes[x][0]-axes[y][0])+abs(axes[x][1]-axes[y][1])==1
      assert (d==1)==expected
      if d==1: source_contacts.append((x,y))
    for j in range(1,n):
      for i in range(m):
        e=(index[(i,j)],index[(i+1,j)])
        if hole in e: continue
        weights[e]=alpha*(i-1) if j==1 else Q(1) if i==0 else gamma
    for i in range(1,m):
      for j in range(n):
        e=(index[(i,j)],index[(i,j+1)])
        if hole in e: continue
        weights[e]=alpha*(j-1) if i==1 else Q(1) if j==0 else gamma
    assert set(weights)=={e for e in source_contacts if hole not in e and any(k in moving for k in e)}
    force={k:[Q(0),Q(0)] for k in moving}; rows=[]
    for (x,y),w in weights.items():
      assert w.sign()>0; counts['weighted_moving_edges']+=1
      r=sub(old[x],old[y]); row=[Q(0)]*(2*I)
      for k,sgn in ((x,1),(y,-1)):
        if k in moving:
          for dim in (0,1):
            force[k][dim]+=sgn*w*r[dim]
            row[2*col[k]+dim]=sgn*r[dim]
      rows.append(row)
    assert all(f==[Q(0),Q(0)] for f in force.values())
    counts['moving_equilibria']+=I
    W=sum(weights.values(),Q(0)); lmin=minimum(weights.values())
    assert lmin==minimum((Q(1),alpha,gamma))
    expected_W=alpha*F((m-2)*(m-1)+(n-2)*(n-1),2)+(m+n-4)+gamma*((n-2)*(m-1)+(m-2)*(n-1))
    assert W==expected_W
    rho=s*lmin/(2*I*(m+n)*W); assert rho.sign()>0
    for k in moving:
      i,j=axes[k]
      for r in range(i,m):
        e=(index[(r,j)],index[(r+1,j)])
        assert e in weights and sub(old[e[1]],old[e[0]])==u
        counts['anchored_chain_rows']+=1
      for r in range(j,n):
        e=(index[(i,r)],index[(i,r+1)])
        assert e in weights and sub(old[e[1]],old[e[0]])==v
        counts['anchored_chain_rows']+=1
    if (m,n)==(3,3):
      assert len(rows)==8 and rank(rows)==2*I==6
      counts['full_rank_small_fixtures']+=1
    D2=maximum(distances)
    competitor=[(Q(i),Q(j)) for j in range(n+1) for i in range(m+1)]
    assert (D2-(m*m+n*n)).sign()>0
    for x,y in combinations(range(len(competitor)),2):
      d=dist2(competitor[x],competitor[y])
      assert (d-1).sign()>=0 and (m*m+n*n-d).sign()>=0
      counts['smaller_competitor_pairs']+=1
    records.append({'angle':name,'m':m,'n':n,'rational_rotation_parameter':str(t),
                    'cos_epsilon':a.serial(),'sin_epsilon':b.serial(),
                    'moving_labels':I,'moving_rows':len(rows),'alpha':alpha.serial(),
                    'gamma':gamma.serial(),'total_weight':W.serial(),
                    'minimum_weight':lmin.serial(),'finite_isolation_radius':rho.serial(),
                    'old_diameter_squared':D2.serial(),'competitor_diameter_squared':m*m+n*n})
out=Path(__file__).with_name('target_c_near_coherent_one_vacancy_pinning_slot07_certificate_2026_10_10.json')
out.write_text(json.dumps({'arithmetic':'exact rational and Q(sqrt(15))',
                          'counts':counts,'fixtures':records,
                          'limits':'Pinned unit-edge equilibrium, anchored rank, and finite sources only. Not full-source normalized KKT stresses or canonical minimizers; moving walls and disconnected endpoints are not excluded.'},indent=2)+'\n')
print('PASS: near-coherent pinning '+json.dumps(counts)+'; '+str(len(records))+' fixtures.')
