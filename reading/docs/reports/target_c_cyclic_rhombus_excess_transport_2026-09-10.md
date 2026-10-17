> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_rhombus_excess_transport_2026-09-10.md) · source SHA-256 `ee836d8c2e77755c49cce5f84dfd0aafe25281c77d41fafea47d951ba127b220`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F47E8F741FC5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic circuit Oler cancellation exposes only O(D) rhombus defect

**Date:** 2026-09-10

**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the cyclic Reuleaux reports in this branch

**Run type:** exact source-population bookkeeping / Target C-to-B bridge

**Target:** post-ZF `s_Z=0`, Woodall cyclic branch `d_H=0`

## LEVEL I STATUS

`STILL OPEN`.

Let `R_4` be the number of bounded quadrilateral contact faces.  C51 makes every such
face a strict convex unit rhombus.  Put

```math
a_0={\sqrt3\over2},\qquad c_0={\sqrt3\over4},
```

and define its total angular-area excess by

```math
\boxed{
E:=\sum_{F\ {
m quadrilateral}}
\bigl(\operatorname{area}F-a_0\bigr)\ge0.
}
\tag{CRE.1}
```

The cyclic circuit identities let the facewise Oler inequalities be summed without
losing this positive excess.  If `N_F` is the **entire source population lying in the
force hull** `F`, including contact-isolated points in bounded contact faces and in the
outer contact face, then

```math
\boxed{
a_0N_F
\le
\operatorname{area}F+c_0P_F+a_0-E.
}
\tag{CRE.2}
```

The C17 Reuleaux container `mathcal R` traps all remaining source points in the convex
caps between `F` and `partial mathcal R`.  Oler on those caps gives, with

```math
\delta_{\mathcal R}:={\pi D^2\over4}-\operatorname{area}(\mathcal R)\ge0,
```

```math
\boxed{
E+\delta_{\mathcal R}
<
c_0\bigl(2P_F+\pi D-2q\bigr).
}
\tag{CRE.3}
```

In particular, since `P_F<=pi D`,

```math
\boxed{E=O(D)}
\tag{CRE.4}
```

uniformly throughout the cyclic circuit branch.

This is stronger than the `o(D^2)` defect one gets from asymptotic area saturation.
It supplies exactly the boundary-order total rhombus angular defect required by the
Target B phase-cut machinery, but it does **not** assert the whole C-II source is
first-order jammed or a pure rhombic disk.  Exceptional bounded faces and outer
pockets remain as train endpoints.

---

## 1. Exact face count in the circuit phase

Let

- `m=|V(C)|` be the nonisolated positive-contact core population;
- `R_4` be the number of bounded quadrilateral faces;
- `f` be the number of bounded exceptional faces;
- `Q=sum(deg(F)-4)` over those exceptional faces;
- `b` be the outer contact-face walk length.

Face incidence and Euler give

```math
4R_4+4f+Q=2e-b,
\tag{1.1}
```

```math
e=m+R_4+f-1.
\tag{1.2}
```

Eliminating `e`,

```math
2m=2R_4+2f+b+Q+2.
\tag{1.3}
```

In the exact cyclic circuit branch,

```math
s_Z=d_H=0,
\qquad h=q,
\qquad b+Q=2h=2q.
\tag{1.4}
```

Therefore

```math
\boxed{m=R_4+f+q+1.}
\tag{1.5}
```

No simplicity assumption on the outer contact walk is used.

---

## 2. Exceptional-face Oler with the quadrilateral excess retained

Let `z_i` be the number of contact-isolated source points in the interior of the
exceptional bounded face `F_i`, and put

```math
r_i:=\deg(F_i)-4,
\qquad k_i=r_i+4.
\tag{2.1}
```

C51 makes `F_i` a convex unit-edge `k_i`-gon.  Oler gives

```math
a_0(k_i+z_i-1)
\le
\operatorname{area}(F_i)+c_0k_i.
\tag{2.2}
```

Since `c_0=a_0/2`, this rearranges to

```math
\operatorname{area}(F_i)
\ge
a_0z_i+a_0+{a_0\over2}r_i.
\tag{2.3}
```

Summing over exceptional faces and writing

```math
Z_{def}:=\sum_i z_i,
```

gives

```math
\boxed{
A_{exc}
\ge
a_0(Z_{def}+f)+c_0Q.
}
\tag{2.4}
```

The quadrilateral faces have total area exactly

```math
A_4=a_0R_4+E.
\tag{2.5}
```

Hence, using (1.5),

```math
\begin{aligned}
a_0(m+Z_{def})
&=a_0R_4+a_0(f+Z_{def})+a_0q+a_0\\
&\le A_4-E+A_{exc}-c_0Q+a_0q+a_0\\
&=A_{bnd}-E-c_0Q+a_0q+a_0.
\end{aligned}
\tag{2.6}
```

---

## 3. Add the internal outer-face isolates

Let `Z_in` be the contact-isolated source points lying in `F` and in the outer
contact face.  OP.1 gives the exact inequality

```math
Z_{in}
\le
{1\over a_0}H+{P_F-b\over2},
\qquad
H=\operatorname{area}F-A_{bnd}.
\tag{3.1}
```

Multiplying by `a_0` and using `c_0=a_0/2`,

```math
a_0Z_{in}
\le H+c_0(P_F-b).
\tag{3.2}
```

Add (2.6) and (3.2).  The exact circuit identity `b+Q=2q` and
`a_0=2c_0` cancel the full graph-boundary contribution:

```math
\begin{aligned}
a_0(m+Z_{def}+Z_{in})
&\le
\operatorname{area}F-E
-c_0(Q+b)+a_0q
+c_0P_F+a_0\\
&=
\operatorname{area}F+c_0P_F+a_0-E.
\end{aligned}
\tag{3.3}
```

The left side is `a_0N_F`.  This proves CRE.2.

The sign of `E` is important.  Ordinary Oler on all points in `F` would simply omit
the final `-E`; the planar face decomposition recovers it exactly.

---

## 4. Oler on the Reuleaux caps outside the force hull

Let `mathcal R` be the unique width-`D` Reuleaux polygon supplied by C17 from the odd
diameter cycle.  The cyclic-cap theorem in this branch proves that every loaded
terminal lies on `partial mathcal R`, and the `q` force-hull sides partition
`mathcal R\setminus F` into `q` convex circular segments `C_j`.

For cap `C_j`, let

- `s_j` be its force-hull chord;
- `phi_j` be its radius-`D` arc angle;
- `z_j` be the number of source points in `C_j\setminus F`.

Every such source point is contact-isolated, but that fact is not needed for Oler.  The
set consisting of the two chord endpoints and those `z_j` points is unit-separated in
`C_j`.  Therefore

```math
a_0(z_j+1)
\le
\operatorname{area}(C_j)
+c_0(s_j+D\phi_j).
\tag{4.1}
```

Hence

```math
a_0z_j
\le
\operatorname{area}(C_j)
+c_0(s_j+D\phi_j)-a_0.
\tag{4.2}
```

The cap interiors are disjoint and exhaust `mathcal R\setminus F`; moreover

```math
\sum_js_j=P_F,
\qquad
D\sum_j\phi_j=\pi D.
\tag{4.3}
```

Thus, for

```math
Z_{ext}:=\sum_jz_j=n-N_F,
```

```math
\boxed{
a_0Z_{ext}
\le
\operatorname{area}(\mathcal R)-\operatorname{area}F
+c_0(P_F+\pi D)-a_0q.
}
\tag{4.4}
```

A source point on a force-hull chord is already in `F`; a source point on a Reuleaux
arc belongs to the unique adjacent cap up to harmless endpoint assignment.  No source
point is double counted.

---

## 5. Global strict lattice comparison gives the defect bound

Add CRE.2 and (4.4):

```math
a_0n
\le
\operatorname{area}(\mathcal R)
+2c_0P_F+c_0\pi D
+a_0-a_0q-E.
\tag{5.1}
```

Subtract `a_0` and use `a_0=2c_0`:

```math
\boxed{
a_0(n-1)
\le
\operatorname{area}(\mathcal R)
+c_0(2P_F+\pi D-2q)-E.
}
\tag{5.2}
```

The canonical strict translated-lattice comparison for a global minimizer is

```math
a_0(n-1)>{\pi D^2\over4}.
\tag{5.3}
```

Write

```math
\delta_{\mathcal R}:={\pi D^2\over4}-\operatorname{area}(\mathcal R)\ge0,
\tag{5.4}
```

where nonnegativity is the planar isodiametric inequality because `mathcal R` has
diameter `D`.  Comparing (5.2) and (5.3) gives exactly

```math
\boxed{
E+\delta_{\mathcal R}
<
c_0(2P_F+\pi D-2q).
}
\tag{5.5}
```

This proves CRE.3.

Since `q>=0` and `P_F<=pi D`,

```math
E<3\pi c_0D,
\tag{5.6}
```

which proves CRE.4.  One may retain the favorable `-2q` and
`delta_{mathcal R}` terms in later cyclic estimates.

---

## 6. Consequence for rhombic train geometry

For a strict unit rhombus with acute angle `theta in (pi/3,pi/2]`, its area excess is

```math
\sin\theta-a_0>0.
```

The Target B phase-cut theorem PC applies to any finite strict unit-rhombus complex
satisfying the shared train geometry; it does not require the complex itself to be a
global minimizer for its purely combinatorial/angular conclusion.  Its angular-defect
budget `Delta_train` satisfies

```math
{3\Delta_{train}\over\pi}
\le(2+\sqrt3)E.
\tag{6.1}
```

Therefore CRE.4 implies

```math
\boxed{\Delta_{train}=O(D).}
\tag{6.2}
```

and PC deletes only `O(D)` rhombus-crossing relations to obtain an exact acyclic real
phase potential on the remaining train graph.

This is a legitimate C-II-to-Target-B transfer because it concerns only the actual
strict rhombic bounded faces of the same contact core.  It does **not** import Target
B's jammed-source edge count, pure-disk identity, or shell conclusion.

---

## 7. Scope and regressions

- Exceptional bounded faces are retained and become train endpoints; they are not
  filled by fictitious rhombi.
- The outer contact region and all OP pockets are retained.
- Contact-isolated source points outside `F` are counted capwise in (4.4); no small
  isolate hypothesis is imposed.
- The regular odd shell has no quadratic rhombic sea and is not contradicted by CRE.
- CRE.4 alone does not imply a coherent three-phase core; the Target B sliding-interval
  regression still applies to abstract dense train graphs.
- No active diameter constraint is moved.  PC is used only as a graph/phase theorem,
  not as a physical deformation.

## 8. Exact next obligation

In the cyclic `0.952890...` equality-near normal form, the exceptional-face estimate
forces one macroscopic near-isoperimetric face and leaves a quadratic area of strict
rhombi between that face and the almost circular outer force hull.  CRE proves that
those rhombi have only `O(D)` total angular defect.

The next branch-specific target is therefore:

> **Annular phase-density theorem.**  For a strict unit-rhombic complex occupying all
> but `o(D^2)` of the region between an almost circular outer boundary and one
> near-circular macroscopic exceptional face, with `T=O(D)` stopped trains and total
> angular defect `O(D)`, prove that either the promoted NE coherent-core hypotheses
> hold on a quadratic fraction of the rhombi, or the exact shell/population surplus
> contradicts the cyclic source bound.

No such theorem is asserted here.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In s_Z=d_H=0:
    b+Q=2q,
    m=R_4+f+q+1.
Write A_4=a0 R_4+E.
Exceptional-face Oler gives
    A_exc >= a0(Z_def+f)+c0 Q.
OP.1 gives
    a0 Z_in <= H+c0(P_F-b).
After exact cancellation using b+Q=2q and a0=2c0:
    a0 N_F <= area(F)+c0 P_F+a0-E.

C17/CRC partition R\F into q convex Reuleaux caps.  Oler on each cap, including its
two loaded endpoints, gives
    a0 Z_ext <= area(R)-area(F)+c0(P_F+pi D)-a0 q.
Adding and using the strict translated-lattice comparison
    a0(n-1)>pi D^2/4
proves
    E+delta_R < c0(2P_F+pi D-2q).
Hence E=O(D) throughout the cyclic circuit branch.

Therefore the actual rhombic faces satisfy the Target B phase-cut angular-defect
hypothesis at boundary order, without importing Target B jamming or pure-disk
assumptions.
```
