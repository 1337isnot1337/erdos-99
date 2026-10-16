# Erdos Problem #99 - pentagon hidden-contact gap budget

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** empty-pentagon trapezoid endpoint; pentagonal two-contact tooth extraction; exact force-hull residual conservation
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The flat-pentagon endpoint gives linearly many pentagonal faces with two-contact teeth
whose hidden chord has length `1+o(1)`. The existing argument is qualitative: it uses
compactness separately at every fixed gap threshold and then diagonalizes. For a
source-level deformation, a stronger quantity is available. The pentagon residual
itself controls the **sum of the two missing contact gaps**.

Let an isolate-free convex equilateral pentagonal face be cyclically labeled

\[
l,m,r,a,b
\]

as in the flat-trapezoid endpoint, and put

\[
x:=|m-a|,\qquad y:=|m-b|.
\tag{HG.1}
\]

In the triangle-free branch `x,y>1`. There is an absolute neighborhood of the flat
trapezoid in which

\[
\boxed{
r(P)\ge {1\over2}\bigl((x-1)+(y-1)\bigr).
}
\tag{HG.2}
\]

Consequently, after tightening the fixed pentagon stability threshold once, every
family `G` of distinct good pentagonal faces satisfies

\[
\boxed{
\sum_{P\in G}\bigl[(|m_P-a_P|-1)+(|m_P-b_P|-1)\bigr]
\le 2R_F.
}
\tag{HG.3}
\]

This gives an `L^1` contact-activation budget, not merely pointwise convergence.

Combining it with the existing one-tooth-per-pentagon greedy extraction gives a fixed
constant `theta_0>0` and two families:

- `H`, pairwise endpoint-disjoint hidden chords, and
- `T`, pairwise vertex-disjoint two-contact teeth,

such that

\[
\boxed{
X+{R_F\over\theta_0}+9|H|
\ge (f_*-o(1))D,
}
\tag{HG.4}
\]

\[
\boxed{
X+{R_F\over\theta_0}+13|T|
\ge (f_*-o(1))D,
}
\tag{HG.5}
\]

where

\[
X:=Q-f,
\qquad
f_*:=\sqrt{\Delta_2}-{\pi\over4}+0.00021
=0.167124643466509\ldots .
\]

The extracted families can be chosen simultaneously with

\[
\boxed{
\sum_{e\in H} (|e|-1)\le2R_F,
\qquad
\sum_{(x,y,z)\in T} (|x-z|-1)\le2R_F.
}
\tag{HG.6}
\]

In particular, on the hard branch

\[
X=o(D),\qquad R_F=o(D),
\]

there are at least

\[
\left({f_*\over13}-o(1)\right)D
= (0.012855741805116\ldots-o(1))D
\]

pairwise vertex-disjoint two-contact teeth whose **total** missing-side excess is
`o(D)`. The average missing-side excess is therefore `O(R_F/D)=o(1)`, but (HG.6) is
strictly stronger than that average statement and is the form suitable for a
simultaneous finite-motion or first-contact argument.

---

## 1. Exact area formula in the two hidden diagonals

Let

\[
a_0={\sqrt3\over2}.
\]

For an isolate-free pentagon the canonical fixed-boundary residual is

\[
r(P)={A(P)\over a_0}-{3\over2}.
\tag{HG.7}
\]

Because the pentagon is convex, the two diagonals from `m` triangulate it into

\[
\triangle mra,\qquad \triangle mab,\qquad \triangle mbl.
\]

The first and third triangles have side lengths `(1,1,x)` and `(1,1,y)`. Define

\[
F(s):={s\over4}\sqrt{4-s^2}.
\tag{HG.8}
\]

The middle triangle has side lengths `(x,y,1)`. By Heron's formula define

\[
G(x,y):={1\over4}
\sqrt{(x+y+1)(-x+y+1)(x-y+1)(x+y-1)}.
\tag{HG.9}
\]

Therefore the pentagon area is exactly

\[
\boxed{
A(P)=F(x)+G(x,y)+F(y).
}
\tag{HG.10}
\]

No asymptotic approximation is used in (HG.10).

At the flat equality trapezoid, `x=y=1`, and

\[
F(1)=G(1,1)={\sqrt3\over4},
\qquad
A={3\sqrt3\over4},
\qquad
r=0.
\tag{HG.11}
\]

---

## 2. First-order residual cost of opening either hidden contact

Differentiate (HG.8):

\[
F'(s)={2-s^2\over2\sqrt{4-s^2}},
\qquad
F'(1)={1\over2\sqrt3}.
\tag{HG.12}
\]

For the middle triangle it is convenient to write

\[
16G(x,y)^2
=4x^2y^2-(x^2+y^2-1)^2.
\tag{HG.13}
\]

Differentiating at `(1,1)` gives

\[
\partial_xG(1,1)=\partial_yG(1,1)
={1\over2\sqrt3}.
\tag{HG.14}
\]

Hence for

\[
\rho(x,y):={F(x)+G(x,y)+F(y)\over a_0}-{3\over2},
\]

we have the exact endpoint gradient

\[
\boxed{
\partial_x\rho(1,1)=\partial_y\rho(1,1)={2\over3}.
}
\tag{HG.15}
\]

The functions are smooth in a neighborhood of `(1,1)`. Therefore there is
`eta_0>0` such that throughout

\[
1\le x,y\le1+\eta_0
\]

both partial derivatives are at least `1/2`. Integrating first in `x` and then in
`y` from `(1,1)` yields

\[
\rho(x,y)
\ge {1\over2}(x-1)+{1\over2}(y-1).
\tag{HG.16}
\]

For every pentagon in this neighborhood, `rho(x,y)=r(P)` by (HG.7)--(HG.10), proving
(HG.2).

The direction of the inequality is important. Moving either hidden chord above one
costs residual **linearly** at the equality endpoint; there is no quadratic flatness
in this two-diagonal parametrization.

---

## 3. Global L1 gap budget

Tighten the flat-pentagon stability threshold so that every retained pentagon

1. has no assigned interior isolate (by the first Wegner residual jump), and
2. lies in the neighborhood `1<=x,y<=1+eta_0` from Section 2.

Call the resulting fixed positive residual threshold `theta_0`.

The exceptional-face residuals are nonnegative and their total is at most `R_F`.
Therefore the number of pentagons with residual at least `theta_0` is at most

\[
{R_F\over\theta_0}.
\tag{HG.17}
\]

For any family `G` of retained good pentagons, summing (HG.2) gives

\[
\begin{aligned}
\sum_{P\in G}
\bigl[(x_P-1)+(y_P-1)\bigr]
&\le2\sum_{P\in G}r(P)\\
&\le2R_F,
\end{aligned}
\]

which proves (HG.3).

This summation does not require the pentagons to be vertex-disjoint.

---

## 4. Combine with the pentagon count and tooth extraction

Let `p_5` be the number of bounded exceptional pentagons. The exact degree-excess
identity gives

\[
p_5\ge f-X,
\qquad X=Q-f.
\tag{HG.18}
\]

The AG42/Section-171 face floor is

\[
f\ge(f_*-o(1))D.
\tag{HG.19}
\]

After deleting the at most `R_F/theta_0` high-residual pentagons from (HG.17), the
number `G_0` of retained good pentagons obeys

\[
G_0
\ge (f_*-o(1))D-X-{R_F\over\theta_0}.
\tag{HG.20}
\]

Choose one of the two leaf teeth from every good pentagon. The existing tooth-conflict
argument has maximum degree at most eight for hidden-chord endpoint conflicts and at
most twelve for full three-vertex conflicts. Hence greedy extraction gives

\[
|H|\ge {G_0\over9},
\qquad
|T|\ge {G_0\over13}.
\tag{HG.21}
\]

Equations (HG.20)--(HG.21) are exactly (HG.4)--(HG.5).

Every selected hidden chord is one of the two chords counted in (HG.3). Passing to a
subset can only decrease the nonnegative gap sum, so both extracted families satisfy
(HG.6).

---

## 5. Frontier effect

The previous compactness/diagonalization theorem says that linearly many hidden chords
have length `1+o(1)`. The new statement retains how much **total motion to first
contact** is stored in those inactive constraints:

```text
linear disjoint two-contact teeth
+ total hidden-side excess <= 2 R_F.
```

Thus on `R_F=o(D)` the entire linear family is separated from activation by only
`o(D)` total radial gap. A future source-preserving deformation no longer needs a
uniform per-tooth activation estimate. It would be enough to produce a simultaneous
motion whose aggregate available displacement dominates this `L^1` budget while
keeping the old active contacts and diameter constraints feasible.

This note does **not** supply that global motion. It does not assign KKT multipliers to
the hidden chords, and it does not turn near contacts into exact contacts by compactness
alone. C-II and Level I remain open.
