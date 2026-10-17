> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_macroscopic_interface_face_collapse_2026-09-09.md) · source SHA-256 `559b473fc43c9563294c0ba1b8dcd91832ad38a39c70ee9c25d16c3c759dadcd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 15 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-B3E79813F485","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_macroscopic_interface_face_collapse_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=4c08eceaba36d1b4108901e2db07d8fde5c80cfe; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — macroscopic loaded-interface faces collapse to doubled contact geodesics

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** asymptotic convex-face classification  
**Target:** full-core near-circle endpoint after GP/FS  
**Depends on:** C51 bounded-face convexity, CE/UF full-core rhombus density and area-excess collapse, DC force-hull disk convergence, GP loaded-interface defect theorem  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

GP proves that every full-core near-circle survivor has loaded-interface bounded-face defect

```math
Q_B\ge(2-o(1))D.
```

The principal remaining regression is that a bounded number of giant exceptional faces might carry this linear defect while using very few loaded-terminal interior-contact slots.

C51 and full-core rhombus saturation sharply classify that regression.

Let `F_j` be any sequence of bounded exceptional contact faces with degrees `k_j` in a full-core near-circle survivor of diameter `D_j->infinity`. If

```math
\frac{k_j}{D_j}\to\lambda>0,
```

then, after scaling by `D_j` and taking a subsequence, the convex polygons `F_j` converge in Hausdorff distance to a line segment of length `lambda/2`. Consequently

```math
\boxed{\lambda\le2.}
\tag{MF.1}
```

In particular every single exceptional face satisfies asymptotically

```math
\boxed{k_F\le(2+o(1))D}
\tag{MF.2}
```

whenever its degree is a fixed positive fraction of `D`.

If one loaded-interface face carries asymptotically all of the minimal interface defect,

```math
Q_B=(2+o(1))D,
\qquad
Q_{F_*}=Q_B-o(D),
```

then

```math
\boxed{k_{F_*}=(2+o(1))D,}
\tag{MF.3}
```

its normalized convex hull converges to a diameter segment of the limiting disk, and its two boundary arcs between a farthest pair of face vertices are unit-contact paths of lengths

```math
\boxed{D+o(D)}.
\tag{MF.4}
```

Thus the giant-face escape is not arbitrary cavity geometry. It is a doubled near-geodesic contact corridor.

This does not by itself close Level I: the existing near-diameter-path report explicitly rejects the local shortcut that a nearly straight unloaded contact path must have transverse contacts on both sides. MF deliberately records only the valid geometric reduction.

---

## 1. Full-core strict rhombi fill the force hull in area

Let `R` be the number of bounded quadrilateral contact faces. Every such face is a strict unit rhombus. Write its acute-angle area as

```math
\sin\theta_F
=\frac{\sqrt3}{2}+\epsilon_F,
\qquad \epsilon_F>0.
```

In the full-core near-circle branch, CE/UF gives

```math
\frac{R}{D^2}\to\Delta,
\qquad
\Delta=\frac\pi{2\sqrt3},
\tag{1.1}
```

and

```math
\sum_{F\text{ rhombus}}\epsilon_F=o(D^2).
\tag{1.2}
```

Therefore the total area of the rhombic bounded faces is

```math
\begin{aligned}
A_4
&=\frac{\sqrt3}{2}R+\sum_F\epsilon_F\\
&=\left(\frac{\sqrt3}{2}\Delta+o(1)\right)D^2\\
&=\left(\frac\pi4+o(1)\right)D^2.
\end{aligned}
\tag{1.3}
```

DC gives

```math
\operatorname{area}(F_{\rm force})
=\left(\frac\pi4+o(1)\right)D^2.
\tag{1.4}
```

The interiors of distinct bounded faces of the plane contact graph are disjoint and every bounded face lies in `F_force`. Hence, if `A_exc` is the total area of all bounded nonquadrilateral faces,

```math
0\le A_{exc}
\le \operatorname{area}(F_{\rm force})-A_4
=o(D^2).
\tag{1.5}
```

Thus

```math
\boxed{A_{exc}=o(D^2).}
\tag{MF.5}
```

This is stronger than a statement about loaded-interface faces: the total area of every bounded exceptional face is subquadratic.

---

## 2. A macroscopic exceptional face has a one-dimensional limit

C51 proves that every bounded contact face is a simple strictly convex unit-edge polygon. Thus an exceptional face of degree `k` has Euclidean perimeter exactly

```math
\operatorname{per}(F)=k.
\tag{2.1}
```

Choose any sequence of exceptional faces `F_j` satisfying

```math
k_j/D_j\to\lambda>0.
```

Translate and scale by `D_j`. Since the normalized force hulls converge to the diameter-one disk, the normalized faces lie in a common compact set. Blaschke selection gives a Hausdorff-convergent subsequence

```math
D_j^{-1}F_j\to K
```

for some compact convex `K` of diameter at most one.

MF.5 gives

```math
\operatorname{area}(K)=0.
```

A compact convex planar set of zero area is contained in a line. Since the limiting perimeter is positive, `K` is a nondegenerate line segment.

For convex bodies in the plane, perimeter is continuous under Hausdorff convergence, including degenerate limits. One direct proof uses Cauchy's width formula

```math
\operatorname{per}(K)=\int_0^\pi w_K(\phi)\,d\phi,
```

because support functions, hence widths, converge uniformly under Hausdorff convergence.

A line segment of length `ell` has width `ell|cos(phi-phi_0)|`, so its Cauchy perimeter is

```math
2\ell.
```

Therefore

```math
\lambda=2\ell.
\tag{2.2}
```

Since `ell<=diam(K)<=1`,

```math
\lambda\le2.
```

This proves MF.1-MF.2.

---

## 3. Equality forces a diameter segment

Suppose now

```math
k_j/D_j\to2.
```

Then (2.2) gives `ell=1`. The limiting force hull is the diameter-one disk. A segment of length one contained in that disk is necessarily a diameter segment: its endpoints are antipodal boundary points.

Thus any asymptotically maximal exceptional face has a normalized Hausdorff limit equal to a diameter of the disk.

Let `a_j,b_j` be a farthest pair of vertices of the convex polygon `F_j`. Convex-polygon diameter is attained at vertices. Hausdorff convergence to a unit segment gives

```math
|a_j-b_j|=(1-o(1))D_j.
\tag{3.1}
```

The boundary cycle of `F_j` splits at `a_j,b_j` into two edge-disjoint polygonal arcs of lengths `L_j^+` and `L_j^-`. Every edge is a unit contact, so these lengths are integers and count the contact edges in the two paths.

Each polygonal arc joins `a_j` to `b_j`, hence

```math
L_j^+\ge|a_j-b_j|,
\qquad
L_j^-\ge|a_j-b_j|.
\tag{3.2}
```

Also

```math
L_j^++L_j^-=k_j=(2+o(1))D_j.
\tag{3.3}
```

Combining (3.1)--(3.3),

```math
\boxed{
L_j^+=D_j+o(D_j),
\qquad
L_j^-=D_j+o(D_j).
}
\tag{3.4}
```

Thus both sides of the collapsed face are near-geodesic unit-contact paths spanning asymptotically the full source diameter.

---

## 4. One-face concentration of minimal interface defect

For one exceptional face

```math
Q_F=k_F-4.
```

Assume a full-core near-circle sequence satisfies

```math
Q_B=(2+o(1))D
```

and some loaded-interface face `F_*` has

```math
Q_{F_*}=Q_B-o(D).
```

Then

```math
k_{F_*}=Q_{F_*}+4=(2+o(1))D.
```

Section 3 applies, proving MF.3-MF.4.

Therefore the extremal single-face configuration is forced into the normal form

```text
near-circular force hull
+ one convex exceptional interface face
+ face perimeter 2D+o(D)
+ face area o(D^2)
+ normalized face -> diameter segment
+ two boundary contact paths, each D+o(D), between an asymptotically diametral pair.
```

---

## 5. Finite macroscopic-face decomposition

Fix `epsilon>0`. Since post-ZF gives `Q=O(D)`, the number of exceptional faces with

```math
k_F\ge\epsilon D
```

is bounded by a constant depending only on `epsilon`.

After passing to a subsequence, every such face has a segment limit as in Section 2. Hence for every fixed threshold the loaded-interface defect splits into:

1. finitely many macroscopic doubled-segment faces;
2. faces of degree `<epsilon D`.

This is the rigorous form of the intended long-face/short-face split.

The first class is now reduced to near-geodesic contact geometry. The second class remains a train-end / one-slot incidence problem.

---

## 6. Relation to existing near-geodesic work

The report `target_c_near_diameter_path_unloaded_core_2026-09-09.md` proves strong consequences for unit-contact paths whose endpoints are actual diameter endpoints or which arise in the dominant-diameter route. It also explicitly records a counterexample to the tempting local statement

> a nearly straight unloaded path vertex must have off-path contacts on both sides.

Therefore MF does **not** infer a local flex or contradiction from (3.4).

What MF contributes is a new source of two near-geodesic paths: a macroscopic interface face at the sharp `2D` scale automatically produces them. A future continuation may combine the face-side condition (one side of each path is an empty contact face) with the stronger global hypotheses of the ZSP/C100-C102 near-chain machinery, but that implication has not been proved here.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| total exceptional bounded-face area `o(D^2)` | proved | full-core rhombus area saturation + force-hull disk area |
| macroscopic exceptional face has segment limit | proved | C51 convexity + MF.5 + Hausdorff compactness |
| macroscopic face degree coefficient at most 2 | proved | convex perimeter continuity + segment perimeter |
| degree coefficient 2 gives diameter-segment limit | proved | equality in diameter-one containment |
| two face arcs have length `D+o(D)` | proved | path length >= chord + total perimeter `2D+o(D)` |
| near-geodesic face already contradicts KKT equilibrium | false/not claimed | existing local counterexample blocks this shortcut |
| Level I | still open | short-face incidence and near-geodesic global exclusion remain |

---

## 8. Next target

The loaded-interface obstruction is now split cleanly.

- **Macroscopic concentration:** finitely many exceptional faces collapse to doubled contact segments. At the minimal one-face endpoint this gives two `D+o(D)` face-boundary contact paths.
- **Diffuse interface:** no face carries a fixed fraction of `D`, so `Q_B>=2D-o(D)` is spread over submacroscopic convex exceptional faces.

For the first branch, the next target is to import the strongest valid near-geodesic global theorem while retaining the extra face-side emptiness condition.

For the second branch, the next target is an endpoint-count theorem: bound the number of stopped-train incidences that submacroscopic interface faces can absorb when almost every loaded terminal has only one interior contact slot.
