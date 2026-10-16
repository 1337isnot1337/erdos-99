# Hostile audit — global Type-I safe-lattice pooling

**Date:** 2026-09-12  
**Audited source:** `research/target_c_typeI_global_safe_lattice_pooling.md`  
**Verdict:** PASS at proof-only scope.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Geometry separation

The internal safe union lies in inactive chambers inside the force hull `F`. A genuine
Section-80/162 exterior cap lies in the region between `F` and the full source hull
`K`, on the exterior side of its force-hull chord. Its depth-one inner body is contained
in its interior. Thus the two safe regions have disjoint interiors; boundary overlap has
zero area and is irrelevant for translation averaging.

No claim is made that the exterior cap has a unit-contact boundary. Its safe set is
exactly the full inner parallel body from audited-working Section 165.

## 2. Deleted populations

`Z_F` is the Section-77 contact-isolated population assigned to chambers inside `F`.
`Z_E` is the contact-isolated population assigned to the selected genuine exterior cap.
They lie in disjoint container interiors/assignments. Every actual diameter endpoint is
loaded, whereas both assigned populations are inactive, so both are disjoint from the
vertex cover `U` of the complete actual diameter graph.

Hence the deletion count in the pooled competitor is exact.

## 3. Separation audit

All replacement points use one translate of the unit triangular lattice, so cross-region
new-new separation is automatic.

For a new point in an internal chamber, the corresponding wall-shield theorem controls
all retained old source points outside that chamber. For a new point in the exterior
cap depth-one body, Section 165's convex protected-depth argument gives strict distance
above one from every retained source point outside the cap interior. All assigned old
points inside each relevant container were removed.

Thus old-new separation is valid in both regions without any interaction assumption
between the two protection mechanisms.

## 4. Diameter audit

The cover `U` meets every edge of the complete actual diameter graph, so retained
old-old distances are strictly below `D`. Every new point lies in `int K`: this is
clear for internal chambers inside `F`, and is an explicit part of Section 165 for the
exterior-cap inner body. An interior point of a convex diameter-`D` body is strictly
within distance `D` of every point of the body. Hence all new-old and new-new distances
are strictly below `D`.

The replacement has cardinality `n`, is unit-separated, and has diameter `<D(n)`.
Triangle-freeness of the replacement is not needed.

## 5. One-floor scalar algebra

Translation averaging on the disjoint union gives one count with mean

\[
 [area(S_F)+area(C_{E,-1})]/a_0.
\]

Since `Z_F+z_E` is an integer,

\[
 floor(area(S_all)/a_0)-(Z_F+z_E)
 =floor(area(S_F)/a_0-Z_F+area(C_{E,-1})/a_0-z_E).
\]

The internal theorem supplies the real lower bound `Xi` for the first term and the
second term is exactly `Psi_E`. Therefore `Xi+Psi_E>=tau(H)` is sufficient for the
pooled lattice to replace all inactive points plus a minimum diameter cover.

No separate floor inequality is used, and no Oler bound is reversed.

## 6. Scope correction

The theorem deliberately does not use the stale proof-only claim that a genuine
Section-80/162 exterior cap has one artificial chord plus a unit-contact boundary
path. That claim was removed on this branch. The only exterior-cap input is the
full-collar Section-165 theorem.

**Final verdict:** PASS. The Type-I survivor condition is strengthened to

\[
 Xi+Psi_E<tau(H)\le ceil(q/2),
\]

with `Psi_E=0` in the purely internal branch. C-II remains open because no theorem yet
forces the left side above the cover size.
