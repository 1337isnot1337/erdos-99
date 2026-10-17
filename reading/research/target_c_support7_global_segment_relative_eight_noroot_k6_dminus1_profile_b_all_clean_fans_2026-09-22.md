> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026-09-22.md) · source SHA-256 `b218f2c36e78aed09d8fa5329abaf5e260ebed3ea6a6fde767d2a5f36dd880e4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3f2fd0ff1c048953d6abc0905ce0ec76c7efcdb0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c4618b981062c19f036575182023284b4937e8a3d5c936de8361f2a69e1d10a2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: require every three-clean puncture fan in the remaining Profile B

Date: 2026-09-22

Status: rigorous strengthening of the remaining eight-no-root `k=6, D=-1, p=9` Profile B finite target. Profile A is already closed structurally. This note does not close Profile B without execution of the strengthened finite cover.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_all_clean_fans_2026_09_22.py`

It wraps the current actual-state realization verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_actual_state_realization_2026_09_22.py`.

## 1. Remaining source profile

The only remaining eight-no-root `k=6, D=-1, p=9` profile is

```text
rank(P_8)=2,
d_8=3,
nine singleton replacements,
replacement-functional rank 9.
```

Thus the nine actual source replacement classes form a basis of the nine-dimensional source functional quotient `V_8`.

The rank-two projective-column theorem already proved in the `k=6` reduction gives at least two three-clean source coordinates. A source coordinate `i` is three-clean exactly when every puncture deleting a set `S` with

```text
i in S,
1 <= |S| <= 3
```

preserves coefficient rank two. Equivalently, `i` lies in the support of no nonzero word of `P_8` of weight at most three.

The previous global-lift and fixed-nine verifiers selected one such three-clean coordinate and followed only its `8 -> 7 -> 6 -> 5` fan. A genuine source must satisfy the same conditions through every three-clean source coordinate, not merely through one chosen witness.

## 2. All-clean-fans lemma

Let `i` be any three-clean coordinate of a genuine Profile B source.

The already-proved Profile B sharpening applies to an arbitrary three-clean coordinate, so after deleting `i`:

```text
rank(P_7)=2,
d_7=3,
dim(V_7)=8.
```

For every second coordinate deletion from that seven-row state:

```text
rank(P_6)=2,
d_6=3,
dim(V_6)=7.
```

For every third deletion in that fan:

```text
rank(P_5)=2,
d_5 in {2,3},
dim(V_5)=3+d_5 in {5,6}.
```

Puncture functoriality sends each of the same nine actual source singleton classes either to its descended replacement class or to zero. The descended actual classes span every child quotient. Because the source nine classes form a basis, the same fixed nine-block set must therefore have exact image ranks

```text
8 at every three-clean seven-row shadow,
7 at every six-row child in every three-clean fan,
3+d_5 at every five-row child in every three-clean fan.
```

The corresponding disappearance bounds are immediate:

```text
at most 1 source basis block disappears at seven rows,
at most 2 disappear at six rows,
at most 9-(3+d_5) disappear at five rows.
```

These conditions hold simultaneously for every three-clean source coordinate.

## 3. Distinct clean-puncture kernel lines

There is an additional cross-fan constraint.

Let `C` be the source virtual-complete block set and

```text
N = null(P_8),
dim(N)=6.
```

As in the Profile A kernel-incidence argument, form

```text
U = Q^C direct_sum N
```

and let `R:U->T` be the canonical relation map. External containment makes the projection of the dependency space

```text
K = ker(R)
```

onto `N` surjective. Its kernel is the three-dimensional dependency space among the complete-block rows, so

```text
dim(K)=6+3=9.
```

The source functional quotient is canonically dual to `K`:

```text
V_8 ~= K^*.
```

For a three-clean coordinate `i`, write

```text
N_i = {alpha in N : alpha_i=0}.
```

The seven-row child has the same deficiency three, hence its dependency space `K_i` has dimension

```text
5+3=8.
```

Under the puncture-functoriality identification, `K_i` is a hyperplane of `K`, the map `V_8 -> V_{7,i}` is restriction from `K^*` to `K_i^*`, and its kernel is the annihilator line

```text
L_i = ann(K_i).
```

If two distinct three-clean coordinates `i,j` had `L_i=L_j`, then their hyperplanes would coincide. Projecting to `N` would give `N_i=N_j`. The coordinate functionals `alpha->alpha_i` and `alpha->alpha_j` are nonzero on `N` because the one-coordinate punctures preserve rank two. Equal kernels make them proportional, so

```text
e_i - lambda e_j in N^perp = P_8
```

for some nonzero `lambda`. This is a nonzero word of `P_8` supported on `{i,j}`, contradicting the rank-two preservation of the `{i,j}` puncture. Therefore the kernel lines attached to distinct three-clean coordinates are pairwise distinct.

Now take the fixed nine source singleton basis. If one chosen basis block ceases to be virtual-complete after deleting a three-clean coordinate `i`, its nonzero source class maps to zero and hence lies in `L_i`. The same chosen block cannot disappear after a second three-clean coordinate `j`, because its source class would lie in the intersection of the distinct lines `L_i` and `L_j`.

Thus:

> among the first seven-row punctures of all three-clean fans, a particular source basis block can disappear in at most one fan.

This couples the clean fans before any expensive functional rerank.

## 4. Strengthened finite audit

The new wrapper leaves all existing source-realization conditions intact:

1. the exact six-row rank-two Profile B seed cover;
2. the selected global rank-two lift;
3. one fixed nine-block source functional basis;
4. extension of an exact seven-block six-row basis;
5. exact generation of the prescribed source coefficient plane by the chosen actual block states;
6. exact source defect `-1` from the reconstructed actual relation matrix.

For each chosen nine-block source basis that reaches the source-rank test, it additionally:

1. enumerates every source coordinate satisfying the exact three-clean puncture criterion;
2. requires at least two such coordinates, as guaranteed by the projective-column theorem;
3. reconstructs the canonical `d_7=3` state for every clean deletion;
4. reconstructs all seven `d_6=3` children of every clean seven-row state;
5. reconstructs the 21 five-row shadows in each fan and requires `d_5 in {2,3}`;
6. applies the exact complete-block disappearance bounds to the same nine source blocks at every level;
7. rejects any source basis block that disappears in two distinct clean seven-row shadows, by the distinct-kernel-line lemma above; and
8. computes over `Q` the exact replacement-functional image rank of the same nine source classes at every seven-, six-, and five-row state in every clean fan.

The wrapper uses the existing exact `Fraction` rank machinery. It does not replace any exact source-state check with a modular heuristic.

A genuine Profile B source satisfies all of these conditions. Therefore a zero-survivor result over the complete 20,451-orbit cover excludes Profile B rigorously.

## 5. Remaining bottleneck

Profile A no longer requires computation. The sole remaining eight-no-root `k=6,D=-1,p=9` target is Profile B.

The immediate finite bottleneck is execution of the strengthened all-three-clean-fans actual-state audit. A survivor would now be an explicit source state whose same nine singleton blocks realize the source coefficient plane and defect, extend the synchronized six-row basis, and satisfy every three-clean puncture fan simultaneously. A zero full-cover result closes Profile B.

Target C-II and Erdős Problem #99 remain open until this residual is excluded or otherwise resolved.
