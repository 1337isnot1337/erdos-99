# Reference-path repair

This change restores five reference targets at their original research paths. Each file retains its exact pinned source bytes.
The source commit is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
The integration baseline for this change is `d30b74aa7d157fbadfa062618d9a7c26c4efe718`.
The [restoration record](restored-references.json) identifies the source blobs and their destination paths.

These files were already available as destination Git objects. Their archive locations did not resolve the links in the imported documents.
The existing five-module import repair remains unchanged. The original worker commits, inventories, and test receipts remain unchanged.
No existing baseline proof, theorem-state file, or publication manifest changes here.

## Claim status

The G0050 and open-cell notes remain proof-only candidates. The signed-return note retains its historical audited-working scope.
The legacy joint-train program checks floating-point scalar margins. It does not verify the geometric premises or prove a global theorem.
Its assertions require normal Python. An optimized Python run is not a valid execution of those historical checks.
No restored file promotes a claim or closes Target C-II.

## Reference checker

The new checker reads the committed tree, not untracked or modified worktree files.
It scans inline Markdown links in the documents named by Agent 3's pinned unresolved-link receipt.
It resolves each link from the actual destination location of the document.
An exact copy elsewhere in an archive does not discharge a missing literal target.
An owner label such as `assigned_to_agent_2` does not discharge a missing target.

The checker keeps third-party references separate. It does not fetch or redistribute their contents.
A removed or changed historical link needs explicit reconciliation. The checker does not silently accept the disappearance of a link.
Both historical input manifests are pinned to their recorded Git blobs.

Run from the repository root:

```sh
python3 tools/check_migration_references.py --repo . --ref HEAD --output /tmp/e99-reference-receipt-new.json
```

Use a new output path outside the checkout. The checker refuses an existing receipt or a symlink ancestor.
This command must run separately from `check_migration_union.py`. Byte preservation and working reference paths are different requirements.

## Executed tests

The 22 new regression tests passed with Python 3.13.5, normally and under `-O`.
They include the archive-location failure, stale owner labels, changed evidence, symlink rejection, and committed-versus-dirty bytes.

```sh
python3 -m unittest discover -s tools -p 'test_migration_references.py' -v
python3 -O -m unittest discover -s tools -p 'test_migration_references.py' -v
python3 research/verify_target_c_optimized_joint_train_legacy.py
```

The historical scalar program also passed under normal Python 3.13.5.
Its displayed final floating-point margin was `0.0039862558671350`.
The [test receipt](reference-repair-tests.json) records exact code hashes and the verification boundary.

## Remaining work

The original receipt records 61 unresolved reference occurrences: 23 internal references and 38 third-party references.
Restoring these five targets does not establish that every internal link now resolves.
Archived documents can still require a different relative path from their new location.
The complete candidate-level link check was not executed in this local runtime because the full private checkout was not mounted.
The new tests use isolated Git fixtures and exact copies of the authored tool files.

Bulk source recovery, combined coverage, branch/worktree reconciliation, shared indexes, rights review, and Gate 2 remain open.
The reference checker only covers selected documents and inline links. It does not verify anchors, all Markdown syntax, or all imports.
A scoped PASS is not release approval or source-deprecation readiness.
