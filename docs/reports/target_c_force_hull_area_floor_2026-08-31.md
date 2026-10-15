<!-- theorem-state: {"artifact_id":"ART-28DBB80C5CC8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C67: quantitative force-hull area floor

**Date:** 2026-08-31  
**Repository base:** `bc711e54` (main after C66 / PR #69)  
**Run type:** exact geometric theorem / stale-branch audit  
**Target:** Target C Gate C-II / outer-shell geometry  
**Depends on:** C34 loaded-endpoint count, C43 large-n anti-Reuleaux exclusion only indirectly through the live C-II stack, C65 full diameter visibility, planar diameter-thrackle geometry, unit separation  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

This report salvages the force-hull area argument from stale PR #42, but corrects its projective-circle packing lemma. The stale proof claimed that a set of projective directions of diameter below `pi/2` lies in an arc whose length equals that diameter; that statement is false on a circle. The correct threshold `pi/3` is enough here and preserves the same asymptotic constant.

Let `F=conv B` be the canonical C-II force hull after C65, so the response boundary `B` is the full actual diameter-endpoint set. Then

\[
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{2}\sin\Phi(D),
}
\]

where

\[
\Phi(D)=
\min\left\{
\frac\pi3,
\left(\frac D4-1\right)
2\arcsin\frac1{2D}
\right\}.
\]

Consequently

\[
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac12\sin\frac14
=0.1237019796\ldots .
}
\]

Thus the fully force-visible force hull cannot collapse to an asymptotically thin strip. This does not by itself control the fully inactive rattler population or close C-II.

---

## 1. Distinct diameter directions are uniformly separated

Work with the full actual diameter graph `H`, which equals the positive diameter support of a relative-interior normalized KKT stress by C65.

### Lemma C67.1 — shared-endpoint separation

Let `ba` and `bc` be distinct diameter edges sharing `b`, and let

\[
\theta=\angle abc.
\]

Since

\[
|a-b|=|c-b|=D,
\]

the chord formula gives

\[
|a-c|=2D\sin(\theta/2).
\]

Unit separation gives `|a-c|>=1`, hence

\[
\boxed{
\theta\ge2\arcsin\frac1{2D}.
}
\tag{C67.1}
\]

Also `|a-c|<=D`, because `D` is the source diameter, so `theta<=pi/3`. Therefore `theta` is exactly the projective circular distance between the two supporting line directions.

### Lemma C67.2 — disjoint-edge separation

Let `AB` and `CD` be vertex-disjoint diameter edges. The planar diameter-thrackle property makes them cross properly. Let `phi in (0,pi/2]` be the acute angle between their supporting lines.

Put

\[
A=(0,0),\qquad B=(D,0),
\]

and label the endpoints of the crossing chord so that

\[
C=(x,-u),\qquad D'=(y,v),
\]

with `u,v>0` and `x<=y`. Since both endpoints lie within distance `D` of both `A` and `B`,

\[
0\le x\le y\le D.
\]

The vertical and horizontal components of `CD'` are

\[
u+v=D\sin\phi,
\qquad
y-x=D\cos\phi.
\]

Define

\[
a:=x+(D-y)=D(1-\cos\phi).
\]

Suppose `D sin phi<1`. For `D>=2`,

\[
a=
\frac{D\sin^2\phi}{1+\cos\phi}
<\frac12.
\]

Because `0<=x<=a` and `0<=D-y<=a`, unit separation from `A` and `B` gives

\[
u^2+x^2\ge1,
\qquad
v^2+(D-y)^2\ge1.
\]

Hence

\[
u>\sqrt{1-a^2}>\frac{\sqrt3}{2},
\qquad
v>\sqrt{1-a^2}>\frac{\sqrt3}{2}.
\]

Therefore `u+v>sqrt(3)>1`, contradicting `u+v=D sin phi<1`. Thus

\[
\boxed{
\phi\ge\arcsin(1/D)
>
2\arcsin(1/(2D)).
}
\tag{C67.2}
\]

for `D>=2`.

Combining C67.1-C67.2, any two distinct diameter edges have projective direction distance at least

\[
\boxed{
\delta_D:=2\arcsin\frac1{2D}.
}
\tag{C67.3}
\]

---

## 2. Correct projective-circle packing lemma

The stale PR #42 used an incorrect `pi/2` containment threshold. The following replacement is enough.

### Lemma C67.3 — separated points on a projective circle

Let `X` be `h>=2` points on a circle of circumference `pi`, with pairwise circular distance at least `delta>0`. Then two points of `X` have circular distance at least

\[
\boxed{
\min\left\{\frac\pi3,(h-1)\delta\right\}.
}
\tag{C67.4}
\]

#### Proof

Let `r` be the circular diameter of `X`. Suppose

\[
r<\frac\pi3.
\]

Choose `x_0 in X` and identify the circle with `R/pi Z` so that `x_0=0`. Every other point has a representative in `[-r,r]`. Let

\[
a=\max X\cap[0,r],
\qquad
-b=\min X\cap[-r,0]
\]

with `a,b>=0`, omitting one side if it is empty.

If both sides occur, the circular distance between `a` and `-b` is

\[
\min\{a+b,\pi-a-b\}\le r.
\]

If `a+b>r`, then necessarily `pi-a-b<=r`, so

\[
a+b\ge\pi-r>\frac{2\pi}{3}.
\]

But `a+b<=2r<2pi/3`, a contradiction. Therefore `a+b<=r`.

Hence whenever `r<pi/3`, the whole set lies in one ordinary arc of length at most `r`. Packing `h` points in that arc with consecutive separation at least `delta` requires

\[
r\ge(h-1)\delta.
\]

Therefore either `r>=pi/3` or `r>=(h-1)delta`, proving (C67.4). `square`

### Loaded-endpoint input

Canonical C34 gives

\[
2|B|\ge\lceil D\rceil+2.
\]

Every diameter endpoint is incident to at least one diameter edge, so with `h=|H|`,

\[
2h\ge|B|.
\]

Thus

\[
\boxed{
h>\frac D4.}
\tag{C67.5}
\]

Apply C67.3 to the projective line directions of the diameter edges, with `delta=delta_D`. There are two diameter edges whose projective angle `phi` satisfies

\[
\boxed{
\phi\ge
\Phi(D):=
\min\left\{
\frac\pi3,
\left(\frac D4-1\right)
2\arcsin\frac1{2D}
\right\}.
}
\tag{C67.6}
\]

For large `D`, the second term is the smaller one.

---

## 3. Two separated diameter chords force quadratic area

Take the two diameter edges from C67.6.

If they share an endpoint, their three endpoints form a triangle with two sides `D` and included angle `phi`, so its area is

\[
\frac{D^2}{2}\sin\phi.
\]

If they are disjoint, the diameter-thrackle property makes them the crossing diagonals of a convex quadrilateral. The area of a convex quadrilateral is one half the magnitude of the cross product of its diagonal vectors, hence again

\[
\frac{D^2}{2}\sin\phi.
\]

All endpoints lie in the force hull `F`. Therefore:

### Theorem C67 — force-hull area floor

\[
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{2}\sin\Phi(D).
}
\tag{C67.7}
\]

Since

\[
2\arcsin\frac1{2D}=\frac1D+O(D^{-3}),
\]

we have

\[
\Phi(D)=\frac14+o(1),
\]

and therefore

\[
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac12\sin\frac14
=0.1237019796\ldots .
}
\tag{C67.8}
\]

---

## 4. What this removes and what it does not

The full source hull `K=conv A` satisfies the isodiametric bound

\[
\operatorname{area}(K)\le\frac\pi4D^2.
\]

Thus C67 gives

\[
\operatorname{area}(K)-\operatorname{area}(F)
\le
\left(
\frac\pi4-
\frac12\sin\Phi(D)
\right)D^2.
\tag{C67.9}
\]

Asymptotically the coefficient is at most

\[
0.7853981634-0.1237019796
=0.6616961838\ldots .
\]

This is not a capacity contradiction. A round or regular-shell force hull remains compatible with the theorem, and a macroscopic fully inactive rattler population can still occupy the rest of the source hull. The theorem removes only the asymptotically one-dimensional force-hull phase.

## 5. Interaction with C66

C66 shows that if the C-II response defect `epsilon` satisfies `D epsilon ->0`, then the normalized diameter stress is asymptotically concentrated on one diameter star. C67 is deliberately weight-free: even in that stress-star phase, the complete actual diameter graph has `Omega(D)` separated line directions and the force hull has a fixed positive area fraction.

Therefore any closing theorem for the C66 stress-star phase may use a genuinely two-dimensional geometric carrier. It cannot model the remaining source as an asymptotically thin force chain without also accounting for the `Omega(D)` low-weight diameter directions forced by C65 and C34.

## Regression audit

- The projective packing statement uses `pi/3`, not the false `pi/2` threshold from stale PR #42.
- No uniform lower bound on KKT weights is used.
- No lattice or force-bulk assumption is used.
- A regular shell is allowed.
- The asymptotic constant `0.5 sin(1/4)` is unchanged by the corrected circle lemma.
