> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_vertex_isodiametric_defect_2026-09-10.md) · source SHA-256 `9f789bce9e4a65078d17e70b0e659c58d5e5fbd987c43c576dd8273b9d6ad337`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-9ACBE3E15FAE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — boundary-sharing attachment polygons have a uniform isodiametric defect

**Date:** 2026-09-10  
**Branch base:** `50d54f601af6a801199c5dd1b5b19cd70638bd02`  
**Run type:** quantitative convex stability / attachment-cell area defect  
**Target:** Target C, C-II after ZF  
**External input:** Bonnesen's 1924 concentric-annulus stability theorem, in the form quoted as Theorem 1.1 of Nicola Fusco, *The quantitative isoperimetric inequality and related topics*, Bull. Math. Sci. 5 (2015), 517–607, DOI `10.1007/s13373-015-0074-x`  
**Depends on:** only convexity plus the Target C fact that attachment vertices lie on the force-hull boundary

## LEVEL I STATUS

`STILL OPEN`.

ND excludes the exact RD endpoint by a compactness argument.  This report makes its
core geometric mechanism quantitative.

### Theorem BV — boundary-vertex isodiametric defect

Let `F` be a compact convex planar set of diameter `D>0`.  Let `K` be a nondegenerate
convex polygon such that

```math
K\subseteq F,
\qquad
V(K)\subseteq\partial F,
\tag{BV.1}
```

and suppose

```math
\operatorname{diam}K\le\frac35D.
\tag{BV.2}
```

Then

```math
\boxed{
\operatorname{area}K
\le
\left(\frac\pi4-\frac1{1600}\right)
\operatorname{diam}(K)^2.
}
\tag{BV.3}
```

Thus a polygon whose vertices remain on the boundary of a substantially larger convex
body cannot come arbitrarily close to the isodiametric disk bound.  The constant
`1/1600` is deliberately simple rather than optimized.

For a Target C harmonic attachment cell

```math
K_r=\operatorname{conv}A_r,
```

condition BV.1 is automatic because `A_r` consists of loaded force-hull boundary
vertices.  Therefore every attachment cell of diameter at most `3D/5` pays the same
strict quadratic area coefficient.

---

## 1. Normalize and define the isodiametric deficit

Scale so

```math
\operatorname{diam}F=1.
```

Write

```math
d:=\operatorname{diam}K\le\frac35,
\qquad
A:=\operatorname{area}K.
```

Define

```math
\boxed{
\varepsilon:=\pi d^2-4A\ge0.
}
\tag{1.1}
```

by the planar isodiametric inequality.

We prove

```math
\boxed{\varepsilon\ge d^2/400.}
\tag{1.2}
```

Equation BV.3 follows immediately after division by four.

Suppose for contradiction that

```math
\varepsilon<d^2/400.
\tag{1.3}
```

---

## 2. Bonnesen turns area deficit into a thin concentric annulus

Let `P` be the perimeter of `K`.  The planar perimeter-diameter inequality gives

```math
P\le\pi d.
\tag{2.1}
```

Bonnesen's theorem supplies concentric disks

```math
\overline B(c,r_1)\subseteq K\subseteq\overline B(c,r_2)
\tag{2.2}
```

such that

```math
(r_2-r_1)^2
\le\frac{P^2-4\pi A}{4\pi}.
\tag{2.3}
```

Using (2.1),

```math
P^2-4\pi A
\le\pi^2d^2-4\pi A
=\pi\varepsilon.
```

Hence, with

```math
w:=r_2-r_1,
```

```math
\boxed{w\le\frac{\sqrt\varepsilon}{2}.}
\tag{2.4}
```

Because `B(c,r_1) subset K`,

```math
2r_1\le d.
```

Because `K subset B(c,r_2)`,

```math
d\le2r_2.
```

Therefore `r_1<=d/2<=r_2`, and (2.4) gives

```math
\boxed{
\overline B(c,d/2-w)
\subseteq K
\subseteq
\overline B(c,d/2+w).
}
\tag{2.5}
```

Set

```math
R:=\frac d2+w,
\qquad
\rho:=\frac d2-w,
\qquad
x:=\frac{2w}{d}.
\tag{2.6}
```

By (1.3) and (2.4),

```math
\boxed{0\le x<\frac1{20}.}
\tag{2.7}
```

Also

```math
\frac\rho R=\frac{1-x}{1+x}.
\tag{2.8}
```

---

## 3. The polygon vertices force a dense set of support normals for `F`

List the vertices of `K` cyclically as

```math
v_1,\ldots,v_m.
```

For each vertex `v_i`, BV.1 gives `v_i in partial F`.  Choose one unit outer support
normal `n_i` of `F` at `v_i`.  Since `K subset F`, the same line also supports `K` at
`v_i`.

Let

```math
\alpha:=\arccos(\rho/R).
\tag{3.1}
```

We first compare all relevant normals with radial directions from the Bonnesen center
`c`.

Let `m_i` be the outward unit normal of the polygon edge `v_iv_{i+1}`.  The inner disk
in (2.5) implies

```math
(v_i-c)\cdot m_i=h_{K-c}(m_i)\ge\rho,
```

while the outer disk gives `|v_i-c|<=R`.  Thus

```math
\angle(v_i-c,m_i)\le\alpha.
\tag{3.2}
```

The same is true for `v_{i+1}`.  Hence consecutive radial directions satisfy

```math
\boxed{
\angle(v_i-c,v_{i+1}-c)\le2\alpha.
}
\tag{3.3}
```

At a polygon vertex, the normal cone lies between the normals of the two adjacent
edges.  Both adjacent edge normals are within `alpha` of the radial direction, so the
chosen force-hull support normal satisfies

```math
\boxed{
\angle(n_i,v_i-c)\le\alpha.
}
\tag{3.4}
```

By (3.3), every direction on the unit circle lies within `alpha` of some vertex radial
direction.  Combining with (3.4), the selected force-hull support normals form a
`2alpha`-net:

```math
\boxed{
\forall u\in S^1\ \exists i:
\angle(u,n_i)\le2\alpha.
}
\tag{3.5}
```

---

## 4. Dense shared supports bound the entire force hull

For every selected support normal,

```math
h_{F-c}(n_i)
=(v_i-c)\cdot n_i
\le|v_i-c|
\le R.
\tag{4.1}
```

Take any `y in F` and, if `y!=c`, let

```math
u=\frac{y-c}{|y-c|}.
```

Choose `n_i` from (3.5).  Then

```math
(y-c)\cdot n_i
=|y-c|\cos\angle(u,n_i)
\ge|y-c|\cos(2\alpha).
\tag{4.2}
```

Since the support inequality at `n_i` gives the opposite bound by `R`,

```math
|y-c|\cos(2\alpha)\le R.
\tag{4.3}
```

Under (2.7), `2alpha<pi/2`, so

```math
F\subseteq
\overline B\left(c,\frac{R}{\cos(2\alpha)}\right).
```

Therefore

```math
\boxed{
\operatorname{diam}F
\le\frac{2R}{\cos(2\alpha)}.
}
\tag{4.4}
```

Using (2.8),

```math
\cos(2\alpha)
=2\left(\frac{1-x}{1+x}\right)^2-1
=\frac{1-6x+x^2}{1+2x+x^2}.
\tag{4.5}
```

Both `2R=d(1+x)` and the reciprocal of (4.5) increase with `d` or `x` on the present
range.  Hence BV.2 and (2.7) give

```math
\operatorname{diam}F
<
\frac{(3/5)(1+1/20)}{
(1-6/20+1/400)/(1+2/20+1/400)
}.
\tag{4.6}
```

The rational values simplify to

```math
(3/5)(21/20)=\frac{63}{100},
```

and

```math
\frac{1-6/20+1/400}{1+2/20+1/400}
=\frac{281}{441}.
```

Thus

```math
\operatorname{diam}F
<
\frac{63}{100}\frac{441}{281}
=
\frac{27783}{28100}
<1.
\tag{4.7}
```

This contradicts the normalization `diam(F)=1`.

Therefore (1.3) is impossible and

```math
\varepsilon\ge d^2/400.
```

This proves BV.3.

---

## 5. Target C attachment-cell corollary

For an unloaded harmonic component `I_r`, let

```math
K_r=\operatorname{conv}A_r.
```

C36 gives `A_r subset partial F`, and C44 gives

```math
\operatorname{diam}K_r
=\operatorname{diam}A_r
\le\delta_r+2.
\tag{5.1}
```

If

```math
\delta_r+2\le\frac35D,
\tag{5.2}
```

then BV gives

```math
\operatorname{area}K_r
\le
\left(\frac\pi4-\frac1{1600}\right)
\operatorname{diam}(K_r)^2
\le
\boxed{
\left(\frac\pi4-\frac1{1600}\right)(\delta_r+2)^2.
}
\tag{5.3}
```

Now suppose along a post-ZF sequence

```math
\limsup\frac{e_{BB}+2s_C}{D}<\frac35.
\tag{5.4}
```

ZK gives

```math
\sum_r\delta_r
\le6+e_{BB}+2s_C.
```

Hence for all sufficiently large `D`, every component satisfies (5.2).  Summing (5.3)
and using

```math
\sum_r(\delta_r+2)^2
\le
\left(\sum_r\delta_r\right)^2+O(D),
```

we obtain the improved generic attachment-cell capacity

```math
\boxed{
\limsup_{D\to\infty}
\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\left(\frac\pi4-\frac1{1600}\right)
\lambda^2,
}
\tag{5.5}
```

where

```math
\lambda:=\limsup\frac{e_{BB}+2s_C}{D}<\frac35.
```

This strictly strengthens GU throughout the entire numerical neighborhood of the
current RD frontier.

---

## 6. What changes in the RSR/DD system

RD used the attachment coefficient `pi/4`.  BV replaces it by

```math
\boxed{
c_{BV}:=\frac\pi4-\frac1{1600}}
\tag{6.1}
```

for every candidate surplus below `3/5`.

Thus every post-ZF survivor limit with `lambda<3/5` must satisfy

```math
\boxed{
A(y,p)-c_{BV}\lambda^2
\le
\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{6.2}
```

and

```math
\boxed{
A(y,p)-c_{BV}\lambda^2
\le
\frac{2}{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{6.3}
```

These are the exact RD inequalities with a strictly smaller attachment-area
coefficient.  Hence the current `lambda_RD` endpoint is excluded quantitatively, not
only by ND compactness.

The next report should solve the perturbed optimizer and certify a decimal strictly
above `0.5981536184...`.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| Bonnesen annulus width bound | external theorem, exact hypothesis match | planar convex polygon |
| support-normal `2alpha` net | proved | inner/outer concentric disks + shared boundary vertices |
| force-hull radius bound | proved | selected supporting halfplanes |
| `1/1600` isodiametric coefficient loss | proved | exact rational evaluation at `d=3/5,x=1/20` |
| attachment-cell corollary | proved | C36/C44 + ZK total diameter budget |
| improved RD inequalities | proved for `lambda<3/5` | replace GU coefficient by BV coefficient |
| optimized new surplus constant | not yet claimed | next compact optimization |
| Level I | still open | high-surplus branch remains |

---

## 8. Next run

Repeat RX with `c_BV=pi/4-1/1600`.  The monotonic geometry is unchanged: the JC branch
still decreases before the FSDB/RSR crossover, the DD branch still increases, and the
same unique crossover `p_e(y)` controls the area currency.  Solve the new equality
pair and certify the resulting constant using the existing exact-Fraction framework.
