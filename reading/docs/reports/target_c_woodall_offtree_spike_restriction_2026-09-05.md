> Generated reading edition · [exact source](../../../docs/reports/target_c_woodall_offtree_spike_restriction_2026-09-05.md) · source SHA-256 `b39f01573d086c34530ef128c50c8bb66b0d6ca96e8b0b46e379c53fcd2f598a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-84DC3877C987","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: Woodall restriction on the unique endpoint-equality defect

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Input

Assume the exact C96 endpoint floor

`q=2D+2`.

The preceding reports prove that the complete source diameter graph contains a spanning tree

`T_*`

with `q-1=2D+1` edges, and at most one further diameter edge `e_*`.

Every source diameter graph is a straight-line thrackle: two diameter segments cannot be geometrically disjoint, because two disjoint diameter segments have a cross-pair of endpoints farther apart than the common diameter.

We now use the classical Woodall classification of straight-line thrackleable graphs:

> every connected straight-line thrackle is either a caterpillar tree or a spiked odd cycle (and disconnected straight-line thrackles are unions of caterpillars).

For the present argument only the connected unicyclic consequence is needed: a connected straight-line thrackle with exactly one cycle has an odd unique cycle, and every vertex outside that cycle is a leaf adjacent directly to a cycle vertex.

## 2. Consequence when the extra diameter exists

If `e_*` does not exist, the full diameter graph is simply the spanning caterpillar tree `T_*`.

Suppose `e_*` exists. Then

`G_diam = T_* union {e_*}`

has `q` vertices and `q` edges. Since `T_*` is spanning and connected, `G_diam` is connected and unicyclic. Woodall therefore forces `G_diam` to be a spiked odd cycle.

Let `x,y` be the endpoints of `e_*`, and let

`P_*(x,y)`

be the unique `x`-to-`y` path in `T_*`. Then the unique cycle of `G_diam` is exactly

`P_*(x,y) union {e_*}`.

Hence:

1. `|E(P_*)|` is even, because the cycle length `|E(P_*)|+1` is odd;
2. every vertex of `T_*` outside `P_*` is a leaf of `T_*` adjacent directly to a vertex of `P_*`;
3. equivalently, `P_*` contains every non-leaf vertex of `T_*`;
4. therefore `P_*` is a full spine of the equality tree `T_*` (possibly with redundant degree-2 end vertices).

This sharply restricts the possible identity of the sole off-tree edge: it cannot join an arbitrary pair of tree vertices. Its tree path must traverse the entire non-leaf core.

## 3. Combine with the one-sided chain defect

The preceding one-sided-defect theorem proves independently that `e_*` cannot cross the pivot train `tau_s`. By C83 its chain-crossing set is one interval, so it lies wholly before or wholly after the pivot.

Therefore any exact endpoint configuration with a full `q`-edge diameter graph must simultaneously satisfy two conditions:

- **global thrackle condition:** `e_*` closes the full spine of `T_*` into an odd cycle;
- **chain condition:** the prefix interval of `e_*` avoids `s` and is confined to one side of the common chain cut.

This is a genuine coupling of global diameter-graph topology and the C83 chain coordinate. The previous C96 equality classification used only the common-cut tree and therefore did not impose the first condition.

## 4. Immediate no-go criterion

We obtain the following finite criterion.

### Theorem W1 — off-tree-edge no-go

At `q=2D+2`, if every pair `x,y` whose tree path in `T_*` contains all non-leaf vertices has a diameter prefix interval containing the pivot level `s`, then the full diameter graph has no off-tree edge at all.

Indeed, any hypothetical `e_*=xy` would have to close such a full-spine path by Woodall, but the one-sided-defect theorem forbids `e_*` from crossing `tau_s`.

Thus proving the stated prefix-interval property for the four C96 equality patterns A--D would upgrade endpoint equality from

`|E(G_diam)| <= q`

to the exact global tree identity

`G_diam=T_*`.

## 5. Remaining gate

The missing step is now precise. One must identify the possible spine endpoints of `T_*` inside equality patterns A--D and prove that any physical diameter joining such endpoints necessarily has a C83 prefix interval through `s`, or else rule out the corresponding equal-length chord geometrically.

This is substantially narrower than classifying an arbitrary extra diameter.

## Reference

D. R. Woodall, *Thrackles and deadlock*, in **Combinatorial Mathematics and its Applications**, Academic Press, 1971, 335--347. The straight-line classification is also restated in later thrackle literature as: a graph is straight-line thrackleable iff it is a union of disjoint caterpillars or a spiked odd cycle (with isolated vertices allowed).
