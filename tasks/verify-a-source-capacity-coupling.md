# verify-a-source-capacity-coupling

**Investigation:** `verify-a-source-capacity-coupling-successor-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: Test whether a proposed coupling pays the true joint source demand. The checker must expose which geometric realization hypothesis is still absent.

Prior evidence:
- [agent-audited](../docs/research/review-artifacts/pr78/independent-audit.txt) at `9f230b2f900bf050a27ce7430ae7b3fed8ef8eda`: Completed independent finite Schur/linkage proof and checker audit, with merger-owned replay. Remaining: Actual source-capacity coupling was outside the reviewed domain.
- [agent-audited](../docs/audits/target_a_zero_slack_matching_image_overlap_regression_2026-10-17.md) at `2e4a3e1e73877df4f4756fcb4c7d331dcda1327f`: separate-matching overlap regression. Remaining: Actual source realization remains open.

Independent integration reviews: [Target A](../docs/research/review-artifacts/merge-2026-10-18/review-a.txt), [Target B](../docs/research/review-artifacts/merge-2026-10-18/review-b.txt), [Target C](../docs/research/review-artifacts/merge-2026-10-18/review-c.txt).

**Track / priority:** independent-verification / independent evidence; selection weight 1 (attention only).

## Exact objective

Can an exact source-capacitated checker test a proposed Section-168 coupling using both actual incidence maps, without identifying independent matchings?

## Definitions, hypotheses and complete prerequisites

- The checker verifies finite graph instances and stated algebraic matrices; it does not prove the geometric shield hypotheses or the global theorem.
- Use exact integer/rational arithmetic and make all vertex capacities and source/sink sets explicit.
- Preserve the difference between path-count rank upper bounds and a source-specific Schur nullity theorem.

- [docs/targets/target-a/27-tube-only-right-deficiency-frontier.md](../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md): Section-175 Schur cut and sector-local path argument
- [docs/targets/target-a/26-tube-shield-sector-balance.md](../docs/targets/target-a/26-tube-shield-sector-balance.md): Section-174 basis matching and sector separation hypotheses
- [docs/RESEARCH_WORKFLOW.md](../docs/RESEARCH_WORKFLOW.md): certificate registration and computational scope

Read the full statements and proofs. Submitted evidence does not supply an accepted premise.

## Approach and first bounded experiment

Reuse the reviewed finite Schur/path implementation from PR #78. Add a separate layer with one capacity per source label and the two stated incidence maps. Encode the PR #98 overlap case as a failure control, then require an actual-source fixture before claiming geometric applicability.

## Expected evidence

- An independently implemented exact verifier with positive cases and meaningful negative controls.
- A precise mapping from each finite graph condition to the theorem hypothesis it checks and a list of unverified geometric steps.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the checker is presented as validating arbitrary canonical response geometry, or if graph rank is substituted for the stated Schur matrix without a proof.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py verify-a-source-capacity-coupling
```

## Remaining lemma and limitations

For the actual source and response, establish rank(S)<=d_int+|C^partial|-Delta_Lambda (d_sc>=Delta_Lambda); in the locked branch the exact Section-175 surplus is |O_iso|+sum_i max(0,|O_i|-|C_i|)>=j_*+|T_Z|. Any untouched zero-slack/global-realization branch remains.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.
