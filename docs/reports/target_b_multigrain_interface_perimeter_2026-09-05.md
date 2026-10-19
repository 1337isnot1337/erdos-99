<!-- theorem-state: {"artifact_id":"ART-9677C6BE878E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3746e959022112aaceff899406af33cf5fefbd64", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_b_multigrain_interface_perimeter_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0a3f21474e964fbe9e6da3124198d2d2fcf0d07230fd3fd43babc7d32e94d9ff"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - Target B multigrain interface-perimeter theorem

**Date:** 2026-09-05  
**Run type:** exact train/rhombus topology + Euclidean isoperimetry  
**Target:** multi-grain local-to-global transfer  
**Depends on:** pure simply connected edge-to-edge strict unit-rhombic disk; train-track definition  
**LEVEL I STATUS:** STILL OPEN

## 1. Purpose

The current Target B obstruction is genuinely multi-grain. Section 50 may leave several coherent train components whose retained crossing masses are all macroscopic. Local phase-stability theorems control one component once it dominates the global quadratic rhombus scale, but no theorem has converted several retained components into one global geometric cost.

This report gives an exact first bridge. Deleting train crossings is the same as deleting rhombi. The surviving train-crossing components determine physical retained grain regions, and their total interface perimeter is controlled by the original outer boundary plus four unit edges per deleted rhombus.

## 2. The full train-crossing graph is connected

Let `R` be a connected edge-to-edge rhombic disk. Let `Gamma` be its train-crossing graph:

- vertices are train tracks;
- each rhombus is one edge joining the two trains that cross in that rhombus.

### Lemma MG1 - train-crossing connectivity

If the rhombic disk contains at least one rhombus, `Gamma` is connected.

### Proof

The bounded-face adjacency graph of a topological rhombic disk is connected. Two rhombi sharing an internal unit edge are consecutive along the train track crossing that shared edge. Hence the two corresponding edges of `Gamma` share the vertex representing that train.

Therefore every face-adjacency path in the rhombic disk gives an edge-adjacency walk in `Gamma`. Since every train occurs in at least one rhombus, every vertex of `Gamma` is incident to an edge reached this way. Thus `Gamma` is connected. `square`

The theorem below does not need more than this local adjacency fact, but connectivity confirms that any multi-grain decomposition created by deleting crossings is an actual cut of one train system rather than a pre-existing disjoint union.

## 3. Delete an arbitrary rhombus set

Let

`F subset E(Gamma)`

be any set of deleted train crossings. Identify `F` with the corresponding set of deleted rhombi.

Let

`H_1,...,H_m`

be the nonempty edge-containing connected components of `Gamma-F`.

For each `j`, let `mathcal R_j` be the union of all retained rhombi whose train-crossing edge belongs to `H_j`. The set `mathcal R_j` may have more than one Euclidean connected component; this causes no problem below.

Let

`P_j`

be the total Euclidean perimeter of all connected components of `mathcal R_j`, counting each boundary unit edge once.

Let `B` be the unit-edge length of the original outer rhombic boundary. In a pure train disk,

`B=2T`.

## 4. Adjacent retained rhombi cannot belong to different train components

### Lemma MG2 - retained face adjacency respects train components

If two retained rhombi share an internal unit edge, then they belong to the same `mathcal R_j`.

### Proof

As in Lemma MG1, the two rhombi share one train track: the track passes through the common edge from one rhombus to the other. Their two train-crossing edges in `Gamma-F` are therefore incident with the same surviving train vertex. Hence those edges lie in the same connected component of `Gamma-F`. `square`

Consequently no unit edge can be an interface directly between two distinct retained grain regions. A retained grain boundary edge is either an original outer-boundary edge or faces a deleted rhombus.

## 5. Exact interface-perimeter budget

Each original outer-boundary unit edge can occur in the boundary of at most one retained region.

Each deleted rhombus has four unit sides. A side can contribute to the boundary of at most one adjacent retained rhombus. Therefore deleted rhombi contribute at most `4|F|` retained-boundary edges in total.

By Lemma MG2 these exhaust all possibilities.

### Theorem MG3 - global retained-grain perimeter budget

`boxed{
 sum_(j=1)^m P_j <= B+4|F| = 2T+4|F|.
}`                                                       (5.1)

The bound is exact at the combinatorial level and does not assume phase coherence, minimum degree, or asymptotics.

## 6. Convert grain perimeter to retained rhombus population

Let `R_j` denote the number of retained rhombi in `mathcal R_j` and `A_j` their total Euclidean area.

A strict unit rhombus in a unit-separated triangle-free source has both diagonals strictly greater than one. If its acute angle is `theta`, this gives

`pi/3<theta<=pi/2`

after choosing the acute angle, and therefore

`area=sintheta>sqrt(3)/2=:a_0`.

Hence

`A_j>=a_0 R_j`.                                         (6.1)

Write the Euclidean connected components of `mathcal R_j` as `Q_{j,r}`, with areas `A_{j,r}` and perimeters `P_{j,r}`. The planar isoperimetric inequality gives

`P_{j,r}>=2sqrt(pi A_{j,r})`.

Summing over `r` and using

`sum_r sqrt(A_{j,r}) >= sqrt(sum_r A_{j,r})=sqrt(A_j)`,

we get

`P_j>=2sqrt(pi A_j)>=2sqrt(pi a_0 R_j)`.                (6.2)

Combine with MG3:

### Theorem MG4 - square-root multigrain population bound

`boxed{
 2sqrt(pi a_0) sum_j sqrt(R_j)
 <= 2T+4|F|.
}`                                                       (6.3)

Equivalently,

`boxed{
 sum_j sqrt(R_j)
 <= [T+2|F|]/sqrt(pi a_0).
}`                                                       (6.4)

No assumption that `mathcal R_j` is connected is needed.

## 7. Normalized form

Suppose `T=xD+o(D)`, the deleted crossing population satisfies `|F|=fD+o(D)`, and retained grain `j` has

`R_j=r_jD^2+o(D^2)`.

Then MG4 gives

`boxed{
 sum_j sqrt(r_j)
 <= [x+2f]/sqrt(pi a_0).
}`                                                       (7.1)

If `|F|=o(D)`, this becomes

`sum_j sqrt(r_j)<=x/sqrt(pi a_0)+o(1)`.                 (7.2)

Thus a decomposition into several quadratic grains has a genuine linear interface-perimeter cost even when the grains have unrelated phase frames.

## 8. Relation to Section 50

Theorem 50.1 currently deletes

`|F|<=C_delta D^(2-eta)+C_T lambda D^2`.

At that raw scale MG4 is not yet strong enough: the deletion bound can be superlinear in `D`, while the useful physical interface scale is only linear.

The theorem therefore identifies a sharper upstream target:

> produce the coherent grain decomposition with only `O(D)` deleted rhombi (or otherwise charge the superlinear deletion term to an already-forbidden resource).

This is plausible because the canonical sixfold phase-defect energy is itself only `O(D)`, but the present Section-50 pruning also deletes low-degree vertices and pays the coarse `C_T lambda D^2` term.

A decomposition based on fixed-width phase bins / coarea rather than minimum-degree pruning could potentially keep the deletion count at boundary order. MG4 gives the exact payoff if such a decomposition is obtained.

## 9. What this does not prove

MG4 alone does not rule out two or finitely many macroscopic crystalline grains. Two disk-scale regions separated by a boundary-order interface are compatible with (6.3).

Nor does it imply a local phase-stability theorem without a retained minimum-degree condition. A grain may have many trains and relatively few crossings.

The next viable combination is:

1. build a fixed-coherence decomposition by deleting only `O_epsilon(D)` high phase-variation crossings;
2. use MG4 to control the number and sizes of physical grains;
3. apply PDG/PC3/GPI inside grains carrying quadratic crossing mass;
4. use the remaining interface perimeter as the physical charge coupling the grains.

## Handoff

```text
Exact multi-grain geometry:

- the train-crossing graph of a connected pure rhombic disk is connected;
- after deleting any crossing/rhombus set F, adjacent retained rhombi always lie in the same surviving train component;
- therefore every retained-grain boundary edge is either on the original outer boundary or adjacent to a deleted rhombus.

Hence

  sum_j P_j <= 2T+4|F|,

and since every triangle-free unit rhombus has area >=sqrt(3)/2,

  2 sqrt(pi*sqrt(3)/2) sum_j sqrt(R_j)
    <= 2T+4|F|.

This is the first exact physical interface budget for the current multi-grain Target B endpoint. To become decisive, the coherent decomposition must be produced with boundary-order rather than quadratic deletion cost.
```
