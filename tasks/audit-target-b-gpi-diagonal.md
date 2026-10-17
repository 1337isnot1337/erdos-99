# audit-target-b-gpi-diagonal

**Investigation:** `audit-target-b-gpi-diagonal-successor-20261017`. **Status:** open. Source: `01be955ed9209f1d4a096148e61851837fa190d4`.

Downstream use: Decide whether the diagonal estimate is reusable. Then compare its quantitative gain with deletion/interface loss before claiming a shell improvement.

Prior evidence:
- [author-checked](https://github.com/1337isnot1337/erdos-99/blob/01be955ed9209f1d4a096148e61851837fa190d4/docs/reports/target_b_gpi_mcp2_quantifier_audit_2026-10-17.md) at `01be955ed9209f1d4a096148e61851837fa190d4`: Separate diagonal estimate beyond the completed fixed-lambda scope audit. Remaining: Uniform constants, propagation conditions and error summation require independent proof review.

**Track / priority:** independent-audit / independent evidence; selection weight 1 (attention only).

## Exact objective

Does PR #94 justify lambda_D=D^(-kappa), 0<kappa<(1-eta)/2, with uniform constants and valid angular-error summation, while keeping GPI restricted to fixed positive tau?

## Definitions, hypotheses and complete prerequisites

- Use the exact canonical dependency audit and current Target B route map.
- Do not strengthen the one-component GPI theorem or treat audited-working reports as premises.
- The deliverable is an independent scope audit or a precise counterexample to an overbroad paraphrase.
- The diagonal estimate is unreviewed; the common scope audit does not accept it.

- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): TB-DENSE-GRID canonical entry and exact scope
- [docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md](../docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md): promoted MCP2 and GPI statements
- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): global multi-grain obstruction

Read the full statements and proofs. Submitted evidence does not supply an accepted premise.

## Approach and first bounded experiment

Check out PR #94 at 01be955ed9209f1d4a096148e61851837fa190d4. Independently reconstruct the Section-50/PC3 constants, the graph-diameter and zero-gain-cycle condition, and the sum of angular errors. Test the exponent boundary and reject any use of fixed-tau GPI for tau_D tending to zero.

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

Establish G+E>=(sqrt(3)/4)B+(sqrt(3)/2)(t+chi-1) for the full canonical source with all multi-grain, interface, topology and uniformity hypotheses, or construct the full same-cardinality strict sub-D competitor.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.
