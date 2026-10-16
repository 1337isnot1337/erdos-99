#!/usr/bin/env python3
"""Exact finite certificates for the slot-07 rhombic two-site cell.

Uses Q(sqrt(15)) arithmetic, with no floating-point tolerances. The report
proves the universal angle threshold, source shield, and capacity theorem.
This script checks the finite fixtures, triangulation, ranks, sample endpoints,
and exact algebraic identities; it does not prove canonical extraction/globality.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json
from pathlib import Path

class Q:
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    @staticmethod
    def coerce(x): return x if isinstance(x, Q) else Q(x)
    def __add__(self, x):
        x=self.coerce(x); return Q(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,x): return self+-self.coerce(x)
    def __rsub__(self,x): return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x); return Q(self.a*x.a+15*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x); den=x.a*x.a-15*x.b*x.b
        assert den != 0
        return self*Q(x.a/den,-x.b/den)
    def __eq__(self,x):
        x=self.coerce(x); return self.a==x.a and self.b==x.b
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a>=0 and b>=0: return 1
        if a<=0 and b<=0: return -1
        cmp=(a*a>15*b*b)-(a*a<15*b*b)
        return cmp if a>0 else -cmp
    def __bool__(self): return self.a!=0 or self.b!=0
    def serial(self): return {'a':str(self.a),'b':str(self.b),'field':'sqrt(15)'}

def add(p,q): return (p[0]+q[0],p[1]+q[1])
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def norm2(p): return p[0]*p[0]+p[1]*p[1]
def dist2(p,q): return norm2(sub(p,q))
def rank(rows):
    a=[list(row) for row in rows]; r=0
    for col in range(len(a[0])):
        pivot=next((k for k in range(r,len(a)) if a[k][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][col]; a[r]=[v/z for v in a[r]]
        for k in range(len(a)):
            if k!=r and a[k][col]:
                z=a[k][col]; a[k]=[v-z*w for v,w in zip(a[k],a[r])]
        r+=1
        if r==len(a): break
    return r

axial=[(-1,0),(0,-1),(1,-1),(2,0),(1,1),(0,1),(0,0),(1,0)]
guards=axial[:6]
tris=[(0,1,6),(0,6,5),(1,2,6),(6,2,7),
      (6,7,5),(7,4,5),(7,2,3),(7,3,4)]
def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
assert all(orient(*(axial[k] for k in tri))==1 for tri in tris)
edges=Counter(tuple(sorted((tri[i],tri[(i+1)%3]))) for tri in tris for i in range(3))
boundary={tuple(sorted((i,(i+1)%6))) for i in range(6)}
assert {e for e,n in edges.items() if n==1}==boundary
assert all(n==1 if e in boundary else n==2 for e,n in edges.items())
for (a,b),(c,d) in combinations(edges,2):
    if len({a,b,c,d})<4: continue
    p,q,r,s=(axial[k] for k in (a,b,c,d))
    assert not (orient(p,q,r)*orient(p,q,s)<0 and orient(r,s,p)*orient(r,s,q)<0)
assert sum(axial[i][0]*axial[(i+1)%6][1]-axial[(i+1)%6][0]*axial[i][1] for i in range(6))==8

# Polynomial identity in c, coefficients in increasing degree order.
def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
left=[2,F(0),-2]
prod=pmul([F(5,4),1],[1,1])
left=[F(x)-y for x,y in zip(left,prod)]
right=[F(3,4)*z for z in pmul([1,-4],[1,1])]
assert left==right
# The all-angle capacity proof uses s^2-h*k=3/4 and
# s^2-k/2-1/4=(1/2-c)*(1+c), with h=1/2-c, k=1/2+c.
prod=pmul([F(1,2),-1],[F(1,2),1])
assert [x-y for x,y in zip([F(1),F(0),F(-1)],prod)] == [F(3,4),F(0),F(0)]
assert pmul([F(1,2),-1],[1,1]) == [F(1,2),F(-1,2),F(-1)]

fixtures=[('square',Q(0),Q(1)),
          ('wide_13_85',Q(F(13,85)),Q(F(84,85))),
          ('wide_11_61',Q(F(11,61)),Q(F(60,61))),
          ('wide_9_41',Q(F(9,41)),Q(F(40,41))),
          ('critical',Q(F(1,4)),Q(0,F(1,4))),
          ('blocked_7_25',Q(F(7,25)),Q(F(24,25))),
          ('blocked_5_13',Q(F(5,13)),Q(F(12,13))),
          ('blocked_8_17',Q(F(8,17)),Q(F(15,17)))]
results=[]; pair_checks=0; path_checks=0
for name,c,s in fixtures:
    assert c*c+s*s==1 and c.sign()>=0 and (Q(F(1,2))-c).sign()>0
    pts=[(Q(a)+b*c,b*s) for a,b in axial]
    contacts=[]; diameters=[]
    for i,j in combinations(range(8),2):
        d2=dist2(pts[i],pts[j]); pair_checks+=1
        assert (d2-1).sign()>=0 and (9-d2).sign()>=0
        if d2==1: contacts.append((i,j))
        if d2==9: diameters.append((i,j))
    assert len(contacts)==9 and diameters==[(0,3)]
    assert {j if i==6 else i for i,j in contacts if 6 in (i,j)}=={0,1,5,7}
    assert {j if i==7 else i for i,j in contacts if 7 in (i,j)}=={2,3,4,6}
    assert not any(6 in edge or 7 in edge for edge in diameters)
    cset=set(contacts)
    assert not any(all(tuple(sorted(e)) in cset for e in combinations(t,2)) for t in combinations(range(8),3))
    rows=[]
    for i,j in contacts+diameters:
        row=[Q(0)]*16; dx,dy=sub(pts[i],pts[j])
        row[2*i],row[2*i+1],row[2*j],row[2*j+1]=dx,dy,-dx,-dy
        rows.append(row)
    assert rank(rows)==9 < 13
    r0sq=(1+c)/2
    assert (1-r0sq).sign()>0
    assert (r0sq-Q(1)/(2+2*c)).sign()>=0
    h,k=Q(F(1,2))-c,Q(F(1,2))+c
    assert s*s-h*k==Q(F(3,4))
    assert s*s-k/2-Q(F(1,4))==h*(1+c)
    assert h.sign()>0 and (1-k).sign()>0
    delta=(1-2*c)/100
    strict=(delta*s,-delta*c)
    assert all((dist2(strict,g)-1).sign()>0 for g in pts[:6])
    wide=(Q(F(1,4))-c).sign()>=0
    record={'fixture':name,'c':c.serial(),'s':s.serial(),
            'source_pairs':28,'contacts':9,'diameter_squared':'9',
            'unit_triangles':0,'mixed_rank':9,'required_canonical_rank':13,
            'interior_contact_degrees':[4,4],'interior_diameter_endpoints':False,
            'cover_radius_squared':r0sq.serial(),'hop':wide,
            'strict_capacity_one_site':True,'capacity_identities':True}
    if wide:
        threshold=(1-c*c)/(Q(F(5,4))+c)
        assert threshold-r0sq == 3*(1-4*c)*(1+c)/(10+8*c)
        assert (threshold-r0sq).sign()>=0
        assert (5-4*c-4).sign()>=0
        samples=[(Q(0),Q(0)),(c,s-1),(2*c,Q(0)),(Q(F(1,2)),Q(0)),
                 (1-2*c,Q(0)),(1-c,1-s),(Q(1),Q(0))]
        for p in samples:
            for g in pts[:6]:
                assert (dist2(p,g)-1).sign()>=0
                assert (9-dist2(p,g)).sign()>=0
                path_checks+=1
            b=p[1]/s; a=p[0]-c*b
            assert (b+1).sign()>=0 and (1-b).sign()>=0
            assert (a+b+1).sign()>=0 and (2-a-b).sign()>=0
            assert (a-b+1).sign()>=0 and (2-a+b).sign()>=0
        record['path_sample_guard_checks']=len(samples)*6
    else:
        assert (Q(F(5,4))-c-1).sign()<0
        record['bisector_guard_upper_squared']=(Q(F(5,4))-c).serial()
    results.append(record)

# The only possible nonendpoint equality in the diameter-disk estimate at c=1/4
# is blocked by the opposite guard at squared distance 1/4.
v=(Q(F(1,4)),Q(0,F(1,4)))
exc=(Q(F(5,8)),Q(0,F(-1,8)))
assert norm2(exc)==Q(F(5,8))
assert dist2(exc,(Q(F(1,2)),Q(0)))==Q(F(1,4))
assert dist2(exc,sub((Q(1),Q(0)),v))==Q(F(1,4))

square=[(i,j) for i in range(3) for j in range(3) if (i,j)!=(2,2)]
assert len(square)==8
assert min((x-x2)**2+(y-y2)**2 for (x,y),(x2,y2) in combinations(square,2))==1
assert max((x-x2)**2+(y-y2)**2 for (x,y),(x2,y2) in combinations(square,2))==8 < 9

# A whole guarded one-row strip: all its interiors may be replaced together.
# The universal capacity proof is analytic; these certify strict k-1 packets.
strip_results=[]; strip_source_checks=0; strip_endpoint_checks=0; strip_strict_checks=0
for name,c,s in fixtures:
    for k in (2,3,5,9):
        wax=[(-1,0)]+[(j,-1) for j in range(k)]+[(k,0)]+[(j,1) for j in reversed(range(k))]
        iax=[(j,0) for j in range(k)]
        wall=[(Q(a)+b*c,b*s) for a,b in wax]
        old=wall+[(Q(j),Q(0)) for j in range(k)]
        contact_count=0
        for i,j in combinations(range(len(old)),2):
            d2=dist2(old[i],old[j]); strip_source_checks+=1
            assert (d2-1).sign()>=0 and ((k+1)**2-d2).sign()>=0
            contact_count+=(d2==1)
        assert contact_count==5*k-1
        delta=(1-2*c)/100
        eps=F(1,128)
        for attempt in range(96):
            packet=[(Q(j)+delta*s,-delta*c+(-1)**j*eps) for j in range(k-1)]
            safe=True
            for p in packet:
                b=p[1]/s; a=p[0]-c*b
                safe &= all(z.sign()>0 for z in (b+1,1-b,a+b+1,k-a-b,a-b+1,k-a+b))
                safe &= all((dist2(p,g)-1).sign()>0 for g in wall)
            if safe: break
            eps/=2
        else: raise AssertionError('strict strip packet did not certify')
        assert all((dist2(p,q)-1).sign()>0 for p,q in combinations(packet,2))
        new=wall+packet
        assert len(new)==len(old)-1
        for i,j in combinations(range(len(new)),2):
            d2=dist2(new[i],new[j]); strip_endpoint_checks+=1
            assert (d2-1).sign()>=0 and ((k+1)**2-d2).sign()>=0
            if i>=len(wall) or j>=len(wall):
                assert (d2-1).sign()>0; strip_strict_checks+=1
        assert dist2(new[0],new[k+1])==(k+1)**2
        grid_width=isqrt(len(old)-1)+1
        grid=[(i%grid_width,i//grid_width) for i in range(len(old))]
        grid_d2=max((x-x2)**2+(y-y2)**2 for (x,y),(x2,y2) in combinations(grid,2))
        assert grid_d2<(k+1)**2
        strip_results.append({'fixture':name,'k':k,'old_population':len(old),
                              'endpoint_population':len(new),'old_contacts':contact_count,
                              'diameter_squared':(k+1)**2,'epsilon':str(eps),
                              'strict_packet_sites':len(packet),'grid_competitor_diameter_squared':grid_d2})

# Weighted co-circular cap identity; the continuous proof is in the strip report.
cap_identity_checks=0; cap_clear_checks=0
for name,c,s in fixtures:
    a=(Q(-1),Q(0)); v=(c,s); mv=(-c,-s)
    N=24
    for L in range(N+1):
        lam=F(L,N)
        for T in range(-(N-L),N-L+1):
            t=F(T,N); mu=(1-lam+t)/2; nu=(1-lam-t)/2
            p=(Q(-lam)+t*c,t*s)
            assert lam*dist2(p,a)+mu*dist2(p,v)+nu*dist2(p,mv)==1-norm2(p)
            cap_identity_checks+=1
            if (dist2(p,v)-1).sign()>=0 and (dist2(p,mv)-1).sign()>=0:
                cap_clear_checks+=1
                defect=norm2(p)+p[0]
                assert defect.sign()<=0
                assert defect.sign()<0 or p==a or p==(Q(0),Q(0))
cert={'arithmetic':'Q(sqrt(15)); no floating point','fixtures':results,
      'source_pair_checks':pair_checks,'path_sample_guard_checks':path_checks,
      'triangulation_triangles':8,'triangulation_area_coefficient':4,
      'capacity_polynomial_identities':True,'critical_extra_equality_excluded':True,
      'nonglobal_square_competitor_diameter_squared':8,
      'strip_source_pair_checks':strip_source_checks,
      'strip_endpoint_pair_checks':strip_endpoint_checks,
      'strip_strict_inserted_pair_checks':strip_strict_checks,
      'strip_fixtures':strip_results,
      'cap_weighted_identity_checks':cap_identity_checks,
      'cap_clear_disk_checks':cap_clear_checks,
      'limits':'Finite fixtures and identities only. Universal path, shield, capacity and threshold proofs are analytic in the report. No canonical patch extraction, refill, or global optimality.'}
out=Path(__file__).with_name('target_c_rhombic_vacancy_hop_slot07_certificate_2026_10_10.json')
out.write_text(json.dumps(cert,indent=2)+'\n')
print(f'PASS: {pair_checks} source pairs; {path_checks} exact sample guard/upper checks; 8 triangulation triangles; critical equality and capacity identity; {len(fixtures)} ranks.')
print(f'PASS: {strip_source_checks} strip source pairs; {strip_endpoint_checks} endpoint pairs; {strip_strict_checks} strict inserted pairs; {len(strip_results)} exact one-vacancy packets.')
print(f'PASS: {cap_identity_checks} weighted cap identities; {cap_clear_checks} exact clear-cap disk samples.')
