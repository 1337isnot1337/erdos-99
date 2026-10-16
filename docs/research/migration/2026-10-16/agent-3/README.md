# E-99 to erdos-99 migration — Agent 3

This directory records Agent 3's deterministic corpus shard, source PR review, branch and dirty-worktree recovery, file-level provenance, and verification. The migration preserves research and its evidence. It does not promote theorem claims or change destination theorem-state, publication-policy, or rights manifests.

## Pinned repositories and allocation

The reproducible comparison used source `e-99` commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`) and destination `erdos-99` commit `c6e0394b3152d21075328bf4f26e6c070229bf13` (tree `383999d67c789e79166e6e3c8f69aa5d56844c8e`). Fresh source and destination main refs matched those pins when fetched for this run; the pre-PR refs and destination PR inventory are recorded in [`evidence/final-refs-before-pr.json`](evidence/final-refs-before-pr.json). The full source-main comparison is in [`source-main-allocation.jsonl`](source-main-allocation.jsonl); grouped units are in [`source-main-units.jsonl`](source-main-units.jsonl).

The 4,717 source-main files partition as 1,471 exact-content destination copies, 203 members of the existing frozen 813-report set, 2,938 missing-content files, and 105 same-path content conflicts. The 3,043 missing or changed files form 2,685 deterministic research units. Units use normalized report/verifier basename pairing for `target_a_`, `target_b_`, `target_c_`, and `global_` files; other files use their full source paths. Scoring follows the assignment prompt, then units are sorted by descending cost and key and assigned sequentially to the least-loaded total from seed `[90, 75, 60]`.

| Agent | Units | Files | Final seeded workload score |
| --- | ---: | ---: | ---: |
| 1 | 894 | 1,014 | 4,280 |
| 2 | 896 | 1,015 | 4,280 |
| 3 | 895 | 1,014 | 4,279 |

The max-minus-min score spread is 0.0234% of the mean. SHA-256 of the complete allocation is `509d1c3d4927cba83d77e9973d242931e48a2b195dd2720af91e2476dae3debd`; the unit ledger is `2721761cbb31f62776a38ca7f79e93cd17b06ae3dad0f8cd7e4e0285924c22d8`. The pinned frozen-report index hash is `12e5b08b2ff78f48e28ce00cbf8b351ac16b5ea0856c5fb102f75fe182d211ca`. The excluded frozen set was not re-imported.

Rebuild the main allocation from the pinned commits and the frozen index with:

```sh
python3 docs/research/migration/2026-10-16/agent-3/build_allocation.py \
  --source "$SOURCE" --destination "$DESTINATION" \
  --source-commit 42f0296d1aca068c809f74cee5dcdb4ebdb27c73 \
  --destination-commit c6e0394b3152d21075328bf4f26e6c070229bf13 \
  --frozen-index docs/research/migration/2026-10-16/shards/frozen-813-index.jsonl \
  --output /tmp/agent3-allocation
sha256sum /tmp/agent3-allocation/source-main-allocation.jsonl
```

## Source-main migration

Agent 3's 1,014 assigned files resulted in 956 preserved destination files (894 at source paths and 62 historical snapshots) and 58 explicit scope exclusions. The preserved material is 7,189,651 bytes. Every source-main row records its pinned source commit, Git blob, SHA-256, lifecycle metadata, destination hash, transformations, and disposition in [`source-main-dispositions.jsonl`](source-main-dispositions.jsonl). The 58 exclusions are 22 third-party papers/OCR files, 28 unrelated infrastructure files, 7 shared navigation changes, and 1 unrelated item. These exclusions do not discard first-party proof text or verifiers.

The 62 historical snapshots retain conflicting or prior source versions with provenance and nonpromotion notices. Current destination corrections take precedence where applicable. The original frozen Target C report migration remains intact and is represented by the unchanged shared 813-file index and receipts.

## Assigned source PRs

The exact head SHAs, full file inventories, and per-file dispositions are captured in [`pr-dispositions.jsonl`](pr-dispositions.jsonl), [`pr-disposition-summary.json`](pr-disposition-summary.json), and the four `evidence/pr-*-file-disposition.json` files. Across 18 changed files, 6 mathematical files were new and preserved, 5 were byte-identical destination copies, 3 README navigation changes were retained as a patch, and 4 source artifact-index edits were excluded from the shared destination registry.

| PR and pinned head | File dispositions | Mathematical significance and limits |
| --- | --- | --- |
| [#953](https://github.com/1337isnot1337/e-99/pull/953), `7be6a6b746e9cf6ea18145248b652c7a0f206dc4` | Full inventory: report plus shared artifact index. The report is new and preserved; the index edit is excluded. | The report develops a one-arm-per-crossed-edge source-localization bound with exception `|E(Σ)| + 8d + 1`. Its population-scale estimate is vacuous, it gives no Section-175 rank improvement, and a lozenge regression rules out the direct gate-to-Schur step. Source-response sector surplus remains open. |
| [#966](https://github.com/1337isnot1337/e-99/pull/966), `88b473899edc5f63c50aa6f90bf9a4d63112a66d` | Five files: report, certificate, and verifier are exact destination copies; artifact-index edit is excluded; README change is recorded in the shared patch. | The coembedded triangular-lattice regression has full Schur rank on its stated open-phase/nonzero-weight domain and gives a locked three-spoke fan with one crossing. Whole-population replacement makes that family nonglobal for `m ≥ 32`. It does not refute the canonical endpoint or settle source/global diameter coupling. |
| [#967](https://github.com/1337isnot1337/e-99/pull/967), `3a80b4bd2d75a439835ab26a863521816a0f39d1` | Seven files: the report, Cartesian checker, rhombus certificate, run note, and integral-norm verifier are preserved; the artifact-index edit is excluded; README change is recorded in the shared patch. | The rhombus-mesh obstruction shows that the specified endpoint cannot be reached under pairwise nonexpansion and records the local growth needed to reach diameter `2(R−1)`. A separate near-triangular nonglobal regression has a strict same-cardinality competitor. The bound does not apply to an arbitrary tiny strict improvement and does not close Level I. |
| [#969](https://github.com/1337isnot1337/e-99/pull/969), `b3983cdc7f4ca32ad8083eade92952d451c60848` | Four files: report and verifier are exact destination copies; artifact-index edit is excluded; README change is recorded in the shared patch. | The report gives a Hall-tight row/strict-isolate reduction with individual terminal eligibility, and a fully locked neutral-fan regression where zero Schur nullity is not forced. A three-point global plateau blocks unrestricted simultaneous terminal choice. The source-response sector-surplus step remains open. |

Reports and copied verifiers remain unreviewed/noncanonical. Their source PR status and internal PASS labels are provenance only. The shared README diffs are in [`pr-shared-metadata-diffs.patch`](pr-shared-metadata-diffs.patch); no shared index or theorem-state file was changed.

## Source branches and dirty worktrees

The union of fetched local and live-remote source refs had 138 refnames and 111 ahead-of-main branch-head observations. Their histories contained 478 unique commit objects; 370 were reachable from source PR head refs and were accounted for there. The 108 residual unique commits were assigned by `SHA256(full refname) mod 3`; Agent 3 owns 49. Seven non-PR refs and one PR-named residual ref had Agent 3 ownership. The residual is `refs/heads/swarm/sol/diameter-stress-gap-20261002`, whose remaining commit `d33db214…` changes a report that is already an exact Agent 3 source-main artifact. The PR #631 head commits themselves are accounted for through the PR ref. Full branch-head and commit evidence is in [`source-branch-heads.jsonl`](source-branch-heads.jsonl), [`source-branch-commits.jsonl`](source-branch-commits.jsonl), and [`source-branch-summary.json`](source-branch-summary.json).

Commit changes were compared to each commit's first parent, including merge commits, so merged second-parent file additions were not lost. Deduplicating against destination main, pinned source main, PR-reachable commits, frozen-report receipts, and sibling allocations yielded 746 unique branch file versions. Of these, 21 current, unreviewed Agent 3 branch artifacts and 76 historical versions were preserved as 97 unique files. The other 649 versions are accounted for as exact destination duplicates (99), exact body duplicate (1), Agent 3 source-main preservation (180), verified frozen-report migrations (6), or source-main assignments to Agents 1/2 (363). The full rows and exact hashes are in [`source-branch-artifacts.jsonl`](source-branch-artifacts.jsonl) and [`branch-dispositions.jsonl`](branch-dispositions.jsonl).

The current branch set preserves distinct work on global attainment/triangle-free infima, isolate-forest normalization, periodic release and diameter transfer, and a local lex/crystalline obstruction. The Target C reports preserve source-wide population-reserve, shallow-wall release, Delaunay/Voronoi defect-spacing, fan-forest, isolate-normalization, core-cap, and shell-fold arguments. Negative reports retain the pentagon opening/contact-debt and short-wall winding obstructions. These artifacts contain their own hypotheses, computational records, and limitations; the migration does not treat them as the missing global bridge. `research/level_i_closure_run_2026_10_07.md` is retained as a historical run record, not as a closure certificate.

The frozen dirty-worktree snapshot contains 32 path records. Four accessible Agent 3 paths from `/home/cinna/math/e99-global-repacking-20261012` match the frozen snapshot: a report, verifier, hybrid-matching JSON fixture, and shared README change. The report and verifier are preserved as historical source versions, the fixture is retained at its destination verifier path, and the README change is kept in [`dirty-shared-readme.patch`](dirty-shared-readme.patch). One Agent 3 path remains unresolved: the worktree `/tmp/e99-diameter-stress-gap-20261002`, ref `refs/heads/swarm/sol/diameter-stress-gap-20261002`, head `d33db214…`, is inaccessible and has no recoverable worktree files or `.git` metadata in the frozen snapshot. Its exact unresolved record is in [`dirty-dispositions.jsonl`](dirty-dispositions.jsonl); no source worktree was reset, cleaned, or deleted. The other three unresolved dirty records belong to unmapped/detached paths outside Agent 3's ownership.

## Verification and open items

The independent verifier [`verify_agent3_migration.py`](verify_agent3_migration.py) reports `PASS`, zero integrity errors, and checks each assigned source blob/SHA-256, destination hash and Git blob, proof-body preservation after recorded wrappers, branch and PR dispositions, imports, and relative links. Its receipt is [`evidence/verification.json`](evidence/verification.json). It checked 685 Markdown files and 1,515 relative links; 1,454 resolve directly. The 61 unresolved paths are classified: 9 assigned to Agent 1, 13 to Agent 2, 1 excluded by Agent 3's scope, and 38 third-party references intentionally not copied. There are 8 missing-local-import references; each points to a support module assigned to Agent 1 or 2, with no missing Agent 3-owned local dependency.

Ten selected proof/certificate runs passed, plus a source dirty-worktree integrity check that confirmed the worktree state was unchanged. The logs and exact script/input/output hashes are in [`evidence/verifiers/`](evidence/verifiers/) and `evidence/verifiers/verifier-results.json`. Covered checks include PR #966 locked Schur rank, PR #967 Cartesian certificate and rhombus mesh, PR #969 tight isolates, global attainment, isolate forest, periodic release, Target C crop-return suffix, and both destination and frozen dirty-worktree global-palette verifiers. Packomania inputs were not copied; exact local fixture hashes are recorded in the receipt. Imported scripts were inspected before execution. An AST import audit scanned 393 Python files; `numpy`, `scipy`, and `sympy` were available. The eight cross-shard missing imports above were not run as standalone scripts in this shard.

Preserved outputs are 956 source-main files, 6 new PR files, 97 branch versions, and 3 dirty-snapshot files: **1,062 unique files**. There are **654 PR/branch duplicate or sibling/frozen handoff records**. Separately, the corpus-level allocation excluded 1,471 exact source-main content copies before assigning work. The single unresolved Agent 3 item is the inaccessible dirty worktree noted above; all source-main, PR, and branch artifact rows have explicit dispositions. Current Level I remains open; Target C-I remains closed and C-II remains open.

## Integrity files

[`SHA256SUMS.txt`](SHA256SUMS.txt) records the SHA-256 of each file in this Agent 3 evidence directory except the checksum file itself. Regenerate from the repository root with:

```sh
find docs/research/migration/2026-10-16/agent-3 -type f ! -name SHA256SUMS.txt ! -path '*/__pycache__/*' -print0 \
  | sort -z | xargs -0 sha256sum > docs/research/migration/2026-10-16/agent-3/SHA256SUMS.txt
```
