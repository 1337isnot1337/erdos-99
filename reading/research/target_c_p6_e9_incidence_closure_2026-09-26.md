> Generated reading edition · [exact source](../../research/target_c_p6_e9_incidence_closure_2026-09-26.md) · source SHA-256 `6bd51322965ce108eaa5e9d1ddf935eeaedaa4581529a8867a5f2d879f339bb6`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b077d0c1b0761430f8e89e3b291eb4377762f516", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_p6_e9_incidence_closure_2026-09-26.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cc7544b108025df3e9de6d2d5d00fb229348ca4b752742d17545f496fc4da293"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: close the final p=6, e=9 layer

Date: 2026-09-26

Scope: final eight-no-root branch `k=5, D=-1, d_root=0, p=6`.

The preceding empty-incidence cap proves `e<=9`. This note closes the endpoint `e=9`.

Committed inputs are `rank(P)=3`, generalized weights `(d1,d2,d3)>=(2,4,5)`, exactly six touched singleton blocks, no selected pair block, and the local empty-block rule used by the existing `e=4,5,6` verifiers: an actual-empty triangle block has rank two exactly when one of its containing tetrahedral supports occurs with multiplicity at least two; otherwise it has rank one. For a block `b`, write `I_b` for the external cycle coordinates touching it and `n_b=|I_b|`.

Let `r` be the number of rank-two empty blocks. Let `z` be the number of rank-one empty blocks with `n_b=2`. The preceding cap gives, for `e=9`,

`z >= r+1` and `z<=3`.

## 1. Three weight-two empty lines are impossible

Suppose `z=3`. The three rank-one empty spaces with `n_b=2` are distinct lines with pairwise disjoint two-coordinate supports. They are therefore a basis of the three-dimensional space `P`.

Any other rank-one empty space is another line in `P`. Its nonzero vector is a linear combination of that basis. Because the three basis supports are disjoint, there is no cancellation between them: the support of the combination is the union of the two-coordinate supports whose coefficients are nonzero. Since the line is not one of the three `n_b=2` lines, its support has size at least four.

Thus the six singleton blocks contribute at least `6`, the three weight-two empty blocks contribute `6`, every rank-two empty contributes at least `4`, and every other rank-one empty contributes at least `4`. With `e=9`,

`sum_b n_b >= 6 + 6 + 4r + 4(9-r-3) = 36`,

contradicting `sum_b n_b=32`. Hence `z<=2`, and therefore `r<=1`.

## 2. The case r=1 is impossible

If `r=1`, then `z>=r+1` and `z<=2`, so `z=2`. The incidence inequality from the preceding cap is then an equality:

`32 >= 6 + 3e + r - z = 32`.

Consequently all six singleton blocks have incidence one, the unique rank-two empty block has incidence four, the two weight-two rank-one empties have incidence two, the other six rank-one empties have incidence three, and there is no touched complete block.

The rank-two empty block lies in a tetrahedral support of multiplicity at least two. Every one of the four triangular faces of that repeated tetrahedron is touched at least twice. None can be a singleton, because all singleton incidences equal one; none can be complete, because no touched complete block exists. Hence all four faces are actual-empty blocks. But every empty face of a repeated tetrahedral support is rank two. This gives at least four rank-two empty blocks, contradicting `r=1`.

Therefore `r=0`.

## 3. With r=0 all eight tetrahedral supports are distinct

Now `z` is either one or two. The incidence lower bound is

`sum_b n_b >= 6 + 27 - z`,

so the available slack above the lower bound is `z-1`, at most one.

If a tetrahedral support occurred with multiplicity at least two, none of its four triangular faces could be empty, because `r=0`. Those four distinct touched faces would therefore have to be singleton or complete blocks. Each has incidence at least two. Relative to the lower-bound count, a singleton face of incidence at least two costs at least one unit of slack, while a touched complete face costs at least two because complete blocks were omitted entirely from the lower bound. Four faces therefore require at least four units of slack, impossible.

Thus the eight external cycles have eight distinct tetrahedral supports.

## 4. Distinct-support collision count

Set

`C = sum_b binom(n_b,2)`.

With `r=0`, the `z` weight-two empty blocks contribute `z`, and each of the other `9-z` empty blocks has incidence at least three and contributes at least three. Singleton and complete blocks can only increase `C`. Hence

`C >= z + 3(9-z) = 27-2z >= 23`.

Because the eight tetrahedral supports are distinct, two external cycles contribute to `C` exactly when their distinct 4-subsets of the seven vertices share a triangular face, equivalently when their intersection has size three. Distinct tetrahedra share at most one triangular face. Therefore `C` is exactly the number of intersection-three pairs among the eight supports.

The companion exact verifier proves the finite Johnson-graph lemma:

> Any eight distinct 4-subsets of a seven-element set contain at most 19 pairs whose intersection has size three.

The verifier is small. If the induced maximum degree is at most four, the handshake lemma gives at most 16 edges. Otherwise choose a maximum-degree support and use `S_7` transitivity to fix it. It has 12 intersection-three neighbors and 22 nonneighbors. For center degree `d=5,6,7`, the verifier exhausts

`C(12,d) C(22,7-d)`

choices, 204072 cases in total. The exact maxima are 19 for each of `d=5,6,7`. The verifier was executed successfully in this run.

This contradicts `C>=23`. Hence `e=9` is empty.

## Result

The final `p=6` branch is now reduced from `e in {7,8,9}` to

`e in {7,8}`.

Sections 1-3 and the reduction `C>=23` are proof-level. The only computational component is the finite 204072-case Johnson-graph lemma, performed with exact set intersections and integer edge counts. No phase enumeration, modular rank, floating point, or external relation-rank computation is used.
