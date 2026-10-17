> Generated reading edition · [exact source](../../../docs/reports/repository_theorem_state_cleanup_2026-09-11.md) · source SHA-256 `786a7e7e5522809fb0ad628f8ace3644f4a1549b3e736f17ba6d9367983d9838`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f1dca98d4544ffbfddb352eb805e37a7746468d4", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/repository_theorem_state_cleanup_2026-09-11.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "83c88c6696a4ec61d790614469afe8462f7a65808fbeaf94895a900474831514"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Repository theorem-state cleanup — 2026-09-11

**Classification:** repository-state migration, provenance audit, and limited theorem
promotion  
**Baseline:** `34085ac264eb5241985de7b453bf7d612a25fa4d`  
**Working branch:** `cleanup/authoritative-state-2026-09-11`  
**LEVEL I STATUS:** STILL OPEN

## Purpose

The September 11 branch consolidation repaired source-control fragmentation but left a
large epistemic problem: hundreds of reports with different lifecycle states now coexist
on `main`. Several operational documents also lagged the actual route maps. This cleanup
makes the current theorem state explicit and prevents ordinary search/retrieval from
silently defining authority.

This is not a claim that every historical report has been re-proved. It is a
reconstruction of the active theorem state, a classification of known late work, and a
structural change to how future promotion works.

## Input repository state

The immediately preceding consolidation audit records:

- 117 remote topic branches in addition to `main` before cleanup;
- 99 topic branches outside `main` ancestry;
- 636 outside-main commits;
- 53 open pull requests;
- 459 substantive branch-only paths retained in the consolidated tree;
- no theorem promotion caused merely by that consolidation.

The consolidation also retained explicit rejected/corrected material, including the
cyclic path-inference audit.

## Stale active-state documents found

### Target A drift

The authoritative Target A route map had advanced through Section 174, but several
navigation/prompt documents still described Section 167 and the source-labeled planar
Menger lemma as the live endpoint:

- `docs/README.md`;
- `docs/KNOWLEDGE_MAP.md`;
- `docs/prompts/README.md`;
- `docs/reports/README.md`;
- the old active Target A continuation prompt.

The whole-problem prompt knew that the route map was newer, but worked around the drift
rather than eliminating it.

### Target C drift

The Target C map correctly said C-I was closed, but operational material still contained
historical C-I missions. The old route map also mixed a long promoted-addenda catalog,
withdrawn regressions, partial promotions, and current-state prose in one large file.
Co-located numbered modules made filename order look more authoritative than it was.

## New authority architecture

The cleanup introduces:

- `docs/STATE.md` — first human authority/lifecycle lock;
- `docs/state/theorem-state.yaml` — machine-readable mirror;
- `docs/state/README.md` — status and retrieval rules;
- `docs/targets/target-c/CURRENT.md` — compact C-II live frontier;
- a shortened Target C route map;
- current Target A and Target C continuation prompts;
- compatibility redirects for formerly active stale prompt paths;
- a mechanical consistency checker and GitHub Actions workflow.

The default is now explicit: an unpromoted report is noncanonical even when it is on
`main` or came from a merged PR.

## Historical preservation decision

Hundreds of dated reports were **not** physically moved. Moving them would break
provenance links and create a large path migration without improving theorem truth.
Instead, lifecycle status is externalized into the state manifest.

The complete pre-cleanup Target C route map is preserved verbatim as
`docs/targets/target-c/HISTORY-pre-cleanup-2026-09-11.md`. Its old promoted-addenda
catalog remains valid subject to overrides in the new state lock.

The exact original blobs of the old Target A and Target C prompts are preserved under
`docs/prompts/historical/`. Their former active paths become explicit compatibility
pointers to the new prompts.

## Reconstructed target state

### Target A

Canonical route remains open and is current through Section 174. The global Schur
rank/nullity endpoint is unchanged. The live locked-response subbranch is the
stress-sector population inequality; the zero-slack/descent branch survives.

The Section-167 source-labeled Menger endpoint is classified `superseded` as a current
frontier, not rejected as a historical theorem target.

### Target B

Canonical route and joint outer-shell stability endpoint remain unchanged. Later
corrected grid/penetration/phase-interpolation work is classified audited-working unless
separately promoted.

### Target C

C-I remains closed by the September 9 orientation/dependency restoration. C-II remains
open. The promoted zero/additive-transfer exclusion is retained.

Two later results are promoted by this cleanup after dependency/status review.

#### Woodall diameter topology

The report `target_c_woodall_diameter_topology_2026-09-10.md` is promoted. The imported
straight-line-thrackle classification was rechecked against Collins–Roberts, Theorem
2.3, which states the Woodall classification in the required form. Combined with the
canonical diameter-graph edge bound, the report yields:

- `d_H=0`: one connected odd-unicyclic diameter graph with every off-cycle vertex
  pendant on the cycle;
- `d_H>0`: a disjoint union of caterpillars with exactly `d_H` components.

#### Universal common-contact-bridge exclusion

`target_c_common_bridge_transfer_exclusion_2026-09-10.md` and its separate
`target_c_common_bridge_transfer_audit_2026-09-10.md` are promoted. The audit avoids the
potential circular dependency on later unpromoted C56 equality machinery by deriving
the needed transfer sign directly from promoted C53 identities. Hence the common
selected-diameter route intersection is exactly one positive-contact bridge block.

## Late work deliberately not promoted

### PR #188 renormalized-surplus chain

The strongest surviving report states

`liminf mu_D >= z_* > 0.9604`,

with `10 asin(z_*) - 4 pi = z_*/3`. The final audit explicitly retains FD.1–FD.5 and
this numeric bound while withdrawing the claim that its Eppstein near-equality remainder
forces near-quadrangulation.

Because the result is the end of a long mostly self-audited dependency chain, the cleanup
classifies it `audited-working`. Future promotion should audit that chain as one theorem
rather than promoting every intermediate scalar constant.

### PR #191 cyclic all-surplus extension

This latest cyclic report extends the earlier `s_Z=0` atomic-transport argument to
arbitrary `s_Z` in the Woodall cyclic branch and reports the ordinary-surplus floor
`0.99554058458...` with a qualitative endpoint gap. It is classified audited-working
pending an independent dependency audit.

### Cyclic P1/S1 and RSR/DD families

These remain visible as audited-working/repaired report families. The RSR family must
not import equality uniqueness from the 1985 source; later repaired arguments that avoid
that premise are not discarded.

## Binding rejected claims recorded globally

The state lock now records the following so they cannot silently re-enter current
prompts:

- consecutive incident diameter states imply Euler trail/path — false;
- force-bulk FB4 localization — rejected;
- incompatible-orientation pentagon regression against C53 — rejected;
- RSR equality uniqueness attributed to the cited source — unavailable/rejected as a
  dependency;
- five-arc Eppstein near-quadrangulation interpretation — rejected.

Each rejection is narrower than deleting every theorem in its surrounding report chain.

## Future promotion invariant

Any frontier-changing promotion must update in the same change:

1. `docs/STATE.md`;
2. `docs/state/theorem-state.yaml`;
3. the affected route map/current-frontier file;
4. the active prompt when the next obligation changes.

`tools/check_theorem_state.py` enforces the mechanical portion of this invariant and
checks key stale-state regressions plus links in the authoritative document layer.

## Files rewritten/added by this cleanup

Core state/navigation:

- `README.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `docs/STATE.md`
- `docs/state/README.md`
- `docs/state/theorem-state.yaml`
- `docs/README.md`
- `docs/KNOWLEDGE_MAP.md`
- `docs/targets/target-c/README.md`
- `docs/targets/target-c/CURRENT.md`
- `docs/targets/target-c/HISTORY-pre-cleanup-2026-09-11.md`

Prompt layer:

- `docs/prompts/README.md`
- `docs/prompts/erdos_problem_99_TARGET_A_CURRENT_CONTINUATION_PROMPT.md`
- `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
- `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
- compatibility redirects at the former Target A/C active prompt paths
- original prompt blobs preserved under `docs/prompts/historical/`

Workflow:

- `CONTRIBUTING.md`
- `docs/RESEARCH_WORKFLOW.md`
- `docs/reports/README.md`
- `docs/reports/REPORT_TEMPLATE.md`
- `tools/check_theorem_state.py`
- `.github/workflows/theorem-state.yml`

## Theorem effect

The cleanup itself does not settle Level I. Its mathematical promotions are limited to
the Woodall diameter-topology theorem and the independently audited common-contact-bridge
exclusion. Everything else is status reconstruction, correction propagation, or
repository-state engineering.
