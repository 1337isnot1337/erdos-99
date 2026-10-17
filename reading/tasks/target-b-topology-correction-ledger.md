> Generated reading edition · [exact source](../../tasks/target-b-topology-correction-ledger.md) · source SHA-256 `b68a32b8751befbcada1a887411d2d0f7252ab323d802763c7367a9bd8d0b91a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# target-b-topology-correction-ledger

**Track / priority:** target-b / direct frontier; selection weight 3 (attention only).

## Exact objective

Can the outer-shell inequality be proved on finite rhombic cell complexes with holes and multiple components while retaining exactly the correction (t+chi-1), rather than importing a disk-only estimate?

## Definitions, hypotheses and complete prerequisites

- The required global expression is G+E >= (sqrt(3)/4)B + (sqrt(3)/2)(t+chi-1).
- Count boundary components, holes, and component terms with the canonical sign convention from Target B.
- A proof for a simply connected disk is not a proof for general topology.

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): joint shell stability inequality and current topology requirement
- [docs/targets/target-b/01-jammed-rhombic-branch.md](../docs/targets/target-b/01-jammed-rhombic-branch.md): Sections 24-56 and exact boundary/shell quantities
- [docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md](../docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md): promoted phase-cut results and hole correction HA

Read the named statements and their complete proofs; this card does not weaken their hypotheses. Audited-working premises: none silently admitted; consult the exact claim lifecycle if importing an additional result.

## Relation to Level I

Advances only the stated route obligation; global closure still requires all canonical hypotheses and the universal minimizer quantifiers.

## Existing obstructions

- [docs/targets/target-b/README.md](../docs/targets/target-b/README.md): the phase-star exclusion is limited to its pure-disk and coherent-core hypotheses
- [docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md](../docs/reports/target_b_phase_cut_and_biclique_2026-09-05.md): HA pays the stated hole correction but does not establish the full shell inequality

## Approach and first bounded experiment

Enumerate the Euler and perimeter identities for a disk, annulus, and two-component rhombic cellulation. Derive the coefficient of each boundary component before using any phase-energy estimate; then attempt the smallest extension of HA that preserves the displayed topology term.

Methods: Euler characteristic and face-incidence accounting, exact finite cellulation enumeration

## Expected evidence

- An exact combinatorial-geometric identity for the boundary and face terms on the stated cell complexes.
- A proof that its error terms imply the canonical coefficient, or a small exact cellulation that falsifies the proposed identity.

## Falsification and stopping

Test the proposed implication against every listed obstruction with the same hypotheses. Exhibit a concrete failing constraint, parameter order or rank/population ledger; do not interpret an optimistic relaxation as a feasible source.

Stop if the proof sets t+chi-1 to zero, treats a multiply connected domain as a disk, or obtains only an O(D) correction when the endpoint is boundary-order exact.

## Reproduction

```sh
python tools/check_public.py
python tools/task_context.py target-b-topology-correction-ledger
```

The task-context command lists certificate commands for the direct and transitive file prerequisites. For a proof-only task, reproduce the derivation rather than claiming a computation proves it.

## Remaining lemma and limitations

Establish G+E>=(sqrt(3)/4)B+(sqrt(3)/2)(t+chi-1) for the full canonical source with all multi-grain, interface, topology and uniformity hypotheses, or construct the full same-cardinality strict sub-D competitor.

No finite model, one-grain result, local packing, infinitesimal flex or supplied-set calculation proves Level I, global source realization, uniform onset, or the unencoded remainder of its route.

## Live overlap and session scope

Run `python scripts/choose_research_task.py --task target-b-topology-correction-ledger --live-overlap --json` and inspect matching public work. [Proposal snapshots](../docs/research/proposals.md) record adjacent source proposals without assuming they are accepted or live public claims.

One 30–60 minute proof sublemma, exact finite model, independent replay or precise handoff; recheck upstream before continuation.
