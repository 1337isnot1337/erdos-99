#!/usr/bin/env python3
"""Exact three-no-root rank-density barrier for the Target-C four-cycle system.

This extends the companion two-no-root verifier by treating every family with
exactly three four-cycles that avoid ground root 0.  With M, T, Q and
delta(A)=r_M(A)-r_Q(A) as in the relative normal-form audit, it proves

    3 * delta(A) <= |A|

for every such family.  Together with the already-certified t<=2 cases, every
hypothetical sufficient 44-cycle family must contain at least four no-root
cycles.

The 187,460 unordered no-root triples are reduced to 77 S_7 orbits.  Only
local states with quotient-kernel dimension k=2,p<=2 or k=3,p<=5 can violate
the density inequality.  The verifier enumerates all 1,006,703 such states.
For each state it constructs an integer matrix for the T-images of a basis of
Q-relations.  Rank is computed modulo the Mersenne prime P=2^127-1.  A
Lucas-Lehmer check certifies P prime, every relation row has squared Euclidean
norm at most 1215, and P^2 > 1215^15.  Hadamard's determinant bound therefore
certifies that every modular rank is exactly the rational rank.

Use --orbit-start/--orbit-end to shard the 77 orbit representatives.
"""

from fractions import Fraction
from itertools import combinations, permutations
from collections import Counter
import argparse

VERTICES=tuple(range(8))
SEGMENTS=tuple(combinations(VERTICES,2)); SEGMENT_INDEX={e:i for i,e in enumerate(SEGMENTS)}
LINE_EDGES=[]; LINE_EDGE_INDEX={}
for i,j in combinations(range(len(SEGMENTS)),2):
    if set(SEGMENTS[i]) & set(SEGMENTS[j]):
        LINE_EDGE_INDEX[(i,j)]=len(LINE_EDGES); LINE_EDGES.append((i,j))
assert len(SEGMENTS)==28 and len(LINE_EDGES)==168

def seg(a,b): return SEGMENT_INDEX[tuple(sorted((a,b)))]
def line_cycle(ids):
    row=[0]*len(LINE_EDGES); ids=list(ids)
    for x,y in zip(ids,ids[1:]+ids[:1]):
        if x<y: row[LINE_EDGE_INDEX[(x,y)]] += 1
        else: row[LINE_EDGE_INDEX[(y,x)]] -= 1
    return row

def k8_cycle(vs):
    vs=list(vs); return line_cycle([seg(vs[i],vs[(i+1)%len(vs)]) for i in range(len(vs))])
def side_triangle(a,b,c): return line_cycle([seg(a,b),seg(b,c),seg(a,c)])
def star_triangle(r,a,b,c): return line_cycle([seg(r,a),seg(r,b),seg(r,c)])

SIDE=[side_triangle(*t) for t in combinations(VERTICES,3)]
GROUND=[star_triangle(0,1,i,j) for i,j in combinations(range(2,8),2)]
FOUR=[]; DESC=[]; seen=set()
for vertex_set in combinations(VERTICES,4):
    a=min(vertex_set); rest=[x for x in vertex_set if x!=a]
    for perm in permutations(rest):
        if perm[0]>=perm[-1]: continue
        d=(a,)+perm; row=k8_cycle(d); key=min(tuple(row),tuple(-x for x in row))
        if key in seen: continue
        seen.add(key); FOUR.append(row); DESC.append(d)
assert len(SIDE)==56 and len(GROUND)==15 and len(FOUR)==210

class RationalBasis:
    def __init__(self,rows=()):
        self.rows={}
        for row in rows: self.add(row)
    def reduce(self,row):
        r=[Fraction(x) for x in row]
        for p in sorted(self.rows):
            if r[p]:
                q=r[p]; b=self.rows[p]; r=[x-q*y for x,y in zip(r,b)]
        return r
    def add(self,row):
        r=self.reduce(row); p=next((i for i,x in enumerate(r) if x),None)
        if p is None:return False
        q=r[p]; self.rows[p]=[x/q for x in r]; return True
    @property
    def rank(self): return len(self.rows)

class RationalCoordinateBasis:
    def __init__(self,vectors):
        self.rows={}; self.dimension=len(vectors)
        for idx,row in enumerate(vectors):
            r=list(row); coeff=[Fraction(0)]*self.dimension; coeff[idx]=1
            for p in sorted(self.rows):
                if r[p]:
                    q=r[p]; b,bc=self.rows[p]
                    r=[x-q*y for x,y in zip(r,b)]; coeff=[x-q*y for x,y in zip(coeff,bc)]
            p=next(i for i,x in enumerate(r) if x); q=r[p]
            r=[x/q for x in r]; coeff=[x/q for x in coeff]; self.rows[p]=(r,coeff)
    def coordinates(self,row):
        r=list(row); coeff=[Fraction(0)]*self.dimension
        for p in sorted(self.rows):
            if r[p]:
                q=r[p]; b,bc=self.rows[p]
                r=[x-q*y for x,y in zip(r,b)]; coeff=[x+q*y for x,y in zip(coeff,bc)]
        assert not any(r); return coeff

def exact_rank(rows):
    basis={}
    for row in rows:
        r=[Fraction(x) for x in row]
        for p in sorted(basis):
            if r[p]:
                q=r[p]; b=basis[p]; r=[x-q*y for x,y in zip(r,b)]
        p=next((i for i,x in enumerate(r) if x),None)
        if p is None: continue
        q=r[p]; basis[p]=[x/q for x in r]
    return len(basis)

side=RationalBasis(SIDE)
M_res=[side.reduce(r) for r in FOUR]; T_res=[side.reduce(r) for r in GROUND]
assert RationalBasis(T_res).rank==15
BLOCK_LABELS=list(combinations(range(1,8),3)); BLOCKS=[]
for face in BLOCK_LABELS:
    ids=tuple(i for i,d in enumerate(DESC) if set(d)=={0,*face}); assert len(ids)==3; BLOCKS.append(ids)
SECTION_IDS=[e for block in BLOCKS for e in block[:2]]
coord_basis=RationalCoordinateBasis([M_res[e] for e in SECTION_IDS]+T_res)
COORD=[coord_basis.coordinates(r) for r in M_res]
assert all(x.denominator==1 for c in COORD for x in c)
QCOORD=[tuple(int(x) for x in c[:70]) for c in COORD]; MCOORD=[tuple(int(x) for x in c) for c in COORD]
assert exact_rank(MCOORD)==85 and exact_rank(QCOORD)==70
LOCAL=((1,0),(0,1),(1,-1))
for b,ids in enumerate(BLOCKS):
    for j,e in enumerate(ids):
        support=[(QCOORD[e][2*h],QCOORD[e][2*h+1]) for h in range(35)]
        assert support[b]==LOCAL[j] and all(v==(0,0) for h,v in enumerate(support) if h!=b)
NO_ROOT=[i for i,d in enumerate(DESC) if 0 not in d]; assert len(NO_ROOT)==105
BLOCK_INDEX={face:i for i,face in enumerate(BLOCK_LABELS)}
QCOMP={}
for e in NO_ROOT:
    comp=tuple((QCOORD[e][2*b],QCOORD[e][2*b+1]) for b in range(35))
    touched={b for b,v in enumerate(comp) if v!=(0,0)}
    exp={BLOCK_INDEX[tuple(face)] for face in combinations(sorted(set(DESC[e])),3)}
    assert touched==exp and len(touched)==4; QCOMP[e]=comp

# states (mask,cost,complete,span kind,line,p)
STATES=[]
for mask in range(8):
    chosen=[j for j in range(3) if (mask>>j)&1]; cost=len(chosen); complete=mask==7
    if cost==0: kind,line,p=0,None,0
    elif cost==1: kind,line,p=1,LOCAL[chosen[0]],1
    else: kind,line,p=2,None,0 if complete else 2
    STATES.append((mask,cost,complete,kind,line,p))

def int_plane(plane):
    from math import gcd, lcm
    ds=[x.denominator for x in plane]; L=1
    for d in ds: L=lcm(L,d)
    a=[int(x*L) for x in plane]
    g=0
    for x in a:g=gcd(g,abs(x))
    a=[x//g for x in a]
    for x in a:
        if x:
            if x<0:a=[-y for y in a]
            break
    return tuple(a)

def alpha_basis_int(k,plane=None):
    if k==3:return [(1,0,0),(0,1,0),(0,0,1)]
    a,b,c=int_plane(plane)
    if a:return [(-b,a,0),(-c,0,a)]
    if b:return [(1,0,0),(0,-c,b)]
    return [(1,0,0),(0,1,0)]

def solve_local_coeffs_int(mask,w):
    wx,wy=w; chosen=[j for j in range(3) if (mask>>j)&1]
    if not chosen:
        assert wx==0 and wy==0; return [0,0,0]
    if len(chosen)==1:
        j=chosen[0]; ux,uy=LOCAL[j]
        q=wx//ux if ux else wy//uy
        assert q*ux==wx and q*uy==wy
        out=[0,0,0];out[j]=q;return out
    j,h=chosen[:2]; ax,ay=LOCAL[j]; bx,by=LOCAL[h]; det=ax*by-ay*bx
    q=(wx*by-wy*bx)//det; r=(ax*wy-ay*wx)//det
    assert q*ax+r*bx==wx and q*ay+r*by==wy
    out=[0,0,0];out[j]=q;out[h]=r;return out

def relation_rows_int(ext,touched,states,k,plane=None):
    rows=[]
    for b,s in zip(touched,states):
        if STATES[s][2]:
            ids=BLOCKS[b];rows.append([MCOORD[ids[0]][70+j]-MCOORD[ids[1]][70+j]-MCOORD[ids[2]][70+j] for j in range(15)])
    for alpha in alpha_basis_int(k,plane):
        tv=[sum(alpha[i]*MCOORD[e][70+j] for i,e in enumerate(ext)) for j in range(15)]
        for b,s in zip(touched,states):
            vx=sum(alpha[i]*QCOMP[e][b][0] for i,e in enumerate(ext)); vy=sum(alpha[i]*QCOMP[e][b][1] for i,e in enumerate(ext))
            beta=solve_local_coeffs_int(STATES[s][0],(-vx,-vy));ids=BLOCKS[b]
            for j0,q in enumerate(beta):
                if q:
                    for jj in range(15):tv[jj]+=q*MCOORD[ids[j0]][70+jj]
        rows.append(tv)
    return rows

P=(1<<127)-1

def rank_mod(rows,p=P):
    a=[[x%p for x in row] for row in rows]; r=0; n=len(a)
    for c in range(15):
        piv=next((i for i in range(r,n) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]; pv=a[r][c]
        for i in range(r+1,n):
            q=a[i][c]
            if q:
                a[i]=[(pv*x-q*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def relation_defect(ext,touched,states,k,plane=None):
    rows=relation_rows_int(ext,touched,states,k,plane)
    for row in rows:
        assert sum(x*x for x in row) <= 1215
    delta=rank_mod(rows)
    # Reduction mod P cannot increase rational rank.  Conversely every
    # (delta+1)-minor is 0 mod P.  Hadamard gives |det|^2 <= 1215^15 < P^2,
    # so such an integer determinant has |det| < P and must be exactly zero.
    # Hence the modular and rational ranks are equal.
    assert P*P > 1215**15
    n=3+sum(STATES[s][1] for s in states)
    return n-3*delta,delta,len(rows)

def cycle_key(desc):
    d=list(desc); return tuple(sorted(tuple(sorted((d[i],d[(i+1)%4]))) for i in range(4)))
KEY_TO_ID={cycle_key(DESC[e]):e for e in NO_ROOT}; KEY={e:cycle_key(DESC[e]) for e in NO_ROOT}
PERMS=list(permutations(range(1,8)))
def map_key(key,pmap): return tuple(sorted(tuple(sorted((pmap[a],pmap[b]))) for a,b in key))
def orbit_of_tuple(items):
    out=set(); keys=[KEY[e] for e in items]
    for perm in PERMS:
        pmap={i+1:perm[i] for i in range(7)}
        out.add(tuple(sorted(KEY_TO_ID[map_key(k,pmap)] for k in keys)))
    return out

remaining=set(combinations(NO_ROOT,3)); orbits=[]
while remaining:
    rep=min(remaining); orb=orbit_of_tuple(rep); assert orb<=remaining
    orbits.append((rep,orb)); remaining-=orb
print('orbits',len(orbits), 'sum',sum(len(o) for _,o in orbits), flush=True)
assert len(orbits)==77

# local kernel type for a block/state. Return ('all',None), ('plane', normalized normal), or ('line',basis signature).
def norm_vec(v):
    v=[Fraction(x) for x in v]
    # normalize first nonzero to 1
    for x in v:
        if x:
            return tuple(y/x for y in v)
    return tuple(v)

def local_kernel_type(ext,b,state_id):
    vals=[QCOMP[e][b] for e in ext]
    st=STATES[state_id]; kind=st[3]
    # residual map columns/coordinates on alpha in Q^3.
    # kind 2 => quotient 0 -> all kernel
    if kind==2:
        return ('all',None)
    if kind==0:
        # map alpha -> sum alpha_i (x_i,y_i), 2 x 3 matrix. rank 1 or 2 (touched ensures not 0)
        x=[v[0] for v in vals]; y=[v[1] for v in vals]
        r=exact_rank([x,y])
        if r==0:return ('all',None)
        if r==1:
            # kernel plane normal is nonzero row among x/y
            n=x if any(x) else y
            return ('plane',norm_vec(n))
        # kernel line, unacceptable for k>=2
        return ('line',None)
    # kind1 quotient Q2/line -> 1 dim, functional det(line, val)
    lx,ly=st[4]; n=[lx*v[1]-ly*v[0] for v in vals]
    if not any(n): return ('all',None)
    return ('plane',norm_vec(n))

# Enumerate potential negative states only using kernel compatibility.
# k=3: all local type all, p<=5. k=2: types all/same plane, at least one plane, p<=2.

def compatible_state_tuples(ext,touched,target_k,pmax):
    options=[]
    for b in touched:
        ob=[]
        for s in range(8):
            typ,val=local_kernel_type(ext,b,s)
            if typ=='line': continue
            ob.append((s,typ,val,STATES[s][5]))
        options.append(ob)
    cur=[]
    def rec(pos,p,plane,seen_plane):
        if p>pmax:return
        if pos==len(touched):
            if target_k==3:
                if not seen_plane: yield tuple(cur)
            else:
                if seen_plane: yield tuple(cur)
            return
        for s,typ,val,sp in options[pos]:
            if target_k==3:
                if typ!='all': continue
                cur.append(s); yield from rec(pos+1,p+sp,plane,seen_plane); cur.pop()
            else:
                if typ=='plane':
                    if plane is not None and val!=plane: continue
                    np=val if plane is None else plane
                    cur.append(s); yield from rec(pos+1,p+sp,np,True); cur.pop()
                else:
                    cur.append(s); yield from rec(pos+1,p+sp,plane,seen_plane); cur.pop()
    yield from rec(0,0,None,False)

parser=argparse.ArgumentParser()
parser.add_argument("--orbit-start",type=int,default=0)
parser.add_argument("--orbit-end",type=int,default=len(orbits))
args=parser.parse_args()
assert 0 <= args.orbit_start <= args.orbit_end <= len(orbits)

# Lucas-Lehmer certificate that P=2^127-1 is prime.
assert all(127 % d for d in range(2, 12))
sll=4
for _ in range(125):
    sll=(sll*sll-2)%P
assert sll==0

potential=0; min_def=None; neg=[]; recs=[]; total_k2=total_k3=0
for idx in range(args.orbit_start,args.orbit_end):
    rep,orb=orbits[idx]
    touched=sorted(b for b in range(35) if any(QCOMP[e][b]!=(0,0) for e in rep))
    counts={2:0,3:0}; mins={2:None,3:None}
    for k,pmax in [(2,2),(3,5)]:
        for states in compatible_state_tuples(rep,touched,k,pmax):
            p=sum(STATES[s][5] for s in states)
            crude=3+p-3*k
            if crude>=0:
                continue
            counts[k]+=1; potential+=1
            # Recover the common plane for k=2 from the first plane-type block.
            plane=None
            if k==2:
                for b,s0 in zip(touched,states):
                    typ,val=local_kernel_type(rep,b,s0)
                    if typ=='plane': plane=val; break
                assert plane is not None
            defect,delta,drel=relation_defect(rep,touched,states,k,plane)
            if min_def is None or defect<min_def:min_def=defect
            if mins[k] is None or defect<mins[k]:mins[k]=defect
            if defect<0: neg.append((idx,rep,k,p,defect,states,delta,drel))
    total_k2 += counts[2]; total_k3 += counts[3]
    recs.append((len(orb),len(touched),counts[2],counts[3],mins[2],mins[3]))
    print('orbit',idx+1,'/',args.orbit_end,'size',len(orb),'touch',len(touched),'k2',counts[2],'k3',counts[3],'mins',mins, flush=True)
print('potential',potential,'k2',total_k2,'k3',total_k3,'min_def',min_def,'neg',len(neg))
print('orbit_size_counts',Counter(len(o) for _,o in orbits))
print('touched_counts',Counter(r[1] for r in recs))
print('recs',recs)
if neg:
    print('NEG',neg[:5])
else:
    print('PASS t=3 density shard',args.orbit_start,args.orbit_end)
