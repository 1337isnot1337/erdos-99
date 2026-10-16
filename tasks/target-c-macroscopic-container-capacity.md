# target-c-macroscopic-container-capacity

**Track / priority:** target-c / direct frontier; selection weight 3 (attention only).

## Exact objective

Can the macroscopic inactive-container branch yield a source-preserving equal-cardinality packet or finite move after the fixed-wall capacity barriers, without losing the actual loaded core or any contact isolate?

## Definitions, hypotheses and complete prerequisites

- Keep the macroscopic-container branch separate from the full-core Type-II branch.
- Any replacement checks all full-source lower constraints and actual-diameter upper constraints, including retained isolates.
- The fixed-wall strict-capacity barriers do not apply automatically to moved walls or multi-cell packets.

- [docs/targets/target-c/CURRENT.md](../docs/targets/target-c/CURRENT.md): macroscopic-container branch and the exact remaining packet-capacity limits
- [docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md): Audit 108, Audit 110, and arbitrary-container capacity endpoint
- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): C-EXTERIOR-STATIC-PACKET-BARRIER and canonical source scope

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-c/CURRENT.md](../docs/targets/target-c/CURRENT.md): D(8) shows a shield need not create even one replacement slot; fixed strict-safe area is a no-go
- [docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md): paired-cap fixed-wall capacity is at most |S1|+|S2|+3; no source-preserving refill follows
- [docs/audits/target_c_exterior_cap_moved_core_refill_independent_audit_2026-10-09.md](../docs/audits/target_c_exterior_cap_moved_core_refill_independent_audit_2026-10-09.md): moved-core refill exists in a nonglobal family and does not establish canonical extraction
- [docs/reports/target_c_pentagon_activation_and_contact_debt_preservation_2026-10-15.md](../docs/reports/target_c_pentagon_activation_and_contact_debt_preservation_2026-10-15.md): A boundary-only cellulation by one pentagon and a one-cell rhombus chain has zero strict wall-safe capacity. Length alone does not certify surplus; source embedding and all source labels still require proof.

## Approach and first bounded experiment

Choose one exact container class and one proposed deletion/refill rule. Compute the full-source strict capacity with fixed walls, then allow the smallest specified wall motion and test whether the capacity changes while every isolate and old diameter pair remains feasible.

Methods: convex-container and Oler accounting with all labels, exact moved-core packet feasibility

## Expected evidence

- A uniform capacity or finite-move theorem under explicit geometric extraction hypotheses, plus a proof those hypotheses hold in the canonical branch.
- Or an exact counterexample to a proposed fixed-wall or moved-core capacity inference.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the result is only an area/Oler deficit, a fixed-wall surplus count, or a packet that is not embedded into the actual canonical source.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-c-macroscopic-container-capacity
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Construct a canonical full-source same-cardinality finite endpoint preserving every lower and actual-diameter upper pair bound and all applicable face constraints, with a triangle-free endpoint at D with lexicographically fewer contacts/actual-diameter pairs or strict sub-D diameter; separately close any untouched macroscopic-container restoration branch.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-c-macroscopic-container-capacity --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.


## Complete bent-array evidence

Source PR #948 gives an unreviewed linear external-boundary attachment result for actual complete bent arrays with both dimensions proportional to D, plus a quadratic outside-isolate burden and a full-diameter-forest classification. The [quarter-fold/bent-array track](../docs/research/tracks/target-c-quarter-folds-bent-arrays.md) records the exact hypotheses. The remaining task is extraction from a general canonical survivor or a different source-level endpoint; the conditional array results do not establish either.
