#!/usr/bin/env python3
"""Exact e=5 closure for the final p=6 branch; shardable phase scan."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse, contextlib, importlib.util, io

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e4_weight_closure_2026_09_26.py"
sp=importlib.util.spec_from_file_location("p6_e5_parent",BASE)
B=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(B)
M=B.M; SUPPORTS=B.SUPPORTS; PERM_DATA=B.PERM_DATA

def support_orbits():
    reps={}
    unseen=set(combinations(range(35),3)); out=[]
    while unseen:
        ss=min(unseen)
        orb={tuple(sorted(smap[i] for i in ss)) for smap,_ in PERM_DATA}
        unseen.difference_update(orb)
        if B.support_nullity(ss)<=6: out.append(ss)
    reps[3]=tuple(out)
    for m in range(4,9):
        cands=set()
        for ss in reps[m-1]:
            for j in range(35):
                if j in ss: continue
                u=tuple(sorted(ss+(j,)))
                if B.support_nullity(u)<=6: cands.add(B.canonical_support(u))
        reps[m]=tuple(sorted(cands))
    got={m:(len(v),dict(sorted(Counter(B.support_nullity(s) for s in v).items()))) for m,v in reps.items()}
    assert got=={
      3:(10,{3:10}),4:(38,{4:35,5:3}),5:(135,{4:1,5:107,6:27}),
      6:(302,{5:2,6:300}),7:(10,{6:10}),8:(0,{})},got
    return reps

PROFILES={
  3:((3,3,2),),
  4:((3,3,1,1),(3,2,2,1),(2,2,2,2)),
  5:((3,2,1,1,1),(2,2,2,1,1)),
  6:((3,1,1,1,1,1),(2,2,1,1,1,1)),
  7:((2,1,1,1,1,1,1),),
  8:((1,1,1,1,1,1,1,1),),
}

def empty_quintuples(ss,a):
    poss={}
    for b,tri in enumerate(M.R.BLOCK_LABELS):
        idx=tuple(j for j,si in enumerate(ss) if set(tri).issubset(SUPPORTS[si]))
        if not idx: continue
        n=sum(a[j] for j in idx); plane=any(a[j]>=2 for j in idx)
        if plane:
            if n<4: continue
            poss[b]=(idx,2)
        else:
            if n<2: continue
            poss[b]=(idx,1)
    out=[]
    for q in combinations(poss,5):
        ok=True
        for x,y in combinations(q,2):
            if poss[x][1]==poss[y][1]==2:
                shared=set(poss[x][0])&set(poss[y][0])
                if sum(a[j] for j in shared)<2: ok=False; break
        if ok: out.append(q)
    return tuple(out)

def enumerate_prefilter():
    reps=support_orbits(); ac=Counter(); ka=Counter(); kq=Counter(); kept=[]
    for m in range(3,9):
        for ss in reps[m]:
            for p in PROFILES[m]:
                for a in B.assignment_orbits(ss,p):
                    ac[m]+=1; qs=empty_quintuples(ss,a)
                    if qs:
                        key=(m,tuple(sorted(a,reverse=True)))
                        ka[key]+=1; kq[key]+=len(qs); kept.append((ss,a,qs))
    assert dict(ac)=={3:17,4:399,5:2655,6:4967,7:39},ac
    assert sum(ac.values())==8077
    assert dict(ka)=={
      (5,(3,2,1,1,1)):24,
      (6,(3,1,1,1,1,1)):874,
      (6,(2,2,1,1,1,1)):121,
      (7,(2,1,1,1,1,1,1)):39},ka
    assert dict(kq)=={
      (5,(3,2,1,1,1)):94,
      (6,(3,1,1,1,1,1)):7370,
      (6,(2,2,1,1,1,1)):414,
      (7,(2,1,1,1,1,1,1)):3897},kq
    assert len(kept)==1058 and sum(len(q) for _,_,q in kept)==11775
    return kept,ac,ka,kq

def masks(ext,blocks):
    out={}
    for b in blocks:
        x=y=0
        for j,e in enumerate(ext):
            vx,vy=M.R.QCOMP[e][b]
            if vx&1:x|=1<<j
            if vy&1:y|=1<<j
        out[b]=(x,y)
    return out

def rank2(rows):
    basis={}
    for z in rows:
        x=z
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    return len(basis)

def scan(kept,start,stop):
    c=Counter()
    for ss,a,qs in kept[start:stop]:
        c["phases"]+=3**sum(x<3 for x in a)
        blocks=set(b for q in qs for b in q)
        for ext in B.phase_exts(ss,a):
            mm=masks(ext,blocks)
            for q in qs:
                c["pairs"]+=1
                r=rank2(tuple(z for b in q for z in mm[b]));c[f"rank{r}"]+=1
                assert r>3,(ss,a,ext,q,r)
    return c

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--assignment-start",type=int,default=0)
    ap.add_argument("--assignment-stop",type=int)
    ap.add_argument("--prefilter-only",action="store_true")
    args=ap.parse_args()
    kept,ac,ka,kq=enumerate_prefilter()
    print("support_multiplicity_orbits",sum(ac.values()))
    print("prefilter_assignments",len(kept))
    print("prefilter_empty_quintuples",sum(len(q) for _,_,q in kept))
    print("prefilter_profile_assignments",dict(ka))
    print("prefilter_profile_quintuples",dict(kq))
    if args.prefilter_only:return
    stop=len(kept) if args.assignment_stop is None else args.assignment_stop
    assert 0<=args.assignment_start<=stop<=len(kept)
    c=scan(kept,args.assignment_start,stop)
    print("assignment_range",args.assignment_start,stop)
    print("phase_configs",c["phases"])
    print("phase_empty_quintuple_pairs",c["pairs"])
    print("rank_F2_census",{int(k[4:]):v for k,v in sorted(c.items()) if k.startswith("rank")})
    print("PASS: every checked e=5 case has rank_F2(U)>3")
if __name__=="__main__":main()
