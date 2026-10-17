> Generated reading edition · [exact source](../../../docs/audits/target_c_quadratic_core_cap_extraction_independent_audit_2026-10-09.md) · source SHA-256 `3b3c3554321dcca88eb5510b4080ba20e70a5c9ba57226dee2c42a6569c0f4c0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FFB06BA281F9","canonical":true,"claim_ids":["C-QUADRATIC-CORE-CELL-BOUNDARY-STRIP-POPULATION","C-QUADRATIC-CORE-DEEP-CAP-GRID-RETURNS","C-QUADRATIC-CORE-LOADED-CHORD-CAP-EXTRACTION"],"claim_statuses":{"C-QUADRATIC-CORE-CELL-BOUNDARY-STRIP-POPULATION":"canonical","C-QUADRATIC-CORE-DEEP-CAP-GRID-RETURNS":"canonical","C-QUADRATIC-CORE-LOADED-CHORD-CAP-EXTRACTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.189 — quadratic-core cap extraction and deep returns

**Date:** 2026-10-09  
**Audit base:** `origin/main=1503e109c53d2ffb0dac6b83fc6cd5d22248bb0f`, state `2026-10-09.audit.183`  
**Frozen source:** `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`  
**Source report:** `docs/reports/target_c_quadratic_core_cap_extraction_deep_returns_2026-10-08.md`, SHA-256 `35cedb4005ef51cf38b12ee1fc672b33a7a7f4ee428a93758b1f4376fa2cead3`  
**Source verifier:** `research/verify_target_c_cap_crop_return_suffix_2026_10_08.py`, SHA-256 `d1846b155a775ea6351b27757c97c32c95141d1313d008c4e95e675a31a4babd`  
**Verdict:** PASS — promote the cap extraction, deep cropped-grid returns, and whole-cell boundary-strip population at the scopes below. The report's Type-II uniform near-port grid is already subsumed by Audit.173 and receives no duplicate ID.

## Exact scope and claims

Work along an unbounded canonical contact-minimal then actual-diameter-pair-minimal triangle-free C-II sequence in the quadratic positive-contact-core branch, with `D -> infinity`. Retain every source label, including contact isolates. Fix `epsilon in (0,pi/6)` and use the Section-78 coherent physical grain in one unloaded positive-contact component `I`, with attachment set `A`, cell `P=conv(A)`, area `A_0 >= rD^2`, and physical perimeter `O(D)` for a fixed `r>0`.

The audited extraction gives a proper loaded-hull chord cap `C` selected from this same `A`, and an epsilon-coherent subgrain `G` in `I intersect int(P) intersect int(C)` with area `A_G >= alpha D^2` and perimeter `O(D)`, for a fixed `alpha>0`. If `eta` is signed unit-normal height above the chord and `H=max_{a in A} eta(a)`, an actual attachment `a_*` attains `H >= A_G/D >= alpha D`.

For `h=A_G/(8*pi*D)`, `s=A_G/(4D)`, and `W=C_{-h} intersect {eta <= H-s}`, a further coherent grain crop still has quadratic area and perimeter `O(D)`. Section 73 therefore gives a complete physical train grid in `W` with both shores of size `Omega(D)`. Applying the promoted Audit.133 loaded-return theorem to its `uv=Omega(D^2)` crossing rhombi gives `p=Omega(D)` pairwise vertex-disjoint actual contact paths to distinct vertices of `A`. Trimming each path after its last source vertex in `W` leaves at least `ceil(h)-1` distinct internal vertices in `I minus W`; in total, `Omega(D^2)` distinct source vertices lie outside the entire cropped region. Every grid vertex is also at distance at least `s=Omega(D)` from `a_*`.

The separate whole-cell variant uses `h_0=A_0/(8*pi*D)` and `W_0=P_{-h_0}`. It gives `Omega(D^2)` distinct vertices of the same component in the boundary strip `{x in I: dist(x,partial P)<h_0}`.

## Independent reconstruction

1. **Strict harmonic trapping.** At an unloaded vertex, positive contact equilibrium expresses its position as a strictly positive convex combination of contact neighbors. If a supporting functional of `P` attained its maximum at such a vertex, equality forces every neighbor to attain that maximum. Propagating through the connected component reaches all of `A`, contradicting the canonical noncollinearity of `A`. Thus `I subset int(P)`, and every closed grain face lies in `int(P)`.
2. **A proper cap with quadratic coherent mass.** Since `q>=ceil(D)`, eventually `q>=4`; among three distinct attachments in `A`, some pair is nonconsecutive on the full loaded hull. Their line cuts a proper cap and meets the full convex hull only in their chord. Choose the side containing at least half of `G_0`. A unit rhombus meeting the chord lies in its radius-two tube, whose area is at most `4D+4*pi`; disjoint face interiors and the minimum rhombus area `a_0=sqrt(3)/2` bound the number of deleted faces by `(4D+4*pi)/a_0=O(D)`. The surviving selected-side area is at least `A_0/2-O(D)`, and deleting those faces adds at most four unit boundary edges per face. Hence total surviving perimeter is `O(D)`. If the surviving edge-components have areas `A_j` and perimeters `P_j`, isoperimetry gives `sum sqrt(A_j)<=sum P_j/(2sqrt(pi))`; one component therefore has area `Omega(D^2)` and perimeter `O(D)`.
3. **Port height.** Let `a_*` maximize `eta` on `A`. The selected grain lies in `P intersect C`, with heights between zero and `H=eta(a_*)`. Every horizontal section of the diameter-`D` hull has length at most `D`, so `A_G<=DH`. Positive area gives `H>0`, and `a_*` is an actual attachment on the selected hull arc.
4. **Deep crop and grid.** The cap-boundary loss is at most `pi D(h+2)=A_G/8+O(D)`; the upper-height loss is at most `D(s+2)=A_G/4+O(D)`. Thus at least half the grain area survives eventually. Every removed face exposing new retained boundary meets `partial W` and lies in its radius-two tube. Since `W` is convex with perimeter at most `pi D`, the tube has area `O(D)`, so the sum of retained component perimeters remains `O(D)`. Isoperimetry again yields a quadratic component, to which the canonical Section-73 grid theorem applies.
5. **Actual returns and suffix count.** The grid contributes `uv=Omega(D^2)` distinct actual strict-rhombus faces in `I`. Audit.133's `p>=ceil(F(uv))`, `F(R)=(sqrt(25+4cR)-5)/(2c)`, `c=8*pi/sqrt(3)`, gives `p=Omega(D)` vertex-disjoint paths to distinct actual loaded attachments. A last visit to `W` is at least distance `h` from every loaded endpoint, all of which are outside `int(C)`. Unit contact edges force at least `ceil(h)` edges in the suffix, hence `ceil(h)-1` internal source vertices outside `W`. Vertex-disjointness preserves distinctness across all suffixes. Replacing `C` by `P` and omitting the height cut gives the boundary-strip variant; every attachment is an extreme point of `P`, so each path suffix stays in `I` and lies outside `P_{-h_0}`.

## Hostile scope and proof boundaries

- Face deletion changes only the auxiliary grain complex. It deletes no source label and changes no contact. All source contact isolates remain in the full configuration.
- The cap, chord, port, and grid are selected from the same actual harmonic attachment cell. This does not validate a separately prescribed cap or port.
- The return endpoints are actual loaded diameter endpoints and the paths use actual source contacts. The artificial boundary terminals in the finite verifier are not treated as loaded endpoints.
- The `Omega(D^2)` count is source population outside a crop, not exchange capacity, a vacancy, or a source move. The crop boundary strip can itself have quadratic population; no contradiction follows.
- The Type-II near-port uniform grid claim in source Section 6 is already covered by canonical `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` / Audit.173 and is not promoted again.
- The finite verifier uses exact rational arithmetic on three nonglobal fixtures. It checks source pairs, contacts, cap/cell crops, physical grids, integral path flows, and last-crop-visit suffixes. It does not prove the analytic area/perimeter extraction, canonical source hypotheses, stress, or global optimality. Re-run on the frozen source snapshot: 829,032 source-pair checks, 1,856 rhombi, 210 chord-crossing-face checks, 823 cap rhombi, and 36 disjoint actual-contact returns; the three fixtures retain 80 distinct suffix vertices in total.

## Dependencies and disposition

- Promote `C-QUADRATIC-CORE-LOADED-CHORD-CAP-EXTRACTION`, depending on `C-HARMONIC-CARRIER-QUAD`, `C-LOADED-HULL`, and `C-ZRF`.
- Promote `C-QUADRATIC-CORE-DEEP-CAP-GRID-RETURNS`, depending on the cap extraction, `C-PSEUDO-GRID`, and `C-RHOMBUS-BULK-LOADED-RETURN-BOUND`.
- Promote `C-QUADRATIC-CORE-CELL-BOUNDARY-STRIP-POPULATION`, depending on `C-HARMONIC-CARRIER-QUAD`, `C-PSEUDO-GRID`, and `C-RHOMBUS-BULK-LOADED-RETURN-BOUND`.
- Do not add an ID for the report's Section-6 near-port grid; it is already canonical at a more directly uniform attachment scope.

The current C-II finite-move/payment obligation is unchanged. The quadratic-core branch now has an extracted actual loaded-chord cap and many deep returns, but no payment against the global population/phase budget and no full-source strict-`D` competitor. C-II and Level I remain open.
