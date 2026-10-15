<!-- theorem-state: {"artifact_id":"ART-5292A4F9B534","canonical":true,"claim_ids":["C-MIXED-CORE-FINITE-RIGIDITY"],"claim_statuses":{"C-MIXED-CORE-FINITE-RIGIDITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: finite rigidity of the mixed contact/diameter core

Date: 2026-10-07. Audit base: `origin/main=ae5c7797ab5bcfe9d11b05495f7ee5e14b053b1a`, state `2026-10-07.audit.116`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source report `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`. Exact finite verifier `research/verify_target_c_finite_core_rigidity_2026_10_02.py`, SHA-256 `5005feac3244fe835262a9c5f1671631da7ca4403a288856f08267ea932f18b0`.

## Verdict

**PASS — promote `C-MIXED-CORE-FINITE-RIGIDITY`.** The author’s Theorem 1 is correct under the canonical positive-semidefinite stress and core-scoped ZRF/ZF hypotheses. This audit covers only that theorem. It does not audit the source report’s three-connectivity, two-puncture anchoring, incidence, move-energy, interpolation, or regression claims; each retains its own lifecycle.

The result is:

```text
same exact lengths on every actual contact and diameter edge of V
 -> zero positive-semidefinite stress energy
 -> every coordinate of Q lies in span{1,Px,Py}
 -> affine map T with T^T T = I
 -> all pairwise distances on V are preserved
```

## Exact statement and scope

Let `A` be the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`; let `V` be its nonisolated positive-contact core, and let `C,H` be its actual unit-contact and actual-diameter edges on `V`. Choose a relative-interior normalized KKT stress with positive coefficients `alpha_e,beta_h`, satisfying

```text
sum_H beta_h = 1,       sum_C alpha_e = D^2,
Omega = L_C(alpha)-L_H(beta) >= 0,
ker(Omega|_V) = span{1,Px,Py}.
```

The first two identities are the canonical virial normalization; positive semidefiniteness is the restored C-I result; the kernel statement is the canonical ZRF theorem, all on the same core `V`.

For any finite `k` and any placement `Q_i` in Euclidean `R^k` satisfying

```text
|Q_i-Q_j| = |P_i-P_j|  for every ij in C union H,
```
there are `b in R^k` and a linear map `T:R^2 -> R^k` such that `Q_i=b+T P_i` for every `i in V`, with `T^T T=I_2`. Consequently every pairwise distance among vertices of `V` is preserved.

Contact isolates and all labels outside `V` are outside the theorem. The theorem requires equality on every active mixed edge; it does not permit replacing old diameter equalities with upper inequalities, does not require a feasible path from `P` to `Q`, and makes no assertion about inactive full-source constraints.

## Independent proof reconstruction

Write `Q` as the `v` by `k` matrix of coordinates. The edge-length equalities give

```text
tr(Q^T Omega Q)
 = sum_C alpha_e |Q_i-Q_j|^2 - sum_H beta_h |Q_i-Q_j|^2
 = sum_C alpha_e - D^2 sum_H beta_h
 = D^2-D^2
 = 0.
```

Since `Omega` is positive semidefinite, each coordinate column of `Q` is in its kernel. The core-scoped ZR identity therefore yields `Q_i=b+T P_i` for an affine map from the source plane into `R^k`.

Set `M=T^T T-I_2`, a symmetric `2 by 2` matrix. For every edge vector `r=P_i-P_j` in `C union H`, length equality gives `r^T M r=0`. The planar velocity `u_i=(M/2)P_i` is therefore a mixed infinitesimal bar flex, since the first derivative of its squared edge length is `2 r^T(u_i-u_j)=r^TMr=0`. Canonical ZF says every such velocity on `V` is Euclidean: `u_i=a+S P_i` with `S^T=-S`. Because `V` affinely spans the plane, equality of these affine maps at the core vertices forces `a=0` and `M/2=S`. A matrix both symmetric and skew-symmetric is zero, so `M=0`, hence `T^TT=I_2`.

The use of ZF here is only its exact core-scoped infinitesimal-rigidity conclusion. The finite implication is supplied by the separate PSD trace identity; no inference from infinitesimal rigidity to finite rigidity is made by itself.

## Adversarial scope checks

- **Core only:** `Omega` and its three-dimensional kernel are used on `V`. No zero rows are appended for contact isolates, and no conclusion is drawn about their positions or distances to the core.
- **Exact mixed lengths:** equality on every row of `C union H` is required. Contact preservation alone, or old-diameter upper bounds alone, do not make the trace zero.
- **Stress normalization:** both `sum alpha=D^2` and `sum beta=1` are load-bearing; dropping either invalidates the zero-energy step.
- **No local/global shortcut:** the conclusion is a finite congruence theorem for the core framework under its full mixed edge set. It does not say the source has a feasible contact-isometry, or that inequalities and inactive constraints survive along an interpolation.
- **Known regressions are compatible:** the source report’s two-triangle hinge has no canonical positive PSD stress and shows why infinitesimal rigidity alone is insufficient. Its tetrahedral placement preserves contacts but shortens old diameter rows, so it violates this theorem’s exact `C union H` equality premise. The nonglobal square packet is a finite illustration, not a large canonical-source instance.

## Computation boundary

The frozen exact verifier was rerun successfully; output SHA-256 is `5973ba2574a6e18cc4355ae8808e68ca3446026a1e09596fbfb8aa94dc455f92`. It checks a square’s stress factorization, kernel and mixed rigidity; every single-row deletion; all 11 square punctures; a higher-dimensional tetrahedral contact-only regression; a locally rigid two-triangle hinge; and the listed finite contact-isometry examples. These computations test examples only. The general finite-rigidity proof is the stress/kernel/infinitesimal argument above, not an inference from those samples.

## Canonical disposition

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Finite rigidity of the exact mixed contact/diameter core in every finite Euclidean dimension | PASS — promote | `C-MIXED-CORE-FINITE-RIGIDITY` |
| Mixed three-vertex connectivity and two-puncture loaded anchoring | Not audited in this cycle | Preserve the source report’s candidate status pending separate audit |
| Contact-incidence, move-energy, interpolation, and remaining regressions in the source report | Not audited in this cycle | No lifecycle change |
| C-II or Level I closure | NOT CLAIMED | Both remain open |

This theorem supplies an exact finite rigidity tool for later source-cut arguments. It neither proves a source cut exists nor changes the current full-core finite-move or macroscopic-container obligations.
