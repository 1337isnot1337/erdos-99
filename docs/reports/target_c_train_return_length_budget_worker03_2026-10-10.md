<!-- theorem-state: {"artifact_id":"ART-EFDC9677E3A7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — train returns, shared grids, and rigidity-forced linkage (Worker Slot 03)

> **Destination lifecycle:** imported as unreviewed research from source PR #950. The source proof audit is preserved as evidence, but neither report changes destination theorem-state. The result stops before endpoint overlap, a feasible finite competitor, or C-II/Level I closure.

**Date:** 2026-10-10\
**Repository commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`\
**State version:** `2026-10-10.audit.234`\
**Run type:** Target C-II proof research\
**Target:** C-II, train-return payment and loaded-hull geometry\
**Starting status:** canonical full-core train/return theorems; finite-move/payment obligation open\
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`\
**External literature search:** one 2026 preprint checked as contextual literature; no theorem imported\
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint

I used the fetched `main` tip and state lock, not the pre-existing local research branch. The assigned endpoint is the full-source finite-move/payment obligation in Target C-II. In particular, Audits 179 and 180 give a linear number of disjoint actual-contact returns from long physical strict-rhombus trains to distinct loaded vertices when `R_4/D^2 -> r>0`; Audit 235 sharpens the separator bound. The paths are in the full positive-contact graph, may have length zero, and had no individual route-length bound or face/interface payment.

The implication sought was

```text
new path-cost control -> source-compatible train/interface payment
                     -> same-cardinality endpoint with all lower and upper
                        constraints feasible -> strict contact/diameter gain
                     -> eliminate the quadratic-core C-II branch.
```

The new results supply a path-length quantile, couple a positive-density return family to one common source-realized coherent grid, and use core rigidity to extract a second linear family of vertex-disjoint attachment-to-grid paths. They do not yet align the two families at common attachment labels or supply movement/payment.

## 2. Strongest genuinely new result

**Classification:** proved candidate awaiting independent audit. It combines canonical Audits 179, 180, 206, and 235 with the canonical loaded near-unit adjacency, Type-II cell-tiling/coherence/grid theorems, and face-tail port access. The positive-length extraction, route-length quantile, and common-grid return coupling are not separate theorem-ledger claims.

### Statement

Consider a canonical unbounded C-II sequence in the scope of `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS`, with `D -> infinity` and `R_4/D^2 -> r>0`. Fix `epsilon in (0,r)`, and define

```text
a_* = (2/3) sqrt(r-epsilon),
ell = epsilon/(3 pi),
beta = 40/(pi sqrt(3)),
kappa = (sqrt(25 ell^2 + 4 beta a_* ell) - 5 ell)/(2 beta) > 0.
```

After deleting at most `O(D^(2/3))` trains from the Audit 179 long-train bank, choose one terminal vertex outside the loaded set on each remaining train. Audit 235 then supplies a family of `K_D` mutually vertex-disjoint, **nontrivial** actual-contact paths starting at distinct chosen unloaded terminal vertices and ending at distinct actual loaded vertices, with `liminf K_D/D >= kappa`. There is a choice of this Menger family for which, for each fixed

```text
t > pi/(2 sqrt(3) kappa),
```

at least

```text
(kappa - pi/(2 sqrt(3) t) - o(1)) D
```

of the paths have at most `tD` contact edges. In particular, at least `(kappa/2-o(1))D` returned trains have an endpoint-inclusive return path of at most

```text
(pi/(sqrt(3) kappa) + o(1)) D
```

contact edges. The bound counts paths in the actual full-source contact graph; every contact isolate remains in the Oler population bound. Thus the length quantile applies to genuine positive-length returns, not merely endpoint-inclusive paths that may pair a train terminal to itself.

### Removing zero-length terminals by hull-train depletion

Let `A_D` be the selected long bank from Audit 179 and let `H_L` be the canonical family of trains with at least one terminal occurrence on an actual unit loaded-hull side. For the fixed `epsilon`, every train in `A_D` has `d_tau>=L_D`, where `L_D=floor(epsilon D/(3 pi))=ell D+O(1)`. Audit 206 gives `R_H=O(D^(5/3))`, where `R_H` counts actual rhombus crossings incident to `H_L`. Each train `tau` is incident to `d_tau` such crossing incidences; a crossing with both ends in `H_L` contributes twice to the sum of train incidences and once to `R_H`. Therefore

```text
L_D * |A_D intersect H_L|
    <= sum_{tau in H_L} d_tau
    <= 2 R_H
    = O(D^(5/3)),
```

so `|A_D intersect H_L|=O(D^(2/3))`. Removing those trains leaves
`|A_D'| >= (a_*-o(1))D` long trains.

For each `tau in A_D'`, choose either one of its two terminal unit edges. If both endpoints of that edge belonged to the actual loaded set `B`, then they would be loaded endpoints at distance one. Since `D>=6` and `conv(B)` has positive area, canonical `C-LOADED-NEAR-UNIT-ADJACENCY` says that every such loaded pair is a side of `conv(B)`. The chosen train would then lie in `H_L`, contrary to `tau in A_D'`. Thus each chosen terminal edge has at least one endpoint outside `B`; choose that endpoint as the rail endpoint. The selected terminal set `X_D` is disjoint from `B`.

Apply the canonical Audit 235 separator inequality to these `a_D'=|A_D'|` distinct trains and these chosen rail endpoints. Its hypotheses allow an arbitrary one rail endpoint per train, so no inherited carrier route is needed. Since `a_D'/D>=a_*-o(1)` and `(L_D+1)/D->ell`, its quadratic limiting argument gives the same lower bound `liminf K_D/D>=kappa`. Menger's endpoints lie in disjoint vertex sets `X_D` and `B`, hence none of the returned paths has length zero. This proves the stated nontrivial family.

This argument only deletes trains from the auxiliary selected family; it deletes no source point, contact, or rhombus from the original configuration. The positive-area loaded hull and all-source hypotheses are precisely those of the canonical inputs.

### Concentrating the positive returns in one unloaded component

The canonical `C-UNIFORM-HARMONIC-CELL-AREA` theorem bounds the number of unloaded connected components of the positive-contact core by a fixed integer `M_0` along the sequence, in either exhaustive C-II branch. Assign each train in `A_D'` to the unloaded component containing its chosen terminal vertex. By pigeonhole, for every sufficiently large `D` some component `I_D` contains the chosen roots of a family `A_D(I)` of at least

```text
(a_*/M_0 - o(1)) D
```

distinct long trains. Put

```text
a_I = a_*/M_0,
kappa_I = (sqrt(25 ell^2 + 4 beta a_I ell) - 5 ell)/(2 beta) > 0.
```

Apply the same Audit 235 separator inequality to just `A_D(I)` and their already chosen unloaded rail endpoints. It gives at least `(kappa_I-o(1))D` vertex-disjoint paths from these roots to distinct vertices of `B`. Truncate each path at its first vertex in `B`. Every earlier vertex lies in `I`, and the last is an actual loaded attachment of `I`; the truncated paths remain vertex-disjoint, nontrivial, and end at distinct loaded attachments. Thus one source-realized unloaded component contains linearly many selected terminals of distinct long trains and supports linearly many disjoint actual-contact routes from those terminals to its own loaded attachment set.

The full-source Oler count gives the same quantile inside this component: for every fixed `theta in (0,1)`, at least `(theta*kappa_I-o(1))D` truncated paths have at most

```text
pi / (2 sqrt(3) (1-theta) kappa_I) * D
```

contact edges. The constant may be smaller than `kappa` because of the component pigeonhole. Contact-isolated source points are still counted in the full-source Oler bound and remain untouched.

### Type-II train-root access to coherent grids

In the Type-II branch, fix any `lambda>0` and choose `eta=kappa_I/4`. The canonical `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` theorem supplies a fixed radius `rho_0>0` such that fewer than `eta D` attachment incidences fail to have an actual contact route of length `<lambda D` from the attachment to every component point within distance `rho_0D`. Decrease the radius if needed so that `rho=min(rho_0,1/2)` lies in `(0,1)`; the route conclusion remains true for this smaller ball.

Apply `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` in the same component `I_D` at each loaded attachment `b` reached by the component return family, with this `rho` and any fixed phase tolerance in `(0,pi/6)`. It supplies an actual coherent train grid in `I_D`, with both shores of size at least `cD` for fixed `c>0`, all grid vertices within `rho D` of `b`. All but fewer than `eta D` of the selected return endpoints are good attachment incidences. From the Oler quantile with `theta=1/2`, there are at least `(kappa_I/2-o(1))D` returns of length at most `(pi/(sqrt(3)kappa_I)+o(1))D`; after discarding bad attachments, at least `(kappa_I/4-o(1))D` distinct long-train roots remain. Each has an actual positive-contact route of length at most

```text
(pi/(sqrt(3) kappa_I) + lambda + o(1)) D
```

to every vertex of its own coherent local grid: concatenate the truncated train return with the attachment-to-grid route and erase any loops. The routes after concatenation need not be mutually disjoint, and the grids may overlap. This is a source-realized train-to-grid access statement in Type II; it introduces no scaffold vertices and leaves all contact isolates in the source.

### One common coherent grid for a linear return-port family

The cell geometry lets us strengthen individual access to a common target. Fix
`lambda>0`, a phase tolerance `epsilon_g in (0,pi/6)`, and the quadratic-core
sequence and train-bank parameter `epsilon` above. Put `kappa=kappa_I`. Apply
`C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` with `eta=kappa/8`, obtaining a fixed
port radius `rho_0>0`. Fix any `rho in (0,min(rho_0/2,1))` for the cell crop.
From `C-UNIFORM-HARMONIC-CELL-AREA`, choose fixed constants `alpha>0` and
`d_0=sin(pi/12)/4` such that every unloaded cell `P_I` has
`area(P_I)>=alpha D^2` and `diam(P_I)>=d_0D` eventually. Set

```text
r_0 = d_0*alpha/6,
delta = rho*r_0/2,
N = ceil(pi/delta),
c_port = kappa/(4N).
```

For every sufficiently large source, there are at least
`(c_port-o(1))*D` distinct actual loaded attachments `a` in one unloaded
component `I_D` with all of the following properties:

- Each `a` is the first loaded endpoint of a nontrivial return from a distinct
  selected long-train terminal. These train-terminal-to-attachment paths are
  mutually vertex-disjoint and have at most
  `(pi/(sqrt(3)*kappa)+o(1))*D` contact edges.
- A single complete `epsilon_g`-coherent train grid `G_D`, with both shores at
  least `c_grid D` for some fixed `c_grid>0`, lies in `I_D` and within the
  closed Euclidean ball `B(a,rho_0D)` for every selected attachment `a`.
- From each selected `a`, every vertex of this same grid `G_D` is reachable by
  an actual contact route of fewer than `lambda D` edges. Thus each selected
  train terminal has a source contact route to every vertex of `G_D` of length
  at most `(pi/(sqrt(3)*kappa)+lambda+o(1))*D`.

The terminal-to-attachment paths are mutually vertex-disjoint. Their
attachment-to-grid continuations are not asserted to be disjoint.

### Proof of the common-grid statement

The `theta=1/2` Oler quantile gives at least
`(kappa/2-o(1))*D` vertex-disjoint, nontrivial train-terminal returns, each
with the stated linear length bound. The face-tail theorem with
`eta=kappa/8` excludes fewer than `kappa D/8` of their distinct attachment
incidences. At least `(kappa/4-o(1))*D` return endpoints therefore have
short contact routes to every source point in their `rho_0D` balls. Retain
these good endpoints in `I_D`.

Let `P=P_{I_D}` and `A=area(P)`. Its perimeter is at most `pi D`. Choose a
diametral segment of length `d=diam(P)`. The projection of `P` onto the
segment has length `d`, while its total perpendicular width `w` satisfies
`A<=d*w`. Thus `w>=alpha D`, since `d<=D`. One of the two sides of the
diametral line has a point at height at least `w/2>=alpha D/2`. The triangle
formed by this point and the diametral segment lies in `P`, has area at least
`d*w/4 >= d_0*alpha*D^2/4`, and perimeter at most `3D`. Its inradius is at
least `d_0*alpha*D/6=r_0D`. Hence `P` contains a disk `B(o,r_0D)`.

The good attachments are vertices of the convex polygon `P`. Partition its
boundary into at most `N=ceil(pi/delta)` arcs of length at most `delta D`.
One arc contains at least `(kappa/(4N)-o(1))*D` of the good return
endpoints. Fix one such endpoint `a_0`; every other selected endpoint `a`
on this arc satisfies `|a-a_0|<=delta D`.

The canonical Type-II cell tiling gives
`Delta_I=area(P)-A_{4,I}=o(D^2)`, uniformly over unloaded cells, where
`A_{4,I}` is the area of the actual unloaded-only strict rhombi assigned to
`I_D`. For each selected attachment form the convex crop

```text
Q_a = (1-rho)*a + rho*P.
```
The disk

```text
Q_* = (1-rho)*a_0 + rho*B(o,r_0D/2)
```
is contained in every `Q_a`. Indeed, for `x in B(o,r_0D/2)`, set
`x_a=x+((1-rho)/rho)*(a_0-a)`. Since
`delta=rho*r_0/2`, we have
`|x_a-o|<=r_0D/2+(1-rho)r_0D/2<r_0D`, so `x_a in P`, and
`(1-rho)*a+rho*x_a=(1-rho)*a_0+rho*x`. The common disk `Q_*` has area
`pi*rho^2*r_0^2*D^2/4`, lies in `P`, and is contained in `B(a,rho D)`
for every selected endpoint `a`.

The cell deficit `Delta_I=o(D^2)` and the `O(D)` area of rhombi meeting
`partial Q_*` leave a positive quadratic area of actual unloaded-only
strict rhombi wholly inside `Q_*`. The fixed-phase cut from
`C-COHERENT-GRAINS` deletes only `O_{epsilon_g}(D)` additional rhombi and
has total interface perimeter `O_{epsilon_g}(D)`. Cutting at `partial Q_*`
adds only `O(D)` perimeter. Therefore the retained coherent components
inside `Q_*` have total rhombus area `Omega(D^2)` and total perimeter
`O(D)`. If component `j` contains `R_j` rhombi and has perimeter `P_j`,
then each rhombus has area at least `a_0=sqrt(3)/2`, and planar isoperimetry
gives `P_j>=2*sqrt(pi*a_0*R_j)`. The total-perimeter bound implies
`sum_j sqrt(R_j)=O(D)`; the total-area lower bound implies
`sum_j R_j=Omega(D^2)`. Hence one component contains `Omega(D^2)` rhombi.
Apply the proof of canonical `C-PSEUDO-GRID` to this cropped finite rhombic
component itself. If it has `R_j=Omega(D^2)` faces and local train count
`T_j=P_j/2=O(D)`, Theorem 10.6 gives `R_j<=T_j^2/4` and a triangle-free
pseudosegment crossing graph. Fox--Pach extraction gives complete crossing
shores of size at least `c_PS R_j/T_j`; phase purification loses at most a
factor two on each shore. Thus both shores have size at least `c_grid D` for
some fixed `c_grid>0`. Here each train is the local track of the **cropped
complex**, stopped where it meets the crop boundary; the selected tracks and
their crossing rhombi therefore use only source vertices in `Q_*`. This is
the finite proof of the grid extraction, not an assumption that tracks from a
larger uncropped grain stay inside the crop. Every grid vertex is therefore
in `I_D` and within `rho D<rho_0D` of each selected attachment. The face-tail
property supplies the claimed actual contact routes. Concatenation with the
disjoint train returns proves the terminal-to-grid length bound.

The common-grid extraction preserves every source label, including contact
isolates. It controls the number of ports and gives them one common actual grid
target; by itself it does not control congestion in the continuation paths or
give a finite motion.

### Rigidity forces a linear attachment-to-grid linkage

The common grid has a linear Euclidean diameter, not merely linear shore sizes.
If its shores have sizes at least `c_grid D`, their `c_grid^2 D^2` crossing
pairs give that many distinct strict unit rhombi. Each rhombus has acute angle
at least `pi/3` (its short diagonal is at least one), hence area at least
`a_0=sqrt(3)/2`; distinct face interiors are disjoint. If `X_0` is the set
of their source vertices, then

```text
area(conv(X_0)) >= a_0*c_grid^2*D^2,
diam(X_0) >= gamma*D,
gamma = c_grid*sqrt(2*sqrt(3)/pi) > 0,
```

by the isodiametric inequality. Let `X_D` be the vertex set of the connected
actual contact subgraph consisting of the selected grid trains and crossing
rhombi. It lies in the same unloaded component, contains `X_0`, and therefore
also has diameter at least `gamma D`.

**Rigidity-brace lemma.** In the canonical C-II core, if `X` is any connected
set of unloaded core vertices and `G_X` is the induced unit-contact graph on
`X`, then

```text
|delta_C(X)| >= diam(X) + 2,
```

where `delta_C(X)` is the set of actual unit contacts with exactly one endpoint
in `X`. The straight unit-contact embedding is planar: if two nonincident unit
segments cross at `z`, write their endpoint distances from `z` as `s,1-s` and
`t,1-t`, and let `phi<=pi/2` be the acute angle between one pair of crossing
rays. The squared distances between the two endpoint pairs on those rays and
on the opposite rays sum to

```text
s^2+(1-s)^2+t^2+(1-t)^2
 - 2*cos(phi)*(s*t+(1-s)*(1-t)) < 2,
```

contradicting the unit separation of all four endpoints. The induced graph is
also triangle-free. To see the graph sparsity bound, put `q=|X|` and
`e_X=|E(G_X)|`.
For a 2-connected block `B` of the triangle-free planar graph `G_X`, let `p_B`
be the length of its outer facial cycle. Euler's formula and the fact that every
face has length at least four give

```text
|E(B)| <= 2|V(B)| - p_B/2 - 2.
```

A bridge block has `2|V(B)|-|E(B)|-2=1`. The block-cut tree identity
`q=1+sum_B(|V(B)|-1)` consequently yields

```text
2q-e_X >= 2 + sum_{2-connected B} p_B/2 + number_of_bridge_blocks
        >= diam(X)+2.
```

For the last inequality, a 2-connected block's outer cycle encloses its
vertices and has perimeter at least twice their Euclidean diameter; along the
block-cut-tree path joining a diametral pair, the sum of block diameters bounds
the pair's Euclidean distance. Since the rigidity-matrix rank of `G_X` is at
most `e_X`, its infinitesimal-flex space has dimension at least
`2q-e_X >= diam(X)+2`.

Now suppose fewer than `diam(X)+2` contact edges leave `X`. Their linearized
bar equations impose fewer conditions than this flex-space dimension. There is
a nonzero flex of `G_X` satisfying every crossing contact row; extend it by
zero to the rest of the core. Because `X` is unloaded, no strong active
diameter row is incident to it. The extension is therefore a nonzero flex of
the full mixed contact/diameter framework, contradicting canonical `C-ZRF`,
which has rank `2|V|-3`. It cannot be a rigid motion: the two distinct loaded
endpoints of an active diameter edge lie outside `X` and have zero velocity.
This proves the lemma. It is a core rigidity argument only; all contact
isolates stay in the original source and are not moved or dropped.

Use the endpoint-inclusive form of vertex Menger. Let `S` be any vertex set
such that, after deleting `S`, no vertex of `A_I-S` is connected to a vertex
of `X_D-S` in the contact graph induced by `I_D union A_I`. The separator may
contain loaded attachments or grid vertices. Let `U_1,...,U_m` be the distinct
components of the deleted graph meeting `X_D-S`. Each `U_j` is wholly
unloaded. Every actual contact leaving it ends in `S`: any other unloaded
neighbor belongs to the same `I_D`, while an unsuppressed loaded neighbor
would connect it to `A_I-S`. Apply the brace lemma to any selected subfamily
of these components. With `e_S` the number of actual contacts internal to
`S`, the degree bound gives

```text
sum_j (diam(U_j)+2) <= sum_j |delta_C(U_j)|
                       <= 5|S|-2e_S.                 (R)
```

Choose `p,q in X_D` at Euclidean distance `diam(X_D)`. The grid contact
subgraph is connected. Contract each `U_j` to a node, retain the vertices of
`S`, and follow a simple quotient path from the node containing `p` to the
node containing `q`. Only components meeting the grid are needed. If both
endpoints lie in the same `U_j`, use that component alone. Write `l` for the
number of component nodes on the selected path, `e_U` for the number of its
two endpoints lying in components, and `t_S` for its edges with both ends in
`S`. Each component node is used once. Its entry and exit points have
Euclidean distance at most `diam(U_j)`; every edge between quotient nodes
is an actual unit contact. There are exactly `2l-e_U` edges between a
component and `S`, and `t_S<=e_S`. The triangle inequality and (R), applied
to these `l` components, therefore give

```text
|p-q| <= sum_selected_j diam(U_j) + 2l-e_U+t_S
      <= 5|S|-2e_S-e_U+t_S
      <= 5|S|.
```

When the quotient path uses only vertices of `S`, the same inequality follows
directly from its at most `|S|-1` unit edges. Thus **every** endpoint-inclusive
separator has size at least `diam(X_D)/5`, including separators that delete
part or all of either terminal set. Restricting the argument to separators
disjoint from both terminal sets would not justify distinct-endpoint Menger.

Vertex Menger therefore gives at least
`(gamma/5-o(1))*D` pairwise vertex-disjoint actual-contact paths from distinct
loaded attachments of `I_D` to distinct vertices of the common grid. The
finite Oler bound on the **full** source gives a length quantile as well: for
each fixed `theta in (0,1)`, at least
`(theta*gamma/5-o(1))*D` of these paths have at most

```text
5*pi/(2*sqrt(3)*(1-theta)*gamma) * D
```

edges. Thus the attachment-to-grid family can be made linearly large,
vertex-disjoint, and `O(D)` in length without summing face charges. Isolates
remain included in the Oler population bound.

The degree bound used here is exact: at any source vertex, consecutive contact
directions have angular gaps strictly greater than `pi/3`; a smaller gap would
put two neighbors less than one apart, and equality would make a unit
equilateral triangle. Thus there are at most five contact neighbors.

This does **not** yet give root-to-grid paths from the selected long trains.
The rigidity/Menger linkage starts at the full attachment set, while Audit 235's
disjoint return linkage ends at another subset of that set. If the two endpoint
subsets have a common subfamily of `sD` labels, their paths can be composed at
those labels: any separator from train roots to the grid must hit one of the
two paths for each common label, and each separator vertex hits at most one path
from each linkage, so it has size at least `sD/2`. Menger then gives a linear
root-to-grid linkage. The exact remaining endpoint issue is to prove such a
linear common-label overlap (or an equivalent gammoid-rank inequality); path
counts alone do not imply it.
### Proof

Let `n_D` be the number of source points. The finite Oler inequality (shared theory 03, Lemma 21.1) applies to the full unit-separated source in its convex hull. The hull has diameter `D`, area at most `pi D^2/4` by the isodiametric inequality, and perimeter at most `pi D` by Cauchy's perimeter formula. With `a_0=sqrt(3)/2`,

```text
n_D <= area/a_0 + perimeter/2 + 1
    <= pi D^2/(2 sqrt(3)) + pi D/2 + 1.
```

Write `P_1,...,P_{K_D}` for the pairwise vertex-disjoint paths supplied by Audit 235, and let `ell_i` be the number of contact edges in `P_i`. A path with `ell_i` edges contains `ell_i+1` distinct source vertices. The path vertex sets are disjoint, so

```text
sum_i (ell_i+1) <= n_D,
sum_i ell_i <= n_D-K_D.
```

For fixed `t>0`, every path with `ell_i>tD` contributes more than `tD` to this sum. Therefore

```text
#{i : ell_i>tD} <= (n_D-K_D)/(tD)
                  <= (pi/(2 sqrt(3) t) + o(1))D.
```

Since `K_D >= (kappa-o(1))D`, subtraction gives

```text
#{i : ell_i<=tD} >= (kappa - pi/(2 sqrt(3)t) - o(1))D.
```

Taking `t=pi/(sqrt(3)kappa)` proves the particular half-bank bound. The proof uses no identification of a contact path with a motion, and no source labels are removed.

### Full length quantile and optimized return constant

The same counting argument gives the full tradeoff: for every fixed
`theta in (0,1)` and every admissible `epsilon`, at least
`(theta*kappa(epsilon)-o(1))*D` paths have at most

```text
pi / (2 sqrt(3) (1-theta) kappa(epsilon)) * D
```

contact edges. Here `theta` is the retained fraction of the Audit 235 return
bank; choosing `theta=1/2` gives the preceding bound.

The constant can be optimized over the proof parameter `epsilon`. Put
`c=1/(3*pi)`, so `ell=c*epsilon`, and regard `kappa(epsilon)` as the positive
root of

```text
F(epsilon,k) = beta*k^2 + 5*c*epsilon*k
               - (2/3)*c*epsilon*sqrt(r-epsilon) = 0.
```

It tends to zero at both ends of `(0,r)`, so its maximum is attained inside.
Implicit differentiation gives the stationary equation

```text
5*kappa + epsilon/(3*sqrt(r-epsilon)) = (2/3)*sqrt(r-epsilon).
```

Writing `u=epsilon/r`, this and `F=0` are equivalent to

```text
64*(2-3*u)^4 = 75*r*u^4*(1-u),   0 < u < 2/3,
kappa_* = sqrt(r)*(2-3*u)/(15*sqrt(1-u)).
```

The equation has exactly one root in `(0,2/3)`: its left side strictly
decreases there and its right side strictly increases. The stationary equation
forces `epsilon<2r/3`, so this root is the unique critical point and hence the
global maximum. Thus the full quantile holds with `kappa_*` in place of
`kappa(epsilon)`. For example, at the canonical near-disk quadratic-core value
`r=pi/(2*sqrt(3))`, the root is approximately `u=0.52014809`, giving
`kappa_*=0.04028549`; half of these returns have at most `45.0237*D+o(D)`
edges. This numerical evaluation is illustrative; the algebraic formula is the
claim.

### Dependencies

- `C-QUADRATIC-CORE-TRAIN-BANK` and `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS`, canonical in `docs/state/theorem-state.yaml`; exact return constant and hypotheses are in `docs/audits/target_c_oler_sharp_separator_independent_audit_2026-10-10.md` (Audit 235), sharpening Audits 179–180.
- `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`, canonical from Audit 206, with `R_H=O(D^(5/3))` as stated in `docs/audits/target_c_midpoint_and_quantitative_hull_train_independent_audit_2026-10-09.md`.
- `C-LOADED-NEAR-UNIT-ADJACENCY`, canonical in `docs/state/theorem-state.yaml`, with its exact finite threshold and positive-area loaded-hull scope in `docs/reports/target_c_loaded_near_unit_hull_adjacency_2026-10-01.md`.
- `C-UNIFORM-HARMONIC-CELL-AREA`, canonical from Audit 173, giving the fixed finite bound `M_0` on unloaded components in either branch.
- `C-ZRF`, canonical on the nonisolated positive-contact core `V`: the mixed contact/strong-diameter rigidity matrix has rank `2|V|-3`; no rigidity or motion claim is extended to contact isolates.
- In Type II only, `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` and `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY`, canonical from Audit 173 and its supplement, respectively give the local grid and attachment-to-grid contact routes.
- The common-grid argument also uses canonical `C-HARMONIC-CELL-TILING` (cell deficit `o(D^2)`), `C-COHERENT-GRAINS` (the fixed-phase `O(D)` deletion/interface budget), and the proof of `C-PSEUDO-GRID`, re-applied to the cropped finite complex with all train tracks stopped at its cut boundary.
- Finite Oler, shared theory 03, Lemma 21.1, `docs/theory/03-oler-shell.md`.
- Isodiametric inequality and Cauchy's perimeter formula, with the stated diameter normalization.

No reports outside the canonical route were used as premises.

For context only, I checked Archit Das, “Stress, rigidity and rhombic reductions for an
Erdős minimum-diameter problem (Problem #99),” Zenodo, 2026, DOI
[`10.5281/zenodo.22768362`](https://doi.org/10.5281/zenodo.22768362). Its idealized
rhombus-disk section formulates the unresolved obstruction as boundary pinning of
train-track rotations by diametral pairs. I import no result from that preprint; the
present incidence corollary is derived from the canonical repository theorems above.

The nonadvancing deep-cap check additionally uses `C-QUADRATIC-CORE-LOADED-CHORD-CAP-EXTRACTION`, `C-QUADRATIC-CORE-DEEP-CAP-GRID-RETURNS`, and `C-PSEUDO-GRID` from `docs/state/theorem-state.yaml`, plus `C-CORE-UNLOADED-SEPARATOR-AREA-BOUND` from Audit 235. These inputs are canonical at the recorded state version.

### Marked-rail separator check (valid, but redundant)

I also checked whether Audit 235's separator-area budget improves the return count from Audit 189's deep cap grid. It gives the following necessary compatibility inequality, but the resulting count is weaker than the existing Audit 133 return bound. Let `A_D,B_D` be the two phase-pure shores in the Audit 189 grid inside `W`, and let

```text
alpha_A = liminf |A_D|/D > 0,
alpha_B = liminf |B_D|/D > 0,
delta   = liminf h_D/D > 0,
lambda  = alpha_B/2,
beta    = 40/(pi sqrt(3)),
kappa_grid = (sqrt(25 lambda^2 + 4 beta alpha_A lambda) - 5 lambda)/(2 beta).
```

Here `h_D=A_G/(8 pi D)` is the Audit 189 cap depth. Then

```text
delta * kappa_grid <= pi/(2 sqrt(3)).
```

Write `K_cap` for the geometric cap and `C_*` for the positive-contact core graph. To prove the bound, each `A_D` track crosses every `B_D` track in a distinct strict rhombus. Its actual rail inside `W` therefore contains a simple contact subpath of at least `|B_D|` edges. Each source vertex lies on at most five selected rail subpaths: distinct local trains use distinct contact edges at a common vertex, and the positive-contact degree is at most five. When `|B_D|>=4`, Hall's theorem gives distinct marked vertices, one on each `A_D` rail: for any `s` rails the union of their vertices has size at least `s(|B_D|+1)/5 >= s`. From each selected mark, choose a one-sided rail subpath of `L_D=floor(|B_D|/2)` edges; it remains inside `W`.

The marked points form a distinct source set `X_D`. For any vertex separator `S` of size `k` from `X_D` to the loaded set `B`, let `U` be the union of components of `C_* - S` meeting `X_D - S`. At most `5k` selected subpaths meet `S`. Every unhit subpath lies in the component of the core graph `C_* - S` containing its marked vertex, so it is counted by `U`; each vertex is counted on at most five such subpaths. Thus

```text
(|A_D|-5k)_+ (L_D+1) <= 5|U|
                         <= beta k^2 + 10k,
```

where the second inequality is Audit 235. If `K_D` is the minimum separator size, the limiting quadratic gives `liminf K_D/D >= kappa_grid`.

The same-cell Audit 189 package gives `W subset (K_cap)_{-h_D}`, and every loaded endpoint is outside the interior of `K_cap`. Hence each marked point has Euclidean distance at least `h_D` from the loaded set. Unit contact edges imply every `X_D`-to-`B` path has at least `h_D` edges. Menger supplies `K_D` vertex-disjoint such paths; counting their vertices gives `n_D >= K_D(h_D+1)`. The finite Oler bound above yields `limsup n_D/D^2 <= pi/(2 sqrt(3))`, proving the displayed inequality.

This does not sharpen Audit 189. Its `|A_D| x |B_D|` grid supplies `R=|A_D||B_D|` actual rhombus crossings, so the canonical Audit 133 return theorem already gives `p >= F(R)`, with `F(R)=(sqrt(25+4cR)-5)/(2c)` and `c=8 pi/sqrt(3)`. If `|A_D|/D -> alpha_A` and `|B_D|/D -> alpha_B`, this has limiting return density `sqrt(alpha_A alpha_B/c)`. Our separator root satisfies

```text
beta kappa_grid^2 + (5 alpha_B/2) kappa_grid = alpha_A alpha_B/2,
```

so `kappa_grid < sqrt(alpha_A alpha_B/(2 beta))`. Since `2 beta=80/(pi sqrt(3)) > 8 pi/sqrt(3)=c` (equivalently `pi^2<10`), this is strictly below Audit 133's limiting lower bound. The calculation is a valid cut-count extension to marked local rails, but it does not add a new canonical capacity or eliminate a branch. All source labels, including contact isolates, remain in the Oler bound.

## 3. Alternative mechanisms and hostile checks

### Geometric train shear

A single strict unit-rhombus train has a local shear parameter: its unit sides remain unit as the angle changes inside `(pi/3,2pi/3)`, keeping both diagonals at least one. This makes a train a plausible source of a discrete replacement. The canonical return paths do not specify which crossing train or face may absorb the endpoint motion. Intersecting train constraints, new lower pairs, every actual diameter upper pair, and retained isolates all remain unchecked. Thus no finite shear follows from the path family.

### Face-defect route payment

Audit 134 gives a fixed-port route of length at most `(4/sqrt(3))R + 15N + 5Q_sigma`, where `N` counts nearby loaded attachments and `Q_sigma` charges exceptional augmented faces met by the straight segment between the port and target. Summing these inequalities over the disjoint Menger paths is not justified: disjointness applies to the graph paths, while distinct straight port-target segments may meet the same charged face and nearby-attachment ball many times. The global face-tail allowance can therefore be counted repeatedly. A valid multicommodity theorem must charge actual path incidences with a proved multiplicity bound, or produce paths whose charged face sets and attachment neighborhoods have bounded overlap. The Oler result above bounds path lengths in aggregate but does not provide this missing payment.

### Stress-weighted path allocation

For an unloaded component `I` with positive contact equilibrium, write the equilibrium at each `x in I` as `sum_{y~x} lambda_xy (y-x)=0`, with `lambda_xy>0`. For any scalar `u` on `I` extended by zero to the loaded attachments `A`, summing the equations after multiplication by `u_x` gives the exact vector identity

```text
sum_{xy internal to I} lambda_xy (u_x-u_y)(y-x)
  + sum_{x in I, a in A} lambda_xa u_x(a-x) = 0.
```

An indicator `u=1_U` gives positive-stress force balance across the contact cut of `U`. This is compatible with the pinned-rank proof behind Audit 235, but it does not put a uniform positive stress amount on any selected train terminal or Menger path. Positive support alone cannot price those paths. The exact missing bridge is a source-uniform lower bound or a stress-flow decomposition that assigns a nonzero, nonreused load to a linear subfamily of returns and then integrates that load to a finite endpoint.

### Regression checks

- Audit 235 explicitly permits length-zero returns for arbitrary selected terminals. The new family avoids that endpoint case by first removing the `O(D^(2/3))` hull-ended trains and selecting unloaded endpoints on every remaining terminal edge.
- The loaded-pair adjacency input applies because the relevant terminal edge has length exactly one and both endpoints, if loaded, lie in the full actual loaded set with positive-area hull. It is not applied to a source-hull side or an auxiliary scaffold.
- The factor two in `sum_{tau in H_L} d_tau <= 2 R_H` allows every rhombus crossing to have both train labels in `H_L`; it does not assume the depleted trains are crossing-disjoint.
- The removed `O(D^(2/3))` trains are negligible against the fixed-epsilon bank size `(a_*-o(1))D`; no uniformity as `epsilon` tends to zero is used.
- Component concentration counts only unloaded connected components of the positive-contact core, exactly the objects in `C-UNIFORM-HARMONIC-CELL-AREA`. It does not identify or discard contact isolates. Truncation at the first loaded point is required: the original Menger path after that point need not remain in the same unloaded component.
- Type-II grid access uses the face-tail theorem only on the distinct attachment incidences selected by the truncated paths. Its exceptional count is `eta D`; choosing `eta=kappa_I/4` leaves a linear good subfamily after the half-bank route-length quantile. Concatenated routes can overlap, so this does not provide a multicommodity face-charge bound.
- Audit 179's common carrier can reuse bottlenecks. The new proof uses Audit 235's vertex-disjoint paths in the full contact graph, not carrier routes.
- Audit 186's shared-carrier example has artificial pins and is nonglobal; it is not used to contradict the canonical return theorem.
- The `4/sqrt(3)` factor in Audit 134 is necessary by its exact rhombus regression; no sharper route stretch is assumed.
- The bound is an average/quantile consequence. It does not imply that every return is `O(D)`, that a bounded route can be moved, or that any diameter pair shortens.
- Contact isolates enter `n_D` and remain fixed as source constraints. No isolate is deleted or assigned a core stress coordinate.

The linear route-length scale cannot be improved from disjointness, unit
separation, triangle-freeness, and diameter alone. For the exact Pell family in
the monotone-route regression, let `(p,q)` range over the solutions generated
from `(3,5)` by `(p,q)->(2p+q,3p+2q)`, and let `u=(1,0)`, `v=(c,s)` with
`c=(p^2-1)/(2p^2-1)`, `s=pq/(2p^2-1)`, and `q^2-3p^2=-2`. Every nonzero
integer displacement `iu+jv` has squared length
`i^2+j^2+2cij >= 1`, with equality only on the two coordinate axes. Thus the
patch

```text
S_N = { i*u + j*v : 0 <= i,j <= N }
```

is unit-separated and its unit-contact graph is the triangle-free rectangular
grid. Its diameter is `D_N=N*sqrt(2+2c)`. The `N+1` horizontal rows are
vertex-disjoint contact paths, each with `N` edges, so their lengths equal
`D_N/sqrt(2+2c)` and remain a positive constant times `D_N` as
`p -> infinity` (the ratio tends to `1/sqrt(3)`). This exact regression is not a
canonical global minimizer and its row endpoints are not asserted to be loaded
diameter endpoints. It only shows why a sublinear route bound needs the missing
source-specific loaded-hull or interface input.

## 4. Exact frontier effect

The proved candidate now supplies (i) a positive-density family of nontrivial returns with an `O(D)` route-length quantile, concentrated in one actual unloaded component; (ii) a common source-realized coherent grid accessible from a positive-density subfamily of these return endpoints; and (iii) independently, a positive-density family of vertex-disjoint `O(D)` contact paths from distinct loaded attachments of that component to the common grid. If a positive-density endpoint overlap is established, the two linkages compose to a source-realized train-root-to-grid linkage. The endpoint overlap is unproved, and no face/interface payment or finite move has been constructed. No C-II branch has been eliminated, and Level I remains open.

## 5. Exact remaining lemma

Prove a **linear endpoint-overlap or direct-flow theorem**: in every canonical Type-II quadratic-core sequence with `R_4/D^2 -> r>0`, show that the Audit-235 train-root-to-loaded-attachment linkage and the rigidity-forced loaded-attachment-to-common-grid linkage have a common attachment-label subfamily of size `cD` for some fixed `c>0`, or directly prove a linear vertex-disjoint linkage from selected long-train terminals to the common grid. Given such a linkage, construct a finite same-cardinality competitor retaining every source label, with all pairwise distances in `[1,D]`, and either diameter strictly below `D` or diameter `D` with lexicographically fewer (positive unit contacts, actual diameter pairs). Every lower pair, every old and newly active diameter pair, all grid and train constraints, and every contact-isolated point must be checked. This endpoint contradicts the canonical contact-minimal/diameter-pair-minimal choice and removes the Type-II quadratic-core branch; it does not by itself eliminate Type I or prove Level I.

## 6. Validation and limits

The hull-depletion argument is an asymptotic analytic deduction from canonical Audits 179, 206, and 235 and `C-LOADED-NEAR-UNIT-ADJACENCY`; component concentration additionally uses canonical Audit 173; the Type-II common-grid extraction uses Audit 173, its face-tail supplement, `C-HARMONIC-CELL-TILING`, `C-COHERENT-GRAINS`, and `C-PSEUDO-GRID`. The rigidity-brace lemma is a finite block-counting argument plus canonical `C-ZRF`; the disjoint attachment-to-grid linkage follows by vertex Menger, and its route-length quantile uses finite Oler on the full source. The parameter optimization and Pell-grid regression are analytic and exact; no script or finite certificate is required. The Pell regression is explicitly nonglobal. The separate marked-rail check also uses canonical Audits 189 and the pseudosegment-grid theorem; its inequality is weaker than Audit 133 and is recorded as a nonadvancing attempt. These route corollaries await independent audit. No theorem-state file, route map, or prompt was changed.

**Promotion recommendation:** independently check and, if accepted, register the nontrivial positive-length return extraction, same-component concentration, Type-II common-grid access, common-grid diameter estimate, rigidity-brace lemma, attachment-to-grid Menger family, and the Oler route-length quantiles as corollaries of the canonical claims listed above. Do not promote any finite-move or route-payment claim from them.
