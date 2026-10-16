# Frozen Target C report shards

This manifest fixes the user's five disjoint path ranges against source main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73` and destination baseline main `358af8253f85ab7b9cdbf976ce186ee8426718e4`. It selects unique `target-c` entries in the source artifact index whose exact path is absent from the baseline Git tree, then sorts by path. The full file-level record and each shard slice include source blob and SHA-256, source index lifecycle/dependency fields, exact baseline tree membership, and proposed destination. Hashes in `manifest.json` protect each ledger slice.

The ranges are exactly: shard 1, indexes 0–162 (163 paths); shard 2, 163–325 (163); shard 3, 326–488 (163); shard 4, 489–650 (162); shard 5, 651–812 (162). The lists are mutually exclusive and their union is all 813 selected paths.

G0050 is a separate, coordinator-preserved source-main research batch in destination PR #34. Its ten `research/` paths have zero overlap with the 813 missing `docs/reports/` paths. It does not reduce any worker shard.

## Worker boundary

Each worker may edit only its assigned report paths and a uniquely named shard-local disposition file. Do not edit the central artifact index, central migration ledger, candidate registry, Target C frontier, general README/navigation, release manifest, or publication verification records; the coordinator owns those shared surfaces. For every path, state its distinct mathematical content, exact source identity, lifecycle, dependencies, destination relation, disposition, and any transformation. Byte or SHA identity proves copy equivalence only. A same-topic match is not mathematical redundancy. Record a specific subsumption argument before using `already represented by stronger successor`. Preserve source context for conditional/unreviewed results, corrections, counterexamples, failed routes, and computational evidence. Do not promote canonical theorem state.

Workers must submit separate reviewable PRs and wait for coordinator merge. The coordinator independently checks source Git blobs and the PR destination tree before integrating.
