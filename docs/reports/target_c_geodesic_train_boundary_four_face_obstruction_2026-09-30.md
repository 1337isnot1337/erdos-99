<!-- theorem-state: {"artifact_id":"ART-2658536E05FB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_geodesic_train_boundary_four_face_obstruction_2026-09-30.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=61da3f67d83aac613a153f31ddc58385e78cb387; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C: geodesic train boundaries require four straight limit faces

**Date:** 2026-09-30<br>
**Base main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; noncanonical.<br>
**Level I:** open. C-II remains open.

## 1. Exact target and implication chain

The rooted wrapping endpoint on current main forces both total harmonic route
excess and bounded nonquadrilateral defect to be sublinear. This report uses
those currencies directly:

\[
Z_w+Q_w=o(D)
\Longrightarrow \text{four straight support faces of the carrier limit}
\Longrightarrow \text{contradiction at the three-gap rooted endpoint}.
\]

The general train-boundary theorem below uses canonical train and phase inputs.
The application to the numerical rooted endpoint is conditional on the
explicitly unpromoted rooted and complement-gap moment reports listed below.
No canonical promotion or full C-II closure is claimed.

## 2. Statement

Let \(P_D=\operatorname{conv}(A_D)\) be actual harmonic attachment polygons
along a canonical full-core Type-II sequence, with induced contact graphs
and their full bounded strict-rhombus complexes. Assume, for constants
\(r,C_T,C_{\rm ph}>0\),
\[
R_{4,D}\ge rD^2,\qquad T_D\le C_TD,\qquad
\sum_R\delta_R\le C_{\rm ph}D.
\tag{2.1}
\]
Here \(T_D\) counts the original local trains stopped only at physical
boundaries of the full rhombus complex. Write \(L_D\) for the
occurrence-counted outer walk, \(p_D=\operatorname{per}P_D\), and \(Q_D\)
for the local bounded nonquadrilateral degree excess. Suppose
\[
L_D-p_D=o(D),\qquad Q_D=o(D),\qquad D^{-1}P_D\to K
\tag{2.2}
\]
in Hausdorff distance, with \(K\) a positive-area convex body.

Then \(K\) has four distinct positive-length straight support faces. Their
oriented tangent directions are
\[
\alpha,\quad\alpha+\pi,\quad\beta,\quad\beta+\pi,
\qquad \operatorname{dist}_{\mathbb R/\pi\mathbb Z}(\alpha,\beta)=\pi/3.
\tag{2.3}
\]
Consequently (2.1)--(2.2) cannot hold if \(K\) has at most three straight
support faces.

The conclusion is about a fixed subsequential convex limit. It asserts no
finite equality, no rate of Hausdorff convergence, and no rate of convergence
of the phase-bin center.

## 3. Proof

### 3.1 Obtain two families of original trains

Canonical Section 90, applied to (2.1), supplies two distinct phase-label
families \(\mathcal A_D,\mathcal B_D\) of at least \(\kappa D\) original
local trains each, for a fixed \(\kappa>0\). Within each family all projective
edge directions lie in an \(O(D^{-1})\) interval. Their two interval centers
have limiting projective separation \(\pi/3\).

The phase-circle cut used in Section 90 removes crossing **edges of the
crossing graph**. It does not replace the original local trains by new
segments stopped at the cut rhombi. We retain the original trains and their
original physical ends. Thus no artificial \(O(D)\) end capacity is introduced.

Pass to a subsequence so the two moving phase centers converge to
\(\alpha,\beta\) modulo \(\pi\). The directions relative to these fixed
limits are only \(o(1)\); the \(O(D^{-1})\) width is relative to the
moving centers. This distinction is retained throughout the proof.

### 3.2 Almost all selected trains have two outer ends

Every physical rhombus-boundary edge faces either the old outer face or a
bounded nonquadrilateral face. The latter faces have total incidence
capacity at most \(5Q_D=o(D)\), by canonical Sections 82 and 89.
Each physical boundary incidence terminates only one train. Delete selected
trains with any such exceptional end; both families still contain
\((\kappa-o(1))D\) trains with two ends on the old outer walk.

Orient that walk with the incident bounded face on its left. The two
terminal edge occurrences of a train have opposite oriented edge vectors.
Indeed, opposite sides of every traversed rhombus are parallel. Orient the
train's transverse coordinate along a normal to that edge direction. It
increases strictly through successive rhombi. At the first terminal edge the
train enters the face on the left; at the last it exits from the left. This
requires opposite boundary orientations. Gluing the rhombi across their
opposite sides preserves this orientation; a reversal would reverse the
strict transverse progress.

Therefore each family supplies \((\kappa-o(1))D\) distinct outer terminal
occurrences in **each** of its two opposite oriented direction cones. The
four limiting cones in (2.3) are distinct.

### 3.3 Charge all angular leakage to occurrence-counted route excess

Choose the distinguished exterior occurrences of the attachment vertices
in cyclic order. Split the outer walk into routes \(W_i\) between consecutive
attachments. Let \(\ell_i\) be a route's unit-edge occurrence count, let
\(s_i\) be the corresponding polygon side length, and let \(u_i\) be the
oriented side's unit direction. For its oriented edge vectors \(z_e\),
\[
\ell_i-s_i=\sum_{e\in W_i}(1-u_i\cdot z_e),
\qquad
\sum_i(\ell_i-s_i)=L_D-p_D=:Z_D=o(D).
\tag{3.1}
\]
Every summand is nonnegative. Repeated vertices and bridge occurrences are
retained in these sums.

Fix \(\eta>0\) first. At most
\[
\frac{Z_D}{1-\cos\eta}=o(D)
\tag{3.2}
\]
unit-edge occurrences make oriented angle at least \(\eta\) with their host
polygon side. For large \(D\), terminals in a chosen fixed limiting cone
are themselves within \(\eta\) of its limiting direction. Thus all but
\(o(D)\) of its \((\kappa-o(1))D\) terminal occurrences lie on routes
whose polygon side directions are within \(2\eta\) of that direction.

If \(J_D(\eta)\) denotes those sides, their full routes contain at least
\((\kappa-o(1))D\) occurrences, while
\[
\sum_{i\in J_D(\eta)}\ell_i
\le\sum_{i\in J_D(\eta)}s_i+Z_D.
\]
Hence
\[
\liminf_D\frac1D\sum_{i\in J_D(\eta)}s_i\ge\kappa.
\tag{3.3}
\]
This is a bound on physical occurrence mass, not on a set of exceptional
vertices.

### 3.4 The positive boundary mass becomes a straight support face

For a convex polygon, sides whose oriented tangent directions lie in one
small cone occur consecutively around the boundary. Their chain length in
(3.3) is at least \((\kappa-o(1))D\); its endpoint displacement projected
onto the cone's middle direction is at least this length times
\(\cos(2\eta)\).

Now pass to limits in the required order: first \(D\to\infty\) for each
fixed \(\eta\), then \(\eta\downarrow0\). A diagonal subsequence of the
two normalized chain endpoints has separation at least \(\kappa\).
The side normals of the chains converge to the same outward normal. Hausdorff
convergence and continuity of convex support functions place both endpoint
limits on the same support line of \(K\). Their segment is a straight
support face of length at least \(\kappa\).

Apply this argument to each of the four oriented terminal families. Distinct
outward normals give four distinct straight support faces, proving (2.3).
No shrinking direction interval is used before a fixed-angle limit.

## 4. Application: the exact rooted wrapping endpoint is impossible

Assume the unpromoted rooted endpoint package on current main and let a
positive-area center-wrapping carrier have
\[
d_w/D\to\lambda_1<1,\qquad
\lambda_1+4\lambda_1\sqrt{1-\lambda_1^2}=\pi/2.
\]
The rooted defect-stability report gives
\[
\sum_r(L_r-p_r)=o(D),\quad \sum_r Q_r=o(D),\quad
\sum_r d_r=(\lambda_1+\pi/2)D+o(D).
\tag{4.1}
\]
In particular (2.2) holds for the wrapping carrier. Local rhombic saturation
and positive normalized area give (2.1) through canonical Sections 68, 82,
89, and 90.

Let \(S\) be its normalized attachment limit on the radius-\(1/2\) circle,
let \(K=\operatorname{conv}S\), and write its complementary angular gaps as
\(g_j\). The unpromoted uncapped complement-filling moment says
\[
\liminf_D D^{-1}\sum_{r\ne w}d_r\ge C(K):=\sum_j\sin(g_j/2).
\tag{4.2}
\]
Put \(\theta=2\arcsin\lambda_1\), \(\phi=2\pi-2\theta\).
Canonical Section 101 gives
\[
C(K)\ge\sin(\theta/2)+2\sin\theta
=\lambda_1+4\lambda_1\sqrt{1-\lambda_1^2}=\pi/2.
\]
Equations (4.1)--(4.2) force equality.

For completeness, equality requires exactly three positive gaps of lengths
\((\theta,\phi,\phi)\). The gap constraints are \(g_j\le\theta\), at
least three \(g_j\ge\phi\), and total mass at least
\(H=\theta+2\phi\). If the mass exceeds \(H\), reducing it while
preserving three \(\phi\)-floors strictly reduces the increasing chord sum.
At mass \(H\), the decreasingly sorted gap vector is majorized by
\((\theta,\phi,\phi,0,\ldots)\): the first partial sum is at most
\(\theta\), the second at most \(\theta+\phi\), and every later one at
most \(H\). Strict concavity of \(\sin(x/2)\) forces this exact vector
at equality. For a countable vector, any positive entry outside that vector
permits a strict finite mass transfer; truncating the remaining tail gives
the same conclusion. This is the same equality argument audited in
canonical Section 102.2 and does not use its older endpoint equation.

Consequently \(K\), the convex hull of this circle support, has exactly
three straight boundary faces. Its remaining boundary is circular support;
there is no additional straight face. This contradicts the four-face
theorem. The exact rooted wrapping endpoint is therefore excluded, conditional
on the current unpromoted rooted package.

This is a subsequential endpoint exclusion. It supplies no explicit gap or
finite threshold, and does not exclude carriers with larger normalized
diameter, a diameter-one wrapping limit, the two-half-disk alternative, or a
macroscopic inactive container.

## 5. Dependencies and hostile audit

| Input | Lifecycle and use |
| --- | --- |
| Canonical Sections 68, 82, 89, 90 | Phase defect, original physical train count/end capacity, and inverse-phase extraction. |
| Canonical Sections 101 and 102.2 | Complement-chord bound and strict equality mechanism, with the new parameter substituted. |
| `target_c_wrapping_root_defect_stability_2026-09-30.md` | Unpromoted; gives (4.1). |
| `target_c_shape_detour_nearglobal_carrier_0988676_2026-09-29.md`, Section 2 | Unpromoted; states (4.2) and identifies its earlier proof/audit. |

The new bridge is analytically proved, with no load-bearing computation.
It was checked against repeated outer-walk occurrences, hole-end capacity,
phase-cut-created endpoints, opposite boundary orientation, vanishing cells,
moving phase centers, and fixed-angle-before-limit order. The carrier must
have positive limiting area; vanishing cells are not assigned a train shore.
No diameter degree bound or incidence transfer is assumed. Contact-isolated
points remain in the source. No finite motion or exact triangle is inferred.

**Promotion disposition:** general four-face theorem is a proved candidate
awaiting independent promotion; the rooted endpoint application remains
conditional on its named unpromoted inputs.
