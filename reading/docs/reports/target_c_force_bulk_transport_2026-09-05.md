> Generated reading edition · [exact source](../../../docs/reports/target_c_force_bulk_transport_2026-09-05.md) · source SHA-256 `640656caa99f8eb763d343ad3a9b9ff0eea675dd86b4149e4e8e1981cd651658`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AAF3BCF0FC45","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - C-II force-bulk transport

**Date:** 2026-09-05\
**Target:** C-II\
**Status:** localization/FB4 rejected; weaker asymptotic conclusion lacks this proof

**Correction:** The [September 8 audit](target_c_force_bulk_and_correction_audit_2026-09-08.md)
gives a globally optimal heptagon-plus-center counterexample to the isolated-point
localization and FB4 strengthening. The weaker displayed n-m bound is not itself
refuted by that example, but the argument below does not prove it. Retain interior
isolates explicitly. The later restoration of C53/C-I does not repair this error.

## Theorem

Let A be a contact-minimal, diametrally saturated, triangle-free global
minimizer in the fully force-visible branch C=C_*. Choose a relative-interior
normalized KKT stress, let C be its positive unit-contact graph, and put
m=|V(C)|. Then n-m <= pi D. Thus all but O(D) source points lie in the
force-visible contact core.

## Proof

In the branch C=C_*, the relative-interior stress has positive contact support
equal to the complete unit-contact graph, C_+=C. Therefore V(C) is exactly the
set of source points incident to at least one unit contact. Every point outside
V(C) is contact-isolated.

The canonical jammed-branch lemma says that every contact-isolated source point
is a diameter endpoint. Hence all n-m such points lie on Q=V(conv A).
Consecutive vertices of the convex hull are distinct points of a unit-separated
set, so each hull edge has length at least one. Consequently

    n-m <= |Q| <= perimeter(conv A) <= pi D.

The last inequality is the planar perimeter-diameter inequality. This proves
the claim.

## Scope and consequence

This closes the previously stated force-bulk transport obligation n-m=O(D) in
C-II. It does not close C-II itself: the strongest current force-visible-core
capacity estimate has leading coefficient pi/(2 sqrt(3)), exactly equal to the
reciprocal triangular-lattice coefficient, and its remaining error is only
O(D). A positive second-order area gap or a response contradiction is still
required.

The proof uses only the promoted C26 normalization and the canonical isolated
vertex lemma; it does not apply in C-I, where C_+ may differ from C.

## Combined C49 consequence

Insert (FB1) into the refined C49 capacity estimate
$$
m\le \frac{\pi}{2\sqrt3}D^2-\frac{2}{\sqrt3}G+7q+O(1),
$$
and use $q\le\pi D$. Every C-II survivor therefore obeys
$$
n\le \frac{\pi}{2\sqrt3}D^2-\frac{2}{\sqrt3}G+8\pi D+O(1).
\tag{FB2}
$$
Since the translated triangular-lattice comparison gives
$n>D^2/c$ with $c=2\sqrt3/\pi$, the quadratic terms cancel and (FB2)
forces
$$
G<4\sqrt3\,\pi D+O(1).
\tag{FB3}
$$
Thus the remaining C-II problem is exactly a linear area-gap problem: any
uniform lower bound for $G$ exceeding the explicit coefficient in (FB3), or
an independent strict response defect, would finish the branch.

The endpoint bookkeeping can be sharpened. The $q=|B_+|$ nonisolated diameter
endpoints and the $n-m$ isolated diameter endpoints are disjoint vertices of
the same convex hull. Therefore
$$
(n-m)+q\le |Q|\le\pi D.
\tag{FB4}
$$
Replacing $n-m\le\pi D$ by (FB4) in C49 lowers the linear error to $7\pi D$
and gives
$$
G<\frac72\sqrt3\,\pi D+O(1).
\tag{FB5}
$$
This remains a linear bound, so it still does not close C-II.
