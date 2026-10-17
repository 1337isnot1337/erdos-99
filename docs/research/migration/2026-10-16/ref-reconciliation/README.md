# Captured branch and worktree reconciliation

**Current follow-up:** all five formerly missing dirty versions were exactly
recovered from the original local worktrees; see [local recovery](LOCAL_RECOVERY.md)
and its identity ledger. All 30 captured dirty rows are present. The two
historical markers retain unknown state at migration capture. The earlier
search observations below remain historical evidence.

Source main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
Captured integration: `f282d53169df4d507117893bfdcc99f663855923`.
Level I, Target A, Target B, and C-II remain open; C-I remains closed.
These archives preserve historical bytes and provenance. They promote no claim.

The [ref comparison](live-ref-reconciliation.json) records a fresh GitHub capture:
all 45 remote branch heads and all 21 open PR heads match the frozen inventory.
The [historical ref comparison](historical-branch-ref-reconciliation.jsonl) retains
147 distinct ref/head records representing 139 distinct head identities.
The earlier 69-head count covered local ahead branches only.

The three immutable branch-artifact ledgers contain 1,643 rows.
Source-main recovery supplies 192 rows whose original bytes were absent:
140 delegated copies and 52 versions previously represented by transformed archives.
This directory preserves another 249 exact blobs, totaling 35,559,061 bytes.
These comprise 175 excluded state/index/bibliography/tooling versions and 74
original versions previously represented by transformed historical archives.
The [archive ledger](branch-support-blobs.jsonl) records both hashes, byte counts,
original paths, available commit identities, and branch refs.
All archive files use `.source` and mode `100644`; they remain inert.
Current destination theorem state and execution entry points remain authoritative.

The frozen dirty-worktree inventory contains 30 known file rows and two markers
without captured file identities. Initially, 23 known rows were preserved.
Two artifact indexes were subsequently reconstructed from 1,047 common rows plus
their known dirty report rows. Their entire captured SHA-256 hashes and byte
lengths match. The [recipes](dirty-index-reconstruction.json) reproduce both.
Twenty-five known dirty rows are preserved; five research/code versions remain missing.
Their [identity ledger](known-missing-dirty-identities.jsonl) retains exact paths,
hashes, sizes, original worktree locations, and source heads.

All 15 documented original worktree paths and the original frozen audit directory
were absent from the last available runtime. The [path check](local-worktree-path-check.json)
distinguishes that observation from the current environment outage.
The saved cleanup evidence ZIP contained workflow code and logs, not these payloads.
Related saved migration text supplied paths and hashes rather than missing bytes.
GitHub main path history was empty for the three never-committed files.
The [loose-object scan](full-object-dirty-scan.json) hashed 7,772 blobs.
The [Git batch scan](full-git-object-dirty-scan.json) hashed 7,800 blobs including
alternate and unreachable objects. Neither found the five missing hashes.

Run `python tools/check_migration_refs.py --repo . --candidate HEAD --output /tmp/e99-refs-new.json`.
The output must be new and outside the checkout, without symlink ancestors.
The checker pins the captured obligation manifests and uses original Git objects.
It executes no research code. Exit 1 reports missing known bytes or invalid evidence.
The [recovery receipt](recovery-checkpoint.json) distinguishes earlier local tests
from code reconstructed after the execution environment became unavailable.
The reconstructed Python files require a fresh test run when execution returns.

The historical five-file gap is resolved by the local recovery follow-up.
Source deprecation remains deferred pending owner disposition of the two
markers without captured identities.
No original commit, PR, branch, or author metadata was rewritten or removed.
Prepared with Codex AI assistance.
