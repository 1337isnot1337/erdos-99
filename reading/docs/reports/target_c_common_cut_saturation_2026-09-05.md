> Generated reading edition · [exact source](../../../docs/reports/target_c_common_cut_saturation_2026-09-05.md) · source SHA-256 `82f97c8f89b05a90978c794751f5fa5cef7996ee743c2bb371edd4a85706e2d7`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2C6CC17BBA03","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C97: common-cut saturation identities

**Date:** 2026-09-05  
**Repository base:** `89c17412` (main after branch-consolidation audit)  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C65 complete source diameter graph, Hopf--Pannwitz, C90 train-cut caterpillar theorem, C96 common-chain cut

C96 proves that the complete source diameter graph crossing the C87 common chain train `tau_r` is a caterpillar forest with at least `2D+1` edges and at least `2D+2` incident diameter endpoints. This note keeps the endpoint and edge deficiencies instead of discarding them. The result is an exact slack decomposition and a sharp classification of the zero-slack phase.

## 1. Notation

Let `H` be the complete source diameter graph on its `q` nonisolated diameter endpoints. Let

`F=H_(tau_r)`

be the subgraph consisting of all diameter edges whose endpoints lie on opposite sides of the C87 common train `tau_r`.

Write

- `m=|E(F)|=2D+1+e`, with `e>=0`;
- `c` for the number of nontrivial components of `F`;
- `v` for the number of vertices incident with `F`;
- `r=q-v` for the number of diameter endpoints not incident with the common-cut graph;
- `s=q-(2D+2)` for the endpoint surplus above the C96 floor;
- `delta=q-|E(H)|>=0` for the Hopf--Pannwitz edge deficiency;
- `o=|E(H)\E(F)|` for the number of diameter edges not crossing `tau_r`.

C90 makes `F` a forest, so

`v=m+c`.

## 2. Exact endpoint-slack identity

Substituting `m=2D+1+e` into the forest identity gives

`v=2D+1+e+c`.

Since `q=v+r`,

`q-(2D+2)=e+(c-1)+r`.

Hence:

### Theorem C97.1 — exact common-cut endpoint saturation

`boxed:  s=e+(c-1)+r.`

The C96 inequality

`q-(2D+2) >= e+(c-1)`

is therefore exact after adding the omitted endpoint term `r`. Every unit of endpoint surplus is accounted for by exactly one of:

1. an extra common-cut diameter edge beyond `2D+1`;
2. an extra nontrivial common-cut component beyond one;
3. a diameter endpoint not touched by the common-cut forest.

There is no fourth source of endpoint slack.

## 3. Exact off-cut edge identity

By definition of `delta`,

`|E(H)|=q-delta`.

Therefore

`o=|E(H)|-m=q-delta-(2D+1+e)`.

Using `q=2D+2+s`,

`o=1+s-e-delta`.

Using Theorem C97.1 to eliminate `s`, this is equivalently

### Theorem C97.2 — off-cut saturation

`boxed:  o=c+r-delta.`

In particular,

`o <= c+r <= s+1`

and also

`o <= 1+s-e`.

Thus a small endpoint surplus forces the complete diameter graph itself to be close, in edge edit distance, to the single common-cut caterpillar forest. This is stronger than saying only that most endpoints are used by the cut.

## 4. Zero-slack classification

Assume

`q=2D+2`,

so `s=0`. Theorem C97.1 forces simultaneously

`e=0`, `c=1`, `r=0`.

Hence `F` is one spanning caterpillar tree on all `q` diameter endpoints with exactly `q-1=2D+1` edges. Theorem C97.2 gives

`o=1-delta`.

Since `o>=0` and `delta>=0`, only two cases are possible.

### Case A: `delta=1`, `o=0`

Then

`H=F`.

The complete source diameter graph itself is the spanning common-cut caterpillar tree.

### Case B: `delta=0`, `o=1`

Then `H` has exactly `q` edges and differs from `F` by one edge not crossing `tau_r`. Adding one edge to a spanning tree creates exactly one cycle. Every cycle in a planar diameter graph is odd. Therefore the unique added edge closes an odd cycle.

### Corollary C97.3 — exact minimum-endpoint normal form

If `q=2D+2`, the complete source diameter graph is exactly one of:

1. a spanning common-cut caterpillar tree; or
2. that tree plus one off-cut diameter edge, producing one unique odd cycle.

No other diameter edges or diameter endpoints exist in this phase.

## 5. Near-minimum stability

If

`s=o(D)`,

then Theorem C97.1 gives separately

`e=o(D)`, `c-1=o(D)`, `r=o(D)`.

Theorem C97.2 then gives

`o=o(D)`.

Thus in the C96 minimum-slack regime the complete source diameter graph has all but `o(D)` diameter endpoints incident with the common cut, only `o(D)` extra common-cut edges/components, and only `o(D)` off-cut diameter edges. Equivalently, deleting `o(D)` vertices/edges reduces the full diameter graph to one spanning-scale common-cut caterpillar.

In C94's low-train phase C82 gives

`q/D <= 4-2Delta_2+o(1)=2.1862006358...+o(1)`.

Hence

`s/D <= 2-2Delta_2+o(1)=0.1862006358...+o(1)`.

C97 therefore budgets the entire deviation from the zero-slack diameter normal form by the same `0.1862006358... D+o(D)` endpoint reserve.

## 6. What this does and does not prove

C97 does not yet exclude either zero-slack normal form. Abstract spanning diameter caterpillars are geometrically realizable, so a contradiction must still use the chain-prefix labels, unit-contact/rhombic structure, KKT weights, or global packing optimality.

The useful new reduction is that the next argument need not control an arbitrary complete diameter graph. In the low-train phase it suffices to control a graph obtained from the C96 common-cut caterpillar by only `O(0.1863D)` endpoint/edge defects; at exact minimum there is at most one off-cut edge.

The next target is to combine this saturation with the C87 paired staircase projection. At zero slack the `2D` selected non-chain diameter edges and the chain diameter already exhaust the common-cut tree, so any forced additional diameter incidence immediately leaves the minimum phase.
