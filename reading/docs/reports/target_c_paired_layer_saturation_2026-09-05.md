> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_layer_saturation_2026-09-05.md) · source SHA-256 `4572edef2ba843ca408fabb41caf0d051912f6551060c3b079a60fc3e9802b25`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E96847D7CB09","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C98: paired layer saturation

**Date:** 2026-09-05  
**Repository base:** C97 branch after `5e6dc53`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C83 chain levels, C87 paired staircase tree, C90 train-cut forest, C96 common cut, C97 saturation identities

C87 associates the exact C80 chain atom with a simple prefix tree on levels `0,1,...,D`. Every one of its `D` tree edges occurs as at least one active source diameter in each physical hull-arc orientation. C96 places all these selected diameters, together with the chain diameter `za`, across one common chain train.

This note counts how many distinct physical source endpoints are required above each prefix level. The resulting split budget is much sharper than a bare total endpoint count: in the low-train phase, at least `0.813799...D` interior chain levels are forced to have exactly one selected endpoint on each hull arc.

## 1. Fix one paired lift of the C87 tree

Let `G_P` be the C87 simple prefix tree on the `D+1` levels `0,...,D`.

For every tree edge `{a,b}`, `a<b`, choose exactly two active source diameter pairs:

- one positive-orientation pair `L_a U_b`;
- one reverse-orientation pair `U_a L_b`.

Let `S` be the graph consisting of these `2D` selected non-chain diameter edges together with the chain diameter `h_0=za`. Thus

`|E(S)|=2D+1`.

Every edge of `S` crosses the C87 common train `tau_r`. Since the complete common-cut diameter graph is a forest by C90, `S` is itself a forest.

Let `c_S` be the number of nontrivial components of `S`, and let `v_S` be the number of source vertices incident with `S`. Then exactly

`v_S=2D+1+c_S`.

In particular `v_S>=2D+2`.

## 2. Physical multiplicity over one prefix level

Every source vertex has a unique C83 chain level `k(v) in {0,...,D}`. For each level `k`, let

`n_k = # {v in V(S): k(v)=k}`.

Because `G_P` spans every prefix level, each level is incident with at least one tree edge.

For an interior level `1<=k<=D-1`, the two selected orientations of any incident tree edge use one endpoint on hull arc `L` at level `k` and one endpoint on hull arc `U` at level `k`. The open arcs `L\{z,a}` and `U\{z,a}` are disjoint. Therefore

`n_k>=2` for `1<=k<=D-1`.

At the extreme levels only

`n_0>=1`, `n_D>=1`

is forced, because the two hull arcs meet at `z` and `a`.

Define the physical layer-splitting excess

`A := (n_0-1)+(n_D-1)+sum_(k=1)^(D-1)(n_k-2)`.

Since every vertex has one unique level,

`sum_(k=0)^D n_k=v_S`,

while the baseline multiplicity is

`1+1+2(D-1)=2D`.

Hence

`A=v_S-2D`.

Using the forest identity for `S` gives the exact formula:

### Theorem C98.1 — exact paired-layer split identity

`boxed: A=1+c_S.`

Thus the entire excess physical multiplicity of a paired lift is exactly one plus its number of forest components.

## 3. Endpoint-surplus control

Every selected endpoint is a source diameter endpoint, so

`v_S<=q`.

Write again

`s=q-(2D+2)>=0`.

Then

`2D+1+c_S=v_S<=2D+2+s`,

so

`c_S<=s+1`

and therefore

`A=1+c_S<=s+2`.

Let `B` be the number of interior levels with `n_k>=3`. Each such level contributes at least one to `A`. Hence:

### Theorem C98.2 — unsplit-level bound

At least

`(D-1)-(s+2)=D-s-3`

interior prefix levels satisfy

`n_k=2`.

At every such level there is exactly one selected source endpoint on `L` and exactly one selected source endpoint on `U`.

This statement is selection-independent: choose any one active diameter in each C87 orientation over every prefix-tree edge, and the same bound holds.

## 4. Incidence rigidity at an unsplit level

Fix an interior level `k` with `n_k=2`. Write its unique selected endpoints as

`L_k` and `U_k`.

For every prefix-tree edge `{k,j}` incident to `k`, the positive and reverse selected physical diameter edges require an endpoint of level `k` on each hull arc. Since there are no alternatives at this level, all such incidences use the same two source vertices `L_k,U_k`.

Therefore the two physical selected vertices each have selected non-chain degree exactly

`deg_(G_P)(k)`.

So every unsplit level is an exact two-sheet lift of the local prefix-tree star: the combinatorial branching of `G_P` is copied identically onto one vertex on each hull arc.

Splitting of physical incidence among several same-level source vertices is confined to at most `s+2` interior levels, and usually fewer because endpoint excess can also occur at levels `0,D` or with multiplicity larger than three.

## 5. Zero-slack phase

If

`q=2D+2`,

then `s=0`. C97 already shows that the complete common-cut graph has exactly `2D+1` edges, is connected, and is spanning. Since `S` already contains `2D+1` common-cut edges,

`S=H_(tau_r)`

and `c_S=1`.

C98.1 now gives the exact physical layer excess

`A=2`.

Consequently all but at most two interior levels are unsplit. More precisely,

`(n_0-1)+(n_D-1)+sum_(k=1)^(D-1)(n_k-2)=2`.

Thus the entire freedom to duplicate physical source vertices over the `D+1` prefix levels consists of exactly two units of multiplicity.

If `n_0=1`, the unique level-zero selected endpoint must be `z`: both hull arcs meet only at `z` at that endpoint level. Similarly `n_D=1` forces the unique level-`D` endpoint to be `a`.

Combined with C97, the zero-slack complete diameter graph is therefore a spanning common-cut caterpillar whose `2D` non-chain edges are a paired physical lift of the C87 prefix tree, with only two total units of layer splitting, and with at most one additional off-cut edge in the Hopf--Pannwitz equality case.

## 6. Low-train numerical consequence

In C94's low-train phase, C82 and C96 give

`q/D <= 2.1862006358...+o(1)`

and hence

`s/D <= 0.1862006358...+o(1)`.

C98.2 therefore forces at least

`D-s-3 >= (0.8137993642...-o(1))D`

interior levels to be unsplit.

The constant is

`0.8137993642... = pi/sqrt(3)-1 = 2Delta_2-1`,

the same coefficient that appears in C94's lower bound for the dimension of the exact active-face tangent flat. C98 does not identify those two objects, so this numerical coincidence is not yet a theorem connecting the flat to the paired lift. It does show that both large structures occupy the same linear scale and leaves only a `0.1862D+o(D)` exceptional layer budget.

## 7. Frontier effect

C96/C97 reduced the complete diameter graph to a near-spanning common-cut caterpillar. C98 adds a source-level rigidity statement: almost every prefix level in the low-train phase has exactly two selected physical endpoints, one on each hull arc, and all paired diameter incidences at that level are forced through those two vertices.

The next useful target is an ordered two-sheet classification: prove that a C87 antitone prefix tree with only `s+2` split levels cannot realize the paired diameter-thrackle geometry unless either

1. many shared-endpoint diameter stars occur, contradicting the C18 global angular container bound;
2. an even diameter cycle is forced; or
3. the exceptional split levels have linear size beyond the C98 budget.

No such final exclusion is claimed here.
