<!-- theorem-state: {"artifact_id":"ART-C6D2303B0099","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C dominant-diameter geodesic-flow stability

**Date:** 2026-09-05  
**Repository state:** after promoted C97-C98  
**Run type:** exact finite KKT cut / geodesic stability theorem  
**Target:** quantitative bridge from C98 one-leaf concentration toward C97  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Setup

Work in a C65 full-support normalized KKT stress. Thus

`sum_(h in H) beta_h=1`,

and the total positive contact stress is

`sum_(e in C) alpha_e=D^2`.

Fix one actual diameter edge

`za in H`

with weight

`beta=beta_za`.

C98 proves that in the C71-B near-zero sequence one may choose such an edge with

`beta=1-o(1)`.

The point of this note is that a dominant diameter edge already forces a nearly saturated contact flow to its **specific endpoint** `a`, not merely to the whole diameter-leaf set of `z`.

## 2. Every z-a contact cut has large capacity

Let `U` be any set of positive-contact vertices with

`z in U`, `a notin U`.

Sum the KKT equilibrium equations over `U`. Internal contact forces and internal diameter reactions cancel. Orient every crossing edge from `U` to its complement. The diameter edge `za` crosses the cut and contributes the vector

`beta (p_z-p_a)`

of norm `beta D`.

Every other crossing diameter edge has total beta weight at most `1-beta`, and each has length `D`. Hence the resultant of all the other crossing diameter reactions has norm at most

`D(1-beta)`.

Therefore the total crossing diameter resultant has norm at least

`D[beta-(1-beta)] = D(2beta-1)`.

The crossing contact resultant equals it. Taking the triangle inequality on the contact side gives

### Theorem 1 — dominant-edge cut bound

For every `z-a` contact cut,

`cap_alpha(U) >= D[2beta-1]_+`.

This is exact and finite.

## 3. Specific-leaf max flow

By max-flow/min-cut in the positive contact graph, there is an undirected contact flow from `z` to the **single vertex** `a` of value

`F >= D[2beta-1]_+`.

Choose a flow of value exactly

`F_*=D[2beta-1]_+`

when the maximum is larger. Remove cycles and decompose it into simple `z-a` paths `P` with weights `x_P>=0`:

`sum_P x_P=F_*`.

Let `m(P)` be the number of unit contact edges in `P`. Since `|z-a|=D`,

`m(P)>=D`.

The total absolute edge-flow mass is

`M=sum_P x_P m(P)=sum_e |f_e|`.

Capacity gives

`M<=sum_e alpha_e=D^2`,

whereas the path-length lower bound gives

`M>=D F_*`.

For `beta>=1/2`, this yields the exact excess bound

`0 <= M-D F_* <= D^2-D^2(2beta-1)`

`=2D^2(1-beta)`.

Thus:

### Theorem 2 — dominant-edge path-excess stability

If `beta_za>=1/2`, there is a contact flow of value

`F_*=D(2beta_za-1)`

from `z` to `a` whose path decomposition satisfies

`sum_P x_P[m(P)-D] <= 2D^2(1-beta_za)`.

In particular, if `beta_za=1-o(1)`, then

- `F_*=D-o(D)`;
- `M=D^2-o(D^2)`;
- the weighted mean path excess is `o(D)`.

## 4. Exact angular-energy identity

Let

`u=(p_a-p_z)/D`.

Orient every edge of a path `P` from `z` to `a`, and let its unit direction vectors be

`e_(P,1),...,e_(P,m(P))`.

Because the path displacement is exactly `D u`,

`sum_r e_(P,r)=D u`.

Hence

`m(P)-D = sum_r [1-e_(P,r) dot u]`.

Since `|e-u|^2=2(1-e dot u)` for unit vectors,

`sum_r |e_(P,r)-u|^2 = 2[m(P)-D]`.

Multiply by `x_P` and sum over the path decomposition. Theorem 2 gives:

### Theorem 3 — dominant-edge directional-energy stability

For `beta_za>=1/2`, the flow can be chosen so that

`sum_P x_P sum_(e in P) |dir_P(e)-u|^2`

`<=4D^2(1-beta_za)`.

Thus C98's `beta_za=1-o(1)` conclusion implies a `z`-to-`a` contact flow of value `D-o(D)` that consumes `D^2-o(D^2)` contact capacity and whose capacity-weighted unit-edge directions have total squared deviation `o(D^2)` from the diameter direction.

Equivalently, for every fixed angular threshold `theta>0`, the total flow-edge mass carried by oriented path edges making angle at least `theta` from `u` is at most

`4D^2(1-beta_za) / [4 sin^2(theta/2)]`

`= D^2(1-beta_za)/sin^2(theta/2)`.

So every fixed-angle transverse population is `o(D^2)` in C98.

## 5. Relation to C81 and C97

C81 gives a flow from `z` to the whole star-leaf set. The theorem here is sharper once C98 produces one dominant diameter edge: the sink is the single dominant leaf `a`, and no star-cancellation scalar is needed.

At exact equality `beta_za=1`, Theorems 2-3 force

`F_*=D`, `M=D^2`,

and every positive-flow path has exactly `D` unit edges all parallel to `u`. This is the geodesic/capacity equality mechanism feeding C76-C80 and ultimately the C97 terminal-twist contradiction.

For `beta_za=1-o(1)`, the theorem supplies the quantitative precursor that was missing from C98: the dominant mechanical edge forces an almost-saturated, almost-parallel contact transport to its own endpoint.

It still does not prove that the underlying contact graph is a pure rhombic disk, nor that the small transverse capacity can be removed without changing the diameter. Those are the remaining stability/topology tasks.

## 6. Audit classification

| Statement | Classification | Reason |
| --- | --- | --- |
| every `z-a` cut has capacity at least `D(2beta-1)` | proved | summed KKT equilibrium + all other beta mass `<=1-beta` |
| specific-leaf max flow of value `D(2beta-1)` | proved | max-flow/min-cut |
| weighted path excess `<=2D^2(1-beta)` | proved | total contact capacity is exactly `D^2` |
| directional energy `<=4D^2(1-beta)` | proved | exact path displacement identity |
| C98 implies almost-saturated almost-parallel flow to one leaf | proved | substitute `beta=1-o(1)` |
| this alone yields the C97 finite contradiction | not proved | topology and defect localization remain open |

## 7. Handoff

```text
LEVEL I STATUS: STILL OPEN.

New exact bridge from C98:
If a diameter edge za has KKT weight beta>=1/2, then every z-a contact cut has capacity >=D(2beta-1). Hence there is a z-to-a contact flow of that value with

  sum_P x_P(m(P)-D) <= 2D^2(1-beta)

and, writing u=(a-z)/D,

  sum_P x_P sum_(e in P)|dir_P(e)-u|^2
      <=4D^2(1-beta).

Therefore C98 beta=1-o(1) gives a specific-leaf flow of value D-o(D), using D^2-o(D^2) capacity, with o(D^2) total transverse directional energy.

Next target:
Turn this transverse-capacity defect into either a quantitative terminal-twist cost, an exceptional-topology cost, or a positive lower bound on D*epsilon.
```