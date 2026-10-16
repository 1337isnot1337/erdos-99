<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "89ef136f160b5a60564e9bc854e6a06aeedef96d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_bounded_face_fan_crossing_floor_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f239bc67b4a0cd74df8cee20cb3aa750188c9fda70af40edb5ff954876e05c93"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — bounded-face fan crossing floor (retracted)

**Date:** 2026-09-12  
**Audited source:** `target_c_bounded_face_fan_crossing_floor_2026-09-12.md`  
**Disposition:** REJECTED for the density-floor conclusion; finite pair accounting passes.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This audit checks the exact pair count, the Jensen reduction, and the normalized
algebra leading to the `1.935992...` floor. It does not promote the result or claim
that the remaining higher-density branch is impossible.

**Correction:** the normalized algebra did not pass. The exact Jensen inequality is
`20f <= T(T-1)-2R`, but `f=O(D)` and `T=O(D)`. After division by `D^2`, its left
side is `o(1)`, not `20f/D`. Thus the density-floor conclusion is withdrawn. The
finite pair count and endpoint-fan scope remain valid.

## 1. Train-pair accounting

The complete stopped-train crossing graph has one vertex per train and one edge per
strict-rhombus crossing, because canonical train geometry gives at most one crossing
per pair. For a bounded nonquadrilateral face `F`, the no-loop theorem gives at most
one terminal occurrence of a fixed train on `F`. The endpoint-fan theorem makes every
pair counted by `choose(d_F,2)` noncrossing.

If the same pair were counted at two bounded faces, both trains would have terminal
occurrences on both faces, contradicting bounded-face endpoint simplicity. Therefore
the face pair sets are disjoint and

`sum_F choose(d_F,2) <= choose(T,2)-R`

is exact with occurrence-counted face endpoints.

## 2. Jensen step

Writing `I=sum_F d_F=4f+Q`, C-II face degrees give `Q>=f`, hence `I>=5f`. Jensen
gives

`sum_F choose(d_F,2) >= (I^2/f-I)/2 >= 10f`.

The last expression is increasing for `I>=5f`. Combining with the exact pair budget
gives `20f <= T(T-1)-2R`, including the harmless finite `-T` term.

## 3. Normalized elimination (rejected)

With `t=(q-k)/D`, `kappa=k/D`, and `varphi=f/D`, the train ledger gives
`T/D=t+2varphi`. The phase floor gives `2varphi-kappa>=gamma`, while the outer-walk
perimeter bound gives `varphi<=2t-pi+o(1)`. Dividing the pair inequality by `D^2`
gives

`20varphi <= (t+2varphi)^2-2 Delta_2`.

For `t` below the displayed endpoint, the right-hand side moved to the left is
strictly decreasing over the admissible interval `varphi<=2t-pi`, since the train
count there is below five. Thus its minimum occurs at
`varphi=(gamma+kappa)/2`, and the resulting inequality is

`t >= sqrt(2 Delta_2+10 z)-z`, `z=gamma+kappa`.

The perimeter admissibility gives `z<=4t-2pi`. On the resulting bounded interval,
the function `g(z)=sqrt(2 Delta_2+10z)-z` is increasing; hence
`g(z)>=g(gamma)=t_fan`. This contradicts `t<t_fan`.

The interval and monotonicity checks are certified by the companion rational-bound
script; no floating-point value is used as a theorem premise.

Those checks certify only arithmetic under the invalid normalization and do not
rescue the density claim.

## 4. Scope and limitations

The result depends on the proof-only all-regime phase floor and the audited bounded-
face fan/simplicity package. It controls only the normalized density variable
`(q-k)/D`; it does not upper-bound the remaining higher-density Type-II configurations,
does not control Type-I inactive containers, and does not produce a source-preserving
deformation or an exact unit triangle.

All contact-isolated source points remain outside the train and core rigidity ledgers.

**Final audit verdict:** REJECTED as a Type-II density-floor candidate because of the
`D` versus `D^2` normalization error. PASS remains only for the underlying finite
pair-count and endpoint-fan statements; C-II remains open.
