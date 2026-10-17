> Generated reading edition · [exact source](../../../docs/audits/target_c_oblique_lattice_global_comparison_independent_audit_2026-09-14.md) · source SHA-256 `2cdfc3f407f2ed073238c55b394a95155652e77330bc79d27d9705e77151f1d6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-85E7741C3A58","canonical":true,"claim_ids":["C-OBLIQUE-LATTICE-COMPETITOR"],"claim_statuses":{"C-OBLIQUE-LATTICE-COMPETITOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — finite oblique-lattice global comparison

**Date:** 2026-09-14
**Target:** Target C-II / restricted affine-source subroute
**Audited artifact:** `docs/reports/target_c_oblique_lattice_global_comparison_2026-09-14.md`
**Status:** PASS for the stated restricted theorem; canonical promotion is valid only with the scope below.

## Audited statement

Let (u,v) be unit vectors with

[
  \\pi/3<\\theta:=\\angle(u,v)\\le \\pi/2,
  qquad \\Lambda_\\theta=\\mathbb Zu+\\mathbb Zv.
]

For a finite full-dimensional (A\\subset\\Lambda_\\theta), put
(n=|A|), (D=\\operatorname{diam}(A)), and
(\\kappa=\\sqrt{(\\sqrt3/2)/\\sin\\theta}). If

[
 (1-\\kappa)D>4\\kappa+2/\\sqrt3,
]

then there is an (n)-point subset (B) of the unit triangular lattice with
(\\operatorname{diam}(B)<D). Consequently (A) cannot be a global
minimum-diameter (n)-point unit-separated configuration.

The theorem is finite, source-cardinality exact, and applies to the original
source (A), not merely to a contact scaffold. It does not assert that an
arbitrary C-II source has an affine-lattice chart.

## Proof audit

1. **Unit separation.** For a nonzero lattice difference (iu+jv), if (ij\\ge0)
   then (\\|iu+jv\\|^2\\ge i^2+j^2\\ge1). If (ij<0), writing
   (a=|i|,b=|j|) gives
   [
   \\|iu+jv\\|^2=(a-b)^2+2ab(1-\\cos\\theta)\\ge1.
   ]
   The only possible unit differences in the open angle range are the basis
   differences. Thus every finite lattice subset is feasible, and its unit
   contact graph is bipartite under the parity of (i+j). No triangle-free
   hypothesis is being smuggled into the diameter comparison.

2. **Fundamental-cell population bound.** The half-open cell
   (Q=\\{\\alpha u+\\beta v:0\\le\\alpha,\\beta<1\\}) has area
   (s=\\sin\\theta). Its four vertices have norm at most (2), hence
   (Q\\subset B(0,2)). The translates (a+Q), (a\\in A), have disjoint
   interiors and lie in (K+B(0,2)), where (K=\\operatorname{conv}A). Therefore
   [
   ns\\le \\operatorname{area}(K+B(0,2)).
   ]
   For a full-dimensional convex (K), Steiner's formula, the isodiametric
   inequality, and (\\operatorname{per}(K)\\le\\pi D) give
   [
   ns\\le \\frac{\\pi D^2}{4}+2\\pi D+4\\pi
      =\\pi(D/2+2)^2.
   ]
   This is a bound on the full source hull and has no hidden density or
   contact-graph assumption.

3. **Exact competitor cardinality.** The unit triangular lattice has Voronoi
   cell area (a_0=\\sqrt3/2) and covering radius \\(\\rho=1/\\sqrt3\\).
   If (N(r)) counts its sites in a radius-(r) disk, the Voronoi cells of
   those sites cover the radius-(r-\\rho) disk, so
   [
   N(r)a_0\\ge\\pi(r-\\rho)^2.
   ]
   With (r=\\rho+\\sqrt{a_0n/\\pi}), at least (n) sites lie in the
   disk. Selecting any (n) of them preserves unit separation and gives an
   actual (n)-point source (B) with
   [
   \\operatorname{diam}(B)\\le2r
      =2\\rho+2\\sqrt{a_0n/\\pi}
      \\le \\kappa D+4\\kappa+2\\rho.
   ]
   The displayed strict hypothesis is exactly the condition making this bound
   less than (D). The global-minimality contradiction is therefore valid.

4. **Lower-dimensional hull.** If (K) is a segment, unit separation gives
   (n\\le D+1). The same triangular-lattice disk construction has diameter
   (O(\\sqrt n)=O(\\sqrt D)), hence is strictly smaller for all sufficiently
   large (D). The full-dimensional theorem itself does not rely on this
   auxiliary case.

Every inequality in this chain is finite. No asymptotic subsequence, deleted
isolated point, stress integration, or change from source to scaffold occurs.

## Scope audit and exact frontier effect

The theorem excludes fixed and mesoscopic angle excess whenever the displayed
finite threshold holds. Rearranging the necessary condition for a global minimizer
gives

[
0<\\sin\\theta-\\sqrt3/2\\le (8+4/\\sqrt3)/D,
]

and hence (\\theta-\\pi/3=O(D^{-1})) in the acute range. The proof does not
exclude the critical inverse-diameter shear, does not prove affine-lattice
structure for a canonical full-core source, and does not touch the
macroscopic-container branch. The theorem is therefore a restricted source-level
comparison, not a C-II or Level-I closure.

## Adversarial regressions

- The (\\theta=\\pi/3+R^{-2}) vanishing-shear lattice family has (D=O(R)),
  so ((1-\\kappa)D=O(R^{-1})) and fails the strict threshold. It is not
  contradicted.
- A square lattice ((\\theta=\\pi/2)) satisfies the threshold for large (D),
  but its finite patches remain valid triangle-free sources; the conclusion is
  only that they are not global minimizers at those cardinalities.
- Unit equilateral triangles may occur in the triangular competitor (B); this is
  permitted and is precisely why (B) is a valid competitor rather than a source
  classification.
- Contact-isolated points of (A), if any, remain in the (n)-point cell count.
- No claim is made for rhombic grains, holes, phase interfaces, or a union of
  affine charts. Those are outside the theorem's hypotheses.

## Audit verdict

PASS. Promote only the restricted claim
`C-OBLIQUE-LATTICE-COMPETITOR` with this exact finite scope. The promotion must
also record the remaining (O(D^{-1})) shear endpoint and must not state that
all C-II minimizers are affine-lattice sources. The scalar near-floor regression
must remain noncanonical and rejected as a source-level closure mechanism.
