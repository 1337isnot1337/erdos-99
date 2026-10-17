> Generated reading edition · [exact source](../../../docs/reports/target_c_negative_transfer_two_crossing_normal_form_2026-09-11.md) · source SHA-256 `94feeed63f2771534d3b7c72f95088252549caa3911d85393d7fb53f4c0a71cc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-174393B84608","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — two-crossing negative response splits have a terminal normal form

**Date:** 2026-09-11
**Status:** new proved theorem, hold report
**Target:** C-II strict-negative transfer branch

## Statement

Let $`H`$ be the actual loaded diameter graph in the canonical C-II source. Use the
consistent C53 circular terminal order and its positive circular-interval split
representation

```math
K=Q^{\mathsf T}\Lambda^+Q
 =\sum_A\lambda_A z_Az_A^{\mathsf T},
\qquad \lambda_A\ge0.
```

Suppose a split $`A\mid A^c`$ contributes negatively to an off-diagonal transfer
between two diameter edges $`e_0\ne e_{m-1}`$. Thus

```math
\lambda_A>0,\qquad z_{A,0}z_{A,m-1}=-1.
```

Write $`k_A=|\operatorname{supp}z_A|`$, the number of diameter edges crossing the
split. Then $`k_A\ge2`$. One of the two interval shores, say $`S`$, satisfies

```math
H[S]=\varnothing,\qquad |S|\le k_A.
\tag{1}
```

If $`k_A=2`$, exactly one of the following holds:

1. $`S=\{v\}`$ and $`\deg_H(v)=2`$;
2. $`S=\{u,v\}`$, $`uv\notin E(H)`$, and
   $`\deg_H(u)=\deg_H(v)=1`$.

In the Woodall cyclic branch, case 1 is a cycle vertex with no pendant diameter leaf
attached, and case 2 is a pair of pendant diameter leaves. In the Woodall forest
branch, case 1 is a degree-two vertex of a caterpillar and case 2 is a pair of
diameter leaves.

This is a response-to-diameter normal form, not a contact-separator theorem. It does
not exclude the strict-negative branch.

## Proof

The C53 split representation has one vector $`z_A`$ for each circular interval
shore. Since $`z_{A,0}z_{A,m-1}=-1`$, both $`e_0`$ and $`e_{m-1}`$ cross the split.
They are distinct, so

```math
k_A\ge2.
\tag{2}
```

The loaded diameter graph is a straight-line thrackle in the strictly convex terminal
order. If both $`H[A]`$ and $`H[A^c]`$ contained an edge, those two edges would have
four endpoints in disjoint circular intervals. Their straight chords would be
disjoint and noncrossing, contradicting the thrackle property. Therefore one shore,
call it $`S`$, has no internal $`H`$-edge.

Every loaded vertex belongs to at least one diameter edge. Since $`H[S]`$ is empty,
every diameter edge incident with a vertex of $`S`$ crosses the cut. Counting one
endpoint in $`S`$ for every crossing edge gives

```math
|S|\le\sum_{v\in S}\deg_H(v)=k_A.
\tag{3}
```

This proves (1).

Now assume $`k_A=2`$. If $`|S|=1`$, equation (3) and the fact that the unique vertex
is loaded give $`\deg_H(v)=2`$, proving case 1. If $`|S|=2`$, the sum of the two
degrees is exactly $`k_A=2`$, and both vertices are loaded, so both degrees are one.
The shore is independent by construction, proving case 2. A larger $`S`$ is
impossible by (3). This proves the normal form.

Woodall's classification says that the cyclic branch is one odd unicyclic component
with pendant leaves, while the forest branch consists of caterpillars. In the cyclic
case a degree-two vertex is a cycle vertex without an attached pendant leaf, and a
degree-one vertex is a pendant leaf. In the forest case the same degree descriptions
are the corresponding caterpillar descriptions. $`\square`$

## Exact response consequence

For a negative off-diagonal entry,

```math
K_{0,m-1}
 =\sum_A\lambda_Az_{A,0}z_{A,m-1}<0.
```

The negative contributions therefore have total coefficient larger than the positive
contributions after the same pair is fixed. The theorem says that every
two-crossing negative contribution is supported on either

- the two diameter edges incident with one loaded degree-two vertex; or
- two diameter-leaf edges whose terminal vertices form an interval shore.

This is the only support-size-$`2`$ possibility. A support-size-$`1`$ split cannot
contribute to an off-diagonal entry with opposite signs.

## Why this does not close C-II

The response split coefficient $`\lambda_A`$ has no established positive lower bound.
Thus a large-support split may carry the whole strict-negative sign with arbitrarily
small coefficient, and a family of two-crossing splits may also have total mass
tending to zero. The theorem does not convert $`S`$ into a contact cut: $`S`$ is a
shore in the circular response decomposition, not a component of $`C\setminus e`$.
Consequently C35 degree caps and the $`3d_H`$ forest charge cannot be applied to
$`S`$ without a new response-to-contact transport lemma.

The regular odd and even polygon response regressions realize the degree-two
alternative, while the weighted four-cycle realizes strict-negative cancellation in a
bridgeless contact block. Both remain compatible with the theorem. The unresolved
case is therefore the large-support or vanishing-mass strict-negative phase, together
with the missing global source-capacity implication.

## Scope audit

- Contact-isolated source points are irrelevant to the response statement and are not
  discarded from C-II.
- Shared diameter endpoints are allowed; the proof uses only loaded degree counting.
- Repeated outer-walk edges do not affect the diameter-thrackle argument.
- Exceptional contact faces and whole-circuit attachment exceptions are untouched.
- No $`s_Z=0`$ identity is used, so the statement does not silently extend a circuit
  identity to $`s_Z>0`$.
