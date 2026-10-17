<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c90eb5abe2e2b620d6f90571ce380d2e6f67cfed", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_multigrain_endpoint_capacity_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b4b96a22910b83c0ef3c933b0909047eae75f359b1d26063916d49cdefde5aff"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C multi-grain endpoint-capacity lemma

Date: 2026-09-12

Lifecycle: proof-only candidate awaiting hostile audit. Theorem-state authority is
unchanged; C-II and Level I remain open.

This note closes the disconnected-phase-component gap in the proof-only Section-118
safe window. It does not claim a global C-II closure.

## Inputs

Work in the proof-only Section-118 full-core window with carrier slack at most
`0.0088`. Use the audited conservative constants

```
A_4/D^2 >= 0.4703752-o(1)
T/D     <= 1.8488+o(1)
B_bad/D <= 0.1163+o(1)
E_route/D <= 1.8693+o(1)
```

Here `A_4` is the carrier strict-rhombus area, `T` the complete train count,
`B_bad` the Section-118 bad-train capacity for one collapsed projective direction
interval, and `E_route` the principal-route endpoint budget. The total reduced-phase
defect is at most `5.317D`.

## Component pruning and phase collapse

Discard crossings with reduced-phase increment greater than `10000/D`. At most
`0.0005317D^2` crossings are discarded. Repeatedly delete train vertices of current
degree below `10^-5D`; this removes at most `0.0000185D^2` further crossings. Since
the carrier has at least `0.4703752D^2` crossings before pruning, the retained graph
has at least `0.4697D^2` crossings for large `D`.

Every retained connected component has minimum degree at least `10^-5D`. Along a
shortest graph path, vertices three steps apart have disjoint closed neighborhoods.
The train ceiling `1.8488D+o(D)` therefore bounds every component's graph diameter by
an absolute constant. Each retained edge changes reduced phase by `O(D^-1)`, so every
component has phase diameter `O(D^-1)`. Its trains occupy at most three collapsed
projective label intervals.

## Endpoint capacity across all grains

Put `K_0=3(0.1163)=0.3489`. A component with `n_i/D=x_i` trains has at most
`K_0D` bad trains, even after charging the three labels separately. Each complete
train has two physical terminal occurrences. Thus the principal-route budget gives

```
2 sum_i (x_i-K_0)_+ <= 1.8693+o(1).                 (1)
```

This remains safe when phase intervals of different components overlap, because
charging bad capacity separately only enlarges the allowed off-route population.

The retained train crossing graph is simple and bipartite (the selected crossing
edges use one unordered pair of distinct phase labels), hence each component is
triangle-free. Mantel gives `e_i <= n_i^2/4`. With
`sum_i x_i <= 1.8488`, the retained edge lower bound implies

```
S^2 + K_0 S + K_0(1.8488) - 4(0.4697) <= 0,
S := sum_i (x_i-K_0)_+.
```

The positive root satisfies `S>0.9499`, so (1) would require
`2S-1.8693>0.0305`, a contradiction.

Therefore a proof-only Section-118 safe-window full-core carrier cannot split its
quadratic train-crossing mass among multiple phase grains. The argument keeps all
source points, uses only a selected train subgraph, and makes no Euler-trail or
incident-diameter inference.

## Certificate and scope

`python3 research/target_c_multigrain_endpoint_capacity.py` checks the conservative
finite scalar margin. It certifies only the displayed pruning and Mantel arithmetic;
it does not establish the inherited carrier, the Section-118 bad-capacity theorem,
global minimum-diameter optimality, or Level I.

Classification: proved candidate awaiting hostile audit, proof-only full-core
Section-118 scope. The inactive-container branch and all full-core slack above
`0.0088` remain open.
