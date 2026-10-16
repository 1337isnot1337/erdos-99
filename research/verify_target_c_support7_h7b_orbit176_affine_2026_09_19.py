#!/usr/bin/env python3
"""Exact affine certificate for generic H7b orbit 176 force-closure exclusion."""
from fractions import Fraction as Q
import itertools

N=range(1,8)
def edge(a,b): return tuple(sorted((a,b)))

# Exact one-based survivor 176 from the repaired 184-orbit generic H7b census.
M=frozenset({(1,3),(1,6),(2,4),(2,7),(3,5),(4,6),(5,7)})
KS=(3,3,3,3,3,3,3)
SIGNST=(
((0,1),-1),((0,2),-1),((0,3),-1),((0,4),-1),((0,5),-1),((0,6),-1),((0,7),-1),
((1,2),-1),((1,4),1),((1,5),1),((1,7),-1),
((2,3),-1),((2,5),1),((2,6),1),
((3,4),-1),((3,6),1),((3,7),1),
((4,5),-1),((4,7),1),((5,6),-1),((6,7),-1))
SD=dict(SIGNST)

def cyc_order(i): return [((i-1+k)%7)+1 for k in range(1,7)]
def gchi(i,k,j): return 1 if cyc_order(i).index(j)<k else -1
def present_order(i):
    b=cyc_order(i);k=KS[i-1];full=b[:k]+[0]+b[k:]
    return tuple(j for j in full if j==0 or edge(i,j) not in M)
def full_order(i):
    b=cyc_order(i);k=KS[i-1];return tuple(b[:k]+[0]+b[k:])

X={(i,k):5*(i-1)+k for i in N for k in range(5)}
R={(i,p):35+6*(i-1)+p for i in N for p in range(6)}
H={i:77+i-1 for i in N};NV=84

def rowadd(a,j,c):
    c=Q(c)
    if c:
        a[j]=a.get(j,Q(0))+c
        if not a[j]: del a[j]
def addrows(a,b,scale=Q(1)):
    z=dict(a)
    for j,c in b.items(): rowadd(z,j,scale*c)
    return z

def full_angle(i,a,b):
    o=full_order(i);pa=o.index(a);pb=o.index(b);lo,hi=sorted((pa,pb));r={}
    for p in range(lo,hi): rowadd(r,R[(i,p)],1)
    return r

def ground_ccw(a,b):
    r={};k=a
    while k!=b:
        rowadd(r,H[k],1);k=1 if k==7 else k+1
    return r

def ground_angle(a,b):
    arc=ground_ccw(a,b);chi=gchi(a,KS[a-1],b)
    return (arc,Q(0)) if chi>0 else ({j:-c for j,c in arc.items()},Q(2))

def force_cycle(i):
    raw=present_order(i);pos=tuple(j for j in raw if SD[edge(i,j)]>0);neg=tuple(j for j in raw if SD[edge(i,j)]<0)
    cyc=pos+neg;assert len(cyc)==5;return cyc

def force_arc(cyc,i,a,b):
    r={};ia=cyc.index(a);ib=cyc.index(b);k=ia
    while k!=ib:
        rowadd(r,X[(i,k)],1);k=(k+1)%5
    return r

def raw_force_angle(cyc,i,a,b,raw):
    arc=force_arc(cyc,i,a,b);same=SD[edge(i,a)]==SD[edge(i,b)];chi=1 if raw.index(b)>raw.index(a) else -1
    if same and chi>0:return arc,Q(0)
    if same and chi<0:return({j:-c for j,c in arc.items()},Q(2))
    if (not same) and chi>0:return arc,Q(-1)
    return({j:-c for j,c in arc.items()},Q(1))

def triangle_angle(v,a,b):
    if v==0:return ground_angle(a,b)
    return full_angle(v,a,b),Q(0)

def equalities():
    eq=[];cyc={i:force_cycle(i) for i in N}
    for i in N:eq.append(({X[(i,k)]:Q(1) for k in range(5)},Q(2)))
    eq.append(({H[i]:Q(1) for i in N},Q(2)))
    for i in N:
        po=present_order(i)
        for a,b in zip(po,po[1:]):
            vr=full_angle(i,a,b);vf,c=raw_force_angle(cyc[i],i,a,b,po)
            eq.append((addrows(vr,vf,Q(-1)),c))
    for a,b,c in itertools.combinations(range(8),3):
        rr={};cc=Q(0)
        for v,p,q in ((a,b,c),(b,a,c),(c,a,b)):
            vv,cv=triangle_angle(v,p,q);rr=addrows(rr,vv);cc+=cv
        eq.append((rr,Q(1)-cc))
    assert len(eq)==92
    return eq

def dense_hom(rr,d):
    row=[Q(0)]*(NV+1)
    for j,c in rr.items(): row[j]=Q(c)
    row[NV]=-Q(d)
    return row

def echelon(rows):
    basis={}
    for row in rows:
        r=row[:]
        for p in sorted(basis):
            if r[p]:
                q=r[p];br=basis[p];r=[x-q*y for x,y in zip(r,br)]
        p=next((j for j,x in enumerate(r) if x),None)
        if p is None:continue
        q=r[p];r=[x/q for x in r];basis[p]=r
    return basis

def in_span(basis,row):
    r=row[:]
    for p in sorted(basis):
        if r[p]:
            q=r[p];br=basis[p];r=[x-q*y for x,y in zip(r,br)]
    return not any(r)

EQ=equalities();B=echelon([dense_hom(r,d) for r,d in EQ]);assert len(B)==57

def vtx(i): return ((i-1)%7)+1

targets=[]
for i in N:
    rr={X[(vtx(i+3),1)]:Q(1),X[(vtx(i+4),4)]:Q(1),X[(i,0)]:Q(-1)}
    targets.append((rr,Q(1)))
targets.append(({X[(i,0)]:Q(1) for i in N},Q(1)))
for t in targets: assert in_span(B,dense_hom(*t))

print('PASS: orbit 176 exact affine force-gap consequences')
print('equality rank:',len(B))
print('certified cyclic cross-face relations: 7')
print('certified sum_i x[i,0] = 1')
