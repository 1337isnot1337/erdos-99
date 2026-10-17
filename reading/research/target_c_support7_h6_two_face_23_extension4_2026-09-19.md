> Generated reading edition · [exact source](../../research/target_c_support7_h6_two_face_23_extension4_2026-09-19.md) · source SHA-256 `226c13eeccde4e28191736fa32b9e3bdce93726155590cee262559a60ee95be0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3109e9a234f9b753ef418f07d7b06e23ffb2c64a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h6_two_face_23_extension4_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4bce9d5dad96ea660c4f2281b6f52ee5e1dd1e706cb746cb04310593e82d0afc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven H6: face-(2,3) extension IV

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The previous explicit exact generic-H6 endpoint is

$$
4805=3823\,C_7+982\,(C_3\sqcup C_4).
$$

Continuing the fixed physical-face pair `(2,3)` scan beyond the previously completed first 700 positions of the 4,944-cell one-face-adaptive endpoint gives 101 further exact exclusions. Therefore the explicit exact endpoint becomes

$$
\boxed{4704=3760\,C_7+944\,(C_3\sqcup C_4)}.
$$

The 101 new exclusions split as

```text
C7       63
C3+C4    38
```

and by normalized ground sign pattern as

```text
235   12
236   15
245    3
256   51
345    1
346    1
356   18
```

The resulting explicit survivor census is

```text
145      4
156     16
235    642
236   1263
237     16
245    471
256   1153
345     20
346    478
347      4
356    637
```

These counts sum to 4,704.

## Exact certificate layer

For each candidate cell, retain the full twenty-way local branch cover at physical face 2 and again at physical face 3: ten cyclic force-gap orders times the two closed median branches. The global system is the committed 85-variable complete-angle affine lift.

A one-face branch is marked dead only after its numerical LP support is recovered as an exact rational Farkas certificate. Every branch that remains locally live at face 2 is paired with every locally live branch at face 3. The cell is excluded only when every such pair product also has an exact rational Farkas contradiction.

Thus every accepted cell exclusion covers all `20*20` local branch products. Numerical LP signs are discovery data only.

The 101 cells use exactly

$$
2657+5589=\boxed{8246}
$$

exact rational certificates:

```text
one-face dead-branch certificates       2657
two-face live-product certificates      5589
total                                   8246
```

Their exact forced constants split as

```text
strictly negative   7826
zero                 420
```

with zero exactification failures in the completed batch. The largest active rational dual denominator is

```text
5955951748146827421119871
```

The 101 candidates are disjoint from every previously committed adaptive/two-face candidate list. Their `q` indices begin at 819, while the third prior fixed-face `(2,3)` extension ends at `q=816`; the verifier also checks the full set-theoretic disjointness against all 171 earlier exact post-order-hull exclusions.

The discovery scan covered positions 700 through 1199 of the 4,944-cell one-face-adaptive endpoint. It found 101 numerical candidates with no LP failures. Exactification was then rerun in three independent contiguous chunks, all with zero failures. The committed verifier reconstructs and rechecks the certificates and supports `--start/--stop` chunking so the expensive exact run need not be repeated as one monolithic job.

Certificate:

`research/verify_target_c_support7_h6_two_face_23_extension4_2026_09_19.py`

## Reflection corollary

The exact H6 hull reflection proved in `target_c_support7_h6_reflection_closure_bound_2026-09-19.md` pairs ground patterns as

```text
145 <-> 347
156 <-> 237
235 <-> 356
236 <-> 256
245 <-> 346
345 self
```

For a non-self-mirror pair, the symmetric 14,174-cell universe has equal cardinality on both sides. Therefore an imbalance in the current survivor counts forces at least the absolute difference to disappear when the exact exclusion set is closed under reflection.

At the new 4,704 endpoint the forced additional reflected exclusions are at least

```text
145/347       |4 - 4|       =   0
156/237      |16 - 16|      =   0
235/356     |642 - 637|     =   5
236/256   |1263 - 1153|     = 110
245/346     |471 - 478|     =   7
                                  ---
                                  122
```

Hence the reflection-closed generic-H6 survivor set satisfies the rigorous bound

$$
\boxed{|S_{H6}^{\rm refl}|\le 4704-122=4582}.
$$

This is an upper bound, not an explicit 4,582-cell census. A state-level reflection map would identify the actual reflected union and can only improve the bound.

## Remaining finite work

This batch covers only positions 700 through 1199 for the fixed physical face pair `(2,3)`. The same exact branch test still has unscanned positions beyond 1200 and other physical face pairs. Hull reflection sends `(2,3)` to `(3,4)`, so an explicit state-level reflection closure should be constructed before duplicating that scan.

The newer metric-order results also supply a separate stronger direction: all 168 adjacent reciprocal-segment comparisons live on one `L(K8)` order graph, and generic H6 has fourteen exact all-root interior-domination disjunctions. Those should be layered onto the surviving affine cells with incremental exact cycle pruning. Cells surviving the rational sign/order layer then face the fifteen independent nonlinear sine-law metric equations, preferably through short line-graph cycles with certified angle bounds.

Reciprocal-collinearity walls remain a separate nongeneric branch.
