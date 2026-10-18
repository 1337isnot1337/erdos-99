# target-a-zero-slack-source-transfer

**Investigation:** `target-a-zero-slack-source-transfer-successor-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: The coupling must bound the source-specific Schur demand or yield a same-cardinality competitor. Another arbitrary matching collision does not advance that implication.

Prior evidence:
- [agent-audited](../docs/audits/target_a_zero_slack_matching_image_overlap_regression_2026-10-17.md) at `2e4a3e1e73877df4f4756fcb4c7d331dcda1327f`: five-source matching-overlap example: separate matchings do not supply joint source capacity. Remaining: No actual zero-slack source or Schur realization.

Independent integration reviews: [Target A](../docs/research/review-artifacts/merge-2026-10-18/review-a.txt), [Target B](../docs/research/review-artifacts/merge-2026-10-18/review-b.txt), [Target C](../docs/research/review-artifacts/merge-2026-10-18/review-c.txt).

**Track / priority:** target-a / direct frontier; selection weight 4 (attention only).

## Exact objective

Can one source-capacitated coupling theorem join the actual Section-168 source and response matchings while retaining their overlap and exact exceptional-set cost?

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

Use the five-source overlap regression in PR #98 as a failure control. Specify an actual zero-slack source and both incidence maps. Derive the minimum joint source-capacity deficit; test the proposed bound before converting it to Schur demand.

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
