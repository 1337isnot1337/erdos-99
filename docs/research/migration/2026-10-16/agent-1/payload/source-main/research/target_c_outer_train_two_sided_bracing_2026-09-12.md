# Target C — response-free two-sided diameter bracing of outer trains

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research theorem; theorem authority unchanged.  
**Base:** branch `research/cii-face-closure-rank-20260912`, after commit `890fcca4`.  
**Dependencies:** C65 full actual diameter visibility; relative-interior positive KKT stress; audited finite outer-to-outer train cut/shear primitive.

This note repairs the useful part of the old train-bracing idea without using any
response-conductance theorem. Every complete stopped train with both terminal
occurrences on the actual outer face is crossed by actual diameter pairs on **both**
transverse sides of the train direction.

The key finite fact is elementary: a diameter-bounded planar set contains at most one
diameter segment in any projective direction. If all first shear derivatives of
crossing diameter pairs vanished, that fact leaves a unique crossing diameter pair,
and the exact train shear strictly shortens it to second order while preserving every
old contact. Lexicographic minimality then gives the contradiction.

---

## 1. Parallel diameter segments are unique

### Lemma 1.1

Let `X` be a finite Euclidean set of diameter `D>0`. If two diameter pairs are
parallel, then they are the same unordered pair.

### Proof

Orient the two parallel diameter segments in the same direction and write

\[
b-a=Du,
\qquad
d-c=Du,
\qquad |u|=1.
\]

Put `v=c-a`. Since every distance in `X` is at most `D`, the two cross distances obey

\[
|b-c|=|Du-v|\le D,
\qquad
|d-a|=|Du+v|\le D.
\]

Squaring and adding gives

\[
2D^2+2|v|^2
=|Du-v|^2+|Du+v|^2
\le2D^2.
\]

Hence `v=0`, so `c=a` and `d=b`. `square`

No convexity or extremality hypothesis is used.

---

## 2. KKT cut resultant for one outer train

Let `tau` be a complete stopped train whose two terminal occurrences lie on the actual
outer face. Use the audited train primitive to choose its Jordan shore split

\[
V=S\sqcup T
\]

so that the contact cut is exactly the set `E(tau)` of parallel contact edges belonging
to the train.

Choose the unit vector `u` so every cut contact, oriented from `T` into `S`, has contact
vector `u`. Let the relative-interior KKT contact weights be `alpha_e>0` and the actual
diameter weights be `beta_h>0`. Put

\[
A_\tau:=\sum_{e\in E(\tau)}\alpha_e>0.
\]

Sum KKT equilibrium over all vertices in `S`. Internal contact and diameter forces
cancel. The remaining contact cut is `A_tau u`, so

\[
\boxed{
A_\tau u
=
\sum_{\substack{h=xy\in H\\x\in T,\ y\in S}}
\beta_h(p_y-p_x).
}
\tag{2.1}
\]

In particular at least one actual diameter edge crosses the train cut.

For each crossing diameter edge orient

\[
r_h:=p_y-p_x,
\qquad x\in T,\ y\in S,
\qquad |r_h|=D.
\]

Dot (2.1) with `Ju`:

\[
\boxed{
\sum_{h\pitchfork\tau}
\beta_h(r_h\cdot Ju)=0.
}
\tag{2.2}
\]

---

## 3. Both transverse signs are mandatory

### Theorem 3.1 — two-sided outer-train bracing

For every complete outer-to-outer stopped train `tau`, there are crossing actual
diameter pairs `h_+` and `h_-` such that

\[
\boxed{
r_{h_+}\cdot Ju>0,
\qquad
r_{h_-}\cdot Ju<0.
}
\tag{3.1}
\]

### Proof

Assume the crossing values `r_h dot Ju` do not contain both signs. Since every
`beta_h>0`, the zero weighted sum (2.2) forces

\[
r_h\cdot Ju=0
\qquad
\text{for every crossing diameter }h.
\tag{3.2}
\]

Thus every crossing diameter segment is parallel to `u`. By Lemma 1.1 there is only
one such unordered diameter pair. Equation (2.1) then has one term. Because its left
side is a positive multiple of `u`, the oriented crossing diameter vector must be

\[
r_h=Du.
\tag{3.3}
\]

Now use the exact finite one-train shear. Keep shore `T` fixed and translate shore `S`
by

\[
\Delta_\theta=R_\theta u-u.
\tag{3.4}
\]

The audited train primitive says this rotates every cut contact of `tau` through angle
`theta` while preserving its unit length, leaves every same-shore contact unchanged,
and preserves every old contact exactly. For sufficiently small `theta`, every strict
old noncontact remains strictly longer than one.

The unique crossing diameter pair changes from `Du` to

\[
Du+\Delta_\theta.
\]

Its squared length is exactly

\[
\begin{aligned}
|Du+\Delta_\theta|^2
&=D^2+2D(\cos\theta-1)+2(1-\cos\theta)\\
&=D^2-2(D-1)(1-\cos\theta).
\end{aligned}
\tag{3.5}
\]

For every sufficiently small nonzero `theta` and every C-II source with `D>1`, this
is strictly smaller than `D^2`.

All old diameter pairs lying within one shore are unchanged. There are no other old
diameter pairs crossing the train cut, by uniqueness above. Every pair that was
strictly shorter than `D` remains shorter than `D` for sufficiently small `theta` by
finite slack.

Therefore the sheared **full source** is unit-separated and has diameter at most `D`.
It has exactly the same cardinality and all old unit contacts are preserved. Two cases
remain.

1. If some same-shore diameter pair remains, the sheared source is another global
   diameter minimizer with the same unit-contact set but strictly fewer actual diameter
   pairs. This contradicts the secondary lexicographic normalization.
2. If no same-shore diameter pair remains, every old diameter pair has shortened and
   every old non-diameter pair stays below `D`; hence the new source has diameter
   strictly below `D`, contradicting global diameter minimality.

Thus (3.2) is impossible, proving (3.1). `square`

---

## 4. Immediate finite consequences

For every outer-to-outer train:

1. at least two distinct actual diameter edges cross its contact cut;
2. the crossing diameter set cannot be a star consisting of one edge repeated with
   multiplicity, because actual diameter pairs are simple unordered source pairs;
3. the train shear has active diameter first derivatives of both signs, so no one-sided
   first-order diameter descent exists along a single train coordinate; and
4. any aggregate train-shear descent must exploit correlations among several trains,
   not a missing one-train brace.

Together with the exceptional-face closure theorem on the same branch, if `L_OO` is the
number of outer-to-outer trains then

\[
L_{OO}\le h,
\]

and, when at least one bounded defect face exists,

\[
L_{OO}\le h-1.
\]

Theorem 3.1 strengthens this from a dimension count to a signed geometric statement
for every one of those trains.

---

## 5. Why this does not already close C-II

A single diameter edge may cross many train cuts. Hence `2L_OO` signed incidences do
not imply `2L_OO` distinct diameter edges. A convex diameter thrackle can reuse one
macroscopic chord across many nested cuts.

The next useful theorem must exploit one of:

- order of the outer train cuts versus the convex-thrackle diameter chords;
- the positive KKT weights in the vector resultants (2.1), not only their signs;
- simultaneous train shears, where a diameter edge accumulates contributions from every
  train cut it crosses; or
- the phase/corridor constraints on which train cuts can be nested.

Support incidence alone is known to be insufficient in the pure-tooth matrix endpoint.

---

## 6. Hostile audit and scope

- **Full source:** the finite shear moves one entire source shore; contact-isolated
  points are assigned to their geometric shore and are not discarded. No isolated
  coordinate is inserted into the Section-57 affine kernel.
- **Inactive constraints:** there are finitely many old noncontacts and nondiameter
  pairs. Their strict slacks persist for sufficiently small `theta`.
- **Exact contacts:** the finite train-shear primitive preserves every old contact,
  rather than only its first derivative.
- **Diameter orientation:** if the zero-transverse case has one crossing diameter,
  equation (2.1), not a sign convention, forces its oriented vector to be `+Du`.
- **Triangle-free comparison:** preserving all old contacts and not creating new
  contacts for sufficiently small `theta` preserves triangle-freeness.
- **Response theory:** unused. No response conductance, strict response defect, or
  KKT-weight lower bound appears.
- **Theorem authority:** unchanged; this is proof-only and depends on the audited
  outer-train shear primitive.

**Disposition:** exact proof-only structural theorem. It eliminates the unbraced and
one-projective-diameter outer-train cases, but C-II remains open.