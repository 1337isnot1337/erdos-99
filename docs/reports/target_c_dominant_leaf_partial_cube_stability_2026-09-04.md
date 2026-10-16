<!-- theorem-state: {"artifact_id":"ART-FEF7AFDBA6EA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C99 candidate: dominant-leaf partial-cube stability

**Date:** 2026-09-04
**Repository base:** branch after audited C98 (`08510bdb`)
**Run type:** exact train-combinatorics + max-flow theorem
**Target:** one-leaf near-chain phase
**Depends on:** C11 total contact stress; C65 full visibility; C77 train pseudolines; C81 cut-flow method; C98 one-leaf concentration
**External combinatorial input:** region/tope graphs of pseudoline arrangements (more generally COMs) are partial cubes
**Status:** proved working result; audit pending
**LEVEL I STATUS:** STILL OPEN

C98 proves that the C71-B near-zero phase has one actual diameter edge `h_*=za` with beta weight `1-o(1)`. C99 converts this stress statement into a geometric train statement without assuming the exact C76/C80 chain face.

Let `P(za)` be the set of train tracks separating `z` and `a` in a pure simply connected strict-rhombic disk, and put

`k=k_(za)=|P(za)|`.

Then for every normalized KKT stress with

`b=beta_(za)>1/2`, C99 proves

`D <= k <= D/(2b-1)`.

If `b=1-eta`,

`0<=k-D <= 2D eta/(1-2eta)`.

Moreover, orient every separating train contribution `a_tau` from the `z` side to the `a` side and let

`u=(p_a-p_z)/D`.

Train coordinates give

`D u = sum_(tau in P) a_tau`, `|a_tau|=1`.

Hence the direction defect is exactly

`sum_(tau in P)|a_tau-u|^2 = 2(k-D)`.

Thus `b->1` forces the dominant diameter to cross only `D+o(D)` trains and forces their directions to be `L^2`-close to the diameter direction. This is the first direct stability bridge from C98 to C97's exact straight-chain geometry.

---

## 1. The rhombic contact graph is the chamber graph of the train arrangement

Use C77's train curves: through each rhombus join the midpoints of one pair of opposite contact edges; continue across opposite edges. A maximal train is a proper simple arc of the disk, two trains cross at most once, and a contact edge is crossed by exactly the train carrying that edge.

The train curves partition the disk into chambers. Locally, a rhombus is cut by its two crossing trains into four sectors, one incident to each rhombus vertex. Gluing sectors across contact edges identifies exactly the sectors incident to the same contact vertex. Hence:

- chambers are in bijection with contact vertices;
- crossing one chamber wall is crossing one contact edge;
- that wall belongs to the unique train label of the contact edge.

Assign to a chamber/vertex `v` the sign vector recording on which side of every train curve it lies. Adjacent contact vertices differ in exactly one sign, namely the label of their common contact edge.

The region graph of a pseudoline arrangement in a disk is a tope graph of a complex of oriented matroids and is a partial cube. Equivalently, the sign-vector embedding is isometric: graph distance is Hamming distance.

Therefore:

### Lemma C99.1 — train separation is contact distance

For any two contact vertices `x,y`,

`d_C(x,y)=#{tau: tau separates x and y}`.

In particular

`d_C(z,a)=k`.

A shortest contact path from `z` to `a` crosses every train in `P(za)` exactly once and no other train.

For the present disk one can also view this as the standard tope-graph property of the C77 pseudoline arrangement; no metric property of the rhombus angles is used.

## 2. A dominant diameter edge gives a large direct max flow

Fix the actual diameter edge `za` with KKT weight

`b=beta_(za)`.

Take any vertex set `U` in the positive contact graph with

`z in U`, `a notin U`.

Sum KKT equilibrium over `U`. Internal contact and diameter forces cancel. The crossing diameter-force sum contains the force of `za`, of magnitude `Db`, plus crossing forces from all other diameter edges. Their total beta weight is at most `1-b`, so their vector norm is at most `D(1-b)`.

Hence the crossing contact-force resultant has norm at least

`Db-D(1-b)=D(2b-1)`.

The scalar contact capacity of the cut is at least the norm of its force resultant. Thus, if `b>1/2`,

`cap_alpha(U)>=D(2b-1)`

for every `z`-`a` cut.

By max-flow/min-cut:

### Lemma C99.2 — dominant-edge flow

There is a contact flow from `z` to `a` of value

`F>=D(2b-1)`.

This is a one-leaf refinement of the C81 star-leaf cut argument and does not require a star-center decomposition.

## 3. Partial-cube distance converts flow into a train-count bound

Remove cycles from the flow and decompose it into simple `z`-to-`a` contact paths with nonnegative path weights `x_Q`. Every such path has at least

`d_C(z,a)=k`

edges by Lemma C99.1. Therefore its total absolute edge-flow mass satisfies

`sum_e |f_e| >= k F`.

On the other hand `|f_e|<=alpha_e`, and C11 gives the exact total contact capacity

`sum_e alpha_e=D^2`.

Thus

`k D(2b-1) <= kF <= D^2`.

### Theorem C99.3 — dominant-leaf train-count stability

For every actual diameter edge `za` of beta weight `b>1/2`,

`k_(za) <= D/(2b-1)`.

Since every contact path between points at Euclidean distance `D` has at least `D` unit edges,

`k_(za)>=D`.

Therefore, writing `b=1-eta` with `0<=eta<1/2`,

`0<=k-D
 <= D[1/(1-2eta)-1]
 = 2D eta/(1-2eta)`.

In particular `eta=o(1)` implies

`k=D+o(D)`.

The finite theorem also implies that if `2D eta/(1-2eta)<1`, then `k` is the unique integer in the interval `[D,D+1)`, a useful arithmetic rigidity regime when the diameter is correspondingly close to an integer.

## 4. Exact vector defect of the separating trains

Train coordinates give, for the oriented diameter vector,

`r=p_a-p_z=sum_(tau in P) a_tau`,

where each `a_tau=d_tau u_tau` is a unit vector oriented from the `z` side toward the `a` side.

Put

`u=r/D`.

Taking the dot product with `u` gives

`sum_(tau in P) u dot a_tau = D`.

Since `|u|=|a_tau|=1`,

`|a_tau-u|^2=2(1-u dot a_tau)`.

Summing:

### Theorem C99.4 — exact direction-defect identity

`sum_(tau in P)|a_tau-u|^2=2(k-D)`.

Combining with C99.3,

`sum_(tau in P)|a_tau-u|^2
 <= 4D eta/(1-2eta)`.

Consequences:

1. **mean-square alignment**

   `(1/k) sum |a_tau-u|^2 = O(eta)` when `eta=o(1)`;

2. **few macroscopic angular outliers**: for every fixed `rho>0`,

   `#{tau in P: |a_tau-u|>=rho}
    <= 4D eta/[(1-2eta)rho^2]`;

3. a shortest `z`-`a` contact path has exactly one edge from each separating train and therefore is a `D+o(D)`-edge near-geodesic whose edge directions have the same `L^2` alignment bound.

This is weight-free geometry after the single scalar beta concentration has been established.

## 5. Insert C98

C98 proves in the C71-B phase with `D epsilon->0` that one actual diameter edge `za` satisfies

`beta_(za)=1-o(1)`.

Apply C99 with `eta=1-beta_(za)`:

`k_(za)=D+o(D)`,

and

`sum_(tau in P(za))|a_tau-u|^2=o(D)`.

Thus the single-port near-zero phase contains a canonical **near-chain train atom**:

- it has only `o(D)` excess separator tracks beyond Euclidean diameter;
- all but `o(D)` separating tracks lie in any fixed angular neighborhood of the diameter direction;
- a shortest contact path crosses those tracks once each and is a near-straight unit-edge geodesic.

C97 rules out the exact endpoint `k=D`, all `a_tau=u`, in the canonical pure chain-face regime.

## 6. What C99 does not yet prove

C99 does not make the near-chain exact at the response-defect scale currently known. `D epsilon->0` gives `eta=o(1)`, not necessarily `eta=o(1/D)`, so `k-D` may still diverge sublinearly.

Nor does `L^2` alignment alone imply C97's exact terminal twist or C87's exact prefix staircase. A sublinear set of badly oriented separator tracks can carry all topological changes needed to evade the exact endpoint contradiction.

The next target is therefore finite-defect stability:

> charge every excess/bad separator train to either response defect `D epsilon`, nonstar beta mass, or outer-shell defect strongly enough to make `k-D=0` (or directly produce a unit triangle) for large global minimizers.

The new feature is that the exceptional train set is now `o(D)`, rather than a linear-sized unconstrained train system.

## 7. Literature note

The only external combinatorial input is the standard fact that chamber/tope graphs of pseudoline arrangements are partial cubes. For example, Chepoi--Knauer--Philibert describe pseudoline-arrangement region graphs as tope graphs/partial cubes, and Eppstein proves the corresponding pseudoline-arrangement graph is a partial cube via the halfspace-bit embedding. C77 supplies the required proper pseudoline arrangement from the rhombic train system.
