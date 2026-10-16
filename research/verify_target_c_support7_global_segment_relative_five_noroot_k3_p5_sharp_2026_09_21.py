#!/usr/bin/env python3
"""Exact sharp boundary audit for five-no-root k=3,p=5.

Using D >= 5+p+3*d-3*q = 10+3*d-3*q, the only class that
could lie below D=1 is d=1,q=5.  The d=1 virtual states admit at most
three compatible canonical-complete singleton blocks, so that class is empty.
For the D=1 boundary it remains to exactify d=1,q=4 and d=2,q=5.
The result is D>=1 uniformly, with exactly 6,445 canonical D=1 cores, all
of type d=2,q=5 with five singleton replacements.
"""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_five_noroot_k3_p4_sharp_2026_09_21.py"
spec = importlib.util.spec_from_file_location("five_k3_p4_for_p5", BASE)
P4 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P4)

C=P4.C; R=P4.R; P0=P4.P0; K=P4.K; MOD=P4.MOD

EXPECTED_D1_CAPACITY={0:71,2:3,3:12}
EXPECTED_COUNTS={
    ("pair+3sing_d1_q4","exact"):144,
    ("5sing_d2_q5","exact"):67515,
    ("5sing_d2_q5","not_realize_P"):268,
}
EXPECTED_DEFECTS={
    ("pair+3sing_d1_q4",7):144,
    ("5sing_d2_q5",1):6445,
    ("5sing_d2_q5",4):35573,
    ("5sing_d2_q5",7):17156,
    ("5sing_d2_q5",10):8175,
    ("5sing_d2_q5",13):166,
}
EXPECTED_D1_RANKS={(3,6):41,(4,7):340,(5,8):2992,(6,9):3072}


def scan(start,stop):
    keys,orbits,orbit_sizes,augmentation_candidates=K.five_no_root_orbits()
    assert len(orbits)==20451 and sum(orbit_sizes)==96560646 and augmentation_candidates==20475
    key_to_global={K.cycle_key(R.DESC[e]):e for e in R.NO_ROOT}
    rank_cache={}; base_census=Counter(); d1_capacity=Counter(); d1_support=Counter()
    counts=Counter(); defects=Counter(); d1_ranks=Counter(); spaces=0; max_norm2=0; first_below_one=None
    for oi in range(start,stop):
        ext=tuple(key_to_global[keys[i]] for i in orbits[oi])
        touched=tuple(sorted(b for b in range(35) if any(R.QCOMP[e][b]!=(0,0) for e in ext)))
        pos={b:i for i,b in enumerate(touched)}
        for P,min_sgen in C.candidate_spaces(ext,touched):
            spaces+=1
            base=C.virtual_canonical(ext,touched,P)
            complete=tuple(b for b,s in zip(touched,base) if s==7)
            basis=rank_cache.get(complete)
            if basis is None:
                basis=C.rref_basis_mod([P0.COMPLETE_T[b] for b in complete]);rank_cache[complete]=basis
            d=len(complete)-len(basis);base_census[(min_sgen,d)]+=1
            if d not in (1,2):continue
            opts={b:P4.compatible_singletons(ext,b,P) for b in touched}
            sigs=set()
            if d==1:
                good=[b for b in complete if opts[b]]
                d1_capacity[len(good)]+=1
                for b in good:
                    d1_support[sum(R.QCOMP[e][b]!=(0,0) for e in ext)]+=1
                # d=1,q=5 would require five singleton-compatible complete
                # blocks and d=1,q=4 with five singleton incompletes would
                # require four.  Both are excluded by the capacity <=3 census.
                # The only remaining sharp q=4 form is one pair plus three
                # singleton replacements, all on canonical-complete blocks.
                for singles in combinations(good,3):
                    for pair_block in complete:
                        if pair_block in singles:continue
                        for singleton_states in product(*(opts[b] for b in singles)):
                            for pair_state in (3,5,6):
                                states=list(base);states[pos[pair_block]]=pair_state
                                for b,s in zip(singles,singleton_states):states[pos[b]]=s
                                sigs.add(("pair+3sing_d1_q4",tuple(states)))
            else:
                # The only d=2 class on the D=1 containment boundary is q=5,
                # forcing five singleton replacements.
                good=[b for b in complete if opts[b]]
                for blocks in combinations(good,5):
                    for singleton_states in product(*(opts[b] for b in blocks)):
                        states=list(base)
                        for b,s in zip(blocks,singleton_states):states[pos[b]]=s
                        sigs.add(("5sing_d2_q5",tuple(states)))
            for kind,states in sigs:
                if P4.actual_space(ext,touched,states)!=P:
                    counts[(kind,"not_realize_P")]+=1;continue
                rows=P0.relation_rows(ext,touched,states,P)
                for row in rows:max_norm2=max(max_norm2,sum(x*x for x in row))
                delta=R.rank_mod(rows);n=5+sum(R.STATES[s][1] for s in states);D=n-3*delta
                counts[(kind,"exact")]+=1;defects[(kind,D)]+=1
                if D<1 and first_below_one is None:first_below_one=(oi,kind,D,ext,P,states)
                if D==1:d1_ranks[(sum(s==7 for s in states),delta)]+=1
    return dict(spaces=spaces,base_census=base_census,d1_capacity=d1_capacity,d1_support=d1_support,
                counts=counts,defects=defects,d1_ranks=d1_ranks,max_norm2=max_norm2,
                first_below_one=first_below_one,rank_cache=len(rank_cache))


def main():
    ap=ArgumentParser();ap.add_argument('--orbit-start',type=int,default=0);ap.add_argument('--orbit-end',type=int);args=ap.parse_args()
    assert R.lucas_lehmer_127()
    _,orbits,_,_=K.five_no_root_orbits();end=len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0<=args.orbit_start<=end<=len(orbits)
    z=scan(args.orbit_start,end);assert z['first_below_one'] is None,z['first_below_one']
    assert MOD*MOD>max(1,z['max_norm2'])**15
    if args.orbit_start==0 and end==len(orbits):
        assert z['spaces']==535040
        assert dict(sorted(z['base_census'].items()))==C.EXPECTED
        assert dict(sorted(z['d1_capacity'].items()))==EXPECTED_D1_CAPACITY
        assert dict(z['d1_support'])=={3:42}
        assert dict(z['counts'])==EXPECTED_COUNTS
        assert dict(z['defects'])==EXPECTED_DEFECTS
        assert dict(sorted(z['d1_ranks'].items()))==EXPECTED_D1_RANKS
        assert sum(z['d1_ranks'].values())==6445
        assert z['max_norm2']==44
    print('PASS: five-no-root k=3,p=5 sharp boundary')
    print('orbit_range',args.orbit_start,end)
    print('rank2_virtual_states',z['spaces'])
    print('d1_singleton_capacity_census',dict(sorted(z['d1_capacity'].items())))
    print('replacement_census',dict(sorted(z['counts'].items())))
    print('exact_defect_census',dict(sorted(z['defects'].items())))
    print('D1_core_rank_census',dict(sorted(z['d1_ranks'].items())))
    print('D1_canonical_cores',sum(z['d1_ranks'].values()))
    print('max_relation_row_norm_squared',z['max_norm2'])
    print('hadamard_exact_rank_bound',MOD*MOD>max(1,z['max_norm2'])**15)

if __name__=='__main__':main()
