> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_train_mantel_phase_star_endpoint_2026-09-14.md) · source SHA-256 `85666aeabb0f209e1f96d0014c5bf0b5569ebb30f544cedb7714ad2666648bdc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-0B796CCBDA65","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_train_mantel_phase_star_endpoint_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=21fdc5a9d34ca42326739a53a85ff6e109061c3d; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Mantel-extremal train graph at the full-core floor endpoint

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** exact asymptotic endpoint reduction / adversarial audit
**Target:** Target C-II / Level I
**Status:** unreviewed; no theorem-state promotion requested

## LEVEL I STATUS

`STILL OPEN`

This report does not settle Erdős Problem #99. It proves a new necessary structure for
any full-core sequence attaining the current loaded-chord/train-surplus floor. The
strict-rhombus train-crossing graph is asymptotically Mantel-extremal, and after the
canonical (O(D)) phase cut its three phase classes form a near-extremal
three-partite system. The unresolved step is still the geometric transfer from this
near-extremal, potentially holed/interface-bounded train system to a source-preserving
strict diameter decrease or an exact unit equilateral triangle.

## 1. Scope and candidate implication chain

Work only in the canonical full-core, no-macroscopic-container, near-disk Type-II
branch. Let (D	oinfty) along a sequence of triangle-free global minimizers in the
canonical contact-minimal, diameter-pair-minimal normal form. Let

* (mathcal R_D) be the complete set of bounded strict unit-rhombus contact faces;
* (R_D=|mathcal R_D|);
* (B_D) be the occurrence-counted boundary-edge number of this rhombus complex;
* (Gamma_D) be its train-crossing graph;
* (T_D=|V(Gamma_D)|) be the number of local train segments;
* (b_D) be the occurrence-counted outer contact-face walk length;
* (f_D) be the number of bounded nonquadrilateral contact faces; and
* (Q_D=sum_P(deg P-4)), summed over bounded nonquadrilateral faces.

The canonical endpoint assumptions used here are

[
 {R_Dover D^2}	oDelta_2:={piover2sqrt3},qquad
 {b_Dover D}	opi,qquad
 {Q_D-f_Dover D}	o0,
\tag{1.1}
]

and

[
 {f_Dover D}	o f_{
m TC}:={4sqrt{Delta_2}-piover5}.
\tag{1.2}
]

The value in (1.2) is the equality value from the canonical train-coupled surplus
floor. The candidate chain is

```text
floor equality
  -> rhombus-boundary count asymptotically saturates both train inequalities
  -> train-crossing graph has R/T^2 -> 1/4
  -> O(D) phase cut gives a near-extremal three-class crossing system
  -> near-extremal phase-star geometry / hole-interface transfer
  -> strict source-preserving descent or exact unit triangle.
```

Only the first four arrows are proved below. The last arrow is not asserted.

## 2. Exact boundary squeeze at the floor endpoint

Canonical train-boundary accounting gives the two finite inequalities

```math
 4\sqrt{R_D}le B_D,
\tag{2.1}
```

and

```math
 B_Dle b_D+4f_D+Q_D.
\tag{2.2}
```

The first is the track/Mantel boundary bound. The second counts every rhombic
boundary occurrence by the old outer contact face or a bounded nonquadrilateral face;
it is an occurrence count, so bridges, repeated outer vertices, holes, and interface
occurrences are not simplified away.

Using (1.1) and (1.2),

```math
 {4\sqrt{R_D}\over D}	o4\sqrt{\Delta_2},
```

while

```math
 {b_D+4f_D+Q_D\over D}
\to \pi+5f_{
m TC}
 =\pi+4\sqrt{\Delta_2}-\pi
 =4\sqrt{\Delta_2}.
```

Thus the squeeze in (2.1)--(2.2) is asymptotically sharp:

```math
\boxed{
 {B_D\over D}	o4\sqrt{\Delta_2}=3.809251227455829\ldots .
}
\tag{2.3}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The exact numerical value is orientation only; the proof uses the symbolic identity
\(pi+5f_{
m TC}=4\sqrt{\Delta_2}).
```



The train convention in the canonical theorem gives exactly two boundary-edge
occurrences per local train segment, including holes and all other boundary
components. Therefore

```math
 T_D={B_D\over2},
\qquad
 {T_D\over D}	o2\sqrt{\Delta_2}.
\tag{2.4}
```

Since each rhombus is one crossing edge of (Gamma_D), (1.1), (2.3), and (2.4)
give

```math
\boxed{
 {R_D\over T_D^2}	o {\Delta_2\over4\Delta_2}={1\over4}.
}
\tag{2.5}
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
This is stronger than merely knowing that the train graph has positive crossing
density: it approaches equality in the exact Mantel bound
\(R_D\le T_D^2/4\).
```



## 3. Phase cut and three-class near-extremality

The canonical phase-circle cut applies to the full strict-rhombus train graph. It
removes a set (F_D) of crossing edges with

```math
 |F_D|=O(D),
\tag{3.1}
```

and assigns every train segment a label in (mathbb Z/3mathbb Z). Every retained
crossing joins two distinct labels. Two trains with the same label cannot cross: all
reduced phases lie in one open interval of length (pi/3), while a strict
triangle-free unit rhombus requires acute projective separation strictly greater than
(pi/3). This use of strictness is valid for the actual source; it is not a generic
perturbation claim.

Let the three label classes have sizes (M_Dge b_D^{\rm ph}ge a_D^{\rm ph}), and
let (E_D^{\rm ph}) be the number of retained crossing edges. To avoid collision with
the outer-walk variable (b_D), write these class sizes as (M_D,U_D,V_D) below:

```math
 M_D\ge U_D\ge V_D,
\qquad M_D+U_D+V_D=T_D.
\tag{3.2}
```

Then

```math
 E_D^{\rm ph}=R_D-O(D),
\qquad
 {E_D^{\rm ph}\over T_D^2}	o{1\over4}.
\tag{3.3}
```

### Lemma 3.1 — three-partite triangle-free phase bound

Let a tripartite graph have class sizes (M\ge U\ge V), no triangle with one
vertex in each class, and edge count (E). Then

```math
\boxed{E\le M(U+V).}
\tag{3.4}
```

#### Proof

Write

```math
 x=MU-e_{MU},
 \qquad y=MV-e_{MV},
```

for the missing edges in the two pairs incident with the largest class. For every
edge (uv) between the (U)- and (V)-classes, the neighborhoods of (u) and
(v) in the (M)-class are disjoint. Hence, if (d_M(u)) and (d_M(v)) denote
those two degrees,

```math
 d_M(u)+d_M(v)\le M.
```

Summing over all (UV)-edges gives

```math
 M e_{UV}
 \le Vx+Uy
 \le M(x+y),
\tag{3.5}
```

because (U,V\le M). Thus (e_{UV}\le x+y), and

```math
 E=e_{MU}+e_{MV}+e_{UV}
 =M(U+V)-x-y+e_{UV}
 \le M(U+V).
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
This proves (3.4). \(square)
```



Apply (3.4) to (3.2)--(3.3). Since

```math
 M_D(T_D-M_D)\le {T_D^2\over4},
```

we obtain

```math
 {T_D^2\over4}-o(T_D^2)
 \le E_D^{\rm ph}
 \le M_D(T_D-M_D).
\tag{3.6}
```

The quadratic (z(1-z)) has its unique maximum (1/4) at (z=1/2). Therefore

```math
\boxed{
 {M_D\over T_D}\to{1\over2},
 \qquad
 {U_D+V_D\over T_D}	o{1\over2}.
}
\tag{3.7}
```

Moreover, defining the phase-star deficit

```math
 \Delta_D^{\rm ph}:={M_D(U_D+V_D)-E_D^{\rm ph}\over T_D^2}\ge0,
```

the same squeeze gives

```math
\boxed{
 \Delta_D^{\rm ph}\to0.
}
\tag{3.8}
```

Equations (3.7)--(3.8) are the exact near-extremal phase-star reduction. They do not
claim that either center-to-leaf pair is individually near-complete; that additional
stability statement requires a separate finite graph argument and, for the geometric
diameter step, an interface-stable train-order theorem.

## 4. What the endpoint reduction does and does not give

The endpoint now has the following simultaneous source-level structure:

```math
\begin{array}{rcl}
R_D/D^2&\to&\Delta_2,\\
T_D/D&\to&2\sqrt{\Delta_2},\\
R_D/T_D^2&\to&1/4,\\
M_D/T_D&\to&1/2,\\
\Delta_D^{\rm ph}&\to&0.
\end{array}
\tag{4.1}
```

The endpoint is therefore not a free scalar compatibility witness: it is forced into a
near-Mantel, near-three-partite-extremal train geometry. This is a genuine narrowing
of the current floor endpoint.

There are two mathematically distinct remaining possibilities.

### 4.1 Near-extremal phase-star transfer

One needs a theorem that turns (4.1), together with the actual train-centerline
geometry, into one of the following:

1. a center-to-leaf complete or almost-complete phase grid with dimensions large
   enough for the trimmed-grid diameter inequality;
2. a direct ordered near-grid diagonal estimate that tolerates (o(T_D^2)) missing
   crossings; or
3. a source-preserving finite deformation of the actual contact configuration.

The current canonical complete-grid theorem handles a complete phase-pure grid even
with holes, but (4.1) gives only near-extremality. A general graph cannot be replaced
by a complete grid from (o(T_D^2)) missing edges: random sparse missing-edge patterns
can have no linear-by-linear complete subgraph. The train arcs and their boundary
budget are the needed extra geometry, and that stability theorem has not been proved.

### 4.2 The phase-cut/interface mismatch

The phase cut removes crossing relations, not source points or physical contact edges.
The deleted relations are (O(D)), while the nonquadrilateral-face and hole/interface
boundary is also allowed to be (O(D)). No source-preserving operation may silently
delete the cut crossings, fill the holes, or identify the phase-cut train graph with a
new contact source. Thus (4.1) cannot yet be fed directly into a global diameter
comparison.

The exact missing implication is

```math
\boxed{
\text{(4.1) + actual holed/interface train geometry}
\Longrightarrow
\text{unit equilateral triangle or strict same-cardinality sub-}D(n)\text{ source}.
}
\tag{4.2}
```

This is a source-level statement. A positive KKT force, a graph edge deletion, or an
abstract train rerouting is not a substitute for (4.2).

## 5. Regression audit

* The regular odd shell has a triangle-free diameter graph and does not approach the
  full-core train-floor endpoint under the canonical rhombic-cell hypotheses; no
  global-minimality conclusion is drawn from it.
* The vanishing-shear oblique lattice shows that near-triangular density and
  (O(D)) total angular defect do not force an exact equilateral triangle. It is not a
  global minimizer and is not used to disprove (4.2).
* The five-sector and plus-shaped complexes show that positive local stress and
  diametral hull vertices do not force a global descent. They do not satisfy the
  quadratic near-disk floor endpoint.
* Holes, bridges, and repeated boundary occurrences remain counted. The squeeze uses
  occurrence-counted (B_D) and (b_D), not distinct boundary vertices.
* Contact-isolated source points remain in the full source. None occurs in
  (R_D,T_D,Gamma_D) merely by notation, and no isolate is deleted or repacked.
* The rejected full-source affine-kernel extension is not invoked.
* No incident-diameter Euler path, matching assumption, or KKT multiplier lower bound
  is used.

## 6. Dependency and status audit

The proof uses only the following canonical inputs:

* `C-FULLCORE-NEAR-DISK` / Sections 79--80 for the full-core Type-II setting and
  (R_D/D^2	oDelta_2);
* `C-HARMONIC-CELL-TILING` and `C-HARMONIC-CARRIER-QUAD` for the occurrence-counted
  rhombus boundary inequalities;
* `C-FULLCORE-TRAIN-SURPLUS-FLOOR` for the endpoint value (1.2);
* the canonical train theorem for (T_D=B_D/2), the triangle-free train graph, and
  the phase-circle cut; and
* the elementary tripartite Lemma 3.1 proved above.

No unpromoted Target B stability theorem is used as a premise. In particular, the
report does not cite the pure-disk near-extremal phase-star exclusions as if they
already applied to a holed full-core carrier.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The report is asymptotic and conditional on a sequence attaining
\(mu_D\to\mu_{\rm TC}\). It supplies no uniform finite threshold and no implication
for the higher-surplus branch $`\liminf\mu_D>\mu_{\rm TC}`$.
```



## 7. Handoff

The exact endpoint chain is now:

```text
mu_D -> mu_TC
  -> B_D/D -> 4 sqrt(Delta_2), T_D/D -> 2 sqrt(Delta_2)
  -> R_D/T_D^2 -> 1/4
  -> after O(D) phase cut:
       largest phase = T_D/2+o(T_D),
       phase-star deficit = o(T_D^2)
  -> unresolved near-extremal holed-train stability / source-preserving descent.
```

The higher-surplus full-core branch and the entire macroscopic-container branch remain
uncovered. No canonical file or theorem-state entry is changed by this report.
