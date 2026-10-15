<!-- theorem-state: {"artifact_id":"ART-E2759D9C2661","canonical":true,"claim_ids":["C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE"],"claim_statuses":{"C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.199 — two-thirds global population reserve

Date: 2026-10-09. Audit base: `origin/main=49b3ad7a57c932ecd8c40e5ff21a9944c6c3b833`,
state `2026-10-09.audit.192`; C-II and Level I remain open.

Frozen candidate: `origin/research/level-i-fused-review-20261009` at
`6132201c1d3056ca68a222217094acb819f5b4d7`. Audited source artifact: the
[candidate report](../reports/target_c_full_source_lattice_conflict_deletion_reserve_2026-10-09.md),
SHA-256 `a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2`.

## Verdict

**PASS — promote `C-GLOBAL-POPULATION-EXCESS-TWO-THIRDS-RESERVE`.** There
is an absolute `kappa>0` such that for every planar unit-separated global
`n`-point diameter minimizer with diameter `D>=2`,

\[
 g_A=n-1-\frac{\pi D^2}{2\sqrt3}\ \ge\ \kappa D^{2/3}.
\]

The proof uses an independent triangular-lattice competitor and global
optimality only at the final subset comparison. It applies to every global
minimizer and does not assert any structural property of its source. The older
explicit square-root reserve remains separately canonical: the new unspecified
absolute constant proves the stronger asymptotic order but is not certified to
dominate that older finite-range bound at every `D>=3`.

This does not prove a triangle in every large minimizer, provide a source-level
move, close C-II, or solve Level I.

## Independent reconstruction

Let `Lambda` be the unit triangular lattice and `a0=sqrt(3)/2` its covolume.
First, uniformly over translations and for open or closed disks of radius
`r>=2`,

\[
 \#((z+\Lambda)\cap B_r)=\frac{\pi r^2}{a_0}+O(r^{2/3}).
\]

For completeness, choose a nonnegative smooth unit-mass mollifier supported
in the unit disk and scale it to radius `t`. The disk transform has bound
`|\widehat{1_{B_R}}(\xi)|\le C\sqrt R|\xi|^{-3/2}`: the divergence-theorem
boundary integral is split into arcs of angular width `eta` around its two
stationary points and their complement. The near arcs contribute
`O(R eta/|xi|)`; integration by parts on the remaining monotone-phase arcs
contributes `O(1/(|xi|^2 eta))`. Taking
`eta=(R|xi|)^{-1/2}` proves the bound when `R|xi|` is large, while the area
bound covers the remaining range. Smoothness of the mollifier gives Fourier
decay `O((1+t|xi|)^-3)`. The reciprocal lattice is separated and has
`O(T^2)` points in a radius-`T` disk, so dyadic summation gives

\[
 \sum_{k\in\Lambda^*\setminus\{0\}}|k|^{-3/2}(1+t|k|)^{-3}=O(t^{-1/2}).
\]

The periodized convolution therefore has absolutely convergent Fourier series
and, uniformly over the translate, differs from its mean by
`O(sqrt(R/t))`. Convolutions of radii `r-t` and `r+t` sandwich respectively
the open and closed disk counts; the mean area error is `O(rt+t^2)`. Taking
`t=r^{-1/3}` gives the stated `O(r^{2/3})` discrepancy, including lattice
points on either boundary.

Put `A1=pi/a0`, choose `0<c<=1`, and set

\[
 \delta=cD^{-1/3},\qquad S=D/2+\delta.
\]

The possible difference vectors between two lattice sites in the open
radius-`S` disk whose distance is at least `D` lie in
`W={w in Lambda : D<=|w|<D+2delta}`. Applying the uniform disk estimate to
an outer closed disk and inner open disk gives, for `D>=2`,

\[
 |W|\le K_0D^{2/3},\qquad K_0=8\pi/a_0+3C_{disk}.
\]

If two radius-`S` disks have center distance `2S-epsilon`, their common
half-height at abscissa `x` is at most
`sqrt(2S(epsilon/2-|x|))`. Integration yields lens area at most
`(4/3)sqrt(S) epsilon^(3/2)`. Hence every `w in W` contributes lens area at
most `(8sqrt(2)/3)c^(3/2)`.

Translate `Lambda` uniformly over a fundamental parallelogram. Let `N` be
the number of lattice sites in the open radius-`S` disk and `E` the number of
unordered pairs in it at distance at least `D`. Unfolding the finite sums gives

\[
 \mathbb EN=\frac{\pi S^2}{a_0},\qquad
 \mathbb EE=\frac1{2a_0}\sum_{w\in W}A_{lens}(S,|w|)
 \le K_1c^{3/2}D^{2/3},\quad
 K_1=\frac{4\sqrt2}{3a_0}K_0.
\]

The factor `1/2` counts each unordered pair once; the interval for `W`
includes ties at distance exactly `D`. Choose

\[
 c=\min\{1,(A_1/(2K_1))^2\},\qquad \kappa=A_1c/2>0.
\]

The mean of `N-E` therefore satisfies

\[
\mathbb E[N-E]\ge\frac{\pi D^2}{4a_0}+\kappa D^{2/3}.
\]

Since `N-E` is integer-valued, some translate attains at least this mean. In
that translate, delete one selected endpoint of every conflict edge. The union
of deleted endpoints has size at most `E`, and the remaining lattice subset
has diameter strictly below `D`: every pair of distance at least `D`,
including a tie, was covered by a deleted endpoint. Its cardinality is at
least

\[
 \frac{\pi D^2}{4a_0}+\kappa D^{2/3}
 =\frac{\pi D^2}{2\sqrt3}+\kappa D^{2/3}.
\]

If this cardinality were at least `n` for a global `n`-point minimizer,
any `n`-point subset would have diameter below `D`. Thus its integer size is
at most `n-1`, yielding the claimed reserve without rounding loss.

## Hostile checks and limits

- The comparison counts all lattice difference vectors in the thin annulus,
  not a selected outer bank; the per-vector lens factor gives the profitable
  `c^(3/2)` cost.
- Distance-`D` ties are counted as conflicts, which is necessary for strict
  diameter reduction.
- Deletion occurs only in the independent comparison lattice. No original
  minimizer label is removed, moved, or assumed to lie in a lattice.
- The all-minimizer quantifier follows from the strict-subset contradiction;
  no triangle-free restriction, contact-minimality, KKT condition, or stress
  hypothesis enters.
- The source report's separate shell, one-lattice-interior, contact-face, and
  optimized-coefficient claims are outside this audit and remain unreviewed.

No finite verifier certifies this analytic estimate. The source branch's
`verify_target_c_two_port_triangular_limits_2026_10_09.py` concerns a different
finite two-port claim and is not used as evidence here.

## Canonical disposition

Promote the all-minimizer `D^(2/3)` reserve with no theorem dependency. Keep
`C-GLOBAL-POPULATION-EXCESS-SQRT-RESERVE` canonical as the explicit finite-range
bound; no uniform dominance relation is claimed for the unspecified `kappa`.
The exact source-wide shell/interface upper bound needed to turn this reserve
into a Level I contradiction remains unproved. C-II and Level I are unchanged.

### Later dependency registration

At the original Audit.199 promotion, the strict-sub-`D` lattice competitor was part of the proof but had no separate theorem ID. Audit.245 now registers that exact construction as `C-TRIANGULAR-LATTICE-STRICT-D-COMPETITOR-RESERVE`; the current theorem-state graph records the resulting dependency of this all-minimizer reserve. The theorem and proof above are otherwise unchanged.
