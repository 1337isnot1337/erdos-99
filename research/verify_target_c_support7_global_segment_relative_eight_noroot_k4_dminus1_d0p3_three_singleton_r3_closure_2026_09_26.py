#!/usr/bin/env python3
"""Exact support certificate closing the r=3 weight-two-line subcase."""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_support_closure_2026_09_26 as B

SHARDS=((0,5000),(5000,10000),(10000,15000),(15000,20000),(20000,25000),(25000,27763))
EXPECTED_H20=(4633,2628,2451,1370,1691,801)

def matchings3():
    out=[]
    for U in combinations(range(8),2):
        rest=tuple(x for x in range(8) if x not in U)
        def rec(items):
            if not items:
                yield (); return
            a=items[0]
            for k in range(1,len(items)):
                b=items[k]; tail=items[1:k]+items[k+1:]
                for m in rec(tail): yield ((a,b),)+m
        for m in rec(rest):
            out.append((tuple(sorted(tuple(sorted(p)) for p in m)),tuple(U)))
    assert len(out)==len(set(out))==420
    return tuple(out)
MATCHINGS=matchings3()

def mask_of(occ):
    return occ if isinstance(occ, int) else sum(1<<i for i in occ)

def sharp_survival(mask,pairs):
    return all((mask & ~((1<<a)|(1<<b))).bit_count()>=2 for a,b in pairs)

def virtual_survivor(data,pairs,U):
    T=tuple(sorted(data)); rank_T=B.tri_rank(T)
    pm=tuple((1<<a)|(1<<b) for a,b in pairs); um=(1<<U[0])|(1<<U[1])
    E=set(); S=set(); small=set()
    for b,(occ,dim,n) in data.items():
        mask=mask_of(occ)
        if (dim==1 and ((n==2 and mask in pm) or n>=3)) or (dim==2 and n>=4):
            E.add(b)
        if sharp_survival(mask,pairs) and ((dim==1 and n>=2) or (dim==2 and n>=4)):
            S.add(b)
            if dim==1 and n==2:
                assert mask==um
                small.add(b)
    if len(S)<3: return None
    C0=set(T)-E
    for sing in combinations(sorted(S),3):
        ss=set(sing)
        if len(ss&small)>1: continue
        C=tuple(sorted(C0-ss))
        if B.tri_rank(C)!=len(C): continue
        if rank_T-B.tri_rank(C)<4: continue
        dim=sum(data[b][1] for b in E if b not in ss)+sum(data[b][1]==2 for b in ss)
        if dim<4: continue
        cover=0
        for b in E:
            if b not in ss: cover |= mask_of(data[b][0])
        for b in ss:
            if data[b][1]==2: cover |= mask_of(data[b][0])
        if cover.bit_count()<7: continue
        return (tuple(sorted(E)),sing,C,dim,cover)
    return None

def run_shard(reps,s):
    a,z=SHARDS[s]; C=Counter(); survivors=[]
    for i in range(a,z):
        data=B.block_data(reps[i]); C['orbits']+=1
        if len(data)>20: continue
        C['h20']+=1
        for pairs,U in MATCHINGS:
            C['tests']+=1
            w=virtual_survivor(data,pairs,U)
            if w is not None:
                survivors.append((i,reps[i],pairs,U,w)); break
        if survivors: break
    assert C['orbits']==z-a,C
    assert C['h20']==EXPECTED_H20[s],C
    assert C['tests']==EXPECTED_H20[s]*420,C
    assert not survivors,survivors
    return C

def main():
    ap=ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(6)); args=ap.parse_args()
    assert B.lucas_lehmer_31()
    assert B.MOD*B.MOD>3**15
    reps=B.support_multiset_orbits(); assert len(reps)==27763
    shards=range(6) if args.shard is None else (args.shard,)
    total=Counter()
    for s in shards:
        C=run_shard(reps,s); total.update(C)
        print('shard',s,'range',SHARDS[s],'h_le_20',C['h20'],'support_matching_pairs',C['tests'],'virtual_survivors',0)
    if args.shard is None:
        assert total['orbits']==27763 and total['h20']==13574 and total['tests']==5701080
        print('PASS: r=3 three-weight-two-line subcase closed')
        print('support_multiset_orbits_size_8',total['orbits'])
        print('touch_at_most_20',total['h20'])
        print('three_pair_matchings',len(MATCHINGS))
        print('support_matching_pairs_tested',total['tests'])
        print('virtual_survivors',0)
        print('hadamard_exact_rank_bound',B.MOD*B.MOD>3**15)
if __name__=='__main__': main()
