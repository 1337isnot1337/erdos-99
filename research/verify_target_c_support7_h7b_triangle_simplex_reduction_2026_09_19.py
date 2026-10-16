#!/usr/bin/env python3
"""Exact Farkas certificates for the generic H7b triangle/simplex reduction.

The numerical optimizer used during discovery is not part of this certificate.
The verifier imports the exact generic H7b census, rebuilds all non-ground
reciprocal triangle-angle equations, and solves 106 hard-coded sparse dual
supports over fractions.Fraction. Every solved certificate is a strict
contradiction to the audited physical-pentagon simplex facets.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib, importlib.util, io

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_h7b_generic_order_sign_reduction_2026_09_19.py"
spec=importlib.util.spec_from_file_location("h7b_base",BASE); base=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(base)
HULL=base.HULL; edge=base.edge; VIDX={(i,k):(i-1)*5+k for i in HULL for k in range(5)}; NVAR=35

def add_rows(a,b,scale=Fraction(1)): return [x+scale*y for x,y in zip(a,b)]
def force_cycle(i,slots,missing,signs):
    raw=base.local_raw(i,slots[i-1],missing); pos=tuple(r for r in raw if signs[edge(i,r)]>0); neg=tuple(r for r in raw if signs[edge(i,r)]<0)
    assert {len(pos),len(neg)}=={2,3}; return pos+neg

def force_arc(cycle,i,a,b):
    row=[Fraction(0) for _ in range(NVAR)]; k=cycle.index(a); stop=cycle.index(b)
    while k!=stop: row[VIDX[(i,k)]]+=1; k=(k+1)%5
    return row

def raw_chi(i,a,b,slots,missing):
    raw=base.local_raw(i,slots[i-1],missing); return 1 if raw.index(b)>raw.index(a) else -1

def raw_angle_affine(i,a,b,slots,missing,signs,cycles):
    arc=force_arc(cycles[i],i,a,b); same=signs[edge(i,a)]==signs[edge(i,b)]; chi=raw_chi(i,a,b,slots,missing)
    if same and chi>0:return arc,Fraction(0)
    if same and chi<0:return [-z for z in arc],Fraction(2)
    if (not same) and chi>0:return arc,Fraction(-1)
    return [-z for z in arc],Fraction(1)

def triangle_affine(a,b,c,slots,missing,signs,cycles):
    assert all(edge(*e) not in missing for e in ((a,b),(a,c),(b,c)))
    row=[Fraction(0) for _ in range(NVAR)]; constant=Fraction(0)
    for i,j,k in ((a,b,c),(b,a,c),(c,a,b)):
        rr,cc=raw_angle_affine(i,j,k,slots,missing,signs,cycles); row=add_rows(row,rr); constant+=cc
    return row,Fraction(1)-constant

def exact_system(state):
    typ,missing,slots,signs=state; cycles={i:force_cycle(i,slots,missing,signs) for i in HULL}; rows=[]; rhs=[]; labels=[]
    for i in HULL:
        row=[Fraction(0) for _ in range(NVAR)]
        for k in range(5): row[VIDX[(i,k)]]=1
        rows.append(row); rhs.append(Fraction(2)); labels.append(("F",i))
    for a,b,c in combinations(HULL,3):
        if any(edge(*e) in missing for e in ((a,b),(a,c),(b,c))): continue
        row,value=triangle_affine(a,b,c,slots,missing,signs,cycles); rows.append(row); rhs.append(value); labels.append(("T",a,b,c))
    qrows=[]
    for i in HULL:
        for k in range(5):
            row=[Fraction(0) for _ in range(NVAR)]; row[VIDX[(i,k)]]+=1; row[VIDX[(i,(k+1)%5)]]+=1; row[VIDX[(i,(k+3)%5)]]-=1; qrows.append(row)
    return rows,rhs,labels,qrows

def solve_unique(columns,rhs):
    m=len(columns[0]); n=len(columns); assert len(rhs)==m
    A=[[Fraction(columns[j][i]) for j in range(n)]+[Fraction(rhs[i])] for i in range(m)]; piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[x-q*y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    for row in A:
        if all(row[c]==0 for c in range(n)) and row[-1]!=0: raise AssertionError("inconsistent support system")
    assert len(piv)==n
    sol=[Fraction(0) for _ in range(n)]
    for i,c in enumerate(piv): sol[c]=A[i][-1]
    for i in range(m): assert sum(Fraction(columns[j][i])*sol[j] for j in range(n))==Fraction(rhs[i])
    return sol

CERT_SUPPORTS={}
def put(ids,fac,eq):
    for i in ids:CERT_SUPPORTS[i]=(fac,eq)
put((0,6),(1,3,4,15,17,18,31,33),(('F',4),('T',1,4,7)))
put((1,2,9,10,12,13,14,20,25),(6,9,15,16,18,31,33,34),(('F',4),('T',2,4,7)))
put((3,4,5,7,8,11,17,22,27,31),(11,13,16,18,31,32,33,34),(('F',4),('F',7),('T',3,4,7)))
put((15,16,18,19,21),(1,3,5,7,8,11,13,16,33),(('F',2),('F',7),('T',1,4,7),('T',2,4,7),('T',3,4,7)))
put((23,24,26,28,29,30),(1,3,7,8,11,13,16,21,23,24,26,27,29,33),(('F',2),('F',5),('F',7),('T',1,4,7),('T',2,4,7),('T',2,5,6),('T',3,4,7)))
put((58,59),(1,2,6,7,8,9,12,13,15,16,17,18,21,22,27,28,31,32,33,34),(('F',1),('F',2),('F',3),('F',4),('F',5),('F',6),('F',7),('T',1,4,5),('T',1,6,7),('T',2,4,5),('T',2,6,7),('T',3,4,5),('T',3,6,7)))
put((64,65,66,72,76,79),(6,9,11,14,16,17,19,31,33,34),(('F',3),('F',4),('T',2,3,7),('T',3,4,7)))
put((67,68,78,81,82),(1,3,4,16,18,19,31,33),(('F',4),('T',1,4,7)))
put((69,70,71,73,74,75,77,80),(6,9,11,14,16,17,19,31,33,34),(('F',4),('T',2,3,7),('T',3,4,7)))
put(tuple(range(83,96)),(1,3,16,17,18,19,31,33),(('F',4),('T',1,4,7)))
put((96,101,102,103,104),(0,1,2,3,11,13,16,18,21,23),(('F',1),('F',3),('F',4),('T',1,3,5),('T',3,4,5)))
put((97,105,108),(1,2,11,13,16,18,21,23,25,27,28,31,33),(('F',1),('F',4),('F',5),('F',6),('T',1,3,5),('T',1,6,7),('T',3,4,5)))
put((98,106,107,109,110,111,115,116),(0,1,2,3,11,13,16,18,21,23),(('F',1),('F',4),('F',5),('T',1,3,5),('T',3,4,5)))
put((118,119,121),(1,2,3,6,7,9,11,12,13,16,18,19,21,22,24,27,28,30,31,33),(('F',1),('F',2),('F',4),('F',5),('F',7),('T',1,3,5),('T',1,3,6),('T',1,6,7),('T',2,4,5),('T',2,4,7),('T',2,6,7),('T',3,4,5)))
put((120,122),(1,3,11,12,13,14,26,28,31,33),(('F',1),('F',3),('T',1,3,6),('T',1,6,7)))
put((124,125,126),(1,2,3,6,7,8,9,11,12,13,16,18,19,21,22,27,28,30,31,33),(('F',1),('F',2),('F',4),('F',5),('F',7),('T',1,3,5),('T',1,3,6),('T',1,6,7),('T',2,4,5),('T',2,4,7),('T',2,6,7),('T',3,4,5)))
put((127,),(1,2,3,7,8,11,12,13,16,17,18,21,22,27,28,31,32,33),(('F',1),('F',2),('F',4),('F',5),('F',7),('T',1,3,5),('T',1,3,6),('T',1,6,7),('T',2,4,5),('T',2,4,7),('T',2,6,7),('T',3,4,5)))
put((161,),(6,8,16,18,19,30,31,33),(('F',4),('T',2,4,7)))
put((162,),(6,8,9,20,21,23,31,33),(('F',5),('T',2,5,7)))
put((163,),(1,3,4,6,8,9,11,13,14,15,16,18,20,21,23,25,26,28,30,31,33,34),(('F',3),('F',4),('F',5),('T',1,3,5),('T',1,3,6),('T',1,4,6),('T',2,4,6),('T',2,4,7),('T',2,5,7),('T',3,5,7)))
put((164,),(1,3,4,6,8,9,11,13,15,16,18,20,21,23,26,28,29,30,31,33),(('F',3),('F',4),('F',5),('T',1,3,5),('T',1,4,6),('T',2,4,6),('T',2,4,7),('T',2,5,7)))
put((165,166),(1,3,4,6,8,11,13,15,16,18,21,23,24,26,28,30,31,33),(('F',3),('F',4),('T',1,3,5),('T',1,4,6),('T',2,4,7)))
put((167,),(5,6,8,16,18,26,28,29),(('F',4),('T',2,4,6)))
put((176,),(1,2,3,6,7,8,11,12,13,16,17,18,21,22,23,26,27,28,31,32,33),(('F',1),('F',2),('F',4),('F',6),('F',7),('T',1,2,3),('T',1,2,7),('T',1,6,7),('T',2,3,4),('T',3,4,5),('T',4,5,6),('T',5,6,7)))
put((177,178),(1,2,3,6,7,8,11,12,13,16,17,18,21,22,23,26,27,28,31,32,33),(('F',1),('F',2),('F',3),('F',6),('F',7),('T',1,2,3),('T',1,2,7),('T',1,6,7),('T',2,3,4),('T',3,4,5),('T',4,5,6),('T',5,6,7)))
put((179,180,181,182,183),(1,2,3,6,7,8,11,12,13,16,17,18,21,22,23,26,27,28,31,32,33),(('F',1),('F',2),('F',6),('F',7),('T',1,2,3),('T',1,2,7),('T',1,6,7),('T',2,3,4),('T',3,4,5),('T',4,5,6),('T',5,6,7)))

def rep(i):return base.ORBIT_MEMBERS[base.ORBIT_KEYS[i]][0]
kappa_counts=Counter(); excluded_by_type=Counter()
for oi,(fac,elabs) in CERT_SUPPORTS.items():
    state=rep(oi); typ=state[0]; rows,rhs,labels,qrows=exact_system(state); li={x:i for i,x in enumerate(labels)}; es=tuple(li[x] for x in elabs)
    cols=[qrows[j]+[Fraction(1)] for j in fac]+[rows[r]+[Fraction(0)] for r in es]; target=[Fraction(0) for _ in range(NVAR)]+[Fraction(1)]
    sol=solve_unique(cols,target); na=len(fac); alpha=sol[:na]; mu=sol[na:]; assert all(a>0 for a in alpha) and sum(alpha)==1
    kappa=-Fraction(1,3)-sum(mu[t]*rhs[r] for t,r in enumerate(es)); assert kappa<=0; kappa_counts[kappa]+=1; excluded_by_type[typ]+=1
assert len(CERT_SUPPORTS)==106 and excluded_by_type==Counter({"C7":72,"C3+C4":34})
assert kappa_counts[Fraction(0)]==54 and sum(v for k,v in kappa_counts.items() if k<0)==52
expected=Counter({Fraction(-1,30):35,Fraction(-1,66):7,Fraction(-1,102):3,Fraction(-1,24):2,Fraction(-1,120):2,Fraction(-7,156):1,Fraction(-5,114):1,Fraction(-1,57):1})
assert Counter({k:v for k,v in kappa_counts.items() if k<0})==expected
angle=set(CERT_SUPPORTS); survivors=set(range(184))-angle; assert Counter(rep(i)[0] for i in survivors)==Counter({"C7":48,"C3+C4":30})
trace=set(base.TRACE_ORBIT_INDICES); assert len(trace)==8 and len(trace&angle)==7 and trace-angle=={160}
union=angle|trace; assert len(union)==107; survivors=set(range(184))-union; assert Counter(rep(i)[0] for i in survivors)==Counter({"C7":47,"C3+C4":30})
print("PASS: 106/184 generic H7b orbits have exact triangle/simplex Farkas contradictions; 78 survive that layer (48 C7 + 30 C3+C4).")
print("PASS: union with the 8 signed-trace exclusions removes 107/184; 77 remain (47 C7 + 30 C3+C4), i.e. 176 -> 77 from the prior trace-reduced state.")