> Generated reading edition · [exact source](../../../docs/reports/target_c_residual_square_grid_regression_2026-09-14.md) · source SHA-256 `fb3051c2fb7110d6157c60f4933310049c95ada59c88315899f4f331ab716a13`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1146CB9A65CB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — square-grid regression for the attachment-span residual

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** exact finite regression / C-II residual audit
**Target:** Target C-II / Level I
**Status:** unreviewed, noncanonical

## LEVEL I STATUS

`STILL OPEN`.

This report does not construct a global minimizer and does not disprove Erdős
Problem #99. It records an exact local/contact-complex obstruction to a tempting
closure of the repaired Type-II payment theorem.

## 1. The tempting but unsupported bridge

The repaired Type-II aggregate payment leaves the exact term

$$
2\sum_r(a_r-d_r),
\qquad a_r=|A_r|,\quad d_r=\operatorname{diam}(\operatorname{conv}A_r).
$$

A possible shortcut would be to assert, from triangle-freeness, planar contact
topology, harmonic equilibrium, and harmonic trapping alone, that

$$
a_r-d_r=o(d_r)\quad\text{or even}\quad a_r\le d_r+O(1).
\tag{1.1}
$$

The family below disproves both assertions at the stated local scope. The
regression is intentionally stronger than a scalar witness: it has an explicit
finite planar coordinate realization and exact equilibrium at every unloaded
vertex.

## 2. Exact square-grid family

Fix an integer $m\ge5$. Let

$$
I_m=\{1,\ldots,m-1\}^2,
$$

and let $A_m$ be the noncorner boundary points of the $(m+1)$-by-
$(m+1)$ grid:

$$
A_m=\{(i,j)\in\{0,\ldots,m\}^2:
 i\in\{0,m\}\text{ or }j\in\{0,m\},\quad
 (i,j)\notin\{(0,0),(0,m),(m,0),(m,m)\}\}.
$$

Put $V_m=I_m\sqcup A_m$, and join two points when their Euclidean distance is
exactly one.

The following facts are finite and exact.

1. Every two distinct points of $V_m$ are at distance at least one, because
   $V_m\subset\mathbb Z^2$.
2. The contact graph is a subgraph of the square grid and is bipartite under
   the parity coloring $(i,j)\mapsto i+j\pmod2$. It therefore contains no
   triangle, in particular no unit equilateral triangle.
3. Every $x\in I_m$ has all four grid neighbors in $V_m$. The four unit
   contact vectors sum to zero, so the positive unit-contact equilibrium
   equation holds at every unloaded vertex:
   $$
   \sum_{y\sim x}(y-x)=0.
   \tag{2.1}
   $$
4. Every $a\in A_m$ has a unit contact to $I_m$. Thus $A_m$ is the
   distinct loaded attachment set of the connected unloaded component $I_m$,
   and every unloaded point is contained in $P_m:=\operatorname{conv}A_m$.

The last assertion can be checked directly. The vertices of $P_m$ are

$$
(1,0),(m-1,0),(m,1),(m,m-1),(m-1,m),(1,m),(0,m-1),(0,1),
$$

and every point of $I_m$ lies in this octagon.

## 3. Exact attachment count and diameter

The boundary of the integer square has $4m$ points, and four corners were
removed. Hence

$$
a_m:=|A_m|=4m-4.
\tag{3.1}
$$

The displayed octagon has diameter attained, for example, by
$(0,1)$ and $(m,m-1)$, or by $(1,0)$ and $(m-1,m)$. Therefore

$$
d_m:=\operatorname{diam}P_m
=\sqrt{m^2+(m-2)^2}.
\tag{3.2}
$$

Consequently

$$
a_m-d_m
=4m-4-\sqrt{m^2+(m-2)^2}
=(4-\sqrt2)m+O(1).
\tag{3.3}
$$

In particular,

$$
\lim_{m\to\infty}\frac{a_m-d_m}{m}=4-\sqrt2>0.
\tag{3.4}
$$

Thus the attachment-span residual is genuinely linear in an exact harmonic,
triangle-free, unit-separated planar contact complex.

## 4. Scope audit: the hypotheses this regression lacks

The family is not a Target C-II counterexample. It lacks several decisive global
hypotheses:

- the loaded attachment vertices are not the vertices of a strictly convex
  near-disk force hull; many lie on collinear grid sides;
- the square grid is not a locally rhombus-saturated carrier at triangular
  packing density;
- no diameter graph, KKT stress, global minimum-diameter certificate, or
  contact-minimal lexicographic selection is supplied;
- the family is only one local contact component and says nothing about
  contact-isolated source points or the required source cardinality;
- the cell is not embedded as one of the canonical near-disk attachment cells
  with all current Section-122/123 asymptotic hypotheses.

Accordingly, (3.3) cannot be substituted into the global theorem as a disproof.
Its exact conclusion is narrower:

$$
\boxed{
\text{local triangle-free harmonic attachment geometry does not control }a_r-d_r.
}
$$

Any successful bound on the residual must use genuinely additional information,
such as near-rhombic area saturation plus global cell geometry, the actual
diameter graph/KKT response, or a finite source-preserving deformation.

## 5. Interaction with the active C-II endpoint

The current audited Type-II payment is

$$
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\le 10(e_{BB}-k-d_{\rm tile})
 +2\sum_r(a_r-d_r)-4M_{\rm miss}-6C_\partial.
$$

The square-grid family does not validate the right side for a global survivor;
it only blocks the unproved local inequality (1.1). The exact remaining bridge
therefore remains one of:

1. a canonical near-disk/full-core theorem that forces a sufficiently negative
   aggregate $\sum_r(a_r-d_r)$ after all cells and repeated boundary
   occurrences are counted;
2. a source-preserving strict diameter decrease generated by the non-rhombic
   carrier; or
3. an exact unit equilateral triangle forced by the added global hypotheses.

No one of these has been proved here.

## 6. Regression checklist

- **Triangles:** excluded exactly by the parity coloring.
- **Unit separation:** exact from the integer grid.
- **Equilibrium:** (2.1) is an exact vector identity for every unloaded vertex;
  no infinitesimal-to-finite inference is used.
- **Trapping:** all unloaded coordinates lie in the displayed attachment hull.
- **Boundary multiplicity:** no outer-walk claim is made, so bridges or repeated
  occurrences are not silently simplified.
- **Global optimality:** not claimed.
- **Source cardinality:** not claimed.
- **Near-disk force hull:** not claimed.

The regression is therefore compatible with all canonical warnings about
confusing local jamming or harmonic response with global diameter optimality.

## 7. Literature imports

No external theorem is imported. The construction is an explicit subset of
$\mathbb Z^2$, and all claims used in the regression are proved directly.

## 8. Computation

The symbolic formulas (3.1)--(3.4) are the certificate. An auxiliary finite
check was run for $5\le m\le24$, verifying pairwise separation, the four
neighbors and zero vector sum at every $x\in I_m$, and positivity of
$a_m-d_m$. The command was an inline Python check using exact integer
coordinates and `math.hypot` only for the displayed diameter comparison. It is
diagnostic; the all-$m$ proof does not depend on floating-point output.

The check does not test global optimality, a KKT stress, the near-disk force-hull
normalization, or source-cardinality optimality.

## 9. Corrections / supersessions

This report does not supersede a canonical theorem. It narrows the admissible
use of a proposed local implication $a_r\le d_r+O(1)$: that implication is
rejected at the local harmonic/contact-complex scope, while any stronger
global-minimizer version remains unresolved rather than rejected.

## 10. Promotion recommendation

**Regression/rejection only.** Keep the artifact unreviewed and noncanonical.
No theorem-state version, route map, or canonical dependency is changed.

## 11. Handoff

1. Strongest result: an exact square-grid harmonic attachment complex with
   $a_m-d_m=(4-\sqrt2)m+O(1)$.
2. Canonical dependency chain: none; this is a direct finite regression against
   the residual term left by the audited Type-II payment.
3. Exact remaining lemma: use additional near-disk, rhombic-density,
   diameter/KKT, or global-minimality hypotheses to control the aggregate
   $\sum_r(a_r-d_r)$, or replace it by a source-preserving strict descent.
4. Binding dead route: local harmonic equilibrium plus triangle-freeness alone
   cannot provide that control.
5. Files to read next: `docs/targets/target-c/CURRENT.md`,
   `docs/targets/target-c/123-augmented-cell-defect-budget-audit.md`, and
   the audited Type-II report
   `docs/reports/target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md`.
