> Generated reading edition · [exact source](../../../docs/reports/target_c_train_track_crossroute_audit_2026-08-31.md) · source SHA-256 `4695448c248788b02ffc6182d17b35c0283b4d5c12f6849b4aacc85f5467cf5c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E20E37CB8D6B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C train-track cross-route audit

**Date:** 2026-08-31  
**Repository base:** `853a1b32` (main after PR #82)  
**Run type:** theorem-ledger audit / cross-route reconciliation  
**Status:** no new Level I claim

## Correction

The Target C reports labeled C77 and C78 are mathematically correct under their stated
hypotheses, but their novelty classification was too strong because the active shared
Target B stack already contains stronger train-track machinery.

In particular:

- Target B Section 24 already uses the simple triangle-free train crossing graph and
  Mantel's bound `T>=2 sqrt(R)` in the rhombic branch.
- Shared Theory Section 22, Theorem 22.3 already proves the defect-extended per-track
  span inequality
  
  ```math
  L_\tau+\frac{\sqrt3}{2}s_F(\tau)
  +\sum_{e\in\partial\tau\cap\partial_\infty}\rho_e
  \le D,
  ```

  and its summed form.
- Target B Section 24 strengthens this to the exact support-width equality
  
  ```math
  w_K(\nu_\tau)=L_\tau+d_{e_-}+d_{e_+}.
  ```

- Target B Sections 26 and 39 already develop the sixfold phase energy, macroscopic
  grain decomposition, phase-atomic/exposed-hull theorem, and the stronger pure-disk
  lower bound
  
  ```math
  \liminf T/D\ge2.5395008183\ldots .
  ```


Therefore C77-C78 must be read as **Target C imports/syntheses**, not as discoveries of
train-track pseudolines or the basic width identity.

## Genuinely new cross-route content retained

The recent Target C work still adds information not present in those older statements:

1. C75 gives a convenient explicit short-diagonal slack currency
   
   ```math
   \Sigma_{diag}=\sum_f(s_f-1)
   ```

   with a linear area/capacity coefficient.
2. Combining C75 with the already established train-span identity yields the retained
   synthesis
   
   ```math
   \sqrt3 F_4+2c_{rh}\Sigma_{diag}
   +\frac{\sqrt3}{2}b_F+H_\infty
   \le
   \sum_\tau w_K(\nu_\tau),
   ```

   in the topology where the Shared Theory Section 22 terms are defined.
3. More importantly, Target C supplies a separate KKT response route unavailable in
   the old shell argument: C66/C68/C70/C71/C72/C74 and C76 force a small-response
   survivor toward a one-dimensional mechanical/electrical stress star while the
   geometry remains two-dimensional.

The research priority is therefore to combine the mature Target B train-angle/shell
machinery with the Target C stress-star degeneration, not to re-prove train geometry.

## Updated target

The strongest cross-route question is:

> Can the C66/C76 approach to the exact straight-chain KKT face coexist with the
> macroscopic train-angle neutral/equality spaces proved in Target B Sections 39--43?

A contradiction here would attack the principal weakness of the Target B machinery:
its higher-order blockers can be supported by diameter bars whose KKT weights are not
quantitatively controlled. Target C now supplies exactly such weight concentration.

## Ledger disposition

- C77 theorem statements remain valid but are imported from / subsumed by the mature
  Target B train theory.
- C78's basic span and track-count statements remain valid but are imported from
  Shared Theory Sections 22--23 / Target B Section 24.
- The C75 diagonal-slack coupling to those identities is retained as a cross-route
  synthesis.
- No Level I closure is claimed.
