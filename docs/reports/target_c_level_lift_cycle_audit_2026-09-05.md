<!-- theorem-state: {"artifact_id":"ART-060604C23EE2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_level_lift_cycle_audit_2026-09-05.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=016b29a6089b3ddf2070a31b41f2385a6f62b324; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdos Problem #99 — Target C C97 worklog: level-lift cycle audit

**Date:** 2026-09-05  
**Base:** `89c17412` (`main`)  
**Branch:** `research/target-c-c97-level-lift-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Immediate input

C87 gives a simple prefix tree `G_P` on levels `0,...,D` with exactly `D` edges. Every simple prefix edge `{a,b}` occurs in both physical hull-arc orientations, and every such interval crosses one common chain train `tau_r`. C96 then puts all of these selected physical diameter edges, together with the chain diameter `za`, inside one cross-cut diameter forest.

The naive quotient picture is a two-sheet lift of `G_P`: for a simple edge `{a,b}` one has physical edges of the forms `L_a U_b` and `U_a L_b`. Since the two hull arcs meet at levels `0` and `D`, identifying the two sheets at both endpoints would create two lifts of the unique `0`–`D` path and hence a cycle.

That observation is **not yet a proof**, because a prefix level can contain more than one source vertex on a hull arc. C87 is a circulation on prefix levels, not a statement that all edges incident to one prefix level share one physical source endpoint. The only possible escape from the two-sheet cycle is therefore endpoint multiplicity inside at least one level on the `0`–`D` path.

## 2. Exact combinatorial lemma to prove

Let `P_0` be the unique `0`–`D` path in `G_P`. For each oriented realization of each edge of `P_0`, record its physical endpoint on each hull arc. If at every internal path level `k` the incoming and outgoing selected diameter edges in a fixed orientation can be chosen to use the same physical level-`k` endpoint, then the two opposite-orientation lifts of `P_0`, together with `z` and `a`, form a cycle in `H_(tau_r)`, contradicting C96.

Hence every triangle-free survivor must have a **level-splitting obstruction** on `P_0`: for every attempt to concatenate both orientation lifts, at least one internal prefix level must use distinct physical source vertices for the two incident lifted edges.

The useful target is a quantitative version: prove that the number of necessary split vertices along `P_0` is large, and charge them either to extra diameter endpoints `q-(2D+2)` or to exposed-hull/train surplus.

## 3. What must be checked next

1. Extract from the pure-rhombic train geometry the exact structure of source vertices having the same chain-prefix level on one hull arc.
2. Determine whether two distinct source vertices on the same hull arc and same prefix level force at least one non-chain boundary/train event between them.
3. If yes, inject level-splitting events into the secondary-train population `T-D`, yielding a lower bound that can be combined with C82/C92 and C96.
4. Keep the argument at the level of the complete source diameter graph; do not infer endpoint sharing from the prefix quotient alone.

No Level I closure is claimed in this commit.
