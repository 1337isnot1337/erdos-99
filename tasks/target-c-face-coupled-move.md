# target-c-face-coupled-move

**Track / priority:** target-c / direct frontier; selection weight 5 (attention only).

## Exact objective

Can the surviving full-core outer-to-bounded or bounded-to-bounded train/face system be converted into a source-realized finite move or discrete replacement that improves the contact/diameter-pair lexicographic count at D while remaining triangle-free or gives a same-cardinality strict sub-D competitor?

## Definitions, hypotheses and complete prerequisites

- Use the contact-minimal, then diameter-pair-minimal canonical source with C=C_* and H=H_*.
- Retain every source point, including all contact-isolated points, in the move and every feasibility check.
- At diameter D the endpoint must remain triangle-free and have lexicographically
  fewer unit contacts/actual diameter pairs. A same-contact endpoint with fewer
  actual diameter pairs is sufficient; contact loss accompanied by a new unit
  triangle is insufficient. A strict sub-D competitor need not be triangle-free.
- [Finite lexicographic exchange proof](../docs/audits/target_c_contact_budget_diameter_exchange_independent_audit_2026-10-06.md): exact equality-diameter endpoint and all inserted-pair hypotheses.
- Check every old unit contact, every full-source noncontact lower pair, every
  full-source upper pair including previously inactive upper pairs, all
  at-most-d_H exceptional upper constraints, and each unary rhombus test.

- [docs/state/theorem-state.yaml](../docs/state/theorem-state.yaml): Target C canonical scope and current C-II status
- [docs/targets/target-c/CURRENT.md](../docs/targets/target-c/CURRENT.md): full-core exact remaining endpoint and finite-move limitations
- [docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md): exact next split and full-core finite-move tests
- [docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md](../docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md): Audit 171 supplied-W deletion; no W extraction or restoration
- [docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md](../docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md): Audit 174 removes the positive one-cell collar range only

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md): generic near-unit planarity and O-O supply are bounded; the remaining linear obstruction must be face-coupled or an explicit unary blocker
- [docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md](../docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md): stress-killing deletion has no extracted W or cardinality restoration
- [docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md](../docs/audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md): the higher-(q-k)/D Type-II range and separate macroscopic branch remain open
- [docs/reports/seed090_finite_rhombus_contraction_2026-10-13.md](../docs/reports/seed090_finite_rhombus_contraction_2026-10-13.md): Unreviewed corrected Seed 90: nonexpansive endpoints can lock a dense nonglobal frame; its contact-preserving bow requires only two actual diameter pairs and explicit full-source gaps, so it does not supply a canonical endpoint.
- [docs/reports/seed090_shared_edge_overlap_audit_2026-10-14.md](../docs/reports/seed090_shared_edge_overlap_audit_2026-10-14.md): Exact shared-label regression: same-half-plane rhombi may share a third label. Use the overlap case split before reusing edge propagation.
- [docs/reports/target_c_pentagon_activation_and_contact_debt_preservation_2026-10-15.md](../docs/reports/target_c_pentagon_activation_and_contact_debt_preservation_2026-10-15.md): Unreviewed finite wall obstructions: one opened side must exceed sqrt(3); exactly two opened sides require a^2+b^2>4; internal-only contact repayment needs deleted wall adjacencies. Actual train-collar embedding remains conditional.

Source PR #950 supplies unreviewed path structure but no endpoint. Its linear train-return family and separate linear attachment-to-grid Menger family can end at disjoint loaded labels; the corrected endpoint-inclusive cuts fix the linkage proof but do not give label overlap or a finite move. The [train-return/rigidity-grid track](../docs/research/tracks/target-c-train-returns-rigidity-grid.md) records the original candidate, and the [harmonic-cell/face-floor track](../docs/research/tracks/target-c-harmonic-cell-face-floor-source-bridge.md) adds the source-main full-cell variant, the face-floor exclusion, and the exact missing attachment-count or common-label bound.

Source PR #948 adds conditional quarter-fold restrictions on convex, deep, rigid, and large faces. They constrain an existing full-source exact-graph endpoint; they do not establish one. The [quarter-fold/bent-array track](../docs/research/tracks/target-c-quarter-folds-bent-arrays.md) records the seven claims and the required full-source endpoint checks.

The separate October threshold-staircase route now has edgewise KKT packets, a
common opposite-shore load, and a conditional two-cut shear. Its exact
limitations and distinction from the complete-grid branch are in the
[exact-phase packet and cross-shore track](../docs/research/tracks/target-c-exact-phase-packet-fork.md).
Packet positivity has no uniform stress gap, and the shear shortens only a
selected linear family of diameter rows; use it as route evidence, not as a
finite endpoint.

## Approach and first bounded experiment

Write one candidate move with explicit train endpoints, owner labels, deleted labels, and restored labels. Encode the lower and upper squared-distance constraints for every source pair, including isolates, and solve the smallest nontrivial face-coupled case exactly before seeking a uniform theorem.

Methods: owner/face implication graph plus exact displacement constraints, small rational realization and exact squared-distance audit

## Expected evidence

- A finite-move theorem with all source constraints, giving either strict sub-D
  diameter or a triangle-free endpoint at D with strict lexicographic improvement
  in unit contacts/actual diameter pairs.
- Or a certified exact regression to the proposed endpoint, identifying the obstruction that a stronger lemma must avoid.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the argument only builds a path forest, deletes stress-support labels without restoring cardinality, assumes simultaneous compatibility of individual exchanges, or treats C-I shear results as a C-II finite motion.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-c-face-coupled-move
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Construct a canonical full-source same-cardinality finite endpoint preserving every lower and actual-diameter upper pair bound and all applicable face constraints, with a triangle-free endpoint at D with lexicographically fewer contacts/actual-diameter pairs or strict sub-D diameter; separately close any untouched macroscopic-container restoration branch.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-c-face-coupled-move --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.

## Related full-source owner-release candidates

Before building a new implication graph, read the [owner-release and loaded-anchor track](../docs/research/tracks/target-c-owner-release-loaded-anchor.md). It records exact strict/equal-floor closure, unequal-height isolate transport, the loaded-anchor upper box, and the current source-extraction obligation. Those theorems solve only their supplied owner classes; they do not supply the canonical family or a nonzero feasible assignment.
