> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_vertex_isodiametric_penalty_2026-09-09.md) · source SHA-256 `3f112fe2d3c8272f87d9ca22d4278ad7c35ad94082f0453cf5dce47f34fd403b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7C6A3DF7044C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — BVP: boundary-vertex nesting costs a fixed isodiametric area gap

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** finite convex-geometry stability theorem  
**Target:** quantitative ESN / attachment-cell area bound  
**Depends on:** C26/C42 only for the later Target C application; planar perimeter-diameter inequality; Bonnesen concentric-annulus inequality  
**External source:** Nicola Fusco, *The quantitative isoperimetric inequality and related topics*, Bulletin of Mathematical Sciences 5 (2015), 517–607, Theorem 1.1, DOI `10.1007/s13373-015-0074-x` (stating Bonnesen's 1924 concentric-circle inequality)  
**Computation:** none; all numerical comparisons below use terminating decimals and `pi>3`

## LEVEL I STATUS

**STILL OPEN.**

ESN proves qualitatively that an attachment polygon cannot approach its isodiametric disk while all of its vertices remain vertices of a larger diameter-one force hull. BVP makes that obstruction finite and explicit in the range relevant to ENS.

### Theorem BVP — explicit boundary-vertex isodiametric penalty

Let `P subset K` be planar compact convex sets such that

1. `P` is a convex polygon;
2. every vertex of `P` is an extreme point of `K`;
3. `diam(K)=1`;
4. with
   $$
   r:=\operatorname{diam}(P),
   $$
   one has
   $$
   \frac{12}{25}=0.48\le r\le\frac12.
   $$

Then

$$
\boxed{
\operatorname{area}(P)
<
\frac\pi4r^2-\frac1{2500}.
}
\tag{BVP.1}
$$

Thus a nested attachment polygon in this diameter range loses at least

$$
\boxed{0.0004}
$$

of normalized area from the ordinary isodiametric disk bound.

The constant is deliberately conservative. The point is that it is explicit and already large enough to move the Target C scalar frontier visibly.

---

## 1. Bonnesen turns small isodiametric deficit into a thin concentric annulus

Put

$$
A:=\operatorname{area}(P),
\qquad
\Delta:=\frac\pi4r^2-A\ge0.
\tag{1.1}
$$

Assume for contradiction

$$
\Delta\le\frac1{2500}.
\tag{1.2}
$$

Bonnesen's theorem gives a center `c` and concentric closed disks

$$
B(c,a)\subseteq P\subseteq B(c,b)
\tag{1.3}
$$

such that

$$
(b-a)^2
\le
\frac{\operatorname{per}(P)^2-4\pi A}{4\pi}.
\tag{1.4}
$$

The planar perimeter-diameter inequality gives

$$
\operatorname{per}(P)\le\pi r.
$$

Therefore

$$
\frac{\operatorname{per}(P)^2-4\pi A}{4\pi}
\le
\frac{\pi^2r^2-4\pi A}{4\pi}
=\Delta.
$$

So, writing

$$
w:=b-a,
$$

we obtain

$$
\boxed{w\le\sqrt\Delta\le\frac1{50}=0.02.}
\tag{BVP.2}
$$

Because `P` contains the radius-`a` disk and has diameter `r`,

$$
a\le\frac r2.
\tag{1.5}
$$

Hence

$$
\boxed{b\le\frac r2+\frac1{50}.}
\tag{BVP.3}
$$

On the other hand `P subset B(c,b)` gives

$$
A\le\pi b^2.
$$

Using (1.1)--(1.2),

$$
b^2
\ge
\frac{A}{\pi}
=\frac{r^2}{4}-\frac{\Delta}{\pi}
\ge
\frac{r^2}{4}-\frac{1}{2500\pi}.
$$

Since `pi>3`,

$$
\boxed{
b>
\sqrt{\frac{r^2}{4}-\frac1{7500}}.}
\tag{BVP.4}
$$

Combining with `a=b-w` and BVP.2,

$$
\boxed{
a>
\sqrt{\frac{r^2}{4}-\frac1{7500}}
-\frac1{50}.}
\tag{BVP.5}
$$

---

## 2. A diameter-one container supplies an exterior point

Choose diameter endpoints `x,y in K` with

$$
|x-y|=1.
$$

For any point `c`, the triangle inequality gives

$$
1=|x-y|\le|x-c|+|y-c|,
$$

so one endpoint, call it `z`, satisfies

$$
\boxed{d:=|z-c|\ge\frac12.}
\tag{BVP.6}
$$

BVP.3 and `r<=1/2` give

$$
b\le\frac14+\frac1{50}=0.27<\frac12\le d.
$$

Thus `z notin P`.

Let

$$
Q:=\operatorname{conv}(P\cup\{z\})\subseteq K.
\tag{2.1}
$$

Every vertex of `P` is extreme in `K`, hence remains extreme in `Q`: if a vertex of `P` were a convex combination of other points of `Q`, the same combination would witness that it is not extreme in `K`.

---

## 3. Preserving every old vertex forces one visible edge

For a point outside a convex polygon, the boundary of `conv(P union {z})` consists of

- two tangent segments from `z` to two vertices `u,v` of `P`; and
- the non-visible boundary chain of `P` joining `u` to `v`.

Every vertex strictly inside the complementary visible chain ceases to be a vertex after adjoining `z`.

Here no vertex of `P` may disappear. Therefore the visible chain contains no intermediate polygon vertex. Its tangent endpoints `u,v` are adjacent vertices of `P`, and

$$
\boxed{uv\text{ is one edge of }P.}
\tag{BVP.7}
$$

The segments `zu,zv` are supporting edges of `Q`. Hence the cone at `z` bounded by the rays `zu,zv` contains all of `P`, and therefore contains the inner disk `B(c,a)`.

Let

$$
\gamma:=\angle uzv.
$$

The smallest cone with apex at distance `d` from the center of a radius-`a` disk and containing that disk is bounded by its two tangent rays. Thus

$$
\boxed{
\gamma\ge2\arcsin\frac ad.
}
\tag{BVP.8}
$$

---

## 4. The visible edge is simultaneously too long and too short

Because `u,v in P subset B(c,b)`,

$$
|z-u|\ge d-b,
\qquad
|z-v|\ge d-b.
\tag{4.1}
$$

For two rays separated by angle `gamma`, the distance between points whose radial distances from the apex are both at least `ell` is minimized when both radial distances equal `ell`. Therefore

$$
|u-v|
\ge
2(d-b)\sin\frac\gamma2.
$$

Use BVP.8:

$$
\boxed{
|u-v|
\ge
2(d-b)\frac ad.
}
\tag{BVP.9}
$$

Since `d>=1/2`,

$$
\frac{d-b}{d}=1-\frac bd\ge1-2b,
$$

so

$$
\boxed{|u-v|\ge2a(1-2b).}
\tag{BVP.10}
$$

On the other hand `uv` is a supporting edge of `P`. Since `B(c,a) subset P`, the supporting line through `uv` has distance at least `a` from `c`. Since `u,v` lie in the radius-`b` disk,

$$
\boxed{|u-v|\le2\sqrt{b^2-a^2}.}
\tag{BVP.11}
$$

Combining BVP.10-BVP.11 gives the necessary inequality

$$
\boxed{
a(1-2b)\le\sqrt{b^2-a^2}.}
\tag{BVP.12}
$$

But BVP.2 gives

$$
b^2-a^2
=(b-a)(b+a)
\le\frac1{50}(2b).
\tag{BVP.13}
$$

The remaining contradiction is a three-interval rational check.

---

## 5. Exact decimal certificate on `0.48<=r<=0.50`

All decimal numbers below terminate and therefore denote exact rationals.

### Interval I: `0.48<=r<=0.49`

From BVP.5 and `pi>3`,

$$
a>
\sqrt{0.24^2-1/7500}-0.02.
$$

Now

$$
0.24^2-1/7500
=0.057466\ldots
>0.2397^2,
$$

so

$$
a>0.2197.
$$

BVP.3 gives

$$
b\le0.49/2+0.02=0.265,
$$

hence

$$
a(1-2b)>0.2197(0.47)=0.103259.
\tag{5.1}
$$

But BVP.13 gives

$$
b^2-a^2\le0.04(0.265)=0.0106<0.103^2,
$$

so

$$
\sqrt{b^2-a^2}<0.103,
$$

contradicting BVP.12.

### Interval II: `0.49<=r<=0.495`

Similarly

$$
0.245^2-1/7500
>0.2447^2,
$$

so

$$
a>0.2247.
$$

Also

$$
b\le0.495/2+0.02=0.2675.
$$

Thus

$$
a(1-2b)>0.2247(0.465)=0.1044855.
\tag{5.2}
$$

While

$$
b^2-a^2\le0.04(0.2675)=0.0107<0.1035^2,
$$

so the right side of BVP.12 is below `0.1035`. Contradiction.

### Interval III: `0.495<=r<=0.50`

Here

$$
0.2475^2-1/7500
>0.2472^2,
$$

so

$$
a>0.2272.
$$

Also

$$
b\le0.25+0.02=0.27.
$$

Hence

$$
a(1-2b)>0.2272(0.46)=0.104512.
\tag{5.3}
$$

But

$$
b^2-a^2\le0.04(0.27)=0.0108<0.104^2,
$$

so the right side of BVP.12 is below `0.104`. Contradiction.

The three intervals cover the entire required range. Therefore assumption (1.2) is impossible, proving BVP.1.

---

## 6. Target C attachment-cell application

For every unloaded component `I_r`, C49 gives the attachment polygon

$$
P_r:=\operatorname{conv}(A_r)\subseteq F.
$$

C26/C42 give

$$
B_+=\operatorname{Vert}(F).
$$

Since every attachment belongs to `B_+`, every vertex of `P_r` is a vertex of `F`: if an attachment point were nonextreme in `P_r`, it would be a convex combination of other attachment points and therefore could not be extreme in `F`.

After scaling by `D`, `K=F/D` has diameter one. Thus every attachment cell whose normalized diameter lies in `[0.48,0.50]` satisfies

$$
\boxed{
\frac{\operatorname{area}(P_r)}{D^2}
\le
\frac\pi4
\left(\frac{\operatorname{diam}(P_r)}D\right)^2
-\frac1{2500}.
}
\tag{BVP.14}
$$

This is a fixed quadratic penalty, unlike the previous qualitative ESN compactness argument.

---

## 7. Regression audit

- The vertex-preservation assumption is essential. A small disk can lie inside a larger disk with no area penalty if its boundary points need not remain extreme in the larger body.
- BVP does not assume `K` is a polygon.
- Only `P` must be polygonal, which holds for finite attachment sets.
- The proof uses no smoothness of `P`; Bonnesen applies to convex bodies/curves.
- The visible-chain argument uses only extremality, not Target C topology.
- The constant `1/2500` is not optimized.
- The theorem is scale-normalized to `diam K=1`; at scale `D` the area penalty is `D^2/2500`.

## 8. Next target

Insert BVP.14 into the ZK/GU attachment-area estimate. In the ENS slope window `lambda in[0.48072358,0.49)`, either

1. some attachment cell has diameter at least `0.48D`, and BVP directly subtracts `D^2/2500`; or
2. all cells have diameter below `0.48D`, in which case the convex square-sum bound loses more than `D^2/2500` because the total component-diameter budget is already at least `0.48072358D`.

Therefore the entire attachment-cell capacity should improve from

$$
\frac\pi4\lambda^2D^2
$$

to

$$
\left(\frac\pi4\lambda^2-\frac1{2500}\right)D^2+o(D^2)
$$

throughout the relevant scalar window. Feeding that into ENS/JC should raise the explicit pinned/contact floor by about `3.7e-4`, orders of magnitude larger than the earlier four-point stability increment.

## 9. Compact handoff

```text
BVP finite theorem.
Let P subset K, P a convex polygon, every Vert(P) extreme in K,
diam K=1, and r=diam P in [0.48,0.50]. Then
    area(P) < pi r^2/4 - 1/2500.

Proof:
Bonnesen gives concentric disks B_a subset P subset B_b with
    (b-a)^2 <= (per(P)^2-4pi A)/(4pi)
              <= pi r^2/4-A = Delta.
If Delta<=1/2500, annulus width w<=0.02.
A diameter endpoint z of K satisfies d=|z-c|>=1/2.
All P vertices must remain extreme after adding z, so z sees exactly one P edge uv.
The supporting rays zu,zv must contain B_a:
    angle uzv >=2 asin(a/d).
Hence
    |uv| >=2(d-b)a/d >=2a(1-2b).
But uv is a support edge of P inside B_b, so
    |uv| <=2 sqrt(b^2-a^2).
Thus a(1-2b)<=sqrt(b^2-a^2).
Using w<=0.02, the three rational intervals
    [0.48,0.49], [0.49,0.495], [0.495,0.50]
contradict this inequality directly.

Target C: every attachment polygon has all vertices in Vert(F), so BVP applies
after scaling by D.
```