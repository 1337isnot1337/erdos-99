# Target C: fixed nine-block basis constraint for the remaining `k=6, D=-1` Profile B

Date: 2026-09-22

Status: proved a stronger necessary condition and implemented it as an exact rational wrapper around the direct global-lift audit. No closure is claimed until the finite cover executes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_fixed_nine_basis_2026_09_22.py`

## 1. The looseness in the previous global lift

The direct global Profile B lift requires

```text
eight rows: d_8 = 3, compatible singleton span = 9;
seven rows: d_7 = 3, compatible singleton span = 8;
six-row clean fan: d_6 = 3, compatible singleton span = 7.
```

Those are necessary conditions, but the previous verifier allowed the spanning singleton blocks to be chosen independently at the three levels. A genuine Profile B does not have that freedom. Its global profile has exactly nine changed blocks and all nine are singleton replacements.

For a rank-two coefficient plane on `t` rows with virtual deficiency `d`, the replacement-functional quotient has dimension

```text
s_t = t - 2 + d.
```

Thus Profile B has dimensions `9,8,7` at the eight-, clean seven-, and clean six-row levels. Every five-row puncture of a synchronized six-row Profile B state has `d_5 in {2,3}`, hence quotient dimension `5` or `6`.

## 2. Fixed-nine-block basis lemma

Let `b_1,...,b_9` be the nine actual singleton replacement blocks of a genuine eight-row Profile B state and let `v_j` be their replacement-functional classes in the eight-row quotient `V_8`.

The actual replacements span `V_8`, and `dim V_8=9`. There are exactly nine of them, so

```text
v_1,...,v_9 form a basis of V_8.
```

Choose one of the guaranteed three-clean coordinate deletions and let

```text
pi_7 : V_8 -> V_7
```

be the induced puncture map. The descended actual replacements span `V_7`, whose dimension is eight. Hence the images of the same nine global classes span rank eight. Since the source classes are a basis and `ker(pi_7)` has dimension one, at most one of the nine basis blocks can cease to be virtual-canonical complete under this puncture.

Now delete any one of the seven remaining coordinates. The clean seven-row construction gives a rank-two, deficiency-three six-row state, so the corresponding quotient has dimension seven. The composite puncture map

```text
pi_6 : V_8 -> V_6
```

is surjective on the descended actual replacement classes. Therefore the same nine global classes have image rank seven in every member of the six-row fan. At most two of the nine basis blocks can disappear in any such double puncture.

Delete one further coordinate from one of those six-row states. The resulting five-row coefficient plane still has rank two. Its virtual deficiency is two or three, so its replacement quotient has dimension five or six. The same nine global classes must have image rank exactly `3+d_5`. Equivalently, at most `6-d_5` of the nine basis blocks can disappear: at most four when `d_5=2`, and at most three when `d_5=3`.

These are simultaneous necessary conditions on one fixed nine-block set. It is not enough that the union of all compatible singleton blocks span separately at each row count.

## 3. Singleton states are fixed

On a virtual-canonical complete block, singleton compatibility is unique. The three singleton constraints are represented by the local rows `y`, `x`, and `x+y`. If two were contained in the coefficient plane, then both `x` and `y` would be contained, which is the canonical-empty condition and contradicts completeness.

Consequently each chosen global block has one singleton state. Puncture functoriality preserves that state whenever the block remains virtual-canonical complete; if the block stops being complete, its replacement class maps to zero.

There is therefore no independent state choice at seven, six, or five rows.

## 4. Exact finite test

The wrapper leaves the existing orbit, coefficient-plane, and global-lift cover unchanged. It is called only after an eight-row candidate has already passed the old conditions `d_8=3`, singleton capacity at least nine, and full compatible-singleton span nine.

It enumerates every nine-block subset of the eight-row singleton-compatible complete blocks. For each subset it requires:

1. at most one chosen block disappears in the selected clean seven-row puncture;
2. at most two chosen blocks disappear in each of the seven six-row punctures of that clean seven-row state;
3. in each of the 21 distinct five-row double punctures of the clean seven-row state, at most `6-d_5` chosen blocks disappear;
4. the nine chosen classes have exact extra rank nine at eight rows;
5. the images of those same chosen classes have exact extra rank eight at seven rows;
6. their images have exact extra rank seven in every six-row member of the clean fan;
7. their images have exact extra rank `3+d_5` in all 21 five-row shadows.

The 42 ordered two-step punctures are deduplicated to the 21 five-row subsets before the exact rank tests.

All new functional-rank calculations use the existing `Fraction` elimination over `Q`. The wrapper does not replace exact arithmetic with a finite-field heuristic.

A genuine Profile B state supplies its own nine actual singleton blocks and therefore must pass this test. Hence a full-cover result with zero fixed-nine survivors excludes Profile B rigorously.

## 5. Remaining bottleneck

This does not yet assert closure because the finite cover has not executed successfully on the available runner infrastructure. The new endpoint is nevertheless sharper than the previous global lift: a survivor must now carry one fixed nine-block singleton basis consistently through the entire selected `8 -> 7 -> 6 -> 5` clean puncture fan, with exact rational ranks at every level.
