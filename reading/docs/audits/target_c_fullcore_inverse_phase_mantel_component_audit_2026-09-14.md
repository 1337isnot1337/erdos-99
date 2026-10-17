> Generated reading edition · [exact source](../../../docs/audits/target_c_fullcore_inverse_phase_mantel_component_audit_2026-09-14.md) · source SHA-256 `6eadbc4f17f6e969c9b1607e935689d411814741f9985c199b6913018019738a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-FDC2BAD43A16","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — full-core inverse-phase Mantel component

**Date:** 2026-09-14
**Candidate:** `docs/reports/target_c_fullcore_inverse_phase_mantel_component_2026-09-14.md`
**Verdict:** PASS as a report-level sequential endpoint reduction; not a C-II closure.
**Global Level I status:** STILL OPEN.

## 1. Endpoint train-count squeeze

At (mu_D	omu_{\rm TC}), the promoted train-coupled endpoint bookkeeping gives

```math
(q-k)/D\to\mu_{\rm TC},
\qquad f_D/D\to f_{\rm TC},
\qquad R_D/D^2\to\Delta_2.
```

The exact inequalities (T_D\le q-k+2f_D) and (T_D\ge2\sqrt{R_D}) have the
same limit (2\sqrt{\Delta_2}), so (T_D/D\to2\sqrt{\Delta_2}). The relation

```math
\mu_{\rm TC}+2f_{\rm TC}=2\sqrt{\Delta_2}
```

is exact. PASS.

The audit treats the equality rate (f_D/D\to f_{\rm TC}) as part of the promoted
endpoint bookkeeping. If that equality rate were not available, the squeeze would
not follow from the scalar limit alone; the report lists it explicitly rather than
silently deriving it.

## 2. Mantel stability

The phase cut deletes (O(D)) edges and no train vertices, so the cut train graph
has (R_D-O(D)) edges on (T_D) vertices. Canonical train geometry supplies a
simple triangle-free graph. With (R_D/D^2\to\Delta_2) and
$`T_D/D\to2\sqrt{\Delta_2}`$, its edge density tends to (1/4). Lemma 2.1 is
correct: triangle-freeness gives (d(x)+d(y)\le v) on every edge, the variance
bound follows, and the neighborhood of a near-half-degree vertex supplies the
balanced partition. PASS.

## 3. High-defect deletion and incidence trimming

For (K_D\to\infty), the global $`\sum\delta_e\le C_{\rm phase}D`$ bound gives at
most (C_{\rm phase}D^2/K_D=o(T_D^2)) edges above (K_D/D). Adding the Mantel missing
cross edges still gives (U_D=o(T_D^2)). The threshold $`\rho_DT_D`$, with
$`\rho_D=\sqrt{U_D}/T_D`$, deletes at most (2\rho_DT_D=o(T_D)) vertices.
The surviving good graph has opposite-shore degree at least the opposite-shore
size minus (o(T_D)). PASS.

The zero-error case (U_D=0) is harmless: no vertex is deleted and all subsequent
error terms are zero.

## 4. Diameter-three phase collapse

If every surviving vertex has degree $`|\text{opposite shore}|-o(T_D)), any two
vertices on one shore have a common neighbor. For a cross-shore nonedge (x y),
choose (y_1\in N(x)`$; the neighborhoods of (y) and (y_1) on the opposite shore
have a common vertex, giving a path of length three. Each good edge changes the real
phase by at most (K_D/D) in absolute value, so graph diameter at most three gives
phase diameter at most (3K_D/D=o(1)). PASS.

## 5. Label concentration and cyclic-order saturation


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Same-label trains cannot be crossing partners in a sufficiently small strict-rhombic
phase bin. Hence same-label pairs across the Mantel shores are part of the (o(T_D^2))
cross-missing set. The Cauchy--Schwarz estimate for the sum of minority populations is
correct. Since both Mantel shores have size (T_D/2+o(T_D)), at least one label is
assigned to each shore; with three labels the concentration pattern is (1+2), or
the degenerate (1+1) pattern if one label is absent. The sole label on one shore has
size (T_D/2+o(T_D)), and the other label classes together have size
\(T_D/2+o(T_D)). The good edge count is (T_D^2/4-o(T_D^2)), which gives
```



```math
|E(H_D)|=M_D^{\rm cls}(a_D^{\rm cls}+b_D^{\rm cls})-o(T_D^2).
```

PASS.

## 6. Scope and non-implications

The proof does not turn (H_D) into a source, a contact complex, or a pure disk.
Deleting train vertices is an analytical subgraph operation; no source point is
deleted from the original configuration. The report does not use the rejected
full-source affine-kernel extension, does not infer an Euler path from diameter-edge
incidence, and does not integrate a local stress into a finite motion. PASS.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The result remains sequential: it assumes a subsequence with
\(\mu_D\to\mu_{\rm TC}\), and it does not provide a finite uniform endpoint gap for
all full-core minimizers. It also does not address $`\liminf\mu_D>\mu_{\rm TC}`$ or the
macroscopic-container branch. PASS.
```



## 7. Final audit verdict

The endpoint reduction is valid under the explicitly listed canonical hypotheses.
Its missing arrow is exactly a full-core near-extremal exclusion theorem that permits
holes, exceptional faces/interfaces, bridges, repeated boundary occurrences, and all
source points. Mantel stability, phase collapse, and fixed-density pseudosegment
extraction do not supply that arrow. The artifact should remain unreviewed until a
promotion audit also checks the endpoint equality bookkeeping against the current
manifest.
