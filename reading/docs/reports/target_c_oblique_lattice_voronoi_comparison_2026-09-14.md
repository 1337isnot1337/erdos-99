> Generated reading edition · [exact source](../../../docs/reports/target_c_oblique_lattice_voronoi_comparison_2026-09-14.md) · source SHA-256 `c0c017b0603ae3c0649d41381315f12686308d5c2915d042e9c822690b613112`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-70D0F38992B1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Voronoi-cell comparison for an oblique affine source

**Date:** 2026-09-14  
**Repository commit:** 06021a626e3bfb35a5135d87debcb3a2b1a84263  
**State version:** 2026-09-14.audit.51  
**Run type:** closing proof / restricted source-level comparison  
**Target:** Target C-II / restricted affine-source subroute  
**Starting status:** canonical restricted oblique-lattice comparison; C-II remains open  
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md  
**External literature search:** used for context; no external theorem is imported below  
**Computation:** not used for the proof

## LEVEL I STATUS

STILL OPEN

This report proves a finite, source-cardinality-exact strengthening of the
restricted exact-affine-lattice comparison. It does not prove that a canonical
full-core source is one affine lattice, and it does not settle either C-II branch.

## 1. Starting endpoint and implication chain

The canonical restricted comparison used a radius-two fundamental parallelogram.
For a finite full-dimensional subset of one oblique unit lattice it gave the
sufficient condition

```math
 (1-\kappa_\theta)D>4\kappa_\theta+2/\sqrt3,
 \qquad
 \kappa_\theta=\sqrt{\frac{\sqrt3/2}{\sin\theta}},
```

for a strict same-cardinality triangular-lattice competitor. The present argument
uses the exact Voronoi hexagon of the oblique lattice instead.

The intended chain is

    exact affine lattice source
        -> exact Voronoi-cell population bound
        -> same-cardinality triangular-lattice source with smaller diameter
        -> exclusion of a larger finite shear from global minimizers

The chain stops there: no canonical theorem currently supplies the exact affine
lattice hypothesis for an arbitrary C-II full-core source.

## 2. Strongest genuinely new result

**Classification:** proved candidate, unreviewed and noncanonical.

### Theorem — finite Voronoi comparison

Let $`u,v`$ be unit vectors with

```math
 \theta:=\angle(u,v)\in(\pi/3,\pi/2],
 \qquad \Lambda_\theta:=\mathbb Zu+\mathbb Zv.
```

Let $`A\subset\Lambda_\theta`$ be finite and full-dimensional, with
$`n=|A|`$ and $`D=\operatorname{diam}(A)`$. Define

```math
 s:=\sin\theta,\qquad a_0:=\frac{\sqrt3}{2},\qquad
 \rho:=\frac1{\sqrt3},\qquad
 \kappa:=\sqrt{\frac{a_0}{s}}<1,
```

and

```math
 p_V(\theta):=4\tan\frac\theta2+
                 \frac{2\cos\theta}{\cos(\theta/2)}.
```

If

```math
 \boxed{
 D>2\rho+\kappa
 \sqrt{D^2+\frac{2p_V(\theta)}{\pi}D+\frac4\pi},
 }
 \tag{V.1}
```

then there is an exactly $`n`$-point subset $`B`$ of the unit triangular lattice
with

```math
 \operatorname{diam}(B)
 \le 2\rho+\kappa
 \sqrt{D^2+\frac{2p_V(\theta)}{\pi}D+\frac4\pi}
 <D.
 \tag{V.2}
```

Consequently, $`A`$ cannot be a global minimum-diameter $`n`$-point unit-separated
configuration. The source in this statement is the full finite set $`A`$; no
contact-isolated point is removed.

The same statement applies to a basis angle in $`[\pi/2,2\pi/3)`$ after replacing
one basis vector by its negative. At the endpoint angles $`\pi/3`$ and
$`2\pi/3`$, the affine lattice itself contains unit equilateral triangles, so those
endpoints are outside the triangle-free affine subroute.

### Proof

Write $`c=\cos\theta`$, so $`0\le c<1/2`$, and use coordinates

```math
 \alpha=x\cdot u,\qquad \beta=x\cdot v.
```

The Voronoi cell of $`0`$ in $`\Lambda_\theta`$ is

```math
 V_\theta=
 \{x:|\alpha|\le1/2,\ |\beta|\le1/2,\ |\beta-\alpha|\le1-c\}.
 \tag{V.3}
```

Here is a direct verification that no other lattice inequality is needed. Let
$`z=iu+jv\ne0`$. If $`i,j`$ have the same sign, symmetry lets us assume
$`i,j\ge0`$. For $`x\in V_\theta`$,

```math
 x\cdot z\le\frac{i+j}{2}
 \le\frac{i^2+j^2+2cij}{2}=\frac{|z|^2}{2},
```

because
```math
 i^2+j^2+2cij-i-j=i(i-1)+j(j-1)+2cij\ge0.
```

If $`i,j`$ have opposite signs, write $`z=au-bv`$, with integers $`a,b\ge1`$.
For fixed $`\alpha`$, the smallest allowed $`\beta`$ is
$`\max\{-1/2,\alpha-(1-c)\}`$. Thus, when $`a\ge b`$, the objective is maximized
at $`\alpha=1/2,\beta=c-1/2`$; when $`b\ge a`$, the symmetric endpoint is
maximizing. Consequently the maximum of $`a\alpha-b\beta`$ over (V.3) is, for
$`a\ge b`$,

```math
 \frac{a+b}{2}-bc,
 \tag{V.4}
```

and for $`b\ge a`$ the symmetric expression is
$`\frac{a+b}{2}-ac`$. In the first case,

```math
 \frac{a^2+b^2-2abc}{2}-
 \left(\frac{a+b}{2}-bc\right)
 =\frac{(a-1)(a-2bc)+b(b-1)}2\ge0,
```

since $`2c<1`$ and $`a\ge b`$. The other case is symmetric. Thus (V.3) is
exactly the intersection of all perpendicular-bisector inequalities, hence is a
Voronoi cell; its translates tile the plane with disjoint interiors.

In the $`(\alpha,\beta)`$-plane, (V.3) is the unit square with two opposite
right triangles of leg $`c`$ removed. The coordinate map has Jacobian $`s`$, so

```math
 \operatorname{area}(V_\theta)=\frac{1-c^2}{s}=s.
 \tag{V.5}
```

Its four uncut sides have physical length $`(1-c)/s=\tan(\theta/2)`$, and its two
cut sides have physical length $`c/\cos(\theta/2)`$. The three edge vectors in one
half of its cyclic boundary are, in $`(\alpha,\beta)`$-coordinates,
```math
 (1-c,0),\qquad (c,c),\qquad (0,1-c).
```
Their physical vectors generate $`V_\theta`$ as a Minkowski sum of centered
segments, so this also gives the required zonotope representation below. Therefore

```math
 \operatorname{per}(V_\theta)=p_V(\theta).
 \tag{V.6}
```

Let $`K=\operatorname{conv}(A)`$. Since the translates $`a+V_\theta`$, $`a\in A`$,
have disjoint interiors and are all contained in $`K+V_\theta`$, (V.5) gives

```math
 ns\le\operatorname{area}(K+V_\theta). \tag{V.7}
```

Every centrally symmetric planar polygon is a zonotope; here the preceding edge
vectors give this representation explicitly. Write
$`V_\theta=\sum_i[-w_i/2,w_i/2]`$, omitting the zero cut-edge generator at the square
endpoint. Then $`p_V=2\sum_i|w_i|`$. Adding these generating segments one at a time gives

```math
 \operatorname{area}(K+V_\theta)
 =\operatorname{area}(K)
  +\sum_i|w_i|\,\operatorname{width}_K(w_i^\perp)
  +\operatorname{area}(V_\theta).
 \tag{V.8}
```

For clarity, (V.8) is elementary: adding a segment of vector $`w`$ increases area
by $`|w|`$ times the width perpendicular to $`w`$; the cross terms contributed by
previous generators are exactly the determinant sum for the area of their
zonotope. Since $`K`$ has diameter $`D`$, each projection width is at most $`D`$.
The isodiametric inequality and (V.5)--(V.8) therefore yield

```math
 ns\le \frac{\pi D^2}{4}+\frac{p_V(\theta)}2D+s. \tag{V.9}
```

Now use the unit triangular lattice. Its Voronoi cells have area $`a_0`$ and
covering radius $`\rho`$. If $`N_\triangle(r)`$ counts its sites in the closed
disk of radius $`r`$, the cells of those sites cover the disk of radius $`r-\rho`$.
Hence

```math
 N_\triangle(r)a_0\ge\pi(r-\rho)^2. \tag{V.10}
```

Choose
```math
 r=\rho+\sqrt{\frac{a_0n}{\pi}}. \tag{V.11}
```
Then $`N_\triangle(r)\ge n`$. Select exactly $`n`$ sites in that disk and call the
resulting source $`B`$. It is unit-separated and

```math
 \operatorname{diam}(B)\le2r
 =2\rho+2\sqrt{\frac{a_0n}{\pi}}. \tag{V.12}
```

From (V.9),

```math
 \frac{a_0n}{\pi}
 \le\frac{a_0}{s}
 \left(\frac{D^2}{4}+\frac{p_V(\theta)}{2\pi}D+\frac1\pi\right). \tag{V.13}
```

Taking square roots in (V.13) and using (V.12) gives the first quantity in
(V.2). Hypothesis (V.1) makes it strictly smaller than $`D`$, proving the
theorem. The competitor has exactly $`n`$ points, so this is a genuine
source-cardinality-preserving global-minimality contradiction.

### Consequence for the surviving affine shear scale

If a finite full-dimensional affine-lattice subset satisfies global minimality,
(V.1) must fail. Put
```math
 B=\frac{2p_V(\theta)}\pi,\qquad C=\frac4\pi.
```
Failure of (V.1) implies

```math
 (1-\kappa)D
 \le2\rho+\kappa\left(\sqrt{D^2+BD+C}-D\right), \tag{V.14}
```

and, since the denominator in the rationalized difference is at least $`2D`$,

```math
 (1-\kappa)D
 \le2\rho+\kappa\left(\frac B2+\frac C{2D}\right). \tag{V.15}
```

Thus only inverse-diameter shear remains in this exact affine class. More
explicitly,

```math
 0<s-a_0=s(1-\kappa)(1+\kappa)
 \le2(1-\kappa)=O(D^{-1}), \tag{V.16}
```

with the constant supplied by (V.15). The asymptotic boundary penalty in (V.1) is
$`2\rho+\kappa p_V(\theta)/\pi`$, rather than the old $`2\rho+4\kappa`$ penalty.
This is a finite constant improvement, not a closure of the inverse-diameter
endpoint.

## 3. Exact frontier effect

The result strengthens the canonical C-OBLIQUE-LATTICE-COMPETITOR threshold for
one exact affine lattice. It is source-level and preserves all source points, but it
does not change the canonical C-II route because the missing implication is still

    canonical full-core near-rhombic cells
        -> one exact global affine lattice containing every source point

and that implication is not proved. Phase interfaces, rhombic grains, holes,
macroscopic inactive chambers, and contact-isolated populations remain outside the
theorem.

## 4. Exact remaining lemma

A closing next lemma would have to prove one of:

1. every sufficiently large canonical full-core triangle-free minimizer admits one
   exact affine-lattice chart containing the full source;
2. a multi-grain version of (V.9) with an interface term strictly below the
   triangular competitor's boundary advantage; or
3. a source-preserving finite deformation or exact unit-triangle conclusion for the
   surviving inverse-diameter shear.

None is established here.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| (V.3) is the exact oblique Voronoi cell | proved candidate | direct lattice-vector calculation | All lattice vectors are checked by sign cases. |
| (V.5)--(V.9) | proved candidate | coordinate geometry and zonotope area identity | Applies to the full convex hull of the source. |
| Exact same-cardinality competitor (V.2) | proved candidate | triangular Voronoi covering | At least $`n`$ sites are in the selected disk and exactly $`n`$ are retained. |
| Extension to arbitrary C-II sources | unresolved | missing affine co-embedding theorem | Not inferred from local rhombi or the ZR/ZF core kernel. |
| Level-I settlement | unresolved | both C-II branches and all global minimizers | (V.1) is a restricted hypothesis. |

## 6. Regression checks

| Regression/correction | Result | Exact reason |
| --- | --- | --- |
| Vanishing shear $`\theta=\pi/3+R^{-2}`$, $`D=O(R)`$ | passes | $`(1-\kappa)D=O(R^{-1})`$, so (V.1) eventually fails. |
| Square-lattice patches | passes | The conclusion is only nonoptimality under (V.1), not a source classification. |
| Contact-isolated points | passes | Every point of $`A`$ contributes one complete Voronoi cell in (V.7). |
| Non-affine grains and phase interfaces | outside scope | No common Voronoi tiling is assumed. |
| Scalar C-II ledgers | outside scope | No scalar assignment is used as a planar source or global optimum. |
| Positive KKT stress or local jamming | outside scope | The proof constructs a finite competitor directly. |

## 7. Literature imports

The public Erdős Problems status page was checked for orientation and records
Problem 99 as open; it is not used in the proof. A related paper by
Pach--Radoičić--Radoičić--Vondrák, *On the diameter of separated point sets with
many nearly equal distances*, was checked as a near miss. No theorem from either
source is imported below.

## 8. Computation

No computation is logically required. The result follows from the finite geometric
identities (V.3)--(V.15), with no numerical search or floating-point optimization.

## 9. Corrections / supersessions

An earlier draft of this refinement used $`4\sin\theta/\pi`$ in the radical. That
factor is incorrect: after dividing (V.9) by $`s`$, the constant term is $`1`$, so
the radical contains $`4/\pi`$, independent of $`\theta`$. This report supersedes
that draft. The older radius-two theorem remains valid but weaker.

## 10. Promotion recommendation

**Unreviewed.** Preserve this as a proof candidate until an independent audit checks
the Voronoi inequalities, the zonotope area bookkeeping, and the exact cardinality
step. No theorem-state, route-map, or state-version promotion is requested.

## 11. Handoff

1. Strongest new theorem: finite Voronoi comparison (V.1)--(V.2) for one exact
   oblique affine lattice.
2. Canonical dependency chain: C-OBLIQUE-LATTICE-COMPETITOR plus elementary convex
   geometry; no full-source affine-kernel extension is used.
3. Exact remaining lemma: bridge canonical near-rhombic multi-grain sources to the
   exact affine theorem, or close inverse-diameter shear by a source-preserving
   descent/triangle argument.
4. Binding dead routes: scalar-only elimination, local stress-to-release inference,
   and source/scaffold identification.
5. Files to read next: docs/targets/target-c/CURRENT.md, canonical Sections 122--123
   modules, and the full-core higher-surplus reports.
