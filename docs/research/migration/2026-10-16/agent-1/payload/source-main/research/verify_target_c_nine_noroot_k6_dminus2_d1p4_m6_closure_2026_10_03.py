#!/usr/bin/env python3
"""Exact closure of the m=6 slice in nine-no-root k=6,D=-2,d_root=1,p=4.

Inputs proved in the companion reduction chain force four touched singleton root
blocks, no touched empty/pair blocks, singleton touch multiplicity at least four,
touched-complete nullity at most one, coefficient rank three with generalized
weights (d1,d2,d3)>=(3,4,6), and required external relation-rank increment six.
The support-compression theorem reduces m=6 to the profile (3,2,1,1,1,1) on
the five facets of a five-set W plus one extra tetrahedron G, with |G cap W|
equal to 3 or 2. This verifier exhausts both canonical support types without
quotienting the 61+25 admissible support/root skeletons by their stabilizers.

All coefficient tests are exact over integers/rationals. Final relation ranks are
computed modulo 2^127-1, certified prime by Lucas-Lehmer; an explicit Hadamard
bound makes those modular ranks equal the rational ranks.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from collections import Counter
from math import gcd, lcm

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
        for row in rows:self.add(row)
    def reduce(self,row):
        r=[Fraction(x) for x in row]
        for p in sorted(self.rows):
            if r[p]:
                q=r[p];b=self.rows[p];r=[x-q*y for x,y in zip(r,b)]
        return r
    def add(self,row):
        r=self.reduce(row);p=next((i for i,x in enumerate(r) if x),None)
        if p is None:return False
        q=r[p];self.rows[p]=[x/q for x in r];return True
    @property
    def rank(self):return len(self.rows)
class RationalCoordinateBasis:
    def __init__(self,vectors):
        self.rows={};self.dimension=len(vectors)
        for idx,row in enumerate(vectors):
            r=list(row);coeff=[Fraction(0)]*self.dimension;coeff[idx]=1
            for p in sorted(self.rows):
                if r[p]:
                    q=r[p];b,bc=self.rows[p];r=[x-q*y for x,y in zip(r,b)];coeff=[x-q*y for x,y in zip(coeff,bc)]
            p=next(i for i,x in enumerate(r) if x);q=r[p]
            r=[x/q for x in r];coeff=[x/q for x in coeff];self.rows[p]=(r,coeff)
    def coordinates(self,row):
        r=list(row);coeff=[Fraction(0)]*self.dimension
        for p in sorted(self.rows):
            if r[p]:
                q=r[p];b,bc=self.rows[p];r=[x-q*y for x,y in zip(r,b)];coeff=[x+q*y for x,y in zip(coeff,bc)]
        assert not any(r);return coeff

def exact_rank(rows): return RationalBasis(rows).rank
side=RationalBasis(SIDE)
M_res=[side.reduce(r) for r in FOUR];T_res=[side.reduce(r) for r in GROUND]
assert RationalBasis(T_res).rank==15
BLOCK_LABELS=list(combinations(range(1,8),3)); BLOCK_INDEX={f:i for i,f in enumerate(BLOCK_LABELS)}; BLOCKS=[]
for face in BLOCK_LABELS:
    ids=tuple(i for i,d in enumerate(DESC) if set(d)=={0,*face});assert len(ids)==3;BLOCKS.append(ids)
SECTION_IDS=[e for block in BLOCKS for e in block[:2]]
coord_basis=RationalCoordinateBasis([M_res[e] for e in SECTION_IDS]+T_res)
COORD=[coord_basis.coordinates(r) for r in M_res]
assert all(x.denominator==1 for c in COORD for x in c)
QCOORD=[tuple(int(x) for x in c[:70]) for c in COORD]; MCOORD=[tuple(int(x) for x in c) for c in COORD]
NO_ROOT=[i for i,d in enumerate(DESC) if 0 not in d]; assert len(NO_ROOT)==105
QCOMP={}
for e in NO_ROOT:
    comp=tuple((QCOORD[e][2*b],QCOORD[e][2*b+1]) for b in range(35))
    touched={b for b,v in enumerate(comp) if v!=(0,0)}
    exp={BLOCK_INDEX[tuple(face)] for face in combinations(sorted(set(DESC[e])),3)}
    assert touched==exp and len(touched)==4; QCOMP[e]=comp
LOCAL=((1,0),(0,1),(1,-1)); DIR_MASK={(1,0):1,(0,1):2,(1,-1):4}
SUPPORTS=tuple(combinations(range(1,8),4))
SUPPORT_CYCLES={F:tuple(e for e in NO_ROOT if set(DESC[e])==set(F)) for F in SUPPORTS}
assert all(len(v)==3 for v in SUPPORT_CYCLES.values())

def cycle_key(desc):
    d=list(desc)
    return tuple(sorted(tuple(sorted((d[i],d[(i+1)%4]))) for i in range(4)))
KEY_TO_CYCLE={cycle_key(DESC[e]):e for e in NO_ROOT}

def complete_root_row(block):
    ids=BLOCKS[block]
    return tuple(MCOORD[ids[0]][70+j]-MCOORD[ids[1]][70+j]-MCOORD[ids[2]][70+j] for j in range(15))
HROW=tuple(complete_root_row(b) for b in range(35))
P=(1<<127)-1

def rank_mod(rows,p=P):
    if not rows:return 0
    a=[[int(x)%p for x in row] for row in rows];r=0;n=len(a);m=len(a[0])
    for c in range(m):
        piv=next((i for i in range(r,n) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r];pv=a[r][c]
        for i in range(r+1,n):
            q=a[i][c]
            if q:a[i]=[(pv*x-q*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def permute_support(F,pmap): return tuple(sorted(pmap[x] for x in F))
def permute_block_idx(b,pmap): return BLOCK_INDEX[tuple(sorted(pmap[x] for x in BLOCK_LABELS[b]))]

def stabilizer(family):
    fam=set(family); out=[]
    for perm in permutations(range(1,8)):
        pmap={i+1:perm[i] for i in range(7)}
        if {permute_support(F,pmap) for F in fam}==fam:
            out.append(pmap)
    return out

def skeleton_reps(family):
    family=tuple(sorted(family)); stab=stabilizer(family)
    cand=[]
    for i3 in range(6):
      for i2 in range(6):
        if i2==i3: continue
        mult={family[i]: (3 if i==i3 else 2 if i==i2 else 1) for i in range(6)}
        touch=Counter()
        for F,m in mult.items():
            for tri in combinations(F,3): touch[BLOCK_INDEX[tuple(sorted(tri))]] += m
        eligible=tuple(sorted(b for b,v in touch.items() if v>=4))
        touched=tuple(sorted(touch))
        for singles in combinations(eligible,4):
            complete=tuple(b for b in touched if b not in singles)
            rr=rank_mod(tuple(HROW[b] for b in complete))
            if len(complete)-rr>1: continue
            cand.append((tuple(mult[F] for F in family),tuple(sorted(singles))))
    def transform(sk,pmap):
        mults,singles=sk
        md={family[i]:mults[i] for i in range(6)}
        md2={permute_support(F,pmap):m for F,m in md.items()}
        m2=tuple(md2[F] for F in family)
        s2=tuple(sorted(permute_block_idx(b,pmap) for b in singles))
        return (m2,s2)
    unseen=set(cand); reps=[]
    while unseen:
        sk=min(unseen); reps.append(sk)
        orb={transform(sk,p) for p in stab}
        unseen.difference_update(orb)
    return family,stab,tuple(reps),len(cand)

def rank3_basis(rows):
    # return three independent rows if rank is 3, None otherwise; four rows max
    for inds in combinations(range(len(rows)),3):
        rr=[rows[i] for i in inds]
        # any nonzero 3x3 minor
        for cols in combinations(range(9),3):
            a,b,c=rr
            i,j,k=cols
            det=a[i]*(b[j]*c[k]-b[k]*c[j])-a[j]*(b[i]*c[k]-b[k]*c[i])+a[k]*(b[i]*c[j]-b[j]*c[i])
            if det:
                # ensure fourth row in span; rank cannot exceed 3 is required separately
                if rank_mod(rows)==3:
                    return rr
                return None
    return None

def primitive(v):
    g=0
    for x in v:gcd(g,abs(int(x)))
    for x in v:g=gcd(g,abs(int(x)))
    assert g
    q=tuple(int(x)//g for x in v)
    for x in q:
        if x:return tuple(-y for y in q) if x<0 else q
    raise AssertionError

def generalized_weights(rows3):
    cols=[tuple(row[j] for row in rows3) for j in range(9)]
    zero=cols.count((0,0,0)); d3=9-zero
    dirs=Counter(primitive(c) for c in cols if c!=(0,0,0)); d2=9-(zero+max(dirs.values()))
    nonzero=[c for c in cols if c!=(0,0,0)]; normals=set()
    for a,b in combinations(nonzero,2):
        n=(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
        if n!=(0,0,0):normals.add(primitive(n))
    maxplane=max(sum(n[0]*c[0]+n[1]*c[1]+n[2]*c[2]==0 for c in cols) for n in normals)
    d1=9-maxplane
    return d1,d2,d3

def rowspace_key(rows):
    basis={}
    for row in rows:
        r=[Fraction(x) for x in row]
        for p in sorted(basis):
            if r[p]:
                q=r[p]; br=basis[p]; r=[x-q*y for x,y in zip(r,br)]
        p=next((i for i,x in enumerate(r) if x),None)
        if p is None: continue
        q=r[p]; r=[x/q for x in r]
        for p0 in list(basis):
            if basis[p0][p]:
                q0=basis[p0][p]; basis[p0]=[x-q0*y for x,y in zip(basis[p0],r)]
        basis[p]=r
    return tuple(tuple(basis[p]) for p in sorted(basis))

def primitive_int(v):
    L=1
    for x in v:L=lcm(L,x.denominator)
    a=[int(x*L) for x in v]; g=0
    for x in a:g=gcd(g,abs(x))
    if g:a=[x//g for x in a]
    for x in a:
        if x:
            if x<0:a=[-y for y in a]
            break
    return tuple(a)

def nullspace_int(key,n):
    piv=[next(i for i,x in enumerate(row) if x) for row in key]
    free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        v=[Fraction(0)]*n;v[f]=1
        for row,p in zip(key,piv):v[p]=-row[f]
        out.append(primitive_int(v))
    return out

def solve_local_coeffs(mask,w):
    wx,wy=w; chosen=[j for j in range(3) if (mask>>j)&1]
    if len(chosen)==1:
        j=chosen[0];ux,uy=LOCAL[j];q=wx//ux if ux else wy//uy
        assert q*ux==wx and q*uy==wy
        out=[0,0,0];out[j]=q;return out
    j,h=chosen[:2];ax,ay=LOCAL[j];bx,by=LOCAL[h];det=ax*by-ay*bx
    q=(wx*by-wy*bx)//det;r=(ax*wy-ay*wx)//det
    assert q*ax+r*bx==wx and q*ay+r*by==wy
    out=[0,0,0];out[j]=q;out[h]=r;return out

def relation_rows(ext,touched,single_dir,key):
    rows=[HROW[b] for b in touched if b not in single_dir]
    for alpha in nullspace_int(key,len(ext)):
        tv=[sum(alpha[i]*MCOORD[e][70+j] for i,e in enumerate(ext)) for j in range(15)]
        for b in touched:
            vx=sum(alpha[i]*QCOMP[e][b][0] for i,e in enumerate(ext)); vy=sum(alpha[i]*QCOMP[e][b][1] for i,e in enumerate(ext))
            mask=DIR_MASK[single_dir[b]] if b in single_dir else 7
            beta=solve_local_coeffs(mask,(-vx,-vy)); ids=BLOCKS[b]
            for j0,q in enumerate(beta):
                if q:
                    for jj in range(15): tv[jj]+=q*MCOORD[ids[j0]][70+jj]
        rows.append(tuple(tv))
    return rows

def singleton_row(ext,b,d):
    lx,ly=d
    return tuple(lx*QCOMP[e][b][1]-ly*QCOMP[e][b][0] for e in ext)

def ext_choices(family,mults):
    parts=[]
    for F,m in zip(family,mults):
        cyc=SUPPORT_CYCLES[F]
        if m==3: parts.append((cyc,))
        elif m==2: parts.append(tuple(tuple(sorted(c)) for c in combinations(cyc,2)))
        else: parts.append(tuple((e,) for e in cyc))
    for sel in product(*parts):
        ext=tuple(sorted(e for tup in sel for e in tup)); assert len(ext)==9
        yield ext

def raw_skeletons(family):
    family=tuple(sorted(family)); cand=[]
    for i3 in range(6):
      for i2 in range(6):
        if i2==i3: continue
        mult={family[i]: (3 if i==i3 else 2 if i==i2 else 1) for i in range(6)}
        touch=Counter()
        for F,m in mult.items():
            for tri in combinations(F,3): touch[BLOCK_INDEX[tuple(sorted(tri))]] += m
        eligible=tuple(sorted(b for b,v in touch.items() if v>=4)); touched=tuple(sorted(touch))
        for singles in combinations(eligible,4):
            complete=tuple(b for b in touched if b not in singles)
            rr=rank_mod(tuple(HROW[b] for b in complete))
            if len(complete)-rr>1: continue
            cand.append((tuple(mult[F] for F in family),tuple(sorted(singles))))
    return family,tuple(cand)

def scan(family,label):
    family,cands=raw_skeletons(family); counts=Counter(); inc=Counter(); maxnorm=0
    touched=tuple(sorted({BLOCK_INDEX[tuple(sorted(tri))] for F in family for tri in combinations(F,3)}))
    for idx,(mults,singles) in enumerate(cands):
      complete=tuple(b for b in touched if b not in singles); root_rank=rank_mod(tuple(HROW[b] for b in complete))
      assert len(complete)-root_rank==1
      for ext in ext_choices(family,mults):
        counts['oriented']+=1
        local={(b,d):singleton_row(ext,b,d) for b in singles for d in LOCAL}
        for dirs in product(LOCAL,repeat=4):
          counts['direction']+=1
          rows=tuple(local[(b,d)] for b,d in zip(singles,dirs))
          basis=rank3_basis(rows)
          if basis is None: continue
          counts['rank3']+=1
          gw=generalized_weights(basis)
          if not (gw[0]>=3 and gw[1]>=4 and gw[2]>=6): continue
          counts['weight']+=1
          key=rowspace_key(rows); rel=relation_rows(ext,touched,dict(zip(singles,dirs)),key)
          for row in rel:maxnorm=max(maxnorm,sum(x*x for x in row))
          incr=rank_mod(rel)-root_rank; inc[incr]+=1
          assert incr<6
      if idx%10==0: print(label,idx,dict(counts),dict(inc),flush=True)
    return len(cands),dict(counts),dict(inc),maxnorm


def lucas_lehmer_127():
    s=4
    for _ in range(125):
        s=(s*s-2)%P
    return s==0

def main():
    assert lucas_lehmer_127()
    W=(1,2,3,4,5)
    faces=[tuple(sorted(set(W)-{x})) for x in W]
    f3=tuple(sorted(faces+[tuple(sorted((1,2,3,6)))]))
    f2=tuple(sorted(faces+[tuple(sorted((1,2,6,7)))]))
    a=scan(f3,'overlap3')
    b=scan(f2,'overlap2')
    assert a[0]==61 and b[0]==25
    assert a[1]=={'oriented':14823,'direction':1200663,'rank3':44664,'weight':432}
    assert a[2]=={0:432}
    assert a[3]==46
    assert b[1]=={'oriented':6075,'direction':492075,'rank3':25650}
    assert b[2]=={}
    assert b[3]==0
    B=max(a[3],b[3],max(sum(x*x for x in row) for row in HROW),1)
    assert P*P > B**15
    print('PASS: nine-no-root k=6,D=-2,d_root=1,p=4 m=6 closure')
    print('overlap3_raw_skeletons',a[0])
    print('overlap3_counts',a[1])
    print('overlap3_external_increment_census',a[2])
    print('overlap2_raw_skeletons',b[0])
    print('overlap2_counts',b[1])
    print('overlap2_external_increment_census',b[2])
    print('max_relation_row_norm_squared',B)
    print('hadamard_exact_rank_bound',P*P > B**15)

if __name__=='__main__': main()
