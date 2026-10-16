# Scientific reconciliation: source-main Target C batch 1

**Status: INCOMPLETE.** This report reconciles the first preserved source-main
batch with the destination's mathematical authority. It is not a proof audit of
each imported report and it does not close Target C or any part of Level I.

## Frozen comparison

- Source main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`, tree
  `e061f039eac44c286a00eacdcaa9a4cbbb877891`; source theorem-state
  `2026-10-10.audit.234`.
- Destination base: `60c2576b4893a7e9001d2c8bfbe5cfb64c1c969f`, tree
  `f4d73c1080b3b4a1b7757f5fd96109b6cd4b5c76`; theorem-state
  `2026-10-15.publication.2`.
- The destination state remains authoritative. It has 370 canonical C claims,
  4 audited-working claims, 62 regressions and 14 rejected or overridden claims.
  Level I, A, B and C-II remain open; C-I remains closed only in its stated
  scope.

The source theorem-state snapshot counted 371 canonical C entries, 3
audited-working entries, 62 regressions and 14 rejected or overridden entries.
The one-claim difference is reconciled by the destination's inverse-phase
correction below: the source still treats that claim as canonical, while the
destination records it as audited-working. Do not combine these theorem-entry
counts with artifact-index row counts; they count different objects.

The frozen source index contains 1,287 Target C artifact records: 193 marked
`canonical`, 3 `audited-working`, 28 `regression`, 2 `superseded`, 37 `mixed`,
and 1,024 `unreviewed`. Its separate `canonical` flag is true on 230 records,
and 263 records name claims. These are source provenance labels, not
destination decisions. The complete row-by-row record, including each claim ID,
dependency, source blob, lifecycle and disposition, is in
[`ledger/source-main-artifacts.jsonl`](ledger/source-main-artifacts.jsonl).

## Reconciliation of this batch

- **911** source Target C artifacts had no destination file at their original
  path. This batch integrates **85** of them as noncanonical research: **83**
  source-main audits and two linked reports needed to restore the low-response
  audit link and the cyclic fan-flip audit/report evidence chain
  (`target_c_fan_flip_isolate_escape_2026-10-02.md` and
  `target_c_low_response_mu_floor_2026-09-12.md`). The other **826** missing
  reports are queued for later focused batches.
- **338** source artifacts are exact duplicates of destination content, verified
  by SHA-256. This includes 337 exact same-path copies and one identical artifact
  already represented at another path.
- **38** source versions differ from a destination file at the same path. The
  destination bytes remain in place; each source version is retained under
  `docs/archive/source-e99-main-42f0296d/` with a historical warning and exact
  source/public hashes.
- The full direct Markdown dependency closure has **100** records: 31 missing
  source paths, 11 changed source versions, and 58 exact destination copies.
  This batch resolves 4 missing dependency records linked by its imported audit
  closure, and preserves the 11 changed versions (which can overlap the 38
  source-artifact conflict snapshots); the other 27 missing report dependencies
  remain queued. It verifies **84** of the full **384** evidence edges; the other
  300 remain recorded and queued. All 18
  report link corrections are recorded but await their parent report batches.
  No PDF collection or extracted third-party text was copied. No dependency in
  the full closure is marked rights-blocked.

This closure follows Markdown links. Code or fixture paths mentioned only as
inline text are not certified present by this batch's link scan. The full source
research tree is part of the queued next import, where those references will be
checked against the copied scripts and data.

The imported records do not become canonical merely because the source index
calls them canonical or because a source report calls itself an independent
audit. Destination theorem-state, proof graph, current Target C document and
publication inclusion were not replaced. The generated artifact index now
records the added documents; theorem-state counts and claim edges remain
unchanged. Source artifact metadata is retained in the migration ledger so that
later reviewers can assess useful proofs, corrections, computations and failed
routes without confusing historical status with acceptance.

## Correction that must survive the migration

The source's same-path version of
`target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md`
is source-labeled canonical. It is archived with an explicit warning because
the destination's later reconciliation withdraws the global `K'/D`-Lipschitz
chart and the unsupported `q=O(D^(4/5))` inference. The destination keeps
`C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION` audited-working under the corrected
sequence-only argument and the original common-frame and face-tail hypotheses.
The archived source text is evidence of the earlier claim, not a usable premise.
The current correction and its scope are stated in the
[publication reconciliation](../../../publication/scientific-reconciliation.md)
and [Target C current state](../../../targets/target-c/CURRENT.md).

## Remaining reconciliation

The source-main `research/` subtree contains 2,707 Target C files: 152 exact
destination duplicates, 19 source dependencies referenced from reports, and
2,536 remaining research files. This batch includes the two research files
linked from its audits; the other 17 linked files await report batches. The
route tree has 157 Target C documents; their file-by-file queued, duplicate and
dependency states appear in
[`ledger/source-main-files.jsonl`](ledger/source-main-files.jsonl). The pinned
source inventory also contains 21 open PR heads; the proposals and other
historical PR work have not been reconciled into this batch. In particular,
PRs #947, #948, #950, #951, #952, and #955–#960 require separate content-level
comparison with the current destination before retaining any additions.

Accordingly, this batch establishes source identity and preserves substantial
research content; it does not establish that every source mathematical claim is
correct, that every older proof avoids the withdrawn inference, or that the
research-corpus migration is complete. The authoritative promotion and release
gates remain unchanged.
