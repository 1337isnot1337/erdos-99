> Generated reading edition · [exact source](../../research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_weight4_sharpening_2026-09-26.md) · source SHA-256 `c672cb3c3992d87534930352963bee88c02bf75059c02577487f8826d736368a`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "84ac9cb7918f9870fc039d72cf263a6dcf60f5f7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k4_dminus2_weight4_sharpening_2026-09-26.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f17293c4f0e875ef9258d2179f3b77ac4fcef41546432a54ede0c6d750081d7d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: k=4 D=-2 weight sharpening

Date: 2026-09-26

Status: proof-level strengthening of the remaining eight-no-root k=4, D=-2, d_root=0, p=2 branch.

The preceding k=4 reduction gives rank(P)=4 and generalized weights at least (3,4,6,7). For a deleted coordinate set S with s=|S| and puncture rank loss q, D(B-S)=D(B)+2s-3q.

Fix |S|=3. Since d2(P)>=4, q<=1. If q=1, the five-no-root shadow has rank(P)=3, hence k=2, and D=-2+6-3=1. Its incomplete-root cost is at most the original p=2. The committed exact five-no-root k=2 slack theorem proves D>=4 whenever p<=2. Contradiction. Thus every triple puncture preserves rank and d1(P)>=4.

Generalized Hamming weights are strictly increasing. Combining d1>=4 with the previous floors gives

(d1,d2,d3,d4)(P) >= (4,5,6,7).

Consequences: every deletion of at most three coordinates preserves rank four; a four-coordinate deletion loses at most one rank; and no two-dimensional coefficient subspace is supported on four coordinates. Four-row shadows are therefore only (D,k,rankP)=(6,0,4) or (3,1,3); the old q=2, D=0, k=2 boundary is impossible.

This does not close the branch. It reduces the next finite search to rank-four coefficient spaces satisfying the near-MDS weight hierarchy (4,5,6,7).
