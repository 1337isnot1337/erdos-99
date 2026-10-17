> Generated reading edition · [exact source](../../../docs/reports/target_c_rooted_endpoint_route_phase_exclusion_2026-09-30.md) · source SHA-256 `178cd3dbdf9c18a8d540bd142daba263201f19e5fd25206c7f6a5422aabef39f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-91731A271734","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- rooted endpoint route-phase exclusion

Date: 2026-09-30
Base main: b12708a602af4b17bbb8ecf61e5ed461e4bb2e15
Status: proof-only; theorem-state authority unchanged. C-II remains open.

## Theorem

Define

    A(lambda) = lambda + 4 lambda sqrt(1-lambda^2)

and let lambda_1 be the current-main root

    A(lambda_1) = pi/2,

so lambda_1 = 0.9891345915624005... for orientation only.

No positive-area, locally rhombus-saturated, center-wrapping harmonic-cell
sequence can have d_w/D -> lambda_1.

Consequently there are absolute, nonexplicit constants epsilon_1,c_1 > 0 such
that every sufficiently large full-core Type-II survivor has an actual locally
rhombus-saturated harmonic cell P_* with

    diam(P_*) >= (lambda_1 + epsilon_1) D,
    area(P_*) >= c_1 D^2.

## 1. Endpoint equality fixes the support profile

Assume d_w/D -> lambda_1. Put

    theta = 2 asin(lambda_1),
    phi   = 2 pi - 2 theta,

and let g_j be the complement gaps of the limiting circle support S of the
wrapping cell. Set

    C_gap = sum_j sin(g_j/2).

Current main gives

    S_D := sum_r d_r = (lambda_1 + pi/2) D + o(D),

while the uncapped complement-gap moment gives

    S_D >= d_w + C_gap D - o(D).

Hence C_gap <= pi/2. Canonical Section 101 gives

    C_gap >= sin(theta/2) + 2 sin(theta)
          = A(lambda_1)
          = pi/2.

Therefore equality holds.

The Section-101 majorization is strict away from its extremizer: every gap is
at most theta; three distinct gaps are at least phi; total gap measure is at
least theta + 2 phi; and x -> sin(x/2) is strictly increasing and strictly
concave on (0,pi). Equality therefore forces exactly

    (g_1,g_2,g_3) = (theta,phi,phi)

and no other positive gap. Total support measure is

    U = 3 theta - 2 pi.

The gap of length theta has singleton support components at both ends. If an
adjacent support component contained a nontrivial arc, moving a sufficiently
small positive amount into it would produce two support points with minor
angular separation strictly larger than theta and still below pi, contradicting
the angular-diameter bound. The remaining support component has no internal
positive gap, hence is one closed circular arc of length U. Since theta < pi,

    U < pi.

The three positive gaps define the three principal finite outer corridors.

## 2. Current main makes the carrier routes geodesic in aggregate

For consecutive attachment vertices p_i,p_{i+1}, let b_i be the polygon-base
length, q_i its oriented unit direction, and R_i the corresponding outer-face
route with oriented unit edge vectors z and length ell_i. Projection gives the
exact identity

    ell_i - b_i = sum_{z in R_i} (1 - q_i dot z).        (2.1)

Summing over the carrier gives

    L_w - per(P_w) = sum_i (ell_i - b_i).               (2.2)

The current-main rooted defect theorem gives at lambda_1

    Z_D := sum_r (L_r - per(P_r)) = o(D),
    Q_D := sum_r Q_r = o(D).

Every summand in Z_D is nonnegative, so

    L_w - per(P_w) = o(D).                              (2.3)

In particular each principal corridor has route excess o(D).

## 3. Rate-free phase dispersion

Fix physical outer-face edge occurrences whose projective directions lie in an
o(1) window around one fixed limiting direction u, excluding the three
principal corridors. Their number is o(D).

Proof. Fix epsilon > 0 before taking D -> infinity. On routes whose base
direction is at projective distance at least epsilon from u, every selected
edge contributes at least

    1 - cos(3 epsilon / 4) > 0

to (2.1) for all large D. Equation (2.3) therefore makes their total o(D).

For the remaining routes, selected-edge count is at most route length. Their
total route length equals total base length plus o(D). After scaling, the
nonprincipal bases converge to the single radius-1/2 circular support arc;
neighborhoods of the two isolated support points have vanishing normalized
boundary length. Because the tangent-direction range of that arc has length
U < pi, a projective epsilon-window has only one oriented lift on it. Its
intersection with the circular arc has normalized length at most

    (1/2) (2 epsilon) = epsilon.

Convex side-direction monotonicity and Hausdorff convergence therefore give

    limsup_{D->infinity} N_selected / D <= epsilon.

Now send epsilon down to zero. This proves N_selected = o(D). The order of
limits is fixed-epsilon first and requires no convergence rate.

## 4. Contradiction with the two inverse-phase train families

The carrier has area Omega(D^2) and local strict-rhombus filling ratio tending
to one. Canonical Sections 89--90 therefore give two fixed distinct phase-label
train families A_D and B_D, each containing Omega(D) train segments, with
terminal-edge directions in O(1/D) projective windows. Their limiting
directions u_A,u_B satisfy

    dist_RP1(u_A,u_B) = pi/3.                            (4.1)

Each train has two physical boundary ends. At most 5 Q_w = o(D) such terminal
occurrences face bounded nonquadrilateral faces because Q_w <= Q_D. By Section
3, only o(D) endpoints from either selected phase family lie on nonprincipal
outer routes. Hence each phase family has linearly many terminal-edge
occurrences on the three principal corridors.

Pigeonhole one principal corridor for each family. If a principal corridor
with chord direction q_D contains linearly many endpoints from a phase family
with limiting direction u, its route identity

    sum_{z in R} (1 - q_D dot z) = o(D)

forces q = u in RP^1. Otherwise every selected terminal edge would pay a fixed
positive projection loss and the route excess would be Omega(D).

Thus two distinct principal corridor directions must have projective separation
exactly pi/3.

For the gap profile (theta,phi,phi), the three principal chord directions have
pairwise projective separations

    { theta/2, theta/2, pi-theta }.

Current main has lambda_1 > sqrt(3)/2, hence theta > 2 pi/3. Therefore

    theta/2 > pi/3,
    pi-theta < pi/3.

No principal pair differs by pi/3. This contradicts (4.1), proving the endpoint
exclusion.

## 5. Compactness gives a strict qualitative gap

Canonical Section 88 has cap-family capacity

    C_cap(lambda_1) < pi/4.

If no uniform improvement above lambda_1 existed, take a diagonal sequence on
which every fixed quadratic-area cell has normalized diameter at most
lambda_1 + o(1). Canonical small-cell control leaves only finitely many
macroscopic limits and makes the discarded small-cell area arbitrarily smaller
than

    pi/4 - C_cap(lambda_1).

Every macroscopic limit is locally rhombus-saturated. A wrapping limit below
lambda_1 contradicts the current-main rooted scalar theorem; a wrapping limit
equal to lambda_1 contradicts the endpoint exclusion above. Hence every
macroscopic limit is cap type. Canonical Section 88 then bounds their total area
by C_cap(lambda_1), contradicting the full-core area identity

    sum_r area(P_r) = (pi/4) D^2 - o(D^2).

Therefore the stated epsilon_1,c_1 > 0 exist.

No computation or verifier is load-bearing. The remaining full-core problem is
the uniformly separated wrapping regime together with the diameter-one/two-half-
disk alternative. The macroscopic inactive-container branch is unchanged.
