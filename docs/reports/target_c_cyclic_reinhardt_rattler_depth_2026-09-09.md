<!-- theorem-state: {"artifact_id":"ART-5CE9BA81D26D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact Reinhardt shell forces a uniform rattler boundary depth

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE/RC  
**Run type:** exact local geometry / source-population confinement  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** RE exact Reinhardt equality, RC Reuleaux completion, promoted C-I restoration `C=C_*`, C65 rattler isolation  
**External literature:** none used in the proof  
**Computation:** none; the displayed asymptotic expansion is algebraic

## LEVEL I STATUS

`STILL OPEN`

RE and RC put the complete C65 source inside one width-`D` Reuleaux completion `R`. Every vertex of the equilateral force hull lies on `partial R`, and consecutive force-hull vertices are unit distance apart.

The C65 rattlers are not merely interior to `R`. The prescribed unit-spaced shell forces them a fixed positive distance away from its boundary.

### Theorem RD — exact rattler depth

Put

\[
\delta_D:=\frac\pi q
=2\arcsin\frac1{2D}
\]

and define

\[
\boxed{
 s_D^2
:=4D^2\sin^2\frac{\delta_D}{4}
=\frac1{2\left(1+\sqrt{1-1/(4D^2)}\right)}.}
\tag{RD.1}
\]

Let `r_D` be the positive root of

\[
 t^2+s_D^2\left(1-\frac tD\right)=1.
\]

Equivalently,

\[
\boxed{
 r_D
=
\frac12\left[
\frac{s_D^2}{D}
+
\sqrt{\frac{s_D^4}{D^2}+4(1-s_D^2)}
\right].}
\tag{RD.2}
\]

Then every C65 contact-isolated source point `z` satisfies

\[
\boxed{
\operatorname{dist}(z,\partial R)>r_D.}
\tag{RD.3}
\]

Moreover

\[
\boxed{
 r_D
=
\frac{\sqrt3}{2}
+
\frac1{8D}
+
\frac1{128D^3}
+O(D^{-5}).}
\tag{RD.4}
\]

Thus all rattlers lie in the inner parallel body

\[
R_{-r_D}:=
\{x\in R:\operatorname{dist}(x,\partial R)\ge r_D\},
\]

whose diameter obeys

\[
\boxed{
\operatorname{diam}(R_{-r_D})
\le D-2r_D
=
D-\sqrt3-\frac1{4D}+O(D^{-3}).}
\tag{RD.5}
\]

In particular, the force-invisible population has a strictly smaller intrinsic diameter than the full source by an asymptotic additive gap `sqrt(3)`.

---

## 1. Unit-spaced sampling of every Reuleaux boundary arc

The Reinhardt equality classification used in RC supplies a width-`D` Reuleaux polygon `R` containing the force hull `F`, with every defining Reuleaux vertex among the vertices of `F` and every vertex of `F` on `partial R`.

The vertices of `F` occur in the same cyclic order on `partial R` as on the convex polygon `F`. Consecutive vertices `p_i,p_{i+1}` satisfy

\[
|p_i-p_{i+1}|=1.
\tag{1.1}
\]

Every defining Reuleaux vertex is itself one of these shell vertices. Therefore the boundary portion from one force-hull vertex to the next contains no Reuleaux corner in its relative interior. It lies on one radius-`D` circular arc.

For a radius-`D` circle, a unit chord subtends the minor central angle

\[
2\arcsin\frac1{2D}
=\delta_D.
\tag{1.2}
\]

Hence `partial R` is sampled by force-hull vertices so that every shell subarc between consecutive samples has central angle exactly `delta_D`.

---

## 2. Nearest-boundary geometry

Let `z` be a C65 rattler and set

\[
t:=\operatorname{dist}(z,\partial R).
\]

Choose a nearest boundary point `y`.

If `y` is a force-hull shell vertex, then

\[
|z-y|=t.
\]

Since `r_D<1` for the sufficiently large Target C regime, any `t\le r_D` would give a source separation `<1` or `=1`, impossible for a contact-isolated source point after C-I restoration.

It remains to consider `y` in the relative interior of one circular shell subarc between consecutive force-hull vertices `p_0,p_1`.

Let `c` be the center of the radius-`D` circle supporting that Reuleaux arc. Because `R` lies inside `B(c,D)`, the inward normal points from `y` toward `c`. At a nearest smooth boundary point, `z-y` is normal to the boundary, so

\[
|z-c|=D-t
\]

and `z,c,y` are collinear.

Let `phi` be the smaller central angle from the ray `cy` to one of the endpoint rays `cp_0,cp_1`. Since the total subarc angle is `delta_D`, one endpoint satisfies

\[
0\le\phi\le\frac{\delta_D}{2}.
\tag{2.1}
\]

For that endpoint `p`, the law of cosines gives

\[
\begin{aligned}
|z-p|^2
&=(D-t)^2+D^2-2D(D-t)\cos\phi\\
&=t^2+2D(D-t)(1-\cos\phi).
\end{aligned}
\tag{2.2}
\]

The right side increases with `phi` on the present range. Therefore by (2.1)

\[
|z-p|^2
\le
 t^2+2D(D-t)
\left(1-\cos\frac{\delta_D}{2}\right).
\tag{2.3}
\]

By definition of `s_D`,

\[
2D^2\left(1-\cos\frac{\delta_D}{2}\right)=s_D^2,
\]

so

\[
\boxed{
|z-p|^2
\le
 t^2+s_D^2\left(1-\frac tD\right).}
\tag{2.4}
\]

The worst point of a shell subarc is therefore its midpoint; no other boundary location can be farther from both adjacent shell samples at a fixed inward depth.

---

## 3. Solve the exclusion threshold

Define

\[
f_D(t)
:=t^2+s_D^2\left(1-\frac tD\right).
\]

Since `s_D^2<1`, the equation

\[
f_D(t)=1
\]

has one positive and one negative root. The positive root is exactly (RD.2).

For `0\le t<r_D`,

\[
f_D(t)<1.
\]

Equation (2.4) would then give

\[
|z-p|<1,
\]

contradicting unit separation.

If `t=r_D`, then (2.4) gives `|z-p|<=1`. Unit separation forces equality, which would make `z` incident to an actual unit contact with the shell vertex `p`. C-I restoration identifies the actual unit-contact graph with the positive contact graph in the contact-minimal source, while `z` is C65 contact-isolated. Contradiction again.

Therefore

\[
\boxed{t>r_D,}
\]

proving RD.3.

---

## 4. Closed form for the shell-midpoint chord radius

Since

\[
\sin\frac{\delta_D}{2}=\frac1{2D},
\]

we have

\[
\cos\frac{\delta_D}{2}
=
\sqrt{1-\frac1{4D^2}}.
\]

By the half-angle identity,

\[
\begin{aligned}
s_D^2
&=4D^2\sin^2\frac{\delta_D}{4}\\
&=2D^2\left(
1-\sqrt{1-\frac1{4D^2}}
\right)\\
&=
\frac1{2\left(1+\sqrt{1-1/(4D^2)}\right)}.
\end{aligned}
\]

This proves RD.1.

Expanding at large `D`,

\[
s_D^2
=\frac14+\frac1{64D^2}+\frac1{512D^4}+O(D^{-6}).
\]

Substitution into the exact quadratic root (RD.2) gives

\[
r_D
=
\frac{\sqrt3}{2}
+
\frac1{8D}
+
\frac1{128D^3}
+O(D^{-5}),
\]

which is RD.4.

---

## 5. Inner-parallel diameter loss

For any convex body `K`, the inner parallel body at depth `r` can be written as the erosion

\[
K_{-r}
=
\{x:x+rB_2\subseteq K\}.
\]

It is convex. Moreover

\[
K_{-r}+rB_2\subseteq K.
\tag{5.1}
\]

Take support functions in any unit direction `u`. Equation (5.1) gives

\[
h_{K_{-r}}(u)+r\le h_K(u)
\]

and the same inequality for `-u`. Hence

\[
w_{K_{-r}}(u)+2r\le w_K(u).
\tag{5.2}
\]

Our Reuleaux completion has constant width

\[
w_R(u)=D
\qquad\text{for every }u.
\]

Therefore

\[
w_{R_{-r_D}}(u)\le D-2r_D
\]

for every direction. A compact convex body's diameter is the maximum of its directional widths, so

\[
\operatorname{diam}(R_{-r_D})\le D-2r_D.
\]

This proves RD.5.

Equivalently, using the disk-intersection form from RC,

\[
R_{-r_D}
=
\bigcap_{c\in S}\overline B(c,D-r_D).
\tag{5.3}
\]

---

## 6. What the theorem does not yet prove

There are

\[
n-q=\Theta(D^2)
\]

rattlers in the C65 cyclic source, and RD now confines all of them to a unit-separated set of diameter at most

\[
D-\sqrt3+O(D^{-1}).
\]

This is substantial geometric compression, but generic Oler/isodiametric bounds on the inner parallel body still leave an `O(D)` population margin. Therefore RD alone is not a contradiction.

The missing theorem is now sharper:

> exploit the fact that the large unit-separated interior population lives in a **specific Reuleaux inner parallel** while the original shell contributes `q=pi D+O(D^{-1})` prescribed unit-spaced boundary points.

A second-order packing bound improving the generic perimeter correction by a fixed linear amount could close this exact cyclic branch.

---

## 7. Regression audit

### Regular odd shell

The shell itself has no rattlers, so RD is vacuous there. If extra isolated points are placed inside its Reuleaux completion, any one closer than `r_D` to a shell arc violates unit separation from an adjacent shell vertex exactly as proved above.

### Reuleaux corner

Every Reuleaux corner is a force-hull shell vertex. If it is a nearest boundary point, the direct distance `|z-y|=t` is stronger than the smooth-arc midpoint estimate.

### Shell vertex lying inside a smooth Reuleaux arc

The same direct argument applies whenever the nearest boundary point equals any force-hull vertex, not only a defining Reuleaux corner.

### Arc midpoint

This is the sharp local obstruction for the two adjacent shell samples: at fixed depth it maximizes the distance to the nearer endpoint and realizes the equality used to define `r_D`.

---

## 8. Next theorem

The exact `d_H=0` cyclic endpoint now has three nested scales:

1. full source diameter `D`;
2. unit-spaced Reinhardt force shell on `partial R` with `q=Theta(D)` points;
3. all `Theta(D^2)` C65 rattlers inside
   \[
   R_{-r_D},
   \qquad
   r_D=\sqrt3/2+o(1),
   \]
   whose diameter is at most `D-sqrt3+o(1)`.

The highest-value next target is a **sampled-boundary Oler improvement**: prove that a unit-separated set consisting of every unit-spaced Reinhardt boundary sample plus an interior set in `R_{-r_D}` has a linear correction strictly smaller than generic Oler allows.

That would convert RD's additive diameter compression into the first source-wide contradiction for the exact Reinhardt cyclic branch.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The proof is elementary once RE/RC and C-I restoration are accepted. No external theorem is introduced.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact RE shell:
  delta_D=pi/q=2asin(1/(2D)).
Every consecutive shell pair on partial R is a unit chord on one radius-D arc.

Let z be a C65 rattler and t=dist(z,partial R). If the nearest boundary point is
inside a shell subarc, one endpoint p has central offset phi<=delta_D/2. With z on
the inward radial normal,
  |z-p|^2 <= t^2+s_D^2(1-t/D),
where
  s_D^2=4D^2 sin^2(delta_D/4)
       =1/[2(1+sqrt(1-1/(4D^2)))].
Let r_D be the positive root of
  t^2+s_D^2(1-t/D)=1.
Then unit separation plus actual contact-isolation force
  dist(z,partial R)>r_D.
Exactly
  r_D=1/2[s_D^2/D+sqrt(s_D^4/D^2+4(1-s_D^2))],
and
  r_D=sqrt3/2+1/(8D)+1/(128D^3)+O(D^-5).

Hence all rattlers lie in R_-r_D. Since R has constant width D,
  diam(R_-r_D)<=D-2r_D
    =D-sqrt3-1/(4D)+O(D^-3).

Next: sampled-boundary Oler improvement using q~pi D prescribed shell points plus
the compressed interior population.
```
