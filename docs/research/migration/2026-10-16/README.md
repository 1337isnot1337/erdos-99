# Erdős #99 source research migration

**Overall migration status: INCOMPLETE.** The exact source and destination baselines are frozen under [`baseline/`](baseline/). This first reviewable batch integrates source-main Target C audits with their direct evidence and preserves the conflicting historical source versions. The 828 missing source reports, bulk `research/` tree, and source PR candidates remain queued for later batches.

## Frozen repositories

- Source main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`).
- Destination main: `60c2576b4893a7e9001d2c8bfbe5cfb64c1c969f` (tree `f4d73c1080b3b4a1b7757f5fd96109b6cd4b5c76`).

Before preparing this batch, the live source main and open-PR list were refreshed.
Main remained at the frozen SHA above; all 21 open PR numbers and head SHAs still
match the frozen inventory. The timestamped supplemental API response is retained
at [`baseline/source-open-prs-observed-2026-10-16.json`](baseline/source-open-prs-observed-2026-10-16.json).

The source Target C artifact index has 1,287 rows: 83 missing audits and two linked reports are integrated, 826 other missing reports are queued, 338 exact duplicates are verified, and 38 conflicting source versions are archived as historical `.source` snapshots. The recursive source-link audit has 100 records (31 missing, 11 modified, and 58 exact destination copies). This batch resolves four missing linked files and preserves the 11 modified source versions (some overlap the 38 artifact conflict snapshots); 27 missing report dependencies remain queued. It verifies 84 of 384 evidence edges in the imported audit closure. All 18 link corrections are recorded for the report batches. Full source hashes, lifecycle labels, target/state metadata, and destination mapping are in [`ledger/source-main-artifacts.jsonl`](ledger/source-main-artifacts.jsonl). The scientific status of the import, including the one-claim source/destination lifecycle reconciliation and remaining math scope, is in [`scientific-reconciliation.md`](scientific-reconciliation.md).

The 2,707 source-main C research files, 157 route documents, and shared candidates are inventoried in [`ledger/source-main-files.jsonl`](ledger/source-main-files.jsonl). Of the research files, 2,536 other files are queued, 152 are exact destination duplicates, and two of 19 linked dependencies are integrated here; the remaining 17 linked dependencies and all other route files retain explicit queued or duplicate dispositions.

Source lifecycle labels are provenance only. The destination theorem-state remains authoritative. No theorem is promoted by this import. Historical versions are visibly distinguished, including the earlier inverse-phase audit that asserts a global `K'/D`-Lipschitz chart and `q=O(D^(4/5))`; those inferences were withdrawn and must not be used as premises.
