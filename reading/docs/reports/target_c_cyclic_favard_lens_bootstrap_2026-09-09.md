> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_favard_lens_bootstrap_2026-09-09.md) · source SHA-256 `571fac9ecb0fb1530caf13f26af349b3b76dd16970fa852aa0256dda4743c835`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B1D362799280","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: Favard lens bootstrap

**Date:** 2026-09-09  
**Repository base:** PR #118, reconciled against main `6ed9d78ae146b68fd9b14c3c3486b048f3d59074`  
**Run type:** sharp convex-geometry bootstrap  
**Target:** Target C cyclic primitive endpoint  
**Depends on:** CY cyclic shell `per(F)=q`, `h=q-d_H` with `d_H<=2`; main-branch DA difference-body area theorem; Favard's planar diameter theorem  
**External source:** Stefano Campi, *Three-dimensional Bonnesen type inequalities*, Section 2, Theorem 2.2, recalling Favard (1929): among plane convex bodies with perimeter at most `L_0` and area at least `A_0`, the symmetric lens uniquely maximizes diameter. Campi also notes the diameter form directly.  
**Computation:** only evaluation of the final one-variable root; no computation is used in the proof

## LEVEL I STATUS

`STILL OPEN`

The cyclic primitive endpoint has a special perimeter identity unavailable in the generic post-ZF branch:

$$
\operatorname{per}(F)=q,
\qquad
h=q-d_H,
\qquad
0\le d_H\le2.
$$

Main now contains the difference-body lower bound DA. Along a subsequence with

$$
\frac hD\to y,
$$

DA gives

$$
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac{y+\sin y}{6}+o(1).
$$

The ordinary isoperimetric upper bound already bootstraps this to `y>=2.55131...`. Favard's sharp perimeter-area-diameter theorem gives a strictly stronger upper envelope and raises the cyclic threshold to

$$
\boxed{
\liminf\frac hD
=\liminf\frac qD
\ge
 y_F
=2.6189005339279606\ldots .}
\tag{FL.1}

Consequently

\[
\boxed{
\liminf
\frac{\operatorname{area}(F)}{D^2}
\ge
A_F^*
=0.5196858569093050\ldots .}
\tag{FL.2}

This is stronger inside the cyclic endpoint than the new universal PI floor `0.4978566363...D^2` on current main.

---

## 1. Symmetric-lens parameterization

Let a symmetric lens be the intersection of two equal-radius disks. Write `R` for their common radius and let `theta in (0,pi/2]` be the half central angle subtended by the two intersection points on either circle.

The lens boundary consists of two congruent circular arcs. Its perimeter, diameter, and area are

\[
P=4R\theta,
\tag{1.1}
$$

$$
D=2R\sin\theta,
\tag{1.2}
$$

and

$$
A=R^2(2\theta-\sin2\theta).
\tag{1.3}
$$

Therefore, with

$$
y:=\frac PD,
$$

one has

$$
\boxed{
y=Y(\theta):=\frac{2\theta}{\sin\theta}.}
\tag{1.4}

The normalized lens area is

\[
\boxed{
L(y)
:=\frac A{D^2}
=
\frac{\theta-\sin\theta\cos\theta}
{2\sin^2\theta},
\qquad
Y(\theta)=y.}
\tag{1.5}

The map `Y` is strictly increasing because

\[
Y'(\theta)
=
\frac{2(\sin\theta-\theta\cos\theta)}{\sin^2\theta}>0
$$

for `0<theta<=pi/2`. It maps `(0,pi/2]` onto `(2,pi]`.

---

## 2. Favard inverts to a sharp area upper bound at fixed perimeter and diameter

Campi's statement of Favard's theorem is:

> Fix `P_0,A_0`. Among all planar convex bodies with perimeter at most `P_0` and area at least `A_0`, the symmetric lens of perimeter `P_0` and area `A_0` uniquely maximizes diameter.

Let `K` be any planar convex body with perimeter `P`, area `A`, and diameter `D`. Let the Favard lens with the same `P,A` have parameter `eta`. Favard gives

$$
D\le D_{lens}(P,A).
\tag{2.1}

For a symmetric lens of fixed perimeter `P`, its normalized area relative to `P^2` is

\[
a_P(\theta)
:=
\frac A{P^2}
=
\frac{2\theta-\sin2\theta}{16\theta^2}.
\tag{2.2}

Its derivative is

\[
a_P'(\theta)
=
\frac{2\cos\theta(\sin\theta-\theta\cos\theta)}{8\theta^3}>0
$$

for `0<theta<pi/2`. Thus lens area increases strictly with `theta` at fixed perimeter, while its diameter

$$
D_{lens}=P\frac{\sin\theta}{2\theta}
$$

decreases strictly.

Let `theta` be defined from the actual ratio `y=P/D` by `Y(theta)=y`. Inequality (2.1) gives

$$
\frac PD
\ge
\frac{P}{D_{lens}(P,A)}
=Y(\eta).
$$

Since `Y` is increasing,

$$
\eta\le\theta.
$$

Since `a_P` is increasing,

$$
\frac A{P^2}
=a_P(\eta)
\le a_P(\theta).
$$

Multiplying by `P^2/D^2=y^2` gives:

### Theorem FL.1 — Favard area envelope

Every planar convex body with perimeter `P`, diameter `D`, and `2<=P/D<=pi` satisfies

$$
\boxed{
\frac A{D^2}
\le
L(P/D),}
\tag{FL.3}

where `L` is the symmetric-lens function (1.5).

Equality holds only for the corresponding symmetric lens.

---

## 3. A useful derivative identity

Differentiate `L(theta)` and `Y(theta)`. A direct cancellation gives

\[
\boxed{
\frac{dL}{dy}
=
\frac1{2\sin\theta},
\qquad Y(\theta)=y.}
\tag{FL.4}

Hence on `2<y<pi`,

\[
\boxed{L'(y)>\frac12.}
\tag{FL.5}

By contrast, the asymptotic DA lower envelope

\[
A_{DB}(y):=\frac{y+\sin y}{6}
$$

has derivative

$$
A_{DB}'(y)=\frac{1+\cos y}{6}
\le\frac13.
\tag{FL.6}

Therefore

\[
\boxed{
F(y):=L(y)-A_{DB}(y)
\text{ is strictly increasing on }(2,\pi).}
\tag{FL.7}

At `y->2+`, `L(y)->0` while `A_DB(y)->(2+sin2)/6>0`, so `F<0`. At `y=pi`,

\[
L(\pi)=\frac\pi4,
\qquad
A_{DB}(\pi)=\frac\pi6,
$$

so `F>0`. Thus there is exactly one root

$$
\boxed{y_F\in(2,\pi)}
\tag{FL.8}

of

\[
\boxed{
L(y_F)=\frac{y_F+\sin y_F}{6}.}
\tag{FL.9}

Numerically,

\[
\boxed{
y_F=2.6189005339279606\ldots .}
\tag{FL.10}

The associated lens parameter is

\[
\theta_F=1.2373074829148963\ldots .
$$

---

## 4. Apply the two envelopes to the cyclic endpoint

Consider any unbounded sequence of cyclic primitive survivors. Put

$$
y_j:=\frac{h_j}{D_j}.
$$

The diameter-thrackle bound and convex perimeter bound make `y_j` bounded. Pass to a subsequence realizing its lower limit and then to a convergent subsubsequence

$$
y_j\to y.
$$

In the cyclic endpoint

$$
q_j-h_j=d_H\le2,
$$

so

$$
\frac{q_j}{D_j}\to y.
\tag{4.1}

Because every force-hull side is a unit contact,

\[
P_j=\operatorname{per}(F_j)=q_j.
\tag{4.2}

The main-branch DA theorem gives

\[
\liminf
\frac{\operatorname{area}(F_j)}{D_j^2}
\ge
A_{DB}(y)
=
\frac{y+\sin y}{6}.
\tag{4.3}

Favard FL.3 gives on the same sequence

\[
\limsup
\frac{\operatorname{area}(F_j)}{D_j^2}
\le
L(y).
\tag{4.4}

Therefore necessarily

\[
A_{DB}(y)\le L(y).
\tag{4.5}

By the strict crossing result FL.7-FL.9,

\[
y\ge y_F.
$$

Since the subsequence realized the global lower limit, this proves FL.1.

Finally `A_DB` is nondecreasing on `[0,pi]`, so (4.3) and `y>=y_F` give

$$
\liminf
\frac{\operatorname{area}(F)}{D^2}
\ge
A_{DB}(y_F).
$$

Numerically,

$$
\boxed{
A_{DB}(y_F)
=L(y_F)
=0.5196858569093050\ldots ,}
$$

proving FL.2. `square`

---

## 5. Comparison with the simpler isoperimetric bootstrap

Ordinary isoperimetry gives

$$
\frac A{D^2}
\le
\frac1{4\pi}\left(\frac PD\right)^2.
$$

Combined with DA, this forces the weaker root of

$$
y^2
=\frac{2\pi}{3}(y+\sin y),
$$

namely

$$
y=2.5513100241\ldots .
$$

Favard raises the threshold by about

$$
0.06759
$$

because a disk cannot simultaneously have perimeter ratio `y<pi` and diameter `D`; the symmetric lens is the correct sharp area envelope in the intermediate perimeter/diameter regime.

---

## 6. Interaction with PI

Current main also proves the projective-circle area floor PI. Since FL.1 gives

$$
y_F>\pi/2,
$$

the PI spread saturates asymptotically near a right angle in the cyclic endpoint and yields

$$
\operatorname{area}(F)
\ge
\left(\frac12-o(1)\right)D^2.
$$

DA is stronger after the Favard bootstrap:

$$
A_{DB}(y_F)
=0.5196858569\ldots>\frac12.
$$

Thus PI supplies a useful geometric interpretation—cyclic survivors have almost perpendicular actual diameter directions—while DA+Favard supplies the best current area constant.

---

## 7. Equality/stability information

If a cyclic sequence had

$$
\frac hD\to y_F,
$$

then the lower and upper area envelopes squeeze:

$$
\frac{\operatorname{area}(F)}{D^2}
\to A_{DB}(y_F)=L(y_F).
$$

Hence such a threshold sequence must asymptotically saturate both:

1. the DA difference-body direction-gap area lower bound; and
2. Favard's symmetric-lens diameter extremal bound.

These equality mechanisms are geometrically very different. DA extremality concentrates all but one projective diameter-direction gap near the minimum `2a_D`, whereas Favard extremality makes the force hull approach a symmetric lens.

A quantitative incompatibility between these two near-equality structures would raise the threshold again or eliminate the cyclic branch entirely. This is now the most concrete convex-geometric stability target inside the cycle endpoint.

---

## 8. Regression audit

### Regular odd shells

For a large regular odd unit polygon,

$$
q/D\to\pi,
$$

which is above `y_F`. FL does not falsely exclude the canonical shell regression.

### Symmetric lens

A lens can saturate Favard but does not by itself realize the post-ZF discrete diameter-direction system. FL uses the lens only as a sharp upper envelope.

### Isoperimetric disk

The disk upper envelope is weaker for every `y<pi`, so replacing Favard by isoperimetry loses real information but does not invalidate the earlier bootstrap.

### External dependency

Only Favard's classical planar theorem is imported. The inversion and all one-variable monotonicity used here are proved explicitly.

---

## 9. Next theorem

The cyclic primitive endpoint now has

$$
\liminf q/D
=
\liminf h/D
\ge2.6189005339\ldots
$$

and force-hull area at least

$$
0.5196858569\ldots D^2.
$$

The highest-value next theorem is a **DA/Favard stability incompatibility**: show that a convex equilateral force hull with `Theta(D)` actual diameter directions separated as in DB cannot approach the symmetric-lens Favard envelope at the same time that its difference-body direction polygon approaches DA equality.

A fixed positive gap between the two equality regimes would replace `y_F` by a larger constant; an incompatibility throughout `y<pi` would force `q/D->pi` and reduce the cyclic branch to near-constant-width/regular-shell geometry.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The cyclic reduction and DA are report-level. Favard is a classical external theorem with a modern published statement; no canonical route map is changed.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic endpoint:
  per(F)=q,
  h=q-d_H, d_H<=2.
Set y=h/D; then q/D->y along any convergent subsequence.

Main DA:
  area(F)/D^2 >= (y+sin y)/6 + o(1).

Favard lens envelope:
For y=P/D in (2,pi], let theta solve y=2theta/sin theta. Then every convex body
with perimeter P and diameter D satisfies
  area/D^2 <= L(y)
  L(y)=(theta-sin theta cos theta)/(2 sin^2 theta).
Moreover
  L'(y)=1/(2 sin theta)>1/2,
while
  [(y+sin y)/6]'=(1+cos y)/6<=1/3.
So the two envelopes cross exactly once.

Unique root:
  L(y_F)=(y_F+sin y_F)/6,
  y_F=2.6189005339279606... .
Therefore cyclic survivors satisfy
  liminf h/D = liminf q/D >= y_F,
and
  liminf area(F)/D^2 >=0.5196858569093050... .

At threshold, both DA and Favard must be asymptotically sharp. Next target: prove
those two equality mechanisms are quantitatively incompatible.
```
