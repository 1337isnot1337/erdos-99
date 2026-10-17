> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_external_kernel_geometry_2026-09-22.md) · source SHA-256 `bd6795fccd632e0b60ebd21466fd4ab3776cb48f9d6ddba08256f8683bcaa95c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "afef4a4b341916f29521f4c226a6ac08ff5bcee2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_external_kernel_geometry_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c068b68c50ad4fa30cd6ed0a7e3a79bc17fa9f93ef714ff08f75ecdf4262fb10"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: fixed external-kernel geometry for the remaining Profile B

Date: 2026-09-22

Status: rigorous structural strengthening of the sole remaining eight-no-root `k=6` Profile B. It does not by itself close Profile B. It adds a common six-dimensional source-kernel constraint, exact intersection rules across all clean `d=3` puncture fans, and a linear Hall/Rado obstruction for the same nine source singleton basis classes.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_external_kernel_geometry_2026_09_22.py`

The starting point is the committed all-clean-fans reduction together with the newer low-weight source filter, which has already excluded coefficient weight two and isolates coefficient weight three in a separate five-row residual. The present kernel argument applies to every surviving same-deficiency `d=3` clean fan in either the weight-three or `d_1(P)>=4` source class. A genuine remaining source has

```text
t=8,
rank(P)=2,
d_8=3,
nine singleton replacements,
replacement-functional rank 9.
```

Hence its nine replacement classes form a basis of the nine-dimensional source functional quotient. For every three-clean coordinate `i`, the seven-row puncture has `d_7=3`; every second puncture has `d_6=3`; and every third puncture in the clean fan has `d_5 in {2,3}`. The existing verifier already requires the same nine source classes to have exact image ranks `8`, `7`, and `3+d_5`.

## 1. One fixed six-dimensional external subspace controls every same-deficiency kernel

Let `C` be the source virtual-complete block set and let

```text
N = null(P) <= Q^8.
```

Since `rank(P)=2`, `dim N=6`.

Use the dependency-dual model from the Profile A kernel-incidence closure. Let

```text
U = Q^C direct_sum N
```

be the canonical row-index space, let `R:U -> T` be the canonical relation map, and set

```text
K = ker R.
```

The source canonical complete deficiency is three. External containment makes the projection

```text
pi : K -> N
```

surjective, and its kernel

```text
W = ker pi
```

is exactly the pure complete-block dependency space. Therefore

```text
dim W = 3,
dim K = 9.
```

The source replacement-functional quotient is naturally

```text
V = K^*,
dim V=9.
```

Now puncture a set `S` of source external coordinates in one of the established clean fans. Assume:

1. the projected coefficient space still has rank two; and
2. the punctured virtual-complete deficiency is still three.

Write

```text
N_S = {alpha in N : alpha_s=0 for every s in S}.
```

Rank preservation gives

```text
dim N_S = 6-|S|.
```

Let `K_S` be the punctured canonical dependency space, embedded back into the source row-index coordinates. Puncture functoriality gives

```text
K_S subset K,
pi(K_S) subset N_S.
```

The punctured containment theorem gives surjectivity `K_S -> N_S`, while the punctured complete deficiency is again three. Thus

```text
dim K_S = (6-|S|)+3 = 9-|S|.
```

On the other hand

```text
pi^{-1}(N_S)
```

also has dimension

```text
dim W + dim N_S = 3+(6-|S|)=9-|S|.
```

Since `K_S subset pi^{-1}(N_S)`, equality of dimensions forces

```text
K_S = pi^{-1}(N_S).                 (1.1)
```

This is stronger than treating the puncture kernels separately.

Dualize. Let

```text
L = W^perp <= V.
```

Then

```text
dim L = 6.
```

For source coordinate `i`, let `ell_i` be the restriction of the `i`-th coordinate functional to `N`. Via the injection `pi^*:N^* -> K^*=V`, equation (1.1) gives the exact source quotient kernel

```text
G_S := ker(V -> V_S)
     = span{ell_i : i in S} <= L.   (1.2)
```

Whenever the coefficient rank survives deletion of `S`, these `|S|` coordinate functionals are independent, so

```text
dim G_S = |S|.
```

Consequently every source class that becomes zero in any rank-preserving `d=3` clean descendant lies in the same fixed six-dimensional subspace `L`.

## 2. At most six of the nine source basis classes can vanish anywhere in the `d=3` clean fan

Let the nine source singleton replacement classes be

```text
x_1,...,x_9 in V.
```

They form a basis of `V`.

If `x_a` maps to zero in any same-deficiency clean descendant, (1.2) places `x_a` in `L`. Since `L` has dimension six and the `x_a` are independent,

```text
at most six source basis classes can vanish in the union of all d=3 clean descendants.  (2.1)
```

Equivalently, at least three of the nine source singleton classes remain nonzero in every seven-row and six-row clean shadow and in every five-row clean shadow whose deficiency remains three.

A physical source singleton block that ceases to be virtual-complete has zero replacement class in the descendant. Hence the same statement also gives at least three source singleton blocks that cannot disappear in any of those same-deficiency descendants.

## 3. Exact intersections are controlled by deleted coordinate sets

Let `S` and `T` be two clean deletion sets for which both descendants have deficiency three and coefficient rank two. If deleting `S union T` also preserves coefficient rank two, then the coordinate functionals indexed by `S union T` are independent on `N`. Equation (1.2) therefore gives

```text
G_S intersect G_T = G_{S intersect T}
                  = span{ell_i : i in S intersect T}.     (3.1)
```

This contains the previously used kernel-incidence rules as special cases.

For example, fix a three-clean first deletion `i`. The seven second-deletion kernels correspond to the sets `{i,j}`. For distinct `j,k`, deleting `{i,j,k}` preserves coefficient rank two by three-cleanliness, so

```text
G_{i,j} intersect G_{i,k} = G_i.
```

Therefore a source basis label that first becomes zero in one six-row child cannot first become zero in another six-row child. In the notation of the current verifier,

```text
(Z_6(i,j) \ Z_7(i))
```

are pairwise disjoint over the seven second deletions. This strengthens the previous case split, which only prohibited repeated second labels when `Z_7(i)` was already a coordinate basis line and prohibited two coordinate two-planes through a non-coordinate `G_i`.

The same rule applies one level lower whenever the union puncture still has coefficient rank two. In particular, for two `d_5=3` children of the same six-row state, repeated newly-zero labels are impossible whenever the corresponding four-coordinate source puncture preserves rank two.

## 4. A Hall/Rado obstruction for all zero-label patterns simultaneously

The verifier can use more than pairwise intersections.

For every source basis label `a` that is zero in at least one same-deficiency clean descendant, let `S_1,...,S_m` be all deletion sets among the audited `d=3` descendants in which it is zero. Equation (1.2) forces one fixed nonzero source vector `x_a` to lie in

```text
J_a = G_{S_1} intersect ... intersect G_{S_m} <= L.        (4.1)
```

If `J_a=0`, the candidate is impossible.

For different labels, the corresponding `x_a` are distinct members of the fixed nine-element source basis. Hence they are linearly independent. Therefore for every set `A` of constrained labels,

```text
dim(sum_{a in A} J_a) >= |A|.                            (4.2)
```

These are the linear Hall/Rado inequalities for independent representatives from the allowed subspaces `J_a`. They include the six-label union bound (2.1) and many higher-order incidence obstructions that pairwise checks miss.

The companion verifier computes the six-dimensional coordinate-functional model directly from an exact integer basis of `null(P_8)`, constructs every `G_S`, intersects them over all zero occurrences of each fixed source block, and exhaustively checks (4.2). There are at most six constrained labels after (2.1), so at most `2^6-1=63` nonempty subsets need testing.

This is an exact rational calculation. It is not a probabilistic rank filter.

## 5. Scope

This does not close Profile B without running the finite cover. A candidate can avoid all zero-pattern obstructions if its nine source basis classes meet the puncture kernels generically enough.

It does, however, remove another layer of freedom from the current overapproximation. A surviving candidate must now use the same nine actual source singleton states, realize the exact source coefficient plane and defect, satisfy all established clean-fan rank conditions, satisfy the previous first- and second-level kernel incidence, and additionally admit one globally consistent six-dimensional external-kernel realization for every source basis class that vanishes anywhere in a `d=3` clean descendant.

The remaining finite bottleneck is execution of this strengthened full-cover audit.
