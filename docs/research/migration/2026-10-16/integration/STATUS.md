# Migration repair status

Status: draft repair candidate. Not release verified. Source deprecation is blocked.

The original [integration receipt](README.md) records the earlier candidate.
This page records the subsequent recovery and its current limits. Destination
theorem state remains authoritative; Level I remains open.

## Preserved content

The [source coverage records](SOURCE_MAIN_PRESERVATION.md) account for all
4,717 pinned source-main paths: 4,654 exact identities and 63 reference-only
dispositions. The candidate adds 1,282 exact original source files beneath
`integration/source-main/`. A source-compatible replay assembled before the
environment outage contained 4,653 first-party files.

All 813 frozen reports retain their captured bytes, modes, and Git blob
identities. All 1,643 recorded branch-artifact rows have exact retained content.
The [branch and dirty-file audit](../ref-reconciliation/README.md) adds 249 raw
branch blobs and reconstructs two captured dirty artifact indexes exactly.

The [reference recovery](reference-recovery.md) restores 12 original-path
dependencies. The [historical reference map](historical-reference-map.md) retains
version and scope limits. An archived counterpart does not prove that an
uncaptured historical version was recovered.

## Engineering changes

The [integrity policy](integrity-policy.json) pins 1,505 historical Markdown and
Python payloads and 55 imported unreviewed report banners to the original
candidate `f282d53169df4d507117893bfdcc99f663855923`.

Only six existing engineering files change. Each has an exact old copy under
`baseline-originals/`. Existing artifact-index rows and source permission
fields remain unchanged. Added index records remain unreviewed and
noncanonical. Security scanning still covers historical payloads.

The frozen ledger checker, reference and branch audits, release wrapper, bounded
scanner-finding review, and regression controls are included. No canonical
claim, theorem-state file, or accepted proof is promoted or rewritten.

## Verification and outage

Before the execution environment disconnected, diagnostic runs passed 94
registered certificates, 92 migration tests normally and with Python
optimization, 12 publication-policy controls, 33 rights-lineage controls, and
the named verifier/discovery replays. Public integrity reported zero errors.
Four namespace tests could not execute in that sandbox because namespace
operations were denied.

Those outcomes are earlier diagnostic evidence, not a passing receipt for this
reconstructed candidate. The environment disconnected during upload and is
unavailable. Work was recovered from GitHub objects, pinned source inventories,
and retained writer histories. Reconstructed code has not been executed after
that outage. The recovery checkpoints and their receipts state this limit.

The final headless checks compare committed Git object identities and ledger
structure. They do not replace Python regression tests, namespace isolation
tests, the complete certificate/corpus replay, scanner execution, or Gate 2.
Use the [verification procedure](../../../../launch/MIGRATION_VERIFICATION.md)
on the final clean candidate and again on any resulting merge commit.

## Unresolved evidence

Five substantive dirty-file versions remain unavailable. Their paths, sizes,
and captured SHA-256 values are listed in the
[missing-identity record](../ref-reconciliation/known-missing-dirty-identities.jsonl).
Hashes cannot reconstruct their bytes. Twenty-five of the 30 known captured
dirty-file identities are preserved; two other historical worktree markers
have no captured file inventory and retain unknown working-copy state.

The source remains intact. The integration pull request stays draft and
unmerged until the missing evidence has a justified disposition and final
verification succeeds. No source-deprecation or release approval is claimed.
