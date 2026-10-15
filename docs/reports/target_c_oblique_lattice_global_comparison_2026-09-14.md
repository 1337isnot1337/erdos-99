<!-- theorem-state: {"artifact_id":"ART-274D82E6C6B6","canonical":true,"claim_ids":["C-OBLIQUE-LATTICE-COMPETITOR"],"claim_statuses":{"C-OBLIQUE-LATTICE-COMPETITOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — finite oblique-lattice global comparison

**Date:** 2026-09-14
**Target:** Target C-II / restricted affine-source subroute
**Status:** canonical restricted theorem; not a Level-I closure

## Statement

Let (u,v) be unit vectors with

[
  \\pi/3<\\theta:=\\angle(u,v)\\le\\pi/2,
  qquad \\Lambda_\\theta=\\mathbb Zu+\\mathbb Zv.
]

Let (A\\subset\\Lambda_\\theta) be finite, full-dimensional, and contain at
least two points. Put (n=|A|), (D=\\operatorname{diam}(A)), and

[
  a_0=\\frac{\\sqrt3}{2},
  qquad \\rho=\\frac1{\\sqrt3},
  qquad \\kappa_\\theta=\\sqrt{\\frac{a_0}{\\sin\\theta}}<1.
]

If

[
  oxed{(1-\\kappa_\\theta)D>4\\kappa_\\theta+2\\rho,}
  \tag{OL.1}
]

then there is an (n)-point subset (B) of the unit triangular lattice such that

[
  \\operatorname{diam}(B)
  \\le \\kappa_\\theta D+4\\kappa_\\theta+2\\rho<D.
  \tag{OL.2}
]

Thus (A) is not a global minimum-diameter (n)-point unit-separated source.
The conclusion is source-cardinality exact and applies to the full finite source
(A), including any contact-isolated points.

The same assertion applies to a basis angle in
([\\pi/2,2\\pi/3)) after replacing (v) by (-v). At the endpoint angles
(\\pi/3) and (2\\pi/3), the lattice itself contains unit equilateral
triangles, so those endpoints are not part of the triangle-free affine subroute.

## Proof

For a nonzero lattice vector (z=iu+jv), if (ij\\ge0), then

[
  |z|^2=i^2+j^2+2ij\\cos\\theta\\ge i^2+j^2\\ge1.
]

If (ij<0), write (a=|i|), (b=|j|). Then

[
  |z|^2=(a-b)^2+2ab(1-\\cos\\theta)\\ge1.
]

For the open angle range, the only unit differences are the four basis
differences (\\pm u,\\pm v). In particular every finite subset of
(\\Lambda_\\theta) is unit-separated, and its unit-contact graph is bipartite
under the parity of (i+j). This verifies the triangle-free regression but is
not needed for the competitor construction.

Let

[
  Q=\\{\\alpha u+\\beta v:0\\le\\alpha,\\beta<1\\},
  qquad K=\\operatorname{conv}A.
]

The half-open fundamental cell (Q) has area (s=\\sin\\theta). Its four
vertices have norm at most (2), so (Q\\subset B(0,2)). The translates
(a+Q), (a\\in A), have disjoint interiors and are contained in
(K+B(0,2)). Therefore

[
  ns\\le\\operatorname{area}(K+B(0,2)).
]

Steiner's formula, the isodiametric inequality, and the convex-body perimeter
bound (\\operatorname{per}(K)\\le\\pi D) yield

[
  ns
  \\le \\operatorname{area}K+2\\operatorname{per}(K)+4\\pi
  \\le \\frac{\\pi D^2}{4}+2\\pi D+4\\pi
  =\\pi(D/2+2)^2.
  \tag{OL.3}
]

Now consider the unit triangular lattice. Its Voronoi cells have area (a_0)
and covering radius (\\rho). If (N_\\triangle(r)) counts its sites in the
closed radius-(r) disk, the Voronoi cells of those sites cover the radius
(r-\\rho) disk, hence

[
  N_\\triangle(r)a_0\\ge\\pi(r-\\rho)^2
  qquad(r\\ge\\rho).
  \tag{OL.4}
]

Choose

[
  r=\\rho+\\sqrt{\\frac{a_0n}{\\pi}}.
  \tag{OL.5}
]

Then (N_\\triangle(r)\\ge n). Select any (n) sites in that disk and call
the resulting source (B). It has exactly the required cardinality, remains
unit-separated, and satisfies

[
  \\operatorname{diam}(B)
  \\le2r
  =2\\rho+2\\sqrt{\\frac{a_0n}{\\pi}}.
  \tag{OL.6}
]

From (OL.3),

[
  \\sqrt{\\frac{a_0n}{\\pi}}
  \\le\\sqrt{\\frac{a_0}{s}}(D/2+2)
  =\\kappa_\\theta(D/2+2).
]

Substitution into (OL.6) gives (OL.2), and (OL.1) makes its final inequality
strict. Since (B) is an explicit finite feasible source with the same (n),
global optimality of (A) would be contradicted.

If (K) is a segment instead, unit separation gives (n\\le D+1), while
(OL.5)--(OL.6) produce a triangular-lattice competitor of diameter
(O(\\sqrt D)); hence the lower-dimensional case is also beaten for all
sufficiently large (D).

## Necessary angle scale and exact limitation

If a finite oblique-lattice subset in this angle range is a global minimizer,
(OL.1) must fail. Since (\\kappa_\\theta\\le1), this implies

[
  0<\\sin\\theta-\\frac{\\sqrt3}{2}
  \\le\\frac{8+4/\\sqrt3}{D}.
  \tag{OL.7}
]

Thus the angle excess is (O(D^{-1})). The theorem eliminates fixed and
mesoscopic shear under its explicit finite threshold, but does not eliminate
the critical (O(D^{-1})) shear. For example, the regression
(\\theta=\\pi/3+R^{-2}), (D=O(R)), fails the strict threshold.

The theorem also does not prove that a general triangle-free global minimizer is
an affine-lattice subset. Rhombic grains, holes, phase interfaces, contact-
isolated populations, and macroscopic inactive chambers remain outside its
hypotheses. It is therefore a restricted source-level competitor theorem, not a
C-II or Level-I solution.

## Verification and audit

The accompanying sanity script is

    python3 research/verify_target_c_oblique_lattice_global_comparison.py

It checks the exact algebraic identity used in (OL.3) and evaluates fixed,
mesoscopic, boundary, and vanishing-shear test values. Its decimal tests are
non-load-bearing; the proof above is analytic. The independent proof audit is
`docs/audits/target_c_oblique_lattice_global_comparison_independent_audit_2026-09-14.md`.

No external theorem is imported beyond elementary convex geometry and the
unit-triangular Voronoi covering-radius calculation.

**Level-I status:** STILL OPEN. The exact remaining affine-source obstruction is
the inverse-diameter shear endpoint together with the missing theorem that every
canonical full-core source admits the affine-lattice structure used here.
