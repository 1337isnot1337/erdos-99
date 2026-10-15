# target-a-zero-slack-source-transfer

**Track / priority:** target-a / direct frontier; selection weight 4 (attention only).

## Exact objective

Can the boundary-order source localization and genuine-source gates in the zero-slack branch be converted into Schur deficiency or a strict source-cardinality competitor without identifying independently chosen matchings?

## Definitions, hypotheses and complete prerequisites

- Use the actual zero-slack source A^0 and plateau-endpoint response X* with the exact Section-168 matching hypotheses.
- The Section-176/177 exceptional sets are boundary-order and must remain explicit when the target is an exact rank or integer inequality.
- Keep the X* to A^0 and Y_in to A^0 matchings distinct unless a new simultaneous/global coupling theorem proves they agree.

- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): target-a zero-slack branch and global Schur endpoint
- [docs/targets/target-a/28-zero-slack-boundary-order-source-frontier.md](../docs/targets/target-a/28-zero-slack-boundary-order-source-frontier.md): Section 176 source localization and boundary-order defect
- [docs/targets/target-a/29-lens-source-gate-refinements.md](../docs/targets/target-a/29-lens-source-gate-refinements.md): Section 177 disjoint genuine-source V-path and source-gate refinements

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-a/18-common-neighbor-sdr-regression.md](../docs/targets/target-a/18-common-neighbor-sdr-regression.md): two source-matched pairs can share the same unique common lattice neighbor
- [docs/targets/target-a/README.md](../docs/targets/target-a/README.md): local common-neighbor certificates and gate counts alone do not imply Schur nullity
- [docs/targets/target-a/28-zero-slack-boundary-order-source-frontier.md](../docs/targets/target-a/28-zero-slack-boundary-order-source-frontier.md): source matching localization does not by itself relate r to Schur demand s

## Approach and first bounded experiment

Write a two-matching incidence diagram with separate source-image sets. Mark each sector-good, shield-crossing, and exterior label, then derive the exact maximum loss before any Hall or rank step. Test the proposed implication on small bipartite instances with shared-neighbor collisions.

Methods: bipartite incidence and Hall analysis, exact finite counterexample search for proposed coupling lemmas

## Expected evidence

- A simultaneous source/response coupling theorem with exact exceptional-set terms.
- Or an exact finite regression disproving a proposed coupling lemma and specifying the needed additional hypothesis.
- An explicit derivation to Schur deficiency, the global rank inequality, or a strict sub-D competitor.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the proof silently equates the independent matchings, drops an O(D) term at an exact integer endpoint, or treats pairwise feasible gates as simultaneously compatible.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-a-zero-slack-source-transfer
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

For the actual source and response, establish rank(S)<=d_int+|C^partial|-Delta_Lambda (d_sc>=Delta_Lambda); in the locked branch the exact Section-175 surplus is |O_iso|+sum_i max(0,|O_i|-|C_i|)>=j_*+|T_Z|. Any untouched zero-slack/global-realization branch remains.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-a-zero-slack-source-transfer --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
