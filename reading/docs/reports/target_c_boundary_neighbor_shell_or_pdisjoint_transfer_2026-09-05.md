> Generated reading edition · [exact source](../../../docs/reports/target_c_boundary_neighbor_shell_or_pdisjoint_transfer_2026-09-05.md) · source SHA-256 `b460d2e2e0364fbb027192067a91d4bf6bb8eca27d47caf898e8b116dccf626f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CFB18E0956C2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: boundary-neighbor shell / P-disjoint transfer

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Uses current main:** `9c78bad9` chain-terminal hull-transition budget  
**Status:** LEVEL I STILL OPEN

## 1. Setup

Work in the canonical C80--C96 pure-rhombic chain-face branch. Let

- `P={tau_1,...,tau_D}` be the exact C80 chain trains, all with train direction `u`;
- `L,U` be the two contact-boundary arcs from the chain endpoint `z` to the other endpoint `a`;
- `q` be the C65 convex-hull vertex / diameter-endpoint count;
- `T` be the total train count;
- `G=area(K)-area(R)` be the shell area outside the preserved pure rhombic disk;
- `m_2` be the number of distinguished chain-terminal indentation chains of length exactly two from main commit `9c78bad9`.

That theorem proves

`m_2 >= 4D+q-2T-4`,                            (1.1)

and therefore, by C96 `q>=2D+2`,

`m_2 >= 2(3D-T)-2`.                            (1.2)

Each such indentation chain is

`A--V--B`,

where `A,B` are consecutive convex-hull vertices, one unit edge is the terminal edge of a chain train in `P`, and the other is the terminal edge of one secondary train `sigma`.

Call the transition **shallow** if the projective angle `delta(sigma,u)` is `<pi/3`, and **deep** otherwise. Write

`m_2=s+d`

for the shallow and deep counts.

Let

`N_0 = #{secondary trains sigma : sigma crosses no train of P}`.

## 2. A shallow neighbor is P-disjoint

A crossing of two trains in a strict triangle-free unit-rhombic disk occurs in a strict unit rhombus. If the acute projective angle between the two train directions were at most `pi/3`, one rhombus diagonal would have length at most one; equality gives a unit equilateral triangle and strict inequality violates unit separation.

Therefore any secondary train at projective angle `<pi/3` from `u` crosses no train of `P`.

Hence every shallow two-edge transition is carried by a train counted in `N_0`.

## 3. One shallow train can occur in at most one two-edge transition

C91/C90 gives a useful endpoint fact: both terminals of every non-chain train lie on the same one of the arcs `L,U`. Along an oriented boundary arc from `z` to `a`, the two terminal edge vectors of one train are opposite.

For `tau_j in P`, C80 orients its train vector as `u`; crossing its terminal from prefix level `j-1` to `j` along either `z`-to-`a` arc therefore contributes the boundary edge vector `+u`.

Fix a shallow transition and choose the unit secondary direction `v` so that

`u dot v = cos(delta)>1/2`.

If the secondary terminal used in the transition had boundary vector `-v`, then the hull chord between the two endpoint hull vertices would be

`u-v`

(up to the order of the two unit steps), and

`|u-v|=2 sin(delta/2)<1`.

But the two hull vertices are distinct source points, so unit separation requires their distance at least one. Contradiction.

Thus the shallow transition necessarily uses the `+v` terminal of `sigma`; its hull chord is

`u+v`,

with

`|u+v|=2 cos(delta/2)>sqrt(3)`.

The other terminal of the same train has boundary vector `-v`. If that terminal also belonged to another distinguished two-edge transition, its two-step hull chord would again be `u-v`, of length `<1`, impossible.

### Lemma BN1 — shallow transitions are injective in trains

Distinct shallow distinguished two-edge transitions use distinct secondary trains. Every such train is P-disjoint. Consequently

`s <= N_0`.                                      (3.1)

This strengthens the factor-two train-reuse bound from `9c78bad9` exactly in the shallow phase.

## 4. Deep ears add without overlap

For one two-edge indentation chain `A--V--B`, the shell pocket between the contact boundary and the hull side `AB` is exactly the triangle `AVB`. If `alpha` is the angle between the two contact rays `VA,VB`, its area is

`(1/2) sin(alpha)`.

The geometry recorded in `9c78bad9` gives, in the deep case,

`area(AVB) >= sqrt(3)/4`.                       (4.1)

Different distinguished transition chains are different indentation chains between different consecutive hull-vertex pairs. Their shell pockets have disjoint interiors. Therefore the deep-ear charges are genuinely additive, regardless of whether one secondary train supplies terminals to two different deep transitions:

`G >= d sqrt(3)/4`.                             (4.2)

Equivalently,

`d <= 4G/sqrt(3)`.                              (4.3)

## 5. Exact boundary-neighbor transfer theorem

Combine `m_2=s+d`, (3.1), and (4.3):

`m_2 <= N_0 + 4G/sqrt(3)`.

With (1.1):

### Theorem BN2 — shell / P-disjoint transfer

Every canonical C80--C96 pure-rhombic chain-face survivor satisfies the exact finite inequality

`N_0 + 4G/sqrt(3) >= 4D+q-2T-4`.              (5.1)

Using C96,

`N_0 + 4G/sqrt(3) >= 2(3D-T)-2`.              (5.2)

Thus the entire two-edge chain-terminal transition deficit below `3D` is transferred into two static resources:

1. secondary trains that cross **none** of the exact chain family `P`; and
2. pairwise-disjoint shell ears with their exact area charge.

There is no across-time activation issue and no reuse ambiguity.

## 6. Consequences for phase-capacity arguments

A P-disjoint train has an empty C91 interval neighborhood

`J_sigma=empty`.

Hence it is an extreme bad row in every P-versus-secondary Ferrers incidence matrix: it misses all `D` possible chain incidences.

Therefore, if a separate phase-stability theorem gives an upper bound

`N_0 <= eta D + o(D)`

and a shell argument gives

`G <= gamma D + o(D)`,

then (5.2) forces

`3-T/D <= eta/2 + 2gamma/sqrt(3) + o(1)`.

Conversely, any hypothetical sequence with `T/D <= 3-epsilon` must satisfy

`N_0/D + (4/sqrt(3)) G/D >= 2epsilon-o(1)`.      (6.1)

This is exactly the missing boundary-neighbor transfer in a form ready to insert into the repaired wall-capacity or `G+E` shell budget.

## 7. Audit boundary

The theorem does **not** claim that `N_0` is small and does **not** claim that bare shell area `G` alone is small enough to close the problem. Those are the next quantitative inputs required.

The new point is that the local shallow/deep dichotomy from `9c78bad9` can be summed globally after all: shallow events are injectively charged to P-disjoint trains, while deep events are charged to disjoint shell triangles.