<!-- theorem-state: {"artifact_id":"ART-2A933BD3F74D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B — a zero-gradient stress endpoint admits mixed-order descent

**Date:** 2026-10-03
**Research base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**State version:** `2026-09-14.audit.51`
**Classification:** proved candidate awaiting promotion; lifecycle unreviewed.
**Level I / Target B:** STILL OPEN.
**Run type:** closing proof for the four-persistent-bar case-3 endpoint.
**Literature:** none imported.

## 1. New theorem and implication

Work in the finite pure strict-unit-rhombus disk train chart of canonical
Target B Sections 37, 41--43. Every train angle is an independent local
coordinate. The actual source contact graph is this connected pure disk;
no source point is omitted. Retain every active or inactive pair.
For each actual active diameter `h`, put

\[
r_h(\theta)=\sum_\tau d_{h\tau}u(\theta_\tau),\quad
d_{h\tau}\in\{-1,0,1\},\quad
f_h=|r_h|^2-D^2,\quad g_h=\nabla f_h(\theta^0).
\]

Use `L=intersection_h ker(g_h)` and the canonical backward-kernel space
`K=ker(B) subset L`. Let `J` be precisely the persistent bars, those whose
quadratic form vanishes identically on `K`; every other bar has a nonzero
negative-semidefinite quadratic form on `K`.

**Theorem ZM.** Suppose `K!=0`, `h_0 in J`, and `g_0=0` in the full train
coordinates. Let `J'=J\{h_0}` and `r=rank{g_h:h in J'}`.
Suppose there is `v in K` such that the cubic coefficient `C_h(v)` of
`f_h(theta^0+tv)` satisfies

\[
\sum_{h\in J'}\mu_h C_h(v)<0
\quad\text{for every nonzero }\mu\ge0
\text{ with }\sum_{h\in J'}\mu_hg_h=0.                       \tag{1}
\]

If `h_0` has at least `r+2` positive collinear separating contributions,
then an actual same-cardinality strict diameter descent exists. In
particular this holds whenever `D>r+1`.

The motion is explicit up to solving a finite linear system and a strict
linear feasibility problem:

\[
\boxed{\theta(t)=\theta^0+tv+\epsilon t^2a+t^3b.}              \tag{2}
\]

Here `a` is supported on at most `r+2` positive separating trains of `h_0`,
has zero sum, and is neutral to every persistent gradient. The zero-gradient
bar shortens at fourth order; all other persistent bars shorten at third
order. Nonpersistent bars still shorten at second order.

```text
case-3 singleton zero-gradient endpoint + rank <= 2 + nonzero weighted cubic
 -> at most four positive-train correction coordinates
 -> cubic shortening of three persistent bars and quartic shortening of h_0
 -> all active diameters < D, all source separations >= 1
 -> case 3 impossible for D>3.
```

This closes one of the two exact nonflat cases on current main. The repeated
two-bar rational core (case 2), all-flat case 1, larger persistent supports,
full backward rank, and nondisk topology are not settled.

## 2. Dependencies and status boundaries

- Canonical `docs/targets/target-b/01-jammed-rhombic-branch.md`, Sections
  37 and 41--43: exact train chart, signed variance, `L`, backward map,
  and persistent equality conditions.
- The finite cubic coefficient and stress separation are rederived in
  `docs/reports/target_b_tangent_cubic_capacity_2026-09-21.md`, Sections
  3 and 5.2 (unreviewed candidate). The proof below directly supplies the
  mixed-order argument; it does not assume its result already canonical.
- The application uses the precise case-3 endpoint hypotheses of
  `research/target_b_fourbar_211_phase_group_reduction_2026-10-03.md` and
  `research/target_b_fourbar_211_singleton_stress_endpoint_2026-10-03.md`.
  Those reports remain unpromoted. The result here rules out that explicitly
  stated endpoint, without promoting their complete AP/PG reduction.

No Target C core rigidity theorem, contact-isolate affine-kernel extension,
or asymptotic source/scaffold identification is used.

## 3. Proof of Theorem ZM

### 3.1 Zero full gradient means integer collinear separation

For every separating train,

\[
(g_0)_\tau=2r_0\cdot J(d_{0\tau}u_\tau)=0.
\]

Consequently each nonzero unit contribution is `sigma_tau e_0`, with
`sigma_tau in {+1,-1}` and `e_0=r_0/D`. If there are `P` positives and
`N` negatives, then `D=P-N` is a positive integer.

Persistence on `K` forces every forward nonzero contribution to rotate at
the common bar speed `s_0(v)`. The backward-kernel definition forces the
same for every negative one. There are no tangent separating contributions
when `g_0=0`. Thus all separating trains of `h_0` have the same speed along
every `v in K`.

### 3.2 A neutral sparse negative-quadratic correction

Restrict to any `r+2` positive separating coordinates. Impose the at most
`r` independent equations `g_h a=0` for `h in J'`, and impose
`sum_tau a_tau=0`. This homogeneous system has more variables than its
rank, so choose `a!=0` in its kernel and set all other coordinates to zero.
Also `g_0a=0` automatically.

Holding every other train fixed,

\[
r_0(\theta^0+sa)
 =D e_0+\sum_{\tau\in\operatorname{supp}a}
      [(\cos(sa_\tau)-1)e_0+\sin(sa_\tau)Je_0].
\]

The second derivative of its squared length is exactly

\[
\widehat H_0[a,a]
=2\left[(\sum a_\tau)^2-D\sum a_\tau^2\right]
=-2D\sum a_\tau^2<0.                                       \tag{3}
\]

Because `P>=D`, the sufficient condition `D>r+1` supplies `P>=r+2`.

### 3.3 Persistent velocities lie in each full Hessian kernel

This is the cross-term needed for (2); restricting the quadratic form to
`K` alone would not suffice.
Fix any persistent bar `h` and `v in K`. Write
`w_tau=d_h_tau u_tau`, `lambda_tau=r_h dot w_tau`, and `s=s_h(v)`.
Persistent equality and the backward-kernel condition give
`v_tau=s` whenever `lambda_tau!=0`.
Since `g_hv=0`, `r_h'(v)` is perpendicular to `r_h`. Moreover

\[
Jr_h\cdot r_h'(v)=\sum_\tau\lambda_\tau v_\tau=sD^2,
\]

so `r_h'(v)=sJr_h`. For **any** train vector `z`,

\[
\begin{aligned}
\widehat H_h[v,z]
&=2r_h'(v)\cdot r_h'(z)
  -2\sum_\tau\lambda_\tau v_\tau z_\tau\\
&=2s\sum_\tau\lambda_\tau z_\tau
  -2s\sum_\tau\lambda_\tau z_\tau=0.
\end{aligned}                                               \tag{4}
\]

Thus `widehat H_h v=0` in the full coordinate space. In particular the
`tv` and `epsilon t^2a` terms introduce no third-order Hessian cross-term.

### 3.4 Cubic corrector for the remaining persistent bars

Condition (1) and the finite strict linear alternative give `b` such that

\[
g_hb+C_h(v)<0\qquad(h\in J').                               \tag{5}
\]

For completeness, if the affine image `{(g_hb+C_h(v))_h:b}` missed the
strict negative orthant, separating the two convex sets would give a
nonzero `mu>=0`, `sum mu_hg_h=0`, and `sum mu_h C_h(v)>=0`, contrary
to (1). Conversely such a vector is exactly the obstruction.

The strict inequality condition on finitely many normalized stress-polytope
vertices is open in `v`. Perturb `v` within that open subset of `K` to avoid
the proper quadratic kernels of all bars outside `J`.
For each such bar its second-order coefficient is now strictly negative.

Choose `epsilon>0` small enough that

\[
\tfrac12\widehat H_h[v,v]+\epsilon g_ha<0\quad(h\notin J).
                                                                    \tag{6}
\]

This is possible for the finite active set. No claim that `a in K` is made
or needed.

For `h in J'`, Taylor expansion of (2), using `g_hv=g_ha=0` and (4), gives

\[
f_h(\theta(t))=[C_h(v)+g_hb]t^3+O(t^4)<0                    \tag{7}
\]

for all sufficiently small positive `t`.

For `h_0`, all its separating `tv` velocities are common. Factor out their
exact common rotation. Its residual angles are
`epsilon t^2a_tau+t^3b_tau`. Since `g_0=0`, (3) gives

\[
f_0(\theta(t))
=-D\epsilon^2\left(\sum a_\tau^2\right)t^4+O(t^5)<0.        \tag{8}
\]

For bars outside `J`, (6) gives negativity at order `t^2`. Hence every old
active diameter is strictly shorter than `D` simultaneously.

### 3.5 Every source pair is checked

The exact finite train chart preserves all unit contacts identically for
sufficiently small angle changes; initially strict rhombi remain strict.
Every initially noncontact lower-distance inequality has positive slack,
and every inactive upper-distance inequality has positive slack. There are
only finitely many source pairs. Choose one sufficiently small positive
`t` preserving all those inequalities at once. The scoped connected-disk
source has no contact-isolated vertices. An extension with additional fixed
points is valid only if all their lower and upper inequalities are initially
strict, or if every active pair involving them is incorporated in the exact
chart and active-bar analysis. No such extension is inferred here.

No active contact is weakened and all active diameters shorten by (6)--(8).
The finite maximum of all pair distances is therefore strictly below `D`,
at the same source cardinality. This proves Theorem ZM.

## 4. Application: four-bar (2,1,1) case 3 is impossible for D>3

Take the exact endpoint on current main: `J={h_1,h_2,h_3,h_4}`,
`g_2=0`, and

\[
\mathcal P=\operatorname{conv}\{(0,1,0,0),\mu^*\},\qquad
\mu^*=(1,0,k_3,k_4)/(1+k_3+k_4),\quad k_3,k_4>0.
\]

The restricted nonnegative balance polytope for `J'={h_1,h_3,h_4}` is
the singleton `{mu^*}` (with coordinate 2 omitted), positive on all three.
Therefore their gradient rank is at most two. The main-line endpoint gives

\[
\sum_h\mu_h^*F_h(v)
=\mu_3^*n_3(Q_B-Q_A)\delta(v)^3,
\quad\mu_3^*>0,\quad n_3\ne0,\quad Q_B\ne Q_A,
\quad\delta\in K^*\setminus\{0\}.                           \tag{9}
\]

The actual cubic coefficient is `C_h(v)=(D/3)F_h(v)`. Choose the sign of
`delta(v)` to make (9) negative. This satisfies (1). For `D>3`, Theorem ZM
applies with `r<=2`, using at most four positive collinear trains of `h_2`.
The resulting strict competitor contradicts local, hence global, diameter
minimality. Thus **case 3 is eliminated**, rather than left at an integer-
diameter/zero-gradient separator endpoint.

The diameter tends to infinity along any unbounded cardinality sequence:
packing disjoint radius-1/2 disks inside the radius-(D+1/2) disk about one
source point gives `n<=4(D+1/2)^2`. Consequently the restriction `D>3`
has no effect on a sufficiently-large-n branch.

## 5. Audit and limitations

| Concern | Resolution |
| --- | --- |
| Negative weighted curvature mistaken for finite descent | All active bars get their own strictly negative leading coefficient in (6)--(8). |
| Hessian cross-term only neutral on K | The full identity (4), valid against arbitrary corrections, is explicitly proved. |
| Many feasible exchanges combined without compatibility | One exact train-angle path moves the whole finite source. |
| New near-active pair blocks the motion | Every initially inactive pair has a fixed positive slack; choose t below their finite joint threshold. |
| Zero-gradient cubic endpoint persists | It shortens at fourth order, while the other stress endpoint shortens at third order. |
| Backward kernel silently omitted | v lies in K; a need not. Nonpersistent second-order coefficients are protected by epsilon. |
| Scaffold identified with source | The theorem assumes the actual source's exact pure-disk train chart. It makes no extraction theorem for arbitrary sources. |
| Contact-isolate stress extension | None; all source points remain, and the application stays in the stated pure-disk chart. |

The supporting exact algebra verifier is
`research/verify_target_b_zero_gradient_descent_2026_10_03.py`. It checks the
sparse nullspace construction and mixed-order coefficients in finite integer/
rational models; it does not establish train-chart existence or source optimality.

**Promotion recommendation:** preserve as unreviewed pending independent audit.
The theorem is proved under explicit finite hypotheses; the entire upstream
four-bar reduction remains unpromoted.

## 6. Single remaining four-bar nonflat obligation

In case 2, `n_1,n_2!=0`, `n_3=n_4=0`, the two nonflat bars share one
rotation functional, `mu_1n_1+mu_2n_2=0`, and the stress is unique and
positive on all four bars. Their weighted cubic cancels identically and
neither flat singleton is known to have zero full gradient. A closing step
must supply a **joint** higher-order correction controlling those flat bars,
or an actual finite strict source competitor. Theorem ZM cannot silently be
extended to that endpoint.

## Slot 2 recovery provenance — 2026-10-05

Recovered from `research/full-settlement-collar-20261003` at exact source tip `bc52d9f5153c8c936fd3fbf96f755c8d57bbee86`; no original PR was associated with the source branch. This artifact is preserved as a unreviewed proof-only candidate. It does not change theorem state. Any conditional source hypotheses and limits remain as stated above; C-II and Level I remain open.
