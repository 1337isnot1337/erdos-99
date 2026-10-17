#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations, product
from collections import Counter
from functools import lru_cache

# Exact oriented certificate for the nine-no-root k=4,D=-1,d_root=0,p=2
# selected-pair profile, restricted to the two support representatives left by
# the support-level narrowing. All arithmetic governing the coefficient spaces
# is rational.

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
                    q=r[p]; b,bc=self.rows[p]; r=[x-q*y for x,y in zip(r,b)]; coeff=[x-q*y for x,y in zip(coeff,bc)]
            p=next(i for i,x in enumerate(r) if x); q=r[p]
            r=[x/q for x in r]; coeff=[x/q for x in coeff]; self.rows[p]=(r,coeff)
    def coordinates(self,row):
        r=list(row); coeff=[Fraction(0)]*self.dimension
        for p in sorted(self.rows):
            if r[p]:
                q=r[p]; b,bc=self.rows[p]; r=[x-q*y for x,y in zip(r,b)]; coeff=[x+q*y for x,y in zip(coeff,bc)]
        assert not any(r); return coeff

def exact_rank(rows): return RationalBasis(rows).rank

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
QCOORD=[tuple(int(x) for x in c[:70]) for c in COORD]
assert exact_rank(QCOORD)==70
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

@lru_cache(maxsize=None)
def union_key(a,b): return rowspace_key(a+b)

def is_subspace(a,b): return len(union_key(a,b))==len(b)

def empty_key(ext,b):
    vals=[QCOMP[e][b] for e in ext]
    x=tuple(v[0] for v in vals); y=tuple(v[1] for v in vals)
    return rowspace_key((x,y))

EDGES=list(combinations(range(7),2)); EDGE_INDEX={e:i for i,e in enumerate(EDGES)}
H=[]
for tri in combinations(range(7),3):
    a,b,c=tri; row=[0]*21
    row[EDGE_INDEX[(b,c)]]=1
    row[EDGE_INDEX[(a,c)]]=-1
    row[EDGE_INDEX[(a,b)]]=1
    H.append(tuple(row))
assert len(H)==35

@lru_cache(maxsize=None)
def h_rank(mask):
    rows=[H[b] for b in range(35) if (mask>>b)&1]
    return exact_rank(rows)

def parity_profile_ok(W):
    assert len(W)==4
    cols=[tuple(W[r][c] for r in range(4)) for c in range(9)]
    if any(all(x==0 for x in col) for col in cols): return False
    for S in combinations(range(9),3):
        if exact_rank([tuple(cols[c][r] for c in S) for r in range(4)]) < 2:
            return False
    for S in combinations(range(9),6):
        if exact_rank([tuple(cols[c][r] for c in S) for r in range(4)]) < 3:
            return False
    return True

def generalized_weights_from_W(W):
    out=[]
    for j in range(1,6):
        dj=None
        for size in range(1,10):
            found=False
            for S in combinations(range(9),size):
                restricted=[tuple(row[c] for c in S) for row in W]
                if size-exact_rank(restricted) >= j:
                    dj=size; found=True; break
            if found: break
        assert dj is not None
        out.append(dj)
    return tuple(out)

def support_cycles(support0):
    want={v+1 for v in support0}
    es=[e for e in NO_ROOT if set(DESC[e])==want]
    assert len(es)==3
    return tuple(sorted(es))

REP6=[((0,1,2,3),3),((0,1,2,4),1),((0,1,3,4),1),((0,1,4,5),1),((0,2,3,4),1),((0,2,4,5),1),((1,2,3,4),1)]
REP13=[((0,1,2,3),3),((0,1,2,4),3),((0,1,3,4),1),((0,2,3,4),1),((1,2,3,4),1)]

def oriented_exts(rep):
    opts=[]
    for supp,m in rep:
        es=support_cycles(supp)
        if m==3: opts.append((es,))
        elif m==2: opts.append(tuple(combinations(es,2)))
        elif m==1: opts.append(tuple((e,) for e in es))
        else: raise AssertionError(m)
    for choice in product(*opts):
        ext=tuple(sorted(e for part in choice for e in part)); assert len(ext)==9
        yield ext

def candidate_rank4_spaces(ext,touched):
    sources=[empty_key(ext,b) for b in touched]
    spaces={()}
    for E in sources:
        new=set(spaces)
        for W in spaces:
            J=union_key(W,E)
            if len(J)<=4: new.add(J)
        spaces=new
    return tuple(W for W in spaces if len(W)==4)

def structural_survives(ext,W,touched, failures=None):
    touched_mask=sum(1<<b for b in touched)
    virtual_empty={b for b in touched if is_subspace(empty_key(ext,b),W)}
    base_incomplete=sum(1<<b for b in virtual_empty)
    placements=[None]+list(touched)
    passed=[]
    for s in placements:
        incomplete=base_incomplete | (0 if s is None else (1<<s))
        complete=touched_mask & ~incomplete
        rc=h_rank(complete)
        if rc != complete.bit_count():
            if failures is not None: failures['dependent']+=1
            continue
        if h_rank(touched_mask)-rc < 4:
            if failures is not None: failures['capacity']+=1
            continue
        passed.append(s)
    return passed

def run_rep(name,rep,expected_orientations,expected_spaces,expected_weight_pass):
    C=Counter(); structural=[]; failures=Counter()
    for ext in oriented_exts(rep):
        C['orientations']+=1
        touched=tuple(sorted({b for e in ext for b,v in enumerate(QCOMP[e]) if v!=(0,0)}))
        Ws=candidate_rank4_spaces(ext,touched)
        C['rank4_spaces']+=len(Ws)
        for W in Ws:
            if not parity_profile_ok(W): continue
            C['weight_pass']+=1
            d=generalized_weights_from_W(W)
            assert all(a>=b for a,b in zip(d,(2,4,5,7,8))),d
            C[('weight_profile',d)]+=1
            placements=structural_survives(ext,W,touched,failures)
            C['pair_placements_tested'] += len(touched)
            if placements:
                structural.append((ext,W,placements))
    print(name, dict(C), 'structural_survivors', len(structural), 'failures', dict(failures))
    assert C['orientations']==expected_orientations,C
    assert C['rank4_spaces']==expected_spaces,C
    assert C['weight_pass']==expected_weight_pass,C
    assert not structural, structural[:1]
    if name == 'rep6':
        assert C[('weight_profile',(2,4,5,7,9))] == 9, C
        assert failures == Counter({'dependent':144}), failures
    else:
        assert not failures, failures
    return C

def main():
    c6=run_rep('rep6',REP6,729,53455,9)
    c13=run_rep('rep13',REP13,27,1006,0)
    assert c6['pair_placements_tested']==135,c6
    print('PASS: selected-pair profile has zero survivors on both support representatives')

if __name__=='__main__': main()
