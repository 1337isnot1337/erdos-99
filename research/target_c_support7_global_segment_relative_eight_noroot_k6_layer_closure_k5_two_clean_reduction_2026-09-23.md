<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3f15b69311a37ebdf78e06bedd1e862c7955e879", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_layer_closure_k5_two_clean_reduction_2026-09-23.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "47550231a003648e36c3f7396bb791795dcdc9a252f805898fb5870d5a53bbf4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the eight-no-root `k=6` layer and reduce the next `k=5` layer

Date: 2026-09-23

Status: rigorous composition closure of the full eight-no-root `k=6` layer, plus a new rank-three two-clean puncture lemma for the next `k=5` layer. This is a finite metric-basis result. It does not close Target C-II or Erdős Problem #99 and does not change canonical theorem-state authority.

No new exhaustive computation is used here. The `k=6` closure is a proof-level composition of already committed branch closures. The `k=5` reduction below is elementary linear algebra over `Q` combined with the already established all-depth deletion bound.

## 1. The entire eight-no-root `k=6` layer is closed

Let `B=R union E`, `|E|=8`, be a hypothetical eight-no-root counterexample with `k(B)=6`. The committed reduction

`research/target_c_support7_global_segment_relative_eight_noroot_k6_reduction_2026-09-22.md`

proves that the external coefficient-constraint space has rank two, that `D(B) in {-2,-1}`, and that

```text
D(B)=p+3d_root-10.
```

Hence there are exactly seven arithmetic branches:

```text
D=-2: (d_root,p)=(0,8),(1,5),(2,2)
D=-1: (d_root,p)=(0,9),(1,6),(2,3),(3,0).
```

That reduction itself excludes

```text
D=-2: (1,5),(2,2)
D=-1: (2,3),(3,0)
```

and also closes the `D=-1,(d_root,p)=(1,6)` branch. Thus only

```text
D=-2,(d_root,p)=(0,8)
D=-1,(d_root,p)=(0,9)
```

remained.

The first is closed by

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus2_closure_2026-09-22.md`.

For the second, the committed sharpening

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_sharpening_2026-09-22.md`

reduces the whole branch to exactly two global root patterns:

```text
Profile A:
    d_v=2, q=8,
    seven singleton changed blocks + one pair changed block;

Profile B:
    d_v=3, q=9,
    nine singleton changed blocks.
```

Profile A is closed by

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_kernel_incidence_closure_2026-09-22.md`.

Profile B is closed by the subsequent exact chain ending at

`research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_overlap_witness_closure_2026-09-23.md`,

whose final conclusion is that Profile B is empty.

These cases exhaust the seven arithmetic branches. Therefore:

> **Theorem 1.** There is no eight-no-root counterexample with `k(B)=6`.

This is a strict strengthening of the last individual Profile-B closure: the whole rank-two eight-no-root layer is now discharged.

## 2. Exact arithmetic boundary for the next `k=5` layer

Now suppose, for the next layer, that a hypothetical eight-no-root counterexample has

```text
k(B)=5.
```

As in the already closed `k=8,7,6` layers, the established seven-no-root theorem implies that every external row is an `M`-coloop and a `Q`-noncoloop. Hence

```text
D(B) in {-2,-1}.
```

The external coefficient-constraint space

```text
P <= Q^8
```

has rank

```text
rank(P)=8-k=3.
```

The exact root-block formula becomes

```text
D(B)=8+p+3d_root-3k
    =p+3d_root-7.
```

Therefore the complete `k=5` arithmetic boundary is only

```text
D=-2: (d_root,p)=(0,5),(1,2)
D=-1: (d_root,p)=(0,6),(1,3),(2,0).
```

So the next layer has five global arithmetic branches before any virtual-canonical or functional-rank refinement.

## 3. Generalized-weight floors in rank three

For a nonempty deletion set `S subset E`, let `s=|S|` and let `q_S` be the coefficient-rank loss under puncturing on `S`. The established all-depth deletion identity is

```text
D(B\S)=D(B)+2s-3q_S.
```

Every proper deletion has at most seven no-root rows, so the proved seven-no-root theorem gives

```text
D(B\S)>=0.
```

Thus

```text
q_S <= floor((D(B)+2s)/3).
```

Equivalently, if `d_j(P)` denotes the generalized Hamming weights of the rank-three space `P`, then

```text
d_j(P) >= ceil((3j-D(B))/2).
```

For the two possible defects this gives

```text
D=-2: d_1(P)>=3, d_2(P)>=4, d_3(P)>=6;
D=-1: d_1(P)>=2, d_2(P)>=4, d_3(P)>=5.
```

The common condition `d_2(P)>=4`, together with `d_1(P)>=2`, forces a useful puncture geometry that is not needed in the rank-two `k=6` layer.

## 4. Rank-three two-clean-coordinate lemma

Call a coordinate `i` **two-clean** when no nonzero word of `P` of Hamming weight at most two has `i` in its support. Equivalently, puncturing any set `S` with

```text
i in S,
1 <= |S| <= 2
```

preserves `rank(P)=3`.

### Lemma 2

Let `P<=Q^8` have rank three, `d_1(P)>=2`, and `d_2(P)>=4`. Then `P` has at least two two-clean coordinates.

If `d_1(P)>=3`, all eight coordinates are two-clean.

### Proof

The second statement is immediate: `d_1(P)>=3` means there is no nonzero word supported on one or two coordinates.

Assume only `d_1(P)>=2`. There are no weight-one words. Consider the projective lines in `P` generated by weight-two words.

Two distinct such lines must have disjoint supports. Indeed, choose nonproportional weight-two words `u,v`.

- If they have the same support, then the two-dimensional subspace `span(u,v)` is supported on at most two coordinates, contradicting `d_2(P)>=4`.
- If their supports are different but intersect, then `span(u,v)` is supported on their union, of size at most three, again contradicting `d_2(P)>=4`.

Thus the supports of distinct weight-two lines are pairwise disjoint.

Choose one nonzero representative from each such line. Vectors with pairwise disjoint nonempty supports are linearly independent: in any nontrivial linear relation, a coordinate belonging to the support of one representative and no other has a nonzero uncancelled coefficient. Since `dim(P)=3`, there are at most three projective weight-two lines.

Their pairwise disjoint supports therefore cover at most six of the eight coordinates. At least two coordinates lie in the support of no weight-two word. Since weight-one words do not exist, those coordinates are two-clean. `square`

### Consequences in the two defect branches

For `D=-2`, the stronger floor `d_1(P)>=3` makes **every** external coordinate two-clean.

For `D=-1`, Lemma 2 gives at least **two** two-clean external coordinates.

Fix any such coordinate `i`. The one-coordinate puncture has a seven-row rank-three coefficient space, and every further one-coordinate puncture preserves rank three. In other words, every two-clean coordinate produces a synchronized seven-row rank-three shadow.

Because there is no coefficient-rank loss on the first puncture, its defect is exactly

```text
D_7=D(B)+2,
```

so

```text
D=-2 parent -> synchronized seven-row shadow with D_7=0;
D=-1 parent -> synchronized seven-row shadow with D_7=1.
```

Thus the five global `k=5` branches are not arbitrary rank-three states: the entire `D=-2` side has eight synchronized seven-row rank-three shadows, while every `D=-1` state has at least two.

## 5. Frontier reduction

The eight-no-root finite frontier therefore moves strictly below `k=6`.

The next exact target is the rank-three `k=5` layer with only the five arithmetic branches in Section 2 and with the synchronized-shadow condition in Section 4. A closing attack can now work one row lower:

```text
D=-2:
    every one-row shadow is seven-row, rank three, D=0,
    and every second puncture preserves rank three;

D=-1:
    at least two one-row shadows are seven-row, rank three, D=1,
    and every second puncture from those shadows preserves rank three.
```

This removes the completed rank-two `k=6` machinery from the live finite search and gives a precise rank-three puncture target for the next run.

The canonical global Target C-II frontier in `docs/targets/target-c/CURRENT.md` remains open. The finite support-seven/global-segment chain is a proof-only subroute toward that source-level closure and is not being promoted to a global solution here.
