> Generated reading edition · [exact source](../../research/r3_local_rank_repair_status_2026-09-28.md) · source SHA-256 `46b84188e365f1b6d62cb5b6335ce7bceeb178cf0cd77d8c947713843d86e1f1`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e76ca104a948aa7aad98eb50dc6138db54bb62dc", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/r3_local_rank_repair_status_2026-09-28.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "412ebc3726d3ea43423ee18d5f19021c0a92364040ab3608ca8f0df43e4e01d9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# r=3 local-rank repair status

Date: 2026-09-28

The local-rank-safe r=3 reduction is accompanied by persisted executable source.

Verifier: `research/verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d0p3_three_singleton_r3_local_rank_repair_2026_09_28.cpp`
Helper: `research/r3_local_rank_common.hpp`

The verifier implements the support-only relaxation proved in `research/r3_local_rank_reduction_2026-09-28.md`: every actual-empty block lies in `E*`, every actual selected singleton lies in `S*`, and `C*=T\(E* union S)` is a subset of the actual complete family. It does not use the false implication that nonrepeated containing supports force local rank one. The old nominal-dimension and generator-support filters are absent.

The consolidated verifier is fail-closed: it returns success only if it reproduces the full expected census:
- 27,763 support orbits;
- 13,574 with `h<=20`;
- 420 three-pair matchings;
- 5,701,080 orbit/matching tests;
- 676,371 relaxed singleton triples;
- 0 structural passes;
- 0 survivors.

The hardened verifier blob is `f904a296e494041b5419db7c472fbbbd5184e813`. It was compiled and executed locally from byte-identical source during this run and reproduced exactly that census with exit status zero.

Accordingly the r=3 three-singleton branch remains closed after removing the false local-rank converse.
