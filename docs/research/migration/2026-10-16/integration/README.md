# Three-agent integration and coverage repair

Status: incomplete migration; not a release or source-deprecation approval.

## Preserved submissions

The integration commit retains the original commits from PRs #72, #73, and #74 as parents:

- Agent 1: `075d6d99fdc7b9ebd972e335b1f6c040e0bf5dad`.
- Agent 2: `894330fac4df715a551537b5df0ea80f36819a3e`.
- Agent 3: `9ca239fc0e773b41005ddedd1a877b7799019877`.

The destination baseline is `c6e0394b3152d21075328bf4f26e6c070229bf13`.
The source baseline is `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
Its Git tree is `e061f039eac44c286a00eacdcaa9a4cbbb877891`.
The combined staging tree retains every submitted file. Existing destination files remain unchanged.
Source refs, original PR heads, repository visibility, and ordinary Git attribution are unchanged.

## Defect in the earlier acceptance test

The workers implemented different assignment algorithms. Their locally balanced workload totals do not prove a disjoint or complete partition.
The reviewed inventories disagree about ownership for 2,101 source paths.
Joining their own-shard disposition tables gives 2,302 distinct source paths from 3,042 rows.
There are 686 multiply handled paths, including 54 handled by all three agents.
Against Agent 1's 3,043-path backlog, 743 paths have no worker source-main disposition.
These are disposition counts, not a claim that 743 mathematically distinct files are absent.
Branch imports, existing transformed files, and justified exclusions require a separate content check.

Do not repair this defect by changing historical assignment records to claim agreement.
Use the actual combined Git tree and source identities instead.

## Source-identity coverage check

Run from a clone containing the integration commit and baseline history:

```sh
python3 tools/check_migration_union.py --repo . --ref HEAD --output /tmp/e99-union-new-receipt.json
```

The output path must be new and outside the checkout.
The checker reconstructs the complete source Git tree from all three inventories.
It rejects inconsistent source identities, duplicate rows, and a wrong reconstructed tree.
It checks all recorded destination payload hashes and the pinned 813-report disposition set.
It also rejects changes to baseline files, including accepted proofs and theorem state.

Coverage is computed from actual candidate blobs at every path. Owner labels cannot discharge missing content.
The report lists gaps, duplicate payloads, ownership disagreements, and a stable source-to-destination mapping.
A historical archive copy can preserve bytes without being a runnable original-path import.
Unverified source versions remain unresolved rather than being silently classified as superseded.

An exit code of zero means only `PASS_SOURCE_MAIN_ONLY`.
The report always leaves `deprecation_ready` and `release_verified` false.
Branch-only histories, unavailable worktrees, rights, dependency closure, and Gate 2 still need separate evidence.

## Source-main recovery tool

Use an existing authorized local source clone. The tool makes no network request or Git commit.
First generate a plan:

```sh
python3 tools/repair_migration_union.py --repo . --source-repo /absolute/path/to/e-99 --output /tmp/e99-repair-plan-new.json
```

After inspecting the plan, add `--apply` and use another new receipt path.
The tool reads the pinned source commit, not dirty source working files.
It checks both Git blob identity and SHA-256 before preparing a copy.
It writes only under `integration/source-main/`, with a `.source` suffix.
It never overwrites an existing different file or writes through a symlink.
Files with identical existing bytes are left unchanged.

These are historical source snapshots, not current theorem authority or agent instructions.
Review rights and content before committing the explicit additions. Do not use `git add .` on an old migration checkout.
Rerun the union check against the resulting committed tree.
A plan or successful copy operation is not proof of migration completion.

## Reproduction paths repaired here

Five modules were restored at their original `research/` paths.
They address all eight missing local-import references in Agent 3's pinned verification receipt.
Three exact blobs were already archived in the destination. Two required recovery from the pinned source.
`restored-imports.json` identifies every module and its source blob.
No proof text, canonical claim, or source version was changed.
The large support-enumeration programs were not replayed in this repair session.

The optional `--replay-directory` argument to the checker builds a new source-compatible historical view.
It refuses incomplete content, missing exact versions of transformed proofs, existing output paths, and symlinks.
It does not execute code or replace the accepted destination tree.
Do not treat that historical view as the active theorem ledger.

## Verification performed

The new tooling passed 22 regression tests under Python 3.13.5, both normally and with `-O`.
The recovered homothetic-capacity module passed its four existing tests.
The locally executed files match the Git blobs uploaded in this change.
The tests use isolated Git fixtures and include the independent-assignment omission failure.
They also cover frozen-proof protection, alternate archive paths, invalid hashes, and non-overwriting recovery.

```sh
python3 -m unittest discover -s tools -p 'test_migration*.py' -v
python3 -O -m unittest discover -s tools -p 'test_migration*.py' -v
python3 -m unittest discover -s research -p 'test_homothetic_capacity.py' -v
```

No full combined-corpus replay or Gate 2 execution is claimed here.
The private source checkout and complete destination bytes were not mounted in the local test runtime.
GitHub object operations were used for integration and the five-module repair.
The bulk source recovery tool was tested on fixtures, not executed against the private project.

## Remaining acceptance conditions

Run the combined audit and resolve every actual gap or document an approved disposition.
Do not infer global coverage from any individual worker PASS or from GitHub mergeability.
Review branch, PR, and dirty-worktree ledgers independently; retain unresolved inaccessible worktree records.
Complete dependency-path, navigation, artifact-index, and rights reconciliation.
Retain destination mathematical corrections and the current C-I/C-II boundary.
Run the complete release checks against the final committed tree.
Keep `e-99` intact until full-project preservation is established.
