# Target C-II — every isolate-hosting bounded contact face has degree at least seven

**Date:** 2026-09-15  
**Status:** proof-only exact local/source-level strengthening  
**Scope:** canonical triangle-free contact-minimal source; bounded nonquadrilateral contact faces  
**Dependencies:** canonical Section 67 convexity of bounded nonquadrilateral contact faces; unit separation  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Canonical Section 67 makes every bounded nonquadrilateral contact face a convex polygon whose boundary sides are actual unit contacts.  Such a face cannot contain a contact-isolated source point unless it has at least seven sides.

This is stronger than the high-`t` pentagon population theorem needs: **both pentagonal and hexagonal bounded contact faces have zero interior isolate population.**  Consequently every contact-isolate assigned to a bounded exceptional face is concentrated in degree-`>=7` faces.

## 1. Local angle lemma

Let

\[
P=(v_1,\ldots,v_d)
\]

be one canonical bounded nonquadrilateral contact face, in cyclic order.  Thus `P` is convex and

\[
|v_{i+1}-v_i|=1
\]

for every `i` modulo `d`.

Suppose a contact-isolated source point `z` lies in `int P`.  Put

\[
r_i:=|v_i-z|.
\]

Because the full source is unit-separated,

\[
r_i\ge1.
\]

Because `z` is contact-isolated and each `v_i` is another source point, equality is impossible:

\[
\boxed{r_i>1\qquad(1\le i\le d).}
\tag{IF.1}
\]

Let `theta_i` be the smaller angle at `z` from `v_i-z` to `v_{i+1}-z` in the cyclic order around the convex polygon.  Since `z` is in the interior of a convex polygon,

\[
0<\theta_i<\pi,
\qquad
\sum_{i=1}^d\theta_i=2\pi.
\tag{IF.2}
\]

Apply the cosine rule to the unit side `v_iv_{i+1}`:

\[
1=r_i^2+r_{i+1}^2-2r_ir_{i+1}\cos\theta_i.
\]

Hence

\[
\cos\theta_i
={r_i^2+r_{i+1}^2-1\over2r_ir_{i+1}}.
\tag{IF.3}
\]

Now

\[
r_i^2-r_ir_{i+1}+r_{i+1}^2
=(r_i-r_{i+1})^2+r_ir_{i+1}>1,
\tag{IF.4}
\]

where strictness uses `r_i r_{i+1}>1`.  Equation (IF.4) is exactly

\[
r_i^2+r_{i+1}^2-1>r_ir_{i+1}.
\]

Substituting in (IF.3) gives

\[
\boxed{\cos\theta_i>{1\over2},\qquad\theta_i<{\pi\over3}.}
\tag{IF.5}
\]

Summing (IF.5) and using (IF.2),

\[
2\pi=\sum_i\theta_i<d{\pi\over3}.
\]

Therefore

\[
\boxed{d>6.}
\tag{IF.6}
\]

Since `d` is an integer:

### Theorem IF — isolate-host face degree

If a bounded canonical contact face contains a contact-isolated source point in its interior, then

\[
\boxed{d\ge7.}
\tag{IF.7}
\]

In particular, if `z_P` denotes the assigned contact-isolate population of a bounded exceptional face `P`, then

\[
\boxed{\deg P\in\{5,6\}\Longrightarrow z_P=0.}
\tag{IF.8}
\]

No asymptotic argument, KKT multiplier estimate, or triangle-free angle gap is used after canonical face convexity is supplied.

## 2. Defect-budget consequence

Let `f_d` be the number of bounded exceptional faces of degree `d`,

\[
f=\sum_{d\ge5}f_d,
\qquad
Q=\sum_{d\ge5}(d-4)f_d.
\]

Then

\[
Q-f=\sum_{d\ge6}(d-5)f_d.
\tag{IF.9}
\]

Every face that can contain an assigned contact-isolate has `d>=7`, and therefore contributes at least two units to the right side of (IF.9).  If

\[
f_{iso}:=\#\{P:z_P>0\},
\]

then finitely

\[
\boxed{f_{iso}\le {Q-f\over2}.}
\tag{IF.10}
\]

This is a host-count statement, not an isolate-count statement: a single degree-`>=7` face may contain many assigned isolates.

## 3. Modern high-`t` consequence

The current modern high-`t` pentagon theorem gives, in the remaining full-core/no-macroscopic-container Type-II branch, the certified endpoint bounds

\[
\begin{array}{c|c|c|c}
T & f/D\text{ lower} & Q/D\text{ upper} & P_5/D\text{ lower}\\ \hline
1.850 & 0.4007088 & 0.558408 & 0.243\\
1.855 & 0.3982088 & 0.568408 & 0.228\\
1.860 & 0.3957088 & 0.578408 & 0.213.
\end{array}
\tag{IF.11}
\]

Combining (IF.10) with the same certified `f,Q` bounds gives the safe host-count staircase

\[
\boxed{
t\le1.850\Longrightarrow f_{iso}<0.07886D+o(D),}
\tag{IF.12}
\]

\[
\boxed{
t\le1.855\Longrightarrow f_{iso}<0.08510D+o(D),}
\tag{IF.13}
\]

\[
\boxed{
t\le1.860\Longrightarrow f_{iso}<0.09136D+o(D).}
\tag{IF.14}
\]

At the same time every one of the linearly many pentagons from the high-`t` theorem is isolate-free.  For example, throughout `t<=1.855`,

\[
\boxed{P_5>0.228D-o(D)\quad\text{and all of those pentagonal chambers have }z_P=0.}
\tag{IF.15}
\]

Thus the high-`t` exceptional-face system splits sharply:

```text
linear isolate-free degree-5 population
+ isolate-free degree-6 population
+ all bounded-face isolate mass concentrated in <0.09136 D+o(D)
  degree->=7 host faces (through t<=1.860).
```

This does not bound the number of isolates per high-degree host.  It does, however, remove pentagons and hexagons completely from the inactive-isolate storage problem.

## 4. Why this is useful but not yet closure

The modern high-`t` theorem forces a linear pentagon population and large exceptional-face Oler surplus.  The present theorem says that none of those pentagons can store the inactive points that appear in that Oler ledger.  Any surviving source must separate two roles:

1. the abundant degree-5 defect cells carry interface/area currency but no isolates;
2. the much smaller degree-`>=7` subfamily carries all bounded-face isolate population.

A closing argument can now target that concentration: combine the total isolate mass or protected-packing saturation with (IF.10), or couple the isolate-free pentagon sea to the live high-`t` O--O path/hub system.

No upper bound on isolate multiplicity in one degree-`>=7` face is claimed here, and no exact unit triangle or strict sub-`D` competitor follows from (IF.7) alone.

**Disposition:** proved exact local degree-`>=7` obstruction for isolate-hosting bounded contact faces, with a quantitative high-`t` host-count consequence. C-II and Level I remain open.
