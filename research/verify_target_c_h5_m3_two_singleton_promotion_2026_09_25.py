#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations,permutations
from collections import Counter
V=range(7); T=list(combinations(V,3)); E=list(combinations(V,2)); F=list(combinations(V,4))
ti={x:i for i,x in enumerate(T)}; ei={x:i for i,x in enumerate(E)}; fi={x:i for i,x in enumerate(F)}
H=[]; FM=[]
for a,b,c in T:
 r=[0]*21; r[ei[a,b]]=1; r[ei[a,c]]=-1; r[ei[b,c]]=1; H.append(r)
for f in F:
 m=0
 for t in combinations(f,3): m|=1<<ti[t]
 FM.append(m)
PM=[tuple(fi[tuple(sorted(p[x] for x in f))] for f in F) for p in permutations(V)]
def rk(I):
 A=[[Fraction(x) for x in H[i]] for i in I]; q=0
 for c in range(21):
  z=next((i for i in range(q,len(A)) if A[i][c]),None)
  if z is None: continue
  A[q],A[z]=A[z],A[q]; d=A[q][c]; A[q]=[x/d for x in A[q]]
  for i in range(q+1,len(A)):
   d=A[i][c]
   if d: A[i]=[A[i][j]-d*A[q][j] for j in range(21)]
  q+=1
  if q==len(A): break
 return q
def can(M):
 I=[i for i in range(35) if M>>i&1]; best=None
 for p in PM:
  z=sum(1<<p[i] for i in I); best=z if best is None or z<best else best
 return best
R={0}
for _ in range(3): R={can(m|1<<i) for m in R for i in range(35) if not m>>i&1}
assert len(R)==10
C=Counter(); no=0
for M in R:
 I=[i for i in range(35) if M>>i&1]
 tm=FM[I[0]]|FM[I[1]]|FM[I[2]]; ts=[j for j in range(35) if tm>>j&1]
 for mult in set(permutations((3,3,2))):
  U={t:0 for t in ts}; pos=0
  for s,n in zip(I,mult):
   bm=((1<<n)-1)<<pos; pos+=n
   for t in combinations(F[s],3): U[ti[t]]|=bm
  found=0
  for S in combinations(ts,5):
   if rk([t for t in ts if t not in S])!=len(ts)-5: continue
   for B in combinations(S,3):
    u=[U[t] for t in B]
    if min(x.bit_count() for x in u)<3 or min((u[i]|u[j]).bit_count() for i,j in combinations(range(3),2))<4 or (u[0]|u[1]|u[2]).bit_count()<6: continue
    J=[t for t in ts if t not in B]; nu=len(J)-rk(J); assert nu<=1; C[nu]+=1; found=1
  if not found:no+=1
assert no==9 and C=={0:5121,1:1221}
print('PASS',no,C)
