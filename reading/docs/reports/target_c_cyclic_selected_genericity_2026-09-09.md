> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_selected_genericity_2026-09-09.md) · source SHA-256 `1adf50e5a3a6ced31c4bdf04240cc66dba8a942201b42cc52e218a2fd85468c1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 10 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-13A54EF55684","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: every selected stress is generic and maximal-rank

**Date:** 2026-09-09  
**Repository base:** PR #118 after CY selected-support theorem  
**Run type:** exact support-stable transfer/rank refinement  
**Target:** Target C, C-II cyclic primitive endpoint  
**Depends on:** CY.1-CY.2, C53/C56, Theorem Z zero-transfer exclusion, SEPq degree contradiction, C11 Schur/SVD correspondence  
**External web search:** not used  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

CY proves that in the primitive cyclic endpoint every normalized KKT stress has

```math
C_s=C_q,
\qquad
B_s=B_+.
```

Thus support reduction never changes the positive contact network or the terminal polygon; it can only delete positive diameter edges while keeping those edges an edge cover of all `q` terminals.

This lets the report-level zero-transfer exclusion be applied **uniformly over the entire normalized KKT polytope**, not only to the relative-interior full-support stress.

The result is:

```math
\boxed{
\text{every normalized KKT stress is in C56-G, not C56-Z},}
\tag{CG.0}
```

and consequently every selected scalar stress matrix has the same exact affine kernel

```math
\boxed{
\ker\Omega_s
=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad
\operatorname{rank}\Omega_s=q-3.}
\tag{CG.1}
```

So the entire KKT polytope lies in the relative interior of one fixed maximal-rank PSD face. Its boundary is created solely by diameter coefficients reaching zero; scalar-stress rank never drops.

---

## 1. Theorem Z applies to every selected stress

Fix any normalized KKT stress `s` in the cyclic endpoint.

CY.1 gives the complete positive contact cycle

```math
C_s=C_q.
```

Hence the positive contact network is connected and circular-planar on the full terminal set `B_+`.

CY.2 gives

```math
B_s=B_+,
```

so the positive diameter graph `H_s` has no isolated terminal. Its edges are actual diameter chords of the same strictly convex terminal polygon, hence form a straight-line geometric thrackle.

For the large post-ZF regime `q>=6`. Any edge cover of `q>=6` vertices has at least three edges, so

```math
|H_s|\ge3.
\tag{1.1}
```

These are exactly the structural hypotheses needed by Theorem Z.

Suppose `s` were in C56-Z. Theorem Z would make the complete effective-resistance metric of the positive contact network additive. SEPq then produces a contact vertex incident to at least `q` edges if unloaded or `q-1` edges if loaded.

Every terminal here is loaded, and its actual positive contact degree in `C_s=C_q` is exactly two. For `q>=6`,

```math
q-1>2.
```

Contradiction.

Therefore:

### Theorem CG.1 — support-stable generic transfer

For every normalized KKT stress of a sufficiently large cyclic survivor,

```math
\boxed{\text{C56-G holds and C56-Z is impossible}.}
\tag{CG.2}
```

In C56 notation the minimum off-diagonal transfer is strictly negative and the edge-defect kernel is exactly

```math
\operatorname{span}\{\mathbf1,t\}.
\tag{1.2}
```

---

## 2. SVD transfer from edge defect to scalar stress rank

For the selected stress `s`, let

- `Lambda` be the positive-contact Dirichlet response on the terminal set;
- `L_H` be the beta-weighted selected diameter Laplacian;
- `Omega_s=Lambda-L_H`.

There are no positive-contact interior vertices in the cyclic endpoint, so

```math
\Lambda=L_{C_q}(\alpha).
\tag{2.1}
```

On the zero-sum terminal space, define as in the ZR proof

```math
Y=\Lambda^{-1/2}Q B_H^{1/2},
\tag{2.2}
```

where `Q` is the selected diameter incidence matrix and `B_H` the positive diagonal beta matrix.

The C56 edge defect is congruent to

```math
I-Y^{\mathsf T}Y.
```

CG.1/C56-G says the zero eigenvalue of this edge defect has multiplicity exactly two. The nonzero singular values of `Y` are the same from the left and the right, so

```math
I-YY^{\mathsf T}
```

also has zero eigenvalue with multiplicity exactly two.

But the selected boundary defect on the zero-sum terminal space is congruent to

```math
I-YY^{\mathsf T}.
```

Restoring the constant boundary mode adds exactly one kernel dimension. Therefore

```math
\operatorname{nullity}\Omega_s=3.
\tag{2.3}
```

The affine vectors

```math
\mathbf1,P_x,P_y
```

already lie in the kernel by the C11 equilibrium identity and are independent because the force hull is two-dimensional. They therefore exhaust it.

This proves CG.1. `square`

---

## 3. The rank does not drop on the KKT-polytope boundary

Universal selected-stress PSD gives

```math
\Omega_s\succeq0
```

for every normalized KKT stress. CG.1 sharpens this in the cyclic endpoint to

```math
\boxed{
\Omega_s\succeq0,
\qquad
\operatorname{rank}\Omega_s=q-3
\quad(s\in\mathcal S).}
\tag{CG.3}
```

Thus every selected stress has the **same** scalar kernel

```math
K_{aff}:=\operatorname{span}\{1,P_x,P_y\}.
```

Equivalently, after restricting to `K_aff^perp`, every `Omega_s` is positive definite.

For a fixed source the KKT polytope is compact, so the smallest positive eigenvalue has a positive minimum over the complete polytope:

```math
\boxed{
\mu_{cyc}:=
\min_{s\in\mathcal S}
\lambda_{min}(\Omega_s|_{K_{aff}^{\perp}})
>0.}
\tag{CG.4}
```

No uniform-in-`D` lower bound is claimed. The number `mu_cyc` may tend to zero along an unbounded sequence.

The important structural point is exact: KKT-polytope boundary formation never comes from a new scalar zero mode.

---

## 4. Only diameter coordinates define KKT boundary faces

CY.1 already proves every cycle coefficient `alpha_e` is positive at every point of `S`. Compactness therefore gives, for the fixed source,

```math
\boxed{
\alpha_e\ge a_e^{min}>0
\qquad(e\in C_q,\ s\in\mathcal S).}
\tag{4.1}
```

Hence no normalized KKT-polytope face lies in a contact coordinate hyperplane.

All proper faces of `S` arise solely from conditions

```math
\beta_h=0
```

on selected diameter edges, while the selected diameter support continues to cover all `q` terminals by CY.2.

Thus:

### Corollary CG.2 — diameter-only face lattice

The face lattice of the cyclic KKT polytope is induced entirely by the nonnegativity facets of the diameter coefficients. Every face retains

```math
C_s=C_q,
\qquad B_s=B_+,
\qquad \operatorname{rank}\Omega_s=q-3.
\tag{CG.5}
```

This reduces the low-dimensional stress-family problem to a polytope in diameter-weight coordinates; contact support and stress rank are frozen.

---

## 5. Extreme stresses are maximal-rank edge-cover stresses

CY gives for every extreme stress

```math
\lceil q/2\rceil
\le h_s:=|H_s|
\le q-2.
```

CG adds

```math
\operatorname{rank}\Omega_s=q-3.
```

Therefore every KKT extreme simultaneously has:

1. all `q` positive unit cycle contacts;
2. a positive diameter edge cover on all `q` terminals;
3. at most `q-2` positive diameter edges;
4. a maximal-rank PSD scalar stress matrix with affine kernel only;
5. C56 generic negative transfer.

No zero-transfer forest extreme survives, even if the selected `H_s` itself happens to be a forest as an abstract graph. The C56 phase is determined by transfer, not by forest topology alone.

---

## 6. Interaction with the three full-support subcases

Recall

```math
(d_H,s_Z)=(0,2),(1,1),(2,0).
```

### `d_H=2`

The KKT polytope is a singleton. CY already makes the full mixed graph a rigidity circuit. CG says its unique stress is generic-transfer and maximal-rank PSD.

### `d_H=1`

The KKT polytope is a line segment. Both endpoints are extreme stresses. Since every cycle coefficient stays positive, each endpoint is reached only by one or more diameter coefficients becoming zero. Both endpoint diameter supports still cover all `q` vertices and both endpoint stress matrices retain rank `q-3`.

### `d_H=0`

The KKT polytope is two-dimensional. Every boundary edge and vertex again comes only from diameter coefficients vanishing. Every KKT-polytope vertex is a maximal-rank PSD edge-cover stress in C56-G.

The remaining stress-family problem is therefore finite-dimensional in a literal sense: dimensions `0,1,2`, with no hidden support or kernel degeneration on its boundary.

---

## 7. Why this is useful but not yet a contradiction

Abstract maximal-rank PSD stresses on sparse convex frameworks exist. The regular odd-shell regression is compatible with a two-dimensional full stress family and prevents a purely matrix-rank contradiction.

CG instead removes two escape mechanisms from future arguments:

1. a stress-family boundary cannot evade a theorem by dropping cycle contacts or force-hull terminals;
2. a boundary stress cannot acquire an extra scalar kernel or enter the zero-transfer phase.

Any deformation/compactness argument on `S` may therefore move all the way to an extreme stress without changing the mechanical cycle or losing maximal scalar rank.

---

## 8. Next theorem

The strongest next target is now:

> **CG-extreme exclusion/stability.**  Classify maximal-rank PSD C56-G equilibrium stresses supported on a convex equilateral cycle plus a diameter-thrackle edge cover of size at most `q-2`.

Two concrete forms would suffice:

1. prove every such extreme stress forces the primal cycle into a Reinhardt/regular small-polygon equality family and then use the quadratic rattler population from CY; or
2. prove every such extreme support admits a source-preserving finite replacement of the `O(D)` shell.

The d_H=1 and d_H=0 cases can then be reduced to their stress-polytope endpoints without fear of losing the hypotheses.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The proof is exact downstream of report-level CY and Theorem Z/C56. No canonical route map is changed.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

CY gives for every normalized stress in the cyclic endpoint:
  C_s=C_q,
  B_s=B_+,
so H_s is a diameter edge cover of all q terminals.

For q>=6, H_s has at least 3 edges. Therefore Theorem Z applies to every selected
stress. C56-Z would make the cycle resistance metric additive and SEPq would force
a loaded contact degree >=q-1, contradicting deg_C=2. Hence every stress is C56-G.

The C56 edge defect has nullity exactly two. The same SVD/Schur correspondence used
in ZR gives, for every normalized stress,
  ker Omega_s = span{1,P_x,P_y},
  rank Omega_s = q-3.
Thus scalar-stress rank never drops on the KKT-polytope boundary.

Since CY also keeps every alpha_e>0 throughout S, every proper KKT face is created
only by beta_h=0 diameter coordinates. Every face still has full cycle contact
support, all q terminals, C56-G, and maximal scalar rank.

Next: classify/exclude the extreme maximal-rank PSD edge-cover stresses; d_H=0,1
can be pushed to polytope endpoints without losing any cyclic hypothesis.
```
