> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-harmonic-cell-face-floor-source-bridge.md) · source SHA-256 `09bec68e4d093eb028eb911daeb886f604e59d37b854633973aee2e371af0d79`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C harmonic cells, face-tail access, and the surviving endpoint

**Status:** The core harmonic-cell, Type-II grid-access, face-tail multiplicity,
proper-cap, and separate-face floor claims named below are canonical in the
destination theorem-state. The imported source reports preserve their full
proof lineage and finite checks. A separate full-cell/common-grid linkage
variant remains an unreviewed candidate. C-II and Level I remain open.

## Canonical results and their exact limits

Audit.173 promotes `C-UNIFORM-HARMONIC-CELL-AREA`,
`C-TYPEII-LOCAL-COHERENT-GRID-ACCESS`,
`C-TYPEII-ACTUAL-DIAMETER-GRID-ACCESS`,
`C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY`, and
`C-TYPEII-ATTACHMENT-COHERENT-PROPER-CAP`. Read their exact scopes and
conclusions in the [theorem-state manifest](../../../../docs/state/theorem-state.yaml)
and the linked [Audit.173](../../audits/target_c_uniform_harmonic_cells_global_diameter_access_independent_audit_2026-10-08.md)
and [Audit.173 supplement](../../audits/target_c_typeii_face_tail_port_multiplicity_independent_audit_2026-10-08.md).
The three original reports are preserved at
[uniform harmonic cells](../../reports/target_c_uniform_harmonic_cells_global_diameter_access_2026-10-08.md),
[face-tail port multiplicity](../../reports/target_c_typeii_face_tail_port_multiplicity_2026-10-08.md),
and [terminal cancellation](../../reports/target_c_typeii_terminal_cancellation_face_floor_2026-10-08.md).
Their older source-side `unreviewed` labels describe those report versions;
they do not override the destination theorem-state.

Audit.174 promotes `C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR` for the full-core
Type-II near-disk branch. Its canonical conclusion is

```math
\liminf (f-k)/D\ge 6s_2/5,\qquad
\liminf (q-k)/D\ge \pi/2+3s_2/5>2\pi/3,
\quad s_2=\sqrt{\pi/(2\sqrt3)}.
```

This removes the positive one-cell collar range in that branch. The source
report's FC1--FC3 are weaker intermediate floors; its separate-face FC9--FC10
refinement is the result promoted in
[Audit.174](../../audits/target_c_typeii_terminal_cancellation_face_floor_independent_audit_2026-10-08.md).
Neither the canonical floor nor the grid-access results prove a finite move,
stress-mass bound, source-cardinality restoration, or C-II closure. The
high-$`(q-k)/D`$ Type-II range and the macroscopic inactive-container branch
remain open.

## Preserved source proof and computation

The [uniform-cell checker](../../../../research/verify_target_c_uniform_cells_diameter_access_2026_10_08.py)
replays the finite star, circle, fan, direction-separation, and weighted
incidence controls. The [face-tail checker](../../../../research/verify_target_c_face_tail_port_multiplicity_2026_10_08.py)
replays the exact convex-body, port, flatness, strip, and prescribed-port
triangle controls. The [terminal-cancellation checker](../../../../research/verify_target_c_terminal_cancellation_interior_2026_10_08.py)
checks the finite face and terminal identities in the preserved proof. The
three source Audit.173/174 files are already byte-identical destination
artifacts; the import adds the reports and the two missing scripts rather than
copying duplicate audit files.

The terminal-cancellation report also cites a Target B candidate. Its full
source-only report is retained at
[Target B terminal cancellation](../../reports/target_b_terminal_cancellation_boundary_graph_2026-10-08.md).
That report comes from source commit
`12f6833725f281ce39a6d04ebcb45630b3a6768f`, is absent from frozen source main,
and is not an ancestor of it. It records the unreviewed candidate
$`s\le 1-y`$, improving a separate-end estimate $`s\le 1-y/2`$, and the
conditional consequences
$`\liminf T/D,\liminf q/D,\liminf(T-q)/D\ge A`$, where
$`A=\sqrt{2\pi/\sqrt3}`$. The required blocker-rank bound and equality-kernel
exclusion are not proved. Its finite checker is already an exact destination
copy. This is related cross-target research, not a premise of the canonical
Target C face-floor theorem.

## Unreviewed full-cell linkage variant

The [2026-10-15 full-cell report](../../reports/target_c_full_cell_common_grid_preservation_2026-10-15.md)
and its [finite composition checker](../../../../research/verify_full_cell_linkage_composition_2026_10_15.py)
preserve a source-main variant of the PR #950 grid-linkage program. It gives
three useful scoped pieces:

1. By the fixed-port route estimate and the single global augmented-face
   budget, every actual attachment $`a`$ in an unloaded component can reach
   every $`z`$ in that component by an actual contact path of length at most
   $`(4/\sqrt3+30\pi)D`$.
2. In Type II, a quadratic-area cell and the $`o(D^2)`$ cell deficit leave a
   quadratic coherent interior region from which a complete grid can be
   selected without cropping away the source cell.
3. For the connected actual grid graph $`X`$, the endpoint-inclusive cut
   argument gives $`\operatorname{diam}(X)\le5|S|`$ for every attachment-to-grid
   vertex cut $`S`$, hence at least $`\operatorname{diam}(X)/5`$ distinct-endpoint
   attachment-to-grid paths.

Its finite composition lemma is also useful. If $`P,T`$ are terminal sets
that may overlap, $`A`$ is disjoint from both with $`|A|=N`$, and there are
vertex-disjoint path families of sizes $`r`$ from $`P`$ to $`A`$ and $`s`$
from $`A`$ to $`T`$, then
```math
\lambda(P,T)\ge\max\{0,\lceil(r+s-N)/2\rceil\}.
```
The checker exhausts all 40,000 path-family assignments on the 64 four-label
graphs, compares 16,384 systems against independent path-packing and cut
enumeration, and checks the seven-label sharp contact fixture. These finite
checks do not establish the analytic canonical inputs or global optimality.

The missing C-II step is a linear-margin upper bound on the number of actual
attachment labels, such as
$`|A_I|<(\kappa_I+\gamma/5)D`$, or a direct common-label linkage that makes
the two path families overlap. Separate linear path counts do not imply
endpoint overlap. The report proves no face payment, compatible motion,
same-cardinality restoration, or strict-$`D`$ competitor. It is unreviewed in
the destination; the source audit language is provenance, not an exact-head
destination audit.

The machine-readable [candidate registry](../../../../docs/targets/target-c/candidate-registry.json)
links this candidate to the PR #950 linkage route and its exact next obligation.
The active [face-coupled-move task](../../../tasks/target-c-face-coupled-move.md)
and [Type-II stress-mass task](../../../tasks/target-c-typeii-stress-mass-access.md)
now point here. Before proposing another route, keep every source point and
isolate, preserve all lower and actual-diameter upper pair constraints, and
produce a source-realized finite endpoint or strict sub-$`D`$ competitor.

## Exact local commands

```sh
python3 research/verify_full_cell_linkage_composition_2026_10_15.py
python3 research/verify_target_c_face_tail_port_multiplicity_2026_10_08.py
python3 research/verify_target_c_uniform_cells_diameter_access_2026_10_08.py
python3 research/verify_target_c_terminal_cancellation_interior_2026_10_08.py
python3 research/verify_target_b_terminal_cancellation_2026_10_08.py
```

The source and destination hashes, transformations, historical source commit,
duplicates, and check results are recorded in the [migration ledger](../../../../docs/research/migration/2026-10-16/ledger/source-main-artifacts.jsonl),
[file ledger](../../../../docs/research/migration/2026-10-16/ledger/source-main-files.jsonl),
[dependency ledger](../../../../docs/research/migration/2026-10-16/ledger/source-main-dependencies.jsonl),
and [local verification receipt](../../../../docs/research/migration/2026-10-16/receipts/target-c-source-main-typeii-harmonic-verification.json).
