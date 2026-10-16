# Erdős #99 source research migration

**Overall migration status: INCOMPLETE.** Exact source and destination baselines are frozen under the baseline directory. Source-main audit batch 1 merged as PR #19; the PR #1008 population-reserve candidate merged as PR #20 at 495351ba7d127deb48f3666623615ff6ea19c39e. The PR #951 vacancy-release batch is based on that commit. The 826 still-missing source-main reports, bulk research tree, most open-PR additions, and historical PR work remain queued.

## Open source PR batch — #1008 population reserve

The pinned draft head `ad1bda373a5cbd8c666040f64b4f6ecd83223e31` is now
preserved as a separate, noncanonical research candidate. It adds one
mathematical report, one exact verifier, and its finite JSON fixture. The report
strengthens the global population-reserve lower bound from order \(D^{2/3}\)
to an explicit linear-order candidate for every global minimizer. It remains
unreviewed and does not prove the Target C conclusion; the precise upper-reserve
or strict-competitor bridge is in the candidate registry. PR #956 is a relevant
comparison cited by the report and remains queued as a distinct source head.

The five path-level PR #1008 dispositions, source Git blobs and SHA-256 hashes
are in [`ledger/source-pr-files.jsonl`](ledger/source-pr-files.jsonl). The local command outcomes and hosted-CI limitation are preserved in [`receipts/target-c-pr1008-local-verification.json`](receipts/target-c-pr1008-local-verification.json). The report
was transformed only to remove references to third-party PDFs absent from this
destination and to clarify the destination's review policy; its source and
public hashes are recorded. The verifier and JSON fixture are byte-identical to
the pinned PR head. The source tree's `research/README.md` section is retained as
adapted destination navigation, and its generated artifact-index change is
replaced by a destination index rebuild.

## Open source PR batch — #951 vacancy release and restoration research

The pinned source head 0023585a98d8f5f23df64174a091c143710ba78a
(PR merge base d999528cfaafd811a4a19bcfacd00f217c2fc375) contributes seven
first-party proof reports, five exact verifier scripts, and five JSON fixtures.
All 17 mathematical/evidence files are copied byte-for-byte. The changed source
research README is represented by focused destination navigation, and the
generated source artifact-index change is replaced by rebuilding the
destination index. All 19 changed source paths have explicit source Git blob,
SHA-256, target, lifecycle, dependency, treatment, and destination hash records
in [the PR file ledger](ledger/source-pr-files.jsonl).

The substantive route combines one-vacancy full-chart and side-pin release
candidates, an effective fixed-wall packet and wall-span stress identity, exact
rhombic hop and strip-capacity results, a unilateral local-rigidity barrier,
and an arbitrarily near-coherent pinning regression. These conditional results
and counterexamples remain **unreviewed**. The exact remaining obligation is
source extraction plus cardinality restoration through changed guards, outside
capacity, or a nonlocal discrete replacement; no C-II or Level I conclusion is
promoted. The [candidate registry](../../../targets/target-c/candidate-registry.json)
records each claim, canonical dependencies, paired verifier/fixture, obstruction,
validation limit, and next proof obligation.

## Frozen repositories

- Source main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`).
- Frozen destination baseline main: `60c2576b4893a7e9001d2c8bfbe5cfb64c1c969f` (tree `f4d73c1080b3b4a1b7757f5fd96109b6cd4b5c76`).
- Destination main before the PR #1008 batch: 806f150c4b47b1b831163fc89c78f2b1c87318a2 (tree 2969aff9998da3146dda5eab0a0df593f24dc506).
- PR #20 merged as 495351ba7d127deb48f3666623615ff6ea19c39e (tree db11ffa20d29d91548868edd0784d8321c91cfa1); the PR #951 batch is based on this exact tree.

Before preparing this batch, the live source main and open-PR list were refreshed.
Main remained at the frozen SHA above; all 21 open PR numbers and head SHAs still
match the frozen inventory. The timestamped supplemental API response is retained
at [`baseline/source-open-prs-observed-2026-10-16.json`](baseline/source-open-prs-observed-2026-10-16.json).

The source Target C artifact index has 1,287 rows: 83 missing audits and two linked reports are integrated, 826 other missing reports are queued, 338 exact duplicates are verified, and 38 conflicting source versions are archived as historical `.source` snapshots. The recursive source-link audit has 100 records (31 missing, 11 modified, and 58 exact destination copies). This batch resolves four missing linked files and preserves the 11 modified source versions (some overlap the 38 artifact conflict snapshots); 27 missing report dependencies remain queued. It verifies 84 of 384 evidence edges in the imported audit closure. All 18 link corrections are recorded for the report batches. Full source hashes, lifecycle labels, target/state metadata, and destination mapping are in [`ledger/source-main-artifacts.jsonl`](ledger/source-main-artifacts.jsonl). The scientific status of the import, including the one-claim source/destination lifecycle reconciliation and remaining math scope, is in [`scientific-reconciliation.md`](scientific-reconciliation.md).

The 2,707 source-main C research files, 157 route documents, and shared candidates are inventoried in [`ledger/source-main-files.jsonl`](ledger/source-main-files.jsonl). Of the research files, 2,536 other files are queued, 152 are exact destination duplicates, and two of 19 linked dependencies are integrated here; the remaining 17 linked dependencies and all other route files retain explicit queued or duplicate dispositions.

Source lifecycle labels are provenance only. The destination theorem-state remains authoritative. No theorem is promoted by this import. Historical versions are visibly distinguished, including the earlier inverse-phase audit that asserts a global `K'/D`-Lipschitz chart and `q=O(D^(4/5))`; those inferences were withdrawn and must not be used as premises.
