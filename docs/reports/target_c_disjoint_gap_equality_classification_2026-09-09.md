<!-- theorem-state: {"artifact_id":"ART-6D70D14E8341","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — equality classification for the disjoint-diameter gap

**Date:** 2026-09-09  
**Repository branch:** `research/disjoint-diameter-gap-2026-09-09`  
**Run type:** exact equality-case refinement of DG  
**Target:** Target C post-ZF diameter-direction geometry  
**Depends on:** DG disjoint-diameter gap theorem  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

DG proves that two vertex-disjoint diameter edges in a unit-separated diameter-`D` set have acute projective angle

\[
\theta\ge4a_D,
\qquad
a_D:=\arcsin\frac1{2D}.
\]

The proof contains a stronger equality classification that was not extracted in the original report.

If equality holds, the four endpoints necessarily acquire

1. two cross unit contacts; and
2. a third diameter edge whose projective direction lies strictly between the two original diameter directions.

Consequently two **consecutive** projective directions in the complete actual diameter graph can never attain equality. For a vertex-disjoint consecutive pair the correct statement is the strict inequality

\[
\boxed{\theta>4a_D.}
\]

The infimum is still `4a_D`; no uniform positive improvement is claimed.

---

## 1. Recall the DG coordinates

Let `AC` and `BD` be vertex-disjoint diameter edges and orient their diameter vectors

\[
u=C-A,
\qquad
v=D-B,
\qquad
|u|=|v|=D,
\]

so that the angle between them is the acute projective angle `theta`.

Let `m_1,m_2` be the two edge midpoints and set

\[
w=m_2-m_1,
\qquad
p=\frac{u-v}{2},
\qquad
r=\frac{u+v}{2}.
\]

Then

\[
p\perp r,
\qquad
|p|=D\sin\frac\theta2=:P,
\qquad
|r|=D\cos\frac\theta2=:R.
\]

After choosing orthogonal coordinates, write

\[
p=(P,0),
\qquad
r=(0,R),
\qquad
w=(x,y),
\]

with `x,y>=0` after the harmless sign choices used by DG.

DG proves

\[
0\le x\le P,
\qquad
0\le y\le\sqrt{D^2-x^2}-R,
\tag{1.1}
\]

and

\[
\min\{|A-B|,|C-D|\}
\le2D\sin\frac\theta4.
\tag{1.2}
\]

Unit separation then gives `theta>=4a_D`.

---

## 2. Equality forces the midpoint offset uniquely

Assume now

\[
\theta=4a_D.
\tag{2.1}
\]

Then

\[
2D\sin\frac\theta4
=2D\sin a_D
=1.
\]

The two cross endpoints are distinct source points, so unit separation and (1.2) force equality throughout the DG estimate:

\[
\min\{|A-B|,|C-D|\}=1.
\tag{2.2}
\]

In the DG proof one writes

\[
\frac\theta2=t,
\qquad
x=D\sin\phi,
\qquad
0\le\phi\le t,
\]

and obtains

\[
\min\{|A-B|,|C-D|\}^2
\le4D^2\sin^2\frac{t-\phi}{2}
\le4D^2\sin^2\frac t2.
\tag{2.3}
\]

Because `t>0`, the second inequality in (2.3) is equality only when

\[
\phi=0,
\]

hence

\[
\boxed{x=0.}
\tag{2.4}
\]

Equality in the first step also forces the maximal allowed `y` from (1.1):

\[
\boxed{y=D-R.}
\tag{2.5}
\]

Thus, up to the DG sign/relabel symmetries, equality has the unique midpoint offset

\[
\boxed{w=(0,D-R).}
\tag{2.6}
\]

---

## 3. Two unit contacts and a third diameter edge

Choose the origin at the midpoint of `AC`. Since

\[
u=p+r=(P,R),
\qquad
v=r-p=(-P,R),
\]

and the midpoint of `BD` is `w=(0,D-R)`, the endpoints may be written

\[
\begin{aligned}
A&=(-P/2,-R/2),\\
C&=( P/2, R/2),\\
B&=( P/2,D-3R/2),\\
D'&=(-P/2,D-R/2),
\end{aligned}
\tag{3.1}
\]

where `D'` denotes the endpoint previously called `D`, to avoid confusing it with the scalar diameter.

Direct subtraction gives

\[
A-B=(-P,R-D),
\qquad
C-D'=(P,R-D).
\]

Their common squared length is

\[
P^2+(D-R)^2
=4D^2\sin^2\frac\theta4
=1.
\]

Therefore

\[
\boxed{|A-B|=|C-D'|=1.}
\tag{3.2}
\]

So equality creates two actual unit contacts, not merely one.

Moreover

\[
A-D'=(0,-D),
\]

hence

\[
\boxed{|A-D'|=D.}
\tag{3.3}
\]

Thus equality also creates a third actual diameter edge.

Its direction is the `r` direction, while the original diameter vectors are `r+p` and `r-p`. Since `theta>0`, the projective direction of `r` lies strictly between those two directions along their acute projective interval.

The remaining cross distance is

\[
|C-B|=|2R-D|<D
\]

for `theta>0`, so the forced local active pattern is exactly the one described above unless additional coincidences are imposed by other source points.

---

## 4. Consecutive disjoint diameter directions have strict doubled gap

### Theorem DGE

Let `AC` and `BD` be vertex-disjoint actual diameter edges whose projective directions are consecutive in the cyclic order of the **complete actual diameter graph**. Then

\[
\boxed{
\theta>4\arcsin\frac1{2D}.
}
\tag{DGE.1}
\]

### Proof

DG gives `theta>=4a_D`. If equality held, Section 3 would force the third actual diameter edge `AD'`, whose projective direction lies strictly between the directions of `AC` and `BD`. This contradicts consecutiveness in the complete actual diameter-direction order. Therefore equality is impossible. `square`

C65 is important only when this theorem is inserted into Target C: it identifies the selected relative-interior diameter support with the complete actual diameter graph, so an intermediate forced diameter direction cannot be hidden as an unselected active row.

---

## 5. Shared-endpoint equality for comparison

If two diameter edges `ZA` and `ZB` share the endpoint `Z`, their projective angle `theta` satisfies

\[
|A-B|=2D\sin\frac\theta2\ge1,
\]

so

\[
\theta\ge2a_D.
\]

Equality is exactly

\[
\boxed{|A-B|=1.}
\tag{5.1}
\]

Thus the two local angular floors have parallel active-set interpretations:

- shared floor `2a_D`: one new unit contact appears between the two far endpoints;
- disjoint floor `4a_D`: two new unit contacts appear and an intermediate diameter edge appears.

This makes the asymptotic saturation result DS more concrete: a small-outer-walk survivor approaches a source-wide sequence of first contact/diameter events.

---

## 6. Global strict consequence

Let `m` be the number of disjoint cyclic consecutive diameter-direction pairs. If `m>0`, then summing the local gap bounds gives the strict inequality

\[
\boxed{
\pi
>
2a_D(h-m)+4a_Dm
=2a_D(h+m).
}
\tag{6.1}
\]

Since DG.2 gives `m>=d_H=q-h`, every source with at least one diameter tree component (`d_H>0`) satisfies

\[
\boxed{
2a_Dq<\pi.
}
\tag{6.2}
\]

The inequality is strict but has no uniform margin: DGE equality can be approached by letting the forced intermediate cross distance tend to `D` from below. Therefore (6.2) must not be promoted into a false `pi-c/D` gap.

---

## 7. Regression and scope audit

- The four-point DG sharpness example is not a counterexample to DGE: at equality it contains the forced third diameter edge, so the original two directions are not consecutive in the full diameter graph.
- A regular odd polygon realizes the **shared** gap floor around its diameter cycle; DGE does not disturb this binding shell regression.
- The theorem supplies exact strictness, not a quantitative margin.
- Near-active contacts or near-diameter pairs are not treated as active constraints; no compactness-to-exactness shortcut is used.
- No conclusion about Level I follows merely from summing arbitrarily small strict local gaps.

---

## 8. Next target

DGE identifies the only mechanism by which the disjoint floor can be approached: each near-saturated disjoint pair must have

1. two cross distances `1+o(1)`; and
2. an intermediate cross distance `D-o(1)`.

In the UF near-circle phase, DS says almost all relevant gaps are near their floors. The next useful stability theorem is therefore source-specific:

> show that a linear family of these simultaneous near-contact / near-diameter events cannot coexist with lexicographic contact-and-diameter minimality without an actual finite active-set release.

A proof must use finite first-event geometry or the C63 integration machinery; simple limiting compactness is insufficient.
