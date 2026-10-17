> Generated reading edition · [exact source](../../../docs/reports/target_c_macroscopic_rhombic_component_consolidation_2026-09-11.md) · source SHA-256 `e3489482c4f0e6f21d68aa3e2eaab7aba8bdd42a59f9843631ab4a71d54c52ed`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-150C013B4D78","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_macroscopic_rhombic_component_consolidation_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=db298f29c3b581214e236efd7eb5a9744ef467b8; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — macroscopic rhombic-component consolidation

**Date:** 2026-09-11  
**Repository base:** `053e1e1b85643b738b4cde306838d150ea325783` plus GA on this branch  
**Run type:** exact planar consolidation / dense-core reduction  
**Target:** Target C post-ZF dense force-visible core  
**Depends on:** C42 quadrangulation defect, ZE/ZT boundary ledger, GA global rhombus defect only for the phase corollary  
**External input:** planar isoperimetric inequality

## LEVEL I STATUS

`STILL OPEN`.

C42 says a quadratic force-visible core has a quadratic number of strict unit-rhombus
bounded faces and only boundary-order nonrhombic combinatorial defect.  A possible
escape was that `O(D)` exceptional structure could split the rhombi into many thin
components, leaving no macroscopic rhombic domain to which the Target B phase tools
apply.

That escape is impossible.  The total unit-edge boundary length of **all** rhombic-face
components is itself `O(D)`.  Isoperimetry then forces one edge-connected rhombic
component to contain a fixed positive fraction on the `D^2` scale whenever the total
rhombus count does.

---

## 1. Rhombic face components

Let `R` be the number of bounded quadrilateral contact faces.  C51 makes each such
face a strict convex unit rhombus.

Form the face adjacency graph whose vertices are these rhombi and whose edges join two
rhombi sharing a contact edge.  Let

$$
\mathcal R_1,\ldots,\mathcal R_g
$$

be its connected components, and write

$$
R_j=|\mathcal R_j|.
$$

Let `U_j` be the closed polygonal region obtained by the union of the rhombi in
`mathcal R_j`.  The interiors of the rhombi are disjoint, so

$$
\operatorname{area}U_j
=\sum_{F\in\mathcal R_j}\operatorname{area}F
\ge a_0R_j,
\qquad a_0={\sqrt3\over2}.
\tag{1.1}
$$

Let `B_j` be the total number of unit contact-edge occurrences on all boundary
components of `U_j`.  Thus its total geometric boundary length is `B_j`.

---

## 2. Total rhombic boundary is only O(D)

A contact edge on the boundary of a rhombic component is incident on its other side to
one of:

1. the unbounded contact face; or
2. a bounded nonquadrilateral contact face.

Therefore, counting incidences,

$$
\boxed{
\sum_jB_j
\le b+\sum_{F\ {
m exceptional}}\deg F.
}
\tag{2.1}
$$

Write `f` for the number of exceptional bounded faces and

$$
Q=\sum_F(\deg F-4).
$$

Every exceptional face has degree at least five, so `f<=Q`, and

$$
\sum_F\deg F=4f+Q\le5Q.
\tag{2.2}
$$

Hence

$$
\boxed{
B_{tot}:=\sum_jB_j\le b+5Q.
}
\tag{2.3}
$$

Post-ZF gives

$$
b+Q=2(h-s_Z)\le2q,
\qquad Q\le q,
\qquad q\le\pi D.
$$

Consequently

$$
\boxed{B_{tot}\le7\pi D.}
\tag{2.4}
$$

The numerical constant is crude but finite and universal.

---

## 3. Isoperimetry forces one quadratic rhombic component

The connected polygonal region `U_j` may have holes.  Its area is at most the area
enclosed by its outer boundary.  The outer boundary length is at most the total
boundary length `B_j`.  Therefore the planar isoperimetric inequality gives

$$
\operatorname{area}U_j\le{B_j^2\over4\pi}.
$$

Together with (1.1),

$$
\boxed{
R_j\le {B_j^2\over4\pi a_0}.}
\tag{3.1}
$$

Let

$$
R_{max}:=\max_jR_j.
$$

Equation (3.1) also gives

$$
B_j\ge\sqrt{4\pi a_0R_j}.
$$

Since `R_j<=R_max`,

$$
\sqrt{R_j}\ge {R_j\over\sqrt{R_{max}}}.
$$

Thus

$$
\begin{aligned}
B_{tot}
&\ge\sqrt{4\pi a_0}\sum_j\sqrt{R_j}\\
&\ge\sqrt{4\pi a_0}\,{\sum_jR_j\over\sqrt{R_{max}}}.
\end{aligned}
$$

Rearranging proves the finite consolidation inequality

### Theorem RC.1 — rhombic component concentration

$$
\boxed{
R_{max}
\ge
{4\pi a_0\,R^2\over B_{tot}^2}.
}
\tag{RC.1}
$$

Using (2.4),

$$
\boxed{
R_{max}
\ge
{4\pi a_0\over49\pi^2}\,{R^2\over D^2}
={2\sqrt3\over49\pi}{R^2\over D^2}.
}
\tag{RC.2}
$$

Therefore, if along a post-ZF sequence

$$
R\ge r_0D^2
$$

for a fixed `r_0>0`, then some edge-connected rhombic component satisfies

$$
\boxed{
R_j\ge
{2\sqrt3\over49\pi}r_0^2D^2.
}
\tag{RC.3}
$$

So `O(D)` exceptional structure cannot fragment a quadratic rhombic sea into only
subquadratic grains.

---

## 4. Dense-core consequence

C42 gives

$$
R\ge m-5q+3c_I+3e_{BB}+5.
$$

Since `q=O(D)`, any sequence with

$$
\liminf {m\over D^2}>0
$$

also has

$$
\liminf {R\over D^2}>0.
$$

RC.3 therefore gives:

### Corollary RC.2 — every quadratic post-ZF core contains a quadratic rhombic domain

If the force-visible contact core has positive quadratic density, then one
edge-connected component of its strict-rhombus bounded faces contains
`Omega(D^2)` rhombi and has Euclidean area `Omega(D^2)`.

Its total boundary length is `O(D)` because it is at most `B_tot`.

This statement allows holes, exceptional faces, outer-face boundary arcs, and loaded
vertices on its boundary.  No pure-disk conclusion is asserted.

---

## 5. GA phase consequence inside the macroscopic component

GA proves for the **entire** post-ZF source

$$
E=O(D),
$$

where `E` is the sum of strict-rhombus area excesses above `a_0`.  Therefore the
macroscopic component from RC.2 satisfies the same bound on its sub-sum:

$$
E_j=O(D).
$$

The promoted Target B phase-cut theorem then gives boundary-order total angular defect
and removes only `O(D)` crossing relations from the train graph of this component.
Thus every quadratic force-visible core contains an actual quadratic rhombic domain
with:

$$
\boxed{
R_j=\Omega(D^2),\qquad
B_j=O(D),\qquad
E_j=O(D).
}
\tag{RC.4}
$$

This is precisely the scale at which the distributed-strain / phase-density problem
is meaningful; the defect cannot be hidden by splitting the rhombi into only small
pieces.

---

## 6. Scope

- The macroscopic component may be multiply connected.  Pure-rhombic-disk exclusion
  ZB cannot be applied without an additional topology argument.
- RC does not say this component carries a fixed fraction of KKT stress; stress can
  remain anisotropic and concentrated elsewhere.
- One exceptional face of degree `Theta(D)` is allowed and may form a macroscopic
  hole.
- A component can have several phase grains internally; RC is face connectivity, not
  affine-lattice coherence.
- If the force-visible core is only `o(D^2)`, RC makes no assertion.  That is the
  isolate-dominated source branch.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let R_j be the edge-connected components of bounded strict-rhombus faces and B_j their
total unit-edge boundary lengths.  Every boundary edge sees either the outer face or
an exceptional bounded face, so
    sum B_j <= b+sum_exc deg F <= b+5Q <=7pi D.
For each component,
    a0 R_j <= area(U_j) <= B_j^2/(4pi).
Therefore
    R_max >= 4pi a0 R^2/(sum B_j)^2.
If R=Omega(D^2), then R_max=Omega(D^2).

C42 makes R=Omega(D^2) whenever the force-visible core is quadratic.  GA gives total
rhombus area/angular defect E=O(D).  Hence every quadratic post-ZF core contains one
edge-connected rhombic domain with
    R_j=Omega(D^2), boundary O(D), angular defect O(D).
The remaining issue is topology/phase density, not fragmentation into tiny grains.
```
