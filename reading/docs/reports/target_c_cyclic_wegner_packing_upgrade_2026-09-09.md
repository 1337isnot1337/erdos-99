> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_wegner_packing_upgrade_2026-09-09.md) · source SHA-256 `2b98d79cbea175a0ee64d15045439a0ff6f0e0e5841dbde83c5323d7d49529c9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1DD5C53C100B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Wegner finite-packing upgrade in the exact cyclic Reinhardt branch

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE/RC/RD/FB  
**Run type:** sharp finite-packing insertion / quantitative source-capacity upgrade  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** FB force-hull closure, RE exact cyclic perimeter, RC Reuleaux completion/core notation  
**External theorem:** G. Wegner's sharp convex-hull area inequality for congruent disk packings, in the form reviewed by K. Böröczky Jr. and I. Z. Ruzsa, *Note on an inequality of Wegner*  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

FB proves that in the exact `d_H=0` cyclic branch the force hull is the full source hull:

```math
F=\operatorname{conv}A,
\qquad
\operatorname{per}(F)=q.
```

Therefore one can apply the sharp finite disk-packing inequality of Wegner directly to the complete source, rather than use only generic Oler capacity.

### Theorem WG — exact Wegner lower bound for the force-hull area

Every exact cyclic `d_H=0` survivor satisfies

```math
\boxed{
\operatorname{area}(F)
\ge
\frac{\sqrt3}{2}(n-1)
-\frac q2
+\frac{2-\sqrt3}{4}
\left\lceil\sqrt{12n-3}-3\right\rceil.}
\tag{WG.1}
```

Using the strict global diameter comparison

```math
n>\frac\pi{2\sqrt3}D^2,
```

this gives the finite consequence

```math
\boxed{
\operatorname{area}(F)
>
\frac\pi4D^2
-\frac q2
-\frac{\sqrt3}{2}
+\frac{2-\sqrt3}{4}
\left(
\sqrt{2\pi\sqrt3\,D^2-3}-3
\right).}
\tag{WG.2}
```

Since RE gives

```math
q=\pi D-\frac\pi{24D}+O(D^{-3})
```

exactly through the Reinhardt relation, the disk-area deficit satisfies

```math
\boxed{
\frac\pi4D^2-\operatorname{area}(F)
\le
\left(C_W+o(1)\right)D,}
\tag{WG.3}
```

where

```math
\boxed{
C_W
:=
\frac\pi2
-
\frac{2-\sqrt3}{4}
\sqrt{2\pi\sqrt3}
=1.349811370903931\ldots .}
\tag{WG.4}
```

The Oler-only coefficient was

```math
\frac{\pi\sqrt3}{4}
=1.3603495231\ldots ,
```

so WG is a genuine linear improvement.

---

## 1. Scaling Wegner to unit-separated centers

For the unit-separated source `A`, place a closed disk of radius `1/2` around every source point. The interiors are pairwise disjoint.

Scale the entire picture by factor two. The resulting packing consists of `n` pairwise non-overlapping unit disks with centers `2A`.

Because FB gives

```math
F=\operatorname{conv}A,
```

the convex hull of the scaled unit disks is

```math
\mathcal D
=2F+B_2(0,1).
\tag{1.1}
```

Steiner's formula gives

```math
\operatorname{area}(\mathcal D)
=4\operatorname{area}(F)+2\operatorname{per}(F)+\pi
=4\operatorname{area}(F)+2q+\pi.
\tag{1.2}
```

Wegner's inequality states that for the convex hull of `n` non-overlapping unit disks,

```math
\operatorname{area}(\mathcal D)
\ge
2\sqrt3(n-1)
+(2-\sqrt3)
\left\lceil\sqrt{12n-3}-3\right\rceil
+\pi.
\tag{1.3}
```

Subtract `pi`, substitute (1.2), and divide by four:

```math
\operatorname{area}(F)
\ge
\frac{\sqrt3}{2}(n-1)
-\frac q2
+\frac{2-\sqrt3}{4}
\left\lceil\sqrt{12n-3}-3\right\rceil.
```

This proves WG.1. `square`

---

## 2. Insert the global minimum-diameter density

The canonical strict comparison gives

```math
n>\Delta D^2,
\qquad
\Delta=\frac\pi{2\sqrt3}.
```

Therefore

```math
\frac{\sqrt3}{2}(n-1)
>
\frac\pi4D^2-\frac{\sqrt3}{2}.
\tag{2.1}
```

Also

```math
\sqrt{12n-3}
>
\sqrt{12\Delta D^2-3}
=
\sqrt{2\pi\sqrt3\,D^2-3}.
\tag{2.2}
```

Since `ceil(x)>=x`, substituting (2.1)-(2.2) into WG.1 proves WG.2.

RE gives the exact relation

```math
D=\frac1{2\sin(\pi/(2q))},
```

and hence

```math
q
=
\pi D-\frac\pi{24D}+O(D^{-3}).
\tag{2.3}
```

Divide the deficit form of WG.2 by `D` and use

```math
\frac1D\sqrt{2\pi\sqrt3\,D^2-3}
\to
\sqrt{2\pi\sqrt3}.
```

This proves WG.3-WG.4. `square`

---

## 3. Improved lower bound on the Reuleaux core size

RC lets `nu` denote the odd cycle length of the diameter graph, equivalently the number of arcs/defining vertices of the width-`D` Reinhardt Reuleaux completion `R`.

Since

```math
F\subseteq R,
```

we have

```math
\frac\pi4D^2-\operatorname{area}(R)
\le
\frac\pi4D^2-\operatorname{area}(F).
\tag{3.1}
```

The Firey--Sallee maximal-area theorem used in RC gives

```math
\frac\pi4D^2-\operatorname{area}(R)
\ge
\frac{\pi^3D^2}{48\nu^2}.
\tag{3.2}
```

Combining (3.1)-(3.2) with WG.3 yields

```math
\frac{\pi^3D^2}{48\nu^2}
\le
(C_W+o(1))D.
```

Therefore:

### Corollary WG.1 — sharpened odd-core growth

```math
\boxed{
\liminf_{D\to\infty}
\frac\nu{\sqrt D}
\ge
\sqrt{\frac{\pi^3}{48C_W}}
=0.6917794379919272\ldots .}
\tag{WG.5}
```

RC's Oler-only constant was

```math
0.6890947417786648\ldots .
```

The numerical gain is modest, but the proof is exact and replaces a generic boundary correction by the sharp known finite-packing correction.

---

## 4. Equality structure is incompatible with the cyclic hull

The cited sharp form of Wegner's theorem has equality exactly for Wegner packings. Such a packing is a Groemer packing: its center hull can be triangulated by equilateral triangles of the contact lattice, and its center hull has at most six sides.

Our exact cyclic source has

```math
q\sim\pi D\to\infty
```

strictly convex hull vertices, all consecutive hull sides equal to one. Therefore the cyclic source cannot attain equality in WG.1 for sufficiently large `q`.

Thus one has strict inequality in Wegner, not merely the displayed weak inequality.

This does **not** by itself yield a uniform additional linear gap: the equality characterization is qualitative, and no stability theorem with a source-independent positive deficit is imported here. We therefore do not claim more than WG.1-WG.5.

---

## 5. Why WG does not yet close Level I

The linear source-capacity margin remains positive:

```math
C_WD
=1.3498\ldots D.
```

The exact Reinhardt family can have disk-area deficit much smaller than this, so the improved area floor is compatible with the convex hull geometry.

The new high-value question is no longer whether generic Oler can be sharpened at all; Wegner answers that. The missing theorem is a **stability refinement adapted to many hull directions**:

> quantify how far a packing with `q=Theta(D)` strictly convex unit hull edges is from the six-direction Groemer/Wegner equality mechanism.

A fixed further linear improvement in the boundary correction would feed directly into WG.3 and RC/WG.5.

---

## 6. Regression audit

### Groemer/Wegner packing

Equality in WG.1 is allowed in the theorem but cannot satisfy the exact cyclic force-hull hypothesis for large `q`, because its center hull has at most six sides.

### Regular odd Reinhardt shell with no interior points

It does not satisfy the large-`n` global-minimizer density premise used in WG.2, so no contradiction is inferred.

### Dense interior population

Handled directly: FB ensures every source point contributes to the same disk-packing hull `2F+B_1`.

### Strict inequality without stability

Recorded correctly. We do not turn qualitative non-equality into an unproved quantitative gap.

---

## 7. Next theorem

The best packing endpoint is now:

```math
\operatorname{area}(F)
\ge
\frac{\sqrt3}{2}(n-1)-\frac q2
+\frac{2-\sqrt3}{4}
\left\lceil\sqrt{12n-3}-3\right\rceil,
```

with `q=Theta(D)` distinct strictly convex unit boundary directions, while Wegner equality uses at most six lattice directions.

The next target should be a **direction-sensitive Wegner stability theorem**: charge boundary turning away from the six triangular-lattice directions to a quantitative increase in convex-hull area. Any source-independent positive charge summing over the `q` slowly turning hull edges would strengthen WG by another linear term.

---

## 8. Promotion recommendation

**Hold as report pending independent audit.**

WG.1 is an exact direct scaling of a classical sharp packing theorem. The Target C consequences depend on report-level FB/RE/RC.

---

## 9. Literature note

The external input is the sharp form

```math
A(\mathcal D)
\ge
2\sqrt3(n-1)
+(2-\sqrt3)\left\lceil\sqrt{12n-3}-3\right\rceil+\pi,
```

with equality iff the packing is a Wegner packing, as stated in Böröczky--Ruzsa, *Note on an inequality of Wegner*. Their discussion also records that Groemer center hulls have at most six sides.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

FB gives F=conv(A), per(F)=q. Scale radius-1/2 source disks by two. The convex hull
of the resulting unit disks is Dcal=2F+B_1, so
  area(Dcal)=4 area(F)+2q+pi.
Wegner gives
  area(Dcal)>=2sqrt3(n-1)+(2-sqrt3)ceil(sqrt(12n-3)-3)+pi.
Therefore
  area(F)>=sqrt3/2(n-1)-q/2
           +(2-sqrt3)/4 ceil(sqrt(12n-3)-3).

Using n>pi D^2/(2sqrt3) and RE q=pi D+o(D):
  pi D^2/4-area(F) <= (C_W+o(1))D,
  C_W=pi/2-(2-sqrt3)/4 sqrt(2pi sqrt3)
     =1.349811370903931...
versus Oler coefficient pi sqrt3/4=1.3603495231....

Combining with RC/Firey-Sallee:
  liminf nu/sqrt(D) >= sqrt(pi^3/(48C_W))
                     =0.6917794379919272...

Wegner equality is impossible here for large q because a Groemer/Wegner center hull
has at most six sides while q~pi D -> infinity. No uniform quantitative stability
gap is claimed without proof.

Next: direction-sensitive stability away from the six-direction Groemer equality mechanism.
```
