> Generated reading edition · [exact source](../../../docs/reports/target_c_regular_polygon_strict_negative_transfer_regression_2026-09-11.md) · source SHA-256 `6103a4fcb1bfaa6b3385c60ea858cacd69af9e653f8b59b6faebe076c61eb40e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C255C3FC3BF4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: regular polygon realizes the strict-negative transfer phase

**Date:** 2026-09-11  
**Status:** STILL OPEN; regression report  
**Target:** C-II strict-negative response branch  
**Dependencies:** C53 response normalization only  
**Computation:** none

## Statement

For every integer $`k\ge3`$, a regular $`2k`$-gon with side length one is a
triangle-free unit-separated configuration with diameter

```math
D_k=\frac1{\sin(\pi/(2k))}.
```

Its positive unit-contact graph is one bridgeless cycle, its positive diameter
graph is the antipodal matching, and its normalized positive KKT stress has a
strictly negative C53 transfer entry. The family is not claimed to be globally
minimum-diameter for its cardinality.

## Construction and KKT stress

Put

```math
\phi=\frac{\pi}{k},\qquad
R=\frac1{2\sin(\phi/2)},\qquad
p_j=R(\cos(j\phi),\sin(j\phi)),
\quad 0\le j<2k.
```

For a chord spanning $`r`$ polygon steps,

```math
|p_{j+r}-p_j|
=\frac{\sin(r\pi/(2k))}{\sin(\pi/(2k))}.
```

Thus the only unit contacts are consecutive vertices, the only diameter pairs
are antipodal pairs, and the unit-contact graph is $`C_{2k}`$. It has no triangle.

Give each contact edge coefficient

```math
\alpha=\frac1{2k\sin^2(\phi/2)}
```

and each antipodal diameter edge coefficient $`\beta=1/k`$. Then

```math
\sum_{ij\in C}\alpha_{ij}=D_k^2,\qquad
\sum_{h\in H}\beta_h=1.
```

At $`p_j`$,

```math
\bigl(L_C(\alpha)P\bigr)_j
=4\alpha\sin^2(\phi/2)p_j,
\qquad
\bigl(L_H(\beta)P\bigr)_j=2\beta p_j.
```

Hence $`L_C(\alpha)P=L_H(\beta)P`$, so the affine KKT equilibrium holds with all
active coefficients positive.

## Exact negative transfer

Let $`L_0`$ be the unweighted cycle Laplacian and orient

```math
q_i=e_{i+k}-e_i,\qquad 0\le i<k.
```

Since every vertex is a boundary terminal,
$`\Lambda=\alpha L_0`$ and $`\Lambda^+=\alpha^{-1}L_0^+`$.

For the unit current $`q_0=e_k-e_0`$, set $`V_0=0`$. The potential is

```math
V_j=\frac j2\quad(0\le j\le k),\qquad
V_{k+r}=\frac{k-r}{2}\quad(0\le r\le k).
```

Therefore

```math
\begin{aligned}
q_{k-1}^{\mathsf T}L_0^+q_0
&=V_{2k-1}-V_{k-1}\\
&=\frac12-\frac{k-1}{2}
=1-\frac k2<0.
\end{aligned}
```

Consequently

```math
\boxed{
K_{k-1,0}
=q_{k-1}^{\mathsf T}\Lambda^+q_0
=\frac1\alpha\left(1-\frac k2\right)<0.
}
```

The vectors $`p_{i+k}-p_i`$ occupy an open half-plane of angular width
$`\pi-\pi/k<\pi`$, so these orientations are compatible with one C53 projective
cut.

## Exact effect on the research route

This is an unbounded triangle-free unit-contact/KKT family with one common
bridgeless contact block and $`\min_{e\ne f}K_{ef}<0`$. It rules out closing the
strict-negative branch using only response positivity, unit-contact geometry, KKT
equilibrium, or common-block topology.

It is not a disproof of Erdős Problem #99. It has $`2k=O(D_k)`$ points instead of
the $`\asymp D^2`$ population of a global minimum-diameter configuration, and no
global-optimality certificate. The missing ingredient is therefore genuinely
global population/minimum-diameter control, not another local response sign lemma.
