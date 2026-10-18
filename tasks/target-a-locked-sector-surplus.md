# target-a-locked-sector-surplus

**Investigation:** `target-a-locked-sector-surplus-successor-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: A positive result must pay the actual j_* demand; a negative result must identify a source hypothesis that rules out the supplied nonglobal regressions.

Prior evidence:
- [regression](../research-packages/target-a-fan-tube-ledger/README.md) at `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`: Seed-63 full-tube ledger; the submitted canonical-admissibility claim is corrected in the current package. Admissible optimum 1; relaxed optimum M-1. Remaining: Actual source demand and phase selection are absent.
- [agent-audited](../research-packages/target-a-full-tube-fan-ledger/README.md) at `aa111eedcd3bc190f991aeaa7f42299948551207`: seed-66 fixed-phase ledger and basis-independent upper bound 3; not a sharp all-basis optimization. Integration corrects the stale PR #87 comparison; the seed-66 result is unchanged. Remaining: Actual source-demand extraction and a sharp hexagonal all-basis optimum are not established.

Independent integration reviews: [Target A](../docs/research/review-artifacts/merge-2026-10-18/review-a.txt), [Target B](../docs/research/review-artifacts/merge-2026-10-18/review-b.txt), [Target C](../docs/research/review-artifacts/merge-2026-10-18/review-c.txt).

**Track / priority:** target-a / direct frontier; selection weight 5 (attention only).

## Exact objective

For an actual plateau response with a Section-102 admissible basis, what joint source-demand, phase and sink-population inequality can force Xi >= j_* + |T_Z|?

## Definitions, hypotheses and complete prerequisites

- Use the actual plateau-terminalized response X* and the canonical three-channel locked fan when the locked branch is invoked.
- Keep the Section-175 tube, sector sets, isolated exterior sinks, and j_* bookkeeping as defined in the active Target A modules.
- The goal is the canonical global rank/nullity inequality or a genuine same-cardinality competitor, not a bound on a response scaffold alone.

- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): targets.target-a; Sections 175-177 and the global Schur endpoint
- [docs/targets/target-a/27-tube-only-right-deficiency-frontier.md](../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md): Section 175 tube-only right-deficiency identity and exact locked-branch inequality
- [docs/targets/target-a/29-lens-source-gate-refinements.md](../docs/targets/target-a/29-lens-source-gate-refinements.md): Section 177 lens and source-gate alternatives

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-a/README.md](../docs/targets/target-a/README.md): fixed-source Hall capacity is exact and does not exceed the same-hull bound
- [docs/targets/target-a/27-tube-only-right-deficiency-frontier.md](../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md): the pointwise tube charge is O(|V(Sigma)|); the missing term is source-specific sink/sector surplus
- [docs/targets/target-a/29-lens-source-gate-refinements.md](../docs/targets/target-a/29-lens-source-gate-refinements.md): lens shielding retains a basis-sensitive penalty and can have overlapping exterior sink sets

## Approach and first bounded experiment

Start from the corrected seed-63 admissible optimum 1 and the seed-66 pointwise phase obstruction. Name the actual source and its demand before choosing phase. Derive one inequality retaining the deep restriction, distinct sinks and the phase-dependent tube cost.

Methods: sector-by-sector exact accounting, max-flow/Hall reduction with a source-specific surplus lemma

## Expected evidence

- A complete proof of the exact Section-175 surplus inequality under canonical hypotheses, including all overlap and integer terms.
- Or a certified counterexample to a proposed stronger intermediate inequality, with its missing hypothesis identified.
- A final implication to the global Schur endpoint or a strict same-cardinality sub-D competitor.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the argument only improves a tube constant, counts local gates, or gives an O(D) estimate without controlling the required exact Schur deficiency; record the specific unclosed term.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-a-locked-sector-surplus
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

For the actual source and response, establish rank(S)<=d_int+|C^partial|-Delta_Lambda (d_sc>=Delta_Lambda); in the locked branch the exact Section-175 surplus is |O_iso|+sum_i max(0,|O_i|-|C_i|)>=j_*+|T_Z|. Any untouched zero-slack/global-realization branch remains.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-a-locked-sector-surplus --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
