<!-- theorem-state: {"artifact_id":"ART-C8C03A5C88EC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C43: uniform anti-Reuleaux gap for every source triple

**Date:** 2026-08-31  
**Target:** global Target C geometry; no triangle-free or C-II hypothesis  
**Depends on:** canonical Fejes Tóth parallel-body lower bound, strict global upper bound for `D(n)`, and the Reuleaux compactness mechanism of C15-C16  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C15 excludes an exact equilateral triple at the full source diameter. The same global-packing mechanism is stable and gives a stronger uniform statement for arbitrary triples, independent of KKT support.

### Theorem C43 — uniform anti-Reuleaux triple gap

There exist absolute constants

\[
\boxed{\eta_0>0,\qquad n_0<\infty}
\tag{C43.1}
\]

such that for every `n>=n_0`, every planar global minimum-diameter unit-separated `n`-point configuration `A`, and every three distinct points `x,y,z in A`,

\[
\boxed{
\min\{|x-y|,|y-z|,|z-x|\}
\le(1-\eta_0)D(n).
}
\tag{C43.2}
\]

Equivalently, for every sufficiently large global minimizer, the graph joining pairs at distance greater than `(1-eta_0)D(n)` is triangle-free.

The constant is not made explicit here. The proof is compactness plus the strict area-coefficient gap

\[
\frac{\pi-\sqrt3}{2}<\frac\pi4.
\tag{C43.3}
\]

This strengthens C15 from “no exact diameter triangle” to a uniform exclusion neighborhood around the equilateral diameter geometry.

---

## 1. Contradiction sequence

Assume C43 is false. Then for every integer `m>=1` there exist

- a cardinality `n_m>=m`;
- a global minimizer `A_m` of cardinality `n_m` and diameter `D_m=D(n_m)`; and
- distinct points `x_m,y_m,z_m in A_m`

such that

\[
\min\{|x_m-y_m|,|y_m-z_m|,|z_m-x_m|\}
>
\left(1-\frac1m\right)D_m.
\tag{C43.4}
\]

All three distances are at most `D_m`, so after scaling by `D_m`, all three pairwise distances converge to one.

Apply a rigid motion after scaling so that

\[
\tilde x_m=(0,0),
\qquad
\tilde y_m=(r_m,0),
\tag{C43.5}
\]

with `r_m->1`. The points `tilde z_m` remain in the compact unit disk about the origin. Passing to a subsequence, `tilde z_m->z_infty`. The distance limits give

\[
|z_\infty|=1,
\qquad
|z_\infty-(1,0)|=1.
\tag{C43.6}
\]

Thus, after reflecting if necessary,

\[
z_\infty=\left(\frac12,\frac{\sqrt3}{2}\right).
\tag{C43.7}
\]

The normalized triples therefore converge to the vertices of a unit equilateral triangle.

---

## 2. The whole source enters a near-Reuleaux container

Every normalized source point `a/D_m` lies within distance one of each of `tilde x_m,tilde y_m,tilde z_m`, because the source diameter is `D_m`. Hence

\[
\frac1{D_m}\operatorname{conv}A_m
\subseteq
K_m,
\tag{C43.8}
\]

where

\[
K_m
:=
\overline B(\tilde x_m,1)
\cap
\overline B(\tilde y_m,1)
\cap
\overline B(\tilde z_m,1).
\tag{C43.9}
\]

The three centers converge to the unit equilateral triple, so the compact convex sets `K_m` converge in Hausdorff distance to the unit Reuleaux triangle `R_1`.

Area and perimeter are continuous under Hausdorff convergence for planar convex bodies. Therefore

\[
\operatorname{area}(K_m)
\longrightarrow
\operatorname{area}(R_1)
=
\frac{\pi-\sqrt3}{2},
\tag{C43.10}
\]

and `per(K_m)` remains uniformly bounded.

---

## 3. Normalize the half-unit parallel body

The canonical lower diameter estimate implies `D_m->infty` as `n_m->infty`. Put

\[
t_m:=\frac1{2D_m}\longrightarrow0.
\tag{C43.11}
\]

From C43.8,

\[
\frac1{D_m}
\left(\operatorname{conv}A_m+B(0,1/2)\right)
\subseteq
K_m+B(0,t_m).
\tag{C43.12}
\]

Steiner's formula gives

\[
\operatorname{area}(K_m+B(0,t_m))
=
\operatorname{area}(K_m)
+t_m\operatorname{per}(K_m)
+\pi t_m^2.
\tag{C43.13}
\]

Using C43.10-C43.11,

\[
\limsup_{m\to\infty}
\frac{\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))}{D_m^2}
\le
\boxed{\frac{\pi-\sqrt3}{2}}.
\tag{C43.14}
\]

---

## 4. Global minimum diameter forces a larger normalized area

The canonical Fejes Tóth finite-packing inequality gives

\[
\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))
\ge
\frac{\sqrt3}{2}n_m.
\tag{C43.15}
\]

For a global minimizer the canonical strict diameter upper bound is

\[
D_m^2<\frac{n_m}{\Delta_2},
\qquad
\Delta_2=\frac\pi{2\sqrt3}.
\tag{C43.16}
\]

Hence

\[
\frac{n_m}{D_m^2}>\Delta_2,
\]

and therefore for every `m`,

\[
\frac{\operatorname{area}(\operatorname{conv}A_m+B(0,1/2))}{D_m^2}
>
\frac{\sqrt3}{2}\Delta_2
=
\boxed{\frac\pi4}.
\tag{C43.17}
\]

But

\[
\frac{\pi-\sqrt3}{2}<\frac\pi4
\iff
\pi<2\sqrt3,
\tag{C43.18}
\]

so C43.14 and C43.17 contradict each other. This proves C43. `square`

---

## 5. Immediate geometric corollaries

### Corollary C43.1 — threshold near-diameter graph is triangle-free

For the constants in C43, define

\[
G_{near}(A)
:=
\{ij:|p_i-p_j|>(1-\eta_0)D(n)\}.
\tag{C43.19}
\]

Then every sufficiently large global minimizer has triangle-free `G_near(A)`.

This graph contains the full diameter graph and every sufficiently near-diameter pair, not merely KKT-visible pairs.

### Corollary C43.2 — uniform componentwise response geometry in C-II

In the C-II harmonic-component notation of C36-C41, every attachment set `A_r` has at least three vertices. Hence every `A_r` contains a pair `s,t` with

\[
|s-t|\le(1-\eta_0)D.
\tag{C43.20}
\]

C41 says the component response is a strict clique on `A_r`, so the corresponding conductance satisfies `c^{(r)}_{st}>0`. Therefore the C41 component defect obeys

\[
E_r
:=
\sum_{u<v\in A_r}c^{(r)}_{uv}(D^2-|u-v|^2)
\ge
\gamma_0D^2 c^{(r)}_{st}>0,
\tag{C43.21}
\]

where

\[
\boxed{\gamma_0:=1-(1-\eta_0)^2>0.}
\tag{C43.22}
\]

Thus C41's strictness is now uniformly geometric per unit of short-pair effective conductance. What remains uncontrolled is the magnitude of that conductance itself.

---

## 6. Exact effect on Target C

C43 removes a remaining qualitative loophole in the Reuleaux geometry:

```text
large global minimizer:
    no triple can approach the equilateral full-diameter shape
    uniformly in n and independently of KKT support

C-II harmonic response:
    every attachment clique contains a uniformly subdiametral pair
    each such pair pays at least gamma_0 D^2 per unit response conductance
```

This does not yet close the near-minimal response phase because the effective conductance on the forced short pair may tend to zero. A genuine closing theorem must now control **response weight**, not merely response support geometry.

The shortest response-side target becomes:

> **Short-response mass theorem.** Prove that in the C33 near-minimal boundary phase, the total C11 response conductance on pairs with distance at most `(1-eta_0)D` is bounded below by an absolute positive constant.

Combined with C41 and C43 this would give an absolute trace gap

\[
\operatorname{tr}(\Lambda-L_H)\ge c>0.
\]

A further matrix/packing argument would still be required to turn that gap into Level I, but the missing step would be quantitative and explicit.

---

## 7. Regression audit

- **Small regular polygons:** irrelevant; C43 is asymptotic in global minimizers.
- **Exact diameter triangle:** C43 subsumes C15 for sufficiently large `n`.
- **Near-equilateral but nonglobal configurations:** allowed. Global minimum-diameter packing is essential through C43.16-C43.17.
- **KKT-invisible points:** fully covered; C43 is a theorem about arbitrary source triples.
- **Tiny response conductance:** not excluded. C43 gives a uniform geometric deficit per unit conductance, not a conductance lower bound.
- **C-I:** C43 itself is global and may be used there, but Corollary C43.2 uses the C-II harmonic-component structure.

```text
C43:
There exist eta_0>0,n_0 such that every triple in every global minimizer with n>=n_0
has one pair at distance <=(1-eta_0)D(n).

Proof: otherwise choose n_m->infty and triples with all three normalized pair distances
->1. After scaling they converge to a unit equilateral triple, so the whole source lies
in intersections K_m of three unit disks converging to the unit Reuleaux triangle.
The normalized half-unit parallel-body area then has limsup <=(pi-sqrt3)/2, while
Fejes Toth plus the strict global D(n) upper bound gives it >pi/4. Contradiction.

In C-II every C36 attachment clique therefore contains a response pair with uniform
geometric deficit D^2-|s-t|^2 >= gamma_0 D^2. Only its effective conductance remains
uncontrolled.
```
