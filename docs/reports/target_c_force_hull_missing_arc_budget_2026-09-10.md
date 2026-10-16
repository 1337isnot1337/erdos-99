<!-- theorem-state: {"artifact_id":"ART-A48489C667BC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_force_hull_missing_arc_budget_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ccb92ecc7d5319af4921e2c58c09e61a7f9622bb; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — diameter density controls force-hull missing arcs

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`  
**Run type:** structural compactness theorem / closing-proof continuation  
**Target:** Target C, C-II after ZF/FS/FSDB  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The FSDB force-hull area theorem uses the complete polygon of actual diameter
directions, while CAP/CQ use the asymptotic cyclic geometry of the force hull. These
two circle objects are not independent. The diameter-direction polygon lies inside the
force hull up to `o(D)`, and C67 gives `h` projective directions separated by
`1/D+o(1/D)`. Therefore any normalized force-hull limit must retain at least `y`
radians of the projective radius-`1/2` circle when `h/D->y`.

This gives a joint area/perimeter theorem. Put

\[
p_0(y):=y+2\cos(y/2),
\qquad
s(y):=\cos^3\left(\frac{\pi-y}{4}\right),
\qquad
\Phi(y):=\frac{y+\sin y}{4}.
\tag{MA.1}
\]

Then every convergent post-ZF survivor subsequence with

\[
\frac hD\to y,
\qquad
\frac{\operatorname{per}F}{D}\to p,
\qquad
\frac{\operatorname{area}F}{D^2}\to a
\]

satisfies

\[
\boxed{
p\ge p_0(y),}
\tag{MA.2}
\]

and

\[
\boxed{
a\ge\Phi(y)+s(y)\,[p-p_0(y)].}
\tag{MA.3}
\]

At `p=p_0(y)`, MA.3 is exactly the FSDB functional floor `a>=Phi(y)`. For every
larger perimeter it supplies a compulsory area increase with slope greater than
`3/4` throughout the post-ZF range.

---

## 1. Diameter directions occupy projective measure at least `y`

Let `U_D` be the set of the `h` actual diameter-edge directions on the projective
circle `T=R/(pi Z)`. C67 gives the cyclic separation

\[
\operatorname{dist}_T(u,u')\ge
\delta_D:=2\arcsin\frac1{2D}
\qquad(u\ne u').
\tag{1.1}
\]

Thus

\[
D\delta_D\to1.
\tag{1.2}
\]

Take a subsequence with `h/D->y` and, by compactness of the hyperspace of nonempty
compact subsets of `T`, pass further so that

\[
U_D\to U_\infty
\tag{1.3}
\]

in Hausdorff distance.

### Lemma MA.1

The one-dimensional Lebesgue measure on the projective circle satisfies

\[
\boxed{|U_\infty|\ge y.}
\tag{1.4}
\]

### Proof

Around every point of `U_D`, place the closed projective arc of radius `delta_D/2`.
The interiors of these arcs are pairwise disjoint by (1.1), so their union has total
length

\[
h\delta_D\to y.
\tag{1.5}
\]

Fix `epsilon>0`. By Hausdorff convergence, for all sufficiently large `D` every center
in `U_D` lies within `epsilon/2` of `U_infty`; also `delta_D/2<epsilon/2`. Hence the
entire union of separation arcs lies in the `epsilon`-neighborhood
`(U_infty)_epsilon`. Therefore

\[
|(U_\infty)_\epsilon|\ge y-o(1).
\]

Let `D->infinity`, then `epsilon downarrow0`. Since `U_infty` is compact, continuity
from above of Lebesgue measure gives (1.4). `square`

---

## 2. The diameter circle set lies in the force-hull circle set

Translate the actual force hull by the full-source circumcenter and normalize:

\[
K_D:=D^{-1}(F-o).
\tag{2.1}
\]

Pass to a Hausdorff limit

\[
K_D\to K_\infty.
\tag{2.2}
\]

FS.1/FS.4 imply that `K_infty` is centrally symmetric, lies in the radius-`1/2`
disk, and every extreme point lies on its boundary circle.

Let

\[
P_D:=\frac{1}{2D}P_H
=\operatorname{conv}\{\pm u/2:u\in U_D\},
\tag{2.3}
\]

where `P_H` is the complete diameter-direction polygon from DB/FSDB. The FSDB
symmetry conversion gives

\[
P_D\subseteq K_D+o(1)B_2.
\tag{2.4}
\]

Using (1.3) and passing to the limit,

\[
\operatorname{conv}\{\pm u/2:u\in U_\infty\}
\subseteq K_\infty.
\tag{2.5}
\]

Every point `u/2` on the left has radius exactly `1/2`, while `K_infty` is contained
in the radius-`1/2` disk. Hence these circle points themselves belong to the circle
extreme set of `K_infty`.

Let `S_infty subset T` be the projective set of directions `theta` for which the
radius-`1/2` circle point in direction `theta` belongs to `K_infty`. Then

\[
U_\infty\subseteq S_\infty.
\tag{2.6}
\]

By Lemma MA.1,

\[
\boxed{|S_\infty|\ge y.}
\tag{2.7}
\]

Equivalently, if the complementary open projective arcs have lengths

\[
\alpha_1,\alpha_2,\ldots,
\]

then

\[
\boxed{
X:=\sum_i\alpha_i
=\pi-|S_\infty|
\le\pi-y.
}
\tag{2.8}
\]

This is the missing-arc budget.

---

## 3. Exact perimeter and area from missing arcs

For any centrally symmetric convex hull of a closed subset of the radius-`1/2` circle,
with complementary projective gaps `alpha_i`, the disk formulas are

\[
\boxed{
p
=\pi-
\sum_i\left(\alpha_i-2\sin\frac{\alpha_i}{2}\right),}
\tag{3.1}
\]

\[
\boxed{
a
=\frac\pi4-
\frac14\sum_i(\alpha_i-\sin\alpha_i).}
\tag{3.2}
\]

For finitely many gaps these follow by replacing the two antipodal missing circle arcs
by their chords. Countably many gaps follow by monotone finite approximation; the
summands are nonnegative and bounded by the total missing angle.

Put

\[
M:=\pi-y.
\tag{3.3}
\]

The one-gap body with missing angle exactly `M` has

\[
P_0
=\pi-M+2\sin(M/2)
=y+2\cos(y/2)
=p_0(y),
\tag{3.4}
\]

and

\[
A_0
=\frac\pi4-\frac{M-\sin M}{4}
=\frac{y+\sin y}{4}
=\Phi(y).
\tag{3.5}
\]

The missing-arc budget says every actual limit body is obtained from this one-gap
extremal by first shrinking total missing angle from `M` to some `X<=M`, then splitting
the remaining missing interval into the gaps `alpha_i`.

---

## 4. Every shrink or split has a controlled area/perimeter slope

### Lemma MA.2 — shrinking a gap

For a single missing gap of length `x<=M`, infinitesimally shrinking the gap increases
area and perimeter in ratio

\[
\boxed{
\frac{dA}{dP}=\cos^2(x/4)
\ge\cos^2(M/4).
}
\tag{4.1}
\]

### Proof

For one gap,

\[
P(x)=\pi-x+2\sin(x/2),
\qquad
A(x)=\frac\pi4-\frac{x-\sin x}{4}.
\]

Both derivatives are negative, and

\[
\frac{A'(x)}{P'(x)}
=
\frac{1-\cos x}{4(1-\cos(x/2))}
=\frac{1+\cos(x/2)}2
=\cos^2(x/4).
\]

`circle`

### Lemma MA.3 — splitting a gap

Split a missing gap `x=a+b` into two missing gaps `a,b>0`, without changing their
total angle. Let `Delta P` and `Delta A` be the resulting increases in perimeter and
area. Then

\[
\boxed{
\frac{\Delta A}{\Delta P}
=
\cos\frac{a+b}{4}
\cos\frac a4
\cos\frac b4
\ge
\cos^3(M/4).
}
\tag{4.2}
\]

### Proof

Directly from (3.1)--(3.2),

\[
\Delta P
=2\left[
\sin(a/2)+\sin(b/2)-\sin((a+b)/2)
\right],
\]

and

\[
\Delta A
=\frac{
\sin a+\sin b-\sin(a+b)
}{4}.
\]

Put `s=(a+b)/2` and `d=(a-b)/2`. The standard sum-to-product identities reduce the
quotient to

\[
\frac{\Delta A}{\Delta P}
=
\cos(s/2)\cos(a/4)\cos(b/4).
\]

Since `a,b,a+b<=M` and cosine decreases on `[0,pi/4]`, every factor is at least
`cos(M/4)`. This proves (4.2). `square`

---

## 5. Joint force-hull capacity theorem

Starting from the one-gap body of angle `M`, shrink it to the actual total missing
angle `X`, then split it finitely into the actual gaps. Lemma MA.2 gives slope at least
`cos^2(M/4)`, which is at least `cos^3(M/4)`; every split has slope at least the latter
by Lemma MA.3. Therefore the total changes satisfy

\[
a-\Phi(y)
\ge
\cos^3(M/4)\,[p-p_0(y)].
\tag{5.1}
\]

Countably many complementary gaps follow by finite approximation. This is MA.3, and in
particular the right side is nonnegative, proving MA.2. `square`

For the post-ZF range `y>=2rho`, the slope has the uniform bound

\[
\boxed{
s(y)>\frac34.}
\tag{5.2}
\]

Indeed `rho>739/1000`, `pi<22/7`, so

\[
\frac{\pi-y}{4}
\le\frac{\pi-2\rho}{4}<\frac5{12}.
\]

Using `cos x>=1-x^2/2`,

\[
\cos\frac{\pi-y}{4}
>
1-\frac{25}{288}
=\frac{263}{288},
\]

and `(263/288)^3>3/4`.

---

## 6. Scope and decisive use of the full source

MA is source-specific in exactly two places:

1. FS.1/FS.4 derive the common radius circle and asymptotic reflection symmetry from
the **entire globally optimal source**, retaining contact-isolated points.
2. The complete actual diameter support of the lexicographic C-II representative, plus
C67 separation, supplies the projective measure `y` which the force-hull circle set
must retain.

The regular odd shell satisfies MA essentially at equality in the one-gap-free disk
limit `y->pi`; it is not a counterexample. Dense isolated fillings also retain MA but
lack the global-optimality certificate required to be a C-II source.

No response-operator norm, conductance floor, matching-weight theorem, or local
near-equilateral gap is used.

---

## 7. Exact target implication

The previous CAP/CQ route used independent lower bounds on area from diameter density
and perimeter. MA couples them:

\[
\boxed{
A(y,p):=
\Phi(y)+s(y)[p-p_0(y)]
}
\]

is a single lower surface valid on

\[
y\ge2\rho,
\qquad
p\ge p_0(y).
\]

Because `s(y)>3/4`, increasing force-hull perimeter gives less extra JC cavity capacity
than the compulsory force-hull area it creates. This makes the smallest permitted
perimeter `p_0(y)` the favorable case for a hypothetical survivor. The exact resulting
pinned/contact threshold is derived in the next report.

---

## 8. Promotion recommendation

**Hold as report pending joint FS/DB audit.** The missing-arc measure lemma and the
shrink/split slope calculation are exact. If the adjacent JC optimization survives
review, MA should supersede the weaker standalone CAP/CQ perimeter bounds for the
post-ZF closing route.
