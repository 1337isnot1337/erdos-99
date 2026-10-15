<!-- theorem-state: {"artifact_id":"ART-EA64C386AD16","canonical":true,"claim_ids":["C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN","C-FINITE-CONTACT-ISOMETRY-DIAMETER-REPLACEMENT"],"claim_statuses":{"C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN":"canonical","C-FINITE-CONTACT-ISOMETRY-DIAMETER-REPLACEMENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: contact-isometric stress energy and diameter replacement

Date: 2026-10-08. Audit base: `origin/main=c83a03298d49edc1476240dc50f09bb87e0701a9`, state `2026-10-07.audit.119`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source artifact `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`. This audit covers only source Theorem 5 and Corollary 5.1. Sections 5.2 onward and the remaining source claims are outside this audit.

## Verdict

**PASS — promote** `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` and `C-FINITE-CONTACT-ISOMETRY-DIAMETER-REPLACEMENT`, with the scopes below. The stress identity is exact on the nonisolated positive-contact core. The replacement count is a separate full-source consequence and counts all unordered source-label pairs, including pairs incident to contact isolates. Neither statement supplies a contact-isometric endpoint or proves that its full-source pair constraints are feasible.

## Exact statements

Use the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`. Retain the full source `A`. Let `V` be its nonisolated positive-contact core, `P` the `v` by 2 source-coordinate matrix on `V`, `C` the actual contact edges on `V`, and `H_V` the actual diameter pairs whose two endpoints lie in `V`. Choose the canonical relative-interior normalized stress

```text
sum_C alpha_e = D^2,     sum_HV beta_h = 1,
Omega = L_C(alpha) - L_HV(beta) >= 0,
ker(Omega) = span{1, Px, Py} on V,
alpha_e > 0, beta_h > 0.
```

For any planar placement `Q` of the core that preserves every old contact exactly, put `U=Q-P`. Then

\[
\boxed{\sum_{h=ij\in H_V}\beta_h\bigl(D^2-|Q_i-Q_j|^2\bigr)
      =\operatorname{tr}(U^T\Omega U)\ge0.}
\]

Let `Pi` be orthogonal projection in vertex-coordinate space onto `span{1,Px,Py}`. If `v>3` and `lambda_+` is the least positive eigenvalue of `Omega`, then

\[
\operatorname{tr}(U^T\Omega U)
\ge \lambda_+\|(I-Pi)Q\|_F^2.
\]

Thus every contact-isometric core placement that is nonaffine in the source has strictly positive weighted old-diameter shortening, so at least one old core diameter pair becomes shorter, even if another old diameter pair lengthens. If the placement is noncongruent on `V` and no old core diameter pair lengthens, at least one strictly shortens. No uniform lower bound on `lambda_+` is asserted.

For the full-source consequence, let `Q` be a placement of all labels in `A`, unit-separated, with diameter at most `D`, preserving every old contact at length one and creating no new unit contacts. Suppose its restriction to `V` is noncongruent. Let `H_A` be the set of all old diameter pairs in the full source; let `L` count those pairs that become shorter than `D`, and let `N` count formerly inactive unordered source-label pairs that become length `D`. Then

\[
\boxed{L\ge1,\qquad N\ge L.}
\]

The source-label pairs in both counts include every contact-isolated label. In particular, no isolate-involving pair may be omitted from the diameter-pair comparison.

## Independent proof reconstruction

For the core placement, the stress trace identity gives

```text
tr(Q^T Omega Q)
 = sum_C alpha_e |Q_i-Q_j|^2 - sum_HV beta_h |Q_i-Q_j|^2
 = D^2 - sum_HV beta_h |Q_i-Q_j|^2
 = sum_HV beta_h (D^2-|Q_i-Q_j|^2).
```

Here the first equality uses the weighted graph-Laplacian definition; the second uses exact contact preservation and the canonical normalization. Since `Omega P=0`, expanding `Q=P+U` shows `tr(Q^T Omega Q)=tr(U^T Omega U)`. Positive semidefiniteness proves nonnegativity. The spectral theorem on the orthogonal complement of the exact kernel gives the displayed `lambda_+` bound, and `(I-Pi)U=(I-Pi)Q`. A nonaffine placement has a nonzero orthogonal component, so the weighted sum is strictly positive; with every `beta_h>0`, at least one summand has `|Q_i-Q_j|<D`. If all old `H_V` lengths are at most `D` but none shortens, they are all unchanged. Together with the preserved contacts, this is exactly the premise of canonical `C-MIXED-CORE-FINITE-RIGIDITY`, so the placement would be congruent, a contradiction.

For the full-source count, if the new diameter were below `D`, the same-cardinality placement would contradict global optimality. Therefore its diameter is `D`. The exact contact set is unchanged, so the new placement remains triangle-free and has the same number of contacts. The core argument gives at least one shortened old diameter, hence `L>=1`. By the source's secondary diameter-pair minimality, the new full-source diameter graph has at least as many edges as the old one. Every old diameter pair either remains at `D` or is counted by `L`; every new diameter pair was formerly inactive and is counted by `N`. These classes partition the new diameter pairs, giving `|H_Q|=|H_A|-L+N`; therefore `N>=L`. This is a count over all labels, not only `V`.

## Adversarial scope checks

- **Core versus full source:** `Omega`, `C`, and `H_V` use only `V`. The finite energy theorem says nothing about movement or pair constraints of contact isolates. The corollary assumes an actual full-source placement and counts every pair, including isolate-involving pairs.
- **Exact contacts:** every old contact must remain exactly unit. The corollary also forbids any new unit pair, so the complete contact graph and contact count are unchanged.
- **Old diameter upper bounds:** the first weighted identity allows other old diameter pairs to lengthen. The strict-shortening conclusion under noncongruence additionally assumes no old diameter lengthens; the corollary supplies this through its full-source diameter bound.
- **No contact-only rigidity inference:** a contact-isometric placement may be noncongruent. The stress inequality permits diameter changes and does not make the contact graph alone rigid.
- **No uniform gap:** `lambda_+` is source-dependent and may approach zero along a sequence. The theorem gives strict finite-source positivity, not quantitative asymptotic descent.
- **Secondary lexicographic step:** the inequality `N>=L` uses the canonical diameter-pair-minimal choice only after global optimality forces the competitor to have diameter exactly `D` and the exact contact graph is preserved.

The exact unit-square affine rhombus example in the source report has zero stress energy and mixed diameter changes: it is consistent with the theorem and shows why “noncongruent” alone cannot replace the nonaffine or no-lengthening hypotheses. The contact-only hinge and tetrahedral examples in the frozen verifier likewise do not preserve all mixed edge lengths and are not counterexamples to `C-MIXED-CORE-FINITE-RIGIDITY`.

## Computation boundary

The frozen verifier `research/verify_target_c_finite_core_rigidity_2026_10_02.py` (SHA-256 `5005feac3244fe835262a9c5f1671631da7ca4403a288856f08267ea932f18b0`) was inspected and rerun from the frozen source commit under Python 3 with SymPy exact arithmetic. Its square check verifies a finite stress factorization, the exact contact-isometric trace identity on a tetrahedral placement, and the positive-eigenspace inequality in that example. Other checks cover finite rigidity examples, an infinitesimally rigid hinge regression, and a planar contact-isometry example. The verifier does not prove the general stress identity, the full-source replacement count, canonical source optimality, or isolate-pair feasibility. Those general claims are proved analytically above.

## Dependencies and disposition

| Claim | Verdict | Canonical dependencies |
| --- | --- | --- |
| Core weighted stress energy and positive finite spectral bound for nonaffine contact-isometries | PASS — promote `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` | `C-ZRF`, `C-MIXED-CORE-FINITE-RIGIDITY` |
| Full-source mandatory diameter replacement count `N>=L>=1` | PASS — promote `C-FINITE-CONTACT-ISOMETRY-DIAMETER-REPLACEMENT` | `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN`, canonical global and secondary lexicographic minimality |
| Normalized straight-interpolation thresholds and slab-blocker claims in source Section 5.2 onward | Not audited; no lifecycle change | — |
| C-II or Level I closure | NOT CLAIMED; both remain open | — |

The core theorem converts a specified nonaffine contact-isometry into weighted old-diameter shortening. The full-source corollary shows that any feasible contact-isometry retaining the exact contact graph must replace every removed diameter pair with at least as many new ones. It supplies no endpoint, capacity, or strict sub-`D` competitor, so the active C-II frontier is unchanged.
