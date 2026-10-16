# Hostile audit — Type-I safe-area saturation barrier

**Date:** 2026-09-12  
**Audited source:** `research/target_c_typeI_safe_area_saturation_barrier.md`  
**Verdict:** PASS at proof-only scope.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Abstract lattice contradiction

Assume a strict-safe region `S` has area `>a0 z`. Because the inequality is strict,
choose a lattice scale `lambda>1` sufficiently close to one that

\[
 area(S)/(a_0\lambda^2)>z.
\]

Translation averaging for the scaled triangular lattice gives a translate with at
least `z+1` points in `S`. Distinct selected points have distance at least
`lambda>1`.

Delete all `z` assigned contact isolates and one nonisolated positive-contact vertex
`v`, and insert exactly `z+1` selected lattice points. The deleted isolate set has no
unit contacts. Every new-old and new-new distance is strictly above one, so no new unit
contact is created. At least one old unit contact incident to `v` is removed.

All new points lie in `int K`, hence the new diameter is at most `D`. If it is smaller,
global diameter minimality is contradicted directly. If it equals `D`, the new source
is another global minimizer with strictly fewer contacts, contradicting the canonical
lexicographic contact-minimal normalization.

The post-ZF/Type-I setting has a nonisolated positive contact core, so a suitable `v`
exists. No loadedness of `v` is required.

**Verdict:** the abstract area ceiling is valid.

## 2. Strict internal wall shield

Replace the weak boundary guards `>=1` by strict guards `>1`. If an old outside point
had distance `<=1` from the new point, a boundary-vertex exit contradicts the strict
vertex guard. At a proper unit-edge crossing, the two-endpoint inequality with
`|x-y|<=1` gives distance `<=1` from a boundary endpoint, again contradicting the
strict guard.

The strict and weak safe regions differ only on finitely many circle arcs and have the
same area. Thus the abstract saturation lemma applies to the area used in the earlier
safe-area theorem.

## 3. Strict hull-pocket shield

For a Section-67 hull-augmentation outer pocket, use strict distance `>1` from the
added side and strict distance `>1` from old contact-path vertices. A segment of length
`<=1` cannot exit through the added side because the new point would then lie within
one unit of that side. Boundary-vertex and unit-edge exits are handled exactly as in
the internal case.

Again the strict/weak safe regions differ by measure-zero boundaries, so their areas
coincide.

## 4. Genuine exterior cap

Audited-working Section 162 already gives strict distance above one from every retained
source outside the container for every point of the open depth-one inner body. Hence
the abstract lemma applies directly to `C_{*,-1}` for either Type-I container geometry,
including the genuine exterior cap. No mixed-wall geometry is used there.

## 5. Residual coefficients

The internal lower safe-area bound is

\[
 area(S_\partial)\ge A-mc_*-h_*.
\]

Combining with `area(S_partial)<=a0 z` and

\[
 r_\partial=A/a_0-m/2+1-z
\]

gives exactly

\[
 r_\partial\le {\pi\over3\sqrt3}m
 +\left({1\over2}+{2\pi\over3\sqrt3}\right).
\]

For a hull outer pocket, combining

\[
 area(S_{mix})\ge A-s-\ell c_*-h_*
\]

with the pocket residual identity gives exactly

\[
 r\le {\pi\over3\sqrt3}\ell
 +\left({2\over\sqrt3}+{1\over2}\right)s
 +\left({2\pi\over3\sqrt3}-{1\over2}\right).
\]

Summing the chamber area ceilings gives `area(S_F)<=a0 Z_ch`; therefore the aggregate
lower bound `area(S_F)/a0-Z_ch>=Xi` forces `Xi<=0`. Section 162 similarly gives
`Psi_E<=0` for a genuine exterior cap.

## 6. Interpretation audit

The theorem does **not** prove that non-strict unit-packing capacity equals the current
isolate count. The scaled-lattice proof only rules out a guaranteed extra packing with
all pairwise/new-old distances strictly above one. Additional non-strict capacity may
exist through exact unit contacts.

Therefore the diameter-cover theorem is not invalidated. Instead, its remaining
capacity must come from discrete exact-contact structure; mean area alone cannot force
it.

No contact isolate is inserted into the Section-57 affine-kernel theorem, and every
exchange preserves cardinality.

**Final verdict:** PASS. This is a genuine no-go theorem for the area-only Type-I
closure route and isolates exact-contact saturation as the remaining mechanism.
