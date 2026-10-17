> Generated reading edition · [exact source](../../../docs/reports/target_c_odd_cyclic_quadratic_regression_2026-09-11.md) · source SHA-256 `ab2d14acada22f4d9802e7c5638f4a3ee299d2df01911e199700f9b6941efbcb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-9F2E4BA771D1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: odd cyclic quadratic-population strict-negative regression

**Date:** 2026-09-11  
**Status:** STILL OPEN; regression report  
**Target:** C-II cyclic strict-negative branch with contact-isolated points  

## Statement

For every odd $`p=2k+1`$ tending to infinity, there is a triangle-free
unit-separated configuration $`A_p`$ with

```math
D_p\asymp p,\qquad
|A_p|=\frac{\pi}{2\sqrt3}D_p^2-O(D_p),
```

whose positive unit-contact graph is a bridgeless odd cycle, whose actual diameter
graph is the same odd cycle, and whose C53 response kernel satisfies

```math
\min_{e\ne f}K_{ef}<0.
```

The construction is not claimed to be globally diameter-minimal. It is a no-go
against any C-II closure using only the local KKT/response/diameter-topology
hypotheses while ignoring global optimality.

## Polygon and population

Let

```math
\phi=\frac{2\pi}{p},\qquad
R=\frac1{2\sin(\pi/p)},\qquad
p_j=R(\cos(j\phi),\sin(j\phi)),
\quad 0\le j<p.
```

The consecutive sides have length one. The largest chord has step
$`k=(p-1)/2`$, and

```math
D_p=2R\cos\left(\frac{\pi}{2p}\right)
=\frac{\cos(\pi/(2p))}{\sin(\pi/p)}.
```

The only unit contacts are consecutive vertices, so the contact graph is $`C_p`$
and is triangle-free. The diameter pairs are exactly the step-$`k`$ chords. Each
vertex has two such neighbors, and these diameter chords form another $`p`$-cycle.
As the diameter chords of a regular odd polygon, they form a geometric thrackle:
every two share an endpoint or cross.

To obtain quadratic population, let $`s_p=1+D_p^{-1}`$, take a triangular lattice
with nearest-neighbor spacing $`s_p`$, and add all its points in $`B(0,R-2)`$.
The cloud has

```math
\frac{2\pi(R-2)^2}{\sqrt3\,s_p^2}+O(R)
=\frac{\pi}{2\sqrt3}D_p^2-O(D_p)
```

points. Cloud points are mutually farther than one and at least distance two from
the polygon. Thus the only unit contacts remain the polygon cycle. The diameter is
exactly $`D_p`$, and the whole source is triangle-free. All cloud points are
contact-isolated.

## Exact positive KKT stress

Give every polygon contact edge coefficient

```math
\alpha=\frac{D_p^2}{p}
=\frac{\cos^2(\pi/(2p))}{p\sin^2(\pi/p)}
```

and every diameter edge coefficient $`\beta=1/p`$. Then

```math
\sum_C\alpha=D_p^2,\qquad
\sum_H\beta=1.
```

At $`p_j`$, the contact Laplacian is

```math
\bigl(L_C(\alpha)P\bigr)_j
=4\alpha\sin^2(\pi/p)\,p_j.
```

The two diameter neighbors are at angular offsets
$`\pm(\pi-\pi/p)`$, so

```math
\bigl(L_H(\beta)P\bigr)_j
=4\beta\cos^2(\pi/(2p))\,p_j.
```

The displayed $`\alpha,\beta`$ make these equal. Therefore the affine KKT
equilibrium holds with strictly positive coefficients on every contact and every
diameter edge. The isolated cloud points have zero rows in both Laplacians.

## C53 forces strict negativity

Let $`\Lambda`$ be the contact-cycle response and $`Q`$ the incidence matrix of
the diameter $`p`$-cycle, with any one legal C53 orientation. The C53 sign theorem
gives

```math
\min_{e\ne f}K_{ef}\le0,\qquad
K=Q^{\mathsf T}\Lambda^+Q.
```

Suppose equality held. The audited zero-transfer implication gives
$`K=\Beta^{-1}=pI`$. But the incidence matrix $`Q`$ of a cycle with $`p`$ edges
and $`p`$ vertices has rank $`p-1`$, independently of edge orientations. Hence
there is a nonzero $`z`$ with $`Qz=0`$, and so

```math
z^{\mathsf T}Kz
=(Qz)^{\mathsf T}\Lambda^+(Qz)=0,
```

contradicting $`K=pI\succ0`$. Therefore

```math
\boxed{\min_{e\ne f}K_{ef}<0.}
```

This conclusion is orientation-independent because the argument applies after the
single legal C53 orientation is chosen.

## Exact scope

The construction has the cyclic diameter topology $`d_H=0`$, a single bridgeless
contact block, a quadratic population, and contact-isolated source points. It
therefore survives the local response, KKT, common-block, and population
regressions separately.

It is not a disproof of Erdős Problem #99. The polygon-plus-cloud diameter is not
proved minimal for the displayed cardinality. The missing condition is exactly
same-cardinality global minimum-diameter optimality. No local response theorem can
replace it.
