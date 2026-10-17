# Target C-II — three dominant sides already force a through pair in a full pentagonal flower

**Date:** 2026-09-15\
**Status:** proof-only atomic/local structural theorem\
**Scope:** sequences of fully rhombic convex unit pentagonal faces relative to one exact triangular projective orbit\
**Dependencies:** elementary unit-vector closure; triangular six-ray arithmetic; convex cyclic edge order\
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Fix one exact triangular projective orbit with oriented six-ray lift

\[
\widetilde{\mathcal O}
=\{e^{i(\phi+j\pi/3)}:0\le j<6\}.
\]

Consider a convergent sequence of fully rhombic convex unit pentagonal faces. Suppose
at least three of the five side-train directions converge projectively to this orbit.
Pass to oriented side-vector limits and call three selected orbit rays

\[
v_1,v_2,v_3\in\widetilde{\mathcal O},
\]

while the remaining two unit-vector limits are `w_1,w_2`. Polygon closure gives

\[
v_1+v_2+v_3+w_1+w_2=0.
\tag{TF.1}
\]

Then exactly one of the following happens.

1. **All-orbit case.** Both `w_1,w_2` also belong to `widetilde O`. The closed
   five-ray pattern has projective multiplicities `3,1,1`; one repeated phase contains
   opposite signs and admits the standard pentagonal through connector within `pi/6`
   of its train normal.

2. **Alternating-return case.** Up to rotation and reversal,

   \[
   \{v_1,v_2,v_3\}=\{e^{0i},e^{2\pi i/3},e^{4\pi i/3}\},
   \qquad
   w_2=-w_1,
   \tag{TF.2}
   \]

   with the projective direction of `w_1` outside the triangular orbit. The two
   `w`-sides are an opposite-sign same-projective-direction pair. Their midpoint
   connector through the pentagon has positive common-normal projection and makes
   angle at most `pi/6` with that normal; in the genuinely non-orbit case the angle is
   strictly below `pi/6`.

Thus every atomic full flower with at least three sides in one triangular orbit has a
**local through pair**. The pair is either an orbit pair or, in the unique escape
pattern, the two complement sides themselves.

For shrinking phase windows this gives the asymptotic statement

\[
\boxed{
\text{at least three dominant side terminals}
\Longrightarrow
\text{a through pair with phase mismatch }o(1).
}
\tag{TF.3}
\]

Consequently, if `M_D` full flowers are given and `C_D` counts side-terminal
occurrences outside a shrinking dominant-orbit window, while `P_D` counts flowers on
which one of the above asymptotic through pairs is selected, then

\[
\boxed{
M_D-P_D\le {C_D\over3}+o(D).
}
\tag{TF.4}
\]

Equivalently,

\[
\boxed{P_D\ge M_D-{C_D\over3}-o(D).}
\tag{TF.5}
\]

This improves the two-complement allocation law for the broader class of **locally
through-spliceable** flowers: a flower which avoids every such through pair must spend
at least three complement terminal occurrences.

The theorem does not yet claim that through pairs of arbitrary complement phases can
all be spliced simultaneously into one global pseudosegment family. That is the new
global obligation.

---

## 1. Exact three-ray sum classification

Put

\[
s=v_1+v_2+v_3.
\]

Since `w_1,w_2` are unit vectors, (TF.1) implies

\[
|s|=|w_1+w_2|\le2.
\tag{TF.6}
\]

The vector `s` lies in the unit triangular lattice. Its squared norm is an integer of
the form `m^2+mn+n^2`. Direct six-ray arithmetic, also exhausted by the companion
verifier, shows that a sum of three six-ray unit vectors has squared norm in

\[
\{0,1,3,4,7,9\}.
\tag{TF.7}
\]

The closure bound (TF.6) leaves only

\[
|s|^2\in\{0,1,3,4\}.
\tag{TF.8}
\]

We treat these four cases.

---

## 2. If `|s|=1`, all five sides are orbit rays

A three-ray sum of norm one necessarily contains an opposite ray pair. After
cancelling such a pair, the third ray is exactly `s`; the exhaustive six-ray
classification gives no other norm-one pattern.

Write the pair as `v,-v` and the remaining selected orbit ray as `u`. Then

\[
s=u,
\qquad
u+w_1+w_2=0.
\]

Three unit vectors sum to zero if and only if their oriented directions differ by
`2pi/3`. Since `u` is one six-ray orbit vector, `w_1,w_2` are the other two members of
that alternating triangular triple. Hence both lie in `widetilde O`.

---

## 3. If `|s|=sqrt(3)`, all five sides are orbit rays

Equation (TF.1) gives

\[
|w_1+w_2|=\sqrt3.
\]

For two unit vectors whose angular separation is `theta`,

\[
|w_1+w_2|^2=2+2\cos\theta.
\]

Thus `cos theta=1/2`, so their smaller oriented separation is `pi/3`. Their resultant
points along the angle bisector.

Every norm-`sqrt(3)` vector of the triangular lattice points halfway between two
adjacent six-ray directions. Therefore the unique unordered unit pair separated by
`pi/3` and summing to `-s` is precisely that adjacent six-ray pair. Hence

\[
w_1,w_2\in\widetilde{\mathcal O}.
\]

---

## 4. If `|s|=2`, all five sides are orbit rays

Now

\[
|w_1+w_2|=2.
\]

Equality in the triangle inequality for two unit vectors forces

\[
w_1=w_2=-s/2.
\]

Every norm-two vector of the triangular lattice is exactly twice one of its six unit
rays: the integer solutions of

\[
m^2+mn+n^2=4
\]

are `2` times the six solutions of norm one. Thus `-s/2` lies in `widetilde O`, and
again all five side limits are orbit rays.

The equality `w_1=w_2` is permitted as a limiting direction even though each finite
pentagon is strictly convex; no false finite angle gap is used here.

---

## 5. The only non-all-orbit case is `s=0`

The remaining possibility in (TF.8) is

\[
s=0.
\]

Three unit vectors sum to zero exactly when they form an oriented equilateral triple.
For six-ray vectors this means, up to rotation,

\[
\{v_1,v_2,v_3\}=\{1,e^{2\pi i/3},e^{4\pi i/3}\}
\]

or its antipodal triple. These are one side from each projective triangular phase.
Equation (TF.1) then reduces to

\[
w_1+w_2=0,
\]

so

\[
\boxed{w_2=-w_1.}
\tag{TF.9}
\]

If this common projective direction is itself triangular, all five directions are in
the orbit and we are back in case 1. Otherwise (TF.2) is the unique escape pattern.

---

## 6. The complement opposite pair is a genuine through pair

Normalize the alternating dominant triple to oriented directions

\[
a=e^{0i},
\qquad b=e^{2\pi i/3},
\qquad c=e^{4\pi i/3},
\qquad a+b+c=0.
\]

Write

\[
w=e^{i\theta},
\qquad -w=e^{i(\theta+\pi)}.
\]

Using rotation by `2pi/3`, reversal, and exchange of the two complement sides, reduce
to

\[
0\le\theta\le\pi/3.
\tag{TF.10}
\]

At the endpoints `theta=0,pi/3`, the complement projective direction is triangular and
the flower is all-orbit. Assume henceforth

\[
0<\theta<\pi/3.
\]

The cyclic direction order of the convex limiting pentagon is then

\[
a,\ w,\ b,\ -w,\ c.
\tag{TF.11}
\]

Let `m_+` and `m_-` be the midpoints of the `w` and `-w` sides. Starting the polygon
before the `a` side, (TF.11) gives

\[
m_+=a+{w\over2},
\]

\[
m_-=a+w+b-{w\over2}.
\]

Therefore

\[
\boxed{m_--m_+=b.}
\tag{TF.12}
\]

Let

\[
n_w=Jw
\]

be the positive normal to the `w` train direction. Its argument is `theta+pi/2`,
while `b` has argument `2pi/3`. Hence

\[
\angle(b,n_w)
=\left|{\pi\over6}-\theta\right|
< {\pi\over6},
\tag{TF.13}
\]

and

\[
b\cdot n_w
=\cos\left({\pi\over6}-\theta\right)
\ge {\sqrt3\over2}>0.
\tag{TF.14}
\]

The midpoint segment lies inside the convex pentagonal face and its interior is
disjoint from the contact graph. Thus it joins an incoming complement train end to
the opposite-oriented outgoing complement train end with exactly the canonical
through geometry.

For finite flowers converging to this pattern, compactness gives

\[
\angle(v_{conn},n_w)\le\pi/6+o(1),
\qquad
v_{conn}\cdot n_w\ge\sqrt3/2-o(1)>0,
\tag{TF.15}
\]

and the two complement train projective directions differ by `o(1)`.

---

## 7. All-orbit cases have the standard through pair

In Sections 2--4 all five side limits lie in the six-ray orbit. The closed five-ray
classification is elementary. If the signed excess in the three projective phases is
written against two triangular basis rays, closure forces the three phase totals to be
positive odd integers summing to five. Therefore their multiplicities are

\[
3,1,1.
\]

The phase of multiplicity three contains both ray signs. The usual midpoint
calculation for the cyclic five-ray pattern gives a connector equal to an adjacent
triangular ray, at angle exactly `pi/6` from the repeated-phase normal. Thus the
all-orbit flower also has a local through pair satisfying (TF.15).

This recovers locally the through-pair part of the independently developed dominant
pentagon splicing theorem; no global supertrain counting is imported here.

---

## 8. Allocation consequence

Call a full flower **locally through-selected** if one pair supplied by Sections 2--7
is chosen. If a flower has at least three side-terminal directions in the shrinking
dominant window, compactness and the classification above put it in one of those
cases. Therefore a flower which is not through-selected has at most two dominant
side-terminal occurrences and at least three complement occurrences.

If `C_D` is the total complement terminal-occurrence count over the `M_D` flowers,

\[
C_D\ge3(M_D-P_D)-o(D),
\]

which is exactly (TF.4)--(TF.5).

Because one complete stopped train has only two terminal occurrences, the number of
distinct complement trains terminating on non-through-selected flowers is at least

\[
{3\over2}(M_D-P_D)-o(D).
\tag{TF.16}
\]

In particular,

\[
P_D<{M_D\over2}
\quad\Longrightarrow\quad
N_{comp,flower}>{3M_D\over4}-o(D).
\tag{TF.17}
\]

At the current `t<=1.8623` full-flower floor `M_D>0.1327D-o(D)`, this gives the
concrete local dichotomy

```text
either >0.06635 D locally through-spliceable full flowers,
or     >0.099525 D distinct complement trains terminate on the remaining flowers.
```

The first alternative is stronger than the previous all-dominant-only count but now
contains complement-phase through pairs. Converting a linear family of such mixed
through pairs into one globally simple supertrain intersection graph is not proved
here and is the next obligation.

**Disposition:** proved proof-only atomic/local three-dominant through-pair normal
form and three-complement allocation law. C-II and Level I remain open.
