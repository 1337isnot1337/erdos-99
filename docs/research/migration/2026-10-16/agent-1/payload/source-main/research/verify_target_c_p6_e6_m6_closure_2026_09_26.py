#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib, importlib.util, io

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d0p6_e6_mle5_mod2_closure_2026_09_26.py"
sp=importlib.util.spec_from_file_location("e6m6_parent",BASE)
E6=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(E6)
E5=E6.E5; B=E6.B; M=E6.M; SUPPORTS=E6.SUPPORTS

def support_orbits_m6():
    reps=E6.support_orbits_through_m5()
    c=set()
    for ss in reps[5]:
        for j in range(35):
            if j in ss: continue
            u=tuple(sorted(ss+(j,)))
            if B.support_nullity(u)<=7: c.add(B.canonical_support(u))
    out=tuple(sorted(c))
    d=dict(sorted(Counter(B.support_nullity(s) for s in out).items()))
    assert len(out)==470 and d=={5:2,6:300,7:168},(len(out),d)
    return out

def strong_empty_sextuples(ss,a):
    poss={}
    for b,tri in enumerate(M.R.BLOCK_LABELS):
        idx=tuple(j for j,si in enumerate(ss) if set(tri).issubset(SUPPORTS[si]))
        if not idx: continue
        n=sum(a[j] for j in idx)
        dim=2 if any(a[j]>=2 for j in idx) else 1
        if dim==2 and n<4: continue
        if dim==1 and n<2: continue
        poss[b]=(idx,dim,n)
    out=[]
    for q in combinations(poss,6):
        ok=True
        for x,y in combinations(q,2):
            ix=set(poss[x][0]); iy=set(poss[y][0])
            inter=sum(a[j] for j in ix&iy)
            dx,dy=poss[x][1],poss[y][1]
            union=poss[x][2]+poss[y][2]-inter
            if dx==dy==2 and inter<2: ok=False; break
            if dx!=dy and inter<2 and union<5: ok=False; break
            if dx==dy==1 and inter<2 and union<4: ok=False; break
        if ok: out.append(q)
    return tuple(out)

def main():
    profiles=((3,1,1,1,1,1),(2,2,1,1,1,1))
    ac=Counter(); kc=Counter(); qc=Counter(); kept=[]
    for ss in support_orbits_m6():
        for p in profiles:
            for a in B.assignment_orbits(ss,p):
                k=tuple(sorted(a,reverse=True)); ac[k]+=1
                qs=strong_empty_sextuples(ss,a)
                if qs:
                    kc[k]+=1; qc[k]+=len(qs); kept.append((ss,a,qs))
    assert dict(ac)=={(3,1,1,1,1,1):2308,(2,2,1,1,1,1):5522},ac
    assert dict(kc)=={(3,1,1,1,1,1):32},kc
    assert dict(qc)=={(3,1,1,1,1,1):77},qc

    counts=Counter(); ranks=Counter()
    for ss,a,qs in kept:
        blocks=set(b for q in qs for b in q)
        for ext in B.phase_exts(ss,a):
            counts["phases"]+=1
            mm=E5.masks(ext,blocks)
            for q in qs:
                counts["pairs"]+=1
                r=E5.rank2(tuple(z for b in q for z in mm[b]))
                ranks[r]+=1
                assert r>3,(ss,a,ext,q,r)
    assert counts["phases"]==7776,counts
    assert counts["pairs"]==18711,counts
    assert dict(ranks)=={5:36,6:2989,7:15686},ranks
    print("PASS: p=6 e=6 m=6 closure")
    print("support_multiplicity_orbits",sum(ac.values()))
    print("prefilter_assignments",len(kept))
    print("prefilter_empty_sextuples",sum(len(q) for _,_,q in kept))
    print("phase_configs",counts["phases"])
    print("phase_empty_sextuple_pairs",counts["pairs"])
    print("rank_F2_census",dict(sorted(ranks.items())))

if __name__=="__main__": main()
