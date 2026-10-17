# Complete preservation of the pinned source main tree

The pinned source main tree now has no unexplained first-party byte gaps.
This result covers source-main preservation only.
Branch history, inaccessible worktrees, dependency replay, and final release verification have separate records.

The source commit is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
Its Git tree is `e061f039eac44c286a00eacdcaa9a4cbbb877891`.
The audited payload commit is `bad80df13634295c43353a7fd2cc6f61d2192881`.
The destination baseline is `c6e0394b3152d21075328bf4f26e6c070229bf13`.

## Coverage

| Disposition | Source paths |
| --- | ---: |
| Exact source bytes in the destination | 4,654 |
| Third-party reference files not redistributed | 63 |
| Unresolved paths | 0 |
| Total pinned source paths | 4,717 |

The [complete disposition ledger](source-main-complete-dispositions.jsonl) contains one row for each source path.
Each row records the source Git blob, SHA-256, original file mode, and exact destination identity or reference exclusion.
The [preservation receipt](source-main-preservation-receipt.json) records the audited commit and ledger hash.

The checker reconstructs the source Git tree from all three worker inventories.
The actual source checkout independently matches that reconstructed tree.
All 2,297 destination baseline files retain their bytes and file modes.
All 813 frozen imported-report records retain their final destination identities.

## Recovery

The original integration contained 3,372 exact source identities and 203 verified frozen transformations.
Another 1,079 source paths lacked an accepted preservation disposition.
The recovery adds 1,282 exact historical source files.
These include the 1,079 unresolved originals and the 203 originals of frozen transformations.

An existing file at the original path does not establish preservation of the original source bytes.
The earlier same-path comparison therefore understated the original-byte recovery requirement.
The 203 accepted transformations remain valid destination documents.
Their historical originals now survive separately.

The archive uses `integration/source-main/<original-path>.source` beneath the migration directory.
The `.source` suffix keeps historical scripts and instructions inert.
The archive preserves exact bytes and records original file modes in the ledger.
It does not replace corrected canonical documents or promote historical claims.

The repaired recovery tool independently accepted the real 1,079-entry recovery plan.
It found those exact files already present and wrote no duplicates.
The additional 203 original files permit a complete historical replay view.

## Reference exclusions

The 63 excluded paths contain third-party papers, extracted text, and page images.
The ledger retains their source identities without copying their bytes into the destination.
The existing source bibliography and source checksum manifest remain available.
The checksum manifest already had an exact destination copy and contributes one of the 4,654 preserved paths.

No excluded reference bytes entered this recovery.
The source archive remains intact for its existing reference collection.

## Reproduction

After the schema repair and recovery are integrated, run this command from the destination checkout:

```sh
python3 tools/check_migration_union.py --repo . --ref HEAD --output /tmp/e99-union-final.json --replay-directory /tmp/e99-source-replay-final
```

Use new output paths outside the checkout.
The command refuses existing output paths.
Its successful result is `PASS_SOURCE_MAIN_ONLY`.
It does not establish release readiness or source-deprecation readiness.

The replay contains 4,653 non-reference source paths with their original layout and exact bytes.
An independent byte comparison against the pinned source checkout passed for every replay file.
The replay keeps files non-executable.
The original modes remain in the ledger.
The replay is a historical reproduction surface and does not replace the active theorem ledger.

The public validator reported 15,352 existing integration errors on the isolated payload branch.
These errors concern migration links, metadata headers, and helper imports.
This preservation receipt does not claim a public-validation pass.

The receipt uses tool-fix commit `fe3609f`.
The audited payload commit predates that tool integration and this evidence-only addition.
Run the checker again against the final combined commit.
