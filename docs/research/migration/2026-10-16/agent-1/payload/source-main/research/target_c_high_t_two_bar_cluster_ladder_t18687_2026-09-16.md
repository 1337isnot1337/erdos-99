# Target C-II — the high-`t` joint cusp localizes every genuine two-bar reaction inside the macroscopic ladder

**Date:** 2026-09-16
**Status:** proof-only high-`t` structural strengthening
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`
**Dependencies:** high-`t` rectangle joint cusp; common-transversal/rooted-shore sign theorem; adjacent-strip reaction nondegeneracy; one/two-bar tangent certificate; two-bar geometry/localization theorem
**Certificate:** `research/verify_target_c_high_t_two_bar_cluster_ladder_t18687.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The high-`t` joint-cusp theorem puts one bounded-complexity nonhub strip inside a common ordered transverse ladder of more than `0.0783D-o(D)` trains. Its two boundary rows have real phase gap

\[
|\alpha_{i+1}-\alpha_i|
< {7.08\times10^6\over D}+o(D^{-1}).
\tag{HL.1}
\]

The remaining sign issue can now be removed on this **same** strip. A common oriented transverse train fixes the Euclidean signs of the rooted shore vectors, so the physical contact-opening cone has width exactly the real row-phase gap. Therefore the generic two-bar KKT reaction branch is spatially localized at absolute `O(1)` scale while it remains embedded in the macroscopic ladder.

More precisely, for the joint-cusp strip one has the following dichotomy.

### HL1 — one-bar tangent obstruction

One actual switching diameter bar alone blocks every first-order direction that opens both boundary contact families.

### HL2 — genuine two-bar reaction obstruction

If no single switching diameter bar is already a tangent certificate, then the exact nonzero layer reaction admits a positive representation by two actual switching diameter bars `h_1,h_2`, and this pair is automatically a minimal two-bar tangent certificate. If `eta` is their projective direction gap, then

\[
\boxed{
\eta < {7.08\times10^6\over D}+o(D^{-1}).
}
\tag{HL.2}
\]

After orienting the two unordered diameter segments to realize `eta`, write

\[
y_j-x_j=Dv_j,\qquad j=1,2,
\qquad \angle(v_1,v_2)=\eta.
\]

Then

\[
\boxed{
|x_2-x_1|<7.08\times10^6+o(1),
\qquad
|y_2-y_1|<7.08\times10^6+o(1).
}
\tag{HL.3}
\]

Both bars belong to the one-sided switching family toward the common diameter-routing hub. Simultaneously, the strip retains the ordered common transverse family

\[
\boxed{|B_0|>0.0783D-o(D),}
\tag{HL.4}
\]

and every `b in B_0` crosses both boundary rows with angular excess less than

\[
{1.416\times10^7\over D}+o(D^{-1}).
\tag{HL.5}
\]

Thus the live high-`t` TB2 obstruction is no longer an arbitrary pair of diameter chords: it is a pair of almost parallel diameter chords whose corresponding endpoints occupy two uniformly bounded clusters, with a linear ordered near-triangular ladder running through the same adjacent strip.

---

## 1. Use a common column to fix the rooted-shore signs

Take the nonhub adjacent pair `tau_i,tau_{i+1}` supplied by the high-`t` rectangle joint-cusp theorem. That theorem supplies a nonempty family `B_0` for all sufficiently large `D`, because

\[
|B_0|>0.0783D-o(D).
\]

Choose one oriented column train `gamma in B_0`. It crosses `tau_i` and `tau_{i+1}` in the common oriented rectangle branch. The two row-column angular excesses are `O(D^{-1})` by the joint-cusp theorem, so these crossings lie in the same phase-pure Section-76 regime for sufficiently large `D`.

Root the two-cut complement path at the region containing the incoming end of the oriented centerline of `gamma`. The common-transversal/rooted-shore sign theorem applies: if `v_i,v_{i+1}` are the oriented row unit vectors from the real rectangle lift and `u_i,u_{i+1}` are the Section-157 rooted-shore vectors, then

\[
\boxed{u_i=v_i,\qquad u_{i+1}=v_{i+1}.}
\tag{HL.6}
\]

This is the required Euclidean statement. Projective closeness alone would not be enough.

For the physical layer between the consecutive nested cuts, orient both boundary contact vectors from the fixed exterior into the middle layer. The adjacent-strip convention gives

\[
\boxed{a=u_i,\qquad b=-u_{i+1}.}
\tag{HL.7}
\]

The real arguments of `u_i,u_{i+1}` are exactly `alpha_i,alpha_{i+1}` from the joint-cusp theorem. Since their difference is `o(1)`, for large `D`

\[
\angle(a,b)=\pi-|\alpha_{i+1}-\alpha_i|.
\tag{HL.8}
\]

The unit tangent directions opening both boundary contact families are

\[
\Omega=\{w\in S^1:a\cdot w\ge0,\ b\cdot w\ge0\}.
\]

Therefore its angular width is

\[
\boxed{
\varepsilon
=\pi-\angle(a,b)
=|\alpha_{i+1}-\alpha_i|.
}
\tag{HL.9}
\]

Combining (HL.1) and (HL.9),

\[
\boxed{
\varepsilon < {7.08\times10^6\over D}+o(D^{-1}).
}
\tag{HL.10}
\]

---

## 2. The exact nonzero reaction reduces the obstruction to one or two actual bars

The selected interface is nonhub. The joint-cusp theorem therefore gives one-sided switching toward the common hub and switching KKT mass

\[
B_i<{1{,}109{,}000\over D}.
\tag{HL.11}
\]

Reaction nondegeneracy gives

\[
G=Aa+Bb
=\sum_{h\in H_{sw}}\beta_h n_h
\ne0,
\qquad A,B>0,
\tag{HL.12}
\]

where `n_h` is the inward vector of the actual switching diameter bar `h`, with `|n_h|=D`.

Planar conic Caratheodory gives a positive representation of `G` using one or two actual switching bars. If a one-bar representation exists, that bar is itself a tangent obstruction because for every `w in Omega`,

\[
\lambda n_h\cdot w
=G\cdot w
=A(a\cdot w)+B(b\cdot w)\ge0.
\]

This lies in branch HL1.

Suppose instead that a two-bar representation is used,

\[
G=\lambda_1n_1+\lambda_2n_2,
\qquad \lambda_1,\lambda_2>0.
\tag{HL.13}
\]

The same identity shows that `{h_1,h_2}` is a tangent certificate. If either selected bar alone were a tangent certificate, branch HL1 would again hold. Hence, under the hypothesis defining the genuine HL2 branch, the pair in (HL.13) is a **minimal** two-bar tangent certificate.

Thus every source is in HL1 or admits a reaction-generating minimal pair in HL2. No independent Helly pair needs to be chosen.

---

## 3. The genuine two-bar reaction is projectively inverse-diameter close

Apply the audited two-bar geometry theorem to the minimal pair `n_1,n_2`. If `eta` is their projective angular separation, then

\[
\eta\le\varepsilon.
\tag{HL.14}
\]

Equation (HL.10) immediately gives

\[
\eta<{7.08\times10^6\over D}+o(D^{-1}),
\]

which is (HL.2).

This conclusion is stronger than merely finding some two-bar tangent obstruction: the pair can be chosen to generate the **exact KKT layer reaction** and is drawn from the same one-sided switching set.

---

## 4. Quantitative diameter uniqueness gives two bounded endpoint clusters

Orient the two unordered diameter segments so their unit directions `v_1,v_2` realize the projective gap `eta`. The quantitative parallel-diameter lemma gives

\[
|x_2-x_1|,\ |y_2-y_1|
\le2D\sin(\eta/2)
\le D\eta.
\tag{HL.15}
\]

Use (HL.2):

\[
D\eta<7.08\times10^6+o(1).
\]

This proves (HL.3).

The conclusion is absolute-scale localization: as `D` tends to infinity, one corresponding endpoint pair remains within a fixed-radius cluster and the other corresponding endpoint pair remains within another fixed-radius cluster approximately distance `D` away.

---

## 5. The localization occurs inside the same macroscopic ordered ladder

Nothing in Sections 1--4 changes the adjacent pair selected by the joint-cusp theorem. Therefore all of its simultaneous structure survives:

```text
>0.0783 D common transverse trains in one common order
+ both row-column angle excesses < 1.416e7/D + o(1/D)
+ physical opening-cone width < 7.08e6/D + o(1/D)
+ <=1,108,999 switching diameter rows
+ switching KKT mass < 1,109,000/D
+ <=1,108,999 train-terminal occurrences
+ <=221,799 bounded exceptional faces
+ every switch one-sided toward the common hub
+ exact nonzero reaction generated by <=2 actual switching bars
+ if no one-bar certificate exists, the reaction pair is almost parallel
  and its corresponding endpoints lie in two O(1) clusters.
```

This is a sharper local target than the previous high-`t` joint cusp. The unresolved geometry is now an explicit fork:

1. **HL1:** eliminate a single one-sided diameter chord whose inward normal lies in the dual of an inverse-`D` opening cone; or
2. **HL2:** eliminate/exploit two nearly parallel one-sided diameter chords with bounded endpoint clusters while a linear ordered transverse ladder crosses the same strip.

A closure argument can now use the ladder and the endpoint clusters simultaneously rather than treating the sparse reaction and the rectangle as separate structures.

---

## 6. Scope audit

- No claim is made that every switching diameter edge is nearly parallel. The conclusion applies to the reaction-generating minimal pair in branch HL2.
- No endpoint-cluster conclusion is asserted in branch HL1.
- Bounded cluster diameter does not by itself bound the number of source vertices without an enclosing-area argument.
- The `7.08e6` constant is deliberately inherited from the already-certified joint-cusp phase-gap bound; no optimization of this constant is claimed.
- The result is proof-only and does not close C-II or Level I.

**Disposition:** proved a high-`t` one-bar / localized reaction-pair dichotomy on the same macroscopic ordered ladder through `t<=1.8687`. C-II and Level I remain open.
