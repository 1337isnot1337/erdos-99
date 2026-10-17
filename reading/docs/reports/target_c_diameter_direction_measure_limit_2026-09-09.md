> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_direction_measure_limit_2026-09-09.md) · source SHA-256 `f4b0fd540c28a2a18e1652018547a5e251da773a4fd1a0c3a7e78507bd8f3806`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 8 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-4742E60725D2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DDM: separated exact diameter directions survive as positive measure in convex-body limits

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** compactness / diameter-direction measure lemma  
**Target:** shared post-ZF convex-hull limit theory; immediate HKN corollary  
**Depends on:** elementary Hausdorff convergence of convex bodies; no external theorem beyond compactness  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

The post-ZF diameter graph supplies not only two separated diameter directions but `Theta(D)` exact diameter directions at the vanishing separation scale `Theta(1/D)`. Under normalized Hausdorff convergence, that density cannot collapse into finitely many limiting directions.

The vanishing-scale hypothesis is essential and is stated explicitly below. Without `delta_j -> 0`, a singleton direction set would satisfy an arbitrarily chosen positive separation parameter vacuously and no measure conclusion would follow.

### Theorem DDM — diameter-direction measure lower semicontinuity

Let `K_j` be planar compact convex bodies with

```math
\operatorname{diam}(K_j)=1
```

and

```math
K_j\to K
```

in Hausdorff distance. Let `S_j` be finite sets of projective directions of unit-length chords of `K_j`. Suppose

```math
\boxed{\delta_j>0,\qquad \delta_j\to0,}
\tag{DDM.0}
```

that distinct directions in `S_j` have projective distance at least `delta_j`, and that

```math
\liminf_j |S_j|\,\delta_j\ge c.
```

Let `S(K)` denote the projective directions of diameter chords of `K`. Then

```math
\boxed{\mu(S(K))\ge c,}
\tag{DDM.1}
```

where `mu` is projective-circle arc length on `R/pi Z`.

In particular, if `c>0`, the Hausdorff limit `K` cannot be a polygon.

For the HKS threshold sequence, C67 gives

```math
\delta_j=2\arcsin\frac1{2D_j}\to0,
```

while HKN forces

```math
\frac{h_j}{D_j}\to\frac{p_c}{2}.
```

Since `D_j delta_j->1`, DDM gives

```math
\boxed{
\mu(S(K_\infty))
\ge\frac{p_c}{2}
=1.5176561597019888\ldots .
}
\tag{DDM.2}
```

Sharp Hemmi equality makes `K_infty` a six-sided polygon. This gives a second contradiction for HKN.

---

## 1. Diameter directions cannot escape the limiting diameter set

Let

```math
S(K)\subset\mathbb R/\pi\mathbb Z
```

be the set of projective directions of all pairs `x,y in K` with `|x-y|=1`.

### Lemma DDM.1 — eventual neighborhood containment

For every `epsilon>0`, there exists `j_0` such that

```math
\boxed{
S_j\subset N_\epsilon(S(K))
\qquad(j\ge j_0),
}
\tag{DDM.3}
```

where `N_epsilon` is the projective `epsilon`-neighborhood.

#### Proof

Otherwise there are indices tending to infinity and directions

```math
\theta_j\in S_j
```

with

```math
d(\theta_j,S(K))\ge\epsilon.
```

Choose endpoints

```math
x_j,y_j\in K_j,
\qquad
|x_j-y_j|=1,
```

whose chord has projective direction `theta_j`.

After one fixed translation convention, all normalized bodies lie in a common bounded region. Pass to a subsequence with

```math
x_j\to x,
\qquad
y_j\to y,
\qquad
\theta_j\to\theta.
```

Hausdorff convergence gives `x,y in K`, and continuity gives

```math
|x-y|=1.
```

Thus `theta in S(K)`, contradicting

```math
d(\theta_j,S(K))\ge\epsilon.
```

`square`

---

## 2. Thicken the separated finite direction sets

Around every

```math
\theta\in S_j
```

take the closed projective arc of radius `delta_j/2`. Because the centers are pairwise separated by at least `delta_j`, the arc interiors are disjoint.

Let their union be `U_j`. Then

```math
\boxed{
\mu(U_j)=|S_j|\delta_j.
}
\tag{DDM.4}
```

Fix `epsilon>0`. By DDM.3, for all sufficiently large `j`, every center lies in `N_epsilon(S(K))`. Because `delta_j->0`, eventually `delta_j/2<epsilon`, and therefore

```math
\boxed{
U_j\subset N_{2\epsilon}(S(K)).
}
\tag{DDM.5}
```

Taking lower limits gives

```math
c
\le
\liminf_j\mu(U_j)
\le
\mu(N_{2\epsilon}(S(K))).
\tag{DDM.6}
```

The set `S(K)` is compact: it is the continuous image in projective direction of the compact set of diameter pairs

```math
\{(x,y)\in K^2:|x-y|=1\}.
```

Hence the neighborhoods `N_{2epsilon}(S(K))` decrease to `S(K)` as `epsilon downarrow0`, and finite Haar measure is continuous from above. Thus

```math
\boxed{
\mu(S(K))
=
\lim_{\epsilon\downarrow0}
\mu(N_{2\epsilon}(S(K)))
\ge c.
}
```

This proves DDM.1.

---

## 3. A polygon has finitely many diameter directions

Let `P` be a nondegenerate convex polygon.

Suppose `x` lies in the relative interior of one polygon edge and `y in P` is fixed. Parameterize that edge by

```math
x(t)=x_0+tv.
```

Then

```math
|x(t)-y|^2
```

is a strictly convex quadratic in `t`. Its maximum on the edge occurs at an endpoint, and every interior value is strictly below the larger endpoint value. Therefore an endpoint of a global diameter pair cannot lie in the relative interior of an edge.

Thus every endpoint of a diameter pair of a polygon is a polygon vertex. A finite polygon has finitely many vertex pairs, hence finitely many projective diameter directions. Therefore

```math
\boxed{\mu(S(P))=0.}
\tag{DDM.7}
```

Combining DDM.1 and DDM.7 proves the polygon-exclusion clause whenever `c>0`.

---

## 4. HKS/HKN application

Assume the HKN threshold-approaching sequence. Normalize

```math
K_j=D_j^{-1}(F_j-x_j).
```

HKN proves

```math
K_j\to K_\infty,
\qquad
\frac{h_j}{D_j}\to\frac{p_c}{2}.
```

Take `S_j` to be the complete set of actual diameter-edge projective directions. C67 gives

```math
\delta_j
=2\arcsin\frac1{2D_j},
\qquad
D_j\delta_j\to1.
```

In particular `delta_j->0`, as required by DDM.0. Therefore

```math
|S_j|\delta_j
=h_j\delta_j
\to\frac{p_c}{2}.
```

DDM gives DDM.2.

Sharp Hemmi equality at perimeter `p_c` and area `A_H(p_c)` classifies `K_infty` as the six-sided first-branch Hemmi polygon. By DDM.7 its diameter-direction set has measure zero. Contradiction.

This reproves HKN without using the final PI endpoint-hull area-equality step. The contradiction uses only:

1. HKS forcing the Hemmi equality body in the limit;
2. positive asymptotic diameter-direction packing mass at a vanishing angular scale.

---

## 5. General post-ZF consequence

Any future argument that drives a post-ZF force-hull limit into a finite polygonal equality class must account for DDM.

Because DB gives

```math
\liminf h/D\ge2\rho>0,
```

and C67 gives

```math
D\delta_D\to1,
\qquad
\delta_D\to0,
```

any normalized Hausdorff limit `K` of an unbounded post-ZF survivor subsequence satisfies

```math
\boxed{\mu(S(K))\ge2\rho.}
\tag{DDM.8}
```

Thus

```math
\boxed{
\text{no normalized post-ZF force-hull subsequential limit can be a finite polygon.}
}
\tag{DDM.9}
```

This is independent of the HKS scalar near-equality assumption.

---

## 6. Caveats

- The vanishing-scale hypothesis `delta_j->0` is essential to DDM as stated.
- DDM concerns exact diameter chords, not near-diameter pairs.
- Positive measure of diameter directions does not imply constant width in every direction.
- The theorem gives no quantitative finite-`D` Hausdorff distance from polygons.
- Smooth or partially constant-width limiting bodies remain possible.

---

## 7. Classification

**Status:** proved shared compactness lemma, corrected to include its necessary vanishing-separation hypothesis.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.

## 8. Next target

Translate positive diameter-direction measure into a direct convex-geometric area/perimeter improvement.

A natural target is:

> among diameter-one planar convex bodies with projective diameter-direction set of measure at least `s`, determine or lower-bound the minimum area as a function of perimeter and `s`.

At the HKS crossover one has

```math
s\ge p_c/2.
```

Any lower-area bound strictly above the unconstrained Hemmi minimum `A_H(p_c)` would make the HKN gap explicit and raise the scalar surplus floor quantitatively.

## 9. Compact handoff

```text
DDM (corrected):
If K_j -> K in Hausdorff distance, diam K_j=1, delta_j->0, and S_j are exact
diameter directions separated by delta_j with liminf |S_j|delta_j>=c, then the
limiting exact diameter-direction set S(K) has projective measure >=c.

Proof: all S_j eventually lie in every fixed neighborhood of S(K); otherwise choose
escaping diameter chords and take endpoint/direction limits. Thickened radius-
delta_j/2 arcs around S_j are disjoint and have total measure |S_j|delta_j. The
vanishing-scale assumption puts those arcs inside arbitrarily small neighborhoods of
S(K), so neighborhood continuity gives mu(S(K))>=c.

A finite polygon has diameter endpoints only at vertices, hence finitely many diameter
directions and measure zero.

Post-ZF: C67 has delta_D=2 asin(1/(2D))->0 and D delta_D->1, while DB gives
h/D>=2rho. Therefore every normalized force-hull Hausdorff limit has exact diameter-
direction measure >=2rho and cannot be a finite polygon.
```
