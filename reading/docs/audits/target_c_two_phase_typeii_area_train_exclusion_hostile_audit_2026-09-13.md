> Generated reading edition · [exact source](../../../docs/audits/target_c_two_phase_typeii_area_train_exclusion_hostile_audit_2026-09-13.md) · source SHA-256 `9128fb08bb95303a952a433507bef72a67e659cc977a313e76d2ffd6d2f12803`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-86009E390EBD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — retraction of full-core Type-II area/train tradeoff

**Date:** 2026-09-13  
**Reviewed:** `research/target_c_two_phase_typeii_area_train_exclusion_2026-09-13.md`  
**Disposition:** REJECTED after normalization audit; theorem-state authority unchanged.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Bridge bound and side charge

The full bounded-face union in the canonical no-container Type-II core has area
`pi D^2/4-o(D^2)` and is contained in the force hull.  The finite
bridge-subtracted isoperimetric estimate therefore gives

`2 B_o <= (b-pi D)+o(D) = delta D+o(D)`.

Under global two-direction purity, a loaded convex-hull polygon has at most four
phase-aligned sides.  Type-II `c_B=0` and the exact identity

`e_BB=Q+2k+u_B`

then imply that all remaining loaded-hull sides are paid either by outer bridges or
by exceptional-face side incidences.  This gives

`H >= Q+2k+u_B-4-B_o`.

The shared-boundary stability lemma applies because the exceptional-face union has
`o(D^2)` area and each exceptional face is convex.  If `I` is the non-hull incidence
count, `H <= (1+o(1)) I`; with `P_exc=H+I`, this yields

`4f+Q >= 2(Q+2k+u_B-B_o)-o(D)`.

Substitution of the bridge bound and dropping nonnegative terms is exactly

`Q <= 4f+delta D+o(D)`.

No outer-face occurrence is silently identified with a different cell occurrence.

**Verdict:** pass under the explicit global two-phase and near-disk full-core scope.

## 2. Area normalization failure

The per-face Oler bound and disjoint-interior argument do give

`(sqrt(3)/4)(2f+Q) <= (pi/4)D^2+o(D^2)`,

but the normalized consequence is

`2f/D^2+Q/D^2 <= pi/sqrt(3)+o(1)`,

not `2f/D+Q/D <= pi/sqrt(3)+o(1)`.  The latter is the error in the reviewed note.
In the canonical regime `f=O(D)` and `Q=O(D)`, so the corrected inequality is
asymptotically vacuous at the `D` scale.  It cannot be combined with the side charge
to control `f/D`, `Q/D`, or `t`.

**Verdict:** fail; the claimed area-to-train tradeoff is not proved.

## 3. Train consequence withdrawn

The exact identities `T/D=t+2f/D` and `q/D=t+k/D`, and the audited train floor,
remain valid.  They do not provide an upper bound for `2f/D` once the corrected
area normalization is used.  Therefore the displayed train bounds `(TP.13)` and
`(TP.14)`, the zero-detour numerical bound, and the endpoint exclusion are withdrawn.

The verifier has been changed to check only the scale distinction and no longer
certifies a `t` upper bound.

**Verdict:** fail; no train-based exclusion survives.

## 4. Scope and non-implications

- The result requires global purity of all bounded quadrilateral faces in at most two
  projective directions; it is not a theorem about arbitrary Type-II survivors.
- The near-disk full-core area sandwich is required to pay outer bridges and to bound
  exceptional-face area.
- The all-regime train floor is audited-working proof-only input; no theorem-state
  promotion is asserted.
- No contact-isolated source point is deleted, no affine kernel is extended, and no
  KKT weight lower bound is used.
- No low-detour upper bound remains from this report. Phase mixtures, positive-detour
  configurations, unbounded direction sets, and the macroscopic inactive-container
  branch remain.

**Final verdict:** REJECTED proof attempt, retained for provenance. C-II and Level I
remain open.
