# Target C shard 01 review batch 04

Owned frozen source-main indexes: 90–119 inclusive (30 reports). The reports were absent from destination commit `358af8253f85ab7b9cdbf976ce186ee8426718e` and were integrated byte-for-byte by PR #40 at `dfac17ac8f3e7d77eef1a1f95713980a0fa0fbda`. This follow-up records source/current-main hashes, full mathematical result anchors, lifecycle, candidate overlaps, manual comparison decisions, and local dependency state.

The review ledger does not promote any claim. Source files remain `canonical: false` and `unreviewed`. See `dispositions.jsonl` for a reproducible record per report and `dependencies.jsonl` for missing local references.

Run `python verify_reconciliation.py --source /path/to/e-99 --destination /path/to/erdos-99` for exact blob/SHA-256 verification. Run `python compare_frozen_corpus.py --source-repo /path/to/e-99 --destination-repo /path/to/erdos-99` to reproduce the pinned full-tree five-word overlap candidates.

The unique support files for index 101 are preserved under `../support/research/`. Index 95 uses a verifier included in batch PR #43, pending that PR merge. Index 110 retains two unresolved cross-shard report references, listed in `dependencies.jsonl`; the annular Voronoi report it also cites is already present on current main.
