# Target C: exact closure of the `d_6=3` side of `C:(4,11,10)`

Date: 2026-09-21

Status: exact finite closure of the `d_6=3` good-pair-shadow subcase for the remaining eight-no-root `k=7` profile

```text
C: D=-1, p=12, (d_v,q,s)=(4,11,10).
```

Companion verifier:

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d3_exact_profile_2026_09_21.py`

This strengthens the preceding structural extension scan

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d3_pair_extension_2026_09_21.py`

by reranking every structural survivor in the exact ten-singleton-plus-one-pair root profile.

## 1. Structural screen

The committed good-pair reduction supplies a `p=12`-retaining synchronized six-row `k=5` shadow.  In the `d_6=3` subcase the containment bound forces singleton capacity at least seven.  The exact six-row census has 402 such states:

```text
capacity 7:   78
capacity 8:  116
capacity 9:  144
capacity 10:  64
----------------
total:       402
```

For each state, restore either deleted cycle.  The existing six-to-seven obstruction removes `d_7=3`, so any relevant one-cycle lift must have

```text
d_7=4,
singleton capacity >= 9.
```

Combining every compatible pair of one-cycle lifts and requiring global

```text
d_8=4,
singleton capacity >= 10
```

gives the following exact aggregate over four disjoint base-state ranges:

```text
pair extensions tested:  1,035,136
global d_8=4 states:         27,076

capacity 6:   2,132
capacity 7:   9,107
capacity 8:   9,414
capacity 9:   5,499
capacity 10:    924
```

Thus capacity alone does not close this branch: there are exactly 924 structural survivors, all at capacity ten.

## 2. Exact target-profile rerank

The target profile has exactly ten singleton changed virtual-complete blocks and one pair changed virtual-complete block.  Every one of the 924 structural survivors has exactly ten singleton-compatible blocks, and every such block has exactly one compatible singleton orientation.

For each survivor the exact verifier therefore exhausts:

1. the forced singleton state on each of those ten blocks;
2. every possible pair block among the other virtual-complete blocks;
3. all three two-row pair states, masks `3`, `5`, and `6`.

The candidate-pair-block census is

```text
7 pair-block choices: 594 structural survivors
8 pair-block choices: 330 structural survivors
```

so the exact number of actual root profiles tested is

```text
594 * 7 * 3 + 330 * 8 * 3 = 20,394.
```

All 20,394 states reproduce the required rank-one external constraint line.  The relative `T`-rank is then recomputed from the actual selected rows.  The exact defect census is

```text
D = |A| - 3*delta(A)

17: 20,394 states
```

There are zero states with `D<=-1`.  Since the branch being tested requires `D=-1`, none of the 924 structural survivors is an actual counterexample state.

Therefore:

> The `d_6=3` good-pair-shadow subcase of `C:(4,11,10)` is impossible.

## 3. Exact rank certificate

The actual-profile relation matrices have at most 14 rows, and the maximum squared row norm observed in the exhaustive rerank is 24.  Ranks are computed modulo

```text
P = 2^127 - 1.
```

The imported verifier certifies `P` prime by Lucas-Lehmer.  The computation also checks

```text
P^2 > 24^15,
```

which is stronger than needed for every determinant encountered.  By Hadamard's inequality, a nonzero rational minor cannot vanish modulo `P`; the modular ranks used in the defect census are therefore exact over `Q`.

## 4. Remaining `C:(4,11,10)` bottleneck

The only remaining good-pair-shadow deficiency for this profile is `d_6=4`.

The committed singleton-plus-pair functional audit shows that the coarse functional threshold is sharp: there are six-row `d_6=4` states whose ten singleton replacements plus one pair replacement gain the required nine relative directions.  Hence the same capacity/functional argument cannot close this side by itself.

The next target is to impose the full two-cycle restoration/global consistency conditions on those equality witnesses, analogously to the exactification above, rather than treating the six-row functional witnesses in isolation.

The separate all-singleton profile

```text
C:(d_v,q,s)=(5,12,12)
```

also remains split into its `d_6=3` pair-extension audit and its `d_6=5` singleton-functional audit.
