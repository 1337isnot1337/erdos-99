# literature-shell-stability-near-miss-audit

**Track / priority:** literature / scoped exploration; selection weight 1 (attention only).

## Exact objective

Does a published planar packing or convex-body stability theorem, under its exact hypotheses, imply any missing piece of Target B's joint outer-shell inequality beyond the canonical Oler and hole-correction inputs?

## Definitions, hypotheses and complete prerequisites

- Search for primary sources or reliable exact transcriptions and record normalization, domain regularity, topology, and equality hypotheses.
- The relevant object is a finite rhombic shell with phase and topology corrections, not an infinite packing density alone.
- A close theorem is a near miss unless every hypothesis is derived for the canonical Target B source.

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): exact shell inequality and global multi-grain/topology gap
- [docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md](../docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md): hole correction and promoted coherent-family results
- [docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md](../docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md): current phase and grid tools

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): the current chain lacks multi-grain transfer and cannot discard topology or boundary terms
- [docs/reports/wegner_global_boundary_defect_2026-09-09.md](../docs/reports/wegner_global_boundary_defect_2026-09-09.md): an unreviewed Wegner-boundary report addresses global diameter defect/plateau terms but does not state the full Target B shell inequality; check its lifecycle before use
- [docs/RESEARCH_WORKFLOW.md](../docs/RESEARCH_WORKFLOW.md): literature theorem hypotheses and normalization must be checked exactly

## Approach and first bounded experiment

Search specifically for stability refinements of Oler-type finite packing inequalities and planar convex-body shell estimates. Build a comparison table of theorem hypotheses against the Target B domain, including holes, multiple grains, phase crossings, and error order.

Methods: primary-source literature search, hypothesis-by-hypothesis transfer audit

## Expected evidence

- A bibliography with verified primary-source statements and exact constants/hypotheses.
- A proof that a theorem applies to a named canonical subcase, or a concise near-miss record identifying the first unsupported hypothesis.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the sources give only asymptotic packing density, disk-only stability, or an error larger than the boundary-order target; do not retrofit their conclusion to the shell setting.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py literature-shell-stability-near-miss-audit
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Establish G+E>=(sqrt(3)/4)B+(sqrt(3)/2)(t+chi-1) for the full canonical source with all multi-grain, interface, topology and uniformity hypotheses, or construct the full same-cardinality strict sub-D competitor.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task literature-shell-stability-near-miss-audit --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
