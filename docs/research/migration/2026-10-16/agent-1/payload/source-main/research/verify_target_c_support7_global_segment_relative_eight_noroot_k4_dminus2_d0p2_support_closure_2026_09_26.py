from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product

MOD=2147483647
V=tuple(range(7)); SUP=tuple(combinations(V,4)); SI={s:i for i,s in enumerate(SUP)}; TRI=tuple(combinations(V,3)); TI={t:i for i,t in enumerate(TRI)}; EDGES=tuple(combinations(V,2)); EI={e:i for i,e in enumerate(EDGES)}
EXPECTED=(1,1,4,14,61,268,1283,6032,27763)
BOUND=[]
for s in SUP:
    row=[0]*35
    for j in range(4): row[TI[s[:j]+s[j+1:]]]=1 if j%2==0 else -1
    BOUND.append(tuple(row))
TRIROW=[]
for a,b,c in TRI:
    row=[0]*21; row[EI[(b,c)]]=1; row[EI[(a,c)]]=-1; row[EI[(a,b)]]=1; TRIROW.append(tuple(row))

def rank_mod(rows):
    if not rows:return 0
    A=[[x%MOD for x in r] for r in rows]; m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        inv=pow(A[rr][c],MOD-2,MOD); A[rr]=[(x*inv)%MOD for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                q=A[i][c]; A[i]=[(x-q*y)%MOD for x,y in zip(A[i],A[rr])]
        rr+=1
        if rr==m:break
    return rr

@lru_cache(None)
def tri_rank(blocks):return rank_mod([TRIROW[b] for b in blocks])
@lru_cache(None)
def canonical(ms):
    degree=[0]*7
    for si in ms:
        for v in SUP[si]:degree[v]+=1
    vals=sorted(set(degree),reverse=True); groups=[]; pos=[]; off=0
    for val in vals:
        g=tuple(v for v in V if degree[v]==val);groups.append(g);pos.append(tuple(range(off,off+len(g))));off+=len(g)
    best=None
    for choices in product(*(permutations(g) for g in groups)):
        rel=[None]*7
        for oldord,newpos in zip(choices,pos):
            for old,new in zip(oldord,newpos):rel[old]=new
        im=tuple(sorted(SI[tuple(sorted(rel[v] for v in SUP[si]))] for si in ms))
        if best is None or im<best:best=im
    return best

def orbits():
    reps={()}; counts=[1]
    for _ in range(8):
        out=set()
        for ms in reps:
            mult=Counter(ms)
            for si in range(35):
                if mult[si]<3:out.add(canonical(tuple(sorted(ms+(si,)))))
        reps=out;counts.append(len(reps))
    assert tuple(counts)==EXPECTED
    return tuple(sorted(reps))

def block_data(ms):
    mult=Counter(ms);data={}
    for b,tri in enumerate(TRI):
        I=frozenset(i for i,si in enumerate(ms) if set(tri).issubset(SUP[si]))
        if not I:continue
        d=2 if any(mult[ms[i]]>=2 for i in I) else 1
        data[b]=(I,d,len(I))
    return data

def elig(x):return x[2]>=(5 if x[1]==2 else 4)
def compat(x,y):
    Ix,dx,nx=x;Iy,dy,ny=y;inter=len(Ix&Iy);union=nx+ny-inter
    if dx==dy==1:return inter>=4 or union>=5
    if dx!=dy:return inter>=4 or union>=6
    return inter>=5 or (inter>=4 and union>=6) or union>=7

def support_union_size(blocks,data):
    U=set()
    for b in blocks:U.update(data[b][0])
    return len(U)

def structural_ok(ms,data,I):
    T=tuple(sorted(data)); C=tuple(b for b in T if b not in I)
    if tri_rank(C)!=len(C):return None
    nu=len(T)-tri_rank(T)
    cap=len(I)-nu
    if cap<4:return None
    # explicit tetra-boundary injectivity cross-check
    distinct=tuple(sorted(set(ms)))
    full=rank_mod([BOUND[si] for si in distinct])
    restricted=[]
    cols=tuple(sorted(I))
    for si in distinct:restricted.append(tuple(BOUND[si][c] for c in cols))
    if rank_mod(restricted)!=full:return None
    return nu,cap,full

def pair_profile(ms,data):
    h=len(data); Elist=sorted(b for b in data if elig(data[b])); later={b:{w for w in Elist if w>b and compat(data[b],data[w])} for b in Elist}; found=None
    def test(E,dimE):
        nonlocal found
        if dimE<4 or support_union_size(E,data)<7:return False
        # selected pair untouched
        if h<35 and len(E)>=h-15:
            st=structural_ok(ms,data,set(E))
            if st:found=(tuple(E),None)+st;return True
        # selected pair touched
        if len(E)>=h-16:
            for pb in data:
                if pb in E:continue
                st=structural_ok(ms,data,set(E)|{pb})
                if st:found=(tuple(E),pb)+st;return True
        return False
    def rec(E,cands,dimE):
        nonlocal found
        if found:return
        if test(E,dimE):return
        ordered=sorted(cands)
        for i,b in enumerate(ordered):
            rec(E+[b],set(ordered[i+1:])&later[b],dimE+data[b][1])
            if found:return
    rec([],set(Elist),0);return found

def single_profile(ms,data):
    h=len(data);Elist=sorted(b for b in data if elig(data[b]));later={b:{w for w in Elist if w>b and compat(data[b],data[w])} for b in Elist};found=None
    def test(E,dimE):
        nonlocal found
        rem=[b for b in data if b not in E]
        for t in (0,1,2):
            if 35-h<2-t or len(E)<h-15-t:continue
            for S in combinations(rem,t):
                choices=[([0,1] if data[b][2]>=4 else [0]) for b in S]
                for dims in product(*choices) if choices else [()]:
                    nz=list(E)+[b for b,d in zip(S,dims) if d]
                    if dimE+sum(dims)<4 or support_union_size(nz,data)<7:continue
                    objs=[data[b] for b in E]+[(data[b][0],1,data[b][2]) for b,d in zip(S,dims) if d]
                    if any(not compat(objs[i],objs[j]) for i in range(len(objs)) for j in range(i)):continue
                    st=structural_ok(ms,data,set(E)|set(S))
                    if st:found=(tuple(E),tuple(zip(S,dims)),2-t)+st;return True
        return False
    def rec(E,cands,dimE):
        nonlocal found
        if found:return
        if test(E,dimE):return
        ordered=sorted(cands)
        for i,b in enumerate(ordered):
            rec(E+[b],set(ordered[i+1:])&later[b],dimE+data[b][1])
            if found:return
    rec([],set(Elist),0);return found

def lucas_lehmer_31():
    s=4
    for _ in range(29): s=(s*s-2)%MOD
    return s==0

def main():
    assert lucas_lehmer_31()
    assert MOD*MOD>4**15
    reps=orbits(); C=Counter(); res=[]
    for ms in reps:
        data=block_data(ms);h=len(data);C['all']+=1
        if h>20:continue
        C['h_le20']+=1
        p=pair_profile(ms,data);s=single_profile(ms,data)
        if p:C['pair']+=1
        if s:C['single']+=1
        if p or s:res.append((ms,h,p,s))
    assert C['all']==27763 and C['h_le20']==13574,C
    assert C['pair']==0 and C['single']==0 and not res,(C,res[:3])
    print('PASS: eight-no-root k=4 D=-2 d_root=0 p=2 support closure')
    print('orbit_counts_size_0_through_8',EXPECTED)
    print('support_multiset_orbits_size_8',C['all'])
    print('touch_at_most_20',C['h_le20'])
    print('pair_profile_survivors',C['pair'])
    print('two_singleton_profile_survivors',C['single'])
    print('hadamard_exact_rank_bound',MOD*MOD>4**15)
if __name__=='__main__':main()
