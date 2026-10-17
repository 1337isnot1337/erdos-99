> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-owner-release-loaded-anchor.md) · source SHA-256 `e0cad527638492744ad077082882e307b7b29b1a900d3dd630bc6c7cf7ad44d0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C owner release, loaded anchors, and floor closure

**Status:** historical research package from frozen source PR #952. All five reports are unreviewed candidates; none changes theorem-state. C-II and Level I remain open.

**Source:** `e-99` PR #952, head `3536c0b6f6c2a929d9c96fffbdcfc480735fea3`, tree `a6503b1817dbd885f9378ca42677d811fe363c84`; merge base `d999528cfaafd811a4a19bcfacd00f217c2fc375`. The five reports, six fixtures, and four verifier scripts were already retained in this destination. Their complete file-by-file comparison is in the [migration ledger](../../../../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl) and [scientific reconciliation](../../../../docs/research/migration/2026-10-16/scientific-reconciliation.md).

## Route at a glance

This package studies actual finite motions built from disjoint moving owners of a canonical contact core. Its contribution is an exact endpoint criterion once a suitable owner family is supplied. It does **not** extract such a family from every canonical minimizer.

```text
extract actual owner groups and assign every isolate
  -> account for every source lower and upper pair
  -> solve floor and implication constraints exactly
  -> if a core owner survives, construct a full-source finite contradiction
```

Two candidate endpoint mechanisms are retained. Contact loss contradicts contact minimality when the diameter remains at most `D`. If contacts are preserved, the report uses the canonical KKT stress and an actual diameter witness to obtain lexicographic gain. Equality at a contact-opening floor needs separate treatment: a weak upper equality can permit it while a strict inactive upper pair can forbid it.

## Results and exact scope

### Moving components have actual diameter ports; nonzero selections have stress gain

[Component anchoring and source-realized sink](../../reports/target_c_owner_component_anchoring_and_source_realized_sink_2026-10-10.md) proves that, under exact preservation of every contact by a nonzero translation of a proper core subset, every contact component on either side has a crossing actual-diameter edge with positive multiplier. Under the report's canonical relative-interior KKT hypotheses and pairwise acute owner directions, its identity `SG.1` makes the weighted old-diameter gain strictly positive for every nonzero binary owner selection that preserves contacts. It does not establish upper feasibility or a nonzero lower-feasible selection.

The same report gives an upper-safe mixed-component refinement after deleting at most `2 d_H` parent owners, under its stated parent assumptions. Its explicit connected nonglobal source realizes upper safety and strict diameter gain but has a zero-only reduced lower formula. This refutes the reduced implication from those listed hypotheses to Horn feasibility; it is not a canonical counterexample and does not refute an endpoint theorem with the omitted canonical assumptions.

### Unequal-height closure and isolate transport

[Finite parallel release and floor closure](../../reports/target_c_parallel_release_floor_closure_and_isolate_transport_2026-10-10.md) proves a finite shortest-path floor-closure theorem for a supplied family of disjoint core groups with no contacts between moving groups. Every source pair contributes its actual lower/upper cost; isolates receive independent variables. In the report's strict-floor class, a surviving active contact group yields a full-source contact-loss endpoint. It also gives unequal-height repairs and an adaptive isolate-transport construction for exact finite regressions. The common-height obstruction does not rule out unequal heights or isolate motion.

Its exact next obligation is to extract, in every sufficiently large canonical survivor, a source family for which the full-source cost graph cannot collapse every contact-bearing owner to zero. Abstract reachability without geometric bounds is insufficient.

### Inclusive floors and locked-contact cases

[Inclusive floor closure and locked contact releases](../../reports/target_c_inclusive_floor_closure_and_locked_contact_release_2026-10-10.md) extends the strict-floor result to equal-floor endpoints. Its lexicographic shortest-path and finite zero-closure algorithm returns the unique maximal feasible active support while preserving strict pair inequalities. The contact-loss version detects every contact-loss endpoint in its class. In the locked-contact branch, a surviving proper core group gives a canonical lexicographic contradiction even when its active height equals its positive floor. The necessary collapse certificate distinguishes a path of cost strictly below the floor from an equal-cost path carrying a strict witness; an all-weak equal-cost path alone cannot force zero.

The missing source theorem is an actual canonical owner family, with an isolate assignment and at least one fixed core label, whose inclusive closure retains a core group (or whose weak-upper closure opens a contact). The report does not derive that family from terminal owner-capacity or train-depletion bounds.

### Loaded-anchor upper box and the ownership gap

[A parallel upper box from local loaded-anchor coverage](../../reports/target_c_loaded_anchor_parallel_upper_box_2026-10-10.md) supplies a common-ray amplitude box after the stated angular, scale, and owner-local coverage hypotheses. Every upper-relevant label—including assigned isolates—must lie within `R` of a loaded actual-diameter endpoint in the **same** owner, with an actual crossing diameter. Under the stated `R+rho <= D/10` and angular-window assumptions, its normal-window/diameter-incidence deletion count is explicit; remaining inactive upper pairs stay strict throughout the box. In the full-core near-disk branch it proves the explicit proximity bound `|p-z| <= D(2 eta + sqrt(2 eta)) + rho` for every source label `p` with a partner at distance at least `D-rho`, when the loaded convex hull contains the stated `(1/2-eta)D` inner disk. That estimate does not solve ownership: the nearby loaded endpoint may belong to a different owner, and its diameter partners may remain in the same owner.

In a canonical Type-II near-disk sequence, the separate LDE theorem assumes a
supplied subfamily-stable O–O family with Audit.106 contact, unary, small-cloud,
isolate-assignment, and outer-witness hypotheses plus AS coverage
`R=o(D)`, `w=o(1)`, `rho=o(D)`. It proves
`r <= 2 floor(F_D(Phi)) + 147(x_B+m_B)`, with no `2 d_H` term; if
`x_B+m_B=o(D)`, this excludes a linear-sized family. It neither supplies that
family nor proves low boundary defect in every survivor.

The remaining task is to extract enough owner-respecting ports, then prove the lower-only inclusive closure retains a core owner. The far-label regression rules out selecting one convenient loaded point while ignoring other upper-relevant labels.

### Source-history corrections

The source history refines the active obligations. Commit `a7a6dfda` replaces
the earlier CT-only endpoint criterion with UCC, which places actual upper
pairs into the implication system; `c998f842` adds the stress-imbalance port
bound and its canonical extraction obligation. The final registry follows
UCC's lower-and-upper no-unary-sink question. Commit `8053f34b` adds the
native-direction box and LDE capacity bound; the final finite replay covers
744 pair states, superseding the earlier 324-state note. Commit `a223a304`
adds the mixed-component refinement to the component-anchoring report, and
`2dea92b9` adds the signed-clipping correction to unequal-height transport.
These final refinements are retained at the frozen PR head; the report ledger
does not restore superseded CT-only or earlier finite-scope wording.

### Full-source common-release implication systems

[Upper-safe amplification and common contact release](../../reports/target_c_outer_owner_amplification_and_common_release_2026-10-10.md) records several distinct candidates. For fixed `M>1` in its stated scale range, amplitude box `AB` gives full-source upper safety after discarding at most `2 d_H + 4 floor(F_D(theta_M))` supplied owners; amplitudes above one open contacts, while the all-binary case depends on the separate strict-stress-gain candidate. The common-translation criterion `CT`, after its separate bound `2 d_H + 4 floor(F_D(theta_b))` on singleton-unsafe owners, turns the stated exact lower constraints into implications and forced-zero unary clauses and identifies when a nonzero sink component yields contact loss. The stress-imbalance estimate `IM` forces an actual loaded port with `0 < -n_i·v_i <= delta_i/(2 sqrt(delta_i^2/4 + (1-delta_i^2/4) sigma_i^2))` for each owner in its restricted acute-window class. The integrated criterion `UCC` adds all actual upper-pair constraints to the implication graph and constructs the unique maximal feasible assignment; in a canonical source, a nonzero assignment would contradict contact minimality.

The missing theorem is source extraction plus unary avoidance: an actual stable owner family satisfying the report's displacement, isolate-dispatch, and full-source hypotheses whose integrated lower/upper graph has a sink strongly connected component without a unary blocker. The report's source-specific regression and Horn counterexamples remain nonglobal and restricted to the stated reduced hypotheses. Normal atomlessness or a source-free implication graph alone does not establish the needed family.

## Computation and evidence

The source README's exact commands and finite scopes are retained here. The scripts, six JSONL outputs, and their source/destination hashes are individually recorded in the migration ledger. These checks cover explicit fixtures only; the analytic implications and canonical-source extraction remain unverified by computation.

- [Inclusive-floor verifier](../../../../research/verify_target_c_inclusive_floor_release_2026_10_10.py):
  `python3 research/verify_target_c_inclusive_floor_release_2026_10_10.py --graphs 80 --seed 1001001 --diameters 20 30 50` checks inclusive contact floors, lexicographic shortest paths, strict/weak equal-floor paths, and recursive zero cascades. Independent exact elimination enumerates 620 supports. Six triangle-free nonglobal fixtures give 180 full pair-state checks, including a locked move that removes an old diameter and a companion that replaces it with an inactive pair. All labels and newly active upper constraints are checked.
- [Loaded-anchor verifier](../../../../research/verify_target_c_loaded_anchor_upper_box_2026_10_10.py):
  `python3 research/verify_target_c_loaded_anchor_upper_box_2026_10_10.py --diameters 300 500 1000` checks 744 pair-state instances in nine nonglobal fixtures. It includes a localized owner with a retained moving isolate and a far near-diameter-label regression, plus three two-owner native-direction boxes. Those checks cover the exact owner fixtures and original upper constraints, not canonical loaded-port coverage, normal-window counts, lower-closure survival, or globality. Under Audit.106's exact outer-witness hypotheses, the analytic report further obtains `r <= 2 floor(F_D(Phi)) + 147(x_B+m_B)` without the older `2 d_H` exception loss; low boundary defect and owner-family extraction remain additional hypotheses.
- [Owner-sink verifier](../../../../research/verify_target_c_source_realized_owner_sink_2026_10_10.py):
  `python3 research/verify_target_c_source_realized_owner_sink_2026_10_10.py --heights 30 31 100 --symbolic-limit --amplitude-repair --common-implication-system` certifies all lower/upper pairs for the owner-state, amplitude/common-system, and refined-endpoint fixtures, using exact or rational-interval arithmetic for eleven limiting slacks. With both optional modes enabled, `--amplitude-repair --common-implication-system`, the seven-state amplitude fixtures cover 194,684 pair instances and certify repairs removing exactly 12 or 24 contacts while keeping every noncontact strict and reducing diameter. The nine-state common-system fixtures cover 250,308 pair instances; the two singleton states give `A=>B` and `B=>A` with no unary or upper blocker, so the maximal model moves both owners. The checked sources are nonglobal and lack positive full-contact KKT equilibrium; none of these runs verifies canonical family extraction.
- [Unequal-height verifier](../../../../research/verify_target_c_unequal_height_release_2026_10_10.py):
  `python3 research/verify_target_c_unequal_height_release_2026_10_10.py --heights 30 31 100 --symbolic-limit` checks 225,680 full pair-state instances, thirteen limiting slacks, unequal core heights, and independent isolate transport. The finite endpoints remove 24 contacts, keep noncontacts strict, and have exact smaller-diameter certificates. It uses conservative rational enclosures for algebraic graph costs: a successful endpoint is certified, while failure of this compilation is not an exact algebraic infeasibility certificate.

The six retained outputs are [common release](../../../../research/certificates/target_c_common_release_implication_2026_10_10.jsonl), [inclusive floor](../../../../research/certificates/target_c_inclusive_floor_release_2026_10_10.jsonl), [loaded-anchor box](../../../../research/certificates/target_c_loaded_anchor_upper_box_2026_10_10.jsonl), [owner-amplitude release](../../../../research/certificates/target_c_owner_amplitude_release_2026_10_10.jsonl), [source-realized sink](../../../../research/certificates/target_c_source_realized_owner_sink_2026_10_10.jsonl), and [unequal-height release](../../../../research/certificates/target_c_unequal_height_release_2026_10_10.jsonl). Exact finite outputs do not prove universal extraction, canonical optimality, or the analytic arguments.

All six full verifier invocations (four programs, with owner-sink, amplitude,
and common-implication modes run separately) exited zero. They reproduced all
six corresponding checked-in JSONL fixtures byte-for-byte.

## Research handoff

Continue by proving one of the following in each still-open canonical branch:

1. Extract a linear family of actual O–O owners with owner-respecting loaded anchors for every upper-relevant point and isolate, then prove a nonzero assignment survives the inclusive full-source closure; or
2. Prove a source-specific bound that pays for owners whose upper-relevant points remain far from all loaded ports in that owner; or
3. Produce a canonical obstruction to these extraction statements and identify a different full-source endpoint mechanism.

A successful endpoint must preserve cardinality, check every original lower and upper pair, include all isolates, retain the actual source diameter bound, and give either contact loss at diameter `D` or strict lexicographic diameter gain. None of the reports supplies that endpoint for every canonical minimizer. No Target A/B, C-II, Level I, or theorem-state status changes follow from this package.
