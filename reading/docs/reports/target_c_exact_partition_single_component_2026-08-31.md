> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_partition_single_component_2026-08-31.md) · source SHA-256 `f237e533a012c27772077e9f77898fa3cfab1aabfdb9459dc7736a618b5caec3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3D0F1134C455","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C44: an exact noncrossing response partition has one interior component

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C10/C11 boundary reactions, C36-C38, C43  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Assume a fully force-visible response phase with at least one unpinned component, no loaded-loaded unit contacts (`e_BB=0`), and an exact attachment partition: every loaded vertex belongs to exactly one attachment set `A_r`.

Then

`c_I=1` and `A_1=B_+`.

Thus an exact multi-cell noncrossing partition cannot realize the C10/C11 diameter-reaction field. Multiple response components require shared loaded pins, loaded-loaded contacts, or both.

## 1. Proper cyclic intervals have nonzero reaction resultant

Order `B_+={b_1,...,b_q}` cyclically. C10 gives nonzero reaction vectors `g_b`, in strict cyclic direction order, with

`sum_{b in B_+} g_b = 0`.

Let `S` be a nonempty proper cyclic interval and `T=B_+\S`. The reaction directions in `S` occupy one open angular arc and those in `T` the complementary internal arc; the two positive cut gaps are omitted, so the two arc lengths have sum strictly less than `2pi`. Hence at least one of the two intervals has all its nonzero reaction vectors in an open semicircle, and its positive vector sum cannot vanish. If the other interval had zero sum, total balance would force the first to have zero sum as well. Therefore neither can vanish:

`sum_{b in S} g_b != 0`.

## 2. One harmonic component has zero net boundary force

For one unpinned component `I_r`, let `Lambda_r` be its positive-conductance Dirichlet response on `A_r`. As always,

`Lambda_r 1 = 0`.

If `P_{A_r}` is the attachment coordinate matrix, the component boundary force vector is

`f^(r)=Lambda_r P_{A_r}`.

Summing its boundary forces gives

`sum_{b in A_r} f_b^(r)=0`.

Under `e_BB=0` and the exact attachment partition, every positive contact incident to a loaded vertex `b in A_r` enters `I_r`; no other component uses `b`. Hence the component force equals the total C10 contact reaction:

`f_b^(r)=g_b`.

Therefore every partition block satisfies

`sum_{b in A_r} g_b = 0`.

## 3. A noncrossing partition has a proper interval block

Every noncrossing partition of a finite cyclic set with at least two blocks has a nonempty proper cyclic interval block. One proof chooses a block minimal under nesting: if it were not an interval, a gap between consecutive vertices of that block would contain vertices of another block; noncrossing forces the latter block entirely into that gap, contradicting minimality.

C36/C43 make the exact attachment partition noncrossing. If `c_I>=2`, choose a proper interval block `A_r`. Its component force balance gives zero reaction resultant, contradicting Section 1.

## 4. Theorem C44

Under `e_BB=0` and an exact one-component-per-loaded-vertex attachment partition,

`c_I=1` and `A_1=B_+`.

Equivalently, any multi-component response phase with no loaded-loaded contacts must share at least one loaded vertex between components.

## 5. Near-minimal implication

C38 shows that in the near-minimal phase only `o(D)` loaded vertices are shared or unused. C44 identifies the exact zero-defect endpoint:

`no loaded-loaded contacts + no shared/unused loaded vertices -> one harmonic component attached to all B_+`.

Hence any multi-component sequence approaching the C33 boundary minimum must route all inter-component coupling through the sublinear exceptional loaded set.

## Regression audit

- One component attached to all loaded vertices is allowed.
- Two components sharing a loaded pin are outside the exact-partition hypothesis; this is precisely the necessary coupling identified by C44.
- Boundary-only cores are outside the assumption that an unpinned component exists.
