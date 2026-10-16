#!/usr/bin/env python3
"""Verify the final-third certificate for the second order-1 (3,2,2,1) support class."""
import argparse, contextlib, importlib.util, io
from collections import Counter
from itertools import combinations, product
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py"
spec=importlib.util.spec_from_file_location("V",BASE)
V=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)
R=V.R

TARGET=((1,2,3,4),(1,2,3,5),(1,4,5,6),(2,4,6,7))
EXPECTED={
    0:(216,234,4176,112752,84888,4104,36),
    1:(234,252,4176,112752,86256,3888,36),
    2:(252,270,4176,112752,87048,3960,36),
    3:(270,288,4176,112752,88704,4896,36),
    4:(288,306,4176,112752,88704,4896,36),
    5:(306,324,4176,112752,88416,4608,36),
}
EXPECTED_TOTAL=(25056,676512,524016,26352)
EXPECTED_FULL=(75168,2029536,1561464,77544)

def candidates(si):
    faces=tuple(V.SUPPORTS[i] for i in si)
    out=set()
    for p3 in range(4):
        for p1 in range(4):
            if p1==p3:
                continue
            p2=tuple(i for i in range(4) if i not in (p3,p1))
            for o0,o1,c1 in product(range(3),repeat=3):
                ext=[]
                for i,F in enumerate(faces):
                    es=V.SUPPORT_CYCLES[F]
                    if i==p3:
                        ext.extend(es)
                    elif i==p1:
                        ext.append(es[c1])
                    elif i==p2[0]:
                        ext.extend(e for j,e in enumerate(es) if j!=o0)
                    else:
                        ext.extend(e for j,e in enumerate(es) if j!=o1)
                out.add(tuple(sorted(ext)))
    assert len(out)==324
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--subshard",type=int,choices=range(6),required=True)
    a=ap.parse_args()

    si=tuple(V.SUPPORT_INDEX[F] for F in TARGET)
    stab=tuple(c for s,c in V.PERM_DATA if tuple(sorted(s[i] for i in si))==si)
    assert len(stab)==1
    reps=tuple(sorted(candidates(si)))
    assert len(reps)==324

    touched=V.touched_blocks(reps[0])
    assert len(touched)==15 and all(V.touched_blocks(e)==touched for e in reps)
    assert R.exact_rank(tuple(V.HROW[b] for b in touched))==11

    adm=[]
    for sb in combinations(touched,3):
        comp=tuple(b for b in touched if b not in sb)
        rr=R.rank_mod(tuple(V.HROW[b] for b in comp))
        if len(comp)-rr==1:
            adm.append((sb,rr))
    assert len(adm)==232

    start,end,es,ed,er,eg,en=EXPECTED[a.subshard]
    c=[0,0,0,0]
    inc=Counter()
    mx=0

    for ext in reps[start:end]:
        lr={(b,d):V.singleton_row(ext,b,d) for b in touched for d in V.LOCAL}
        c[0]+=len(adm)
        for sb,rr in adm:
            for ds in product(V.LOCAL,repeat=3):
                c[1]+=1
                rows=tuple(lr[(b,d)] for b,d in zip(sb,ds))
                if not V.rank_three(rows):
                    continue
                c[2]+=1
                d1,d2,d3=V.generalized_weights(rows)
                if not (d1>=2 and d2>=4 and d3>=5):
                    continue
                c[3]+=1
                key=R.rowspace_key(rows)
                sd=dict(zip(sb,ds))
                states=tuple(V.DIR_MASK[sd[b]] if b in sd else 7 for b in touched)
                rel=V.relation_rows_int8(ext,touched,states,key)
                mx=max(mx,max(sum(x*x for x in row) for row in rel))
                j=R.rank_mod(rel)-rr
                inc[j]+=1
                assert j==0

    assert tuple(c)==(es,ed,er,eg)
    assert dict(inc)=={0:eg}
    assert mx==en
    assert R.lucas_lehmer_127()
    assert R.P*R.P>mx**15
    assert tuple(sum(v[2+j] for v in EXPECTED.values()) for j in range(4))==EXPECTED_TOTAL
    assert tuple(a+b+c for a,b,c in zip((25056,676512,515484,25812),(25056,676512,521964,25380),EXPECTED_TOTAL))==EXPECTED_FULL
    print("PASS",start,end,*c,dict(inc),mx)

if __name__=="__main__":
    main()
