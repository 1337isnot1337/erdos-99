> Generated reading edition · [exact source](../../../docs/audits/target_c_quarter_fold_outer_isolate_payment_independent_audit_2026-10-09.md) · source SHA-256 `91f15e8f40f74d7eba86f342da6a4f9971c372ad9b72aa487b2c130ee4fbdc3d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5814CEC8D84F","canonical":true,"claim_ids":["C-QUARTER-FOLD-OUTER-ISOLATE-PAYMENT"],"claim_statuses":{"C-QUARTER-FOLD-OUTER-ISOLATE-PAYMENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: quarter-fold outer isolate payment

**Date:** 2026-10-09. **Audit:** 230.
**Audit base:** `origin/main=667700f8273488ad399b8f18ff7886c7ccdcd1e4`, state `2026-10-09.audit.223`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Section 7.3.

## Verdict

**PASS WITH NARROWED SCOPE — promote `C-QUARTER-FOLD-OUTER-ISOLATE-PAYMENT`.** A full lower-feasible endpoint preserving the exact unit-contact graph and the actual bounded-face embedding has no isolates in nonconstant eight-faces. Constant-sign faces cannot gain net isolate population beyond their old population, by the canonical strict wall-packet bound. Therefore the endpoint's outside-region isolate population must increase by at least the old isolate population in nonconstant faces. This is a count statement; it does not track the identities of labels moving between faces.

The source invokes the previous one-isolate bound to say each occupied active face has exactly one isolate. That invocation is unnecessary and its fixed-other-label endpoint hypothesis is not implied by an integrated endpoint that relocates isolates. The stronger population inequality below is proved without that result and permits any number of old isolates in each nonconstant face.

## Exact audited statement

Let `A` be a triangle-free global minimum-diameter source selected with the fewest unit contacts among such sources. Let `W_1,...,W_r` be all its bounded actual unit-contact face cycles. Assume these cycles are simple, their geometric interiors are pairwise disjoint, and every source isolate lies either in exactly one such interior or outside their union. Let `A'` be a unit-separated labeled endpoint with exactly the same unit-contact graph as `A`. Assume the same cycles are the corresponding actual bounded faces in a plane embedding of that graph at `A'`.

Assume every bounded face is of one of these types:

1. Its boundary has constant quarter-fold sign, and `A'` carries the boundary and face interior by the resulting rigid motion.
2. Its old boundary is a simple convex actual eight-sided unit-contact face; `A'` gives it a nonconstant face-closed quarter-fold.

For each type-(2) face `F_i`, let `z_i(A)` be the number of old source isolates in its interior. Let `Z_out(A)` and `Z_out(A')` count isolate labels outside the union of the bounded face interiors in the respective embeddings. Then

```math
\boxed{Z_{\rm out}(A')\;\ge\;Z_{\rm out}(A)
       +\sum_{i:\,F_i\text{ is type (2)}} z_i(A).}
```

No upper-diameter bound on `A'`, endpoint optimality, or fixed placement of any isolate is needed for this population implication. Exact graph preservation supplies unit separation, preserves the isolate labels, and ensures the folded boundary remains triangle-free. The conclusion is conditional on the endpoint and embedding; it does not assert that either exists.

## Independent reconstruction

For a type-(2) face, the transformed boundary labels are unit-separated and triangle-free because the endpoint preserves exactly the old unit-contact graph. Audit.229 supplies the four two-edge arcs, so canonical `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER` applies. Its convex hull is covered by closed unit disks about the transformed boundary labels. The actual bounded face interior lies inside that hull. Any isolate in the new face would be strictly farther than one from every wall vertex, since its exact contact graph degree is zero; the cover gives one wall vertex at distance at most one. Hence the new face contains no isolate.

For a type-(1) face, let `M` be its new interior isolate population. Pull those `M` points back by the inverse rigid motion. The preserved-face embedding puts them strictly inside the old wall. Exact contact-graph preservation makes every pair of these isolates strictly farther than one apart and every one strictly farther than one from every wall vertex. They form a strict packet in the old face. Apply canonical `C-UNIT-WALL-PACKET-POPULATION-BOUND` to the canonical source `A`; it gives `M<=z_i(A)`. This argument uses no upper ledger for the new positions and does not require transporting the old isolate labels themselves.

Summing, the new bounded-face isolate population is at most the old population in constant-sign faces. The old bounded-face population is the constant-sign population plus the population in nonconstant faces. Exact graph preservation keeps the total number of isolate labels fixed, so subtracting bounded populations proves the displayed outside-population inequality, including the case of multiple old isolates in one folded face. This argument bounds populations and does not assert that any particular isolate label ends outside all bounded faces.

## Hostile checks and scope

- **Earlier one-isolate lemma:** the canonical `C-QUARTER-FOLD-EIGHT-FACE-ISOLATE-BOUND` assumes the fold retains every other source label. An integrated endpoint that moves isolates does not satisfy that hypothesis by itself. This audit does not use that theorem.
- **Face type:** the hull argument needs an old simple convex actual eight-face and its local quarter-fold. Nonconstant faces of degree nine or more, nonconvex old faces, nonsimple face boundaries, and embeddings that do not preserve the face correspondence are outside scope.
- **Exact contact graph:** equality of graphs is required, not just retention of old contacts. It ensures isolates stay isolates and the old triangle-free condition persists. Without it, the counting and local lower-feasibility steps do not follow.
- **Outer region:** `Z_out` means outside all bounded face interiors in the stated family, including outer pockets and exterior regions. No capacity bound for that region is proved.
- **Upper constraints and globality:** the endpoint need only be unit-separated with the stated graph and embedding. No diameter descent or Level-I implication follows.
- No finite verifier encodes the infinite-looking composition, and none is claimed; the proof is a finite counting argument from the canonical wall-packet and hull-cover theorems.

## Dependencies and frontier effect

Dependencies are canonical `C-UNIT-WALL-PACKET-POPULATION-BOUND`, `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER`, and `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`. Audit.229 is required to infer the four-two-edge pattern from local endpoint feasibility; the previous one-isolate bound is not a dependency.

The result turns the occupied-face obstruction into an exact required increase of the outside-region isolate population, equal to the total old isolate population in nonconstant eight-faces. It does not identify which labels move outside, bound the outside-region capacity after the core moves, or supply a feasible integrated endpoint. C-II and Level I remain open.
