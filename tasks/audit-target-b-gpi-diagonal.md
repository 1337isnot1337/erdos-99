# audit-target-b-gpi-diagonal

**Investigation:** `audit-target-b-gpi-diagonal-successor-20261017`. **Status:** completed. Source: `01be955ed9209f1d4a096148e61851837fa190d4`.

Downstream use: The reviewed diagonal controls the stated coherence and deletion errors. Compare those gains with the actual interface and virtual-area costs in target-b-multigrain-transfer.

This scope is complete. Continue with [target-b-multigrain-transfer](target-b-multigrain-transfer.md).

Prior evidence:
- [agent-audited](../docs/reports/target_b_gpi_mcp2_quantifier_audit_2026-10-17.md) at `01be955ed9209f1d4a096148e61851837fa190d4`: Independent audit of the Section-50/PC3 diagonal estimate for lambda_D=D^(-kappa), 0<kappa<(1-eta)/2, including uniform constants and angular-error summation. Remaining: No varying-tau GPI, global multi-grain summation, or full shell endpoint follows.

Independent integration reviews: [Target A](../docs/research/review-artifacts/merge-2026-10-18/review-a.txt), [Target B](../docs/research/review-artifacts/merge-2026-10-18/review-b.txt), [Target C](../docs/research/review-artifacts/merge-2026-10-18/review-c.txt).

**Track / priority:** independent-audit / independent evidence; selection weight 1 (attention only).

## Exact objective

Does PR #94 justify lambda_D=D^(-kappa), 0<kappa<(1-eta)/2, with uniform constants and valid angular-error summation, while keeping GPI restricted to fixed positive tau?

## Definitions, hypotheses and complete prerequisites

- Use the exact canonical dependency audit and current Target B route map.
- Do not strengthen the one-component GPI theorem or treat audited-working reports as premises.
- The deliverable is an independent scope audit or a precise counterexample to an overbroad paraphrase.
- The diagonal estimate has an independent scope audit. It supplies no varying-tau GPI or global multi-grain conclusion.

- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): TB-DENSE-GRID canonical entry and exact scope
- [docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md](../docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md): promoted MCP2 and GPI statements
- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): global multi-grain obstruction

Read the full statements and proofs. Submitted evidence does not supply an accepted premise.

## Approach and first bounded experiment

This exact objective is complete. Read its independent review, then use target-b-multigrain-transfer. Reopen only for a changed source or a named discrepancy.

## Expected evidence

- A concise independent derivation with exact quantifier order and a list of conclusions that do not follow.
- Or a specific hypothesis gap or algebraic error supported by a reproducible check.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the work drifts into proving the full Target B inequality; this card audits only the canonical input chain and its scope.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py audit-target-b-gpi-diagonal
```

## Remaining lemma and limitations

No further work on this completed source/domain. Continue with target-b-multigrain-transfer and retain the exact deletion, interface, and virtual-area terms.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.
