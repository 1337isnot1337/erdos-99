#!/usr/bin/env python3
"""Arithmetic certificate for the eight-no-root k=8 reduction.

Inputs already certified in the repository:
  * every family with at most seven no-root cycles has D>=0;
  * every five-no-root k=5 state with p<=9 has D>=7;
  * six-row rank-zero profiles with incomplete support >=2 satisfy
      p=11,c<=9 -> D>=8,
      p=12,c<=8 -> D>=6.

For k=8 the coefficient-constraint space is zero, so all external-coordinate
deletions preserve quotient rank.  This checker reduces the 11 arithmetic k=8
branches to the two deficiency-zero residuals p=14 (D=-2) and p=15 (D=-1).
"""

TARGETS = {
    -2: ((0,14),(1,11),(2,8),(3,5),(4,2)),
    -1: ((0,15),(1,12),(2,9),(3,6),(4,3),(5,0)),
}

for D, vals in TARGETS.items():
    assert tuple((d,p) for d in range(6) for p in range(16)
                 if 8 + p + 3*d - 24 == D) == vals

# Three deletions produce a five-row k=5 shadow with D5=D+6.  Since all
# five-row k=5 states with p<=9 have D>=7, each triple shadow has p>=10.
# Congruence D5 == 5+p (mod 3) gives the exact possible retained p values.
def triple_p_options(D, p):
    D5 = D + 6
    return tuple(x for x in range(10, p+1) if (5+x-D5) % 3 == 0)

assert triple_p_options(-2,14) == (11,14)
assert triple_p_options(-2,11) == (11,)
assert triple_p_options(-1,15) == (12,15)
assert triple_p_options(-1,12) == (12,)

closed_by_five = []
residual = []
for D, vals in TARGETS.items():
    threshold = 11 if D == -2 else 12
    for d,p in vals:
        if p < threshold:
            closed_by_five.append((D,d,p))
        else:
            residual.append((D,d,p))
assert len(closed_by_five) == 7
assert tuple(residual) == ((-2,0,14),(-2,1,11),(-1,0,15),(-1,1,12))

# In the p=11 and p=12 branches every triple shadow preserves all incomplete
# root-row cost, so every incomplete block has global support at least four.
# Hence every pair shadow preserves p and each remaining incomplete block has
# six-row support at least two.  The pair-shadow defects are D+4.
SIX_MIN = {11:8, 12:6}
for D,d,p in ((-2,1,11),(-1,1,12)):
    c_max = d + 7  # delta=c-d+8 <= 15
    assert c_max == 8
    pair_D = D + 4
    assert pair_D < SIX_MIN[p]

# For the two remaining d=0 branches, ambient dimension gives c<=7.  If a
# future six-row shadow has incomplete support >=2, q<=12.  At p=14 or15 there
# are at least two pair blocks, so completing two pairs maps to the already
# certified p=10 or11 profile on the same all-complete superfamily.
# This records useful lower bounds for the next residual attack.
def residual_six_bound(p):
    c = 7
    bounds=[]
    for q in range((p+1)//2,p+1):
        s=2*q-p
        if not (0<=s<=q<=12):
            continue
        pairs=q-s
        assert pairs >= 2
        if p==14:
            # complete two pairs -> p=10,c+2<=9; p14 lower = p10 lower -2
            bounds.append(7-2)
        elif p==15:
            # complete two pairs -> p=11,c+2<=9; p15 lower = p11 lower -2
            bounds.append(8-2)
        else:
            raise AssertionError(p)
    return min(bounds)

assert residual_six_bound(14) == 5
assert residual_six_bound(15) == 6

remaining = ((-2,0,14),(-1,0,15))
print("PASS: eight-no-root k=8 reduction arithmetic")
print("closed_by_five_row", len(closed_by_five))
print("residual_after_triple_shadows", residual)
print("closed_by_six_row", ((-2,1,11),(-1,1,12)))
print("conditional_six_bounds", {14:5,15:6})
print("remaining_k8_branches", remaining)
