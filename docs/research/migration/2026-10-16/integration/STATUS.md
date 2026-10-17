# Migration completion status

Captured-byte preservation is complete. Source deprecation remains deferred
because two historical working-copy states were not inventoried at migration
capture. Both repositories remain private. Level I/A/B/C-II remain open;
C-I remains closed within its recorded scope.

## Preserved content

The [source-main ledger](SOURCE_MAIN_PRESERVATION.md) accounts for all 4,717
pinned source paths: 4,654 exact source identities and 63 explicit external
reference exclusions. It preserves 1,282 recovered originals separately from
corrected destination documents. The active `tools/build_artifact_index.py`
has changed; the source identity survives under
`baseline-originals/tools/build_artifact_index.py.source`, as explicitly
recorded by the union checker.

All 813 frozen report bindings and all 1,643 captured branch-artifact rows
remain obligations of the executable checkers. The 249 raw branch archives,
two exactly reconstructed dirty indexes, and twelve restored original-path
dependencies remain preserved. These are bounded captured inventories, not
an assertion that every historical Git object or working copy was transplanted.

The [local recovery follow-up](../ref-reconciliation/LOCAL_RECOVERY.md)
recovers all five formerly missing dirty-file versions from the original
worktrees. Every recovered version matches its captured SHA-256 and byte
length. All 30 captured dirty-file identities are now present. Exact historical
bytes remain inert `.source` archives and do not replace active proofs or
verifiers. The earlier missing-identity ledger and search receipts are retained
as historical evidence, superseded for current recovery status by the
[exact-recovery ledger](../ref-reconciliation/recovered-dirty-identities.jsonl).

## Historical working-copy limits

The two markers `/tmp/e99-diameter-stress-gap-20261002` and
`/tmp/e99-source-cycle-20261001` retain **unknown historical working-copy state
at migration capture**. Earlier local backups record clean tracked/untracked
snapshots and preserve ignored bytecode. Nine current non-bytecode residual
files for the first marker exactly match its recorded commit. The second path
is absent. These observations do not establish an uncaptured later inventory,
prove there were no later changes, or identify a number of lost files.
The [follow-up evidence](../ref-reconciliation/historical-worktree-followup.json)
records the exact scope. An explicit owner disposition is needed before source
deprecation; the source repository and historical working copies remain intact.

## Verification and integration contract

The six original engineering transformations retain their exact baseline
archives. Two release-status documents additionally prepend current status
while preserving their entire historical text and exact original copies.
The policy permits only those two named document additions and rejects any
historical-text or mode change. Security scanning and rights checks apply.

The earlier outage, headless object reviews, and diagnostic test results remain
historical evidence. A working local CPython 3.14.7 environment and a local
namespace-capable verification route are now available. The
[complete migration verification procedure](../../../../launch/MIGRATION_VERIFICATION.md)
must pass on the exact clean integration candidate and resulting destination
`main`. No denied, skipped, zero-step hosted, or earlier-SHA result counts as a
pass. Repository checks, certificate replay, credential and rights checks, and
mathematical authority checks remain enforced.

Current executable results are recorded in the detached completion evidence
and the release-engineering handoff on
[integration PR #75](https://github.com/1337isnot1337/erdos-99/pull/75), bound to
their tested commit and tree. This page does not embed a self-referential
verification receipt or grant publication permission. No mathematical claim
is promoted. Ordinary Git attribution, including `codex@openai.com`, is retained.
