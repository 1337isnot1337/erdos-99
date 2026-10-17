> Generated reading edition · [exact source](../../../docs/reports/target_c_inactive_chamber_activation_grid_regression_2026-09-12.md) · source SHA-256 `2a413d4c742d49b031e0847446f4a3a8545019bad6ac14b55c085e63d2d504f3`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D320EFAD323A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_inactive_chamber_activation_grid_regression_2026-09-12.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=bdac63e06263ce1b2a2fd953582a6fae33ba5af5; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C — exact-contact activation regression for the inactive chamber

**Date:** 2026-09-12  
**Repository branch:** research/c2-closure-sol-20260912-r1  
**State version:** 2026-09-12.audit.44  
**Run type:** hostile regression / macroscopic inactive-container branch  
**Target:** C-II  
**Computation:** research/verify_target_c_inactive_chamber_activation_grid_regression.py

## STATUS

REGRESSION — PROVED FINITE FAMILY, NONCANONICAL

This note gives an exact family showing that the strongest currently available
inactive-chamber statistics do not force a triangle even after collective contact
activation. A macroscopic chamber can be bounded by a triangle-free unit-contact
frame, contain a quadratic population with only linear Oler slack and quadratic deep
near-unit matching, and be continuously collapsed to a triangle-free exact-contact
rhombic grid while the frame and its diameter remain fixed.

The family is not a global minimum-diameter source. It is therefore not a
counterexample to Erdős Problem #99 and does not close C-II. It rules out the local
implication

    deep near-unit isolate pairs + collective first-contact activation
      -> exact unit equilateral triangle

even when the chamber is genuinely co-embedded with a diameter-carrying contact
core. The surviving theorem must use global optimality or must move the
diameter-carrying core.

## 1. Rational near-triangular lattice

Fix an integer M>=8 and put

    a_M = floor(M/sqrt(3)) + 1,
    t_M = a_M/M.

Then

    1/sqrt(3) < t_M <= 1/sqrt(3) + 1/M.

Define the rational unit vectors

    u=(1,0),
    v=(c_M,r_M),

where

    c_M=(1-t_M^2)/(1+t_M^2),
    r_M=2t_M/(1+t_M^2).

Thus c_M and r_M are rational, c_M<1/2, and, for M>=8,
0<c_M<1/2. The angle theta_M between u and v obeys

    pi/3 < theta_M=2 arctan(t_M) < pi/2,
    theta_M-pi/3=O(1/M).

For a coefficient difference (p,q), the squared distance in this lattice is

    Q_M(p,q)=p^2+2c_M p q+q^2.

Because c_M<1/2, the only nonzero integer differences with Q_M(p,q)=1
are

    (p,q) in {(1,0),(-1,0),(0,1),(0,-1)}.

Indeed, if p and q have opposite signs, the smallest mixed case is
(1,-1), whose squared length is 2-2c_M>1; same-sign mixed differences
are longer, and a difference with one coordinate of absolute value at least two
is also longer. Consequently a finite rectangular patch of this lattice has a
bipartite unit-contact graph and contains no unit equilateral triangle.

## 2. A contact core and a macroscopic chamber

Use coefficient coordinates relative to u,v. Let the outer contact frame be

    B_M={(i,j) in Z^2: 0<=i,j<=M and
         (i=0 or i=M or j=0 or j=M)}.

Its geometric realization is the boundary cycle of the parallelogram

    P_M={alpha u+beta v: 0<=alpha,beta<=M}.

The frame has 4M points and 4M unit-contact edges. Its contact graph is a
cycle, hence is triangle-free. Opposite corners have squared distance

    D_M^2=M^2(2+2c_M).

The chamber population uses the index square 3<=i,j<=M-3, which has
(M-5)^2 points. Let

    o_M=(M/2)(u+v),
    q_M=1+1/M,

and define the initial chamber population by

    I_M^+={o_M+q_M(iu+jv-o_M): 3<=i,j<=M-3}.

Every initial chamber point has lattice coefficient coordinates strictly between
5/2 and M-5/2. The same is true for the unscaled patch

    I_M^0={iu+jv: 3<=i,j<=M-3}.

For a point at coefficient distance alpha from a side of P_M, the squared
distance to the entire supporting line of that side is

    alpha^2(1-c_M^2).

Since alpha>5/2 and c_M<1/2, this exceeds one. Hence every point of either
I_M^+ or I_M^0 is more than one unit from every frame point.

Distinct initial chamber points have all nonzero lattice differences multiplied
by q_M>1, so they are pairwise strictly separated and contact-isolated in the
full source

    A_M^+=B_M union I_M^+.

The bounded face inside the frame is an actual macroscopic inactive chamber:
its area is

    area(P_M)=M^2 r_M,

and its perimeter is 4M. The chamber population is quadratic. Since the sine coordinate divided by
a_0=sqrt(3)/2 equals 1+O(1/M), its isolate-only Oler slack is

    area(P_M)/a_0 + per(P_M)/2 + 1 - |I_M^+| = O(M).

The verifier checks the explicit bound 0<=slack<=16M in the tested family.
The chamber has therefore the same area, population, perimeter, and slack scales
as the surviving Type-I inactive-container branch.

## 3. Deep near-unit matching

For every row j, pair consecutive chamber indices in the i direction.
These pairs are vertex-disjoint and have initial distance exactly

    q_M=1+1/M=1+2/D_M+O(M^{-2}).

There are

    floor((M-5)/2)(M-5)=Omega(M^2)

such pairs. Their coefficient distance from every chamber side is greater than
5/2, so their physical distance from the frame is uniformly greater than one.
They are deep near-unit pairs of the same kind supplied abstractly by the canonical
inactive-chamber matching theorem.

## 4. Collective activation without a triangle

The entire chamber population can be moved simultaneously along the homotopy

    I_M(t)={o_M+s_t(iu+jv-o_M): 3<=i,j<=M-3},
    s_t=1+(1-t)/M,
    0<=t<=1.

At every time, an inner-inner distance is s_t times a nonzero lattice distance
and is therefore at least one. The coefficient buffer remains greater than 5/2,
so the supporting-line estimate above keeps every inner point more than one unit
from the fixed frame. The source remains unit-separated for the entire motion.

At t=0, the chamber points are all contact-isolated. At t=1, the chamber
points have the exact-contact rectangular-grid graph generated by the two unit
directions u and v. This graph is bipartite under the parity of i+j.
The frame is also a cycle, and there are no frame-to-grid contacts. Therefore the
terminal contact graph is a disjoint union of bipartite graphs and has no triangle.
In particular, no three source points have all three mutual distances equal to one.

The frame is held fixed throughout the homotopy. Its opposite corners remain a
diameter pair, so

    diam(A_M(t))=D_M

for every t. The motion is consequently neither a strict diameter decrease nor
a positive-force transfer: it creates an interior exact-contact component while
leaving the old diameter-carrying contact core unchanged.

## 5. What this regression proves

This exact family rules out the following local closure theorem:

    triangle-free unit-contact frame carrying the source diameter
    + quadratic inactive population in its bounded face
    + O(D) isolate-only Oler slack
    + Omega(D^2) deep pairs at distance 1+O(1/D)
    + simultaneous pair-closing motion
      -> exact unit equilateral triangle.

It also rules out the stronger variant in which the conclusion is obtained by
creating a quadratic number of exact contacts. Exact contacts can organize into a
rhombic grid whose contact graph is bipartite. The protected old diameter pair
then prevents the motion from lowering the source diameter.

No contact-isolated point is deleted. The initial and terminal sources have the
same cardinality. The terminal source is an explicit triangle-free same-diameter
configuration, not a claim of global optimality.

## 6. Hostile scope audit and exact remaining obstruction

* The construction is a regression family, not a global minimizer. Its diameter
  may be beaten by a different arrangement with the same cardinality.
* All distance checks use the exact rational quadratic form Q_M; the only
  irrational quantity in the displayed Oler comparison is the harmless scale
  sqrt(3)/2.
* The initial contact core is the outer frame. The interior population is genuinely
  contact-isolated, not merely omitted from a matrix.
* The terminal interior grid is not promoted to positive KKT support. It is an
  interior disconnected contact component, and its contacts may carry zero
  multipliers.
* The diameter pair is retained and fixed. No same-cardinality strict sub-diameter
  competitor is asserted.
* No full-source ZR/ZF affine-kernel theorem is used.

The exact surviving C-II obstruction is now narrower:

    prove that global diameter minimality couples the inactive chamber to the
    diameter-carrying core strongly enough to rule out this finite rhombic-grid
    activation model, or construct a strict same-cardinality sub-D competitor
    that necessarily moves the core.

The chamber statistics alone are insufficient.

## 7. Verification

Run:

    python3 research/verify_target_c_inactive_chamber_activation_grid_regression.py

The script checks rational basis coordinates, exact source separations, the frame
and terminal-grid contact graphs, triangle-freeness, the fixed diameter, the Oler
slack bound, the deep matching, and the coefficient buffer used by the homotopy.
It does not establish global optimality or C-II closure.

Disposition: proved finite regression, noncanonical; theorem state unchanged.
