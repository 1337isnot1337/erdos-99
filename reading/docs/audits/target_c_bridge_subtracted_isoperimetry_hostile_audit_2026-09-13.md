> Generated reading edition · [exact source](../../../docs/audits/target_c_bridge_subtracted_isoperimetry_hostile_audit_2026-09-13.md) · source SHA-256 `a2c848097bc70da72a5de10902482f771dca386c9038b2cc51d729a0cd288694`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5DEF180A783D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C bridge-subtracted outer-face isoperimetry

**Date:** 2026-09-13  
**Reviewed:** `research/target_c_bridge_subtracted_isoperimetry_2026-09-13.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS at proof-only scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Outer-face incidence

Let `U` be the union of the closures of all bounded faces. Every edge on the finite
perimeter of `U` has a bounded face on one side and therefore the unbounded face on
the other side: there is no omitted bounded face on the complement side. Such an edge
is a single outer-face occurrence unless its two sides are the unbounded face, which is
exactly the bridge case excluded from the perimeter.

In a connected plane graph each bridge has the same face on both sides. An outer-face
bridge contributes exactly two occurrences to the boundary walk and no positive-area
boundary edge to `U`. Hence the non-bridge occurrence budget is `L-2B_o`, proving

```math
\sum_jp_j\le L-2B_o.
```

The argument is by physical edge occurrences. Articulation vertices and repeated
outer-walk vertices do not create an extra perimeter occurrence that is not already in
`L-2B_o`.

**Verdict:** PASS.

## 2. Holes and internal bridges

The audit uses the full finite perimeter `H^1(partial U_j)`, not only one chosen outer
boundary component. Thus a hole boundary is included safely. An internal bridge whose
two sides are incident to a bounded face is not counted by `B_o`; it is not an outer
boundary edge of `U` and does not consume an outer-face occurrence. This is the correct
scope for the subtraction.

Positive-area components that meet at only a point are separated before summing
perimeters. Components sharing a positive-length edge would be one component of the
closed bounded-face union, so no shared edge is counted twice across the decomposition.

**Verdict:** PASS.

## 3. Isoperimetric step

For each finite-perimeter planar component,

```math
\operatorname{area}(U_j)\le p_j^2/(4\pi).
```

Summing and applying `sum p_j^2 <= (sum p_j)^2` gives

```math
A\le(L-2B_o)^2/(4\pi).
```

Taking the nonnegative square root and rearranging gives the stated upper bound on
`B_o`. No convexity or simple-boundary assumption is needed.

**Verdict:** PASS.

## 4. Asymptotic and two-phase compositions

The limit in (BI.4) follows directly from `epsilon_D,rho_D -> 0`; it is not a
claim about arbitrary Type-II graphs. The nonzero-surplus estimate (BI.5) is the same
finite inequality after dividing by `D` and taking limits.

The variation lower bound (BI.11) is the separately audited two-phase projection
estimate. When the **full bounded-face union** has saturated area, substituting
`2B_o <= (M-pi)D+o(D)` into `N_o <= P_exc+2B_o` gives (BI.12), and (BI.13)--(BI.14)
follow at `M=pi`.

In the canonical no-container Type-II full core, this full-area hypothesis follows by
sandwiching the bounded-face union `U` between the strict-rhombus union and the force
hull: `A_4 <= area(U) <= area(F)`, with both endpoints tending to `pi D^2/4` by the
promoted near-disk chain. This scope is valid for the full core, but not for an
arbitrary selected harmonic carrier.

For a graph for which only strict-rhombus saturation is available, the available
relation is (BI.9),
`2B_o <= (M-pi)D+P_exc+o(D)`. Substitution into the same occurrence charge gives
`2P_exc/D+M-pi >= (4-sM)/(2-s)-o(1)`, namely (BI.15), not (BI.12). At `M=pi` this
is the half-strength bound (BI.16). The stronger conclusion is valid only under the
additional full bounded-face area hypothesis.

**Verdict:** PASS conditional on the explicitly cited two-phase and near-area
hypotheses.

## 5. Limits and disposition

- The lemma does not prove near-disk area for an arbitrary selected harmonic carrier.
- It does not prove global two-phase purity of the full positive-contact graph.
- It does not control bridges when the outer walk has a linear surplus; it only gives
  `2B_o/D <= M-pi` in the saturated-area limit.
- It does not identify all non-two-phase occurrences with exceptional-face perimeter
  outside the stated incidence hypotheses.
- No contact-isolated source point is removed, and no full-source affine-kernel claim
  is used.
- No strict diameter descent or exact unit triangle follows.

The finite bridge-subtracted inequality is sound and exposes a usable conditional
bridge bound. The earlier strict-rhombus composition had an algebraic overclaim; this
audit records the corrected coefficient. The theorem state and C-II status remain
unchanged.

## 6. Full strict-rhombus route variant

For the union `R` of all strict-rhombus faces, every finite-perimeter boundary edge has
either the unbounded face or a bounded nonquadrilateral face on its other side. An
outer bridge has the unbounded face on both sides and cannot be a rhombus boundary
edge. Assigning each rhombus-boundary edge to its outer-face occurrence or to the
opposite bounded-face occurrence gives

```math
P_R\le(b-2B_o)+P_{exc}.
```

This assignment is occurrence-safe. An exceptional face may have repeated boundary
vertices, but its degree counts the needed edge-side occurrences. A strict-rhombus
edge cannot be a graph bridge.

Applying planar isoperimetry to the rhombus union and using
`A_4=pi D^2/4-o(D^2)` in the full-core Type-II branch gives

```math
(b-\pi D)+P_{exc}-2B_o\ge-o(D).
```

The result is an all-detour relation, not a bridge-free conclusion when
`b-pi D` is linear.

**Verdict:** PASS at proof-only Type-II scope.

**Final verdict:** PASS at proof-only scope; C-II remains open.
