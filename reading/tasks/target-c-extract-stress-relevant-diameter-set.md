> Generated reading edition · [exact source](../../tasks/target-c-extract-stress-relevant-diameter-set.md) · source SHA-256 `f3f0768519cad76d6a1e7c920cf67650a5a6bf1cb0642d4a560530109a169fbb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# target-c-extract-stress-relevant-diameter-set

**Track / priority:** target-c / direct frontier; selection weight 3 (attention only).

## Exact objective

Can one extract from a canonical source a stress-relevant loaded set W to which the supplied-W stress deletion theorem applies, while controlling the exceptional diameter-edge mass and preserving all source labels?

## Definitions, hypotheses and complete prerequisites

- The target source is contact-minimal, then diameter-pair-minimal, with all contact isolates retained.
- Audit 171 is used only after a nonempty actual loaded set W is supplied; it does not itself extract W.
- If the one-star refinement is used, prove its actual diameter support has the stated star scope.

- [docs/state/theorem-state.yaml](../../docs/state/theorem-state.yaml): C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL
- [docs/state/theorem-state.yaml](../../docs/state/theorem-state.yaml): C-STAR-EXCEPTIONAL-FACE-ONE-UNLOADED-TRANSVERSAL
- [docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md](../docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md): C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL
- [docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md](../docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md): C-STAR-EXCEPTIONAL-FACE-ONE-UNLOADED-TRANSVERSAL
- [docs/targets/target-c/CURRENT.md](../docs/targets/target-c/CURRENT.md): supplied-W deletion and star refinement limits

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-c/CURRENT.md](../docs/targets/target-c/CURRENT.md): the full actual diameter graph is required and the stress-relevant W is not extracted
- [docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md](../docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md): the one-star theorem has exact scope restrictions and gives no star extraction
- [docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md): source deletions produce a cardinality-losing descent; restoration remains a separate endpoint

## Approach and first bounded experiment

Start from an extreme normalized stress on the actual contact/diameter constraint system. Identify its support on loaded diameter endpoints, compare that support to the canonical owner and face sets, and formulate the smallest W-selection rule that would give a useful deletion budget.

Methods: stress-face and owner-set analysis, finite exact KKT support enumeration

## Expected evidence

- A canonical-source theorem that extracts W with a quantitative bound on exceptional edge mass and preserves all source labels in the subsequent motion check.
- Or a finite exact stress/polytope regression showing that a proposed support rule cannot be forced from the current hypotheses.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the task merely restates the deletion theorem for a supplied W, assumes a globally single-star support, or treats stress deletion as cardinality-preserving.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-c-extract-stress-relevant-diameter-set
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Construct a canonical full-source same-cardinality finite endpoint preserving every lower and actual-diameter upper pair bound and all applicable face constraints, with a triangle-free endpoint at D with lexicographically fewer contacts/actual-diameter pairs or strict sub-D diameter; separately close any untouched macroscopic-container restoration branch.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-c-extract-stress-relevant-diameter-set --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.

## Related loaded-port route

Use the [owner-release and loaded-anchor track](../docs/research/tracks/target-c-owner-release-loaded-anchor.md) when comparing stress-supported diameter endpoints with owner-respecting anchors. Its global near-disk proximity estimate does not establish the required same-owner crossing incidence; do not treat an arbitrary nearby loaded hull vertex as a valid owner port.
