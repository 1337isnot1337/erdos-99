> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus2_closure_2026-09-22.md) · source SHA-256 `43a33aa07df3196d36bbd8949f3610686bd81a98a4f2aaf139e7893198601258`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6589fc539e2f67789db6868f7d1452ed0da8efda", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus2_closure_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1617f25dd7f35d7044d3b7b20f4001f8f9d6403772da49c61d7d723293229a46"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the eight-no-root `k=6`, `D=-2` branch

Date: 2026-09-22

Status: rigorous closure of the remaining eight-no-root `k=6` branch with `D=-2`. The proof composes the committed three-clean-coordinate reduction with the already-certified synchronized six-row rank-two `d=2` zero-survivor audit. No new heavy census is required.

Companion arithmetic composition checker:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus2_closure_2026_09_22.py`

The exact finite inputs reused below are

- `research/verify_target_c_support7_global_segment_relative_seven_noroot_k5_dminus1_d1p4_2026_09_21.py` for the synchronized six-row deficiency-one singleton-capacity maximum `3`;
- `research/verify_target_c_support7_global_segment_relative_five_noroot_k3_p5_sharp_2026_09_21.py` for the repaired five-row deficiency-one singleton-capacity maximum `3`; and
- `research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py` for the synchronized six-row deficiency-two zero-survivor obstruction.

The full census of the last audit is recorded in

`research/target_c_support7_global_segment_relative_seven_noroot_k5_dminus2_d0p6_closure_2026-09-21.md`.

This closes only the `D=-2` side of the eight-no-root `k=6` layer. The `D=-1,p=9` residual remains open, and Target C-II is not closed here.

## 1. The branch already forced by the current reduction

Assume a hypothetical eight-no-root state `B` in the remaining `k=6` layer has

```text
D(B)=-2,
p=8.
```

The committed eight-no-root rank-two reduction proves that its global virtual-canonical profile is forced to

```text
d_v=2,
q=8,
eight singleton changed blocks.
```

Thus all eight units of incomplete-root cost are singleton rows. There is no pair replacement and no selected incomplete root row outside these eight singleton blocks.

Let `P<=Q^8` be the rank-two coefficient-constraint space. The same reduction proves that `P` has at least two **three-clean** coordinates: a coordinate `i` is three-clean when no nonzero word of `P` of Hamming weight at most three contains `i` in its support.

Fix one three-clean coordinate `i`.

By definition, puncturing any set `S` with

```text
i in S,
1 <= |S| <= 3
```

preserves `rank(P)=2`. Hence the one-, two-, and three-row deletion shadows containing `i` have no coefficient-rank loss.

The exact deletion transport identity therefore gives

```text
|S|=1: D_7=-2+2=0,
|S|=2: D_6=-2+4=2,
|S|=3: D_5=-2+6=4.
```

Deleting no-root rows does not remove selected root rows. We use the unstripped form of the virtual-canonical containment inequalities, in which `p` counts all selected rows in incomplete root blocks, including blocks that become untouched. As already established elsewhere in the repository, an incomplete root row in a block untouched by the remaining no-root rows imposes no external coefficient constraint and no relative `T` relation; keeping it simply contributes its row to the defect. Consequently every shadow considered below still has total incomplete-root cost

```text
p=8.
```

## 2. Every double-deletion shadow containing `i` has `d_6=2`

Choose any second external coordinate `j!=i` and put

```text
B_6 = B\{i,j}.
```

The coefficient plane of `B_6` has rank two. Moreover every one-coordinate puncture of that six-row plane still has rank two, because any such puncture deletes a set `{i,j,k}` of size three containing the three-clean coordinate `i`.

Thus `B_6` is a synchronized six-row rank-two state, so the committed six-row `k=4` containment theorem applies.

Let `C_6` be its virtual-canonical complete set and

```text
d_6 = |C_6|-rank H(C_6).
```

The six-row containment theorem gives `d_6>=1`.

On the other hand, the seven-row shadow `B\{i}` has virtual deficiency two by the committed eight-no-root reduction. Virtual-complete sets only shrink under puncturing, so row-nullity monotonicity gives

```text
d_6<=2.
```

Therefore `d_6` is either one or two.

If `d_6=1`, the unstripped six-row containment inequality is

```text
D_6 >= 6+p+3d_6-3q_6.
```

Substituting `D_6=2`, `p=8`, and `d_6=1` gives

```text
2 >= 17-3q_6,
q_6>=5.
```

Every nonempty incomplete block in the actual root state is one of the eight singleton blocks. Hence these `q_6` virtual-complete changed blocks are compatible singleton blocks in the six-row virtual state. The six-row singleton capacity would therefore be at least five.

But the committed exact synchronized six-row deficiency-one census has unfiltered singleton-capacity maximum three:

```text
capacity 0 :  1 state
capacity 2 :  6 states
capacity 3 : 24 states.
```

So `d_6=1` is impossible. Hence

```text
d_6=2.
```

The same containment inequality now gives

```text
2 >= 6+8+6-3q_6,
q_6>=6.
```

Thus every such synchronized six-row shadow has singleton capacity at least six.

## 3. Every five-row projection of `B_6` has deficiency two

Delete any one of the six remaining external coordinates from `B_6`. Call the resulting five-row shadow `B_5`.

Its coefficient space still has rank two by three-cleanliness of `i`, and its defect is

```text
D_5=4.
```

Its virtual-complete set is contained in the six-row virtual-complete set, so

```text
d_5<=d_6=2.
```

The repaired five-row rank-two containment theorem gives `d_5>=1`. Thus

```text
d_5 in {1,2}.
```

Suppose first that `d_5=1`. The five-row containment inequality gives

```text
4 >= 5+8+3-3q_5,
q_5>=4.
```

Again every nonempty incomplete block is one of the fixed singleton blocks. Therefore the five-row virtual state would have at least four compatible singleton-complete blocks.

The exact repaired five-row deficiency-one singleton-capacity maximum is three. Hence `d_5=1` is impossible.

Therefore every one of the six coordinate projections of `B_6` has

```text
d_5=2.
```

For completeness, its containment threshold is

```text
4 >= 5+8+6-3q_5,
q_5>=5,
```

so every projected five-row state also has singleton capacity at least five.

## 4. The existing exact `d_6=2` audit has zero such states

We have reduced the hypothetical branch to a synchronized six-row rank-two state satisfying all of the following:

1. all six one-coordinate punctures preserve coefficient rank two;
2. `d_6=2`;
3. singleton capacity is at least six;
4. all six five-row coordinate projections have `d_5=2`;
5. each five-row projection has singleton capacity at least five.

This is exactly the structural class exhaustively covered by

`research/verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py`.

That certificate starts from every repaired five-row rank-two `d_5=2` parent of singleton capacity at least five, extends by every possible sixth no-root cycle, enumerates every realizable synchronized rank-two six-row plane, and then filters at `d_6=2` and singleton capacity at least six.

Its exact full-cover census is

```text
five-row d=2 capacity>=5 parents      2,436
parent extensions                    243,600
rank-two P6 candidates               355,691
all six projections rank two         138,552
six-row virtual d6=2                   1,418
six-row singleton capacity >=6           761
all six projected five-row d5=2            0
```

The survivor count is zero before any common singleton block set or final `T`-space rerank is needed.

Our hypothetical `B_6` would be one of those forbidden survivors. Contradiction.

Therefore the global branch

```text
D=-2,
k=6,
p=8
```

is impossible.

## 5. Consequence for the eight-no-root `k=6` layer

The original `D=-2` arithmetic possibilities were

```text
(d_root,p)=(0,8),(1,5),(2,2).
```

The `(1,5)` and `(2,2)` cases were already excluded by the global containment reduction. The argument above closes the last `(0,8)` case.

Hence:

> There is no eight-no-root `k=6` counterexample with `D=-2`.

Only the `D=-1,p=9` side of the current eight-no-root `k=6` reduction remains. Its surviving virtual profiles are

```text
(d_v,q,singleton_min) =
(1,7,5), (1,8,7),
(2,8,7), (2,9,9), (3,9,9).
```

The committed maximal-functional-rank reduction further requires each of these profiles to fill its entire replacement-functional quotient. That is now the exact bottleneck in this layer.
