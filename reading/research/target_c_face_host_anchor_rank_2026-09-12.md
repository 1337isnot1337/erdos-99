> Generated reading edition · [exact source](../../research/target_c_face_host_anchor_rank_2026-09-12.md) · source SHA-256 `55a98fb7705bebec614f069d216f0dc4a61000d353706556eb34db2aaa44ce09`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "42190dddc10644e8bf4fec0cc9f6056d05105ff8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_face_host_anchor_rank_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "87485c5ec9d8b9d236595217c0772edc03d5262670de8081ae57486ce8a7b65d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — defect-face components require outer directional anchoring

**Date:** 2026-09-12
**Status:** audited-working proof-only structural reduction; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The exceptional-face closure matrix has a finite dual obstruction. Let `C_face` be
the two-coordinate train-closure matrix on the connected nonisolated positive-contact
core, and let `K_1,...,K_m` be the connected components of the graph whose vertices
are bounded nonquadrilateral faces and whose edges join faces sharing a train. For
each component `K_j`, let `r_j` be the dimension of the span of the projective train
directions of all train ends from `K_j` that terminate on the outer face. Then

```math
\boxed{\sum_{j=1}^m(2-r_j)\le
\dim\ker(C_{\rm face}^{\mathsf T})
=2f-\operatorname{rank}C_{\rm face}
=\sigma_C\le s_Z.}
\tag{HA.1}
```

Here `sigma_C` is the pure-contact self-stress dimension and `s_Z` is the mixed
rigidity surplus. Thus a bounded-face component with no outer directional anchor
costs two dimensions of `s_Z`; a component with only one projective anchor costs one.

## 1. Component dual vectors

Write the closure matrix in two-coordinate blocks. A train joining two distinct
bounded-face components contributes opposite blocks to its two incident faces, while
a train joining a bounded-face component to the outer face contributes one block
whose vector is its oriented unit direction. A bridge occurring twice on one bounded
face contributes opposite occurrences and hence zero to the outer-anchor span; it is
not an artificial anchor.

For a fixed component `K_j`, assign one vector `z` to every face block in `K_j` and
zero to all other face blocks. The contributions of internal train columns cancel.
The remaining transpose equations require `z` to be orthogonal to the span of the
outer-anchor vectors. Their solution space has dimension `2-r_j`. Different
components use disjoint face blocks, so these subspaces are linearly independent.
This proves the first inequality in (HA.1), including occurrence signs.

## 2. Exact corank and mixed surplus

The audited exceptional-face closure identity gives

```math
2f-\operatorname{rank}C_{\rm face}=\sigma_C.
```

Canonical mixed rigidity has signed stress-space dimension `s_Z+1`. Every pure
contact self-stress extends by zero on the diameter rows, and the normalized KKT
stress has a nonzero diameter part. Therefore `sigma_C+1<=s_Z+1`, proving the final
inequality in (HA.1).

## 3. Scope and remaining obstruction

The statement applies to the full connected nonisolated contact core, with all
boundary occurrences retained. The audited train-loop exclusion is used to remove
nontrivial same-bounded-face returns; no scalar ledger is substituted for that
exclusion. Contact-isolated source points remain in the full source and are not
inserted into any rigidity matrix.

The exact rank statement does not give a quantitative angular lower bound: two outer
anchors may be arbitrarily close to collinear while still having rank two. A closing
theorem must turn near-collinearity into a quantitative source-preserving descent,
an exact row dependency, or a contradiction with the diameter/train geometry.

**Classification:** audited-working proof-only candidate. C-II remains open.
