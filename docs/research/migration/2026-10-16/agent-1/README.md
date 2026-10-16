# Erdős #99 corpus migration — Agent 1

**Disposition: archival preservation only.** Everything imported by this change is below this agent-specific directory. Source lifecycle labels and claim statuses are provenance; this PR does not promote source claims or change destination theorem state, publication registries, or global inclusion manifests. Same-path destination revisions remain in place.

## Pinned inputs and assignment

- Source `e-99` main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`).
- Destination `erdos-99` main: `c6e0394b3152d21075328bf4f26e6c070229bf13` (tree `383999d67c789e79166e6e3c8f69aa5d56844c8e`). The live refs matched these pins when reconciliation began.
- The full three-way source-main allocation is in [`evidence/source-main-three-way-assignment.jsonl`](evidence/source-main-three-way-assignment.jsonl); atomic units are in [`evidence/source-main-three-way-units.jsonl`](evidence/source-main-three-way-units.jsonl). Both are SHA-256 pinned in [`evidence/assignment-SHA256SUMS`](evidence/assignment-SHA256SUMS).
- The deterministic LPT assignment used initial workloads `[90, 75, 60]`. Final workloads are `[4269, 4269, 4268]`, a 1-point spread (0.023427% of the mean). Agent file counts are `[1013, 1016, 1014]`; unit counts are `[893, 894, 894]`.
- Of 4,717 pinned source files, 813 Target C reports were already preserved by the destination frozen-disposition ledger and 861 other files already had identical content in the destination. They are marked preserved in the full assignment and were not copied. The remaining backlog has 3,043 files in 2,681 atomic units.

Agent 1 owns 1,013 backlog files in 893 units. The append-only reconciliation manifest at [`source-main-reconciliation.jsonl`](source-main-reconciliation.jsonl) records exact source hashes, source lifecycle/claim status, destination relation and hashes, payload hashes, conflicts, exclusions, and transformations. It archives 951 first-party mathematical or bibliographic artifacts and gives explicit dispositions for 62 files outside the shard scope. Thirty-five same-path conflicts are resolved by retaining destination bytes and archiving the exact source version under this directory. Two owner-local absolute paths in source prose were redacted, and 12 source files had trailing blank lines or horizontal code whitespace normalized for a clean Git diff; every transformation records the source hash and archived hash.

## Branches, dirty worktrees, and PR #737

- All 69 ahead-of-main branch heads were hash-partitioned and deduplicated against source main and all 21 open PRs. Agent 1 owns 19 unique non-PR heads, containing 58 post-dedup commit occurrences. The per-head, per-commit, and per-artifact ledgers are in [`evidence/source-branches/`](evidence/source-branches/). Agent 1 archived 156 unique research artifact versions, recognized 128 exact matches elsewhere, and explicitly excluded 72 repository-operation or local-support versions. Archived source lifecycle counts are 90 not indexed at that source commit, 63 unreviewed, and 3 source-labeled canonical; none of these labels changes destination status.
- Ten Agent 1 dirty-worktree files were copied from frozen audit snapshots with exact SHA-256 matches. The source worktrees were not modified. The complete 32-row partition and two unavailable-worktree records are in [`evidence/source-dirty-worktrees/`](evidence/source-dirty-worktrees/).
- Source PR [#737](https://github.com/1337isnot1337/e-99/pull/737) was open at head `73fa41814eb1cdac50ba1eab135461868437edf0` (48 PR-only commits, 46 changed paths). Forty-five non-global-metadata files are preserved in [`payload/source-pr-737/`](payload/source-pr-737/); 13 new source artifact-index rows are captured in an agent-specific append-only file. The source index and shared research README were not installed into shared destination paths. The README revision is archived in the agent payload. All 14 indexed PR reports retain source status `unreviewed`; no claim was promoted.
- PR #737’s 5 same-path differences are recorded. The destination version of the nested-hexagon report remains because it carries a clearer scope caveat. The source verifier revisions that rename the output field to `chosen_field` and add an optional half-angle tangent remain in the archive; destination verifier bytes are unchanged.
- The dependency ledger records 86 references across 43 distinct paths: 17 exact destination dependencies, 51 references to preserved PR delta files, 14 source-index references not installed, two third-party literature/extraction references excluded under the no-PDF instruction, one dependency included in Agent 1’s source-main archive, and one dependency awaiting Agent 3’s assigned source-main reconciliation.

## Mathematical content

[`mathematical-content-summary.md`](mathematical-content-summary.md) describes the preserved owner/terminal accounting, exact curved and uneven wall packets, isolate-preserving finite checks, selected-support stress identities, and negative barrier/regression findings. The reports, verifiers, and certificates retain their source classifications. These are finite or conditional research artifacts; the PR does not establish Target C-II or Level I closure.

## Exclusions and blockers

No academic PDFs, extracted paper text, or extracted paper images are copied. First-party paper bibliography and checksum metadata are retained where assigned. Shared theorem state and publication/global inclusion manifests were not changed. All assigned same-path differences have an explicit keep-destination/archive-source disposition; there is no unresolved Agent 1 destination-content conflict.

[`unresolved-blockers.json`](unresolved-blockers.json) records two registered dirty-worktree artifacts absent from the frozen snapshot: one branch-hash-owned by Agent 1 and one by Agent 3. The Agent 1 record is `refs/heads/swarm/tb1-augmented-thrackle-20261001` at `9ddd9538c29244fd22183f9682b2835f54cde0c3`; the path is missing, so its file-level path hash and contents cannot be recovered. The Agent 3 blocker is listed for coordination and was not taken by Agent 1.

## Verification and reproduction

Fifteen safe, bounded verifier executions passed: six PR #737 verifiers and all nine byte-identical destination verifier dependencies identified by the PR reports, each under a 60-second timeout. Seven verifier certificate outputs match their saved PR certificates as parsed JSON. Logs and hashes are in [`verification/`](verification/), including the aggregate [dependency verification results](verification/pr737-dependency-verification-results.json). The two PR discovery scripts were inspected and preserved but not executed: their floating-point LP searches explicitly say they are non-certifying and write discovery outputs to `/tmp`.

From the destination checkout with the pinned source and destination commits available in their Git object databases:

```sh
python3 docs/research/migration/2026-10-16/agent-1/evidence/verify_agent1_manifests.py
python3 docs/research/migration/2026-10-16/agent-1/evidence/compute_assignment.py \
  --source-git /path/to/e-99 --destination-git /path/to/erdos-99 \
  --out /tmp/e99-agent1-assignment-recheck
(cd /tmp/e99-agent1-assignment-recheck && sha256sum -c assignment-SHA256SUMS)

for f in docs/research/migration/2026-10-16/agent-1/payload/source-pr-737/research/verify_*.py; do
  timeout 60s env PYTHONPATH="$PWD/research" python3 -B "$f"
done
timeout 60s python3 -B research/verify_target_c_hub_owner_systems_2026_10_06.py \
  --output /tmp/hub-owner-systems-reproduced.json
for f in \
  research/verify_target_c_binary_crossing_scope_2026_10_06.py \
  research/verify_target_c_pentagon_capped_lock_2026_10_05.py \
  research/verify_target_c_common_angle_train_endpoint_2026_10_06.py \
  research/verify_target_c_one_vertex_wall_shield_2026_10_06.py \
  research/verify_target_c_terminal_oo_geometry_2026_10_06.py; do
  timeout 60s python3 -B "$f"
done
git diff --check
```

`compute_assignment.py` records the cost, grouping, exact-content, frozen-report, and tie-break rules. The manifest checker validates assignment totals, payload hashes, partition hashes, and evidence checksums without requiring source worktrees.
