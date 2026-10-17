> Generated reading edition · [exact source](../../../docs/reports/target_c_three_edge_response_inertia_2026-08-31.md) · source SHA-256 `a07a79866ea97da0c7030a1ac57b5ea21e0946bd436ee332c9bfb038f14a1a64`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4EFCF9D651DA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: response inertia budget

**Date:** 2026-08-31
**Repository state:** 43bae6e (research/target-c-next-2026-08-31), with the route-map edits recorded with this addendum
**Run type:** exact response-matrix reduction
**Target:** Target C Gate C-I, remaining $|H_*|\ge3$ phase
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md
**External web search:** not used for the proof
**Computation:** not used

## LEVEL I STATUS

STILL OPEN

This addendum does not eliminate the diameter-shear separator. It gives an exact
inertia budget for the signed KKT stress matrix and reduces the first
three-diameter obstruction to one scalar response quantity.

## 1. Starting endpoint

The earlier C-I audits handle the low-support cases. The next surviving phase has
at least three strong diameter edges. A generic PSD or Loewner comparison is
unavailable there.

The exact statement proved here is

~~~text
positive diameter endpoints span a two-dimensional force hull
    -> the normalized diameter response has two eigenvalues equal to 1
    -> nu_-(Omega_s) <= rank(L_H)-2 <= |H_s|-2
    -> for a three-edge diameter forest, only one non-affine mode can be negative.
~~~

## 2. Strongest genuinely new audited theorem

### Theorem C30 (response inertia budget)

Fix a normalized KKT stress $s=(\alpha,\beta)$, let $G_s$ be its connected
positive unit-contact graph, let $B=V(H_s)$ be the endpoints of its positive
diameter support, and let

$$
\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta).
$$

Assume $\operatorname{aff}B$ is two-dimensional. Let $\Lambda$ be the positive
contact Dirichlet response on $B$, and let $L_H$ be the beta-weighted diameter
Laplacian. Then

$$
\boxed{
\nu_-(\Omega_s)
\le \operatorname{rank}L_H-2
\le |H_s|-2.
}
\tag{C30.1}
$$

Here $\nu_-$ denotes the number of negative eigenvalues, counted with
multiplicity. In particular, if $H_s$ is a three-edge forest, then
$\Omega_s$ has at most one negative eigenvalue.

### Proof

Let $I=V_s\setminus B$. The positive contact response is defined because the
positive contact graph is connected and $B\ne\varnothing$. Schur elimination of
the positive interior block gives the congruence

$$
\Omega_s\sim_{\mathrm{cong}}
(\Lambda-L_H)\oplus L_{C_s}[I,I],
\tag{C30.2}
$$

where the second summand is positive definite. Thus the negative inertia is that of
$M=\Lambda-L_H$.

Restrict to the subspace $\mathbf1^\perp\subset\mathbb R^B$. The response
$\Lambda$ is positive definite there. Define

$$
A=\Lambda^{-1/2}L_H\Lambda^{-1/2}
\quad\text{on }\mathbf1^\perp.
\tag{C30.3}
$$

The force-hull response identity gives

$$
\Lambda\mathbf1=L_H\mathbf1=0,
\qquad
\Lambda P_B=L_HP_B.
\tag{C30.4}
$$

After subtracting constants from the two coordinate columns, their restrictions to
$\mathbf1^\perp$ are linearly independent because $\operatorname{aff}B$ is
two-dimensional. Equation (C30.4) therefore gives two independent eigenvectors
$\Lambda^{1/2}x$ and $\Lambda^{1/2}y$ of $A$, both with eigenvalue $1$.

The matrix $A$ is positive semidefinite and
$\operatorname{rank}A=\operatorname{rank}L_H$. Every eigenvalue of $M$ on
$\mathbf1^\perp$ is negative exactly when the corresponding eigenvalue of $A$
is greater than $1$. Since two dimensions of the positive spectrum of $A$ are
already occupied by eigenvalue $1$, at most
$\operatorname{rank}L_H-2$ eigenvalues can exceed $1$. Finally
$\operatorname{rank}L_H\le |H_s|$, proving (C30.1). $\square$

### Corollary C30.1 (the three-edge forest scalar)

Assume $H_s$ is a forest with exactly three edges and $\operatorname{aff}B$ is
two-dimensional. Put

$$
\rho_s
:=\sum_{h=ij\in H_s}\beta_h R_{\mathrm{eff}}^{C_s}(i,j)-2,
\tag{C30.5}
$$

where

$$
R_{\mathrm{eff}}^{C_s}(i,j)
=(e_i-e_j)^{\mathsf T}\Lambda^+(e_i-e_j).
$$

Then the three nonzero eigenvalues of $A$ are

$$
\boxed{1,\ 1,\ \rho_s.}
\tag{C30.6}
$$

Consequently,

$$
\boxed{
\begin{array}{rcl}
\rho_s<1&\Longrightarrow&\Omega_s\succeq0,\\
\rho_s=1&\Longrightarrow&\Omega_s\succeq0\text{ with one extra scalar kernel mode},\\
\rho_s>1&\Longrightarrow&\Omega_s\text{ has exactly one negative scalar mode}.
\end{array}}
\tag{C30.7}
$$

### Proof

Because $H_s$ is a three-edge forest, $\operatorname{rank}L_H=3$, so $A$
has exactly three nonzero eigenvalues. Theorem C30 supplies two eigenvalues equal
to one; call the third $\rho_s$.

The trace identity gives

$$
\operatorname{tr}A
=\operatorname{tr}(\Lambda^+L_H)
=\sum_{h\in H_s}\beta_hR_{\mathrm{eff}}^{C_s}(h).
$$

Therefore $\rho_s$ is (C30.5). The sign of the eigenvalue $1-\rho_s$ in
$I-A$ gives (C30.7), and the positive interior block in (C30.2) contributes no
negative eigenvalues. $\square$

## 3. Exact target implication

The C-I shear-separator problem is no longer an uncontrolled matrix-inertia
question in the first three-edge forest phase. It is enough to prove one of:

$$
\boxed{
\sum_{h\in H_s}\beta_hR_{\mathrm{eff}}^{C_s}(h)\le3
}
$$

for every relevant three-edge stress, or to classify the equality mode
$\sum\beta_hR_{\mathrm{eff}}(h)=3$ and integrate it. If the sum is greater than
three, the obstruction is confined to one affine-balanced boundary load.

The theorem does not claim that $\rho_s\le1$. Effective resistance can be large
when the positive contact conductances are uneven, and no uniform stress lower bound
is available.

## 4. Scope and dependency audit

The theorem assumes only the canonical positive-support connectivity, the
force-hull response identity, and Schur-complement linear algebra. It applies to a
selected stress whose positive diameter endpoints span two dimensions; it does not
apply with the same $-2$ count to a collinear support.

Dependencies:

- docs/reports/target_c_force_polygon_2026-08-30.md, Theorem C11:
  $\Lambda P_B=L_HP_B$ and response-kernel facts.
- docs/reports/target_c_support_connectivity_2026-08-30.md and its audit:
  connected positive contact support and force-hull endpoint geometry.
- docs/reports/target_c_critical_cone_duality_2026-08-30.md and
  docs/reports/target_c_second_order_variance_2026-08-30.md:
  the earlier C-I release and direction-dependent second-order framework.

No PSD/Loewner comparison for general $H_s$ is used.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| C30 inertia budget | proved | Schur congruence and two forced affine eigenvectors. |
| Three-edge forest spectrum | proved | Rank three plus the two affine eigenvalues and the trace formula. |
| $\rho_s$ effective-resistance formula | proved | $\operatorname{tr}(\Lambda^+L_H)$. |
| Universal $\rho_s\le1$ | not proved | This is the next exact geometric inequality. |
| C-I fully closed | not proved | The $|H_*|\ge3$ shear separator remains. |
| General KKT PSD | rejected | C30 permits negative modes and only counts them. |

## 6. Regressions and no-go results

- The one-diameter chain and two-diameter quadrilateral are consistent with C30:
  they have no negative mode.
- The theorem does not collapse a rhombic or other two-dimensional contact bulk.
- It does not infer a lower bound on individual contact stresses.
- It does not turn a one-dimensional force-hull argument into a general response
  comparison.

## 7. Next run

Prove or disprove $\rho_s\le1$ for a three-edge diameter forest using the
circular-planar response, the pairwise-intersecting diameter-chord geometry, and the
triangle-free angle restrictions. A certified example with $\rho_s>1$ would be a
useful regression showing that the next C-I step must exploit the unique negative
mode rather than PSD.

## 8. Compact handoff

~~~text
LEVEL I STATUS: STILL OPEN.

C30:
For any normalized KKT stress whose positive diameter endpoints span a 2D force hull,
  nu_-(Omega_s) <= rank(L_H)-2 <= |H_s|-2.
The proof Schur-complements the positive contact response and conjugates
  Lambda-L_H
to I-A on 1-perp, where A has two forced affine eigenvectors of eigenvalue 1.

For a three-edge diameter forest,
  spec_nonzero(A) = {1,1,rho_s},
  rho_s = sum_h beta_h R_eff^C(h) - 2.
Thus rho_s <=1 is exactly the three-edge PSD threshold; rho_s>1 gives one and only
one negative scalar mode.

Next:
prove/contradict rho_s<=1 from circular planarity and diameter geometry, or classify
the rho_s=1 equality mode and integrate it.
~~~
