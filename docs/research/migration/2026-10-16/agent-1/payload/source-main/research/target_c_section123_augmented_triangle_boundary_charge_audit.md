# Target C — hostile audit of Section 123 augmented-triangle boundary charge

**Date:** 2026-09-12  
**Artifact:** `research/target_c_section123_augmented_triangle_boundary_charge.md`  
**Verdict:** **PASS at proof-only scope, conditional on the already stated proof-only Section-121 identities.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The audit targets the two nontrivial steps: classifying augmented triangular faces and
proving that an internal attachment-cell base of length at most two is impossible in
the Type-II near-disk limit.

## 1. Triangle classification

The graph `J_r^+` contains internal/attachment contacts and the full polygon boundary
of `P_r`. A bounded triangular face cannot use zero polygon sides because the old
contact graph is triangle-free.

If it uses two polygon sides, the third edge joins the endpoints of a two-edge ear of
`P_r`. Unless `|A_r|=3`, those endpoints have an `A_r` vertex on one inherited global
boundary arc and another `A_r` vertex on the other, so they are nonconsecutive loaded
vertices of `F`. The third edge would be an old loaded-loaded unit contact, forbidden
by audited Section 122. If `|A_r|=3`, the triangle is the full polygon boundary; since
`I_r` is nonempty inside `P_r`, it is not a bounded face. The same observation rules
out three polygon sides.

Thus exactly one face side is an added polygon side `ab`. The other two sides are unit
contacts through a third vertex `x`. If `x` were loaded, audited Section 122 would make
both loaded contact edges global hull sides. The inherited cyclic order again forces
`A_r={a,x,b}`, making the triangle the cell boundary rather than a bounded face.
Therefore `x` is unloaded. The base satisfies `|ab|<=2`; equality `|ab|=1` would make
a unit contact triangle, so `1<|ab|<=2`.

This verifies Lemma 123.1.

## 2. Uniform short-arc control for every base of length at most two

The Section-122 annulus proof is uniform over all loaded pairs at distance at most two.
If

\[
B(0,r_D)\subset F_D\subset B(0,R_{+,D}),
\qquad r_D/R_{+,D}\to1,
\]

then every supporting normal differs from the local radial direction by at most

\[
\beta_D=\arccos(r_D/R_{+,D})=o(1).
\]

For `|a-b|<=2`, the endpoint radial separation is at most

\[
2\arcsin(1/r_D)=o(1).
\]

Hence every side direction on the short polar arc from `a` to `b` lies in an interval
of width `tau_D=o(1)`, uniformly over the choice of the triangular face.

## 3. An internal base violates source separation

If `a,b` are nonconsecutive globally, the short polar arc contains at least two hull
sides. Let it contain `j` sides. Projection onto the midpoint direction gives

\[
|a-b|\ge j\cos(\tau_D/2).
\]

Since `|a-b|<=2` and `tau_D->0`, eventually `j<=2`. Nonconsecutivity gives `j=2`.
Let `y` be the unique intermediate loaded vertex and let

\[
\ell_1=|a-y|,
\qquad \ell_2=|y-b|.
\]

The same projection estimate gives

\[
2\cos(\tau_D/2)\le|a-b|\le2
\]

and

\[
\ell_1+\ell_2\le {|a-b|\over\cos(\tau_D/2)}.
\]

Because `ell_1,ell_2>=1`, uniformly

\[
|a-b|\to2,
\qquad
\ell_1,\ell_2\to1.
\]

If `M=(a+b)/2`, the unloaded face vertex has

\[
|x-M|^2=1-|a-b|^2/4\to0.
\]

The intermediate loaded vertex satisfies the exact median identity

\[
|y-M|^2={\ell_1^2+\ell_2^2\over2}-{|a-b|^2\over4}\to0.
\]

Thus `|x-y|->0`, contradicting unit separation. No assumption about which side of the
chord contains `x` or `y` is needed. This closes a possible orientation regression in
the source proof.

Therefore every augmented triangular face is based on a nonunit global hull side.

## 4. Cross-cell injectivity

One polygon side borders at most one bounded face within a fixed augmented cell.
Across cells, if two two-dimensional convex cells both used the same global hull side,
then they would both lie in the same inward half-plane of its supporting line. Each
contains a positive-height triangle over every sufficiently small subsegment in the
relative interior of the shared side. Those two triangles overlap in positive area
near the side. This contradicts canonical Section-83 interior disjointness. Hence the
charge is globally injective and

\[
T:=\sum_rT_r\le m.
\]

## 5. Exact algebra check

Section 121 gives

\[
e_{BB}-k={1\over2}(a-T+Q^+)+d_{tile},
\qquad
d_{tile}=q-2-a+2c_I.
\]

Audited Section 122 and canonical Section 63 give

\[
e_{BB}=q-m=Q+2k+u_B.
\]

Direct substitution yields

\[
\begin{aligned}
Q^+
&=2(e_{BB}-k-d_{tile})-a+T\\
&=Q+u_B-(m-T)-2(c_I-1)-d_{tile}.
\end{aligned}
\]

In Type II the positive core has `Theta(D^2)` vertices while the loaded hull has only
`O(D)` vertices, so `c_I>=1` for all sufficiently large survivors. Since
`m-T>=0` and `d_tile>=0`,

\[
Q^+\le Q+u_B.
\]

Section 121's pointwise `P_exc,r<=5Q_r^+` then gives

\[
\sum_rP_{{\rm exc},r}\le5(Q+u_B)=5(e_{BB}-2k).
\]

No limsup/liminf interchange is used in this finite bound.

## 6. Composition check

Section 120 gives pointwise quantities whose normalized liminf obeys

\[
\liminf_D {\sum_r(L_r+P_{{\rm exc},r}-2d_r)\over D}
\ge {\pi\over2}(2-\sqrt3).
\]

Because `P_exc` is pointwise at most `5(Q+u_B)`, replacing it by that upper bound makes
the left side only larger. Hence the Section-123 two-currency inequality is valid.

## 7. Scope

- Section 123 is Type II only.
- It does not address the macroscopic-container branch.
- It depends on proof-only Section 121 and audited proof-only Section 122, so it is not
  canonical under audit.44.
- No source point is deleted and no full-source ZR/ZF statement appears.
- The theorem is structural but not a C-II contradiction.

**Audit verdict:** PASS at proof-only scope.
