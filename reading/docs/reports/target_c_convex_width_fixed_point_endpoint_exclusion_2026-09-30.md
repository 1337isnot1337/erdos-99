> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_width_fixed_point_endpoint_exclusion_2026-09-30.md) · source SHA-256 `5afcb124e9a90d8ba85d13b6738cebf2a5aac7b62812ad93be3c8da83448df03`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-34AF64FDB833","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II - exclusion of the convex-width fixed-point endpoint

Date: 2026-09-30
Base remote main at final recheck: 77d418e49da08328f126fcd5bbab21cccb15b639
Parent proof: target_c_convex_width_section122_feedback_2026-09-30.md
Status: proof-only; theorem-state authority unchanged; C-II remains open.

Salvaged from source branch `proof/target-c-convex-width-nearglobal-upgrade-20260930` at tip `78256ee767f4ce99c2ea6c634e3bd6bcf9419c4b`; no original PR was found. Lifecycle on this branch: **unreviewed**, noncanonical.


The parent proof gives
  liminf X/D >= alpha_*,   X = q-k-sum_r d_r,
with alpha_* = 0.1145033543028727... the unique fixed point
  alpha = pi(2-sqrt(3))/20
        + 4 beta / {5[3+(pi-3-alpha)^3]},
  beta = sqrt(1+pi^2/16)-1.
It also shows that a hypothetical endpoint X/D -> alpha_* would have
  S/D -> sigma_* = 2 beta/M_*,
where
  r_* = pi-3-alpha_*,   M_* = 3+r_*^3.

This note excludes that endpoint. Therefore there is an absolute non-effective
epsilon_cw > 0 such that all sufficiently large canonical full-core Type-II
survivors satisfy
  (q-k-sum_r d_r)/D >= alpha_* + epsilon_cw.

## 1. Disk lemma

Lemma. Let B be the closed disk of radius 1/2. If K_1,...,K_m are compact
convex subsets of B, each has positive area and diameter one, and their interiors
are pairwise disjoint, then m <= 2.

Proof. A diameter-one pair inside B must be an antipodal pair of boundary points.
Thus every K_i contains a full disk diameter segment and hence the disk center o.
If o is interior to one K_i, its open neighborhood meets the interior of every
other positive-area K_j containing o, so no second such set can be interior-
disjoint.

Otherwise o is a boundary point. Choose a support line of K_i at o. Since K_i
contains opposite endpoints of a diameter through o, the support line must be
that diameter line. K_i lies in one of its two closed half-planes. Positive area
provides a point off the diameter line; the triangle spanned by that point and
the diameter segment lies in K_i. Because o is in the relative interior of the
triangle base, a sufficiently small one-sided half-neighborhood of o lies in
int(K_i).

For two such sets to have disjoint interiors, their open supporting half-planes
through o must be disjoint. Two open half-planes through one point are disjoint
only when their boundary lines coincide and the half-planes are opposite. Hence
at most two sets exist. QED.

## 2. Endpoint equality forces three full-diameter cells

Assume for contradiction that X/D -> alpha_*. Normalize
  z_r = d_r/D,   a_r = area(P_r)/D^2.
Full-core area saturation gives
  sum a_r -> c := pi/4.

The parent fixed-point proof gives
  sum z_r <= pi-alpha_*+o(1) = 3+r_*+o(1),
  sum z_r^3 <= M_*+o(1),
and the convex-width/Cauchy chain
  S/D >= [2/(1+rho)] sum (a_r^2/z_r^3)
      >= [2/(1+rho)] (sum a_r)^2/(sum z_r^3),
where rho = sqrt(1+pi^2/16). Terms with z_r=0 have zero area and are omitted.

At the endpoint the left side tends
  sigma_* = [2/(1+rho)] c^2/M_*.
Therefore every lower bound in this chain is asymptotically tight. In particular
  sum z_r^3 -> M_*.

The unique majorization extremizer, up to permutation, for
  0 <= z_r <= 1,   sum z_r <= 3+r_*
is
  1, 1, 1, r_*, 0, 0, ... .
Strict convexity of t^3 gives stability: if the cube sum tends 3+r_*^3, then
the three largest coordinates satisfy
  z_(1), z_(2), z_(3) -> 1.
If the third-largest coordinate stayed <=1-eta on a subsequence, the same mass-
transfer proof would leave a positive cube-sum deficit depending on eta and r_*.

Thus three attachment cells have diam(P_i)/D -> 1.

## 3. Cauchy equality gives positive area to those three cells

Set
  W_D = sum z_r^3,
  R_D = sum a_r^2/z_r^3,
  b_r = a_r/z_r^3,
  w_r = z_r^3/W_D.
Endpoint equality gives
  W_D -> M_* and R_D -> c^2/M_*.
The exact Cauchy excess is
  R_D - (sum a_r)^2/W_D
    = W_D sum_r w_r [b_r - sum_s w_s b_s]^2.
It tends to zero.

Each of the three largest cells has w_i -> 1/M_* > 0, so b_i tends to the
common weighted mean c/M_*. Since z_i -> 1,
  a_i -> c/M_* > 0   for i=1,2,3.
Thus the endpoint requires three attachment cells with diameter D-o(D), each
carrying a fixed positive fraction of D^2 area.

## 4. Compactness contradiction

Canonical C-FULLCORE-NEAR-DISK gives, after translation,
  F_D/D -> B_(1/2)
in Hausdorff distance. Each P_i/D lies in F_D/D, and canonical harmonic-cell
tiling gives pairwise disjoint interiors.

By Blaschke selection, pass to a subsequence on which the three normalized cells
converge to compact convex sets K_1,K_2,K_3 inside B_(1/2). Area continuity gives
  area(K_i) = c/M_* > 0,
and diameter continuity gives
  diam(K_i) = 1.
The limit interiors remain pairwise disjoint: an open disk contained in two limit
interiors would, by convex Hausdorff convergence, force interior overlap for all
sufficiently large prelimit cells.

This contradicts the disk lemma. Hence no canonical full-core sequence can have
  X/D -> alpha_*.

## 5. Uniform non-effective gap

If no absolute gap above alpha_* existed, for every j one could choose a canonical
full-core survivor with D_j -> infinity and
  X_j/D_j < alpha_* + 1/j.
The parent theorem applied to this selected sequence gives liminf X_j/D_j >= alpha_*.
After passing to a subsequence, X_j/D_j -> alpha_*, contradicting Section 4.

Therefore there are constants epsilon_cw > 0 and D_cw < infinity such that
for every canonical full-core Type-II survivor with D >= D_cw,
  q-k-sum_r d_r >= (alpha_* + epsilon_cw) D.

The proof is qualitative; it does not compute epsilon_cw.

## 6. Remaining bottleneck

This removes the exact scalar endpoint of the convex-width/Section-122 route.
It does not close the full-core branch because the current repository has no upper
bound on q-k-sum d_r near 0.1145 D. The next target is either quantitative
stability of the three-cell contradiction or an upper bound on the same X currency
from loaded diameter topology. The macroscopic inactive-container branch is untouched.

No computation is load-bearing. No theorem-state file is changed. Contact-isolated
source points remain retained, and none of the binding rejected routes is used.
