# Target C: reduce the last seven-no-root `k=5` branch

Date: 2026-09-21

Status: rigorous structural reduction of the only remaining seven-no-root `k=5` arithmetic branch,

`D=-1, k=5, d=0, p=7`.

This note eliminates every synchronized six-row virtual-deficiency-one shadow and every virtual-deficiency-two shadow whose seven incomplete root rows are all singletons. The branch is reduced to exactly two root-row patterns:

1. five singleton blocks plus one pair block, with every fully synchronized six-row shadow having `(d_6,q_6)=(2,6)`; or
2. seven singleton blocks, with every fully synchronized six-row shadow having `(d_6,q_6)=(3,7)`.

Companion arithmetic checker:

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d0p7_reduction_2026_09_21.py`

The reduction uses only exact results already committed in the repository. It is not yet a closure of the branch.

## Starting point

After the exact closure of

`D=-2, k=5, d=0, p=6`,

the only seven-no-root `k=5` arithmetic branch left is

`D=-1, k=5, d=0, p=7`.

The rank-two coefficient-constraint space

`P <= Q^7`

satisfies the previously proved generalized-weight bounds

`d_1(P)>=2, d_2(P)>=4`.

A two-coordinate puncture lowers `rank(P)` exactly when `P` has a nonzero word supported on that coordinate pair. Two such rank-drop pairs cannot meet, because subtracting suitable multiples of the two support-two words would produce a support-one word. Three disjoint rank-drop pairs would force the rank-two code to contain three independent support-two directions. Thus the rank-drop pairs form a matching of size at most two.

Consequently at least three of the seven coordinates are incident to no rank-drop pair. Fix one such coordinate `i`.

Deleting `i` gives a six-no-root shadow with

- defect `D_6=1`;
- incomplete-root cost `p=7`;
- rank-two coefficient space; and
- every one-coordinate puncture still of rank two.

The synchronized six-row `k=4` containment theorem therefore applies.

Let `C_6` be its virtual canonical complete-block set, put

`d_6=|C_6|-rank H(C_6)`,

and let `q_6` be the number of blocks of `C_6` that are incomplete in the actual root state. The theorem gives

`1 >= 6 + 7 + 3 d_6 - 3 q_6`,

so

`q_6 >= d_6+4`.

Since `q_6<=7`, necessarily

`1<=d_6<=3`.

If `s_6` of the `q_6` replacements are singleton blocks, every other incomplete replacement costs at least two root rows. Hence

`7 >= s_6 + 2(q_6-s_6)=2q_6-s_6`,

or

`s_6 >= 2q_6-7`.

The complete arithmetic list is therefore

```text
d_6   q_6   minimum singleton replacements
 1     5                3
 1     6                5
 1     7                7
 2     6                5
 2     7                7
 3     7                7
```

## The `d_6=1` case is impossible

The exact synchronized six-row deficiency-one census is already committed in

`research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d1p4_2026_09_21.py`.

It contains exactly 31 synchronized `d_6=1` states. Their number of virtual-canonical complete blocks admitting a compatible singleton is

```text
capacity   states
0              1
2              6
3             24
```

so the maximum is three. The same exact census proves a stronger fact:

> every compatible singleton block in those 31 states is touched by exactly three of the six no-root cycles.

Therefore the `d_6=1` arithmetic list collapses to

`q_6=5, s_6=3`.

The root-row cost is then exactly

`3*1 + 2*2 = 7`.

Thus the actual root state has exactly five nonempty incomplete blocks:

- three singleton blocks; and
- two pair blocks.

There is no row budget for any additional nonempty incomplete block.

Now delete any one of the remaining six no-root coordinates `j`. Because the originally chosen coordinate `i` is incident to no rank-drop pair, the two-coordinate deletion `{i,j}` still leaves coefficient rank two. Its five-row defect is therefore

`D_5=3`.

Virtual complete sets only shrink under coefficient-space projection, so

`d_5<=d_6=1`.

The repaired five-row `k=3` theorem gives `d_5>=1`; hence every such five-row shadow has

`d_5=1`.

At `D_5=3,p=7,d_5=1`, the five-row containment inequality gives

`3 >= 5+7+3-3q_5`,

so

`q_5>=4`.

Since the six-row state has only the five nonempty incomplete blocks listed above, at most one of those five blocks may become virtual-canonical empty after deleting `j`.

Now use the exact five-row deficiency-one singleton census encoded in

`research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026_09_21.py`.

Across every five-row `d_5=1` virtual state, every virtual-canonical complete block admitting a compatible singleton is touched by exactly three of the five no-root cycles.

Take one of the three actual singleton blocks in the six-row shadow. It is touched by exactly three of the six external rows. Delete one of those three touching coordinates. Singleton compatibility projects to the five-row coefficient space. If the block remained virtual-canonical complete, it would be a compatible singleton block touched by only two of the remaining five rows, contradicting the exact five-row support census. Therefore:

> deleting a coordinate that touches one of the three singleton blocks forces that block to become virtual-canonical empty.

But at most one of the five nonempty incomplete blocks may become canonical-empty in any deletion. Hence each of the six coordinates can touch at most one of the three singleton blocks.

The three singleton blocks require

`3*3=9`

touch incidences, while six coordinates can supply at most

`6*1=6`.

Contradiction.

Therefore no synchronized six-row `d_6=1` shadow can arise from the target seven-row branch.

## The `d_6=2` arithmetic splits into two root patterns

The remaining `d_6=2` possibilities are

```text
q_6=6, s_6>=5
q_6=7, s_6=7.
```

If `q_6=6,s_6=5`, the row cost is already exactly seven, so the global root state consists of

- five singleton incomplete blocks; and
- one pair incomplete block.

Call this pattern B.

If `q_6=6,s_6=6`, the six singleton replacements cost six rows and the remaining one row must be one additional singleton incomplete block outside `C_6`. Thus all seven incomplete rows are singleton blocks.

If `q_6=7`, all seven replacements must also be singletons.

So every other `d_6=2` case has seven singleton incomplete blocks.

## All-singleton `d_6=2` is already excluded by the committed `d_6=2` census

Assume a synchronized six-row shadow has `d_6=2` and the global root state consists of seven singleton incomplete blocks.

Every one-coordinate projection has five-row virtual deficiency

`1<=d_5<=2`.

Its exact defect is again `D_5=3`, and all actual nonempty incomplete blocks are singletons.

If `d_5=1`, the five-row containment bound gives

`q_5>=4`.

That would require at least four virtual-canonical complete blocks admitting compatible singleton states. But the exact five-row deficiency-one capacity maximum is three. Thus

`d_5=1`

is impossible for every one of the six projections.

Hence all six projections must have

`d_5=2`.

For `d_5=2`, the same containment inequality gives

`q_5>=5`,

so every projected state has singleton capacity at least five. At the six-row level, `q_6>=6`, so the six-row singleton capacity is at least six.

These are exactly the structural hypotheses exhaustively audited by

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py`.

That exact search found

```text
six-row synchronized d_6=2 states        1,418
singleton capacity >=6                      761
all six projected five-row d_5=2              0
```

The search is independent of the seven-row `p=6` application for which it was first written: it enumerates the coefficient spaces and virtual canonical deficiency data themselves. Therefore the zero-survivor statement applies here as well.

So no `d_6=2` shadow with seven singleton incomplete blocks exists.

The only surviving `d_6=2` possibility is pattern B:

`five singleton blocks + one pair block`,

with

`q_6=6, d_6=2`.

## The `d_6=3` case

The six-row containment arithmetic forces

`d_6=3, q_6=7, s_6=7`.

Thus the global root state consists of exactly seven singleton incomplete blocks. Call this pattern C.

For every one-coordinate projection,

`1<=d_5<=3`.

The same five-row `d_5=1` capacity obstruction used above excludes `d_5=1`, because `D_5=3,p=7,d_5=1` requires at least four singleton replacements while the exact capacity maximum is three.

Therefore every five-row projection in pattern C has

`d_5 in {2,3}`.

Pattern C is not excluded by the currently committed finite censuses.

## Exact remaining state space

The target branch has now been reduced to exactly two global root patterns.

### Pattern B

```text
root incomplete state: 5 singletons + 1 pair
unmatched six-row shadow: d_6=2, q_6=6
```

Every five-row deletion of that six-row shadow has `d_5 in {1,2}`.

If `d_5=1`, then `q_5>=4`. Since there is only one pair block and five singleton blocks, and the exact `d_5=1` singleton capacity is at most three, the pair must remain virtual-complete and exactly three singleton blocks remain virtual-complete. Thus the five-row parent has singleton capacity exactly three. There are exactly

`12`

such `d_5=1` virtual states.

If `d_5=2`, then `q_5>=5`. Even when the pair remains virtual-complete this requires at least four compatible singleton blocks. The exact `d_5=2` capacity census is

```text
capacity   states
0              1
1            297
2            532
3          4,339
4          8,260
5            693
6          1,377
7             68
8            110
9             76
10            48
11            64
```

so there are exactly

`10,696`

`d_5=2` parents of capacity at least four.

Therefore every pattern-B six-row orbit is covered by extending only

`12 + 10,696 = 10,708`

five-row virtual states, rather than by scanning the full 535,040-state rank-two census or the 325,911 six-row cycle orbits blindly.

For each extension it is enough to enumerate synchronized rank-two `P_6`, retain `d_6=2` and singleton capacity at least five, and search for a common set of five singleton blocks plus one pair block satisfying the projected `q_5` thresholds. Only structural survivors require exact local-state realization and final `T`-space reranking.

### Pattern C

```text
root incomplete state: 7 singletons
unmatched six-row shadow: d_6=3, q_6=7
```

Every five-row deletion has `d_5 in {2,3}`.

A `d_5=2` parent needs at least five compatible singleton-complete blocks, so only the already-censused

`2,436`

five-row `d_5=2` states of capacity at least five can occur.

A `d_5=3` parent needs at least six compatible singleton-complete blocks. The next finite task is to add the exact `d_5=3` singleton-capacity census and extend only those capacity-at-least-six parents.

## Consequence

The seven-no-root `k=5` layer is not yet closed, but the last branch is no longer an unrestricted `p=7` search. Its synchronized six-row shadow must be one of two sharply specified types:

```text
B: d_6=2, q_6=6, root pattern 5 singleton + 1 pair
C: d_6=3, q_6=7, root pattern 7 singleton
```

The entire `d_6=1` layer and the all-singleton part of `d_6=2` are excluded.

The next exact computation should attack pattern B first using the 10,708-parent cover above, because every required parent class is already completely classified. Pattern C then requires only one new five-row statistic: the `d_5=3` singleton-capacity-at-least-six census.

The direct C-II endpoint remains unchanged at

`3874 = 3076 C7 + 798 (C3 disjoint-union C4)`.
