#!/usr/bin/env python3
"""Exact rational interval certificate for 35 collapsed support-six rotation-cell orbits.

The JSON data contains only exact decimal-rational angle centers, the two frozen
edge indices, and the exact combinatorial cell. A floating-point Gauss-Jordan
step proposes an approximate inverse C; every proof decision is then repeated
with Fraction interval arithmetic. Floating point therefore cannot create a
false pass: a bad proposed C merely fails the exact contraction inequalities.
"""
from fractions import Fraction as Q
from math import factorial, sin, cos
from pathlib import Path
import json, sys
DATA_PATH=(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('target_c_support6_collapsed_closure35_data_2026_09_19.json'))
DATA=json.load(open(DATA_PATH))
R=Q(1,10**8); SIG=(1,1,1,-1,-1,-1)
BAD={0,2,15,18,19,22,26}; GOOD=set(range(42))-BAD
assert len(DATA)==35 and {d['idx'] for d in DATA}==GOOD

def Iadd(a,b): return (a[0]+b[0],a[1]+b[1])
def Isub(a,b): return (a[0]-b[1],a[1]-b[0])
def Imul(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def Iabsup(a): return max(abs(a[0]),abs(a[1]))
def Ipoint(x): return (x,x)
def atan_inv_interval(n,terms):
    x=Q(1,n); s=Q(0)
    for k in range(terms): s += (-1 if k&1 else 1)*x**(2*k+1)/(2*k+1)
    nxt=(-1 if terms&1 else 1)*x**(2*terms+1)/(2*terms+1)
    return (min(s,s+nxt),max(s,s+nxt))
a5=atan_inv_interval(5,45); a239=atan_inv_interval(239,14)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0] > Q(333,106) and PI[1] < Q(355,113)
def sincos_interval(x,n=42):
    s=Q(0); c=Q(0)
    for k in range(n+1):
        s += (-1 if k&1 else 1)*x**(2*k+1)/factorial(2*k+1)
        c += (-1 if k&1 else 1)*x**(2*k)/factorial(2*k)
    rs=abs(x)**(2*n+2)/factorial(2*n+2); rc=abs(x)**(2*n+1)/factorial(2*n+1)
    return (s-rs,s+rs),(c-rc,c+rc)
def edges_for(tag):
    missing=({(0,3),(1,4),(2,5)} if tag=='X' else {(0,1),(2,3),(4,5)})
    E=[(a,b) for a in range(6) for b in range(a+1,6) if (a,b) not in missing]
    assert len(E)==12; return E

def float_inverse(A):
    n=len(A); M=[list(map(float,A[i]))+[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(M[r][c])); assert abs(M[p][c])>1e-12
        M[c],M[p]=M[p],M[c]; q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q: M[r]=[a-q*b for a,b in zip(M[r],M[c])]
    return [row[n:] for row in M]

def propose_C(th,E,bits,var):
    J=[[0.0]*10 for _ in range(10)]; col={e:j for j,e in enumerate(var)}
    tf=[float(t) for t in th]
    for ei,(a,b) in enumerate(E):
        if ei not in col: continue
        j=col[ei]; tail=b if ((bits>>ei)&1) else a; head=a+b-tail
        for v,sg in ((tail,1.0),(head,-1.0)):
            if v<5:
                J[2*v][j]+=sg*(-sin(tf[ei])); J[2*v+1][j]+=sg*cos(tf[ei])
    inv=float_inverse(J)
    return tuple(tuple(Q(format(x,'.16g')) for x in row) for row in inv)

def certify(d):
    idx=d['idx']; tag=d['tag']; bits=d['bits']; order=d['order']; E=edges_for(tag)
    th=tuple(Q(s) for s in d['theta']); fixed=set(d['fixed']); var=tuple(e for e in range(12) if e not in fixed)
    assert len(fixed)==2 and len(var)==10
    C=propose_C(th,E,bits,var); SC=[sincos_interval(x) for x in th]
    F=[]
    for v in range(5):
        fx=Ipoint(Q(SIG[v])); fy=Ipoint(Q(0))
        for ei,(a,b) in enumerate(E):
            tail=b if ((bits>>ei)&1) else a; head=a+b-tail
            if v==tail: sg=Q(1)
            elif v==head: sg=Q(-1)
            else: continue
            si,co=SC[ei]; fx=Iadd(fx,Imul(sg,co)); fy=Iadd(fy,Imul(sg,si))
        F.extend((fx,fy))
    J=[[(Q(0),Q(0)) for _ in range(10)] for __ in range(10)]; col={e:j for j,e in enumerate(var)}
    for ei,(a,b) in enumerate(E):
        if ei not in col: continue
        j=col[ei]; si,co=SC[ei]; tail=b if ((bits>>ei)&1) else a; head=a+b-tail
        for v,sg0 in ((tail,1),(head,-1)):
            if v<5: J[2*v][j]=Imul(Q(-sg0),si); J[2*v+1][j]=Imul(Q(sg0),co)
    CF=[]
    for row in C:
        z=(Q(0),Q(0))
        for c,a in zip(row,F): z=Iadd(z,Imul(c,a))
        CF.append(z)
    Y=max(Iabsup(z) for z in CF)
    ZMAT=[]
    for i in range(10):
        rr=[]
        for j in range(10):
            z=Ipoint(Q(1 if i==j else 0))
            for k in range(10): z=Isub(z,Imul(C[i][k],J[k][j]))
            rr.append(z)
        ZMAT.append(rr)
    Z0=max(sum(Iabsup(a) for a in row) for row in ZMAT); CN=max(sum(abs(c) for c in row) for row in C); Z=Z0+4*CN*R
    assert Z<1 and Y+Z*R<R,(idx,float(Y),float(Z))
    TH=[(t-R,t+R) if e in col else (t,t) for e,t in enumerate(th)]
    mg=ml=mh=None
    for v in range(6):
        a1,a2,b1,b2=order[v]
        g=[TH[a1],Isub(TH[a2],TH[a1]),Iadd(PI,Isub(TH[b1],TH[a2])),Isub(TH[b2],TH[b1]),Isub(PI,TH[b2])]
        for q in g:
            assert q[0]>0 and 3*q[1]<2*PI[0],(idx,v,q)
            qg=min(q[0],2*PI[0]/3-q[1]); mg=qg if mg is None else min(mg,qg)
        for k in range(5):
            q=Iadd(g[k],g[(k+1)%5]); assert 3*q[0]>2*PI[1] and q[1]<PI[0],(idx,v,k,q)
            a=q[0]-2*PI[1]/3; b=PI[0]-q[1]; ml=a if ml is None else min(ml,a); mh=b if mh is None else min(mh,b)
    return Y,Z,mg,ml,mh
S=[(d['idx'],)+certify(d) for d in DATA]
print('certified orbits:',len(S)); print('indices:',' '.join(str(s[0]) for s in S))
print('max Y = %.3e'%max(float(s[1]) for s in S));print('max Z = %.3e'%max(float(s[2]) for s in S))
print('min strict one-turn margin(rad) = %.6g'%min(float(s[3]) for s in S));print('min strict adjacent-lower margin(rad) = %.6g'%min(float(s[4]) for s in S));print('min strict adjacent-upper margin(rad) = %.6g'%min(float(s[5]) for s in S))
print('PASS: exact contraction certificates place a regular collapsed closure root inside 35 of the 42 rotation-cell symmetry orbits.')
