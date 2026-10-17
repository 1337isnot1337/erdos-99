> Generated reading edition · [exact source](../../../docs/reports/target_c_wrapping_endpoint_four_cell_rigidity_2026-09-30.md) · source SHA-256 `43e57f4468360cdb4f8219d82fa1b68c25696e2322f5f23c1a976e823511a08f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-9AB805C11962","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- wrapping endpoint four-cell rigidity

Base main: b12708a602af4b17bbb8ecf61e5ed461e4bb2e15. Proof-only. C-II open.

Assume a positive-area center-wrapping harmonic cell P_w satisfies d_w/D -> lambda_1, where

lambda_1 + 4 lambda_1 sqrt(1-lambda_1^2) = pi/2.

Write theta_1 = 2 asin(lambda_1), phi_1 = 2 pi - 2 theta_1, and beta_1 = sin(theta_1).

## Theorem

After a subsequence and the standard diagonal selection, there are exactly four macroscopic harmonic-cell sequences to first order:

- the wrapping cell P_w, diameter (lambda_1+o(1))D;
- one residual cap cell P_1, diameter (lambda_1+o(1))D;
- two residual cap cells P_2,P_3, each diameter (beta_1+o(1))D.

All other harmonic cells satisfy

sum_{r notin {w,1,2,3}} d_r = o(D).

The wrapping support has exactly three positive complement gaps,

(g_1,g_2,g_3) = (theta_1, phi_1, phi_1),

and no tail gaps. If G(t)=(t-sin t)/8, then

area(P_1)/D^2 -> G(theta_1),
area(P_2)/D^2, area(P_3)/D^2 -> G(phi_1),

while

area(P_w)/D^2 -> pi/4 - G(theta_1) - 2 G(phi_1).

Moreover P_j/D converges in Hausdorff distance to the full circular cap segment over its gap for j=1,2,3. All four macroscopic cells are locally rhombus-saturated.

## Proof

Current main gives at the exact rooted endpoint

S_D := sum_r d_r = (lambda_1 + pi/2)D + o(D).

Subtracting the wrapping-cell contribution,

sum_{r != w} d_r = (pi/2 + o(1))D.                                           (1)

Let S be the limiting circle support of P_w and let its complement gaps have lengths g_j. The hostile-audited complement-gap filling theorem already used on current main gives

liminf D^{-1} sum_{r != w} d_r >= C(S) := sum_j sin(g_j/2).                    (2)

Canonical Section 101 gives

C(S) >= sin(theta_1/2) + 2 sin(theta_1)
     = lambda_1 + 4 lambda_1 sqrt(1-lambda_1^2)
     = pi/2.                                                                  (3)

Equations (1)-(3) force C(S)=pi/2 and zero first-order slack in the residual diameter moment.

Now put m=|S| and phi=2 pi - 2 theta_1. Section 101's fixed-m majorization gives

C(S) >= f(theta_1) + f(theta_1-m) + f(phi),  f(t)=sin(t/2).

Section 100 gives m <= U:=3 theta_1-2 pi, hence theta_1-m >= phi. Since f is strictly increasing and C(S)=f(theta_1)+2f(phi), equality forces m=U. Thus the total complement measure is theta_1+2 phi.

With this total, every gap at most theta_1, and at least three gaps at least phi, the vector (theta_1,phi,phi,0,...) majorizes every feasible gap vector. Strict concavity of f on (0,pi) shows equality only for this vector. Hence the complement has exactly the three gaps claimed.

For gap j put s_j=sin(g_j/2). The quantitative stability step in the complement-gap filling proof says that, after taking a sufficiently small positive-area cutoff, one actual residual cell in gap j has support span g_j-o(1), hence diameter at least (s_j-o(1))D. There are only three gaps, so choose such cells P_1,P_2,P_3 simultaneously. Their diameter sum is at least (C(S)-o(1))D. By (1), all other residual cells therefore have total diameter o(D). This proves the four-cell diameter decomposition. Since g_1=theta_1 and g_2=g_3=phi_1, their limiting diameters are lambda_1,beta_1,beta_1.

Planar isodiametry gives

sum_{other residual} area(P_r)
 <= (pi/4) sum d_r^2
 <= (pi/4) (sum d_r)^2
 = o(D^2).

Whole-disk Type-II area saturation and the gap-by-gap area filling theorem then force P_j to carry the full first-order area G(g_j) of its gap segment. Any Hausdorff limit Q of P_j/D is a compact convex subset of the closed gap segment C_j with area(Q)=area(C_j). A proper compact convex subset of C_j has strictly smaller area, so Q=C_j. Hence P_j/D -> C_j.

Finally canonical Section 83 gives the nonnegative summed local filling deficit

sum_r (area(P_r)-A_{4,r}) = o(D^2).

Each of the four selected cells has positive limiting area, so each individual deficit is o(D^2); therefore each is locally rhombus-saturated.

## Endpoint profile

Symbolically,

lambda_1 + 2 beta_1 = pi/2,

so the four normalized diameters are

(lambda_1, lambda_1, beta_1, beta_1).

For orientation only:

lambda_1 = 0.9891345915624005...,
theta_1 = 2.8464975254496867...,
phi_1 = 0.5901902562802128...,
beta_1 = 0.2908308676162492....

The limiting normalized areas are approximately

area(P_w) = 0.4575220432294873,
area(P_1) = 0.3194583322291797,
area(P_2)=area(P_3)=0.00420889396939067.

These decimals are diagnostic only.

## Remaining bottleneck

The exact endpoint is now reduced to two opposite lambda_1-scale locally rhombic cells sharing the same long chord, plus two much smaller cap cells; every other cell is negligible in total diameter. The next target is a cross-chord train/interface theorem or a diameter-graph obstruction that excludes this four-cell geometry. The two-half-disk diameter-one alternative and the separate macroscopic inactive-container branch remain open.

No computation, verifier, or CI result is load-bearing.
