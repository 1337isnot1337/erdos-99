> Generated reading edition · [exact source](../../../docs/reports/target_c_endpoint_ferrers_exclusion_2026-09-01.md) · source SHA-256 `6121819cf54c3da52271c9ac45cf0cdbe339f1b43727c7ef095e9e39b30cb491`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7D6EB18AE2FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C91: exclude the C89 endpoint by four Ferrers walls

**Date:** 2026-09-01  
**Repository base:** `2e9b914b` (main after C90 / PR #95)  
**Status:** LEVEL I STILL OPEN

C89 proves

`liminf T/D >= 2+Delta_2`,

where

`Delta_2=pi/(2sqrt(3))=0.9068996821...`,

and classifies equality: if `T/D -> 2+Delta_2`, then `q/D->2`, the C80 chain
direction is the unique heavy atomic center, and the positive-density atomic train
crossing graph is a star centered at that direction.

C91 proves that this endpoint-sharp phase is impossible. The reason is that the star
equality leaves at most two residual atomic directions, each at projective angle
`60 degrees` from the exact chain direction. After splitting each residual phase by
which `z`-to-`a` boundary arc contains its two train terminals, there are at most four
ordered train walls. Almost all trains in each wall cross more than half of the D
chain trains, so their crossing intervals are nested and hence Ferrers.

A complete `i x j` rectangle in one such wall is much more constrained than the
generic Cartesian bound: the chain side has exact length `i`, while the coherent
residual side has length `(1-o(1))j`. The parallelogram law gives

`i^2+j^2 <= D^2+o(D^2)`.

Summing the optimal circular Ferrers profiles over four walls gives at most

`0.8990689038... D^2`

crossings, strictly below the required

`Delta_2 D^2=0.9068996821...D^2`.

Therefore no asymptotic pure-rhombic chain-face survivor can approach the C89 lower
endpoint. In particular there is an absolute, currently non-explicit `epsilon_0>0`
such that every sufficiently large canonical pure-rhombic chain-face survivor obeys

`T/D >= 2+Delta_2+epsilon_0`.

---

## 1. Consequences of C89 equality

Assume for contradiction that a sequence of canonical pure-rhombic chain-face
survivors satisfies

`T/D -> 2+Delta_2`.

Put

`A=1+Delta_2`.

C89 gives

`q/D ->2`,

`q/T -> 2/(A+1)`,

and, for the limiting train-direction measure, chain-atom mass

`a=1/(A+1)`

and total atomic mass

`s=A/(A+1)`.

The exact C80 chain family `P` has `|P|=D`, so it asymptotically exhausts the chain
atom. The residual atomic population therefore has size

`B_res = (s-a)T+o(D) = Delta_2 D+o(D)`.

Also

`R=Delta_2 D^2+o(D^2)`.

C89's equality classification says that the positive-density atomic crossing graph is
a star centered at the chain direction. Target B Section 39.1 says every
positive-density crossing pair of atomic directions differs by projective angle
`pi/3`. Therefore every residual atom carrying positive mass is one of the two
projective directions

`phi_0+pi/3`, `phi_0-pi/3`

relative to the chain atom `phi_0`.

There are consequently at most two positive-mass residual atomic phase directions.
All leading crossing mass is between `P` and those residual atoms; crossings involving
the non-atomic part, residual-residual atomic pairs, or the `o(D)` excess near the
chain atom contribute only `o(D^2)`. Hence

`e(P,res)=Delta_2 D^2-o(D^2)`.

Since the trivial complete bipartite capacity is

`|P| B_res = Delta_2 D^2+o(D^2)`,

the total number of missing `P`-residual incidences is `o(D^2)`.

## 2. Four wall decomposition

Choose shrinking disjoint projective neighborhoods around the two possible residual
atomic directions so that they contain all but `o(D)` residual atomic trains and only
`o(D)` additional non-atomic trains. This is possible by a standard diagonal choice
because the remaining limiting measure is non-atomic at those two points.

For all sufficiently large terms, each neighborhood has projective diameter less
than `pi/3`. Two trains in the same neighborhood therefore cannot cross: a crossing
rhombus in a triangle-free unit rhombic complex has acute train-direction angle at
least `pi/3` (strictly greater in the strict-rhombic branch).

Every residual train is nonparallel to the chain direction, hence is not one of the
C80 trains `P`. By C90, both terminals of such a non-chain train lie on one of the two
boundary arcs `L,U` from `z` to `a`.

Thus the residual trains split, up to `o(D)` exceptions, into at most four classes:

`(+60,L)`, `(+60,U)`, `(-60,L)`, `(-60,U)`.

Call these the **residual walls**.

For a train `sigma` in a wall, its two boundary terminals cut off one subinterval of
that same boundary arc. A chain train `tau_j in P` crosses `sigma` exactly when the
terminal of `tau_j` on that boundary arc lies between the two terminals of `sigma`.
Because the `P` terminals occur in chain order, the `P`-neighborhood of `sigma` is one
consecutive interval

`J_sigma subseteq {1,...,D}`.

## 3. Almost every residual row has length more than D/2

The total `P`-residual missing incidence count is `o(D^2)`. Therefore the number of
residual trains with

`|J_sigma| <= D/2`

is `o(D)`: each such train alone misses at least `D/2` chain trains.

Delete these bad rows, as well as the earlier `o(D)` neighborhood exceptions. The
removed trains contribute only `o(D^2)` crossings.

Every remaining residual train is **good**:

`|J_sigma|>D/2`.

Fix one of the four walls. Its trains are pairwise noncrossing and have both boundary
terminals on the same boundary arc. Two disjoint proper arcs with endpoints on one
boundary interval have terminal subintervals that are either disjoint or nested. The
corresponding `P`-crossing intervals have the same relation.

Two good crossing intervals cannot be disjoint because each contains more than half
of `{1,...,D}`. Hence the good intervals in one wall are totally ordered by inclusion.
After sorting them by decreasing length, their `P` incidence matrix is a Ferrers
diagram with row lengths

`d_1>=d_2>=...>=d_b`.

This is the ordered-wall concentration that was missing from the historical Target A
Section 55 argument; here it follows from endpoint saturation plus the exact chain
atom.

## 4. Circular capacity of an all-ones rectangle

Consider the first `j` rows of one wall. Ferrers nesting says they all cross a common
set of `d_j` chain trains, producing an all-ones `d_j x j` train rectangle.

The trusted train-coordinate/Cartesian-block construction gives an additive grid with
four corner source vertices

`p`, `p+U`, `p+V`, `p+U+V`.

The `d_j` selected chain trains all have the exact C80 unit-edge direction `u`, so

`U=d_j u`,

`|U|=d_j`.

All `j` residual train directions lie in one shrinking phase neighborhood. Orient the
corresponding unit edge vectors consistently across the coherent grid. If the
neighborhood radius is `delta_D ->0`, then

`|V| >= j cos(delta_D)`.

Both diagonals of the corner parallelogram are source differences, so global diameter
`D` gives

`|U+V|<=D`,

`|U-V|<=D`.

The parallelogram law therefore yields

`|U|^2+|V|^2 <= D^2`,

and hence

`d_j^2 + j^2 cos^2(delta_D) <= D^2`.

Thus

`d_j <= sqrt(D^2-j^2 cos^2(delta_D))`.

This circle constraint is stronger here than the generic product bound from Target B
Theorem 10.9 because one train family is the exact straight C80 chain atom.

## 5. Optimal crossing count of one wall

Let a wall contain

`b=lambda D+o(D)`

good trains along a subsequence. Summing the preceding row bound and taking a Riemann
limit gives

`e_wall/D^2 <= F(lambda)+o(1)`,

where

`F(lambda)=integral_0^lambda sqrt(1-t^2) dt`

`= (lambda sqrt(1-lambda^2)+arcsin(lambda))/2`.

Here `0<=lambda<=Delta_2<1`.

The function `F` is concave on `[0,1]` because

`F''(lambda)=-lambda/sqrt(1-lambda^2)<=0`.

## 6. Four walls cannot carry the required rhombi

Pass to a subsequence on which the four wall-size ratios converge to

`lambda_1,...,lambda_4>=0`.

The bad and exceptional residual trains are `o(D)`, while the full residual atomic
population is `Delta_2 D+o(D)`. Hence

`lambda_1+...+lambda_4=Delta_2`.

By concavity and Jensen,

`sum_(r=1)^4 F(lambda_r)
 <= 4 F(Delta_2/4)`.

Numerically,

`4 F(Delta_2/4)=0.8990689038...`,

while

`Delta_2=0.9068996821...`.

The fixed gap is

`Delta_2-4F(Delta_2/4)=0.0078307783...>0`.

Therefore the total `P`-residual crossing count satisfies

`e(P,res) <= 0.8990689038...D^2+o(D^2)`,

contradicting the endpoint requirement

`e(P,res)=Delta_2 D^2-o(D^2)`.

### Theorem C91 — endpoint Ferrers exclusion

No asymptotic canonical pure-rhombic chain-face sequence can satisfy

`T/D -> 2+Delta_2`.

Equivalently, the endpoint-sharp branch of C89 is empty.

## 7. Uniform train-surplus consequence

Suppose there were no absolute positive gap above the C89 endpoint. Then for every
integer `m` one could choose a sufficiently large canonical pure-rhombic chain-face
survivor with

`T/D < 2+Delta_2+1/m`.

A diagonal sequence of such survivors would satisfy

`T/D ->2+Delta_2`,

contradicting C91.

Hence:

### Corollary C91.1 — strict chain-face train surplus

There exist absolute constants `epsilon_0>0` and `D_0` such that every canonical
pure-rhombic C80 chain-face survivor with `D>=D_0` satisfies

`T >= (2+Delta_2+epsilon_0)D`.

The current proof is compactness-based and does not extract a useful numerical value
of `epsilon_0`.

## 8. Frontier effect

C89 left two possibilities: a strict train-surplus branch and an endpoint-sharp atomic
star. C91 eliminates the latter. Therefore every sufficiently large canonical
pure-rhombic chain-face survivor pays a **uniform extra linear train population** above
`(2+Delta_2)D`.

The remaining task is to convert this train surplus, together with C88's quadratic
secondary-train separator budget and C90's macroscopic caterpillar cut, into a global
packing contradiction. The old endpoint escape through two or more ordered walls is
now closed: even four possible residual walls have insufficient circular Ferrers
capacity.
