> Generated reading edition · [exact source](../../../docs/reports/target_c_projective_circle_isodiametric_area_floor_2026-09-09.md) · source SHA-256 `a779e7234362b4a7a12f89e8b863f1a501cf1a0210e8ab9f4fcc1f931ca1f479`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-79CEDA7D0CF7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — projective-circle isodiametry raises the force-hull area floor

**Date:** 2026-09-09  
**Run type:** exact projective-direction packing / convex-area theorem  
**Target:** Target C C-II after ZF/DB  
**Depends on:** C67 diameter-direction separation and two-diameter area formula, DB diameter-edge density, Kemperman's measure-sumset inequality on compact connected groups  
**External source:** Imre Z. Ruzsa, *A concavity property for the measure of product sets in groups*, Fundamenta Mathematicae 140 (1992), 247--254, DOI 10.4064/fm-140-3-247-254; equivalently the classical Kemperman inequality `mu(AB)>=min(mu(A)+mu(B),mu(G))`. A modern statement also appears in Jing--Tran, arXiv:2006.01824.  
**Computation:** only evaluation of displayed constants; not used in the proof

## LEVEL I STATUS

`STILL OPEN`

Canonical C67 packs the projective directions of the actual diameter edges by using their pairwise separation

```math
\delta_D:=2\arcsin\frac1{2D}.
```

Its published finite packing lemma deliberately truncates the forced angular spread at `pi/3`. That truncation is not sharp. A one-dimensional isodiametric argument on the projective circle gives a spread approaching `pi/2` once enough separated diameter directions are present.

Combined with DB's lower density

```math
\liminf h/D\ge2\rho,
\qquad \rho=\cos\rho=0.7390851332\ldots,
```

this improves the universal post-ZF force-hull area floor to

```math
\boxed{
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge
\frac12\sin(2\rho)
=0.4978566363\ldots .
}
```

This is stronger than the previous `sqrt(3)/4=0.4330127019...` DB floor and substantially strengthens the GU attachment-gap threshold.

---

## 1. A circle isodiametric lemma from Kemperman

Let `T_L=R/LZ` be a circle of circumference `L`, with geodesic distance and Haar length `mu`. The only case needed below is `L=pi`.

### Lemma PI.1 — one-dimensional circle isodiametry

If `A subset T_L` is compact and

```math
\operatorname{diam}_{geo}(A)=\psi<L/2,
```

then

```math
\boxed{\mu(A)\le\psi.}
\tag{PI.1}
```

### Proof

Every difference `x-y` with `x,y in A` has geodesic distance at most `psi` from zero. Hence

```math
A-A\subseteq[-\psi,\psi]\pmod L,
```

so

```math
\mu(A-A)\le2\psi<L.
\tag{PI.2}
```

Kemperman's inequality for the compact connected group `T_L`, applied to `A` and `-A`, gives

```math
\mu(A-A)
\ge
\min\{2\mu(A),L\}.
\tag{PI.3}
```

Because the left side is strictly below `L`, the minimum in PI.3 cannot be `L`. Therefore

```math
2\mu(A)\le\mu(A-A)\le2\psi,
```

which proves PI.1. `square`

Only the circle case of Kemperman is used. In the present application `A` is a finite union of arcs, so all measurability issues are trivial.

---

## 2. Sharpened packing of separated projective directions

The projective direction circle has circumference `pi`. Let

```math
S=\{\theta_1,\ldots,\theta_h\}
\subset\mathbb R/\pi\mathbb Z
```

be the directions of the `h` actual diameter edges. C67 gives the pairwise separation

```math
\boxed{
d_{proj}(\theta_i,\theta_j)\ge\delta_D
\quad(i\ne j).
}
\tag{PI.4}
```

Let

```math
\phi:=\operatorname{diam}_{proj}(S)
\in[0,\pi/2]
```

be the largest projective angle between two actual diameter directions.

Around every `theta_i`, take the closed projective arc of radius `delta_D/2`. Their interiors are disjoint by PI.4. Let `U` be their union. Thus

```math
\boxed{\mu(U)=h\delta_D.}
\tag{PI.5}
```

By the triangle inequality on the projective circle,

```math
\operatorname{diam}_{proj}(U)
\le\phi+\delta_D.
\tag{PI.6}
```

If `phi+delta_D<pi/2`, Lemma PI.1 applied to `U` gives

```math
h\delta_D
\le\phi+\delta_D,
```

so

```math
\phi\ge(h-1)\delta_D.
\tag{PI.7}
```

If instead `phi+delta_D>=pi/2`, then directly

```math
\phi\ge\frac\pi2-\delta_D.
\tag{PI.8}
```

Therefore in all cases:

### Theorem PI.2 — sharp projective spread lower bound

```math
\boxed{
\phi
\ge
\Phi(h,D)
:=
\min\left\{
(h-1)\delta_D,
\frac\pi2-\delta_D
\right\}.
}
\tag{PI.9}
```

This replaces C67's conservative `min{pi/3,(h-1)delta_D}` truncation.

### Sanity checks

- If the diameter directions are concentrated in one short projective arc, PI.9 reduces to the obvious one-dimensional packing length `(h-1)delta_D`.
- If the separated arcs occupy more than a projective semicircle in measure, PI.9 forces two directions within `delta_D` of perpendicularity.
- The result does not say the directions themselves lie in one interval; the circle isodiametric lemma covers multi-cluster sets.

---

## 3. Convert projective spread to force-hull area

C67 proves the following exact geometric fact. If two actual diameter edges have projective angle `theta`, then the convex hull of their endpoints has area

```math
\boxed{
\frac{D^2}{2}\sin\theta.
}
\tag{PI.10}
```

If the two diameter edges share an endpoint, this is the area of the triangle formed by the two length-`D` sides. If they are disjoint, the planar diameter-thrackle property makes them crossing diagonals of a convex quadrilateral, whose area is half the product of the diagonal lengths times the sine of their angle.

All endpoints lie in the force hull `F`. Since projective angles lie in `[0,pi/2]` and sine is increasing there, PI.9 gives:

### Theorem PI — exact post-ZF force-hull area floor

```math
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{2}
\sin\left(
\min\left\{
(h-1)\delta_D,
\frac\pi2-\delta_D
\right\}
\right),
}
\tag{PI.11}
```

where

```math
\delta_D=2\arcsin\frac1{2D}.
```

No contact-core population, face topology, or rhombic hypothesis enters PI.11.

---

## 4. Insert the DB diameter-edge density

DB proves

```math
\boxed{
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho=0.7390851332151607\ldots .
}
\tag{PI.12}
```

Also

```math
D\delta_D
=2D\arcsin\frac1{2D}
\longrightarrow1.
\tag{PI.13}
```

Therefore

```math
\liminf (h-1)\delta_D
\ge2\rho,
```

while

```math
\frac\pi2-\delta_D\longrightarrow\frac\pi2.
```

Since

```math
2\rho=1.478170266430321\ldots<\frac\pi2,
```

PI.11 yields:

### Corollary PI.3 — universal DB-upgraded area constant

```math
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
A_{PI}:=rac12\sin(2\rho)
=0.497856636324211\ldots .
}
\tag{PI.14}
```

For comparison:

```math
\frac12\sin1
=0.4207354924\ldots,
```

from the first post-ZF C67 upgrade, and

```math
\frac{\sqrt3}{4}
=0.4330127019\ldots,
```

from the DB projective-direction spread theorem. PI.14 supersedes both universal constants.

The isodiametric upper bound remains

```math
\operatorname{area}(F)\le\frac\pi4D^2
=0.7853981634\ldots D^2,
```

so PI is not by itself a Level I contradiction.

---

## 5. Stronger GU attachment-gap threshold

GU's attachment-cell estimate has the form

```math
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\lambda_2^2D^2+o(D^2),
\qquad
\lambda_2:=\limsup\frac{e_{BB}+2s_C}{D}.
\tag{PI.15}
```

Subtracting this from PI.14 gives

```math
\boxed{
\liminf\frac G{D^2}
\ge
A_{PI}-\frac\pi4\lambda_2^2.
}
\tag{PI.16}
```

Hence a positive quadratic attachment-cell gap is forced whenever

```math
\boxed{
\lambda_2
<
\lambda_{PI}
:=
\sqrt{\frac{4A_{PI}}\pi}
=
0.796172567335008\ldots .
}
\tag{PI.17}
```

This raises the GU transition from

```math
\sqrt{\frac{\sqrt3}{\pi}}
=0.7425152492\ldots
```

to `0.7961725673...`.

---

## 6. Combine with PC: the low-surplus branch has many distinct convex pockets

PC proves

```math
a+e_{BB}\ge q,
\tag{PI.18}
```

where `a` is the number of missing loaded force-hull sides, equivalently the number of distinct strict convex OP outer pockets.

DB gives

```math
\liminf q/D\ge2\rho.
```

Along a PI/GU low-surplus subsequence with

```math
\frac{e_{BB}+2s_C}{D}<\lambda_{PI}-o(1),
```

we have `e_BB/D<lambda_PI+o(1)`. Thus

```math
\boxed{
\liminf\frac aD
\ge
2\rho-\lambda_{PI}
=0.681997699095313\ldots .
}
\tag{PI.19}
```

So the strengthened low-surplus branch simultaneously has:

1. a positive quadratic attachment-cell area gap `G=Omega(D^2)`; and
2. at least `0.6819976991 D-o(D)` **distinct convex outer pockets**.

GU then localizes the quadratic gap to the outer region or to a giant bounded exceptional face. PI.19 narrows the outer-region case to a highly fragmented convex-pocket shell.

---

## 7. Interaction with the earlier difference-body area theorem

The report `target_c_difference_body_area_metric_fork_2026-09-09.md` proves the independent bound

```math
\operatorname{area}(F)
\ge
\frac{D^2}{6}
\left[(h-1)\sin\delta_D+
\sin((h-1)\delta_D)\right].
```

PI.11 is stronger in the DB density range because it uses a pair of widely separated diameter chords directly instead of passing through the planar Rogers--Shephard factor `6`.

The difference-body report's **metric missing-side theorem** remains independent and useful. Only its area route is superseded as the best available force-hull area lower bound.

---

## 8. Regressions and scope

### Multi-cluster projective directions

The old interval-packing shortcut would be invalid if the diameter directions occupy several clusters on the projective circle. PI.1 is exactly what removes that loophole; no containment in one projective interval is assumed.

### Regular shells

A regular odd shell naturally has many well-spread diameter directions and a large convex hull. PI is compatible with it. Global optimality remains necessary elsewhere.

### High diameter-edge density

If `h/D` exceeds `pi/2`, PI.9 saturates near perpendicularity rather than attempting to force a projective angle larger than `pi/2`.

### No measure-to-count confusion

The measure `h delta_D` belongs only to the disjoint thickened direction arcs. The original direction set is finite and has zero Haar measure. The circle isodiametric lemma is applied to the thickened union `U`, not to the center set itself.

### Literature dependency

Only Kemperman's classical Haar-measure sumset inequality is imported. The stronger spherical isodiametric theorem of Böröczky--Sagmeister is not needed.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| PI.1 circle isodiametric lemma | proved from Kemperman | `A-A` support plus measure sumset inequality |
| PI.9 sharpened projective spread | proved | disjoint thickened arcs + PI.1 |
| PI.11 exact area floor | proved | C67 two-diameter area formula |
| universal constant `0.4978566363...` | proved under DB | DB density + elementary limit |
| GU threshold `0.7961725673...` | proved conditional on GU inputs | substitute PI area floor |
| low-surplus pocket count `0.6819976991D` | proved | PC + DB + PI threshold |
| Level I | still open | macroscopic pocket/giant-face and high-surplus branches remain |

---

## 10. Next target

PI pushes the force hull very close to the maximal two-diameter-chord area `D^2/2`, but not close to the isodiametric disk area `pi D^2/4`. The immediate post-PI split is now:

1. **low pinned surplus:** `e_BB+2s_C<0.79617D`, giving both a quadratic attachment-cell gap and at least `0.68199D` distinct strict convex outer pockets;
2. **high pinned surplus:** `e_BB+2s_C>=0.79617D`, where the contact/stress boundary currency itself is linear with an improved constant.

The next useful theorem must turn one of these two concrete structures into either the direct face contradiction or a strict sub-`D` competitor.
