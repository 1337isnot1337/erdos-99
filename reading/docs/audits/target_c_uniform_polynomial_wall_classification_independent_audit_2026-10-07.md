> Generated reading edition · [exact source](../../../docs/audits/target_c_uniform_polynomial_wall_classification_independent_audit_2026-10-07.md) · source SHA-256 `47afa61540b11e0b5aeda0712e517a45160dbc7dde8f57b32b817d62b37bde7a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F15C0DF99D0A","canonical":true,"claim_ids":["C-ARITHMETIC-SIX-WALL-POLYNOMIAL-MAXIMUM-CLASSIFICATION","C-ARITHMETIC-SIX-WALL-POLYNOMIAL-SOURCE-EXCLUSION"],"claim_statuses":{"C-ARITHMETIC-SIX-WALL-POLYNOMIAL-MAXIMUM-CLASSIFICATION":"canonical","C-ARITHMETIC-SIX-WALL-POLYNOMIAL-SOURCE-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.107 — uniform arithmetic-wall maximum classification

**Date:** 2026-10-07  
**Base:** origin/main=60792e909aac445df7b87f329451ba4f0ee6b4c6, state 2026-10-07.audit.106  
**Target:** C-II; C-I closed, C-II and Level I open  
**Verdict:** **PASS WITH NARROWED SCOPE — promote the joint growing-M arithmetic-wall classification and its canonical-source corollary.**

## Run lock and implication chain

The candidate chain is

> uniform effective wall chart -> quantitative positive stress and finite isolation -> exact sorting-packet classification for all M in one polynomial interval -> unit triangle when the interior population is maximal -> exclusion of the entire specified wall from a canonical triangle-free source.

The source-level conclusion is only for the prescribed arithmetic six-sided wall. It does not extract such a wall from an arbitrary canonical minimizer, so the global C-II and Level I frontiers do not change.

## Frozen source and audit boundary

The source branch was refreshed after Audit.106 and remained at
`research/sol/target-c-overnight-closure-20261007`, tip
`c6a75bd708e553c4feb3a540e0b17f3b65e22a82` (66 ahead, 25 behind current
main). The audited report was introduced at immutable commit
`da2dea41e45c9c46d4365d0758370861b4e319fc`; the report, verifier, and saved
certificate are unchanged at the branch tip. The report SHA-256 is
`48b55c2bb6c888f754b8670a374a8ee531bb94a962b8b673df8bd433e83e8e29`.

Source artifact:
`docs/reports/target_c_uniform_polynomial_maximum_wall_classification_2026-10-07.md`.

This audit covers the report's Sections 1–6. Its exact path verifier is
corroborative only. I did not promote the neighboring arbitrary-container
Delaunay transfer or the separate finite radial-lifting certificate.

## Exact promoted statements

Put

$$
a_h=M-1-2h\quad (0\le h<M),\qquad N=3M^2-3M+1.
$$

There is one absolute constant $c_*>0$, independent of M and of the rate
permutation, such that for every $M\ge4$ and
$0<\theta\le c_*M^{-40}$, every pairwise unit-separated union of all
$6M$ vertices of the specified arithmetic six-sided wall and exactly N
additional points in its strict interior has its interior point set equal,
after wall alignment and point relabeling, to a sorting packet associated
with some permutation of $(a_h)$. Each such packet contains the center and
two adjacent first-ring sites at mutual distances one, so the union contains
an actual unit equilateral triangle.

The packet statement is an existence-of-a-representation claim; no uniqueness
of the permutation label is needed or asserted.

As a corollary, for the same M and theta range, no contact-minimal then
diameter-pair-minimal triangle-free global minimizer can contain the complete
specified arithmetic wall. The canonical Oler cap bounds its strict-interior
population by N; the promoted one-deficit source exclusion rules out
populations at most N-1 while retaining all exterior points and contact
isolates; at population N the classification supplies a unit triangle.

## Canonical dependencies

The uniform chart input is `C-ARITHMETIC-SIX-WALL-UNIFORM-CHART`: in its
stated $\theta\le1/(10000M^3)$ range, every maximal cloud is within
$1000M^4\theta$ of the full triangular-lattice chart after rigid alignment.
The exact nested ring/axis stress identities are used only for their selected
strong rows and central-chain energy bound, within
`C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND`'s stated geometry. The exact
fixed-profile sorting construction from
`C-SIX-SIDED-WALL-PROFILE-SORTING-CLASSIFICATION` is compatible with the
packet formulas, but the uniform classification below is reconstructed
quantitatively rather than inferred from that theorem's fixed-M onset.

For the source corollary, I use
`C-ONE-DEFICIT-ARITHMETIC-WINDOW-OLER-CAP` and
`C-ONE-DEFICIT-ARITHMETIC-WINDOW-SOURCE-EXCLUSION`. The chosen $c_*$ is
small enough that $c_*M^{-40}\le1/(100M^3)$ for all M≥4. Those canonical
exchanges retain the entire exterior source and every contact isolate.

## Independent proof reconstruction

### Uniform flat-row inverse

Let J be the complete moving-involving unit-contact row set of a sorting
packet, evaluated first at the flat chart $\theta=0$. Let S consist of
all ring rows and the six radial axes (including the corner guards). For a
moving displacement x with the wall fixed, set

$$
\eta=\|R_0[J]x\|_\infty.
$$

Radial telescoping from the pinned corners gives axial radial components at
most $M\eta$; the central displacement is at most $2M\eta$. Ring-row
sums bound the variation between the six axial tangential components on a
ring by $4M\eta$. Taking one component $\alpha_r$ as the ring value,
the axial vectors differ from $\alpha_rJ(e_k)$ by at most $21M\eta$.

For each off-axis sector point, its u-coordinate determines a scalar
$s_{r,j}$; replace its v-coordinate by the value required by the ring
kernel. Summing ring residuals bounds this change by $26M\eta$. This gives
a linear projection $P_L$ onto the strong-row kernel L with

$$
\|x-P_Lx\|_\infty\le26M\eta.
$$

After this projection, each weak recurrence row has residual at most
$62M\eta$ after division by $c=\sqrt3/2$. For the path selecting the
j smallest full rates, telescoping from the center to the pinned outer side
gives each threshold subset sum error at most $62M^2\eta$. Taking adjacent
threshold differences bounds every increment
$t_h=\alpha_{h+1}-\alpha_h$ by $124M^2\eta$; summing the increments
bounds $|\alpha_r|\le124M^3\eta$. Applying the same path estimate to each
interior sector point gives $|s_{r,j}|\le186M^3\eta$. In Cartesian
coordinates this yields

$$
\|x\|_\infty\le500M^3\eta,
\qquad \sigma_{\min}(R_0[J])\ge(1000M^4)^{-1}.
$$

The last inequality follows by converting the max-coordinate bound to
Euclidean norm over at most $3M^2$ moving points. The same projection gives
$\sigma^+_{\min}(R_0[S])\ge(52M^2)^{-1}$, since the distance to L is at
most $26M\|R_0[S]x\|_\infty$. These are explicit threshold-path bounds,
not a generic-rank or floating-singular-value inference.

### Positive stress uniform in M and the permutation

The central six-chain stress $\lambda^p$ has unit coefficients on the six
radial chains. For its first row derivative, the action on L is

$$
g_0\cdot x=12\sum_h a_{\pi(h)}t_h.
$$

Sort the rates as $b_0<\cdots<b_{M-1}$, and let I_j be the j smallest
rates. Abel summation gives

$$
\sum_j b_jt_{\pi(j)}=-\sum_{j=1}^{M-1}(b_j-b_{j-1})\sum_{h\in I_j}t_h.
$$

Each threshold path has row sum $c\sum_{I_j}t_h$. Distributing the
six-sector path representation assigns weak-row coefficients

$$
\mu_e=\frac2c\sum_{\text{threshold paths containing }e}(b_j-b_{j-1}).
$$

Every active weak row lies on a threshold path, and every adjacent rate gap
is exactly two. Thus each weak coefficient is at least $4/c$, while a row
occurs in at most M−1 thresholds, giving $\mu_e\le C M$. The difference
$g_0+R_0^T\mu$ annihilates L, hence lies in the strong-row span. The
positive singular bound for S gives a strong correction $\nu$ with
$\|\nu\|_2\le C M^4$. Consequently

$$
\lambda_1=(\mu-\nu)/2,\qquad R_0^T\lambda_1=-R_1^T\lambda^p,
$$

and all weak coefficients of $\lambda_1$ are uniformly positive.

Add $\epsilon=c_0M^{-7}$ times the remaining nested stresses so that every
strong row has coefficient at least $\epsilon$. Their total first-force
correction is at most $C\epsilon M^3$; the $R_0^T$ right inverse
corrects $\lambda_1$ by at most $C\epsilon M^7$. A fixed sufficiently
small absolute $c_0$ keeps every weak first-order coefficient positive.
The row matrices have bounded incidence degree and their entries and first
two $\theta$-derivatives are respectively $O(M)$ and $O(M^2)$, since
$|a_h|\le M$. For $\theta\le cM^{-11}$, the active-row singular bound
persists with right-inverse norm at most $2000M^4$. Correcting
$\lambda_0+\theta\lambda_1$ by $O(\theta^2M^9)$ therefore gives an
exact stress $\lambda_\theta$ satisfying

$$
R_\theta^T\lambda_\theta=0,\qquad
\min_e\lambda_{\theta,e}\ge\theta/2,\qquad
\sum_e\lambda_{\theta,e}\le C M.
$$

Every bound is independent of the rate permutation. The exact rational
certificate checks path coverage and finite linear identities; the
polynomial conditioning and stress-continuation estimates above are analytic.

### Finite isolation and arbitrary-cloud classification

For any feasible displacement x from a sorting packet with the same wall,
each active unit row obeys $(R_\theta x)_e\ge-2\|x\|_\infty^2$. The exact
positive stress has zero weighted sum on these rows. Its coefficient floor
and total mass give

$$
\|R_\theta x\|_\infty\le C M\|x\|_\infty^2/\theta.
$$

The perturbed row inverse then yields

$$
x\ne0\quad\Longrightarrow\quad\|x\|_\infty\ge c\theta/M^4.
$$

This is a finite isolation radius; no differentiable path of competing
clouds is assumed.

Now take any maximal cloud in the claim. The canonical uniform chart gives
$\|\delta\|_\infty\le1000M^4\theta$ from the flat chart. Divide by
$\theta$, incorporate the prescribed wall first field, and expand all
nearest-neighbor lower inequalities, including wall-neighbor rows. The
quadratic row error is at most $C M^8\theta$ after division by theta.
Summing the nested strong rows, whose boundary first-field terms are the
specified corner data, bounds each strong residual by $\eta\le C M^9\theta$.
The projection above gives a strong-kernel field within $CM^{10}\theta$.
The weak recurrences then have error $\zeta\le CM^{10}\theta$; every
threshold path yields

$$
\sum_{h\in I}t_h\ge B_j-\rho,\qquad B_j=-j(M-j),\qquad
\rho\le CM^{11}\theta.
$$

Put $\bar t=(M-1)t/(M-1+\rho)$. Since $|B_j|=j(M-j)\ge M-1$,
these inequalities and $\sum t_h=0$ imply $\bar t$ lies in the exact
permutahedron of the arithmetic rates. The initial chart bound gives
$\|t-\bar t\|_2\le CM^{15}\theta$.

For the six radial chains, writing their actual edge vectors as
$y_{r,k}$, their endpoints are $L(\theta)e_k$, where
$L(\theta)=\sum_h\cos(a_h\theta)$. Since $|y_{r,k}|\ge1$, expansion
against the flat unit direction gives the exact lower bound

$$
\sum_{k,r}|y_{r,k}-e_k|^2\ge12(M-L(\theta)).
$$

Taylor expansion of L yields $6\sum a_h^2-CM^5\theta^2$ after division
by $\theta^2$. Replacing the approximate field by its strong-kernel
projection changes the chain energy by at most $CM^{15}\theta$; replacing
t by $\bar t$ costs at most $CM^{20}\theta$. Because the squared norm
is maximized on this permutahedron at its permutation vertices, this proves

$$
0\le\sum_h a_h^2-\|\bar t\|_2^2\le CM^{20}\theta.
$$

The variance identity for a convex combination of permutations supplies a
permutation $t^*$ with $\|\bar t-t^*\|_2\le CM^{10}\sqrt\theta$.
Threshold paths control all remaining sector coordinates and give
$\|d-d^*\|_\infty\le CM^{16}\sqrt\theta$. The exact packet differs from
its first-order approximation by at most $CM^3\theta^2$; therefore the
cloud lies within $CM^{16}\theta^{3/2}$ of that packet.

Choose $c_*>0$ below the finitely many absolute constants needed for the
effective chart, the $M^{-11}$ stress continuation, exact packet
feasibility, the $1/(100M^3)$ one-deficit/Oler range, and
$CM^{20}\sqrt\theta<c_{\rm iso}$. With
$\theta\le c_*M^{-40}$, the last condition is uniform in M. The cloud is
strictly inside the finite isolation radius of a feasible sorting packet,
so it equals that packet. This explains the exponent 40 and proves an
existential universal $c_*$; it does not provide a numerical value.

## Verifier audit

I inspected and executed
`research/verify_target_c_uniform_sorting_threshold_paths_2026_10_07.py` from
the frozen source snapshot. It uses integer dictionary coefficients and
exhausts all 46,232 permutations for M=2,...,8, checking coverage of
1,246,964 active weak rows and 4,166 exact subset-path linear identities
(the linear-identity check is run through M=6). Its saved JSON matched the
reproduced output byte for byte, SHA-256
`2df67164746639875228d880f41fea035712ccf857f9ebc2da0e1b02728e276f`.
This certificate corroborates finite threshold coverage and identities. It
does not prove the all-M polynomial estimates, singular-value bounds, exact
stress continuation, or arbitrary-cloud classification.

## Hostile scope checks

- The profile has adjacent rate gap exactly two. No uniform theorem for
  profiles with arbitrarily small gaps is promoted.
- The joint range is only $\theta\le c_*M^{-40}$; it does not extend the
  result to $\theta$ of order $M^{-3}$ or $M^{-1}$.
- M≥4 is retained for the canonical one-deficit source exclusion. This audit
  does not extrapolate that exchange to M=3.
- The wall constraints are weak pairwise unit separation; existing wall
  contacts are allowed. The proof includes all wall-neighbor rows.
- Exterior source points and contact isolates do not enter the fixed-wall
  classification. In the source corollary, the canonical one-deficit theorem
  retains them rather than dropping them.
- The exact stress gives finite local isolation, but the argument does not
  infer a feasible finite source motion from first-order data.
- No arbitrary canonical source is shown to contain this arithmetic wall.

No counterexample to the narrowed theorem was found.

## Canonical disposition and remaining frontier

Promote `C-ARITHMETIC-SIX-WALL-POLYNOMIAL-MAXIMUM-CLASSIFICATION` and its
corollary `C-ARITHMETIC-SIX-WALL-POLYNOMIAL-SOURCE-EXCLUSION` at the scopes
above. This strengthens Audit.78's fixed-M classification for one arithmetic
profile family to a common shrinking interval as M grows. It does not replace
the profile-general fixed-M theorem or Audit.80's wider one-deficit window.

The remaining curved-wall obligation is to extract a useful wall or an
equivalent strict packet from an arbitrary canonical source. The full-core
face-coupled finite-move obligation is unchanged. C-II and Level I remain
open.

## Audit.242 clarification — interior isolate accounting

The `z<=N-1` source-exclusion branch inherited from Audit.80 deletes the full
strict-interior label set, including any interior contact isolates, and one
wall vertex, then inserts `z+1` packet points. Every interior label is
counted in `z`; all points outside the wall, including exterior contact
isolates, remain. No identity-preserving retention of interior isolates is
asserted. The `z=N` branch is separately ruled out by the unit-triangle
classification, so the polynomial-window source-exclusion result is
unchanged.
