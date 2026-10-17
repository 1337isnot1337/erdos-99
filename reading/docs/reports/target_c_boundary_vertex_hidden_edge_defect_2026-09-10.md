> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_vertex_hidden_edge_defect_2026-09-10.md) · source SHA-256 `b01f4e6cd3f1643242959bf31abcb3c575374261055d622a1bf0e5ae6f4c8dc6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DDA2C161AB0A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — a hidden boundary edge strengthens the attachment-cell isodiametric defect

**Date:** 2026-09-10  
**Branch base:** `5a459584b3b36579e9c03fab28e75f4c9c131437` plus BVE/BF on this branch  
**Depends on:** BV/BVE; C36 attachment vertices lie on the force-hull boundary  
**External input:** only the Bonnesen concentric-annulus theorem already imported in BV  
**Run type:** quantitative convex geometry / boundary-sharing stability  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

BVE uses the fact that every vertex of a harmonic attachment polygon lies on the
boundary of the larger force hull.  Its support-normal argument already gives a
positive isodiametric defect.  There is additional strictness that BVE does not spend:
if the force hull contains a point outside the Bonnesen annulus of the attachment
polygon, the convex hull with that point hides a whole attachment-boundary arc.  Since
every attachment-polygon vertex must remain on the force-hull boundary, the hidden arc
must lie in one polygon edge.  That creates a quantitative perimeter deficit, which
feeds back through Bonnesen.

### Theorem HE — hidden-edge boundary-sharing defect

Let `F` be a compact convex planar set of diameter `D>0`, and let `K subset F` be a
nondegenerate convex polygon satisfying

```math
V(K)\subseteq\partial F.
\tag{HE.1}
```

If

```math
\operatorname{diam}K\le\frac35D,
\tag{HE.2}
```

then

```math
\boxed{
\operatorname{area}K
\le
\left(\frac\pi4-\frac3{4000}\right)
\operatorname{diam}(K)^2.
}
\tag{HE.3}
```

This improves BV's coefficient loss from `1/1600=0.000625` to
`3/4000=0.00075`.

Consequently, for every post-ZF survivor sequence with

```math
\lambda:=\limsup\frac{e_{BB}+2s_C}{D}<\frac35,
```

```math
\boxed{
\limsup\frac1{D^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\left(\frac\pi4-\frac3{4000}\right)\lambda^2.
}
\tag{HE.4}
```

---

## 1. Normalize and choose the Bonnesen annulus

Scale so

```math
\operatorname{diam}F=1.
```

Put

```math
d:=\operatorname{diam}K\le3/5,
\qquad
A:=\operatorname{area}K,
\qquad
P:=\operatorname{per}K.
```

Bonnesen gives concentric disks

```math
\overline B(c,r_1)\subseteq K\subseteq\overline B(c,r_2)
\tag{1.1}
```

such that

```math
(r_2-r_1)^2
\le\frac{P^2-4\pi A}{4\pi}.
\tag{1.2}
```

As in BV/BVE, put

```math
w:=r_2-r_1,
\qquad
x:=\frac{2w}{d}.
\tag{1.3}
```

Since `2r_1<=d<=2r_2`,

```math
\boxed{
\overline B(c,\rho)\subseteq K\subseteq\overline B(c,R),
}
\tag{1.4}
```

where

```math
\rho=\frac d2(1-x),
\qquad
R=\frac d2(1+x).
\tag{1.5}
```

The perimeter-diameter inequality `P<=pi d` inserted into (1.2) gives

```math
\boxed{
A\le\frac{\pi-x^2}{4}d^2.
}
\tag{1.6}
```

Therefore if

```math
x\ge\frac{11}{200},
\tag{1.7}
```

then

```math
\frac{A}{d^2}
\le\frac\pi4-\frac{121}{160000}
<\frac\pi4-\frac3{4000},
```

and HE.3 is proved.

It remains to treat

```math
\boxed{x<11/200.}
\tag{1.8}
```

---

## 2. The force-hull diameter gives a lower annulus-width bound

Under (1.8), `x<3-2sqrt(2)`, so BVE's support-normal argument applies and gives

```math
1
\le
 d\frac{(1+x)^3}{1-6x+x^2}.
\tag{2.1}
```

Since `d<=3/5`,

```math
\frac35(1+x)^3
\ge1-6x+x^2.
\tag{2.2}
```

The left minus right side is strictly increasing in `x`.  At

```math
x=\frac{51}{1000},
```

one has the exact strict inequality

```math
1-6x+x^2-\frac35(1+x)^3
=\frac{198047}{5000000000}>0.
\tag{2.3}
```

Hence

```math
\boxed{x>51/1000.}
\tag{2.4}
```

This recovers, with room, the BVE annulus thickness in the whole `d<=3/5` regime.

---

## 3. An exterior force-hull point hides one macroscopic polygon edge

Because `diam(F)=1`, for every point `c` there is a point `y in F` with

```math
L:=|y-c|\ge1/2.
\tag{3.1}
```

Under (1.8) and `d<=3/5`,

```math
R
=\frac d2(1+x)
<\frac3{10}\frac{211}{200}
=\frac{633}{2000}
<\frac12.
\tag{3.2}
```

Thus `y` lies strictly outside `K`.

Draw the two support lines from `y` tangent to `K`, and let their contact points be
`u,v`.  Since `K` contains the disk `B(c,rho)`, the angle `theta` between the two
support rays satisfies

```math
\theta\ge2\arcsin(\rho/L).
\tag{3.3}
```

Both contact points lie in `B(c,R)`, so

```math
|y-u|,|y-v|\ge L-R.
\tag{3.4}
```

For two points on rays separated by angle `theta`, each at radial distance at least
`L-R`,

```math
|u-v|^2
\ge4(L-R)^2\sin^2(\theta/2).
```

Using (3.3),

```math
|u-v|
\ge2(L-R)\frac\rho L
=2\rho\left(1-\frac RL\right)
\ge2\rho(1-2R).
\tag{3.5}
```

Now consider `conv(K union {y}) subseteq F`.  The open boundary arc of `K` between
the two tangent contacts on the side facing `y` is strictly inside this convex hull.
Therefore it contains no vertex of `K`: every vertex of `K` belongs to `partial F` by
HE.1 and hence cannot be an interior point of the smaller full-dimensional convex set
`conv(K union {y})` contained in `F`.

Since `K` is a polygon, a boundary arc containing no polygon vertex lies in one edge.
Thus one edge of `K` has length `ell` satisfying

```math
\ell\ge|u-v|.
```

Using (1.5),

```math
\boxed{
\frac\ell d
\ge
(1-x)\bigl(1-d(1+x)\bigr).
}
\tag{3.6}
```

The right side decreases in both `d` and `x` on the present range.  With
`d<=3/5` and `x<11/200`,

```math
\frac\ell d
>
\frac{189}{200}\frac{367}{1000}
=
\boxed{\frac{69363}{200000}}.
\tag{3.7}
```

Thus the boundary-sharing condition forces one edge longer than `0.346815 d`.

---

## 4. One long edge forces a perimeter deficit

We need a standalone convex lemma.

### Lemma HE.1 — edge/perimeter deficit

If a planar convex body has diameter `d`, perimeter `P`, and a boundary line segment of
length `ell`, then

```math
\boxed{
\pi d-P
\ge
 d\left(1-\sqrt{1-\frac{\ell^2}{4d^2}}\right)^2.
}
\tag{4.1}
```

### Proof

Take the segment's outward normal direction.  Let `w_0` be the width in that direction.
Choose a point on the opposite support line.  Its distances to both segment endpoints
are at most `d`, while at least one tangential displacement from the two endpoints is
at least `ell/2`.  Therefore

```math
w_0^2+\frac{\ell^2}{4}\le d^2,
```

so

```math
d-w_0
\ge
 d\left(1-\sqrt{1-\frac{\ell^2}{4d^2}}\right)
=:d\eta.
\tag{4.2}
```

The width function is the support function of `K-K`.  Since every vector in `K-K`
has norm at most `d`, the width function is `d`-Lipschitz in angular distance.
Consequently the nonnegative width deficit `d-w(theta)` lies above the triangular
profile

```math
d\max\{\eta-|\theta-\theta_0|,0\}
```

on the projective direction circle.  Cauchy's perimeter formula gives

```math
\pi d-P
=
\int_0^\pi(d-w(\theta))\,d\theta
\ge d\eta^2.
```

This is (4.1). `square`

Put

```math
s:=\pi-P/d.
\tag{4.3}
```

By (3.7) and Lemma HE.1,

```math
s
\ge
\left(1-\sqrt{1-r^2/4}\right)^2,
\qquad
r:=\frac{69363}{200000}.
\tag{4.4}
```

Since `1-sqrt(1-t)>=t/2` for `0<=t<=1`,

```math
\boxed{
s\ge s_0:=\frac{r^4}{64}.}
\tag{4.5}
```

Numerically `s_0=0.0002260536464...`, but only the exact rational value is used.

---

## 5. Perimeter deficit feeds back through Bonnesen

Rewrite Bonnesen (1.2) in normalized form.  Since

```math
P/d=\pi-s,
```

(1.2)--(1.3) give

```math
x^2
\le
\frac{(\pi-s)^2}{\pi}-\frac{4A}{d^2}.
```

Thus

```math
\boxed{
\frac A{d^2}
\le
\frac\pi4
-\frac{x^2}{4}
-\frac s2
+\frac{s^2}{4\pi}.
}
\tag{5.1}
```

On the current case, (2.4) gives

```math
\frac{x^2}{4}
>
\frac1{4}\left(\frac{51}{1000}\right)^2.
\tag{5.2}
```

Also `0<=s<=pi`, so the function

```math
s\mapsto\frac s2-\frac{s^2}{4\pi}
```

is increasing.  By (4.5) and `pi>3`,

```math
\frac s2-\frac{s^2}{4\pi}
\ge
\frac{s_0}{2}-\frac{s_0^2}{4\pi}
>
\frac{s_0}{2}-\frac{s_0^2}{12}.
\tag{5.3}
```

Exact rational arithmetic gives

```math
\frac14\left(\frac{51}{1000}\right)^2
+
\frac{s_0}{2}-\frac{s_0^2}{12}
-
\frac3{4000}
>0.
\tag{5.4}
```

The margin is approximately `1.3272e-5`; a companion verifier can check the displayed
rational inequality with no transcendental input.

Combining (5.1)--(5.4),

```math
\frac A{d^2}
<\frac\pi4-\frac3{4000}.
```

Together with the easy case (1.7), this proves HE.3.

---

## 6. Target C attachment-cell corollary

Let

```math
K_r=\operatorname{conv}A_r.
```

C36 gives

```math
V(K_r)\subseteq A_r\subseteq\partial F,
```

and C44 gives

```math
\operatorname{diam}K_r\le\delta_r+2.
```

If

```math
\lambda
=\limsup\frac{e_{BB}+2s_C}{D}<3/5,
```

then ZK gives

```math
\sum_r\delta_r\le6+e_{BB}+2s_C,
```

so all cells satisfy `diam(K_r)<3D/5` for sufficiently large `D`.  Apply HE.3
cellwise and sum:

```math
\sum_r\operatorname{area}K_r
\le
\left(\frac\pi4-\frac3{4000}\right)
\sum_r(\delta_r+2)^2.
```

As before, `c_I=O(D)` and `sum delta_r=O(D)`, so

```math
\sum_r(\delta_r+2)^2
\le
\left(\sum_r\delta_r\right)^2+O(D).
```

Divide by `D^2` to obtain HE.4.

---

## 7. Consequence for the active RSR/DD frontier

Throughout the current generic frontier, `lambda<3/5`.  Therefore the attachment
coefficient in the JC and DD inequalities can be replaced by

```math
\boxed{
c_{HE}:=\frac\pi4-\frac3{4000}.}
\tag{7.1}
```

This strictly dominates both

- the original GU coefficient `pi/4`, and
- the exact BVE feedback coefficient at the present optimizer, whose loss is only
  `kappa(lambda)^2/4 approx 0.0006566`.

The RX/BRD optimizer proof applies unchanged with `c_HE`, because the new coefficient
is constant in `(y,p)` and the same FSDB/RSR crossover remains active.

High-precision reconnaissance gives the new variational state

```math
y\approx1.5245283152144574,
\qquad
p\approx3.0231381569965496,
```

```math
\lambda\approx0.5983667958145539.
```

These decimals are not claimed as a theorem in this geometric report.  The next
commit should solve the optimizer exactly and add a rational certificate.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| exterior force-hull point exists outside Bonnesen annulus | proved | circumradius from arbitrary center is at least `D/2`, while `R<0.317D` |
| tangent cone angle lower bound | proved | cone contains inner Bonnesen disk |
| hidden arc contains no attachment-polygon vertex | proved | it is interior to `conv(K union {y}) subset F` |
| one edge has `ell/d>69363/200000` | proved | tangent-ray geometry and rational annulus bounds |
| edge/perimeter deficit Lemma HE.1 | proved | opposite support width + Lipschitz width function + Cauchy formula |
| hidden-edge coefficient `3/4000` | proved | Bonnesen plus exact rational case split |
| Target C attachment capacity HE.4 | proved asymptotically | C36/C44/ZK plus HE.3 |
| new optimized surplus constant | not claimed here | next report |
| Level I | still open | high-surplus survivors remain possible |

---

## 9. Next run

Insert `c_HE=pi/4-3/4000` into the exact RX optimizer and certify a clean generic
surplus bound above the current `0.59834`.  Because the coefficient improvement is
uniform on the whole `lambda<3/5` region, no feedback fixed point is needed for this
step.
