# verify-a-schur-linkage-bound

**Investigation:** `verify-a-schur-linkage-bound-completed-20261017`. **Status:** completed. Source: `9f230b2f900bf050a27ce7430ae7b3fed8ef8eda`.

Downstream use: Retain completed coverage so new workers start at the unresolved successor instead of repeating this audit.

This scope is complete. Continue with [verify-a-source-capacity-coupling](verify-a-source-capacity-coupling.md).

Prior evidence:
- [agent-audited](../docs/research/review-artifacts/pr78/independent-audit.txt) at `9f230b2f900bf050a27ce7430ae7b3fed8ef8eda`: The exact finite Schur/linkage domain submitted in PR #78; reviewed before its merge. PR #96 is supplementary reconstruction of the same bytes. Remaining: No canonical promotion or acceptance outside this exact scope.
- [agent-audited](https://github.com/1337isnot1337/erdos-99/blob/6819b4f862508fe843f7a385e2cff992ecf23420/docs/audits/target_a_schur_linkage_independent_audit_2026-10-17.md) at `6819b4f862508fe843f7a385e2cff992ecf23420`: The exact finite Schur/linkage domain submitted in PR #78; reviewed before its merge. PR #96 is supplementary reconstruction of the same bytes. Remaining: No canonical promotion or acceptance outside this exact scope.

**Track / priority:** independent-verification / independent evidence; selection weight 1 (attention only).

## Exact objective

Can a small independent checker verify the finite directed-linkage and rank inequalities used by the Section-175 Schur cut, including sector-local paths after shield deletion?

## Definitions, hypotheses and complete prerequisites

- The checker verifies finite graph instances and stated algebraic matrices; it does not prove the geometric shield hypotheses or the global theorem.
- Use exact integer/rational arithmetic and make all vertex capacities and source/sink sets explicit.
- Preserve the difference between path-count rank upper bounds and a source-specific Schur nullity theorem.

- [docs/targets/target-a/27-tube-only-right-deficiency-frontier.md](../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md): Section-175 Schur cut and sector-local path argument
- [docs/targets/target-a/26-tube-shield-sector-balance.md](../docs/targets/target-a/26-tube-shield-sector-balance.md): Section-174 basis matching and sector separation hypotheses
- [docs/RESEARCH_WORKFLOW.md](../docs/RESEARCH_WORKFLOW.md): certificate registration and computational scope

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-a/README.md](../docs/targets/target-a/README.md): generic matrix rank or planarity does not give the source-specific Schur nullity
- [docs/targets/target-a/29-lens-source-gate-refinements.md](../docs/targets/target-a/29-lens-source-gate-refinements.md): lens sink sets may overlap and require a different coarse Hall graph

## Approach and first bounded experiment

This exact objective is complete. Read its recorded disposition, then use verify-a-source-capacity-coupling. Reopen only for a changed source or a named discrepancy.

Methods: independent max-flow implementation, exact symbolic matrix rank and cross-check fixtures

## Expected evidence

- An independently implemented exact verifier with positive cases and meaningful negative controls.
- A precise mapping from each finite graph condition to the theorem hypothesis it checks and a list of unverified geometric steps.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the checker is presented as validating arbitrary canonical response geometry, or if graph rank is substituted for the stated Schur matrix without a proof.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py verify-a-schur-linkage-bound
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

No further work on this completed source/domain. The separate successor is verify-a-source-capacity-coupling; the route endpoint remains open.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task verify-a-schur-linkage-bound --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
