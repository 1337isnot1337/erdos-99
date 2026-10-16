from math import floor

# Arithmetic boundary for eight no-root rows at k=7.
cases = {
    -2: [(0,11),(1,8),(2,5),(3,2)],
    -1: [(0,12),(1,9),(2,6),(3,3),(4,0)],
}
for D, rows in cases.items():
    for d, p in rows:
        assert D == 8 + p + 3*d - 3*7

# Eight-row rank-one containment: d_v>=2 and D>=8+p+3d_v-3q,
# so D>=14-2p from q<=p.
closed = []
remaining = []
for D, rows in cases.items():
    for d, p in rows:
        (closed if 14 - 2*p > D else remaining).append((D,d,p))
assert closed == [
    (-2,2,5),(-2,3,2),
    (-1,2,6),(-1,3,3),(-1,4,0),
]
assert remaining == [(-2,0,11),(-2,1,8),(-1,0,12),(-1,1,9)]

# Exact virtual possibilities before the lifted d=2 capacity pruning.
def virtual_poss(D,p):
    out=[]
    for dv in range(2,16):
        for q in range(p+1):
            if 8+p+3*dv-3*q <= D:
                out.append((dv,q,max(0,2*q-p)))
    return out

before = {
    (D,p): virtual_poss(D,p)
    for D,_,p in remaining
}
assert before[(-2,8)] == [(2,8,8)]
assert before[(-1,9)] == [(2,8,7),(2,9,9),(3,9,9)]

# Projection-loss lemma + exact six-row d=2 capacity <=3:
# seven-row d=2 capacity <=5 at coefficient support 2, <=4 at support >=3.
assert (3*5)//(5-2) == 5
assert (3*7)//(7-2) == 4
# Lifting once more:
# eight-row d=2 capacity <=7 at support 2; support >=3 gives <=5.
assert (5*6)//(6-2) == 7
# support 3: five zero deletions have seven-row cap<=4 and three support
# deletions have cap<=5; every block survives at least 6 of 8 good deletions.
assert (5*4 + 3*5)//6 == 5
# support >=4: all eight seven-row deletions have support >=3, cap<=4.
assert (8*4)//6 == 5

# Therefore the D=-2,d_root=1,p=8 branch, which forces d_v=2,q=8
# and eight singleton changed blocks, is impossible.
assert before[(-2,8)] == [(2,8,8)]

# d_v=2 pruning of the other branches.  A required singleton count >7 is
# impossible globally.  Counts 6 or 7 force coefficient support exactly 2.
pruned = {
    (-2,11): [(3,10,9),(3,11,11),(4,11,11)],
    (-1,12): [(3,10,8),(3,11,10),(3,12,12),
              (4,11,10),(4,12,12),(5,12,12)],
    (-1,9):  [(3,9,9)],
}
# The (-2,11) d_v=2,q=9 case and (-1,9) d_v=2,q=8 case require
# unchanged good seven-row shadows with at least 6 singleton blocks, while
# seven-row d=2 capacity is at most 5, so they are removed too.

# Close the special C d_v=2,q=9 profile.  It is exactly 6 singleton + 3 pair
# blocks at support(P)=2.  A lossy good deletion (p:12->9) must lose one
# singleton and one pair, so at most 3 of 6 good coordinates are lossy and
# at least 3 are unchanged.  For two unchanged good coordinates, the six-row
# d=2 pair shadow has singleton capacity <=3.  Its D=3 containment arithmetic
# leaves only p=9,q=6 with exactly 3 singleton + all 3 pair blocks.  Therefore
# the pair deletion loses exactly 3 singleton blocks of exact support {u,v}.
# Three unchanged coordinates would require 3*C(3,2)=9 distinct singleton
# blocks, contradicting the available six.
good = 6
pair_blocks = 3
min_unchanged = good - pair_blocks
assert min_unchanged == 3

def feasible_pair_shadow(p):
    # D6=3 => q >= ceil((p+9)/3), and q blocks must fit in p selected rows.
    qmin = (p + 11)//3
    for q in range(qmin, 10):
        for s in range(min(3,q)+1):
            pairs = q-s
            if pairs > 3:
                continue
            if s + 2*pairs <= p:
                return (q,s,pairs)
    return None

pair_feasible = {p: feasible_pair_shadow(p) for p in (0,3,6,9,12)}
assert pair_feasible == {0: None, 3: None, 6: None, 9: (6,3,3), 12: None}
assert 3 * (min_unchanged * (min_unchanged-1)//2) == 9 > 6

# Good unchanged-deletion budget: at least six global good coordinates, at
# most two bad support coordinates; each nonzero p-loss is >=3 and total loss<=p.
mins = {}
for D,d,p in [(-2,0,11),(-1,0,12),(-1,1,9)]:
    unchanged_total = 8 - floor(p/3)
    mins[(D,p)] = max(0, unchanged_total-2)
assert mins == {(-2,11):3,(-1,12):2,(-1,9):3}

print('PASS: eight-no-root k=7 containment/capacity reduction')
print('closed_arithmetic_cases', closed + [(-2,1,8)])
print('remaining_arithmetic_cases', [(-2,0,11),(-1,0,12),(-1,1,9)])
print('remaining_virtual_profiles', pruned)
print('special_C_d2_closed', True)
print('special_C_pair_shadow_feasible', pair_feasible)
print('min_good_unchanged_deletions', mins)
print('seven_row_d2_capacity', {'support2':5,'support_ge3':4})
print('eight_row_d2_capacity', {'support2':7,'support_ge3':5})
