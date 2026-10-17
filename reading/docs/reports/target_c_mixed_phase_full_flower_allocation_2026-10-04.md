> Generated reading edition · [exact source](../../../docs/reports/target_c_mixed_phase_full_flower_allocation_2026-10-04.md) · source SHA-256 `58740d3a3b11c252b3a3231bcef1b61bec83b88b4aa232400f31e0d2c20b18fc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5FA9170B1DDE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_mixed_phase_full_flower_allocation_2026-10-04.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=fc265f18e2abc48c85f8fd2da1b1f433f92fbd59; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C: mixed-phase full-flower allocation and through-splicing lemmas

**Date:** 2026-10-04\
**Repository commit:** `63d21d191b673c5a3de3b3f0189c9b5f491deeac`\
**State version:** `2026-09-14.audit.51`\
**Run type:** synthesis of proof-only research candidates\
**Target:** C\
**Starting status:** unreviewed candidate reports\
**External literature search:** not used\
**Computation:** four finite regression scripts; none certifies global optimality

## Level I status

`STILL OPEN`. These local allocation and graph-deficit results do not close C-II.

## Provenance

The source is `sol/c2-flower-blocker-20260915` at exact tip
`95013b579895183089c4d2b3f0962588eda6abcd`. No pull request was opened for that
branch. Its five proof reports, five hostile audits, and four regression scripts are
preserved under `research/`. The separate projective-blocker report has no companion
script. The hostile audits accept the scoped claims while explicitly rejecting a
global-motion or C-II conclusion.

The current main report
`research/target_c_dominant_pentagon_through_splicing_2026-09-15.md` preserves an
all-dominant through-splicing/Mantel-deficit result. This salvage adds distinct
full-flower allocation, blocker localization, and mixed-complement-phase lemmas; it
does not replace or strengthen the canonical route.

## Preserved claims

1. **Nested orbit allocation.** For one exact triangular projective orbit, if four
   sides of a strict convex unit pentagonal contact face lie in its projective
   `rho`-neighborhood, with `0<rho<1/10`, then all five lie in the neighborhood of
   radius `2 asin(2 rho)`. The hostile audit repairs and checks the atomic-limit
   quantifier. The result is applied to the exact dominant-orbit splicing theorem only
   after taking the outer limit `rho -> 0`.
2. **Projective blocker.** No projective arc of length `pi/3` contains four side
   directions of a fully rhombic convex pentagon. Thus each external train is
   noncrossing with at least two of the five flower trains and crosses at most three.
   For `T_R` trains and `M` such flowers, the exact localized degree inequality is
   `sum_{tau in I(F)} d_R(tau) <= 3(T_R-5)` for each flower, with the corresponding
   noncrossing-pair count retaining the finite `-2` term.
3. **Three-dominant local normal form.** A limiting full pentagon with at least three
   sides in one exact triangular orbit either has the all-orbit through-pair form or
   an alternating-return form. Unselected flowers in the latter population contribute
   at least three complement terminal occurrences each; this count is by occurrence
   and does not assume endpoint simplicity between flowers.
4. **Mixed-phase splicing deficit.** Under the stated uniform direction-mismatch,
   connector-interiority, and positive-projection hypotheses, a linear population
   `L_D` of local through pairs contains a vertex-disjoint subpopulation of size at
   least `L_D/3`, yielding `T_D^2/4-R_D >= L_D^2/18-o(D^2)`. When phase continuity
   excludes short splice cycles and the component count is `o(D)`, the matching size
   improves to `L_D/2-o(D)`, yielding `T_D^2/4-R_D >= L_D^2/8-o(D^2)`.

These are proof-only structural statements with the exact hypotheses in their linked
research reports. The displayed numerical floors are below the already-known
aggregate full-flower Mantel deficit; the preserved value is localization to actual
local through mechanisms and arbitrary complementary phases. No source deformation,
diameter decrease, or simultaneous application of all splices is proved.

## Exact regression runs

All commands were run at this report's repository base:

| Script | Result |
| --- | --- |
| `research/verify_target_c_full_flower_nested_orbit_allocation.py` | PASS; four-ray squared-norm spectrum `[0,1,3,4,7,9,12,13,16]`; 360 unit four-ray sums |
| `research/verify_target_c_three_dominant_flower_through_pair.py` | PASS; three-ray squared-norm spectrum `[0,1,3,4,7,9]`; finite class census matched |
| `research/verify_target_c_mixed_flower_matching_splice_deficit.py` | PASS; displayed coarse deficit exceeds `0.0002445734722` |
| `research/verify_target_c_mixed_flower_half_matching_upgrade.py` | PASS; displayed coarse deficit exceeds `0.0005502903125` |

The scripts check finite direction arithmetic, graph/matching formulas, and displayed
numerical propagation. They do not independently prove the analytic asymptotic claims.

## Claim classification

**Classification:** unreviewed candidates. No theorem-state, target route, prompt, or
canonical dependency is changed. The next possible use would be to couple the localized
through-splice deficit to diameter bracing or exceptional-face closure while retaining
all complement phase variation.
