# compute-b-two-grain-interface-regressions

**Investigation:** `compute-b-two-grain-interface-regressions-successor-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: Decide whether the abstract sharp examples are geometrically relevant to Target B, and whether a stronger realizable budget is possible.

Prior evidence:
- [agent-audited](../docs/reports/target_b_interface_capacity_2026-10-17.md) at `a392a910899b06d20df6c7c29010896223ebfa70`: shared-interface inequality R >= G + max(p1,p2,p1+p2-K), with finite incidence checks. Remaining: Geometric realization and payment of virtual mass are not established.

Independent integration reviews: [Target A](../docs/research/review-artifacts/merge-2026-10-18/review-a.txt), [Target B](../docs/research/review-artifacts/merge-2026-10-18/review-b.txt), [Target C](../docs/research/review-artifacts/merge-2026-10-18/review-c.txt).

**Track / priority:** exact-computation / scoped exploration; selection weight 2 (attention only).

## Exact objective

Does a smallest explicitly realized two-grain rhombic disk saturate or improve the submitted shared-interface budget after all virtual crossing terms are included?

## Definitions, hypotheses and complete prerequisites

- The model is finite and combinatorial; it is not automatically realizable by a global planar packing.
- Use exact integer/rational arithmetic and publish the enumerated domain.
- A finite regression can reject a universal model claim but cannot disprove Target B without a theorem embedding it.

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): multi-grain transfer and interface obstruction
- [docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md](../docs/reports/target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md): PDG, PC1/PC3, MCP1/MCP2, and GPI scopes
- [research/README.md](../research/README.md): computation documentation contract

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): several macroscopic grains may share quadratic crossing mass while density-only grids miss the cancellation threshold

## Approach and first bounded experiment

Build one rational rhombic cellulation with its retained train components and deleted interfaces. Derive counters from that geometry, then compare with PR #86. Emit either a realizable saturation case or a proved geometric restriction on its abstract extremizers.

Methods: exhaustive exact integer enumeration, SAT/SMT model with independently checked certificate

## Expected evidence

- A runnable enumerator, exact input/output fixture, and minimal counterexample or bounded proof for the declared model.
- A clear statement of whether and what geometric realization theorem would be needed to transfer the model to Target B.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop when the declared finite domain is exhausted or the model cannot represent the intended cross-grain interaction; do not relabel a graph-only witness as a planar packing counterexample.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py compute-b-two-grain-interface-regressions
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Establish G+E>=(sqrt(3)/4)B+(sqrt(3)/2)(t+chi-1) for the full canonical source with all multi-grain, interface, topology and uniformity hypotheses, or construct the full same-cardinality strict sub-D competitor.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task compute-b-two-grain-interface-regressions --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
