# Hostile audit: generic H6 complete-angle affine reduction

**Date:** 2026-09-19  
**Claim audited:** the complete-angle affine lift exactly excludes 616 of the 6,308 cells at the committed generic-`H6` ground-coupled endpoint, leaving 5,692 labelled cells.  
**Theorem-state authority:** unchanged; C-II remains open.

This audit checks the places where the reduction could accidentally gain strength from a wrong angular convention, from treating a missing relation edge as a geometric non-edge, or from floating-point infeasibility.

## 1. Hull-ray angles

At each reciprocal hull vertex all seven other reciprocal points lie in the open interior wedge.  The six consecutive positive ray gaps therefore form a linear order, not a circular order with a wraparound ambiguity.  At the ground hull vertex the previously certified cone width is strictly below `2*pi/3`; at the other five hull vertices strict convexity makes the interior wedge strictly below `pi`.

Hence the ordinary angle between two hull rays is exactly the sum of the consecutive gap variables between them.  No complementary-arc choice is permitted or needed.

## 2. Interior-ray angles

At reciprocal interior vertices 6 and 7 the seven rays use a circular order reconstructed from the rank-three chirotope.  For an ordered pair `(a,b)`, if `chi(v,a,b)>0`, the directed CCW arc from `a` to `b` is the ordinary angle and must lie in `(0,pi)`.  If `chi(v,a,b)<0`, that directed arc lies in `(pi,2pi)` and the ordinary angle is its complement `2*pi-arc`.

The verifier implements exactly these two cases and separately imposes `<pi` for every selected ordinary arc.  Thus the interior angle conversion does not silently assume a global semicircle.

## 3. Missing relation pairs are still geometric pairs

The support graph omits seven non-ground relation edges.  This means those pairs do not carry support forces.  It does not mean the corresponding reciprocal points cease to exist or that the segment joining them has no Euclidean angle data.

All eight reciprocal vertices are points in one plane.  Therefore every triple of reciprocal vertices, including a triple containing one or more missing relation pairs, must satisfy the ordinary Euclidean triangle angle sum.  Adding all `C(8,3)=56` triangle equations is a necessary condition for every generic reciprocal realization.

The force-angle ties are added only for pairs of PRESENT support rays.  Thus the verifier does not invent a force on a missing relation edge.

## 4. Force-angle convention

At each non-ground reciprocal vertex there are exactly five present support rays.  Their edge signs and reciprocal chirotope determine the signed-force cyclic order.  The complete-angle verifier does not rederive this conversion independently; it calls the already committed and audited `raw_angle_affine` routine from the generic-`H6` triangle/simplex verifier.

For every unordered pair among the five present rays, the verifier equates the ordinary reciprocal angle to that audited affine force-angle expression.  There are `7*C(5,2)=70` such ties.  A mismatch in one tie changes an exact equality row and would therefore be visible in the certificate rather than hidden by an optimization tolerance.

## 5. Strictness and Farkas sign

Each local or reciprocal-order restriction is represented as

`f_j(z) = c_j + a_j*z > 0`.

The numerical LP maximizes a common slack `t`.  Its dual is used only as a candidate.  The verifier converts every proposed multiplier to `Fraction`, requires nonnegative facet weights summing exactly to one, and then checks that the weighted facet coefficients plus unrestricted equality multipliers cancel in all 85 variables.

On the equality space, an accepted certificate has

`sum alpha_j f_j(z) = kappa`.

Every accepted exclusion has `kappa=0`.  Because `sum alpha_j=1` and all `f_j(z)>0`, the left side is strictly positive.  Equality to zero is therefore impossible.  No appeal to a numerical sign threshold remains after exactification.

The observed maximum denominator 102 is a property of the accepted exact duals, not a denominator cap on the mathematics; the conversion cap is one million and every accepted identity is rechecked coefficientwise exactly.

## 6. Census consistency

The committed preceding verifier reconstructs the 14,174 generic-`H6` cells and its exact ground-coupled reduction to

`6,308 = 4,936 C7 + 1,372 (C3+C4)`.

The complete-angle verifier reconstructs that endpoint rather than loading an external list.  It then accepts exactly

`616 = 472 C7 + 144 (C3+C4)`

new exact certificates and leaves

`5,692 = 4,464 C7 + 1,228 (C3+C4)`.

The ground-pattern exclusion counts sum to 616 and the survivor counts sum to 5,692.  Their componentwise sums reproduce the 6,308-cell input census.

## 7. Scope limits

This reduction is necessary-only.  Passing it does not prove that a cell admits consistent reciprocal lengths, actual reciprocal coordinates, or seven exactly closed equilateral force pentagons.  Those require the complete sine-law metric conditions and nonlinear pentagon closure conditions.

The calculation also assumes a generic reciprocal oriented-matroid cell.  Collinear reciprocal triples lie on separate walls where ray orders and strict chirotope signs degenerate.  The 5,692 count says nothing about those wall branches.

Within that scope, the 616 exclusions are exact affine contradictions and are safe to use as the next generic-`H6` endpoint.
