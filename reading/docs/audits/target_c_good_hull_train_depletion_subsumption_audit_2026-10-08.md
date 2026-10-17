> Generated reading edition · [exact source](../../../docs/audits/target_c_good_hull_train_depletion_subsumption_audit_2026-10-08.md) · source SHA-256 `e11ee9bc4f19c8cba8a5df3320010011e8e18d1d6c9d0136505d8ff15ee5b47a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BC658F5CEDE1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.135 — PR #666 good-hull train depletion candidate

Date: 2026-10-08  
Audit base: `origin/main=eafdaf917455322a67e1a07c071f836ba688ae53`, state `2026-10-08.audit.134`  
Source snapshot: open draft PR #666, branch `research/sol-hull-train-nonatomic-20261004` at `52aab147b3dfaea1247b67647c603e2653dbeb5b`  
Source report SHA-256: `af658a68092613962791928ad0e3ccaf6e7d53a048d91ce1921f1335a21b89fd`  
Source verifier SHA-256: `dcab21786fc2798ab5715c353d182cdd9863685a1d8cb26531732ff9d4ff55b3`

## Audit boundary and verdict

I audited the finite annular angular-capacity estimate, the finite all-unit-hull-side source-exclusion criterion, the Type-II depletion conclusion, and the claimed high-$`t_D`$ scope elimination. The candidate report and verifier were read at the immutable PR #666 tip. The mathematical content is correct at its stated scope, but it is already covered by stronger or equivalent canonical results. No theorem-state change or new theorem ID is warranted.

**Disposition:**

- `PASS — already subsumed`: finite good-end depletion and the optimized finite criterion, by Audit.125 `C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND` plus its exact canonical ledger.
- `PASS — already canonical`: Type-II depletion, outer-walk tradeoff, and the low-outer-walk high-t exclusion, by Audit.52 `C-FULLCORE-HULL-DEPLETION-FLOOR`.
- `REGRESSION VALID, already represented`: the square attaining the two-double-ended-train correction already appears in the Audit.125 exact certificate.
- The oblique-grid boundary-subdivision example is valid, but it does not refute any canonical claim and is not registered as a separate theorem.

C-II and Level I remain open. The audit does not change the active Target C frontier.

## 1. Exact finite candidate and canonical strengthening

Within the canonical finite C-II source scope of the report, the actual loaded force hull $`F`$, after translation, is assumed to satisfy

```math
B(0,(1/2-\sigma)D)\subset F\subset B(0,(1/2+\sigma)D),\qquad 0\le\sigma<1/2.
```

It defines

```math
C(\varepsilon,\sigma)=4\left[(1/2+\sigma)\tan\varepsilon+
\frac{\sqrt{2\sigma}}{\cos\varepsilon}\right]
```

and claims that if $`G`$ is the set of stopped trains with at least one good outer end, then

```math
E_G\le\frac{\Delta}{\varepsilon}+3TD\,C(\varepsilon,\sigma),
\qquad 0<\varepsilon<\pi/6.
\tag{1}
```

Here $`E_G`$ counts actual strict-rhombus crossings incident to a train in $`G`$, $`T`$ is the total number of stopped trains including singletons, and $`\Delta`$ is the total acute-angle defect. Each good outer end lies on an actual unit side of the loaded force hull. Hence every train in $`G`$ belongs to the canonical set $`H`$ of trains carrying one selected actual unit hull side, and $`E_G \le E_H`$.

Audit.125 proves for that larger set $`H`$, under the same annulus and the same canonical simple train-crossing graph,

```math
E_H\le\frac{A_{\rm ang}}{\varepsilon}+2TD\,C(\varepsilon,\sigma),
\tag{2}
```

where $`A_{\rm ang}=\Delta`$. Thus (2) strictly strengthens (1). The two-window count is sufficient because, after fixing the endpoint outside $`H`$ of a small-defect crossing, a selected hull-side partner lies in one of the two projective windows centered at projective phase $`\pm\pi/3`$; summing over all $`T`$ anchors counts each crossing at least once. This argument uses actual selected hull sides, not all unit edges occurring along the outer face.

For the candidate's optimized form, its assumptions give $`\varepsilon=\sqrt{\Delta/(24TD)}\le1/4`$. The canonical estimate and $`C\le8\varepsilon+8\sqrt{2\sigma}`$ imply at that same ε

```math
E_G\le E_H\le\frac{40}{\sqrt{24}}\sqrt{\Delta TD}
 +16TD\sqrt{2\sigma}.
```

The displayed candidate bound is $`2\sqrt{24\Delta TD}+24TD\sqrt{2\sigma}`$; both coefficients above are strictly smaller. The candidate's square-root source-exclusion criterion therefore follows with a stronger error term from the canonical estimate and the exact ledger.

The report's identities (12c)--(12e) use the same selected unit-hull-side population as Audit.125. The exact identity and $`d\le2`$ correction are canonical; after deleting selected-end trains, the canonical simple triangle-free crossing graph and Mantel give the same no-end square-root bound. The finite criterion is consequently a direct corollary, not an additional theorem.

## 2. Type-II claims are Audit.52 consequences

For every canonical full-core Type-II sequence, `C-FULLCORE-HULL-DEPLETION-FLOOR` gives

```math
\liminf\left(5t_D+\frac{x_B+m_B}{D}\right)
\ge 3\pi+2s,
\qquad s=\sqrt{\frac{\pi}{2\sqrt3}}.
\tag{3}
```

The canonical loaded-hull ledger gives $`0\le m_B\le x_B`$. If $`x_B=o(D)`$, then $`m_B=o(D)`$, and (3) yields

```math
\liminf t_D\ge\frac{3\pi+2s}{5}=2.265880714899\ldots.
```

If $`\limsup t_D \le t_0`$, (3) and $`x_B + m_B \le 2x_B`$ yield

```math
\liminf\frac{x_B}{D}\ge\frac{3\pi+2s-5t_0}{2}
```

whenever the right side is positive. At $`t_0=1.860`$, this is greater than $`1.0147`$. These are exactly the candidate's Type-II depletion, outer-walk tradeoff, and advertised low-$`t_D`$ collar exclusion. The excluded high-$`t_D`$ antecedent does not falsify the conditional local inequalities in those collar reports, but those applications cannot describe an unbounded canonical Type-II source in that regime.

This establishes neither a Type-II closure nor a Level I result. The higher-surplus Type-II and Type-I branches remain open.

## 3. Exact finite certificate and regressions

I inspected the frozen Python verifier. It uses `Fraction` arithmetic for all pair distances, exact contacts, diameter pairs, strict hull vertices, train components, crossings, and train endpoint counts. Its rational Machin-series and square-root brackets certify only the displayed numerical thresholds. I reran the exact source blob; all 12 square and oblique-grid packets passed.

The unit-square packet has $`T=N=2`$ and one rhombus crossing. It refutes the error-free finite claim $`T\ge N+2\sqrt{R_4}`$. The correction $`d\le2`$ for trains with two selected hull ends is essential; the same square/additive-two-sharp case is already in the registered Audit.125 verifier. No duplicate regression ID is added.

For $`j\ge2`$, the oblique packets have many unit contact edges along each collinear boundary chain while each of the four physical parallelogram hull sides has length $`j`$. They confirm that an outer boundary contact occurrence cannot be counted as a unit side of the strict convex hull. The packets are finite configurations, not asserted global minimizers. The verifier proves no global optimality or Type-II asymptotic statement. This example is consistent with the canonical definition that counts actual hull sides only, so it is retained as supporting regression evidence in the source artifact without a separate theorem ID.

## 4. Canonical disposition

| Candidate item | Verdict | Canonical result |
| --- | --- | --- |
| Good-end finite angular bound (1) | PASS — subsumed | Audit.125's `C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND` covers a superset with coefficient 2 rather than 3. |
| Optimized error and finite source-exclusion criterion | PASS — subsumed | Follows from the stronger Audit.125 bound and exact canonical train/face ledgers. |
| Global Type-II depletion and source tradeoff | PASS — already canonical | Audit.52's `C-FULLCORE-HULL-DEPLETION-FLOOR` gives the same conclusion and its surplus floor. |
| Unit-square finite correction regression | REGRESSION VALID — already represented | Audit.125 verifier's square/additive-two-sharp fixture. |
| Oblique boundary-subdivision example | REGRESSION VALID — illustrative only | No canonical inference is refuted; no separate claim ID. |

No discovery branch was modified. PR #666 remains open until this audit disposition is merged; its source report and verifier are preserved at the frozen branch tip. Once the disposition is canonical, the PR can be closed as superseded without deleting that branch.
