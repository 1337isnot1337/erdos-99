# Hostile audit — bounded-face phase mixing capacity

**Date:** 2026-09-12  
**Audited source:** `target_c_bounded_face_phase_mixing_capacity_2026-09-12.md`  
**Disposition:** PASS at the stated proof-only scope; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This audit checks the finite endpoint-count inequality and its directional crossing
corollary. It does not promote the phase-mixing candidate and does not supply the
missing lower bound on the number of crossings.

## 1. Exact pair accounting

For disjoint train families `A,B`, every ordered pair `(tau,sigma)` is either a
strict-rhombus crossing pair or a noncrossing pair. Since the families are disjoint,
there is no diagonal ambiguity, so

`|A||B| = X(A,B)+N(A,B)`

is exact. A pair incident with one bounded face `F` from each family cannot cross by
the audited bounded-face fan lemma. Thus each of the `a_F b_F` pairs is a missing
crossing.

If one pair were charged at two distinct bounded faces, both trains would have a
terminal occurrence on both faces. The audited bounded-face endpoint-simplicity lemma
excludes this. The no-bounded-loop input ensures that a single train does not create a
second terminal occurrence on the same face. Therefore the face-charged pair sets are
disjoint and

`sum_F a_F b_F <= N(A,B)`

holds with occurrence-counted endpoint populations.

## 2. Directional area conversion

For a strict-rhombus crossing with angle `alpha`, the rhombus area is `sin(alpha)`.
If all selected crossings lie in a window `I`, then

`area(selected crossings) <= sup_{alpha in I} sin(alpha) * X(A,B)`,

which gives the stated lower bound for `X(A,B)`. In the shrinking-window version,
`sup sin(alpha) <= 1`, so the weaker displayed estimate `X >= (1-o(1)) area` is
valid; no erroneous unit-area normalization is needed.

The argument charges only actual selected A--B crossing faces. It does not claim that
all strict rhombi, or all train intersections, belong to the chosen directional
window.

## 3. Asymptotic interpretation

Under an independent near-complete crossing hypothesis
`X(A,B) >= |A||B|-o(D^2)`, the exact inequality gives
`sum_F a_F b_F=o(D^2)`. A face carrying linear populations from both families would
contribute a fixed positive multiple of `D^2`, so such a face is excluded. This is a
valid phase-purity consequence, not a statement that the whole bounded-face endpoint
population is small.

## 4. Scope limitations

The result does not control outer-face endpoints, mixed outer/bounded pairs, or
universal crossing completeness. It also does not turn phase purity into a diameter
descent or a strict source improvement. The missing-crossing budget may still be
absorbed by outer-face repetitions and multi-grain phase structure.

Contact-isolated source points are not used or deleted. No full-source affine-kernel
extension is invoked.

**Final audit verdict:** PASS as a finite bounded-face phase-mixing capacity lemma;
C-II remains open.
