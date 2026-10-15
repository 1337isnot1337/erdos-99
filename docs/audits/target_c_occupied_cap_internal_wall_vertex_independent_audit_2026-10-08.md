<!-- theorem-state: {"artifact_id":"ART-ABA5FBC1686A","canonical":true,"claim_ids":["C-EXTERIOR-OCCUPIED-CAP-INTERNAL-WALL-VERTEX"],"claim_statuses":{"C-EXTERIOR-OCCUPIED-CAP-INTERNAL-WALL-VERTEX":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.160 — internal contact vertex in every occupied cap cell

**Date:** 2026-10-08  
**Audit base:** `origin/main=6e8dc144e2a0c268d261a43f298a47524c22b7f1`, state `2026-10-08.audit.155`  
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5` (no open PR)  
**Source artifact:** `docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md`, Git blob `f2d88f0598fa86bfc59c392cff8091955a0b05c0`, SHA-256 `601865a16cd7c444696606e9cca2b09a47c494448d7aa050152baa3bad38a484`  
**Audited unit:** only the unpromoted occupied-cap/internal-wall-vertex extraction at source lines 204–214. The other independent modules in this report were previously audited in Audits.140–143; this report does not reopen them.

## Candidate chain

```text
occupied actual loaded-hull cap
  -> its hull-augmented cell has a unit-contact path between the cap-base endpoints
  -> the occupied-cap closing chord is nonunit, so that path has an internal vertex
  -> Audit.140 gives exact strict packet capacity |S_Q| after omitting that one guard
  -> the fixed-cell strict |S_Q|+1 refill route is impossible
```

This narrows one proposed refill route. It does not produce a source-preserving move, refill, strict sub-`D` competitor, or Level I conclusion.

## Exact statement

Let `A` be a canonical Target C-II source in contact-minimal, then actual-diameter-pair-minimal normal form, with diameter `D>=9`; retain every source point, including contact isolates. Let `B` be the actual loaded diameter endpoints, `F=conv(B)`, and `K=conv(A)`. Let `C` be an occupied actual exterior cap of `F`, with distinct base endpoints `a,b` consecutive on the loaded-hull boundary and an actual source point strictly across its closing chord `ab` from the diameter partners. Let `Q` be the hull-augmented face cell corresponding to that cap. By `C-EXTERIOR-HULL-AUGMENTED-CELLS`, its boundary consists of the cap's full source-hull arc from `a` to `b` and a simple path `P` from `b` to `a` of actual unit-contact edges.

Then `P` has at least two edges, so it has an internal vertex `v` whose two incident `Q` sides are actual unit contacts. Consequently the exact one-guard capacity theorem `C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY` applies to `Q,v`: with `S_Q` the complete set of source labels in `Q` off the unit-contact path,

\[
\operatorname{Pack}_1\{x\in\operatorname{int}(Q):|x-w|>1\text{ for every path vertex }w\ne v\}=|S_Q|.
\]

In particular, no fixed-cell strict packet of size `|S_Q|+1` can replace `S_Q` and `v` after omitting only that internal guard. All labels on the cap's source-hull arc remain included in `S_Q`.

## Independent proof

The canonical hull-augmentation theorem gives a simple actual-unit-contact path `P` between the loaded endpoints `b` and `a` for the face cell associated with the cap. The endpoints are distinct, so `P` is not a zero-edge path.

The canonical occupied-cap chord threshold `C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD` gives

\[
|a-b|\ge \tau_D=\frac{3D}{\sqrt{3D^2+4}+1}>\frac32>1
\qquad(D\ge9).
\]

If `P` had exactly one edge, that edge would join `b` directly to `a`. Since each edge of `P` is an actual unit contact, it would give `|a-b|=1`, contradicting the occupied-cap chord bound. Hence `P` has at least two edges. Any simple path with at least two edges has an internal vertex, and both incident path edges are actual unit contacts by the definition of `P`.

Now apply Audit.140's exact one-internal-guard capacity theorem. That theorem already checks every retained source point, counts every cap-arc isolate in `S_Q`, and proves the equality above. Therefore the proposed one-extra-site strict packet is impossible in every occupied cap cell. This proof uses no equilibrium or loaded-only-stress-cycle argument; it depends only on the canonical cell structure and occupied-cap chord threshold.

## Hostile scope checks

- **Occupied cap is essential.** A cap arc-length or area bound alone does not make its closing chord nonunit. The source point on the opposite side and actual diameter partners are part of the hypothesis of `C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD`.
- **The cell is the actual hull-augmented cell.** The simple path conclusion does not apply to an artificial interior chord or an arbitrary partial wall. Audit.143's retained-isolate regression remains binding for an interior nonunit side.
- **The path edges are actual contacts.** A geometric curve or scaffold path from `a` to `b` is insufficient.
- **Only one guard is omitted.** This does not extend to two deleted wall vertices; the retained-isolate two-deletion regression remains binding.
- **No moved-wall or multi-cell inference.** The capacity theorem is for one fixed cell. Shared tips, cross-cell compatibility, exact-contact packets, and moved-core refill remain separate obligations.
- **No cap extraction.** The statement applies to an actual occupied cap already present in the canonical source; it does not assert that a macroscopic cap exists or can be selected from another regime.

## Dependencies and verifier boundary

Canonical dependencies are `C-EXTERIOR-HULL-AUGMENTED-CELLS`, `C-LOADED-EXTERIOR-CAP-CHORD-THRESHOLD`, and `C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY`. Their exact scopes were checked in the current theorem manifest and their independent audit reports. The source report's exact rectangle-plus-isolate regression is already separately audited at Audit.143; no script is needed for this finite path-length implication. This proof does not treat a certificate as evidence for an analytic step.

## Verdict and disposition

**PASS — promote `C-EXTERIOR-OCCUPIED-CAP-INTERNAL-WALL-VERTEX` at the exact occupied-cap/canonical-cell scope above.** This repairs Audit.140's explicitly withheld macroscopic-cell vertex extraction by using a shorter independent implication from already canonical results. Together with Audit.140, it closes the fixed-cell strict one-extra-site packet route in every occupied actual exterior cap cell.

The exterior-cap branch still needs a capacity/refill mechanism that moves walls, coordinates compatible packets across multiple cells, or pays exact new contacts. Target C-II and Level I remain open.
