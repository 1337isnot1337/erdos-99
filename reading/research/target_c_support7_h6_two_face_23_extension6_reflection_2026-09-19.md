> Generated reading edition · [exact source](../../research/target_c_support7_h6_two_face_23_extension6_reflection_2026-09-19.md) · source SHA-256 `c5df3158d00923ca59fb35289b068bfbb7ea4f0e5902b2b8fcb7b9d6241b7802`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d4704c588fcbfe1c82b3677771204af9b88979d5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h6_two_face_23_extension6_reflection_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a0413b25dbb653e4aceedc74ea35a82f43d74c342be37469cf2efc3dccfa9b8e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven H6: face-(2,3) extension VI with reflection closure

Date: 2026-09-19

Status: exact finite reduction inside the generic H6 branch. The theorem-state authority is unchanged. C-II remains open.

## Result

The previous exact reflection-closed generic-H6 endpoint is

```math
4276=3422\,C_7+854\,(C_3\sqcup C_4).
```

Continuing the fixed physical-face pair `(2,3)` scan through positions 1700 through 2199 of the 4,944-cell one-face-adaptive endpoint produces 59 additional direct exclusions that are still members of the 4,276-state endpoint. All 59 exactify successfully.

The exact H6 hull reflection maps these 59 states to 59 distinct additional current survivors. The direct and reflected sets are disjoint. Closing the batch under reflection removes

```math
59+59=\boxed{118}
```

states and gives the explicit exact endpoint

```math
\boxed{4158=3316\,C_7+842\,(C_3\sqcup C_4)}.
```

The 59 direct exclusions split as

```text
C7       53
C3+C4     6
```

and by normalized ground sign pattern as

```text
235   21
236   17
245    2
256    7
346    9
356    3
```

Their reflected partners split by pattern as

```text
235    3
236    7
245    9
256   17
346    2
356   21
```

The remaining reflection-closed survivor census is

```text
145       4
156      16
235     556
236    1046
237      16
245     449
256    1046
345      16
346     449
347       4
356     556
```

These counts sum to 4,158 and are exactly invariant under the committed reflection pairing

```text
145 <-> 347
156 <-> 237
235 <-> 356
236 <-> 256
245 <-> 346
345 self
```

## Exact certificate layer

For each of the 59 direct candidates, retain the full twenty-way closed local branch cover at physical face 2 and again at physical face 3: ten cyclic force-gap orders times the two median branches. The global system is the committed 85-variable complete-angle affine lift.

A one-face branch is marked dead only after numerical LP support is recovered as an exact rational Farkas certificate. Every branch that remains locally live at face 2 is paired with every locally live branch at face 3. The state is excluded only when every such two-face product also has an exact rational Farkas contradiction. Thus every accepted direct exclusion covers all `20*20` local branch products. Floating-point LP values are discovery data only.

The 59 direct states use exactly

```math
1700+2321=\boxed{4021}
```

exact rational certificates:

```text
one-face dead-branch certificates       1700
two-face live-product certificates      2321
total                                   4021
```

Their exact forced constants split as

```text
strictly negative   3779
zero                  242
```

with zero exactification failures. The largest active rational dual denominator in the batch is

```text
16134134332079733307872774552
```

The reflected 59 states need no new LP assumption: their impossibility is transported by the already-certified exact H6 reflection involution.

Certificate:

`research/verify_target_c_support7_h6_two_face_23_extension6_reflection_2026_09_19.py`

## Validation

The direct candidates were exactified in three contiguous chunks of 20, 20, and 19 states. All 59 exactified with zero failures. The chunks collectively produced the certificate counts and denominator bound above.

An independent state-level reconstruction of the exact reflection map verified involutivity, confirmed that the 59 direct states and their 59 reflected partners are disjoint subsets of the 4,276-state endpoint, and reproduced the 4,158-state graph and pattern census.

The committed wrapper was syntax-checked, and a source-backed one-candidate rerun completed successfully with 95 exact certificates. Reconstructing all predecessor modules makes a monolithic rerun slower than a single bounded runner call; the theorem statement therefore relies on the already-completed three exactification chunks plus the independent state-level reconstruction, not on an incomplete numerical run.

## Remaining finite work

The fixed face-`(2,3)` scan remains available beyond position 2200 of the 4,944-cell one-face-adaptive ordering. The next block, positions 2200 through 2899, has already been numerically screened and contains further candidates, but those candidates are not part of this theorem statement until exactification against the current 4,158-state endpoint is complete.

The nonlinear route remains to impose the common `L(K8)` segment-order constraints, all-root interior-domination disjunctions, and the sufficient 45 four-cycle metric conditions on the explicit survivors, using the exact rational sine-interval machinery. Reciprocal-collinearity walls remain a separate nongeneric branch.
