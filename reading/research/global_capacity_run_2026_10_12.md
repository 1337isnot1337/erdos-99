> Generated reading edition · [exact source](../../research/global_capacity_run_2026_10_12.md) · source SHA-256 `a0dbb4a97ade7cb254e20ee39c650d9f3ac60058a112ae6a0741731531265077`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Global Level I run, 2026-10-12

- Base: `ab6dd3336f9f8d440f2bada76edb32153391cddc` (`origin/main`).
- State version: `2026-10-10.audit.234`; Level I open.
- Branch: `research/global-capacity-20261012`.
- Target: the literal Level I statement, independently of the A/B/C bookkeeping.
- Endpoint: every sufficiently large triangle-free global minimizer must admit
  a same-cardinality planar, unit-separated configuration of strictly smaller diameter.
- Dependencies: the definition in `docs/problem/statement.md`, elementary
  Euclidean distance identities, and exact finite signed-graph feasibility.
  No unpromoted report is a premise. No source label may be omitted.
- Bootstrap: current state lock and manifest, problem statement, the whole-problem
  prompt and workflow read. The C-II route is context, not a proof dependency.

## Global ideas tested before selecting a construction

These are exploratory/rejected shortcuts, not theorem claims.

1. A population-only triangle-free density ceiling cannot settle attainment:
   the canonical triangle-free lattice-competitor regression retains the known
   positive reserve. A strict comparison needs source information as well.
2. A bounded contact coloring permits an orthogonal lift that opens contacts
   and shortens diameters in an extra dimension. Returning to the plane is
   an additional constraint, so this does not give a planar competitor.
3. Fixed-radius reassignment, fixed-wall refill, and a purely affine change
   restrict the competitor before global optimality is used. They are not the
   selected closure mechanism.
4. Shape completion and global packing capacity restate optimality, but do not
   supply strict source improvement without a new packing theorem.

## Selected construction under investigation

Choose an arbitrary line and two positive scale factors. Every label chooses
one of its two reflected positions after scaling normal and tangential
coordinates. Pairwise separation forces some choices to have opposite signs;
the strict diameter bound forces some to have the same sign. The choices
must be made simultaneously, using every source pair, including isolates.

Proposed chain:

```text
full-source reflected/scaled endpoint is feasible
  -> all n labels retained, all pair distances >= 1 and < D
  -> contradiction to the source's global optimality
  -> Level I only if endpoint existence is proved for every sufficiently
     large triangle-free global minimizer
```

## First mathematical checkpoint

The full-source decision theorem and an infinite explicit rectangle-family
construction are proved candidates awaiting promotion, preserved in an
unreviewed report. The 157-label certificate retains both contact isolates,
checks all 12,246 pairs, opens every contact, and strictly reduces squared
diameter from 916 to `865065744/1008005`. Every affine deformation is blocked;
the original source has normalized nonnegative equilibrium and a PSD stress
on its boundary support. Thus this is a concrete escape from that obstruction,
not an optimality certificate. The source is nonglobal.

Evidence: `docs/reports/global_reflected_scale_competitors_2026-10-12.md` and
`research/verify_global_reflected_scale_2026_10_12.py`. Additional explicit
endpoint fixtures check 29,403 and 182,710 full-source pairs. The exact script,
artifact regeneration, theorem-state check, theorem-state PR check, and
`git diff --check` pass.

## Global audit of the construction

`docs/reports/global_reflection_moment_obstruction_2026-10-12.md` gives a
proved candidate obstruction applying to every leading-density source, in
particular every global-minimizer sequence: any feasible one-step endpoint
with diameter at most `(1+o(1))D` must have both scale factors tend to one.
The proof uses canonical Oler Lemma 21.1, the full-source empirical disk
limit, and exact second/fourth moment identities. Isodiametric disk equality
was verified in the original Maggi--Ponsiglione--Pratelli paper.

Unrestricted compositions are not a bridge: allowing infeasible intermediates,
one selective reflection per label can realize any prescribed target. Bounded
coherent packet reassembly would need an independent geometric packing gain.

Exploratory searches tested 24,000 fixed-line/sign linear programs on the
regular unit heptagon, a two-fold differential-evolution run, and coordinate
shuffles over 301 axes and all 5,040 heptagon coordinate permutations. None
gave a strict endpoint. These searches do not prove impossibility or
optimality, and are not mathematical premises. Do not repeat them unchanged.

## Whole-container symmetrization audit

`docs/reports/global_steiner_capacity_loss_2026-10-12.md` gives exact regressions:
a four-label triangle-free global minimizer has Steiner capacity drop 4 to 3;
an unbounded triangle-free unit-rhombus family has original capacity exactly
`(m+1)^2` but symmetrized capacity at most `(m+1)^2-m/10+2/3`. This loses
linearly many labels despite optimal fixed-container capacity and optimal
leading area density. The large examples are certified nonglobal for diameter.
The paired exact verifier checks 97,020 source pairs at `m=20` and the
capacity bounds at `m=20,40,100`.

Endpoint existence in the global-minimizer regime remains unresolved. Neither
macroscopic one-step scaling nor general symmetrized-container capacity is a
closure mechanism. The exact global obligation is unchanged; the next idea
must add genuine source-wide geometric information, not representability,
area density, or a continuous local stress argument.
No Level I closure is claimed. The user's ongoing research goal remains active.

## Reviewable checkpoint and CI provenance

Draft PR: https://github.com/1337isnot1337/e-99/pull/959.
All mathematical reports remain unreviewed. The branch contains unique active
research and is retained for the draft PR and continuing goal.

Remote state-consistency run `38338923570` did not execute any job steps,
so it provides no passing hosted-CI evidence. The local exact verifiers,
theorem-state checks, artifact regeneration and whitespace checks completed
successfully.
