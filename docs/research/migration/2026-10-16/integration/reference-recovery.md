# Reference and reproduction recovery

The pinned source is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
The current mathematical state remains C-I closed and C-II open.
These repairs do not promote a mathematical claim.

The [restoration ledger](reference-restorations.json) records twelve exact source files at their original paths.
These files repair four active references, their document dependencies, and the discrete-replacement reproduction package.
Every entry retains its source Git blob identity.
Accepted baseline research files and immutable source snapshots remain unchanged by these restorations.

The [navigation receipt](reference-navigation-receipt.json) records an earlier complete scan of 4,939 Markdown documents.
That scan had zero active first-party path gaps.
Its local commit and counts survive in the retained tool history.
The local runtime later became unavailable before the original receipt and generated map were uploaded.
The receipts here explicitly distinguish reconstructed records from byte-identical recovered artifacts.
The rebuilt scanner requires a fresh run against the final merged tree.

Most branch references in the earlier scan pointed to exact files from the pinned source-main snapshot.
This mapping does not establish the dependency version at each older branch.
Other records identify a file within the same snapshot, or another historical version with an explicit version limit.
Three stale filenames have explicit navigation corrections.
Independent agents matched corrected README paragraphs and the PR 737 report scope before these corrections.

One historical verifier link remained unrecovered:
`research/verify_threshold_cut_torque_2026_10_02.py`.
Its recorded uncommitted version has SHA-256 `2955a0800602e81caab257d5351b764071ad79e95b9577e4a1decfd24f325375` and 5,459 bytes.
A related verifier or a rewritten program cannot establish preservation of those original bytes.
The separate worktree ledger records this version among the unresolved dirty-file histories.

The [replay receipt](reference-replays.json) retains observed results from before the outage.
The exact three-isometry checker validated all 21 source pairs and five complete row benchmarks through 961 labels.
Its JSON replay rejected truncated states and all-identity substitutions.
The exact mixed-exchange program validated full-source certificates, matching-cover duals, and malformed-witness controls.
The exact discrete-isometry sweep covered 38, 10, 10, 14, 16, and 28 cells across its fixtures.
It rejected the inactive-isolate upper-pair error, truncated states, and nonbinary states.
All three exact programs rejected optimized Python.

The oblique-lattice program supplied floating-point sanity checks.
The seeded three-isometry discovery reproduced trial 8 and all 21 proper three-group patterns.
These numerical results do not replace the separate exact certificate.
The discrete-isometry replay used the locked verification environment because default Python lacked SymPy.

## Reproduce the reference scan

Use new output paths outside the checkout:

```sh
python3 tools/audit_migration_navigation.py --repo . --ref HEAD --output /tmp/e99-navigation-new.json --navigation-output /tmp/e99-historical-map-new.md
```

The tool checks committed Git objects with replacement objects disabled.
It pins the source inventory and the dirty-payload context receipt.
It does not fetch external references or execute research programs.
Its active-document pass is separate from source coverage, historical worktree recovery, and final Gate 2 verification.
