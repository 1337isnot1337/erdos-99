> Generated reading edition · [exact source](../../../docs/reports/target_c_wrapping_rooted_detour_2026-09-30.md) · source SHA-256 `27ec7c5f10f471c1e5525d0955a854dd79ae19c17bdb4e94376e2b1a9bad91af`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7CC1135BA383","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- wrapping-rooted detour

Base main: 5d61bba7f20a5e0600f2c9c1cd9636190f03d4f3. Proof-only; C-II open.

Let S=sum d_r, X=q-k-S. If a positive-area center-wrapping harmonic cell P_* has
d_*/D -> lambda, then the current chord dissection can be rooted at P_*.

The near-disk short-arc estimate has constant C_D->1. Each complementary region
of P_* is a short-arc cap. Splitting a cap by chord f gives
d_1+d_2 <= d_parent+C_D|f|. Summing over all cap chords yields
sum_faces diam(F) <= d_*+C_D I_D.
Together with sum_faces per(F)=per(F_D)+2I_D, I_D=O(D), and per(F_D)=(pi+o(1))D,

sum_faces(per(F)-2diam(F)) >= (pi-2lambda-o(1))D.

The current gap-detour estimate is o(D), so
sum_r(per(P_r)-2d_r) >= (pi-2lambda-o(1))D.
Using L_r>=per(P_r) and the exact upper ledger gives
X >= (pi/2-lambda-o(1))D.

Current main also gives
S >= (2lambda+4lambda sqrt(1-lambda^2)-o(1))D.
Hence
q-k >= (pi/2+lambda+4lambda sqrt(1-lambda^2)-o(1))D.
Since q <= (pi+o(1))D,
lambda+4lambda sqrt(1-lambda^2) <= pi/2.
The left side is strictly decreasing on [sqrt(3)/2,1], so
lambda >= 0.9891345915624005..., the unique root of equality.

The two-half-disk alternative already has diameter-(1-o(1))D defining cells.
Thus the standard cap-family transfer gives an actual quadratic-area locally
rhombus-saturated carrier with diameter at least
(0.9891345915624005...-o(1))D.

Both full-core alternatives also imply
q-k >= (1+pi/2-o(1))D and k <= (pi/2-1+o(1))D.
Thus r_H=2h-q >= (2-o(1))D; in the Woodall forest branch,
sum_j(q_j-2) >= (2-o(1))D.

No computation is load-bearing. The unresolved step is to couple this near-extremal
diameter topology to the inverse-phase train families; the inactive-container branch
is unchanged.
