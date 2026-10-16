# Target C: repair the eight-no-root k=3 local-rank certificate

Date: 2026-09-27

Status: exact support-level repair of `research/target_c_support7_global_segment_relative_eight_noroot_k3_full_layer_closure_2026-09-27.md`.

The old verifier imported the now-refuted converse that a touched empty block has local rank one whenever no containing tetrahedral support repeats. This note removes that converse. The enlarged relaxation still has zero survivors.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k3_local_rank_repair_2026_09_27.cpp`

## Sound local-rank relaxation

The branch data remain

- `k=3, D=-1, d_root=0, p=0`;
- `rank(P)=5`;
- `(d1,d2,d3,d4,d5)(P)>=(2,4,5,7,8)`;
- `h<=23`;
- touched complete rows are independent;
- every actual state requires `rank H(T)-rank H(C)>=3`.

For a touched block `b`, let `I_b` be its external occurrence set and `E_b` its local empty-state coefficient space. The safe support-level information is:

- a repeated containing tetrahedral support forces `dim(E_b)=2`, hence `|I_b|>=4` by `d2>=4`;
- with no repeated containing support, `|I_b|<2` is impossible by `d1>=2`;
- with no repetition and `|I_b|=2` or `3`, only rank one is possible;
- with no repetition and `|I_b|>=4`, both ranks one and two are permitted.

The last case is an intentional relaxation. It removes the false converse.

For two chosen local spaces, the verifier keeps only necessary generalized-weight tests:

- line-line: `|I intersect J|>=2` or `|I union J|>=4`;
- line-plane: `|I intersect J|>=2` or `|I union J|>=5`;
- plane-plane: `|I intersect J|>=4`, or both `|I intersect J|>=2` and `|I union J|>=5`, or `|I union J|>=7`.

These follow by splitting on the intersection dimension and applying `d1,d2,d3,d4` to the intersection or sum.

## Exact certificate

The repaired verifier independently regenerates the `S_7` support-multiset orbit counts

`1,1,4,14,61,268,1283,6032,27763`.

It then enumerates all virtual empty-block rank assignments satisfying the relaxed local rules and the existing necessary global conditions:

- `|E|>=h-15`;
- nominal local-dimension sum at least five;
- occurrence union covering all eight coordinates;
- independence of the complementary touched-complete rows;
- face-local capacity at least three.

The executed census is:

```text
support_multiset_orbits_size_8           27763
touch_at_most_23                         24720
cardinality_compatible_rank_assignments  29704
dimension_at_least_5                     16846
full_support_assignments                   7535
complete_independent                         59
capacity_0                                   38
capacity_1                                   19
capacity_2                                    2
capacity_survivors                            0
```

The old defective verifier had 22,686 cardinality-compatible states, 16,385 dimension-at-least-five states, and 7,203 full-support states. The repaired search is strictly larger at every stage affected by the local-rank ambiguity, yet the final 59 complete-independent states are unchanged and all have capacity at most two.

Therefore the branch `k=3,D=-1,d_root=0,p=0` remains closed.

All support enumeration is exact integer/set arithmetic. Triangle-row ranks are computed modulo `2^31-1`; the verifier checks the Lucas-Lehmer condition and `(2^31-1)^2>3^15`. Since each triangle row has squared norm three and rank at most fifteen, Hadamard's inequality makes these modular ranks equal the rational ranks.

The verifier source persisted with this note is the same source model that was compiled and executed locally; the local run reproduced the complete census above and `capacity_survivors=0`.

## Remaining audit scope

This repairs the eight-no-root `k=3` dependency. The separate old `k=4,D=-1,d_root=1,p=0` verifier on authoritative `main`, and any `k=4,D=-1,d_root=0,p=3` subcase that relies non-monotonically on the old helper's exact local-rank tag, still require separate audit or repair.
