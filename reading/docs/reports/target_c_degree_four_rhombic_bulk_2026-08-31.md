> Generated reading edition · [exact source](../../../docs/reports/target_c_degree_four_rhombic_bulk_2026-08-31.md) · source SHA-256 `7042ee05bee24fa84a8e3c617d377713519bfa97f1a4b102e778b2c61a03cfd7`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-73DD03A052C6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C73: degree-four rhombic bulk

**Date:** 2026-08-31  
**Repository base:** `e72f0dbd` (main after C72 / PR #76)  
**Run type:** exact planar-curvature / unit-rhombus structure theorem  
**Target:** Target C Gate C-II, C68/C71/C72 anisotropic transport phase  
**Depends on:** C26 fully visible no-neutral theorem, C35 loaded degree cap, C42/C49 face-defect budget and strict quadrilateral faces  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C68 makes a near-zero C-II carrier almost radial in contact-stress measure. C71 reduces
its center to a return component or one dominant physical port. C72 proves that, in
the single-port branch, every pre-leaf graph cut transmits `Omega(D)` total stress and
most of the total alpha mass makes almost maximal radial progress.

A train-track or strip argument also needs control of the local vertex types through
which this stress can travel. C42/C49 controlled faces; C73 upgrades that to vertices.

Let `G=(V,E)` be the complete positive contact core in C-II, with `m=|V|`, loaded
boundary set `B` of size `q`, outer-face walk length `h`, and bounded-face defect

```math
Q:=\sum_{f\text{ bounded}}(k_f-4).
```

Then all but at most

```math
\boxed{39q-40<39\pi D}
```

vertices are interior contact-degree-four vertices incident to four bounded strict
unit-rhombus faces.

Thus, when the force-visible core has quadratic size, a `1-O(1/D)` fraction of its
vertices are clean degree-four rhombic bulk. Only `O(D)` local vertices can support
outer-boundary interaction, nonquadrilateral face incidence, or degree-three/five
branching.

---

## 1. Exact degree-curvature identity

Let `f_b` be the number of bounded contact faces. The face-walk degree sum is

```math
2|E|=h+\sum_{f\text{ bounded}}k_f=h+4f_b+Q.
\tag{C73.1}
```

Since the contact core is connected, Euler gives

```math
f_b=|E|-m+1.
\tag{C73.2}
```

Substitution yields

```math
2|E|=4m-h-Q-4,
```

hence

### Lemma C73.1 — planar degree curvature

```math
\boxed{
\sum_{v\in V}(4-\deg_Cv)=h+Q+4.
}
\tag{C73.3}
```

C49 gives the independent C-II face-defect estimate

```math
\boxed{h+Q\le4q-4.}
\tag{C73.4}
```

---

## 2. Quadrilateral-face angles are strictly between 60 and 120 degrees

C49 proves that every bounded quadrilateral contact face is a strict unit rhombus.
If `theta` is one of its angles, its two diagonal lengths are

```math
2\sin(\theta/2),\qquad2\cos(\theta/2).
```

Both diagonals are at least one by unit separation. Equality is impossible: a unit
diagonal would itself be a contact drawn inside the quadrilateral face, splitting it
into contact triangles. Therefore both diagonals are strictly larger than one, so

```math
\boxed{
\frac\pi3<\theta<\frac{2\pi}{3}.
}
\tag{C73.5}
```

This strict upper angle bound is enough to localize degree-three vertices.

---

## 3. Unloaded degree-three vertices are defect-supported

By C26, every unloaded contact-core vertex has degree `3`, `4`, or `5`. A loaded
boundary vertex has degree at most three by C35. The triangle-free unit-distance
neighbor-angle argument also gives the global contact degree cap five.

Let `N_3` be the number of unloaded degree-three vertices. Suppose such a vertex `v`
is not on the outer-face walk and is not incident to a bounded nonquadrilateral face.
All three local sectors at `v` then belong to bounded quadrilateral faces. By C73.5
each sector angle is strictly below `2pi/3`, but the three sectors around the interior
point must sum to `2pi`, a contradiction.

Thus every unloaded degree-three vertex occurs on the outer face or on a bounded
nonquadrilateral face.

Let

```math
L_{\rm def}:=\sum_{\substack{f\text{ bounded}\\k_f\ge5}}k_f.
```

For each integer `k>=5`,

```math
k\le5(k-4),
```

and therefore

```math
L_{\rm def}\le5Q.
\tag{C73.6}
```

Counting distinct vertices by face-walk incidences gives

### Lemma C73.2 — degree-three localization

```math
\boxed{N_3\le h+5Q.}
\tag{C73.7}
```

---

## 4. Euler curvature also localizes degree five

Let `N_5` be the number of unloaded degree-five vertices and put

```math
D_B:=\sum_{b\in B}(4-\deg_Cb).
```

Every loaded vertex lies in the connected core and C35 gives

```math
1\le\deg_Cb\le3,
\qquad
D_B\le3q.
\tag{C73.8}
```

All unloaded degrees are `3`, `4`, or `5`, so C73.3 becomes

```math
N_3-N_5+D_B=h+Q+4.
```

Hence

```math
N_5=N_3+D_B-(h+Q+4).
\tag{C73.9}
```

Using C73.7-C73.8 gives

### Lemma C73.3 — degree-five localization

```math
\boxed{N_5\le4Q+3q-4.}
\tag{C73.10}
```

So negative degree curvature from degree-five vertices cannot appear quadratically;
it is paid for by the same `O(D)` boundary/face-defect budget.

---

## 5. Clean degree-four bulk

Call a contact-core vertex **face-dirty** if it appears on the outer-face walk or on
the boundary walk of a bounded nonquadrilateral face. By C73.6, the number of
distinct face-dirty vertices is at most

```math
h+5Q.
\tag{C73.11}
```

A vertex that is not face-dirty is interior and every incident face is a bounded
quadrilateral, hence a strict unit rhombus. Lemma C73.2 excludes degree three there.
After removing the `N_5` degree-five vertices, every remaining vertex has degree four
and four incident strict unit-rhombus faces.

The number of exceptions is at most

```math
(h+5Q)+N_5
\le h+9Q+3q-4.
\tag{C73.12}
```

Now use C73.4:

```math
\begin{aligned}
h+9Q+3q-4
&\le9(h+Q)+3q-4\\
&\le39q-40.
\end{aligned}
\tag{C73.13}
```

This proves the main statement.

### Theorem C73 — degree-four strict-rhombus bulk

At least

```math
\boxed{m-39q+40}
```

vertices of the fully force-visible C-II contact core are interior degree-four
vertices incident to four bounded strict unit-rhombus faces.

Consecutive force-hull boundary vertices are unit-separated, so

```math
q\le\operatorname{per}(F)\le\pi D.
\tag{C73.14}
```

Therefore the exceptional set has size at most

```math
\boxed{39\pi D-40=O(D).}
\tag{C73.15}
```

---

## 6. What C73 changes after radial cut transport

C72 already shows that, in the near-zero single-port phase,

- the first port has stress `Omega(D)`;
- every graph-distance layer before a star leaf transmits `Omega(D)` stress;
- an asymptotic fraction at least `sqrt(3)/2` of the full `D^2` contact-stress budget
  lies on graph-outward contacts; and
- alpha-weighted radial progress is `D^2-o(D^2)`.

C73 adds a source-wide combinatorial fact independent of alpha magnitudes: there are
only `O(D)` vertices at which the contact carrier can use a nonquadrilateral face,
outer boundary, or unloaded degree-three/five local topology. Everywhere else the
carrier passes through a degree-four strict-rhombus neighborhood.

This does **not** contradict C72's warning that a fixed alpha measure can ignore
geometrically essential low-stress structure. C73 is useful precisely because its
exception count is weight-free.

---

## 7. Next target: clean-rhombus transport

The next exact question is local.

> **Rhombic transport problem.** Classify positive equilibrium at an interior
> degree-four vertex whose four adjacent faces are strict unit rhombi, and propagate
> that classification across a connected clean-rhombus region.

A sufficient theorem would say that an `Omega(D)` stress flux entering a clean region
either pays a definite C68 transverse/radial defect or is transported through a
fixed-direction strip until one of the `O(D)` C73 exceptional vertices is reached.

No equality of opposite-edge stresses is asserted by C73. Establishing or falsifying
such a propagation law is the immediate next step.

---

## 8. Regression audit

- Large rhombic grids are allowed and saturate the intended clean-bulk picture.
- Degree-three vertices are allowed on the outer face or at nonquadrilateral defects.
- Degree-five vertices are allowed, but only `O(D)` of them.
- Bridges/cutvertices that destroy a clean four-rhombus neighborhood are charged to
  the relevant face-walk defect rather than silently excluded.
- The theorem concerns the force-visible contact core, not fully inactive rattlers.
- No lower bound on individual KKT stresses, periodic lattice assumption, or
  two-connectedness is used.

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C73:
For the C-II contact core, with outer-face length h, face defect
Q=sum_bounded(k_f-4), and loaded boundary count q,
  sum_v(4-deg v)=h+Q+4,
  h+Q<=4q-4.
Every bounded 4-face is a strict unit rhombus with angles in (pi/3,2pi/3).
Therefore
  N3_unloaded<=h+5Q,
  N5_unloaded<=4Q+3q-4.
Hence at most
  h+9Q+3q-4 <=39q-40 <39pi D
vertices fail to be interior degree-four vertices with four incident strict rhombi.

Combined with C72, the near-zero single-port carrier transmits Omega(D) stress through
all graph layers but has only O(D) non-rhombic/non-degree-four structural event sites.
Next: prove/falsify positive-stress propagation through one clean-rhombus region.
```
