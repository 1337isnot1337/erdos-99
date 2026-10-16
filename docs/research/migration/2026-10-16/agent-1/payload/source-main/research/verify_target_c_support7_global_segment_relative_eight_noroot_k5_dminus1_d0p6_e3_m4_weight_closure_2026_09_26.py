#!/usr/bin/env python3
"""Exact p=6,e=3,m=4 empty-space-rank closure."""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import contextlib, importlib.util, io

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py"
sp=importlib.util.spec_from_file_location("p6_e3_m4_base",BASE)
M=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(M)

def empty_key(ext,b):
    x=tuple(M.R.QCOMP[e][b][0] for e in ext)
    y=tuple(M.R.QCOMP[e][b][1] for e in ext)
    return M.R.rowspace_key((x,y))

def assignment_orbits(profile):
    out=[]
    for ss in M.four_support_orbits():
        stab=[pm for pm,_ in M.PERM_DATA if tuple(sorted(pm[i] for i in ss))==ss]
        pos={s:i for i,s in enumerate(ss)}
        unseen=set(permutations(profile))
        while unseen:
            a=min(unseen); amap=dict(zip(ss,a)); orb=set()
            for pm in stab:
                z=[None]*4
                for s,v in amap.items(): z[pos[pm[s]]]=v
                orb.add(tuple(z))
            unseen.difference_update(orb); out.append((ss,a))
    return tuple(out)

def phase_exts(ss,a):
    opts=[]
    for si,m in zip(ss,a):
        es=M.SUPPORT_CYCLES[M.SUPPORTS[si]]
        if m==3: opts.append((es,))
        elif m==2: opts.append(tuple(tuple(e for j,e in enumerate(es) if j!=o) for o in range(3)))
        elif m==1: opts.append(tuple((e,) for e in es))
        else: raise AssertionError(m)
    for q in product(*opts):
        ext=tuple(sorted(sum((tuple(x) for x in q),())))
        assert len(ext)==8
        yield ext

def empty_triples(ss,a):
    poss={}
    for b,tri in enumerate(M.R.BLOCK_LABELS):
        idx=[j for j,si in enumerate(ss) if set(tri).issubset(M.SUPPORTS[si])]
        if not idx: continue
        n=sum(a[j] for j in idx)
        if any(a[j]>=2 for j in idx):
            if n>=4: poss[b]=(idx,2)
        elif n>=2:
            poss[b]=(idx,1)
    ans=[]
    for t in combinations(poss,3):
        good=True
        for x,y in combinations(t,2):
            if poss[x][1]==poss[y][1]==2:
                common=set(poss[x][0])&set(poss[y][0])
                if sum(a[j] for j in common)<2:
                    good=False; break
        if good: ans.append(t)
    return tuple(ans)

def scan(profile):
    aa=assignment_orbits(profile); kept=phases=triples=0; ranks=Counter()
    for ss,a in aa:
        ts=empty_triples(ss,a)
        if not ts: continue
        kept+=1
        for ext in phase_exts(ss,a):
            phases+=1
            for t in ts:
                U=()
                for b in t: U=M.R.rowspace_key(U+empty_key(ext,b))
                triples+=1; ranks[len(U)]+=1
                assert len(U)>3
    return len(aa),kept,phases,triples,dict(sorted(ranks.items()))

def main():
    exp={
      (3,3,1,1):(135,17,153,261,{4:30,5:107,6:124}),
      (3,2,2,1):(226,13,351,405,{5:261,6:144}),
      (2,2,2,2):(38,8,648,1296,{5:729,6:567}),
    }
    got={p:scan(p) for p in exp}
    assert got==exp,got
    assert sum(v[0] for v in got.values())==399
    assert sum(v[1] for v in got.values())==38
    assert sum(v[2] for v in got.values())==1152
    assert sum(v[3] for v in got.values())==1962
    print("PASS: p=6 e=3 m=4 empty-space rank closure")
    for p in exp: print(p,got[p])
    print("U_rank_census",{4:30,5:1097,6:835})

if __name__=="__main__": main()
