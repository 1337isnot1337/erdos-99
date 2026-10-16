#!/usr/bin/env python3
from itertools import combinations

COORDS = tuple(range(8))
MATCHING = ((0,1),(2,3),(4,5),(6,7))

def sharp_allowed(support, active_pairs):
    S=set(support)
    for M in active_pairs:
        M=set(M)
        for j in set(COORDS)-M:
            if S <= M|{j}:
                return False
    return True

# A sharp singleton quotient cannot have a weight-one representative.
# A weight-two representative must be wholly unmatched.
for r in range(1,5):
    active=MATCHING[:r]
    U=set(COORDS)-set().union(*map(set,active))
    for q in (1,2):
        for S in combinations(COORDS,q):
            allowed=sharp_allowed(S,active)
            expected=(q==2 and set(S)<=U)
            assert allowed==expected,(r,S,allowed,expected)

# Exhaust the rank-two t=3 case. The d1>=2 and quotient-distance>=2
# bounds force direction profile 1+1+1. For each choice of selected
# direction, the two nonselected-direction quotient rows have two
# different 2-supports. No such pair is sharp when r>=3.
t3_tests=0
for r in (3,4):
    active=MATCHING[:r]
    for T in combinations(COORDS,3):
        T=set(T)
        for selected in tuple(T):
            other=tuple(T-{selected})
            q1=T-{other[0]}
            q2=T-{other[1]}
            t3_tests+=1
            assert not (
                sharp_allowed(q1,active)
                and sharp_allowed(q2,active)
            )

# Perfect-matching rank-two singleton profiles. m_s is the selected
# direction multiplicity; m_1,m_2 are the unordered other multiplicities.
profiles={}
for t in range(1,9):
    out=[]
    for ms in range(5):
        for m1 in range(5):
            for m2 in range(m1,5):
                if ms+m1+m2!=t:
                    continue
                if t-ms<2 or (t-ms)%2:
                    continue
                if t-m1<3 or t-m2<3:
                    continue
                out.append((ms,m1,m2))
    profiles[t]=tuple(out)

assert profiles[1]==profiles[2]==profiles[3]==()
assert profiles[4]==((2,1,1),)
assert profiles[5]==((1,2,2),(3,0,2),(3,1,1))

def pair_index(x):
    return next(i for i,M in enumerate(MATCHING) if x in M)

def active_pair_count(S):
    return len({pair_index(x) for x in S})

# In the t=4 perfect-matching case the two nonselected touches support L
# and therefore form one matched pair. Each quotient representative has
# three coordinates and must be active in at least three matched-pair
# quotient summands. The two selected-direction touches are consequently
# in two distinct other matched pairs.
valid=[]
for a,b in combinations(COORDS,2):
    if pair_index(a)!=pair_index(b):
        continue
    rest=[x for x in COORDS if x not in (a,b)]
    for s1,s2 in combinations(rest,2):
        if active_pair_count({s1,s2,b})<3:
            continue
        if active_pair_count({s1,s2,a})<3:
            continue
        valid.append((a,b,s1,s2))
        assert pair_index(s1)!=pair_index(s2)
        assert pair_index(s1)!=pair_index(a)
        assert pair_index(s2)!=pair_index(a)

assert valid

print("PASS: weight-two unmatched-support localization")
print("rank2_t3_tests_r3_r4", t3_tests)
print("perfect_matching_rank2_t4_profile", profiles[4])
print("perfect_matching_t4_pair_placements", len(valid))
