#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

V=tuple(range(7))
TRI=tuple(combinations(V,3)); TI={t:i for i,t in enumerate(TRI)}
EDGE=tuple(combinations(V,2)); EI={e:i for i,e in enumerate(EDGE)}
SUP=tuple(combinations(V,4)); SI={s:i for i,s in enumerate(SUP)}

H=[]
for a,b,c in TRI:
    r=[0]*len(EDGE)
    r[EI[(a,b)]]=1; r[EI[(a,c)]]=-1; r[EI[(b,c)]]=1
    H.append(tuple(r))
H=tuple(H)

STM=[]
for F in SUP:
    m=0
    for t in combinations(F,3): m|=1<<TI[t]
    STM.append(m)
STM=tuple(STM)

PM=[]
for p in permutations(V):
    PM.append(tuple(SI[tuple(sorted(p[x] for x in F))] for F in SUP))
PM=tuple(PM)
assert len(PM)==5040

def rank(rows):
    A=[[Fraction(x) for x in H[i]] for i in rows]
    q=0
    for c in range(len(EDGE)):
        z=next((i for i in range(q,len(A)) if A[i][c]),None)
        if z is None: continue
        A[q],A[z]=A[z],A[q]
        d=A[q][c]
        A[q]=[x/d for x in A[q]]
        for i in range(q+1,len(A)):
            d=A[i][c]
            if d: A[i]=[A[i][j]-d*A[q][j] for j in range(len(EDGE))]
        q+=1
        if q==len(A): break
    return q

def tmask(mask):
    out=0
    while mask:
        b=mask&-mask; mask-=b; out|=STM[b.bit_length()-1]
    return out

def nullity(tm):
    rows=tuple(i for i in range(len(TRI)) if tm>>i&1)
    return len(rows)-rank(rows)

def canon(mask):
    ids=tuple(i for i in range(len(SUP)) if mask>>i&1)
    best=None
    for pm in PM:
        z=0
        for i in ids: z|=1<<pm[i]
        if best is None or z<best: best=z
    return best

def name(mask):
    return tuple(tuple(x+1 for x in SUP[i]) for i in range(len(SUP)) if mask>>i&1)

expected={
1:(1,{1:1}),2:(3,{2:3}),3:(10,{3:10}),4:(38,{4:35,5:3}),
5:(108,{4:1,5:107}),6:(2,{5:2}),7:(0,{}),8:(0,{})
}
reps={0}; levels={}
for k in range(1,9):
    nxt={}
    for mask in reps:
        for i in range(len(SUP)):
            if mask>>i&1: continue
            z=canon(mask|(1<<i))
            if z in nxt: continue
            nu=nullity(tmask(z))
            if nu<=5: nxt[z]=nu
    reps=set(nxt); levels[k]=nxt
    dist=dict(sorted(Counter(nxt.values()).items()))
    assert (len(nxt),dist)==expected[k]

six=tuple(sorted(name(m) for m in levels[6]))
assert six==(
((1,2,3,4),(1,2,3,5),(1,2,3,6),(1,2,4,5),(1,3,4,5),(2,3,4,5)),
((1,2,3,4),(1,2,3,5),(1,2,4,5),(1,2,6,7),(1,3,4,5),(2,3,4,5)),
)
assert not levels[7] and not levels[8]
print("PASS: h=5 support-nullity compression")
for k in range(3,9):
    print(k,len(levels[k]),dict(sorted(Counter(levels[k].values()).items())))
print("m6",six)
