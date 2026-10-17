> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_macroscopic_rhombic_component_2026-09-09.md) · source SHA-256 `f5b575a2440c34f0299d57bc88230e875d84fbbed6eef3282c131b6b067f6a31`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-06E93C7155C5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZRC: linear defect forces one quadratic rhombic sea

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** component extraction from ZCQ/C42 stopped-train topology  
**Target:** Target C, ZCQ-ZRI train branch  
**Depends on:** ZCQ, C42/C51, DT, post-ZF exact terminal ledger  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZCQ gives a quadratic force-visible core and C42 gives `Omega_eta(D^2)` strict-rhombus faces with only `O(D)` total outer/nonquadrilateral face-edge incidence. This report shows that those rhombi cannot be fragmented into only thin components.

Decompose the strict-rhombus faces by edge adjacency. For each component, its boundary edges are exactly contacts whose other side is the outer face or a bounded nonquadrilateral face. The train decomposition internal to that component gives

```math
B_i=2T_i,
\qquad
R_i\le T_i^2/4=B_i^2/16,
```

where `R_i,T_i,B_i` are its rhombi, stopped trains, and boundary-edge incidences. The global boundary-incidence budget is only `O(D)`.

A Cauchy-type concentration argument then forces one edge-connected pure-rhombic component with `Omega_eta(D^2)` faces and `Omega_eta(D)` stopped trains. ZRI's exceptional face population is `o(D^2)`, so almost every face of this single macroscopic component still has two weak transverse sides.

This turns the low-reset survivor into one genuine macroscopic rhombic sea with holes/defect boundary of only linear total length. The next deformation problem can therefore be posed on one connected quad complex rather than on a diffuse family of strips.

---

## 1. Rhombic face components

Let

```math
\mathcal R
```

be the set of bounded strict-rhombus faces of the force-visible contact core. ZCQ+C42 gives a fixed constant `c_eta>0` such that

```math
\boxed{
R:=|\mathcal R|
\ge(c_\eta-o(1))D^2.
}
\tag{ZRC1}
```

Make a graph on `mathcal R` by joining two rhombi when they share a contact edge. Let its connected components be

```math
\mathcal R_1,\ldots,\mathcal R_s,
```

and write

```math
R_i:=|\mathcal R_i|.
```

For component `i`, let `B_i` be the number of contact edges incident to exactly one rhombus of `mathcal R_i`.

If a contact edge of a rhombus has a rhombus on its other side, that second rhombus lies in the same edge-adjacency component. Therefore every boundary edge counted by `B_i` has on its other side either

- the outer face, or
- a bounded nonquadrilateral face.

Conversely every rhombus-side incidence with one of those defect faces is a component-boundary edge.

Different rhombic components cannot share a contact edge. Hence

```math
\boxed{
\sum_i B_i
\le
E_{def},
}
\tag{1.1}
```

where

```math
E_{def}
:=b+\sum_{F\text{ bounded non4}}\deg F
=b+Q+4f.
\tag{1.2}
```

---

## 2. The post-ZF ledger gives a 6q boundary budget

The exact post-ZF face identity gives

```math
\frac{b+Q}{2}=h-s_Z,
```

where now `h=|H|` is the number of actual diameter pairs. Hence

```math
b+Q\le2h\le2q.
\tag{2.1}
```

The exact terminal partition

```math
q=x_B+f+g_F+2d_H+2s_Z
```

gives

```math
f\le q.
\tag{2.2}
```

Therefore

```math
\boxed{
E_{def}=b+Q+4f\le6q\le6\pi D.
}
\tag{ZRC2}
```

Thus

```math
\boxed{
\sum_i B_i\le6\pi D.
}
\tag{ZRC3}
```

This is sharper in the post-ZF branch than the older generic C42.4 incidence bound.

---

## 3. Exact component train count

Fix one rhombic component `mathcal R_i`.

Let `E_i` be the number of distinct contact edges belonging to at least one face of the component. Face-edge incidence gives

```math
4R_i
=2(E_i-B_i)+B_i,
```

so

```math
E_i=2R_i+\frac{B_i}{2}.
\tag{3.1}
```

Inside the component, connect opposite contact edges across each rhombus as in DT. There are `E_i` edge-vertices and exactly `2R_i` train links.

DT's monotone-projection argument excludes train cycles even in the presence of holes. Therefore this edge-link graph is a forest of paths. Its number `T_i` of components is

```math
T_i=E_i-2R_i.
```

Using (3.1),

```math
\boxed{
T_i=\frac{B_i}{2}.
}
\tag{ZRC4}
```

Equivalently, every component train has two boundary contact edges, with all boundary components and holes counted automatically.

---

## 4. Componentwise train isoperimetry

The train crossing graph of `mathcal R_i` has

- `T_i` vertices;
- `R_i` edges, one per rhombus;
- no loops or multiple crossings by DT;
- no triangles by the strict `(60,120)` rhombus angle geometry.

Mantel therefore gives

```math
R_i\le\frac{T_i^2}{4}.
```

Using ZRC4,

```math
\boxed{
R_i\le\frac{B_i^2}{16},
\qquad
B_i\ge4\sqrt{R_i}.
}
\tag{ZRC5}
```

This is valid for an edge-connected rhombic component with arbitrary holes or pinched boundary topology; no simply connected disk hypothesis is used.

---

## 5. One component has quadratic area scale

Let

```math
M:=\max_i R_i.
```

Then

```math
\begin{aligned}
R
&=\sum_i R_i\\
&=\sum_i \sqrt{R_i}\sqrt{R_i}\\
&\le\sqrt M\sum_i\sqrt{R_i}\\
&\le\frac{\sqrt M}{4}\sum_iB_i\\
&\le\frac{3\pi}{2}D\sqrt M,
\end{aligned}
```

where ZRC5 and ZRC3 were used.

Hence

```math
\sqrt M
\ge
\frac{2R}{3\pi D}.
```

By ZRC1,

```math
\boxed{
M
\ge
\left(\frac{4c_\eta^2}{9\pi^2}-o(1)\right)D^2.
}
\tag{ZRC6}
```

Choose a component `mathcal R_*` attaining `M`, and write

```math
R_*=M,
\quad B_*=B_i,
\quad T_*=T_i.
```

Then

```math
\boxed{
R_*=\Omega_\eta(D^2).
}
\tag{ZRC7}
```

By ZRC4-ZRC5,

```math
T_*=\frac{B_*}{2}\ge2\sqrt{R_*},
```

so

```math
\boxed{
T_*
\ge
\left(\frac{4c_\eta}{3\pi}-o(1)\right)D.
}
\tag{ZRC8}
```

Thus one edge-connected pure-rhombic component already carries linear train complexity.

---

## 6. ZRI weakness persists on the macroscopic component

ZRI has only

```math
o(D^2)
```

exceptional strict-rhombus faces globally. Since `R_*=Omega_eta(D^2)`, their intersection with `mathcal R_*` is `o(R_*)`.

Therefore

```math
\boxed{
R_{*,good}=R_*-o(D^2)=R_*-o(R_*)
}
\tag{ZRC9}
```

faces of the macroscopic component each have at least two nonradial boundary contacts with stress below the ZRI weak scale `a_D->0`.

Applying the ZWT assignment argument **inside this one component** gives a linear family of weak-rich component trains. In particular there are constants `c'_eta,k'_eta>0` such that

```math
\boxed{
\text{at least }c'_\eta D\text{ trains of }\mathcal R_*
\text{ are weak on at least }k'_\eta D\text{ rhombi.}
}
\tag{ZRC10}
```

Using ZEA, a linear subfamily has endpoint-anchored macroscopic weak strips on the boundary of the same rhombic component.

---

## 7. Topological concentration of the remaining obstruction

The full rhombic component boundary length satisfies

```math
B_*\le E_{def}\le6\pi D.
\tag{7.1}
```

Thus the ZCQ/ZRI branch contains one connected quad complex with

```text
Omega_eta(D^2) strict unit rhombi,
Omega_eta(D) stopped trains,
O(D) total boundary length,
1-o(1) fraction of faces carrying weak transverse sides,
linear many endpoint-anchored macroscopic weak train strips.
```

Holes and pinches are still allowed, but all of their boundary complexity is contained in the same `O(D)` budget.

This is a stronger geometric endpoint than a diffuse quadratic face population.

---

## 8. Why this does not yet import the pure-disk Target-B theorem

`mathcal R_*` need not be simply connected. Its holes may contain bounded nonquadrilateral faces, contact subgraphs, or other rhombic components. More importantly, ZCQ supplies only a positive quadratic face coefficient depending on `eta`; it does not prove that the component is near full disk packing capacity or that its total rhombus area excess is `o(D^2)`.

Therefore the Target-B phase-atomic exposed-hull theorem cannot simply be quoted as a contradiction.

What ZRC does justify is using one connected rhombic complex as the object for a new deformation/period analysis. The only topological obstructions to pure train-angle realization now live on `O(D)` boundary/holes rather than in a quadratic defect set.

---

## 9. Exact next theorem

The next high-value target is a **holed train-angle locking theorem**:

> For an edge-connected strict-rhombic component with `Omega(D^2)` faces, `Omega(D)` trains, and only `O(D)` total boundary, quantify the train-angle deformation space after imposing the finite period constraints coming from holes and the actual outer/exceptional attachment constraints. Show that the ZRI/ZWT weak-transverse normal form leaves a nontrivial diameter-nonincreasing mode, or else forces a linear boundary/period rank incompatible with ZSP/ZHA/PI.

This is the correct place to adapt the mature Target-B train-angle Hessian machinery. Reusing the simply connected formulas without the hole-period constraints would be invalid.

---

## 10. Classification

**Status:** proved report-level macroscopic-component extraction theorem.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
