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
