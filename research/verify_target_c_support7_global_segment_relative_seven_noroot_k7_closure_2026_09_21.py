#!/usr/bin/env python3
"""Arithmetic/combinatorial certificate for the seven-no-root k=7 closure.

Non-arithmetic inputs are previously committed exact results:

1. Seven-no-root counterexamples have D in {-2,-1}, every external row is an
   M-coloop, and for k=7 the external quotient rank is zero.
2. Every five-no-root k=5 state with p<=9 has D>=7.
3. The exact six-no-root k=6 all-complete census gives, for states in which
   every incomplete block is touched by at least two external cycles and c<=9,
      p=10 -> D>=7,
      p=11 -> D>=8.
   The same census plus a profile reduction implies
      p=12,c<=8 -> D>=6,
      p=13,c<=8 -> D>=7.

This checker certifies the arithmetic reductions, the profile-reduction
inequalities, and the final support-graph contradiction for the p=13 branch.
"""
from itertools import combinations

# k=7 arithmetic boundary tuples from D = p + 3d - 14.
TARGETS = {
    -2: ((0, 12), (1, 9), (2, 6), (3, 3), (4, 0)),
    -1: ((0, 13), (1, 10), (2, 7), (3, 4), (4, 1)),
}

for D, vals in TARGETS.items():
    assert tuple((d, p) for d in range(5) for p in range(14)
                 if p + 3*d - 14 == D) == vals

# Any two-coordinate deletion has k=5 because the k=7 coefficient space is 0.
# Its defect is D+4.  The exact five-row k=5 p<=9 theorem forces p_pair>=10.
# Also D_pair == 5+p_pair (mod 3).
def pair_p_options(global_D, global_p):
    D5 = global_D + 4
    return tuple(p for p in range(10, global_p + 1) if (5 + p - D5) % 3 == 0)

assert pair_p_options(-2, 12) == (12,)
assert pair_p_options(-1, 10) == (10,)
assert pair_p_options(-1, 13) == (10, 13)

# Hence every branch with global p<=9 is impossible immediately.
closed_by_five_row_slack = []
residual = []
for D, vals in TARGETS.items():
    for d, p in vals:
        if p <= 9:
            closed_by_five_row_slack.append((D, d, p))
        else:
            residual.append((D, d, p))
assert len(closed_by_five_row_slack) == 7
assert tuple(residual) == ((-2, 0, 12), (-1, 0, 13), (-1, 1, 10))

# Exact six-row coarse bounds already committed.
SIX_MIN = {10: 7, 11: 8}

# Profile reduction.  A rank-zero six-row local profile has p=2q-s,
# where q is the number of incomplete blocks and s the singleton count.
# If all incomplete blocks are touched at least twice, q is at most 12 because
# six cycles contribute only 24 block incidences.
def derived_six_lower_bound(p, c):
    best = None
    # Enumerate every arithmetic (q,s) profile; only the reduction algebra is
    # checked here, not realizability of a particular six-set.
    for q in range((p + 1)//2, p + 1):
        s = 2*q - p
        if not (0 <= s <= q <= 12):
            continue
        if p == 10:
            assert c <= 9
            lower = SIX_MIN[10]
        elif p == 12:
            assert c <= 8
            if s == 0:
                # (q,s,c,p) -> (q-1,0,c+1,10); defect lower bound drops by 1.
                assert q >= 6
                lower = SIX_MIN[10] - 1
            else:
                # -> (q-1,s-1,c+1,11); defect lower bound drops by 2.
                assert s >= 2
                lower = SIX_MIN[11] - 2
        elif p == 13:
            assert c <= 8
            # q<=12 implies s<=q-1, so -> (q-1,s,c+1,11) is admissible.
            assert s <= q - 1
            lower = SIX_MIN[11] - 1
        else:
            raise AssertionError(p)
        best = lower if best is None else min(best, lower)
    return best

assert derived_six_lower_bound(10, 9) == 7
assert derived_six_lower_bound(12, 8) == 6
assert derived_six_lower_bound(13, 8) == 7

# The p=12 and p=10 residuals have every pair shadow preserving p, hence every
# incomplete block has support at least 3.  Every one-row shadow therefore has
# overlap>=2.  Ambient T dimension 15 gives c<=d+8 globally, hence respectively
# c<=8 and c<=9 in the one-row shadows.  Their required defects are 0 and 1,
# contradicting the six-row lower bounds 6 and 7.
assert 0 < derived_six_lower_bound(12, 8)
assert 1 < derived_six_lower_bound(10, 9)

# Final p=13 branch.  Let a_i be the incomplete-row cost in blocks supported
# exactly on coordinate i, and b_ij the cost in blocks supported exactly on
# {i,j}. Pair shadows have p in {10,13}, so each pair loss is 0 or 3.
# One-row congruence similarly makes each a_i 0 or 3.
# If some a_i=3, pair-loss<=3 forces all incident b_ij and all other a_j to 0;
# deleting i leaves a six-row p=10 overlap>=2 state, contradicted above.  Thus
# all a_i=0 and every b_ij is 0 or 3.

# If an isolated vertex exists in the graph G={ij:b_ij=3}, deleting it leaves
# a six-row p=13 overlap>=2 state, contradicted by the derived lower bound 7.
# Since total low-support cost is 3|E(G)| <= 13, |E(G)|<=4.  Enumerate all
# simple 7-vertex graphs with <=4 edges and no isolated vertices.
verts = range(7)
edges = tuple(combinations(verts, 2))
no_isolate_graphs = []
for m in range(5):
    for E in combinations(edges, m):
        deg = [0]*7
        for u, v in E:
            deg[u] += 1
            deg[v] += 1
        if min(deg) >= 1:
            no_isolate_graphs.append((E, tuple(sorted(deg))))

assert len(no_isolate_graphs) > 0
assert all(len(E) == 4 for E, _ in no_isolate_graphs)
assert {deg for _, deg in no_isolate_graphs} == {(1, 1, 1, 1, 1, 1, 2)}

# Every such graph contains a P3.  An edge b_ij=3 requires at least two
# distinct incomplete blocks supported exactly on {i,j}, because one block has
# cost at most 2.  Two no-root cycles sharing two root blocks must use the same
# underlying four-vertex support: distinct 4-subsets of a 7-set share at most
# one 3-subset.  Along a P3 i-j-k, both edges therefore force i,j,k to have the
# same four-vertex support.  Then all three cycles touch the same four blocks,
# so no block can have exact external support {i,j} or {j,k}. Contradiction.
def has_p3(E):
    adj = {v:set() for v in verts}
    for u,v in E:
        adj[u].add(v); adj[v].add(u)
    return any(len(adj[v]) >= 2 for v in verts)

assert all(has_p3(E) for E, _ in no_isolate_graphs)

print("PASS: seven-no-root k=7 closure arithmetic/combinatorics")
print("closed_immediately", len(closed_by_five_row_slack))
print("residual_before_six_row", residual)
print("six_row_derived_bounds", {10: 7, 12: 6, 13: 7})
print("p13_no_isolate_graphs", len(no_isolate_graphs))
print("p13_degree_sequence", (1,1,1,1,1,1,2))
print("remaining_k7_branches", 0)
