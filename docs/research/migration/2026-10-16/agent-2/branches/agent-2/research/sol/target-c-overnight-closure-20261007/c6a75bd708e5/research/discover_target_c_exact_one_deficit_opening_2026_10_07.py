#!/usr/bin/env python3
"""Exact finite opening/dual discovery in Q(sqrt(3)).

Usage: script.py M rational_t [output_prefix]. A positive result certifies
only opening derivatives; finite amplitude, root clearance and all-source
exchange must be checked separately. An exact dual rules out strict
opening only at the specific auxiliary packet and parameter.
"""
import sys,json,time
from itertools import combinations
sys.path.insert(0,'research')
from fractions import Fraction as F
import verify_target_c_sorted_rate_packets_2026_10_06 as s
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g
Q=g.Q;zero=Q()
def div(a,b):
 den=b.a*b.a-3*b.b*b.b
 assert den
 return Q((a.a*b.a-3*a.b*b.b)/den,(a.b*b.a-a.a*b.b)/den)
def solve(A,b):
 A=[list(row)+[bb] for row,bb in zip(A,b)];n=len(A)
 for k in range(n):
  p=next(i for i in range(k,n) if A[i][k]!=zero);A[k],A[p]=A[p],A[k];row=A[k];pivot=row[k]
  for j in range(k,n+1):row[j]=div(row[j],pivot)
  for i in range(k+1,n):
   factor=A[i][k]
   if factor==zero:continue
   A[i][k]=zero
   for j in range(k+1,n+1):
    if row[j]!=zero:A[i][j]=A[i][j]-factor*row[j]
 x=[zero]*n
 for k in range(n-1,-1,-1):x[k]=A[k][n]-sum((A[k][j]*x[j] for j in range(k+1,n) if A[k][j]!=zero),zero)
 return x
m=int(sys.argv[1]);t=F(sys.argv[2]);prefix=sys.argv[3] if len(sys.argv)>3 else '/tmp/e99-one-deficit-exact-M'+str(m);assert m>=3 and t>0;actual,_=s.geometry(m,list(range(m-1,-m,-2)),t);hole=(1,m-2);del actual[hole];moving=sorted(p for p in actual if max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))<m);data={'M':m,'moving':moving,'pairs':[(p,q) for p,q in combinations(actual,2) if (p in moving or q in moving) and g.distance(actual[p],actual[q])==Q(1)]};col={p:i for i,p in enumerate(moving)};n=2*len(moving)+1;A=[];b=[]
for pp,qq in data['pairs']:
 p,q=tuple(pp),tuple(qq);row=[zero]*n;v=g.sub(actual[p],actual[q])
 if p in col:row[2*col[p]]=-v[0];row[2*col[p]+1]=-v[1]
 if q in col:row[2*col[q]]=row[2*col[q]]+v[0];row[2*col[q]+1]=row[2*col[q]+1]+v[1]
 row[-1]=Q(1);A.append(row);b.append(zero)
edges=len(A)
for i in range(n-1):
 for sign in (1,-1):
  row=[zero]*n;row[i]=Q(sign);A.append(row);b.append(Q(1))
zv=[Q(-1)]*(n-1)+[zero];eta=[-sum((q*v for q,v in zip(row,zv) if q!=zero),zero) for row in A[:edges]];k=0
for i in range(1,edges):
 if (eta[i]-eta[k]).sign()<0:k=i
x=zv[:-1]+[eta[k]];basis=[edges+2*i+1 for i in range(n-1)]+[k];c=[zero]*(n-1)+[Q(1)];start=time.monotonic()
sparse=[[(i,q) for i,q in enumerate(row) if q!=zero] for row in A]
dot=lambda row,x:sum((q*x[i] for i,q in row),zero)
visited=set();bland=False
for it in range(3000):
 key=tuple(sorted(basis))
 if key in visited:bland=True
 visited.add(key)
 if x[-1].sign()>0:
  assert all((b[k]-dot(sparse[k],x)).sign()>=0 for k in range(len(A)))
  outbasis=[];outrhs=[]
  for k in basis:
   if k<edges:outbasis.append(['edge',k]);outrhs.append(0)
   else:outbasis.append(['bound',(k-edges)//2]);outrhs.append(1 if (k-edges)%2==0 else -1)
  out=dict(data,basis=outbasis,rhs=outrhs)
  json.dump(out,open(prefix+'-basis.json','w'))
  json.dump({'M':m,'half_angle_tangent':str(t),'moving':moving,'velocities':[[[str(q.a),str(q.b)] for q in x[2*i:2*i+2]] for i in range(len(moving))]},open(prefix+'-velocity.json','w'))
  print(json.dumps({'status':'exact positive opening','M':m,'t':str(t),'iterations':it,'seconds':time.monotonic()-start}),flush=True);break
 B=[A[k] for k in basis];BT=[list(row) for row in zip(*B)];lam=solve(BT,c);negative=[i for i,q in enumerate(lam) if q.sign()<0]
 if not negative:
  assert x[-1]==zero
  assert all((b[k]-dot(sparse[k],x)).sign()>=0 for k in range(len(A)))
  weights=[zero]*edges
  for index,k in enumerate(basis):
   if k<edges:weights[k]=lam[index]
   else:assert lam[index]==zero
  assert sum(weights,zero)==Q(1)
  assert all(q.sign()>=0 for q in weights)
  assert all(sum((weights[k]*A[k][j] for k in range(edges)),zero)==zero for j in range(n-1))
  json.dump({'M':m,'half_angle_tangent':str(t),'pairs':data['pairs'],'weights':[[str(q.a),str(q.b)] for q in weights],'classification':'exact finite nonnegative pinned equilibrium'},open(prefix+'-dual.json','w'))
  print(json.dumps({'status':'exact nonpositive optimum','M':m,'iterations':it,'eta_sign':x[-1].sign()}),flush=True);break
 j=min(negative,key=lambda i:basis[i])
 if not bland:
  for i in negative:
   if (lam[i]-lam[j]).sign()<0:j=i
 rhs=[zero]*n;rhs[j]=Q(-1);direction=solve(B,rhs);best=None;ratio=None
 for k in range(len(A)):
  if k in basis:continue
  speed=dot(sparse[k],direction)
  if speed.sign()<=0:continue
  slack=b[k]-dot(sparse[k],x);assert slack.sign()>=0
  r=div(slack,speed)
  if best is None or (r-ratio).sign()<0 or (r==ratio and k<best):best,ratio=k,r
 assert best is not None
 x=[xx+ratio*d for xx,d in zip(x,direction)];basis[j]=best
 if it%20==0:print(json.dumps({'M':m,'iteration':it,'eta_sign':x[-1].sign(),'seconds':time.monotonic()-start}),flush=True)

else:
 print(json.dumps({"status":"iteration limit; no opening or impossibility conclusion", "M":m,"iterations":3000}),flush=True)
