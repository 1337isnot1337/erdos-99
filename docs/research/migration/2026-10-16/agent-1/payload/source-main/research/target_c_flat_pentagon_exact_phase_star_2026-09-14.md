# Erdos Problem #99 - exact phase-star orientation of a flat exceptional pentagon

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** triangle-free exceptional-face geometry; empty-pentagon trapezoid stability; finite stopped-train theorem DT
**Claim class:** proof-only finite geometric refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The empty-pentagon endpoint shows that every sufficiently cheap pentagonal exceptional
face is close to the flat unit trapezoid. Existing train-star notes use only the
asymptotic direction pattern `3:1:1`. There is a strict finite statement hidden in the
same geometry.

Let a sufficiently flat convex equilateral exceptional pentagon be cyclically labeled

\[
l,m,r,a,b
\]

as in the trapezoid endpoint, so the five boundary sides are exact unit contacts and
`l-m-r` is the almost-flat long base. The committed train-star packing theorem, via
no-bounded-return and singleton bounded-loop exclusion, shows that these five boundary
sides belong to five distinct complete stopped trains. Denote those trains by the same
side labels.

Then:

1. the two leaf-hinge train pairs `(lm,lb)` and `(mr,ra)` have acute projective angle
   strictly greater than `pi/3`;
2. the two minority trains `lb` and `ra` have acute projective angle strictly less
   than `pi/3`;
3. after the flatness neighborhood is chosen small enough, the three majority trains
   `lm,mr,ab` are pairwise at projective angle strictly less than `pi/3`.

Consequently the train-crossing graph induced by these five complete trains is a
subgraph of the exact bipartite phase star

\[
\boxed{K_{3,2},\qquad
\{lm,mr,ab\}\ \sqcup\ \{ra,lb\}.}
\tag{PS.1}
\]

In particular the two minority trains can never cross each other in a strict rhombus
anywhere else in the contact graph. This is a finite crossing exclusion, not merely an
`o(1)` direction statement.

The core trigonometric identity is also exact. Put

\[
x:=|m-a|,\qquad y:=|m-b|,
\tag{PS.2}
\]

and

\[
A:=\arccos(x/2),\qquad B:=\arccos(y/2).
\tag{PS.3}
\]

Triangle-freeness gives `x,y>1`, hence `A,B<pi/3`. Define

\[
u:={\pi\over3}-A>0,
\qquad
v:={\pi\over3}-B>0.
\tag{PS.4}
\]

If `Psi` is the angle `angle amb`, then the minority projective gap is

\[
\Gamma=A+B-\Psi.
\tag{PS.5}
\]

For the hypothetical threshold angle

\[
\Psi_0:=A+B-{\pi\over3}
={\pi\over3}-(u+v),
\tag{PS.6}
\]

let `c_0` be the side opposite `Psi_0` in a triangle with adjacent sides `x,y`. Then

\[
\boxed{
1-c_0^2=8\sin u\,\sin v\,\cos(u+v).
}
\tag{PS.7}
\]

In a fixed sufficiently flat neighborhood `u,v>0` and `u+v<pi/2`, so the right side
is positive. Thus `c_0<1`. The actual triangle `mab` has opposite side `|a-b|=1`, and
the opposite side is strictly increasing with its included angle. Hence

\[
\Psi>\Psi_0,
\qquad
\boxed{\Gamma<\pi/3.}
\tag{PS.8}
\]

This is the exact mechanism behind the local phase star.

## 1. Leaf hinges are strictly above sixty degrees

Because `m` and `a` are nonconsecutive boundary vertices of an actual exceptional
contact face, the hidden chord `ma` is strictly longer than one. Likewise `mb>1`.
Thus

\[
x>1,\qquad y>1.
\tag{PS.9}
\]

Consider the unit isosceles triangle `mra`. Its base is `ma=x`. The angle at `m` is
`A=arccos(x/2)`, so the vertex angle at `r` is

\[
\angle mra=\pi-2A.
\tag{PS.10}
\]

Since `A<pi/3`,

\[
\boxed{\angle mra>\pi/3.}
\tag{PS.11}
\]

This is precisely the acute projective angle between the contact-edge axes `mr` and
`ra` once the flat neighborhood is fixed. The same argument for the unit isosceles
triangle `mlb` gives

\[
\boxed{\angle mlb>\pi/3.}
\tag{PS.12}
\]

Thus both leaf-hinge pairs lie strictly on the crossing-eligible side of the DT
`pi/3` threshold. No claim is made that they actually cross elsewhere.

## 2. Exact minority-gap formula

Work in the same neighborhood and let

\[
\Psi:=\angle amb.
\]

The triangle `mra` gives an angle `A` from the ray `mr` to the ray `ma`. The triangle
`mlb` gives an angle `B` from `mb` to `ml`. Reading the cyclic directions through the
convex pentagon shows that the acute projective angle between the minority sides `ra`
and `lb` is

\[
\boxed{\Gamma=A+B-\Psi.}
\tag{PS.13}
\]

At the flat equality trapezoid `A=B=Psi=pi/3`, so `Gamma=pi/3`. The actual
triangle-free face has moved both hidden diagonals outward, and the next subsection
shows that the resulting inequality has a definite sign.

## 3. The threshold-side identity

Set

\[
A={\pi\over3}-u,
\qquad
B={\pi\over3}-v,
\qquad
u,v>0.
\]

Then

\[
x=2\cos A,
\qquad
y=2\cos B.
\tag{PS.14}
\]

If the minority gap were exactly `pi/3`, equation (PS.13) would force the included
angle in triangle `mab` to be

\[
\Psi_0=A+B-{\pi\over3}.
\]

Let

\[
c_0^2:=x^2+y^2-2xy\cos\Psi_0.
\tag{PS.15}
\]

Substituting (PS.14), expanding the angle addition formulas, and simplifying gives

\[
\begin{aligned}
1-c_0^2
&=8\sin u\sin v\cos(u+v).
\end{aligned}
\tag{PS.16}
\]

This identity is exact. Choose the trapezoid-stability neighborhood once so that

\[
0<u,v,
\qquad
u+v<\pi/2,
\qquad
0<\Psi_0<\pi.
\tag{PS.17}
\]

Then (PS.16) is strictly positive, so `c_0<1`.

For fixed positive adjacent sides `x,y`, the opposite-side square

\[
c(\theta)^2=x^2+y^2-2xy\cos\theta
\]

is strictly increasing for `theta in (0,pi)`. The actual third side of triangle `mab`
is the pentagon boundary edge `ab`, hence

\[
c(\Psi)=1>c_0=c(\Psi_0).
\]

Therefore `Psi>Psi_0`, and (PS.13) gives

\[
\Gamma
=A+B-\Psi
<A+B-\Psi_0
={\pi\over3}.
\]

This proves (PS.8).

## 4. Exact local crossing-eligibility graph

DT proves that if two distinct complete trains cross in a strict unit rhombus, their
acute projective direction separation is strictly greater than `pi/3`.

By (PS.8), the minority trains `ra` and `lb` therefore cannot cross. Trapezoid
stability also makes the three majority axes `lm,mr,ab` lie in one arbitrarily small
projective window. Tighten the fixed neighborhood so every majority-majority gap is
strictly less than `pi/3`; no pair of majority trains can cross either.

Hence every actual rhombus crossing among the five terminal trains has one endpoint
in

\[
M:=\{lm,mr,ab\}
\]

and the other in

\[
L:=\{ra,lb\}.
\]

This proves (PS.1). The two leaf pairs singled out in Section 1 are strict
majority-leaf pairs with projective gaps above `pi/3`, explaining the `3:1:1`
phase-star orientation geometrically.

## 5. Quantitative threshold identity and equality behavior

Equation (PS.16) also records why the minority exclusion is second-order near the flat
trapezoid. If one hidden diagonal stays exactly one, then one of `u,v` is zero and the
right side vanishes: the minority gap remains exactly `pi/3`. Only when **both** hidden
contacts open does the minority pair move strictly to the noncrossing side.

For small positive `u,v`,

\[
1-c_0^2=8uv+O((u+v)^4),
\]

so the strict phase-star orientation is bilinear in the two leaf openings. This is why
it is invisible to a first-order one-gap perturbation.

No lower bound on the amount `pi/3-Gamma` is asserted here; one hidden gap may be much
smaller than the other. The finite sign is the useful invariant.

## 6. Consequences for the low-t pentagon sea

On the low-`t`, small-residual branch, all but `o(D)` of the linearly many pentagons
lie in the fixed neighborhood used above. Therefore the train-star packing theorem can
be strengthened as follows:

```text
for every good pentagon:
    3 majority terminal trains are mutually noncrossing;
    2 minority terminal trains are mutually noncrossing;
    every possible crossing among the five is majority-to-minority;
    both geometric leaf hinges are strict >60-degree majority/minority pairs.
```

Thus the local `3:1:1` object is not merely close to a three-axis pattern. It already
has the exact crossing-eligibility signature of a bipartite phase star at every finite
stage.

This does not by itself create a quadratic global Mantel deficit: the five-train stars
need not share a common global phase. Its value is to remove one local ambiguity from
a future phase-propagation or block-locking theorem. Any global model that makes the
two minority trains cross is now ruled out without an asymptotic limiting argument.

## 7. Scope audit

- The theorem applies to the isolate-free flat-pentagon neighborhood supplied by the
  empty-pentagon endpoint/stability theorem.
- Distinctness of the five terminal trains is imported from the committed train-star
  theorem; no boundary side is silently identified with another train variable.
- Hidden boundary chords `ma,mb` are strictly longer than one in every actual
  triangle-free exceptional face.
- The exact inequality `Gamma<pi/3` uses both strict hidden gaps and a fixed sufficiently
  small flatness neighborhood; it is not claimed for every convex equilateral pentagon.
- Crossing exclusion uses only DT's finite `>pi/3` crossing-angle theorem.
- No train is assumed to cross merely because its direction gap exceeds `pi/3`.
- No exact unit triangle or same-cardinality strict sub-`D` competitor is produced.

C-II and Level I remain open.
