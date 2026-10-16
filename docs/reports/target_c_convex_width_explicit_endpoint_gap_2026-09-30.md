<!-- theorem-state: {"artifact_id":"ART-6A4993E346E1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II - explicit quantitative gap above the convex-width fixed point

Date: 2026-09-30
Base remote main at final recheck: 77d418e49da08328f126fcd5bbab21cccb15b639
Depends on:
- target_c_convex_width_outer_detour_floor_2026-09-29.md
- target_c_convex_width_section122_feedback_2026-09-30.md
- target_c_convex_width_fixed_point_endpoint_exclusion_2026-09-30.md
Status: proof-only; theorem-state authority unchanged; C-II remains open.

Salvaged from source branch `proof/target-c-convex-width-nearglobal-upgrade-20260930` at tip `78256ee767f4ce99c2ea6c634e3bd6bcf9419c4b`; no original PR was found. Lifecycle on this branch: **unreviewed**, noncanonical.


The qualitative endpoint exclusion can be made effective with coarse constants.
Let
  alpha_* = 0.1145033543028727...
denote the exact fixed point from the parent report. This note proves the explicit
asymptotic strengthening

  liminf (q-k-sum_r d_r)/D >= alpha_* + 10^(-8).                       (1)

The decimal value of alpha_* is not used as a premise; alpha_* remains defined by
its exact fixed-point equation. The only decimal constants used in the proof below
are conservative rational bounds.

## 1. Scalar slack when x is within 10^(-8) of alpha_*

Take a subsequence on which
  X/D -> x,   X=q-k-sum_r d_r,
and suppose
  alpha_* <= x <= alpha_* + e,   e=10^(-8).                            (2)

Use the notation of the parent proof:
  c = pi/4,
  rho = sqrt(1+pi^2/16),
  C = 2/(1+rho),
  beta = rho-1,
  t(x) = pi-3-x,
  M(x) = 3+t(x)^3,
  U(x) = [10x-c_det]/4,
  c_det = (pi/2)(2-sqrt(3)).

Section 122 plus the exact feedback inequality gives
  limsup S/D <= U(x).                                                    (3)
The convex-width/Cauchy chain gives, for normalized cell diameters z_r=d_r/D
and normalized cell areas a_r=area(P_r)/D^2,
  S/D >= C sum_r a_r^2/z_r^3
      >= C (sum_r a_r)^2/(sum_r z_r^3) + o(1).                          (4)
Full-core area saturation gives sum a_r -> c. The cubic majorization gives
  W := lim sum_r z_r^3 <= M(x).                                         (5)

At the exact fixed point,
  U(alpha_*) = sigma_*,
  C c^2/U(alpha_*) = M(alpha_*).
Since U is linear with slope 5/2 and M decreases with x, (3)-(5) imply

  0 <= M(x)-W
     <= M(alpha_*) * [2.5 e/U(alpha_*)].                                (6)

Coarse elementary bounds are enough:
  pi < 3.142, pi > 3.14, sqrt(3) < 1.733.
They imply alpha_*>0.04, hence t(alpha_*)<0.102 and
  M(alpha_*) < 3.002.
Also beta>0.27, so
  U(alpha_*) = 2 beta/M(alpha_*) > 0.179.
Therefore (6) gives

  M(x)-W < 4.2 * 10^(-7).                                               (7)

## 2. The three largest cell diameters exceed 0.999999 D

Set delta=10^(-6). Suppose the third-largest normalized cell diameter satisfied
  z_(3) <= 1-delta.
Since sum z_r <= 3+t(x)+o(1), convex mass transfer shows that the cube sum is
maximized by
  1, 1, 1-delta, t(x)+delta, 0, 0, ...
because t(x)<0.102 and delta is tiny. Thus

  W <= M(x) - G_delta(t(x)),
where
  G_delta(t)
    = 1+t^3-(1-delta)^3-(t+delta)^3
    = 3 delta(1-t^2) - 3 delta^2(1+t).                                  (8)

For 0<=t<0.102 and delta=10^(-6),
  G_delta(t) > 2.96 * 10^(-6).                                         (9)
This contradicts (7). Hence

  z_(1), z_(2), z_(3) > 0.999999.                                      (10)

## 3. Those three cells each carry more than 0.2 D^2 area

Let
  R = lim sum_r a_r^2/z_r^3.
The Cauchy excess can be written exactly as a weighted variance. Put
  b_r=a_r/z_r^3,   w_r=z_r^3/W.
Then
  R-c^2/W = W sum_r w_r (b_r-c/W)^2.                                   (11)

From (3), R <= U(x)/C. Since M decreases with x,
  0 <= R-c^2/W
     <= U(x)/C - c^2/M(x)
     <= [2.5 e]/C.                                                       (12)

Here C>0.8, so the right side is less than 3.125*10^(-8). For each of
the three cells in (10), z_i^3>(0.999999)^3. Hence (11)-(12) give

  |b_i-c/W| < 1.77*10^(-4).                                             (13)

Also c>0.785 and W<3.002, so
  c/W > 0.26149.
Combining with (10) and (13),

  a_i = z_i^3 b_i > 0.2613 > 0.2,   i=1,2,3.                           (14)

Thus any subsequential limit satisfying (2) requires three attachment cells with
diameter at least 0.999999 D and area at least 0.2 D^2.

## 4. Quantitative three-cell disk obstruction

Canonical full-core near-disk convergence implies that, after translation and for
all sufficiently large D,
  F_D/D is contained in the disk B(0,R0),   R0=0.50005.                 (15)

Lemma. There do not exist three compact convex sets K_1,K_2,K_3 inside B(0,R0)
with pairwise disjoint interiors, each of diameter at most one, diameter at least
l0=0.999999, and area at least A0=0.2.

Proof. For each K_i choose a diameter segment a_i b_i of length l_i>=l0 and let
m_i be its midpoint. The parallelogram identity gives

  |m_i|^2 + l_i^2/4
    = (|a_i|^2+|b_i|^2)/2
    <= R0^2.

With R0=0.50005 and l0=0.999999 this yields
  |m_i| < 0.0072.                                                        (16)

Use the line through a_i b_i as a base line. Let h_+ and h_- be the maximum
perpendicular heights of K_i on its two sides. Orthogonal projection of K_i along
the base has length at most diam(K_i)<=1, so
  area(K_i) <= h_+ + h_-.
Thus one side has height at least A0/2=0.1. Choose p_i on that side at height
at least 0.1. The triangle conv(a_i,b_i,p_i) lies in K_i.

At the base midpoint m_i, the distance to either sloping side of this triangle is
at least
  (l_i/2)*0.1 / 1 > 0.0499,                                             (17)
because each triangle side is at most diam(K_i)<=1. Consequently K_i contains
a one-sided open half-disk of radius 0.049 centered at m_i.

Let n_i be the inward unit normal of that half-disk. Among three unit normals, two
have angular separation at most 120 degrees. For that pair choose the unit bisector
v, so n_i dot v and n_j dot v are both at least 1/2. Put
  y = 0.0288 v.
By (16), for both selected cells
  |y-m_i| < 0.0288+0.0072 = 0.036 < 0.049,
and
  n_i dot (y-m_i) > 0.0144-0.0072 > 0.
Thus y lies in the interiors of both half-disks and hence in both cell interiors,
a contradiction. QED.

## 5. Explicit gap

Equations (10) and (14), canonical interior-disjointness of attachment cells, and
(15) violate the quantitative disk lemma. Therefore no subsequential limit x can
satisfy (2).

Since the parent theorem already gives liminf X/D >= alpha_*, the liminf itself
cannot lie in [alpha_*,alpha_*+10^(-8)]. Hence

  liminf (q-k-sum_r d_r)/D >= alpha_* + 10^(-8),

proving (1). Numerically the displayed lower endpoint is
  0.1145033643028727... .

## 6. Remaining bottleneck

This is still not a C-II closure. It replaces the qualitative epsilon_cw by an
explicit 10^(-8) margin, but the repository still lacks a competing upper bound
on X=q-k-sum d_r near 0.11450336 D. Further decimal improvement alone is not the
target; the useful next step is a loaded-diameter/topological upper bound on X, or
a structural theorem converting the forced three-cell/near-disk pressure into a
source-level contradiction.

The macroscopic inactive-container branch is untouched. No numerical computation
is load-bearing: all constants used in the proof have the displayed conservative
inequalities. No theorem-state file is changed.
