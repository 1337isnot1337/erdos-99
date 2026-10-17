# target-b-phase-deficit-competitor

**Investigation:** `target-b-phase-deficit-competitor-current-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: Name the downstream claim or decision this result can change, the exact quantity it controls, and the remaining hypothesis before extending the investigation.

**Track / priority:** target-b / direct frontier; selection weight 2 (attention only).

## Exact objective

In a phase-imbalanced survivor, can the phase potential be integrated into an actual equal-cardinality competitor of diameter strictly below D while preserving every unit-separation constraint and active diameter bound?

## Definitions, hypotheses and complete prerequisites

- Use the exact Target B phase potential and geometry in the current route; do not replace it by arbitrary graph phases.
- All source points and all active diameter constraints of the proposed competitor must be checked.
- A nonnegative first-order derivative or a local shell energy decrease alone does not produce a finite competitor.

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): global endpoint alternative: shell inequality or strict diameter improvement
- [docs/targets/target-b/01-jammed-rhombic-branch.md](../docs/targets/target-b/01-jammed-rhombic-branch.md): phase potential and sections 49-56
- [docs/RESEARCH_WORKFLOW.md](../docs/RESEARCH_WORKFLOW.md): geometry and finite-motion proof-audit requirements

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): local phase and coherent-core exclusions do not control every survivor
- [docs/targets/target-b/01-jammed-rhombic-branch.md](../docs/targets/target-b/01-jammed-rhombic-branch.md): phase-potential deductions stop short of a source-preserving strict-D motion

## Approach and first bounded experiment

Choose a finite survivor model with a nonzero phase defect and compute the full Jacobian of contact lower constraints and diameter upper constraints. Seek a feasible velocity with a strictly negative derivative for every active diameter pair, then separately prove that the direction integrates to a finite move.

Methods: linearized constraint cone plus nonlinear continuation, exact rational finite survivor search

## Expected evidence

- A full-source feasible finite deformation with exact strict diameter margin and all lower-pair constraints checked.
- Or an exact obstruction showing why the proposed phase direction cannot satisfy the active constraints.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if only the aggregate phase energy decreases, if some active diameter pair is unchecked, or if the argument replaces strict <D by <=D.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-b-phase-deficit-competitor
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Establish G+E>=(sqrt(3)/4)B+(sqrt(3)/2)(t+chi-1) for the full canonical source with all multi-grain, interface, topology and uniformity hypotheses, or construct the full same-cardinality strict sub-D competitor.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-b-phase-deficit-competitor --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
