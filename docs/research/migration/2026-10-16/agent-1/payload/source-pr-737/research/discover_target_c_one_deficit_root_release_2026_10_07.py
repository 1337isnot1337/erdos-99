#!/usr/bin/env python3
"""Exploratory final one-deficit release search; requires NumPy/SciPy.

Root guard comparisons use exact Q(sqrt3) arithmetic. LP margins use
floating arithmetic and are NOT certificates. The recorded margins are
within solver tolerance and no positive velocity was reconstructed.
"""
import sys,json
import numpy as np
from fractions import Fraction as F
from itertools import combinations
from scipy.optimize import linprog
sys.path.insert(0,'research')
import verify_target_c_sorted_rate_packets_2026_10_06 as s
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g

def value(x):return float(x.a)+float(x.b)*np.sqrt(3)
for m in (4,5,6,8):
 # Use a less tiny rational angle for conditioned discovery only.
 # geometry has a fixed rational t; construct the same formula at chosen t.
 actual,_=s.geometry(m,list(range(m-1,-m,-2)),F(1,1000))
 hole=(1,m-2);del actual[hole]
 moving=sorted(p for p in actual if max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))<m)
 columns={p:i for i,p in enumerate(moving)}
 rows=[];pairs=[]
 for p,q in combinations(actual,2):
  if p not in columns and q not in columns:continue
  if g.distance(actual[p],actual[q])==g.Q(1):
   delta=g.sub(actual[p],actual[q]);v=np.array([value(x) for x in delta]);row=np.zeros(2*len(moving))
   if p in columns:row[2*columns[p]:2*columns[p]+2]+=v
   if q in columns:row[2*columns[q]:2*columns[q]+2]-=v
   rows.append(row);pairs.append((p,q))
 objective=np.r_[np.zeros(2*len(moving)),-1]
 res=linprog(objective,A_ub=np.c_[-np.array(rows),np.ones(len(rows))],b_ub=np.zeros(len(rows)),bounds=[(-1,1)]*(2*len(moving))+[(None,None)],method='highs')
 answer={'classification':'floating opening search; no strict-release proof', 'solver_acceptance_threshold':1e-8, 'M':m,'hole':hole,'success':bool(res.success),'first_margin':None if not res.success else float(res.x[-1])}
 wall=(1,m-1);t=F(1,1000);rotation=((1-t*t)/(1+t*t),2*t/(1+t*t));sine=rotation[1]
 a0=g.Q(F(0),F(1,2));w=(g.Q(F(-1,2)),a0);r=g.mul(g.power(rotation,m-2),w);normal=(-r[1],r[0])
 root=g.add(actual[wall],g.scale(normal,3*sine))
 failures=[p for p in actual if p!=wall and (g.distance(root,actual[p])-1).sign()<=0]
 answer['root_failures']=failures
 if res.success and res.x[-1]>1e-8:
  coeff=[[str(F(float(v)).limit_denominator(10**8)) for v in row] for row in res.x[:-1].reshape(len(moving),2)]
  velocity={p:tuple(g.Q(F(v)) for v in row) for p,row in zip(moving,coeff)}
  margins=[]
  for p,q in pairs:
   delta=g.sub(actual[p],actual[q]);d=g.sub(velocity.get(p,(g.Q(),g.Q())),velocity.get(q,(g.Q(),g.Q())))
   margin=delta[0]*d[0]+delta[1]*d[1];assert margin.sign()>0;margins.append(value(margin))
  answer['exact_margin_minimum']=min(margins)
  out={'M':m,'half_angle_tangent':'1/1000','hole':hole,'deleted_wall_vertex':wall,'moving':moving,'velocities':coeff,'classification':'exact positive first margins; finite amplitude still required'}
  json.dump(out,open('/tmp/e99-root-velocity-M'+str(m)+'.json','w'))
 print(json.dumps(answer),flush=True)
