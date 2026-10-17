# Migration Agent 2: completed shard evidence

Observation date: 2026-10-16. This shard was built on a clean worktree from destination main `c6e0394b3152d21075328bf4f26e6c070229bf13`, using pinned source main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` and the frozen 813-report Target C disposition ledger.

All preserved source bytes are under this dated migration namespace. They are archival and noncanonical. The active theorem state, artifact index, rights ledger, candidate registries, and publication manifests were not edited. Existing destination reports and mathematical corrections were left intact. The global problem and Target C-II remain open.

## Assignment and workload

`corpus-assignment.jsonl` contains the deterministic assignment for all 4,717 pinned source-main files, including exact matches, frozen-report dispositions, outstanding obligations, and exclusions. `corpus-assignment-summary.json` records its SHA-256 and work totals.

- Same-path exact matches: 1,452; exact-content matches elsewhere: 13.
- Frozen Target C dispositions: 813, of which 610 overlap same-path exact matches; 203 remain frozen-report-only dispositions.
- Outstanding source-main files: 3,049 in 2,687 units.
- Starting totals: `[90, 75, 60]`; final totals: `[4299, 4299, 4299]`; spread: 0 (0%).
- Agent 2: 1,015 files, 896 units, score 4,224.

## Source-main corpus

`corpus/corpus-dispositions.jsonl` accounts for every Agent 2 source-main file. It records source Git blob SHA-1, byte SHA-256, byte count, source lifecycle fields, destination relation, and action.

- 956 exact source-main files (7,190,620 bytes) were preserved under `corpus/source-main/`. Across source main, the four owned PRs, branch-only heads, and worktrees, 1,217 distinct first-party file blobs were physically preserved.
- 59 files were explicitly excluded: 21 third-party source items, 30 repository/operations items, 4 superseded navigation or policy files, 3 coordinator-owned state files, and 1 migration bookkeeping file.
- 28 preserved source files conflict with destination content at the original pathname. They are archived by source path and were not written over destination files.
- Sixty preserved source files have source artifact-index entries. Proposed noncanonical archive records are in `ledger/proposed-source-main-artifact-index-records.jsonl`; 20 source artifact IDs already exist in the destination index, so the proposals use collision-free proposed IDs and preserve the source IDs only as provenance.

The local cache was treated as read-only evidence. Its recorded SHA-256 values were rechecked against all 885 cache files mapped to Agent 2 source paths; no cache bytes were imported.

- 830 local files are byte-identical to the pinned source and were not used as copy inputs.
- 38 transformed cache variants were not imported; their transform descriptions and source hashes remain in the ledger.
- 14 transformed cache entries are exact destination-path duplicates and were not copied.
- 3 of the audit's 224 local/destination conflicts map to Agent 2 source paths. All are recorded as reconciliation obligations; no destination path was overwritten.

See `ledger/local-cache-agent2-reconciliation.jsonl`. The other 221 local conflict rows do not map to Agent 2 pinned source paths in the audit mapping.

## Four owned source PRs

The full 28-file source-PR-to-destination ledger is `ledger/source-pr-destinations.jsonl`. Exact heads and blob hashes are recorded per changed file. The sources remain open and were not modified.

| PR | Destination action | Research status and limits |
| --- | --- | --- |
| [#949](https://github.com/1337isnot1337/e-99/pull/949) | Preserved 4 new files; registry and research README diffs kept out of shared files. | Target B atomic Mantel equality candidate remains unreviewed and conditional. The report preserves corrected/withdrawn numerical reasoning and the connected-notch negative regression. Exact finite checks do not prove the asymptotic geometric hypotheses or global optimality. |
| [#954](https://github.com/1337isnot1337/e-99/pull/954) | Preserved 10 first-party files; excluded two Packomania coordinate fixtures; kept registry and README diffs out. | Four global reports and five supporting code files remain unreviewed. They distinguish equal infima from attainment, limit a strict-competitor argument to its hypotheses, preserve a dense nonglobal trap and a radial-reassignment barrier, and record a conditional near-triangle population bound. None closes the global problem. The excluded inputs were used ephemerally for the exact checker run; only their provenance and hashes are retained. |
| [#970](https://github.com/1337isnot1337/e-99/pull/970) | Preserved the new run-lock; report, certificate, and verifier are exact destination-main duplicates; shared registry and README changes were not copied. | Noncanonical connected near-disk regression demonstrating a limit of scalar-only virtual payment. It is not a counterexample involving a global minimizer. |
| [#1007](https://github.com/1337isnot1337/e-99/pull/1007) | Preserved both changed files as historical evidence. | Records original dirty-worktree-14 periodic-extension preservation and activity disposition. Its source says the unique periodic extension is in PR #956. That PR's report and exact checker match destination main; the destination audit and catalogue have differing current versions and were not overwritten. The original private worktree bytes and full private metadata were not available to this migration, so no recovery of them is inferred. |

PR file counts: 17 new first-party artifacts preserved; 3 exact duplicates on destination main; 6 shared index/navigation conflicts not copied; 2 third-party coordinate inputs excluded pending rights review. Proposed artifact-index records are in `ledger/proposed-artifact-index-records.jsonl`; proposed rights review rows are in `ledger/proposed-rights-ledger-updates.jsonl`.

## Branch-only and dirty-worktree evidence

- The branch-head manifest records 147 local/live `(full refname, head SHA)` pairs, 21 open PR heads, and all non-PR heads ahead of pinned source main. Agent 2 owns 30 ahead non-PR heads with SHA256(full refname) remainder 1.
- The branch-file manifest contains 541 residual file/head rows after exact-content reconciliation against pinned source main, every open PR tree, and destination main. It preserves 387 first-party path occurrences, representing 235 unique SHA-256 artifacts. Repeated identical content across branch heads is stored once. It excludes 154 path occurrences (118 coordinator state, 19 nonresearch source files, 17 repository/operations files), representing 108 unique blobs.
- Of the 387 preserved branch rows, 293 are same-path destination conflicts (61 distinct paths, 152 unique contents); all remain separately archived.
- The dirty-worktree manifest partitions all 30 identifiable paths by SHA256(path) modulo 3. Agent 2 owns 11: nine exact files were preserved and two dirty artifact-index files were excluded for coordinator reconciliation.
- Two additional registrations have no usable worktree path or artifact hash (`/tmp/e99-diameter-stress-gap-20261002` and `/tmp/e99-source-cycle-20261001`). They could not be partitioned or preserved, and this migration makes no inference about their contents.

The full branch manifests are in `branches/`; their summary has checksums for each manifest.

## Verification

All copied source-main, branch, worktree, and source-PR bytes were checked against their recorded hashes. The read-only local cache hashes were rechecked. `ledger/integrity-verification.json` records the exact counts and a passing destination-integrity check. A static AST inventory parsed 374 preserved Python files with no parse failures; the inventory executes no scripts, and files flagged for dynamic loading, possible writes, or process calls were not run as part of it.

Twelve selected exact/finite verifiers passed: both #949 verifiers; all four #954 verifiers; the exact #970 verifier; the destination-main #956 population-bound verifier; and four Agent 2 corpus verifiers covering Target A, Target B, Target C-II support-level closure, and a global two-copy obstruction. Their hashes, commands, complete output, and limits are in `ledger/special-pr-certificate-results.json`, `ledger/source-pr956-dependency-verification.json`, and `ledger/corpus-certificate-results.json`.

The #954 coordinates were extracted from the source PR Git objects only inside a temporary directory for the read-only run, then removed. They were not committed. The run verifies a finite nonglobal regression; it does not prove global optimality. The Target C-II verifier is support-level finite closure only; C-II remains open. `MANIFEST-SHA256SUMS` records checksums for the generated manifests, reports, verifier receipts, and build scripts.

## Coordinator follow-up

- Review the 60 proposed source-main archive catalogue records and six proposed special-PR records before any shared-index update. The active artifact index remains unchanged.
- Review 23 excluded third-party items in the proposed rights ledger. No third-party PDFs or Packomania coordinate files were imported.
- Keep the three Agent 2 local-cache conflicts and the two unavailable dirty-worktree registrations open until their owners/coordinator resolve them.
- Route the source PR #956 audit/README differences through destination review only if needed; this shard retained the destination versions and verified the exact report/checker already on main.
- Preserve the private-only original-worktree-14 recovery distinction. The source PR #1007 activity disposition is historical evidence, not fresh activity evidence.
