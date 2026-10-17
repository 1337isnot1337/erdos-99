> Generated reading edition · [exact source](../../research/target_c_centered_fan_blocker_closure_2026-10-05.md) · source SHA-256 `39b99086bde574ec0226830d7f3f1ce55c10e21fa5004f4887ec53eca7a33dc1`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — centered-fan blockers force a directed near-unit closure path

**Preservation scope (2026-10-15):** restored from source
`ba8197f5c4ade5dbb55f3c5f138597e47a30191a`, blob
`683e523a8aad8da73c04f75791521ccc566f1504`.
Sections 1–6 are superseded by the exact canonical path theorem in
[Audit 152](../docs/audits/target_c_centered_fan_blocker_closure_independent_audit_2026-10-08.md).
Section 7 and its Section 8 handoff remain conditional research. Face localization
is corrected to the prefix ending at the first core return or depth crossing.
No unpromoted fan-face/payment dependency or new canonical result is accepted.
The [source reconciliation](../docs/audits/fan_blocker_source_reconciliation_2026-10-15.md)
records all five historical commits, proof scope and remaining assumptions.

**Date:** 2026-10-05
**Base:** current main at `2026-10-05.audit.59` when this branch was created.
**Branch:** `research/target-c-fan-blocker-closure-20261005`
**Status:** proof-only research candidate; theorem-state authority unchanged.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note continues canonical `C-CENTERED-FAN-REFLECTIONS`. The canonical fan theorem proves that a degree-two fan leaf can be reflected inward by exactly $`1/D`$, preserving its two old unit contacts and decreasing every old upper distance, but a canonical source must contain a strict-pair lower blocker. The source report checks one- and two-isolate blocker chains computationally but does not prove a general repair theorem.

The new point here is that lower-blocker propagation is directed. If a blocker is translated together with the fan leaf, every new lower blocker lies strictly farther inward in the fan's diameter-normal coordinate. Up to a fixed macroscopic support depth this directionality also makes all upper constraints automatically safe. Therefore a canonical fan leaf cannot have a shallow closure consisting only of contact isolates.

The resulting finite alternative is

```math
\boxed{
\begin{array}{c}
\text{one canonical degree-two fan leaf}\\
\Longrightarrow\\
\text{a strict }(1,1+1/D]\text{ near-unit path reaches the positive-contact core,}\\
\text{or it contains }\Omega(D)\text{ distinct contact isolates and reaches depth }D/10.
\end{array}}
```

No population theorem forcing linearly many fan leaves is claimed here.

---

## 1. Exact fan coordinates

Let $`A`$ be a finite unit-separated planar source of diameter $`D\ge10`$. Let $`p`$ be a fan leaf satisfying the finite hypotheses of canonical `C-CENTERED-FAN-REFLECTIONS`: $`p`$ has a unique diameter partner $`a`$, exactly two unit-contact neighbors $`p_-,p_+`$, and

```math
|p-a|=|p_--a|=|p_+-a|=D,
\qquad
|p-p_-|=|p-p_+|=1.
\tag{1.1}
```

Put

```math
u={p-a\over D},\qquad \delta={1\over D},
\qquad p'=p-\delta u.
\tag{1.2}
```

Thus $`p'`$ is the canonical centered-fan reflection of $`p`$. Choose a unit vector $`t\perp u`$. The two fan neighbors have the exact coordinates

```math
p_\pm=p-{\delta\over2}u\pm\tau t,
\qquad
\tau=\sqrt{1-{\delta^2\over4}}.
\tag{1.3}
```

For every point $`x`$, define its inward support depth relative to the diameter support line at $`p`$ by

```math
s(x):=u\cdot(p-x).
\tag{1.4}
```

Since $`A\subset\overline B(a,D)`$, every source point satisfies $`s(x)\ge0`$.

---

## 2. A strict fan blocker is already at depth about $`\sqrt3/2`$

Call $`y\in A`$ a strict-pair blocker for $`p`$ if

```math
|p-y|>1,\qquad |p'-y|\le1.
\tag{2.1}
```

Canonical `C-CENTERED-FAN-REFLECTIONS` proves that every canonical fan leaf has such a blocker. Write

```math
y=p-su+vt,\qquad s=s(y).
\tag{2.2}
```

### Lemma 2.1 — exact blocker depth

Every strict-pair blocker satisfies

```math
\boxed{
s>
r_D:=
{ -\delta(1-\delta^2)
+\sqrt{12+5\delta^2-6\delta^4+\delta^6}\over4}
\ge {\sqrt3\over2}-{\delta\over4}.
}
\tag{2.3}
```

In particular,

```math
s>{\sqrt3\over2}-{1\over4D}.
\tag{2.4}
```

### Proof

The old and reflected pair conditions give

```math
s^2+v^2>1,
\qquad
(s-\delta)^2+v^2\le1.
\tag{2.5}
```

Source separation from the two fan neighbors gives

```math
(s-\delta/2)^2+(v\mp\tau)^2\ge1.
\tag{2.6}
```

Subtract the second inequality of (2.5) from the two inequalities (2.6). Because the former left side is at most one and the latter left sides are at least one,

```math
1+s\delta-\delta^2\mp2v\tau\ge0.
```

Hence

```math
|v|\le {1+s\delta-\delta^2\over2\tau}.
\tag{2.7}
```

Insert (2.7) into the strict old-distance inequality in (2.5):

```math
1
<
s^2+
{(1+s\delta-\delta^2)^2\over4(1-\delta^2/4)}.
```

After multiplication and cancellation,

```math
4s^2+2\delta(1-\delta^2)s-3-\delta^2+\delta^4>0.
\tag{2.8}
```

The constant term is negative and the quadratic coefficient is positive, so $`s`$ exceeds its positive root, which is $`r_D`$ in (2.3).

For $`0<\delta\le1`$,

```math
5\delta^2-6\delta^4+\delta^6
=\delta^2(1-\delta^2)(5-\delta^2)\ge0.
```

Therefore the square root in (2.3) is at least $`2\sqrt3`$, and

```math
r_D
\ge {\sqrt3\over2}-{\delta(1-\delta^2)\over4}
\ge {\sqrt3\over2}-{\delta\over4}.
```

This proves the claim. $`\square`$

---

## 3. Every lower blocker propagates strictly inward

Fix the common displacement

```math
\Delta=-\delta u.
\tag{3.1}
```

For distinct source points $`x,y`$, put $`d=|x-y|\ge1`$.  Write

```math
x\longrightarrow y
```

when holding $`y`$ fixed and translating $`x`$ by $`\Delta`$ would create
a lower obstruction, with the equality convention chosen so that no new unit
contact is allowed:

```math
\begin{cases}
|x+\Delta-y|\le1,&d>1,\\
|x+\Delta-y|<1,&d=1.
\end{cases}
\tag{3.2}
```

Thus an old strict noncontact is absorbed even when it would merely become a
new contact, while an old contact need only be absorbed if it would become
shorter than one.

### Lemma 3.1 — directed collision edge

If $`x\to y`$, then

```math
\boxed{1\le |x-y|\le1+\delta}
\tag{3.3}
```

and

```math
\boxed{
s(y)-s(x)=u\cdot(x-y)>{\delta\over2}.
}
\tag{3.4}
```

Consequently the directed lower-blocker graph is acyclic.

### Proof

The triangle inequality applied to (3.2) gives the upper bound in (3.3).
Put $`r=x-y`$.

If $`d>1`$, then

```math
0<|r|^2-1
\le |r|^2-|r-\delta u|^2
=2\delta\,u\cdot r-\delta^2.
```

If $`d=1`$, the strict translated violation gives directly

```math
0<1-|r-\delta u|^2
=2\delta\,u\cdot r-\delta^2.
```

In either case $`u\cdot r>\delta/2`$.  Since

```math
s(y)-s(x)=u\cdot(x-y)=u\cdot r,
```

(3.4) follows.  Depth strictly increases on every directed edge, so no
directed cycle exists. $`\square`$

There is also an exact accumulated-gap bound.  Along a directed path
$`x_0\to\cdots\to x_m`$, put $`d_j=|x_{j-1}-x_j|`$.  In both the contact
and strict-noncontact cases,

```math
d_j^2-1
\le
2\delta\,[s(x_j)-s(x_{j-1})]-\delta^2.
```

Since $`d_j+1\ge2`$,

```math
\boxed{
\sum_{j=1}^m(d_j-1)
\le
\delta\,s(x_m)-{m\delta^2\over2}.
}
\tag{3.5}
```

So a macroscopically long propagation path can carry only bounded total
strict gap excess above a unit chain.

## 4. A shallow translated isolate closure cannot create a diameter

Put

```math
H={D\over10}.
\tag{4.1}
```

### Lemma 4.1 — support-cap upper safety

Let $`x\in A`$ satisfy $`s(x)<H`$, and put $`x'=x-\delta u`$. For every $`y\in A`$, if

```math
|x'-y|>|x-y|,
\tag{4.2}
```

then

```math
\boxed{|x'-y|<D.}
\tag{4.3}
```

### Proof

From (4.2),

```math
-2\delta\,u\cdot(x-y)+\delta^2>0,
```

so

```math
s(y)-s(x)=u\cdot(x-y)<{\delta\over2}.
```

Hence

```math
s(y)<H+\delta/2,
\qquad
s(x')=s(x)+\delta<H+\delta.
\tag{4.4}
```

Also
```math
|x'-a|^2
=
|x-a|^2-2\delta\,u\cdot(x-a)+\delta^2
=
|x-a|^2-2\delta(D-s(x))+\delta^2
<
|x-a|^2
```
because $`s(x)<D/10`$ and $`D\ge10`$.  Hence $`x'\in\overline B(a,D)`$.
Both $`x'`$ and $`y`$ therefore lie in the circular support cap

```math
\mathcal C_h
=
\{z\in\overline B(a,D):u\cdot(p-z)\le h\},
\qquad h=H+\delta.
```

Write $`z=a+\xi u+w`$, $`w\perp u`$. Then $`\xi\in[D-h,D]`$ and

```math
|w|^2\le D^2-(D-h)^2=2Dh-h^2.
```

For any two points of the cap,

```math
|z-z'|^2
\le h^2+4(2Dh-h^2)
=8Dh-3h^2.
\tag{4.5}
```

For $`D\ge10`$,

```math
{h\over D}={1\over10}+{1\over D^2}\le {11\over100},
```

and

```math
8{11\over100}
-3\left({11\over100}\right)^2
<1.
```

Thus every two points of $`\mathcal C_h`$, in particular $`x'`$ and $`y`$, are at distance strictly less than $`D`$. $`\square`$

If a cross distance does not increase, it remains at most its old value and hence at most $`D`$. Thus translating any collection of points of depth $`<D/10`$ by the common vector $`-u/D`$ cannot create a new diameter.

---

## 5. Full lower-collision closure must penetrate macroscopically

Now assume $`A`$ is the canonical Target-C representative: first
contact-minimal among triangle-free global diameter minimizers, then
diameter-pair-minimal.

Start with

```math
R_0=\{p\}.
```

Given a current set $`R_j`$, if there are $`x\in R_j`$ and
$`y\in A\setminus R_j`$ with $`x\to y`$, add $`y`$.  Continue until either
some added vertex has support depth at least

```math
H=D/10
\tag{5.1}
```

or the set is successor-closed.  The source is finite, and Lemma 3.1 makes
the blocker relation acyclic, so the process terminates.

### Theorem 5.1 — centered-fan blocker closure reaches depth $`D/10`$

A successor-closed set containing $`p`$ cannot consist entirely of vertices
of depth $`<D/10`$.  Equivalently, every canonical centered fan leaf has a
directed path

```math
\boxed{
p=x_0\to x_1\to\cdots\to x_m
}
\tag{5.2}
```

whose first vertex at depth at least $`D/10`$ is $`x_m`$.

Every edge satisfies

```math
\boxed{
1\le|x_{j-1}-x_j|\le1+{1\over D},
\qquad
s(x_j)-s(x_{j-1})>{1\over2D}.
}
\tag{5.3}
```

The first edge is necessarily a strict old noncontact and hence

```math
\boxed{
1<|p-x_1|\le1+{1\over D},
\qquad
s(x_1)>{\sqrt3\over2}-{1\over4D}.
}
\tag{5.4}
```

### Proof

Suppose $`R`$ is successor-closed and every $`x\in R`$ has $`s(x)<D/10`$.
Translate every point of $`R`$ by

```math
\Delta=-u/D
```

and fix every point outside $`R`$.

**Lower constraints.**
Pairs with both endpoints moved or both endpoints fixed are unchanged.
For a crossing old strict noncontact, successor closure and definition
(3.2) give translated distance $`>1`$.  For a crossing old unit contact,
successor closure gives translated distance $`\ge1`$.  Thus the new source
is unit-separated.  No old strict noncontact becomes a new unit contact,
so the total number of unit contacts cannot increase.

**Upper constraints.**
Moving-moving and fixed-fixed distances are unchanged.  For a moving-fixed
pair whose distance increases, Lemma 4.1 makes the new distance strictly
less than $`D`$.  A nonincreasing moving-fixed distance remains at most its
old value.  Hence no new actual diameter pair is created.

The carrier $`a`$ is not in $`R`$, because

```math
s(a)=u\cdot(p-a)=D>D/10.
```

Therefore the old fan diameter $`pa`$ is a crossing pair and strictly
shortens:

```math
|p+\Delta-a|=D-{1\over D}<D.
```

The translated source has the same cardinality, diameter at most $`D`$,
no more unit contacts, no new diameter pairs, and has lost at least the
diameter pair $`pa`$.

If its diameter is $`<D`$, global diameter minimality fails.  If its diameter
is $`D`$ and the contact count decreased, contact minimality fails.  If the
contact count is unchanged, the source is another contact-minimal global
minimizer with strictly fewer diameter pairs, contradicting the secondary
normalization.  Thus no shallow successor-closed $`R`$ exists.

Tracing the parent edges by which the first depth-$`D/10`$ vertex entered the
closure gives (5.2)--(5.3).  The fan contacts $`pp_-`$ and $`pp_+`$ are
preserved exactly by the centered reflection, so neither is an outgoing
blocker from $`p`$.  Hence the first edge is a strict old noncontact, and
Lemma 2.1 gives (5.4). $`\square`$

---

## 6. Linear, almost-unit penetration

Let $`x_m`$ be the first path vertex with $`s(x_m)\ge D/10`$.  Its
predecessor has depth $`<D/10`$, while every edge has length at most
$`1+\delta`$.  Therefore

```math
s(x_m)<{D\over10}+1+{1\over D}.
\tag{6.1}
```

Also every depth increment is at most its edge length, so

```math
m(1+\delta)\ge {D\over10}.
```

For $`D\ge10`$,

```math
\boxed{m\ge D/11.}
\tag{6.2}
```

Thus **one** canonical centered fan leaf forces a source path with linearly
many distinct vertices penetrating a fixed positive fraction of the diameter.

Equation (3.5) and (6.1) give

```math
\boxed{
\sum_{j=1}^m\bigl(|x_{j-1}-x_j|-1\bigr)
<
{1\over10}+{1\over D}+{1\over D^2}.
}
\tag{6.3}
```

For $`D\ge10`$, every path edge has length at most $`1.1<\sqrt2`$.  The
straight-line graph on source pairs of length $`<\sqrt2`$ is plane, so this
directed path is embedded.  In particular the repair obstruction is not a
diffuse collection of almost-contacts: it contains a simple macroscopic
almost-unit source path with $`O(1)`$ total gap excess.

## 7. Nonbridge fan leaves localize the closure to one exceptional face

**Conditional section.** In addition to the fan hypotheses, supply a bounded
physical exceptional face whose interior sector at p lies between the two fan
contacts. The source cites an unpromoted fan-face/payment argument for this input;
that argument is absent from current main and is not established here. The bridge,
face-excess and return-currency applications below retain those additional
assumptions, as withheld by canonical Audit 152.


The propagation alternative localizes more strongly for the nonbridge fan
leaves already isolated in the October fan-payment work.  A bridge-adjacent
fan leaf must be kept as a separate outer-walk case.

Let both fan contacts $`pp_-`$ and $`pp_+`$ be nonbridges of the positive
contact graph.  The source's unpromoted degree-two fan-face claim would supply one bounded
physical exceptional face $`G(p)`$ whose boundary contains the consecutive
two-edge path

```math
p_--p-p_+.
\tag{7.1}
```

This is precisely the nonbridge scope of
\`target_c_degree2_fan_exceptional_face_payment_2026-10-02.md\`; it is not
asserted for a bridge-adjacent fan leaf.

### Lemma 7.1 — nonbridge face localization

Assume the stated bounded face is supplied and both fan contacts are nonbridges.
Take only the initial segment of the path in Theorem 5.1, stopping at its first
nonisolated vertex after p or its first depth-D/10 vertex, whichever comes first.
Every edge of this prefix lies in $`\overline{G(p)}`$, and its intermediate
contact-isolated vertices lie in $`\operatorname{int}G(p)`$. No later edge is
asserted to remain in that face.

### Proof

For $`D\ge10`$, every propagation edge has length at most

```math
1+1/D<\sqrt2.
```

Consider the straight-line graph on all source pairs of length $`<\sqrt2`$.
It is plane.  If two such edges with four distinct endpoints crossed properly,
their endpoints would form a convex quadrilateral.  Some quadrilateral angle
is at least $`\pi/2`$; the two source-side lengths at that angle are each at
least one, so the opposite diagonal has length at least $`\sqrt2`$, a
contradiction.  The unit-contact graph is a subgraph of this plane near-unit
graph.

The first propagation edge leaves $`p`$ through the interior sector between
the two consecutive contact edges $`pp_-`$ and $`pp_+`$.  In the nonbridge
scope that sector is exactly the bounded face $`G(p)`$, so the first edge
enters $`G(p)`$.

A later propagation edge cannot cross a contact edge.  A contact-isolated
source vertex cannot lie in the relative interior of a unit contact edge
either, because it would be at distance $`<1`$ from one endpoint.  Therefore
a propagation path whose intermediate vertices are contact-isolated cannot
leave $`G(p)`$ without first reaching a contact-graph vertex on
$`\partial G(p)`$.  Such a vertex is exactly the nonisolated terminal
alternative. $`\square`$

### Corollary 7.2 — nonbridge core crosscut or macroscopic exceptional face

Conditional on the supplied face and stated noncanonical face/payment hypotheses,
for a degree-two fan leaf whose two contacts are nonbridges, one of the following
holds for that prefix.

1. **Core crosscut.**  The initial segment specified in Lemma 7.1 joins $`p`$ to another nonisolated
   boundary vertex of $`G(p)`$, with every intermediate vertex
   contact-isolated and every path edge in $`(1,1+1/D]`$.

2. **Macroscopic face.**  The face $`G(p)`$ contains a path vertex $`x`$ with
   $`s(x)\ge D/10`$.  Since $`|p-x|\ge s(x)`$,

   
   ```math
   \operatorname{diam}G(p)\ge D/10.
   ```


   A closed polygonal curve has perimeter at least twice its diameter.  Every
   boundary edge of the physical contact face is a unit contact, so

   
   ```math
   \boxed{\deg G(p)=\operatorname{per}G(p)\ge D/5.}
   \tag{7.2}
   ```


In the second alternative this one face contributes

```math
\boxed{
Q-f\ge \deg G(p)-5\ge D/5-5
}
\tag{7.3}
```

to the canonical degree-$`\ge6`$ face-excess currency.

Canonical \`C-GLOBAL-FACE-RETURN-QUOTAS\` gives a full-boundary
endpoint-inclusive separator of size at least

```math
\left\lceil{\deg G(p)+2\over2}\right\rceil,
```

so the same macroscopic face carries at least

```math
\boxed{D/10-O(1)}
\tag{7.4}
```

units of actual loaded-return/separator capacity.  This is path-count
currency, not packing/refill capacity.

### Bridge-adjacent leaves remain a separate paid case

If at least one of $`pp_-`$, $`pp_+`$ is a bridge, Lemma 7.1 is not
available and no bounded-face localization is asserted. The unpromoted
fan-payment claim would charge such leaves to the loaded outer-walk excess:
if $`U_{\rm br}`$ is the number of degree-two fan leaves with a bridge-adjacent
fan contact, then

```math
\boxed{U_{\rm br}\le2x_B.}
\tag{7.5}
```

Thus a population-level use of Theorem 5.1 has the honest split

```math
\text{bridge fan leaves}\longrightarrow x_B,
```

while only the nonbridge population feeds the bounded-face CROSSCUT /
MACRO-FACE fork above.  This is consistent with the sharper existing
proof-only payment

```math
U\le2x_B+Q+4.
\tag{7.6}
```

No stronger replacement of that payment is claimed here.

---

## 8. Updated research handoff

Conditional on the Section 7 face and payment hypotheses, one nonbridge
degree-two fan leaf has the proposed prefix fork

```math
\boxed{
\begin{array}{ll}
\textbf{CROSSCUT:}&
\text{one bounded physical exceptional face contains a strict near-unit}\\
&\text{isolate path from the loaded fan leaf back to its contact boundary;}\\[1mm]
\textbf{MACRO-FACE:}&
\deg G(p)\ge D/5,\quad Q-f\ge D/5-5,\quad
\text{and }G(p)\text{ carries }\Omega(D)\text{ loaded-return capacity.}
\end{array}}
```

At population level there is a third, already-paid alternative

```math
\textbf{BRIDGE:}\qquad U_{\rm br}\le2x_B.
```

The MACRO-FACE and BRIDGE sides are expressed in currencies already present
in the current Target-C stack.  The genuinely new local object is the
CROSSCUT side.  A useful next theorem would be a finite exchange or
exact-contact argument for a near-unit isolate crosscut inside one convex
unit-contact face.  Audit.59 forbids replacing that task with a
strict-safe-area averaging argument, and no such inference is made here.


No theorem-state promotion is proposed here.
