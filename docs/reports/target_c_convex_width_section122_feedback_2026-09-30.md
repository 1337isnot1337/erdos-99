<!-- theorem-state: {"artifact_id":"ART-9585D80DA2DC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II - convex-width / Section-122 feedback

Date: 2026-09-30
Base remote main at final recheck: 77d418e49da08328f126fcd5bbab21cccb15b639
Depends on: target_c_convex_width_outer_detour_floor_2026-09-29.md
Status: proof-only; theorem-state authority unchanged; C-II remains open.

Salvaged from source branch `proof/target-c-convex-width-nearglobal-upgrade-20260930` at tip `78256ee767f4ce99c2ea6c634e3bd6bcf9419c4b`; no original PR was found. Lifecycle on this branch: **unreviewed**, noncanonical.


Notation:
S = sum_r (L_r - 2 d_r),
S_D = sum_r d_r,
X = q - k - S_D,
Q = Q_loc, F = F_loc,
E = sum_r (L_r + P_exc,r - 2 d_r) = S + 4 F + Q.

Current main gives
  0 <= S <= 2 X + 4 c_I - 4 - Q.                                      (1)
Canonical Section 122 gives
  liminf E/D >= c_det := (pi/2)(2 - sqrt(3)).                           (2)
The preceding convex-width report proves, with
  rho = sqrt(1 + pi^2/16), beta = rho - 1, A_r = area(P_r),
  S >= [2/(1+rho)] (sum A_r)^2 / (sum d_r^3),                            (3)
and full-core area saturation gives sum A_r = (pi/4) D^2 - o(D^2).

## 1. Section-122 feedback

Every bounded local nonquadrilateral face has degree at least five, so F <= Q.
From (1), S + Q <= 2 X + 4 c_I - 4. Therefore
  E = S + 4F + Q
    <= S + 5Q
    = 5(S+Q) - 4S
    <= 10X + 20 c_I - 20 - 4S.                                         (4)
Since c_I = o(D), (2) and (4) imply
  liminf X/D >= c_det/10 + (2/5) liminf S/D.                            (5)

## 2. Self-consistent cubic bootstrap

Set x = liminf X/D. Equation (1) gives x >= 0. If x >= pi-3, the final
bound below is automatic. Assume x < pi-3.

Since q-k <= q <= per(F) <= pi D,
  S_D = q-k-X <= pi D-X.                                                 (6)
For every fixed eps > 0, eventually S_D/D <= pi-x+eps.
Put z_r=d_r/D. Then 0 <= z_r <= 1. If sum z_r <= B in [3,4), convexity
of t^3 gives
  sum z_r^3 <= 3 + (B-3)^3.                                              (7)
Hence
  limsup (sum d_r^3)/D^3 <= 3 + (pi-3-x)^3.                              (8)
Using (3) and pi^2/[8(1+rho)] = 2(rho-1) = 2 beta gives
  liminf S/D >= 2 beta / [3 + (pi-3-x)^3].                               (9)
Substitute (9) into (5):
  x >= T(x) := pi(2-sqrt(3))/20
                + 4 beta / {5[3+(pi-3-x)^3]}.                           (10)

On [0,pi-3],
  T'(x) = 12 beta (pi-3-x)^2 / {5[3+(pi-3-x)^3]^2} < 1.
So x-T(x) is strictly increasing and has a unique zero alpha_* in (0,pi-3).
Equation (10) therefore proves
  liminf (q-k-sum d_r)/D >= alpha_*,                                    (11)
where alpha_* is the unique solution of
  alpha = pi(2-sqrt(3))/20
        + 4(sqrt(1+pi^2/16)-1) / {5[3+(pi-3-alpha)^3]}.                 (12)
Numerically alpha_* = 0.1145033543028727...

Feeding alpha_* back into (9) gives
  liminf S/D >= sigma_* = 0.1810349839475651... .                        (13)
The preceding branch floor for X/D was 0.0905130297..., so this feedback
raises the proved diameter-moment gap to 0.1145033543... .

## 3. Endpoint rigidity

If X/D -> alpha_*, then (4), (9), and the fixed-point identity force
  S/D -> sigma_* and E/D -> c_det.
Set q_* = 2 alpha_* - sigma_* = 0.04797172465818027... .
Equation (1) gives limsup Q/D <= q_*. Since E <= S+5Q and
c_det + 4 sigma_* = 10 alpha_*, the reverse liminf holds. Hence
  Q/D -> q_*.
Then E=S+4F+Q gives
  F/D -> q_* and (Q-F)/D -> 0.
Because Q-F equals the sum of deg(R)-5 over local nonquadrilateral faces R,
any endpoint sequence is asymptotically pentagon-saturated: total degree
excess above pentagons is o(D). Also
  (sum P_exc,r)/D -> 5 q_* = 0.2398586232909013... .

## 4. Remaining bottleneck

The full-core branch now satisfies (11). A closing step must upper-bound the
same X currency below this lower bound, or rule out the simultaneous endpoint
profile using the actual loaded diameter topology. The macroscopic inactive-
container branch is untouched.

No computation is load-bearing. No theorem-state file is changed. Contact-isolated
source points remain retained, and none of the binding rejected routes is used.
