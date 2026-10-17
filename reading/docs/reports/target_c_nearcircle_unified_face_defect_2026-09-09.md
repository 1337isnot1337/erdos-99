> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_unified_face_defect_2026-09-09.md) · source SHA-256 `41d43480190ba433464c37fef528ceda73470c06386369f6b4df76456ccf6874`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EF2FB8C0150F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_unified_face_defect_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=57b5f728bbeb84e8d2106ca6a034589c94492bf2; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — unified near-circle face-defect theorem

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG/DC/DS/OW/GF/CE/CF  
**Run type:** cross-branch optimization / asymptotic packing stability  
**Target:** entire post-ZF `x_B=o(D)` phase  
**Depends on:** DC/OW population localization, DT/DE train compactness, NM one-good-train theorem, ZE/ZT ledgers, C51 face convexity  
**External web search:** not used in the proof  
**Computation:** decimals only; all inequalities are analytic

## LEVEL I STATUS

`STILL OPEN`

The preceding work split the near-circle endpoint according to the quadratic population deficit of the positive contact core. The split can be removed.

Let

$$
\Delta:=\frac\pi{2\sqrt3},
\qquad
\zeta:=\lim\frac{n-v}{D^2}
\in[0,\Delta]
$$

along an arbitrary convergent subsequence of a post-ZF sequence with

$$
x_B=o(D).
$$

The key observation is an exact leading-order area balance. OW and DC remove quadratic population from the two outer regions, so the missing core population lies in bounded exceptional faces. The minimum rhombus area and the minimum Oler area needed by those bounded-face rattlers add to exactly the isodiametric area ceiling:

$$
\frac{\sqrt3}{2}(\Delta-\zeta)
+\frac{\sqrt3}{2}\zeta
=\frac\pi4.
$$

Therefore both parts must asymptotically saturate. In particular the rhombus area excess is `o(D^2)` for **every** `zeta`, not only when `zeta=0`. This lets the one-ended train argument of CE run with rhombus density `Delta-zeta`.

The resulting face-defect bound is

$$
\boxed{
\liminf\frac QD
\ge
\frac\pi5+\frac45\sqrt{\Delta-\zeta}.
}
\tag{UF.1}
$$

Independently, the bounded-face population itself forces

$$
\boxed{
\liminf\frac QD
\ge
\sqrt{\frac{2\pi\sqrt3}{5}\,\zeta}.
}
\tag{UF.2}
$$

The first bound decreases with `zeta`; the second increases. Their unique intersection gives the universal constant

$$
\boxed{
\liminf\frac QD
\ge c_Q
=1.1013451504\ldots
}
\tag{UF.3}
$$

throughout the entire near-circle `x_B=o(D)` phase.

Since

$$
q=x_B+Q+2d_H+2s_Z,
\qquad q/D\to\pi,
$$

this also yields

$$
\boxed{
\liminf\frac hD
\ge
\frac{\pi+c_Q}{2}
=2.1214689020\ldots .
}
\tag{UF.4}

$$

Thus the near-circle phase universally carries more than `1.10D` units of actual bounded-face degree defect and more than `2.12D` actual diameter edges, regardless of whether the positive core is asymptotically full or a quadratic rattler population survives.

---

## 1. Core and defect population densities

Assume

$$
x_B=o(D).
\tag{1.1}
$$

DG/DC gives

$$
q/D\to\pi,
\qquad
\operatorname{area}(F)/D^2\to\pi/4,
\qquad
F/D\to\text{the diameter-one disk}.
\tag{1.2}
$$

Pass to a subsequence on which

$$
\frac{n-v}{D^2}\to\zeta.
\tag{1.3}
$$

The global density theorem gives

$$
\frac n{D^2}\to\Delta,
$$

so

$$
\boxed{
\frac v{D^2}\to\Delta-\zeta.
}
\tag{1.4}
$$

Because `Q<=q=O(D)` and `f<=Q`, the stopped-train identity gives `T=O(D)`. Euler/DT gives

$$
R=v+f-T-1,
$$

hence

$$
\boxed{
\frac R{D^2}\to\Delta-\zeta.
}
\tag{1.5}
$$

---

## 2. Almost all missing core population lies in bounded exceptional faces

C65/C49 partition the noncore source population as

$$
n-v=Z_{def}+Z_{in}+Z_{ext}.
$$

OW gives

$$
Z_{in}=o(D^2)
$$

under `x_B=o(D)`, and DC gives

$$
Z_{ext}=o(D^2).
$$

Therefore

$$
\boxed{
\frac{Z_{def}}{D^2}\to\zeta.
}
\tag{2.1}
$$

Let `A_exc` be the total area of the bounded exceptional faces. C51 makes every such face convex. Facewise Oler, applied to the unit boundary vertices together with its assigned isolated interior points, gives for each face

$$
A_f\ge\frac{\sqrt3}{2}z_f.
$$

Summing,

$$
\boxed{
A_{exc}
\ge
\frac{\sqrt3}{2}Z_{def}.
}
\tag{2.2}
$$

Thus

$$
\liminf\frac{A_{exc}}{D^2}
\ge
\frac{\sqrt3}{2}\zeta.
\tag{2.3}
$$

---

## 3. Leading-order area balance forces rhombus near-equality

Let `A_R` be the total area of the `R` bounded rhombic contact faces. Every strict rhombus has acute angle greater than `pi/3`, so

$$
A_R
\ge
\frac{\sqrt3}{2}R.
\tag{3.1}
$$

The rhombus interiors and exceptional bounded-face interiors are pairwise disjoint subsets of the force hull. Hence

$$
\operatorname{area}(F)
\ge A_R+A_{exc}.
\tag{3.2}
$$

Divide by `D^2`. Using (1.2), (1.5), and (2.3),

$$
\begin{aligned}
\frac\pi4
&\ge
\liminf\frac{A_R+A_{exc}}{D^2}\\
&\ge
\frac{\sqrt3}{2}(\Delta-\zeta)
+\frac{\sqrt3}{2}\zeta\\
&=
\frac{\sqrt3}{2}\Delta
=
\frac\pi4.
\end{aligned}
\tag{3.3}
$$

Every inequality is therefore asymptotically an equality. In particular

$$
\boxed{
A_R-rac{\sqrt3}{2}R=o(D^2).
}
\tag{3.4}
$$

This is exactly the total rhombus-area-excess hypothesis used in DE.

Likewise

$$
A_{exc}-\frac{\sqrt3}{2}Z_{def}=o(D^2),
\tag{3.5}
$$

although that second equality is not needed below.

When `zeta=Delta`, (1.5) gives `R=o(D^2)` and the train crossing inequality below becomes trivial; all displayed conclusions follow by continuity from the formulas. Thus assume `zeta<Delta` when invoking the positive-density train limit.

---

## 4. One-ended train exposure with reduced rhombus density

Put

$$
r:=\Delta-\zeta>0.
$$

The DE compactness proof now applies with

$$
R/D^2\to r
$$

because (3.4) gives the needed rhombus-angle concentration and (1.2) gives disk convergence of the force hull.

Take a subsequence on which

$$
T/D\to\tau
$$

and let `s_atom` be the total atomic mass of the limiting train-direction measure.

DE's finite-Mantel step gives

$$
\boxed{
\tau s_{atom}\ge2\sqrt r.
}
\tag{4.1}
$$

The CE one-ended hull argument uses only

- `q-o(D)` good unit hull sides, which follows from `x_B=o(D)`;
- NM's theorem that at most two trains have two good hull ends;
- disk convergence of the hull perimeter measure.

It therefore applies unchanged and gives

$$
\boxed{
\pi\le\tau(1-s_{atom}).
}
\tag{4.2}
$$

Combining,

$$
\boxed{
\tau-\pi\ge2\sqrt{\Delta-\zeta}.
}
\tag{4.3}
$$

Equivalently,

$$
\boxed{
\liminf\frac{T-q}{D}
\ge2\sqrt{\Delta-\zeta}.
}
\tag{4.4}
$$

This interpolates CE.1 at `zeta=0` and becomes vacuous only when the positive core itself has zero quadratic density.

---

## 5. First face-defect bound: train exposure

ZE gives

$$
2f=(T-q)+d_H+s_Z.
\tag{5.1}
$$

Hence (4.4) gives

$$
\liminf\frac fD
\ge
\sqrt{\Delta-\zeta}
+\frac12\liminf\frac{d_H+s_Z}{D}
\tag{5.2}
$$

in the usual subsequence formulation.

The terminal ledger is

$$
q=x_B+Q+2d_H+2s_Z.
\tag{5.3}
$$

Since `q/D->pi` and `x_B=o(D)`, if

$$
k:=\lim\frac{d_H+s_Z}{D}
$$

along a further subsequence, then

$$
\frac QD\to\pi-2k.
\tag{5.4}
$$

Every exceptional face contributes at least one to `Q`, so `Q>=f`. Combining (5.2)-(5.4):

$$
\pi-2k
\ge
\sqrt{\Delta-\zeta}+\frac k2.
$$

Therefore

$$
k\le\frac25\left(\pi-\sqrt{\Delta-\zeta}\right),
$$

and hence

$$
\boxed{
\liminf\frac QD
\ge
A(\zeta)
:=
\frac\pi5+rac45\sqrt{\Delta-\zeta}.
}
\tag{5.5}
$$

This proves UF.1.

The same inequality gives

$$
\boxed{
\liminf\frac hD
\ge
\frac{3\pi}{5}
+\frac25\sqrt{\Delta-\zeta}.
}
\tag{5.6}
$$

before the second face-defect bound is inserted.

---

## 6. Second face-defect bound: the rattler population itself

Let `k_i` be the perimeters of the bounded exceptional faces and

$$
K_{exc}:=\sum_i k_i.
$$

Since every exceptional face has degree at least five,

$$
K_{exc}=Q+4f\le5Q.
\tag{6.1}
$$

Also every single face contributes `k_i-4` to `Q`, so

$$
\boxed{k_{max}\le Q+4.}
\tag{6.2}
$$

By convex isoperimetry,

$$
A_{exc}
\le
\frac1{4\pi}\sum_i k_i^2
\le
\frac{k_{max}K_{exc}}{4\pi}.
$$

Using (6.1)-(6.2),

$$
\boxed{
A_{exc}
\le
\frac{5Q(Q+4)}{4\pi}.
}
\tag{6.3}
$$

But (2.2) and (2.1) give

$$
A_{exc}
\ge
\left(\frac{\sqrt3}{2}\zeta-o(1)\right)D^2.
\tag{6.4}
$$

If `Q/D->xi` along a subsequence, divide (6.3)-(6.4) by `D^2`:

$$
\frac{\sqrt3}{2}\zeta
\le
\frac5{4\pi}\xi^2.
$$

Therefore

$$
\boxed{
\liminf\frac QD
\ge
B(\zeta)
:=
\sqrt{\frac{2\pi\sqrt3}{5}\,\zeta}.
}
\tag{6.5}
$$

This proves UF.2.

---

## 7. Optimize over the unknown core deficit

Every convergent subsequence with core deficit `zeta` satisfies

$$
\liminf Q/D
\ge
\max\{A(\zeta),B(\zeta)\},
\qquad
0\le\zeta\le\Delta.
\tag{7.1}
$$

`A` is strictly decreasing and `B` strictly increasing. Therefore their maximum is minimized at their unique intersection.

Let `zeta_*` be the unique solution of

$$
\frac\pi5+rac45\sqrt{\Delta-\zeta}
=
\sqrt{\frac{2\pi\sqrt3}{5}\zeta}.
\tag{7.2}
$$

Numerically

$$
\boxed{
\zeta_*=0.5572837714\ldots .
}
\tag{7.3}
$$

The common value is

$$
\boxed{
c_Q=1.1013451504\ldots .}
\tag{7.4}
$$

Thus every subsequence obeys the same lower bound, proving UF.3.

For an exact closed form, write

$$
u_*:=\sqrt{\Delta-\zeta_*}.
$$

Then `u_*` is the positive root of

$$
(8+5\pi\sqrt3)u^2+4\pi u-2\pi^2=0,
\tag{7.5}
$$

and

$$
c_Q=\frac{\pi+4u_*}{5}.
\tag{7.6}
$$

The decimal is more useful than the radical expression.

---

## 8. Universal diameter-edge density in the near-circle phase

The terminal ledger gives

$$
\pi
=
\lim\frac qD
\ge
\liminf\frac QD
+2\liminf\frac{d_H}{D},
$$

because `s_Z>=0` and `x_B=o(D)`.

Equivalently,

$$
\limsup\frac{d_H}{D}
\le\frac{\pi-c_Q}{2}.
$$

Since

$$
h=q-d_H,
$$

we get

$$
\boxed{
\liminf\frac hD
\ge
\frac{\pi+c_Q}{2}
=2.1214689020\ldots .
}
$$

This proves UF.4.

Numerically

$$
\frac{\pi-c_Q}{2}
=1.0201237516\ldots .
$$

---

## 9. What has been removed

Before UF, the near-circle endpoint still had two qualitatively different population branches:

- a full-core phase with strong train control;
- a giant bounded-face rattler phase where DE was not obviously available.

The area balance in Section 3 shows that this distinction is artificial for the rhombus-angle limit. Any quadratic rattler population in bounded exceptional faces exactly replaces the missing minimum rhombus area at leading order, leaving no room for macroscopic rhombus area excess.

Thus the one-ended train theorem survives continuously across the entire range

$$
0\le\zeta\le\Delta.
$$

At the same time the rattler population itself forces an independent `Q` cost. Their optimization is what produces the universal constant `c_Q`.

---

## 10. Remaining theorem after UF

The entire post-ZF problem now has a sharper two-phase description.

### Linear outer-walk phase

$$
x_B=\Omega(D).
$$

OW converts this into explicit outer-pocket capacity, but no contradiction yet follows.

### Near-circle phase

$$
x_B=o(D).
$$

Then universally

$$
F/D\to\text{disk},
\qquad
e_{BB}/D\to\pi,
$$

$$
Q/D\ge1.1013451504-o(1),
\qquad
h/D\ge2.1214689020-o(1),
$$

and DS gives almost-minimal cyclic diameter-direction gaps.

The remaining near-circle lemma is now independent of rattler population:

> show that a near-isodiametric packing with an almost complete unit-contact loaded hull cycle cannot carry `1.101345D` bounded-face degree defect while all unit-contact triangles are absent.

No Level I solution is claimed here.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Assume x_B=o(D), and along a subsequence
    (n-v)/D^2 -> zeta in [0,Delta].
Then
    v/D^2 -> Delta-zeta,
    R/D^2 -> Delta-zeta,
    Z_def/D^2 -> zeta.
Facewise Oler gives
    A_exc >= (sqrt3/2) Z_def.
Rhombi give
    A_R >= (sqrt3/2) R.
Since F area -> pi D^2/4 and
    (sqrt3/2)[(Delta-zeta)+zeta]=pi/4,
both bounds saturate; in particular rhombus area excess=o(D^2).

Therefore DE + the CE one-good-end argument gives
    (T-q)/D >= 2sqrt(Delta-zeta)-o(1).
Using ZE, Q>=f, and the terminal ledger:
    Q/D >= A(zeta)=pi/5+(4/5)sqrt(Delta-zeta).

Independently,
    A_exc <= k_max K_exc/(4pi),
    k_max<=Q+4,
    K_exc<=5Q,
so
    Q/D >= B(zeta)=sqrt((2pi sqrt3/5) zeta).

Optimize max(A,B) over zeta:
    zeta*=0.5572837714...,
    c_Q=1.1013451504....
Hence universally in x_B=o(D):
    Q/D >= c_Q-o(1),
    h/D >= (pi+c_Q)/2-o(1)
        =2.1214689020...-o(1).
```
