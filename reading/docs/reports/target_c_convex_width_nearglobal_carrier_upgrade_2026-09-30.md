> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_width_nearglobal_carrier_upgrade_2026-09-30.md) · source SHA-256 `3e1e4a45be6f134b1dd18927021e317118a0caf62c3c0303010d62711db4f62c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4EF9BF4EE168","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II - convex-width gap expands the near-global carrier branch

Date: 2026-09-30
Base remote main at final pre-write recheck: 77d418e49da08328f126fcd5bbab21cccb15b639
Depends on:
- target_c_convex_width_explicit_endpoint_gap_2026-09-30.md
- research/target_c_terminal_free_nearglobal_carrier_reduction_2026-09-18.md
- hostile-audited all-regime half-disk dichotomy cited there
Status: proof-only composition; theorem-state authority unchanged; C-II remains open.

Salvaged from source branch `proof/target-c-convex-width-nearglobal-upgrade-20260930` at tip `78256ee767f4ce99c2ea6c634e3bd6bcf9419c4b`; no original PR was found. Lifecycle on this branch: **unreviewed**, noncanonical.


Let
  t_D = (q-k)/D,
  S_D = sum_r d_r,
and let alpha_* be the unique fixed point
  alpha = pi(2-sqrt(3))/20
        + 4(sqrt(1+pi^2/16)-1) / {5[3+(pi-3-alpha)^3]}.
The current convex-width branch proves
  liminf (t_D - S_D/D) >= alpha_+ := alpha_* + 10^(-8),                (1)
with alpha_+ = 0.1145033643028727... .

The September 18 near-global-carrier reduction used only the older strict moment
gap c0=pi(2-sqrt(3))/20=0.042089... at this step. Replacing c0 by (1)
raises its structural threshold from 2.042089... to

  t_NG^+ := 2 + alpha_+ = 2.1145033643028727... .                       (2)

More precisely, every canonical full-core Type-II subsequence with
  t_D -> t < t_NG^+
has, after a further subsequence, an actual positive-area harmonic cell P_w,D
whose normalized Hausdorff limit K is center-wrapping and has diameter exactly one.

## 1. The stronger moment gap is the only scalar input needed

Equation (1) says
  liminf (t_D - S_D/D) >= alpha_+.
Therefore along a subsequence t_D -> t,
  limsup S_D/D <= t-alpha_+.                                           (3)

The hostile-audited all-regime Type-II cell dichotomy has two alternatives after
subsequence extraction.

(A) Two-half-disk alternative. There are two distinct actual defining cell
sequences with normalized diameters tending to one. Hence
  liminf S_D/D >= 2.
Together with (3), this forces
  t >= 2+alpha_+.

(B) Center-wrapping alternative. Let lambda be the limiting normalized diameter
of the selected positive-area wrapping cell. If lambda<1, the uncapped complement-
gap theorem from the September 18 report gives
  liminf S_D/D >= H(lambda)
with
  H(lambda)=2 lambda + 4 lambda sqrt(1-lambda^2).                        (4)
For every center-wrapping lambda in [sqrt(3)/2,1), the elementary calculation
in that report proves H(lambda)>2. Hence (3) gives
  t > 2+alpha_+.

Consequently if t<2+alpha_+, neither the two-half-disk alternative nor a fixed
subunit wrapping diameter is possible. The remaining exhaustive case is

  diam(K)=1.                                                            (5)

This proves the expanded threshold (2). No new use of a common cell-diameter cap
is made.

## 2. Quantitative stability of the diameter-one carrier

Let g_j be the complement gaps of the circle support of K and define
  C(K)=sum_j sin(g_j/2).
The uncapped gap-moment theorem remains valid at diameter one:
  liminf_{D->infinity} (sum_{r != w} d_r)/D >= C(K).                    (6)
The carrier itself contributes one unit to S_D/D, so (3) and (6) give

  C(K) <= t - 1 - alpha_+.                                              (7)

For t<t_NG^+, the right side is below one. Define
  A(x) = [asin(x) - x sqrt(1-x^2)]/4,   0<=x<1.
As in the September 18 proof, the disk area omitted by K is the sum of the
circular-segment areas A(sin(g_j/2)). Since A has increasing derivative and is
superadditive on sums below one, (7) implies

  area(K) >= pi/4 - A(t-1-alpha_+).                                     (8)

Local rhombic saturation transfers the same asymptotic coefficient to the strict-
rhombus area of the selected cell. The canonical local train inequalities therefore
give

  liminf T_w,D/D >= 2[pi/4 - A(t-1-alpha_+)],                           (9)

  liminf a_w,D/D >= (1/3)[pi/4 - A(t-1-alpha_+)].                      (10)

All three statements are exact functional improvements of the September 18
near-global-carrier bounds; only the numerical evaluation uses decimals.

## 3. Concrete overlap with the live pentagon-sea range

The proof-only uniform pentagon-sea theorem has a certified positive pentagon floor
through every fixed endpoint t<=2.0215. Since
  2.0215 < 2+alpha_+,
the entire currently certified pentagon-sea range is now forced into the same
diameter-one center-wrapping carrier branch.

At the worst endpoint t=2.0215, (7) gives
  C(K) <= 0.9069966357... ,
and (8) gives, for orientation,
  area(K) >= 0.59686... .                                               (11)
Thus every survivor in the certified pentagon-sea range must simultaneously have
one near-global diameter-one wrapping carrier occupying more than 0.5968 D^2
limiting area and the independent linear source-empty pentagon population.

This is a structural conjunction, not a contradiction: the present repository does
not yet prove that the pentagon population must lie outside that carrier or consume
a fixed positive area per pentagon.

## 4. Terminal-FREE lower endpoint

At the current terminal-FREE scalar lower endpoint
  t0=1.959852849540479... ,
the strengthened carrier bounds are, for orientation,
  C(K) <= 0.8453494853... ,
  area(K) >= 0.64649... ,
  liminf T_w,D/D >= 1.29298... ,
  liminf a_w,D/D >= 0.21549... .

The corresponding September 18 area floor was about 0.5859, so the new convex-width
gap materially enlarges the forced near-global carrier at the same endpoint.

## 5. Remaining bottleneck

The low-t full-core branch is now narrower:

  t < 2.1145033643...
    => one actual positive-area center-wrapping cell has diameter D-o(D),
       with gap currency and area controlled by (7)-(10).

The complementary branch pays t>=2.1145033643... .

This still does not close C-II. A useful next theorem is now sharply localized:
either couple the forced near-global carrier to the linear pentagon/train/interface
structure and obtain a source-level contradiction, or attack the high-t branch using
the loaded-diameter topology. The macroscopic inactive-container branch remains
separate.

No computation or verifier is load-bearing. No theorem-state file is changed.
