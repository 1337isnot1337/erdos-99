> Generated reading edition · [exact source](../../../docs/audits/target_c_cap_local_harmonic_grid_independent_audit_2026-10-08.md) · source SHA-256 `4a6241d3e70412001e7a73fb12f8d9173c1443a3a468020932ef16799b29bdac`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1A3935193E82","canonical":false,"claim_ids":["C-TYPEII-CAP-LOCAL-HARMONIC-GRID"],"claim_statuses":{"C-TYPEII-CAP-LOCAL-HARMONIC-GRID":"audited-working"},"index":"docs/state/artifact-index.jsonl","status":"audited-working","target":"target-c"} -->
# Target C Audit.157 — a fixed-area loaded cap contains a harmonic grid

**Date:** 2026-10-08

**Audit base:** `origin/main=53a205638307720107a532673e475ad779d80178`, state `2026-10-08.audit.153`.

**Frozen source:** `origin/research/sol-c2-deep-port-route-20261004` at `a2ccd6161519c7d27482a7c6e751cd44e595e1b6`, open PR #668.

**Source report:** `research/target_c_open_cell_host_cap_harmonic_localization_2026-10-04.md`, blob `6c10493743b03602830e639e2bde4e01382596f5`, SHA-256 `307e8acdf0ca444ac1c000c90df2920d1b2b2f658cc7e979c97962716eb15a4f`.

## Exact conditional statement

Consider a selected canonical post-ZF Target C sequence in the Type-II branch, with actual source diameter `D` tending to infinity and all source points retained. Fix `epsilon` in `(0,pi/6)`. Assume there is a fixed `alpha>0` and a set `Q_*` of actual loaded diameter endpoints such that

```text
C_* = conv(Q_*) is contained in the canonical force hull F,
area(C_*) >= alpha D^2
```

for all sufficiently large members of the sequence. The set `Q_*` need not be produced by a staircase theorem for this conditional statement.

Then there is an epsilon-coherent finite strict-rhombus subgrain `G_*` such that

```text
G_* is contained in int(C_*) intersect P_*,
P_* = conv(A_*) for one unloaded positive-contact component I_*,
number_of_rhombi(G_*) = Omega_{alpha,epsilon}(D^2),
physical_perimeter(G_*) = O_epsilon(D).
```

The same subgrain contains a complete phase-pure train grid with both shores `Omega_{alpha,epsilon}(D)`. Its grid rhombi lie in `C_* intersect P_*`, and `diam(P_*)=Omega_{alpha,epsilon}(D)`. This is a conditional cap-localization theorem, not an assertion that every canonical source has such a cap.

## Independent reconstruction

Every point of `Q_*` is a vertex of the force hull `F`. If a different loaded force-hull vertex lay in `int(C_*)`, it would be a nontrivial convex combination of points of `Q_*`, contradicting extremality. Hence `B intersect int(C_*)` is empty, where `B` is the full loaded endpoint set.

In the canonical Type-II branch, coherent strict source-rhombus grains cover all but `o(D^2)` area of `F`, and their total physical perimeter is `O_epsilon(D)`. Since `C_* subset F` has area at least `alpha D^2`, the coherent rhombi in `C_*` have total area at least `alpha D^2-o(D^2)`.

Each strict unit rhombus has diameter less than two, area in `[sqrt(3)/2,1]`, and disjoint interior from every other contact face. A rhombus meeting `partial(C_*)` is contained in the two-neighborhood of that boundary. For a convex body of perimeter `P`, the outer width-two strip has area `2P+4pi`, and the inner width-two strip has area at most `2P`; since `perimeter(C_*)<=pi D`, the full boundary neighborhood has area at most `4pi(D+1)`. Therefore only `O(D)` rhombi meet the cap boundary, and deleting them loses only `O(D)` area.

Partition the remaining rhombi into edge-connected components **within each parent coherent grain**, so no two phase frames are combined. Deleting one rhombus exposes at most four unit boundary edges; the sum of component perimeters is therefore at most the parent-grain perimeter budget plus `O(D)`, hence `O_epsilon(D)`. The components wholly inside `int(C_*)` retain `Omega(D^2)` total rhombi. If their counts and physical perimeters are `R_j,P_j`, planar isoperimetry gives `P_j>=2 sqrt(pi (sqrt(3)/2) R_j)`. Thus `sum sqrt(R_j)=O_epsilon(D)`, and

```text
sum R_j <= sqrt(max_j R_j) sum sqrt(R_j)
```

forces one component with `Omega_{alpha,epsilon}(D^2)` rhombi. Its perimeter is at most the total component perimeter, and it inherits one parent grain's phase frame.

All vertices of this component lie in `int(C_*)`, so none is loaded. Its actual unit-contact edges place all its vertices in one connected component `I_*` of the unloaded positive-contact graph. Harmonic trapping puts those vertices in `P_*=conv(A_*)`; convexity then contains every rhombus. The grain area is `Omega(D^2)`, so `area(P_*)=Omega(D^2)` and the isodiametric inequality gives `diam(P_*)=Omega(D)`.

For the grid, the coherent component has `Omega(D^2)` rhombi and `O_epsilon(D)` perimeter. The canonical train count identity gives `O_epsilon(D)` local trains; canonical phase-pure pseudosegment extraction then yields two all-crossing shores of size `Omega(D)`. Applying the canonical hole-stable endpoint projection inside `C_*` and `P_*` is valid because both convex sets contain every product-grid rhombus. The global angular-defect budget is `O(D)`, so division by a shore size `Omega(D)` leaves an `O_epsilon(1)` error. This gives the stated cap-local grid and macroscopic cell diameter.

## Hostile scope checks

- The components are partitioned separately inside each parent coherent grain; no coherence is inferred across different phase bins.
- The proof removes only `O(D)` rhombus faces from the analytic covering argument. It deletes no source point and moves no label. Contact-isolated points remain in the original configuration.
- `C_*` is the convex hull of actual loaded endpoints, not a virtual chart or a replacement container. The result uses its fixed quadratic area as a premise.
- The separate claim that a strong-SCC staircase supplies this fixed-area endpoint cap is not promoted here; it is not a canonical theorem-state entry. Type I is also not part of this theorem.
- The cap-local grain and grid do not by themselves supply a route to the staircase endpoints, a paid multiplicity bound, a source-preserving move, a strict sub-`D` competitor, or Level I.

## Verifier boundary and disposition

The source report has no verifier or computation. The argument above is analytic and uses the canonical Type-II area coverage, coherent-grain perimeter bound, harmonic trapping, phase-pure grid extraction, and hole-stable endpoint projection. No finite check is claimed to prove these asymptotic steps.

**Verdict: PASS WITH NARROWED CONDITIONAL SCOPE.** Record `C-TYPEII-CAP-LOCAL-HARMONIC-GRID` as audited-working under the fixed-area loaded-endpoint-cap premise and canonical Type-II inputs. Do not promote the staircase cap extraction or its Type-I/Type-II fork. The cap-localization result does not change the canonical C-II endpoint; a finite source-preserving move or exact global contradiction remains open.
