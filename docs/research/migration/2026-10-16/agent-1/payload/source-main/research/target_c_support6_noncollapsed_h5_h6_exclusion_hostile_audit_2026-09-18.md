# Hostile audit — noncollapsed support-six H5/H6 exclusion

**Date:** 2026-09-18  
**Audited source:** `target_c_support6_noncollapsed_h5_h6_exclusion_2026-09-18.md`  
**Certificate:** `verify_target_c_support6_noncollapsed_h5_h6_exclusion_2026_09_18.py`  
**Disposition:** PASS at proof-only scope; theorem-state authority unchanged

## 1. H5 angle argument

The argument is local to a non-ground reciprocal hull vertex and uses the actual source
pentagon only through its strict consecutive force-direction gap `<2pi/3`. The ground
reciprocal point is never assigned that source gap. The five raw rays are contained in
the open hull cone, and the `2+3` resultant equation places the negative triple's
resultant on the positive-pair bisector, so the lifted extreme arguments satisfy
`a<0<c`; the displayed cluster gaps are therefore the correct cyclic gaps.

The strictness is preserved at both relevant places. General position makes the two
same-sign rays distinct, hence `p<pi/3` under the assumed `phi<=2pi/3`; the source
pentagon gives strict `<2pi/3` cluster gaps. The trigonometric identity is an equality
derived from the exact unit-vector resultant equation, and its right side is
nonnegative for `u,v>=0` and `u+v<pi/3`. Cosine monotonicity then gives the reverse
inequality needed for contradiction.

The angle-sum step correctly uses the coarse unit-force hull bound at the ground point
only. It does not import the physical source-turn theorem at the auxiliary ground
point.

## 2. H6 finite step

The H6 certificate is independently exact: it enumerates 26 uniform single-element
extensions of the convex-hexagon chirotope and tests all 15 perfect matchings, both
ground sign complements, and all local alternation choices. It returns zero compatible
uniform signings. Its separate 14-wall check also returns zero, and uses no metric
coordinates or tolerances.

The H6 use is conservative: excluding a necessary sign/order set is sufficient for the
branch exclusion, while any nonrealizable abstract order type only enlarges the tested
candidate set.

## 3. Scope and propagation

This result applies only to the degree-pure support-six reciprocal construction. It does
not exclude the collapsed branch `y_1=...=y_6`, larger one-anchor components, or the
global C-II diameter/KKT locking problem. It does not justify deleting contact-isolated
source points or extending the ZR/ZF affine kernel to them.

The coefficient remains `n_1/6` until the collapsed branch is globally excluded. No
theorem-state promotion is claimed.

**Audit disposition:** pass for the stated H5 proof and exact H6 finite check; collapsed
support six remains the smallest live local obstruction.
