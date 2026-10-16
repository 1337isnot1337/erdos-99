<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bcb17c279f621f1753f012a6ab3f31fc673eae84", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/repository_state_and_sol_prompt_review_2026-09-10.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8629d8a0ea2477f19c77984a188c4e8a4fa8ab3a78576f9cc1b164a002c0ddb3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — current-state analysis and sol xhigh prompt design

**Date:** 2026-09-10
**Starting state:** `main`, `3f37ef0eab4407a411f9a6d51d016ba600302be7`; clean worktree
**Run type:** repository-state review / research-prompt authoring
**Target:** Level I, with all three route maps compared
**Mathematical status:** STILL OPEN
**New theorem or promotion:** none

## 1. Outcome and review scope

The new deliverable is the [sol xhigh full-settlement launch prompt](../prompts/erdos_problem_99_SOL_XHIGH_FULL_SOLUTION_PROMPT.md).
It prioritizes C-II, preserves alternative routes and disproof, and distinguishes
the promoted C-I result from the substantial but unpromoted September 9–10 campaign.
It is a launch prompt, not a replacement route prompt or new theorem-state version.

This review inspected the repository instructions, research/prompting workflow,
problem and literature baseline, all three route maps, active prompts, the existing
whole-problem launch, selected underlying theorem sections, the promoted C-I
restoration proof, and recent report-level results and their stated dependencies.
The newest full-source circumradius report was read in full, as were the Z/ZR/ZF
statements and proofs, ZS and the exact post-ZF ledger, the RA representative change,
and the redundant-rigidity report. Selected claims, dependency sections, and handoffs
were inspected in the longer constant-improvement campaign.

This is not an exhaustive independent proof audit of the inherited theorem library
or every recent report. No report-level theorem is promoted by this review. The
distinction between reading a proof, checking its stated role, and independently
auditing all of its dependencies is essential to the recommendations below.

The tracked inventory at the starting commit contains 29 Target A files, 2 Target B
files, 59 Target C files, 265 files under reports, and 37 under research. These are
file counts, not counts of independent theorems. File-number order is not authority.
The route maps and explicitly scoped promotion notices control the live state.

## 2. Promoted mathematical frontier

### Global quantifiers and common numerical input

The [problem statement](../problem/statement.md) requires every sufficiently large
global minimizer to contain a unit triangle. A negative answer requires triangle-free
global minimizers for unbounded cardinalities. Local minima, finite examples,
asymptotic density, or existence of one favorable minimizer per cardinality do not
resolve the quantifiers.

An important sharper input is [Target B Section 36.1](../targets/target-b/01-jammed-rhombic-branch.md):
\[
D(n)^2<\frac{2\sqrt3}{\pi}(n-1).
\]
It is unconditional despite its route-specific file location. Shared Oler applied
to all source points gives, for `K=conv(A)`, `P=per(K)`, `a_0=sqrt(3)/2`,
`c_0=sqrt(3)/4`,
\[
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1)\ge0.
\]
Together with `delta_K=pi D^2/4-area(K)`, the strict lattice bound yields
\[
\delta_K+\mathscr O_A<c_0P.
\]
This is an exact full-population contradiction target, not merely a leading-order
density target. Writing its reverse does not prove it.

### Target A: Section 174, not just Section 167

The [Target A route map](../targets/target-a/README.md) reaches Section 174.
Sections 168–174 add zero-slack normalization, actual-response locking, contact
crosscuts, three disjoint stress channels, sector Hall bounds, and basis-closed
unit-tube sector balance. The [active A prompt](../prompts/erdos_problem_99_1.7.10_FINAL_CONTINUATION_PROMPT.md)
and shorter top-level navigation still emphasize Sections 163–167.

The exact open inequality remains
\[
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda,
\qquad d_{\rm sc}\ge\Delta_\Lambda.
\]
In the locked branch, [Section 174](../targets/target-a/26-tube-shield-sector-balance.md)
reduces this to proving that signed sector population surplus pays the entire
nonterminal shield charge plus `s=Delta_Lambda-d_int`. Coordinate identification,
proper-crosscut existence, exterior-sink sharing, and sector basis imbalance have
already been addressed under the stated branch hypotheses. They are not new closing
lemmas to rediscover.

The [September 8 tube-only report](target_a_tube_only_cut_2026-09-08.md) is a
useful unpromoted refinement:
\[
\zeta\ge t_\Sigma+\delta_\Sigma-|T_\Sigma|.
\]
After audit it would suffice to prove
`t_Sigma+delta_Sigma>=s+|T_Sigma|` for an admissible stress-generated shield.
The zero-slack/descent branch still needs coverage. This report does not prove the
population surplus.

Fixed-hull Hall capacity is exact; a witness exceeding it in the same source hull is
impossible. The five-block strain architecture also has a proved local quartic
barrier. A source-specific transport theorem or an exterior-compatible finite
competitor remains substantive; more local certificates alone do not close A.
Closing A by itself leaves the complementary global branch to address.

### Target B: coherent subcases excluded, coverage open

The [Target B map](../targets/target-b/README.md) promotes the September 5
[phase-cut/coherent-family addendum](target_b_phase_cut_and_biclique_2026-09-05.md).
It supplies PC/PW, coherent crossing estimates, phase-star and near-extremal
exclusions, stability/extraction results, and the hole correction, with their exact
hypotheses. It does not show that every jammed survivor has a coherent core meeting
those coverage and near-extremality conditions.

The exact sufficient shell inequality is
\[
G+E\ge\frac{\sqrt3}{4}B+\frac{\sqrt3}{2}(t+\chi-1).
\]
The global-minimizer allowance is strictly smaller. Any proposed proof must control
holes, exceptional faces, outside points, and active diameter constraints. An
uncontrolled boundary-order loss may consume the entire useful margin. B is not a
substitute for Target A's source-capacity argument unless a transport is proved.

### Target C: C-I closed; full-source C-II open

[Module 56](../targets/target-c/56-ci-restored-frontier.md) and its promoted
[orientation/dependency audit](target_c_c53_orientation_and_ci_restoration_2026-09-09.md)
control older conflicting wording. They establish:

- selected-source PSD for every normalized KKT stress, using actual circular-planar
  response, affine equilibrium, and consistent diameter-thrackle normalization;
- convergent finite correction releasing weak active rows, hence C-I closure;
- contact/diameter lexicographic representatives with `C=C_*` and `H=H_*`;
- the common-stress-kernel local normal form, with isolated scalar coordinates retained.

The remaining gate excludes all sufficiently large triangle-free representatives of
that kind. It is enough to exclude this reduced class if its reduction from an
arbitrary counterexample is preserved. It is not legitimate to identify that
representative with the separate hull-saturated one without proof.

The old pentagon PSD objection is withdrawn; the heptagon-center objection to
force-bulk localization is not. The latter blocks declaring all isolates diametral
or identifying the full population with the positive core. No general numerical
conductance floor, pure-rhombic topology, or complete C-II contradiction is promoted.

## 3. Recent working frontier: valuable, but separate authority

### Full-source circumradius transport — latest commit

The [September 10 FS report](target_c_full_source_circumradius_response_2026-09-10.md)
is the only file in commit `3f37ef0`. It explicitly remains unpromoted.
Its proof chain starts from Oler on the full source and the existing Bonnesen
estimate, then uses containment of every selected force hull and KKT virial balance.
It records
\[
R(K)=D/2+O(\sqrt D),\quad P_*=2D-O(\sqrt D),
\quad\theta_{\text{shared diameter}}=O(D^{-1/4}),
\]
uniformly over selected stresses and global sources, with no small-isolate premise.
It also bounds diameter midpoints about one center and gives near radiality of the
actual response on coordinate fields.

This is the most useful initial candidate for the launch prompt because its stated
dependency chain is short and directly addresses the full-population gap. That is
a research-priority judgment, not a prediction of settlement or a promotion.
It imports an upper containing-radius bound into selected force geometry, not a
near-maximal force-hull area conclusion.

Its two exact shell no-go results are as important as the estimates. Odd unit shells
have `2D-P_* -> 0`, but a matching retains at most asymptotically half the diameter
weight and the actual PSD response trace defect is `2D^2-2`. Dense isolated fillings
preserve that obstruction without a global-optimality certificate. Thus neither
“near matching” nor “small trace” follows from the stated response geometry. The
closing theorem must use additional exact global capacity or reconfiguration data.

### Z/ZR/ZF and the boundary/face ledger

The [zero-transfer campaign](campaign_zero_transfer_and_narrow_paths_2026-09-09.md)
and [consolidated review](campaign_zero_transfer_defect_review_2026-09-09.md)
record a separate unpromoted chain: diagonal transfer becomes an additive terminal
resistance metric, the large C-II zero-transfer case is excluded, the C56 generic
kernel conclusion gives maximal scalar stress rank on the core, and finite
integration gives mixed equality-bar rigidity. Its dependency audit is required;
restoration of C53/C63 alone is not restoration of C56 or all downstream claims.

With `v` core vertices, `e` contacts, and `h` actual diameter pairs, ZF gives
`e+h>=2v-2`. Euler converts a possible contradiction into
\[
b+\sum_{F\text{ bounded}}(\deg F-4)>2h.
\]
The outer walk counts multiplicity. This form keeps exceptional topology visible;
a pure-disk exclusion cannot be silently extended to it.

[ZS](target_c_zf_boundary_surplus_collapse_2026-09-09.md) gives
`q>=h>=delta>=ceil(D)` and `sigma_B>=ceil(D)-2` after ZF. Therefore the older
`sigma_B=o(D)` normal form cannot be reused for that source. The
[ZM/ZS reconciliation](campaign_zm_zs_reconciliation_2026-09-09.md) explicitly
flags this trap. This does not invalidate individual older lemmas whose proofs have
weaker hypotheses; each proposed use must be checked separately.

The [exact defect addendum](target_c_zf_exact_defect_budget_addendum_2026-09-09.md)
resolves the surplus into finite nonnegative quantities:
\[
q=x_B+f+g_F+2d_H+2s_Z,
\qquad c_I+e_{BB}+s_C=q-2+d_H+s_Z.
\]
These identities say where a survivor spends its boundary and stress budget.
They do not by algebra alone make the nonnegative mixed-row slack `s_Z` negative.

### Rigidity and bridge refinements

The September 9 MC/TF/BM/CS/RR reports add actual mixed-support connectivity,
terminal fans, bridge-cut matchings, circuit ledgers, and
[redundant rigidity](target_c_mixed_redundant_rigidity_edge_cuts_2026-09-09.md).
RR's direct row-dependence argument makes every mixed edge redundant after ZF;
a cut with both sides nonsingleton needs at least four mixed edges. A contact
bridge on such a cut therefore has at least three actual diameter bypass edges.
These are useful structural restrictions, not a global packing contradiction.

The [superstable-bar report](target_c_superstable_bar_sap_2026-09-09.md) makes an
essential sign distinction: equality-bar universal rigidity does not establish
rigidity under the packing's cable/strut inequalities. The PSD KKT/bar stress has
the opposite proper-stress signs for those inequalities. This blocks an especially
tempting false “full proof” after maximal-rank PSD.

### Pocket and pinned-surplus campaign

The [projective-circle area report](target_c_projective_circle_isodiametric_area_floor_2026-09-09.md)
records a post-ZF/DB area floor of approximately `0.4978566363 D^2`; this is not the
disk area `pi D^2/4`. Subsequent pocket, cavity, exact-defect, and finite-feedback
reports improve exclusions of low pinned/contact surplus. The newest
[Dirichlet/PI report](target_c_dirichlet_pi_feedback_surplus_04702_2026-09-09.md)
reaches
\[
\liminf (e_{BB}+2s_C)/D\ge0.4702.
\]
It explicitly says that further scalar iteration is insufficient without a new
upper/global incompatibility. Accordingly the launch prompt makes constant chasing
subordinate to a precise closing implication. None of these reports is promoted by
its commit message or numerical improvement.

### Rattler absorption changes the representative

The [RA report](target_c_rattler_first_contact_absorption_2026-09-09.md) constructs
another same-cardinality, same-diameter triangle-free global representative with no
isolated contact vertices while fixing the original positive core. It creates
contacts; those contacts need not be KKT-positive. Reusing `C=C_*`, `H=H_*`, or ZF
on that new representative without transport is invalid. RA is a possible
representative-transfer bridge, not a proof that the lexicographic core contains
all source points.

## 4. Prompt hazards found in the current repository

1. The [existing GPT-6 whole-problem launch](../prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md)
   points at `[local filesystem path omitted]`, whereas this checkout is
   `[local filesystem path omitted]`; it also still asks for both C-I and C-II and carries old
   blanket PSD warnings. Its authority rules mitigate, but do not remove, that
   distraction. The new sol prompt uses the actual path and restored C-I state.
2. Target A's route map is ahead of its active prompt and high-level summaries.
   The new launch explicitly directs the model to Sections 168–174.
3. Target C's controlling update is correct, but its older body and active prompt
   retain extensive superseded C-I text. The new launch states the correction once
   and directs proof effort to C-II.
4. Later reports contain stronger candidate reductions than the promoted maps.
   Ignoring them wastes opportunities; accepting them wholesale skips the required
   dependency audit. The prompt names two bounded entry points, FS and Z/ZR/ZF.
5. A long list of lower bounds can appear closer to contradiction than it is.
   The prompt requires the opposing bound, strict competitor, or exact branch
   exclusion before treating an improvement as a closing step.
6. Small support, pure topology, near-minimal boundary, maximal stress, and alternate
   representatives are different hypotheses. They cannot be combined because their
   conclusions are individually attractive.

These findings are recorded, not silently repaired in canonical mathematics.

## 5. Model-specific prompting choices

Official [GPT-5.6 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6)
recommends removing repetition, specifying autonomy boundaries, and making required
answer detail explicit. The new launch applies those principles by keeping the
assessment separate, stating each operating rule once, allowing local research
actions, and requiring complete mathematical proofs despite a concise chat summary.

Official [reasoning-model guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
favors direct objectives and clear success criteria over “think step by step”
incantations. The prompt therefore asks for exact mathematical artifacts and a
separate proof audit, not disclosure of private exploratory reasoning. “Aggressive”
means persistence toward settlement and rejection of proxy stopping points; it does
not mean requiring a claimed solution regardless of evidence.

[GPT-5.6 Sol documentation](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
confirms `xhigh` support. The launch preserves the user's requested model and effort;
it does not substitute another model, enable pro mode, or impose a time/token budget.
The runner must select those settings. No Sol research run was launched in this task,
and no prompt can guarantee that an open mathematical problem will be settled.

The intended research order is: current promoted C-II state; audit the short FS
bridge; attack full-source capacity or a strict competitor; use audited post-ZF
structure if it creates a concrete stronger implication; switch routes if warranted.
This is a prioritized starting point, not an instruction to force a favorite proof.

## 6. Verification and repository changes

Read `research/README.md` before using the checks. At this state:

```text
python3 -m unittest discover -s research -p 'test_*.py'
  65 tests, OK
python3 research/thrackle_interval_regression.py
  240 exact consistently normalized pentagon/interval checks, PASS
python3 research/near_diameter_path_audit.py
  27,252 exact chord/interval checks, PASS
  stated local-star, lens, and straight-chain checks also PASS
```

These verify their stated finite models and calculations. They do not independently
prove every dependency, global packing optimality, or Level I. No exploratory
floating-point packing/stress search was needed.

Documentation verification includes `git diff --check`, a relative-file-link scan
outside the archive (not an anchor audit), and existence checks for paths in the new
prompt. No unresolved conflict markers were found in the inspected documentation
and research files. Two apparent links in an existing report were arithmetic inside
a fenced code block, not broken Markdown links.

Changes for this task are confined to this unpromoted review, the new sol launch
prompt, and its entry in `docs/prompts/README.md`. No theorem modules, route maps,
existing research results, model configuration, or external services are changed.

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.
Base: main at 3f37ef0, 2026-09-10.

Promoted: C53 selected-source PSD, C63 finite integration, C-I closure,
contact/diameter lexicographic C=C_*, H=H_*, common-kernel local form.
Retain isolated source points; do not impose simultaneous hull saturation.

A: route map reaches Section 174; exact stress-sector population gap remains.
B: exact topology-correct shell bound; coherent-case coverage remains.
C: complete full-source C-II exclusion remains.

Recent candidates, not promoted:
FS full-source containing radius -> P_*=2D-O(sqrt D), small diameter-star angles;
Z/ZR/ZF -> maximal core stress rank and mixed-bar row bound;
ZS -> linear boundary surplus, forbidding the older near-minimal normal form;
exact post-ZF ledgers, mixed redundant rigidity, and pocket-surplus floor 0.4702.

Do not infer matching weight, small response trace, or operator convergence
from FS. Do not infer inequality-tensegrity rigidity from equality-bar rigidity.
Do not infer force visibility from RA's no-isolate representative.

Use the new SOL_XHIGH_FULL_SOLUTION_PROMPT as a whole-problem launch.
Runner: GPT-5.6 Sol, xhigh, repository [local filesystem path omitted]
No mathematical claim was promoted and no solution attempt was launched by this review.
```
