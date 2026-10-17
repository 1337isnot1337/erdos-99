> Generated reading edition · [exact source](../../research/target_c_attachment_route_signed_return_hostile_audit_2026-09-12.md) · source SHA-256 `47e410c7d8261c09484a2c244c9100c8bf4d9ea0a186d3ab84a0ead69bfec1e7`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2ce95b41c9ddb91e289af2f4aad95a53251a0459", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_attachment_route_signed_return_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a75ca4d9062ec721df79945f81fd5e800b905de2d8e6b70166a6da5a1cd9e977"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit: attachment-route signed return

**Date:** 2026-09-12  
**Verdict:** PASS as a finite proof-only lemma; no C-II closure  
**Classification:** audited-working research result

This audit checks the load-bearing bookkeeping in
[`target_c_attachment_route_signed_return_2026-09-12.md`](target_c_attachment_route_signed_return_2026-09-12.md).

1. The cuts are at occurrence-counted consecutive attachment occurrences.  Therefore
the outer routes are disjoint as walk occurrences and their lengths sum to `L`.  The
cyclic attachment chords telescope around the convex attachment boundary, so their
lengths sum to `per(P)` under the inherited Section-101 boundary-order hypothesis.

2. A bounded nonquadrilateral face is charged once as its full clockwise occurrence-
counted boundary.  Its displacement is zero, so its route excess is its full degree.
Shared edges are distinct face occurrences; no edge occurrence is charged twice in the
same route ledger.  This is exactly why `P_exc`, rather than a set of geometric edges,
appears in (AR.1).

3. Every physical strict-rhombus terminal edge has one incident non-rhombus side: the
old outer face or one bounded defect face.  Assigning the terminal to that side is
injective on physical occurrences.  A bridge can recur in the outer walk, but only the
occurrence adjacent to the retained rhombus is assigned; all other occurrences add
nonnegative slack.  Thus no train end is silently dropped and no endpoint is charged
twice.

4. For a complete train the terminal orientations are opposite.  The two exact route
losses therefore combine to `2-(q_i-q_j)·u`, which is bounded below by the support width
of the finite host set.  The same-route case contributes exactly `2` and is stronger
than the width bound.  Hosts have norm at most one, so every summand is nonnegative.

5. The train-span identity is used only after the finite endpoint inequality.  Summing
train area counts each strict rhombus exactly twice, once for each crossing direction;
the span bound is by the diameter of the same `P`, not by a different relaxed carrier.
This proves the direction and scale of (AR.3).

6. The face identities are substituted algebraically, with no asymptotic limit or
global optimality assertion.  Contact-isolated source points are untouched.  The
result is therefore valid only as a proof-only/audited-working carrier lemma.  Since
`Q_att` may contain many directions, the audit finds no universal positive return
constant; the source-specific host-capacity comparison remains open.
