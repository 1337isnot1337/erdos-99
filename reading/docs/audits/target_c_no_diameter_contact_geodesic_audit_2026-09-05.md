> Generated reading edition · [exact source](../../../docs/audits/target_c_no_diameter_contact_geodesic_audit_2026-09-05.md) · source SHA-256 `657bef767fc1416dbe194d4efc1f70380d1f801c1115385c3224ea0ba2f4bc87`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-405E74C6D948","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C strict diameter contact-distance gap

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_c_no_diameter_contact_geodesic_2026-09-05.md`  
**Verdict:** PASS under the stated C65 + pure simply connected strict-rhombic hypotheses.  
**Global LEVEL I status:** STILL OPEN.

## Checks

1. **`d_C=#separating trains`.** This is C99.1 for the strict-rhombic train arrangement.

2. **Equality `d_C=D` forces a literal straight chain.** A shortest path has `D` unit edges and endpoint displacement of norm `D`; equality in the Euclidean triangle inequality forces every oriented path edge to equal the same unit vector `u`. Equivalently C99.3 gives zero train-direction defect.

3. **The path uses exactly the separator trains.** C99.1 says a shortest path crosses every separating train exactly once and no other train, so the `D` straight contacts lie on `D` distinct parallel separator tracks and exhaust the separator family.

4. **C83 does not need β=1 after geometry is supplied.** Its ordered-separator and interval proofs use only the pure-rhombic train coordinates, the pairwise disjoint parallel separator family, and the straight chain ordering. Those are recovered in items 2-3.

5. **C84 does not need β=1.** In the C65 relative-interior stress every active diameter bar has positive β. The straight chain diameter has zero train-angle gradient. Therefore restricting `sum beta_h g_h=0` to the chain tracks gives the same nowhere-zero prefix circulation.

6. **C86 connectivity does not need β=1.** C86.2 is a general consequence of the C63/C65 lexicographic normalization. Preserving all `D` chain contacts and the chain endpoint diameter under an integrated critical motion forces equality in the triangle inequality and hence one common chain angular rate.

7. **C87-C88 inputs are restored.** They need the connected prefix graph, nowhere-zero circulation, hull-arc order, and diameter-thrackle geometry. No β=1 coefficient is used in the paired-orientation/staircase argument once the exact chain atom exists.

8. **C97 terminal twist uses geometry/full support, not the β=1 face.** Internal chain vertices are nonextreme points in the relative interior of `za`, hence are not diameter endpoints in the C65 source. Positive contact equilibrium and triangle-freeness give the degree-four side neighbors. The monotone-row and terminal-boundary arguments then produce `U_0={z}` and `L_D={a}`. C88's `{0,D}` edge and C87's reverse orientation force `za` to act as a non-chain transverse representative, impossible because its transverse coefficient is zero.

9. **Integer conclusion is stated correctly.** Since `d_C` is an integer and `d_C>D`, one has `d_C>=floor(D)+1`. If `D` is nonintegral this equals `ceil(D)` and gives no extra integer beyond the trivial Euclidean lower bound; if `D` is integral it gives `D+1`.

## Scope warning

The proof is not valid outside the pure simply connected strict-rhombic train model. In particular it does not establish `d_C>D` for arbitrary C-II contact topology. The quantitative benefit can vanish when `D` approaches the next lower integer, so no uniform `Omega(1)` additive contact-distance gap is obtained.