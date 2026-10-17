# Target C: exact closure of the `d_6=4` side of `C:(4,11,10)`

Date: 2026-09-21

Status: exact finite closure of the final good-pair-shadow subcase for

```text
C: D=-1, p=12, (d_v,q,s)=(4,11,10).
```

Companion verifier:

- `research/verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d4_exact_profile_2026_09_21.py`

The `d_6=3` side was already excluded by exact target-profile reranking. This note records the exhaustive run of the corrected `d_6=4` verifier and therefore closes the entire `C:(4,11,10)` profile.

## 1. Necessary six-row conditions

For a committed good `p=12` pair deletion, the six-row shadow has `D_6=3`. In the remaining `d_6=4` case, containment forces at least nine changed virtual-complete blocks. If the unique global pair block is not among them, at least nine of those blocks are singleton replacements, contradicting the committed deficiency-four singleton-functional obstruction. Thus every unresolved six-row shadow has

```text
pair block among the six-row complete blocks,
at least eight compatible singleton replacements.
```

The singleton-plus-pair functional inequality then requires the selected eight singleton replacements together with the retained pair replacement to gain at least nine directions modulo the canonical relation-column span.

The exact verifier therefore loses no target state when it keeps only six-row `d_6=4`, singleton-capacity-at-least-eight states and pair block/state choices meeting this nine-direction threshold.

## 2. Exact two-row restoration

For every functional witness, the verifier restores each deleted no-root cycle through the already-forced one-row shadow conditions

```text
d_7=4,
singleton capacity >= 9.
```

Pairs of compatible one-row lifts determine candidate eight-row coefficient lines. The block involving both restored cycles supplies an additional compatibility condition, so the verifier explicitly recomputes the full eight-row block profile and discards a combined line unless it actually occurs there.

The surviving structural target must then satisfy

```text
d_8=4,
singleton capacity >= 10.
```

For each such state, the actual root profile must use exactly ten singleton changed blocks and the retained pair block/state. Restricting this actual profile back to the committed six-row shadow must still contain at least eight of the compatible singleton replacements and, together with the pair replacement, must still attain the necessary nine-direction functional gain. These are necessary conditions on the actual target state, not heuristic filters.

## 3. Exhaustive certificate

The full 325,955-representative six-row augmentation cover was scanned in the following disjoint ranges:

```text
[0,41000)
[41000,61500)
[61500,82000)
[82000,246000)
[246000,266500)
[266500,287000)
[287000,325955)
```

The ranges are contiguous and cover `[0,325955)` exactly. Aggregating the seven successful shards gives

```text
synchronized states:                    1,751,870

d_6=4, singleton capacity >= 8:
  capacity 8:                               15,366
  capacity 9:                               13,536
  capacity 10:                              12,922
  capacity 11:                              11,898
  capacity 12:                               8,614
  capacity 13:                               3,733
  capacity 14:                                 762
  total:                                    66,831

six-row functional-witness states:           4,519
viable pair choices per witness:             6

one-row lift multiplicity census:
  one compatible line:                      12,112
  two compatible lines:                        276

restored cycle pairs tested:                 25,262
candidate combined eight-row lines:          26,780
full-profile-compatible lines:               26,504
full-profile-incompatible lines:                276

structural global d_8=4 states:               1,602
structural capacity census:
  capacity 10:                               1,602

retained pair choices after global screen:    9,612
singleton-block combination census:
  exactly one combination:                   9,612

actual target profiles reaching rerank:           0
D<=-1 candidates:                                 0
```

The last zero is stronger than a favorable defect rerank. Every one of the 9,612 structural pair choices has exactly one possible ten-singleton block set, but its restriction to the committed six-row shadow fails at least one of the two necessary conditions above: it either retains fewer than eight of the required compatible singleton replacements or its selected singleton-plus-pair functionals gain fewer than nine directions. Hence no actual `C:(4,11,10)` target profile reaches the final relation-rank stage.

The full per-shard output is recorded in

- `research/certificates/target_c_C_d4q11_d4_exact_profile_full_scan_2026-09-21.txt`.

## 4. Exactness of the rank filters

All complete-block and functional ranks use

```text
P = 2^127 - 1.
```

The verifier certifies `P` prime by Lucas-Lehmer. Across the exhaustive run the maximum squared functional-row norm was `42` and the maximum functional width was `23`; every shard checked its own Hadamard bound, and the global maxima satisfy

```text
P^2 > 42^23.
```

By Hadamard's inequality, a nonzero rational minor in any functional rank computation cannot vanish modulo `P`. The complete-block rank check is covered by the pre-existing bound `P^2 > 12^15`. Thus the modular deficiency and functional-rank decisions used by the exhaustion are exact over `Q`.

No final relation matrix was needed because the necessary restriction conditions eliminate every structural candidate before reranking.

## 5. Consequence

The `d_6=3` good-pair-shadow side of `C:(4,11,10)` was already impossible. This exhaustive exact scan excludes the only remaining `d_6=4` side. Therefore

> `C:(d_v,q,s)=(4,11,10)` is impossible.

For the other final all-singleton profile `C:(5,12,12)`, deficiencies three and four are already excluded. The remaining finite target is only its `d_6=5` singleton-functional/exact-profile audit.
