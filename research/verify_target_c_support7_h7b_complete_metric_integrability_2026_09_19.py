#!/usr/bin/env python3
"""Exact graph certificate for complete K7 sine-law metric integrability in H7b."""
from fractions import Fraction as Q
import itertools

V=tuple(range(1,8))
EDGES=tuple(itertools.combinations(V,2))
EI={e:k for k,e in enumerate(EDGES)}

def edge(a,b): return (a,b) if a<b else (b,a)

def canon_cycle(seq):
    seq=tuple(seq)
    return min(o[k:]+o[:k] for o in (seq,tuple(reversed(seq))) for k in range(len(seq)))

def missing_cycles():
    out=set()
    for p in itertools.permutations(V):
        c=canon_cycle(p)
        if p==c:
            out.add(frozenset(edge(c[i],c[(i+1)%7]) for i in range(7)))
    return sorted(out,key=lambda x:tuple(sorted(x)))

def spanning_tree(edges):
    parent={v:v for v in V}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    T=[]
    for a,b in sorted(edges):
        ra,rb=find(a),find(b)
        if ra!=rb:
            parent[ra]=rb;T.append((a,b))
        if len(T)==6:break
    assert len(T)==6
    return tuple(T)

def tree_path(T,a,b):
    adj={v:[] for v in V}
    for u,v in T:adj[u].append(v);adj[v].append(u)
    stack=[(a,None,())]
    while stack:
        v,par,path=stack.pop()
        if v==b:return path
        for w in adj[v]:
            if w!=par:stack.append((w,v,path+((v,w),)))
    raise AssertionError

def cycle_row(T,e):
    # Oriented cycle a->b followed by the tree path b->a.
    a,b=e; row=[Q(0)]*len(EDGES)
    def add_arc(u,v,c=Q(1)):
        ee=edge(u,v); row[EI[ee]] += c if (u,v)==ee else -c
    add_arc(a,b)
    for u,v in tree_path(T,b,a):add_arc(u,v)
    return row

def rank(rows):
    A=[r[:] for r in rows];m=len(A);n=len(A[0]) if m else 0;rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr];q=A[rr][c];A[rr]=[x/q for x in A[rr]]
        for i in range(m):
            if i==rr or not A[i][c]:continue
            q=A[i][c];A[i]=[x-q*y for x,y in zip(A[i],A[rr])]
        rr+=1
        if rr==m:break
    return rr

MC=missing_cycles()
assert len(MC)==360
for M in MC:
    P=tuple(e for e in EDGES if e not in M)
    assert len(P)==14
    T=spanning_tree(P)
    rel=[cycle_row(T,e) for e in P if e not in T]
    miss=[cycle_row(T,e) for e in sorted(M)]
    assert len(rel)==8 and len(miss)==7
    assert rank(rel)==8
    assert rank(rel+miss)==15
    # Each added cycle has its own missing-edge pivot; relation cycles use no missing edge.
    for k,e in enumerate(sorted(M)):
        assert all(r[EI[e]]==0 for r in rel)
        assert miss[k][EI[e]] in (Q(1),Q(-1))
        for q,f in enumerate(sorted(M)):
            if q!=k:assert miss[q][EI[e]]==0

# The 15 root-fan triangles 1-i-j form another full K7 cycle basis.
fan=[]
Tstar=tuple((1,i) for i in range(2,8))
for i,j in itertools.combinations(range(2,8),2):fan.append(cycle_row(Tstar,(i,j)))
assert len(fan)==15 and rank(fan)==15
print('PASS: complete K7 metric integrability has cycle rank 15')
print('Hamiltonian missing C7 cases checked:',len(MC))
print('relation graph cycle rank: 8')
print('additional independent missing-edge metric cycles: 7')
print('root-fan triangle basis size/rank: 15/15')
