# Target C — audited §155 quantitative atomic endpoint / outer-detour stability

**Date:** 2026-09-12  
**Lifecycle:** audited-working proof-only route module; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module restores and normalizes the valid all-regime theorem from the historical proof file
`research/target_c_section149_quantitative_atomic_detour_stability.md`. The old internal §149 numbering is provenance only. The active normalized label is **§155**.

Section §154 handles the exact zero-normalized-detour endpoint. Section §155 quantifies the same mechanism for arbitrary normalized outer detour.

Put

\[
\Delta_2={\pi\over2\sqrt3},\qquad s_2=\sqrt{\Delta_2},
\]

and along a Type-II subsequence write

\[
\delta={b-\operatorname{per}(F)\over D}\to\delta\ge0,
\qquad {T\over D}\to x.
\]

## 155.1 Fourier control of outer endpoint atoms

Let

\[
\nu_D={1\over D}\sum_{e\in\partial_{out}C}^{occ}\delta_{\theta_e}
\]

and let `nu` be a weak limit. Its mass is `pi+delta`. Projection variation of the actual occurrence-counted outer walk gives

\[
C\nu(\alpha):=\int|\cos(\theta-\alpha)|\,d\nu(\theta)\ge2.
\]

Writing `g=C\nu-2>=0`, its mean is `2delta/pi`. The Fourier series of `|cos|` therefore gives for every `n>=1`

\[
\boxed{|\widehat\nu(n)|\le\delta(4n^2-1).}
\tag{155.1}
\]

The constant is correct: the complex Fourier coefficient of `|cos|` at projective frequency `n` has modulus `2/[pi(4n^2-1)]`, and every Fourier coefficient of a nonnegative function is bounded by its mean.

Quotient projective directions by `theta~theta+pi/3`. Let `A_j` be the atom masses of the pushed-forward outer endpoint measure. For the Fejer kernel of order `N>=2`, positivity and `K_N(0)=N` give

\[
N\sum_jA_j^2
\le (\pi+\delta)^2
+2\sum_{m=1}^{N-1}\left(1-{m\over N}\right)|\widehat\nu(3m)|^2.
\]

Hence

\[
\boxed{
\sum_jA_j^2\le U_N(\delta),
}
\tag{155.2}
\]

with

\[
\boxed{
U_N(\delta)
={ (\pi+\delta)^2\over N}
+{2\delta^2\over N}
\sum_{m=1}^{N-1}\left(1-{m\over N}\right)(36m^2-1)^2.
}
\tag{155.3}
\]

## 155.2 Train-orbit mass and bounded endpoint capacity

Audited §142 implies that asymptotically all quadratic rhombus crossings occur at projective separation `pi/3`. Group the atoms of the limiting empirical train-direction probability measure by the same three-direction phase orbits and let their masses be `S_j`.

Within each orbit the limiting crossing graph is triangle-free. Weighted Mantel therefore gives

\[
\boxed{
\sum_jS_j^2\ge {4\Delta_2\over x^2}.
}
\tag{155.4}
\]

Let `C_j` be the normalized bounded-defect endpoint incidence mass in orbit `j`. Every train supplies two endpoint incidences, so after the standard fixed-window then shrinking-window limit,

\[
2xS_j\le A_j+C_j.
\]

The exact §143 endpoint multigraph gives

\[
\sum_jC_j\le \liminf {Q+4f\over D}.
\]

Using `ell^1>=ell^2`, the triangle inequality, (155.2), and (155.4),

\[
\boxed{
\liminf {Q+4f\over D}
\ge
\left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+.
}
\tag{155.5}
\]

Since `f<=Q`,

\[
\boxed{
\liminf {Q\over D}
\ge {1\over5}
\left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+.
}
\tag{155.6}
\]

Finally `b+Q=2(q-k)` and `b/D->pi+delta`, so if

\[
t=\lim{q-k\over D},
\]

then

\[
\boxed{
 t\ge {\pi+\delta\over2}
 +{1\over10}
 \left(4\sqrt{\Delta_2}-\sqrt{U_N(\delta)}\right)_+.
}
\tag{155.7}
\]

This is the durable all-regime theorem.

## 155.3 Explicit separation above the §146 endpoint

Let

\[
C_{146}={4\over9}(\pi+s_2)=1.8195135379794445\ldots .
\]

The audited §146 inequalities imply

\[
\delta\le {9\over4}(t-C_{146})-{1\over4}{k\over D}+o(1)
\le {9\over4}(t-C_{146})+o(1).
\tag{155.8}
\]

For `N=7`, direct summation gives

\[
\sum_{m=1}^{6}\left(1-{m\over7}\right)(36m^2-1)^2=687459,
\]

hence

\[
\boxed{
U_7(\delta)={ (\pi+\delta)^2+1374918\,\delta^2\over7}.
}
\tag{155.9}
\]

If `t<=C_146+1/2000+o(1)`, then (155.8) gives `delta<=9/8000+o(1)`. At this detour,

\[
\sqrt{U_7(\delta)}<1.289,
\]

so (155.5) gives asymptotic bounded-endpoint capacity strictly above `2.5202D`. But `Q+4f<=5Q` and `Q/D=2t-pi-delta+o(1)` give an upper bound below `2.493D`. Contradiction.

Therefore

\[
\boxed{
\liminf {q-k\over D}
\ge C_{146}+{1\over2000}
=1.8200135379794445\ldots .
}
\tag{155.10}
\]

The numerical increment is secondary. The main reusable result is (155.5)–(155.7), which charges phase-orbit endpoint atoms directly to the same outer-detour currency that survives §154.

## 155.4 Audit disposition

The following points were independently checked.

- The Fourier coefficient in (155.1) has the correct normalization and sign-insensitive modulus.
- Fejer positivity gives an upper bound on atomic `ell^2` mass even in the presence of a nonatomic part; off-diagonal contributions are nonnegative.
- The `pi/3` quotient is necessary: total atomic mass alone is not quantitatively stable under weak convergence.
- Weighted Mantel is applied orbit-by-orbit to a simple triangle-free train-crossing graph, giving (155.4) with the factor `1/4`.
- Endpoint incidence is occurrence-counted. Bridges and singleton trains remain included in the exact §143 handshake.
- From `2xS_j<=A_j+C_j`, the reverse triangle argument is valid: `2x||S||_2<=||A||_2+||C||_2`.
- The explicit `N=7` polynomial and the `+1/2000` numerical contradiction were recomputed independently.
- No contact-isolated source point is deleted or inserted into the core rigidity matrix.
- No rejected `1.9046256...` unconditional hull floor is used.

**Final disposition:** PASS at audited-working proof-only scope. The theorem strengthens the full-core Type-II lower-density frontier but does not close Type II, C-II, or the macroscopic inactive-container branch.
