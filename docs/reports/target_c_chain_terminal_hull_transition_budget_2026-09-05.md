<!-- theorem-state: {"artifact_id":"ART-C33D72F052E8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C chain-terminal hull-transition budget

**Date:** 2026-09-05  
**Repository state:** `6950289d` (`main`)  
**Run type:** exact finite structural/counting theorem  
**Target:** Target C C80-C96 chain-face branch  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting point

In the C80 chain-face branch the exact chain diameter `za` crosses `D` pairwise disjoint chain trains

`P={tau_1,...,tau_D}`.

C83 orders those tracks as nested `z-a` separators. C87 adds two facts:

1. the terminals of the `D` chain trains occur in chain order on each of the two hull arcs `L,U` from `z` to `a`;
2. every prefix level `k=0,...,D` occurs as the level of at least one active-diameter endpoint on each arc, because the C87 prefix tree is connected on all levels and every simple edge occurs in both physical arc orientations.

C65 puts every active-diameter endpoint in convex position. Therefore each chain-level zone on each hull arc contains a convex-hull vertex.

The pure-rhombic boundary identity from Target B is

`B=2T`,

and the boundary is partitioned into one unit-edge indentation chain between each pair of consecutive convex-hull vertices.

These facts force many very short indentation chains whenever `T<3D`.

## 2. Distinguished transition chains

### Lemma 1 — one distinct hull transition per chain terminal

On each hull arc `L` and `U`, every terminal of `tau_j`, `1<=j<=D`, lies in a distinct indentation chain between consecutive convex-hull vertices. That indentation chain contains exactly one terminal edge from the family `P`.

Hence there are exactly `2D` pairwise distinct distinguished hull indentation chains, one for each side-terminal incidence of the `D` chain trains.

### Proof

C83 gives nested separator regions and C87 states that the chain levels are nondecreasing along each hull arc, with the `P` terminals occurring in chain order. Crossing the terminal edge of `tau_j` changes the chain level from `j-1` to `j`; between consecutive `P` terminals the level is constant.

C87 connectivity and physical pairing give an active diameter endpoint at every level `k` on each of `L,U`. C65 makes each such endpoint a convex-hull vertex. Thus every constant-level boundary zone on each arc contains at least one convex-hull vertex.

Fix the terminal of `tau_j` on one arc. Take the last convex-hull vertex in the level-`j-1` zone before this terminal and the first convex-hull vertex in the level-`j` zone after it. By construction these are consecutive convex-hull vertices. The intervening contact-boundary chain crosses the `tau_j` terminal and no other `P` terminal. Different `j` give different chains because the intervening level zone contains a convex-hull vertex; the two hull arcs are disjoint except at `z,a`. This gives `D` distinguished chains on each side, hence `2D` total. `square`

## 3. Exact short-transition count

Let

- `q` be the number of convex-hull vertices / diameter endpoints in the normalized C65 source;
- `r_i` be the unit-edge length of a hull indentation chain;
- `m_1` be the number of the `2D` distinguished chains with `r_i=1`;
- `m_2` be the number with `r_i=2`.

### Lemma 2 — at most two one-edge distinguished transitions

`m_1<=2`.

### Proof

A one-edge distinguished chain consists only of one terminal edge of a chain train. Every edge of a train in `P` is parallel to the chain direction `u`. If that one unit edge joins consecutive convex-hull vertices, it is itself a side of the convex hull parallel to `u`.

A convex polygon has at most two sides parallel to one unoriented direction, one on each supporting line. Hence at most two distinguished transitions can have length one. `square`

### Theorem — chain-terminal hull-transition budget

The number of two-edge distinguished transitions satisfies the exact finite bound

`m_2 >= 4D+q-2T-4`.

Using C96, `q>=2D+2`, this gives

`m_2 >= 2(3D-T)-2`.

In particular, for every asymptotic survivor with

`T/D <= 3-epsilon`,

there are at least

`(2epsilon-o(1))D`

two-edge hull indentation chains containing exactly one `P` terminal edge.

Moreover, the non-`P` edge in each such two-edge chain is the terminal edge of a secondary train. Since one train has only two boundary terminals, at least

`m_2/2 >= 2D+q/2-T-2`

distinct secondary trains occur in this way. With C96,

`# boundary-neighbor secondary trains >= 3D-T-1`.

### Proof

The full pure-rhombic contact boundary has `B=2T` unit edges. The `q` convex-hull vertices partition it into `q` nonempty indentation chains, so every non-distinguished chain has length at least one.

The `2D` distinguished chains therefore have total length at most

`2T-(q-2D)`.

Among the distinguished chains, those not counted by `m_1,m_2` have length at least three. Hence their total length is at least

`m_1+2m_2+3(2D-m_1-m_2)`

`=6D-2m_1-m_2`.

Therefore

`6D-2m_1-m_2 <= 2T-q+2D`,

so

`2m_1+m_2 >= 4D+q-2T`.

Lemma 2 gives

`m_2 >= 4D+q-2T-4`.

C96 gives `q>=2D+2`, yielding

`m_2>=6D-2T-2=2(3D-T)-2`.

Each distinguished transition contains exactly one `P` terminal edge by Lemma 1. Thus when its length is two, its other unit boundary edge cannot belong to a train in `P`: a `P` train has no boundary edge except a terminal, and a second `P` terminal is excluded by Lemma 1. The other edge is therefore the terminal of a secondary train. Each secondary train has exactly two boundary terminal edges, so one secondary train can account for at most two such transitions. Dividing the `m_2` bound by two proves the final claim. `square`

## 4. Quantitative consequence at the current low-train frontier

The audited two-wall worker branch has reached the separate necessary bound

`T/D>2.9346`

but has not closed the branch. If one works just above that frontier, the theorem here shows why the remaining interval up to `3D` is geometrically special:

at `T/D=2.9346`, the count would force approximately

`m_2/D >= 0.1308`

and at least

`0.0654D`

distinct secondary trains whose boundary terminal is immediately adjacent to a chain-train terminal in a two-edge hull indentation.

This statement does not import the unmerged `2.9346` theorem into the canonical stack; the numerical line is only an interface calculation.

## 5. Geometry of one two-edge transition

Let a distinguished two-edge chain be

`A--V--B`,

where one unit edge belongs to `P` and the other to a secondary train `sigma`. Let `alpha` be the angle between the two contact rays `VA` and `VB`. Unit separation gives

`|A-B|=2 sin(alpha/2)>=1`,

and triangle-freeness makes the inequality strict, so

`alpha>pi/3`.

The shell ear between the two unit edges and the hull chord `AB` has area

`(1/2) sin(alpha)`.

If the projective angle between `sigma` and the chain direction is at least `pi/3`, then `alpha<=2pi/3` (after using the boundary orientation) and this ear has area at least

`sqrt(3)/4`.

If instead the projective angle is below `pi/3`, then the two train directions cannot cross in a unit-separated rhombus; this is a non-`P`-crossing boundary-neighbor regime. In that case the hull chord has length

`|A-B|>sqrt(3)`.

Thus every forced two-edge transition gives one of two concrete resources:

1. a shell ear of area at least `sqrt(3)/4`; or
2. a long hull side `>sqrt(3)` carried by a secondary train direction that cannot cross the chain family at that local projective angle.

No global summation of this dichotomy is claimed yet, because the same secondary train may appear at two terminals and because a noncrossing train can change its relation to the finite chain interval through boundary placement.

## 6. Exact remaining lemma

The new finite bottleneck is:

> **Boundary-neighbor transfer lemma.** Convert a positive linear number of two-edge `P`-terminal transitions into either a positive linear shell charge that survives the global `G+E` budget, or a positive linear population excluded from the two coherent chain-neighbor phases in the C90/TS wall-capacity decomposition.

The second alternative is especially relevant to the current two-wall frontier: near the scalar optimum almost all non-chain atomic train mass is forced into the two coherent side populations, while the theorem above forces a linear population of secondary boundary-neighbor trains whenever `T/D` stays below `3`.

## 7. Audit classification

| Statement | Classification | Reason |
| --- | --- | --- |
| `2D` distinct distinguished hull transition chains | proved | ordered terminals + one hull vertex in every prefix-level zone |
| `m_1<=2` | proved | one-edge transition is a hull side parallel to `u` |
| `m_2>=4D+q-2T-4` | proved | exact boundary-edge count |
| `m_2>=2(3D-T)-2` | proved | C96 `q>=2D+2` |
| at least `m_2/2` distinct secondary neighbor trains | proved | two terminals per train |
| every such train contributes shell area `sqrt(3)/4` | false without angle information | shallow two-edge ears are possible |
| boundary-neighbor count alone closes `T<3D` | not proved | requires transfer into shell or phase capacity |

## 8. Handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem:
C87+C65 force 2D distinct hull indentation chains, one straddling every P-train terminal on each side. If m2 is the number of these chains having exactly two unit edges, then

m2 >= 4D+q-2T-4 >= 2(3D-T)-2.

Their second edges belong to at least

3D-T-1

distinct secondary trains.

At T/D≈2.9346 this is ≈0.1308D two-edge ears and ≈0.0654D distinct secondary boundary-neighbor trains.

Remaining lemma:
Transfer those forced boundary neighbors into either additive shell loss or the residual/noncoherent population in the two-wall phase-capacity theorem.
```
