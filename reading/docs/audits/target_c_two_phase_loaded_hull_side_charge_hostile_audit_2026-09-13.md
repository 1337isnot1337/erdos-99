> Generated reading edition · [exact source](../../../docs/audits/target_c_two_phase_loaded_hull_side_charge_hostile_audit_2026-09-13.md) · source SHA-256 `400c15c026e001f0db9865eb00aa2302a80536f655f34a9dfda8b1b79251d02b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BED67253F75E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C two-phase loaded-hull side charge

**Date:** 2026-09-13  
**Reviewed:** `research/target_c_two_phase_loaded_hull_side_charge_2026-09-13.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS at the stated conditional scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Convex side count

A convex polygon has at most two sides parallel to any fixed line direction: they lie
on the two supporting lines of the polygon in that direction. A third parallel side
would have a supporting line between them and its endpoints would not be extreme.
For two projective directions this gives the bound four. No collinear intermediate
hull vertex is counted because all hull vertices are extreme.

**Verdict:** PASS.

## 2. Face/bridge charge

Under `c_B=0`, loaded-loaded unit contacts are force-hull sides. A side outside the
two selected directions is either a bridge on the outer face or a nonbridge with a
unique bounded face on its other side. If that face were a quadrilateral, the global
phase-purity hypothesis would put the side in one of the selected directions. Hence
the face is nonquadrilateral and its boundary incidence pays the side once.

Distinct nonbridge side occurrences have distinct opposite face incidences. A bridge
is charged once as a physical edge, so the exact safe inequality is

$$
e_{BB}\le4+P_{exc}+B_o.
$$

The algebraic form `2k+u_B<=4f+B_o+4` follows from the exact Type-II identity
`e_BB=Q+2k+u_B`.

**Verdict:** PASS conditional on global phase purity and `c_B=0`.

## 3. Bridge-area composition

The prior audited bridge-subtracted rhombus-area lemma gives

$$
2B_o\le(b-\pi D)+P_{exc}+o(D)
$$

when `A_4=pi D^2/4-o(D^2)`. Substitution into the finite side charge gives the
displayed (LH.5) with coefficients `3/2` and `1/2`; no direction reversal occurs.

**Verdict:** PASS at Type-II full-area scope.

## 4. Limits

The result does not extend corridor phase purity to the entire graph, does not control
the remaining positive-detour term, and does not close C-II. Contact-isolated points
remain outside the positive-core ledger and are not deleted.

**Final verdict:** PASS at proof-only conditional scope; theorem state unchanged.
