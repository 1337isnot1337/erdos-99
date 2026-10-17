> Generated reading edition · [exact source](../../../docs/reports/target_c_forest_isolate_dispatch_2026-10-01.md) · source SHA-256 `e688b38aeebbe5f46fc87923be9ff67fc290c47dd156a1fb8a42c1f0e97b24b9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7FE50C7E45DA","canonical":true,"claim_ids":["C-LONG-PAIR-ISOLATE-DISPATCH"],"claim_statuses":{"C-LONG-PAIR-ISOLATE-DISPATCH":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — isolate dispatch with a diameter-component exception budget

`forest isolate dispatch -> at most d_H exceptional inactive upper constraints
for small ONE-SIGN core swaps -> near-unit obstruction or explicit exceptional
pair -> strict source competitor once both are eliminated`.

**Date:** 2026-10-01.  
**Starting commit/state:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`,
`2026-09-14.audit.51`.  
**Branch:** `swarm/sol/gap-stress-cycle-20261001`.  
**Mission continuation:** extend the newly inspected cyclic isolate dispatch in
PR #600 to the forest branch without dropping isolated source points.  
**Classification:** canonical in `2026-10-05.audit.60` as `C-LONG-PAIR-ISOLATE-DISPATCH` for Sections 1--8.2; later O--O/block-transposition specializations remain unreviewed.  
**Level I / C-II:** OPEN / OPEN.

## 1. Exact finite theorem

Use the canonical contact-minimal, then diameter-pair-minimal triangle-free global
source A. Let V be its nonisolated positive-contact core; retain `Z=A\V`. Let
H be the full actual diameter graph, B its endpoint set, `q=|B|`, `h=|H|`, and
`d_H=q-h`. Put

```math
L=\sqrt{D^2-1},\qquad \gamma=D-L.
```

There is a **fixed** set E of inactive source pairs longer than L, and a fixed
map assigning each isolate either an anchor in B or no anchor, with the following
properties:

- If H is cyclic, E is empty.
- If H is a forest and the full long-pair graph T is a forest, `|E|<=d_H-1`.
- If H is a forest and T is cyclic, `|E|<=d_H`.

For every binary core move `p -> p+f(p)Delta`, `f:V->{0,1}`, with
`s=|Delta|<gamma`, extend it by moving an anchored isolate exactly with its anchor
and leaving unanchored isolates fixed. Every inactive upper-distance constraint
outside E stays **strictly below D**. Old contacts are unchanged by this extension.

If the core move preserves all old contacts, weakly shortens all old diameters,
and strictly shortens at least one, then one of the following must occur:

```math
1<|xy|\le1+s,\qquad |x'-y'|\le1,
\tag{1}
```

or

```math
xy\in E,\qquad |x'-y'|\ge D.
\tag{2}
```

The exceptional set and anchor map depend only on the original source, not on
which core move is being extended. This uniformity is needed for the counting
corollary below.

## 2. Long-pair geometry, with its full proof

Define T to contain exactly pairs of length strictly greater than L. Every endpoint
is extreme: if `p=sum lambda_j a_j`, using other source points, the variance identity
and unit separation give for every q

```math
|p-q|^2=\sum_j\lambda_j|a_j-q|^2-\sum_j\lambda_j|a_j-p|^2
\le D^2-1.
```

Two disjoint T edges that failed to cross would be opposite sides of a strictly
convex four-point quadrilateral. Every angle is incident to one such long side and
another source distance at least one. At an angle at least pi/2, its opposite
diagonal would have squared length greater than `L^2+1=D^2`. Thus T is a straight
geometric thrackle. Its edges at one endpoint do not overlap because all their
endpoints are extreme.

The canonical straight-thrackle classification underlying C-WOODALL now applies
to the abstract graph T: it is a caterpillar forest or a connected odd-unicyclic
graph with pendant leaves. The source-specific d_H conclusions of that canonical
entry apply to H; we use the general geometric graph theorem for T separately.

Every endpoint of T outside B is contact-isolated. Indeed, all actual contacts
have positive stress in the canonical relative-interior normalization. At a
nonisolated point not in B, vertex equilibrium expresses that point as a positive
weighted barycenter of its distinct contact neighbors. It cannot be extreme.
This proves the assertion directly, without extending core ZR/ZF to isolates.

The long-pair argument is independently rederived here. PR #600's cyclic dispatch
report at `eddd8826f23776ab44825fa25183effb23e7a7b6` and PR #598's capacity report
at `439d9ac95211ad7eace207f0e5106f45465d97ec` supplied the checked research lead;
they are provenance only, not premises of the promoted theorem.

## 3. Graph partition theorem for the forest branch

Suppose H is a forest with c nontrivial components; `c=q-h=d_H>=1`. Every component
of H is a connected subtree of T. We prove the following graph statement, which
requires only that T has total cycle rank at most one.

### Lemma 3.1

There is a set E of edges of `T\H` of size at most `c-1+epsilon`, where epsilon
is zero for a forest T and one for a unicyclic T, such that `T\E` is a forest and
each of its components contains at most one component of H.

**Proof.** If T has a cycle, that cycle has an edge outside H because H is acyclic.
Delete one such edge. This produces a forest and costs epsilon edges. Contract
each H component to one marked root vertex in this forest. Partition each remaining
tree that meets the marked roots into connected pieces containing one root each:
start a region at every root and assign the other vertices by a deterministic
multi-source traversal. An edge between regions is deleted. A tree with a roots
requires exactly a-1 such deletions; all these edges are outside H. Summing over
trees meeting H gives at most c-1 additional deletions. Expand the H subtrees.
The result has the asserted properties. QED.

Fix one such partition for the original source. In `T\E`, every connected
isolate-only branch attached to the old B vertices has a **unique** attachment
vertex b in B: two attachment vertices would create a cycle using the unique H
path between them, or join two distinct H components. Assign every isolate in
that branch the anchor b. Components having no H vertex are left fixed. Every
inactive T edge outside E then either has two endpoints with the same anchor or
two unanchored endpoints. There is no remaining new B-B edge.

The last statement follows because a new B-B edge inside one H component would
create a cycle, while one joining two H components was cut by the partition.

## 4. Cyclic branch, separately checked

If H contains an odd cycle, T contains it as well. Straight-thrackle classification
and the edge bound give the same unique odd cycle, with every remaining vertex a
pendant leaf attached directly to the cycle. No additional B-B edge is possible;
every new T vertex is an isolate with one old cycle-vertex neighbor. Anchor it
there. Thus E is empty. This is the finite cyclic dispatch of PR #600, rederived
at its stated scope; the forest partition extends it rather than assuming the
same unique-partner structure in a forest.

## 5. Exact full-source move and minimality fork

Apply the fixed anchor map to any binary core move. A protected inactive long pair
has identical endpoint displacements, so its length is unchanged and remains below
D. Every other inactive pair outside E originally has length at most L, and its
relative displacement has norm at most s. Its final length is at most `L+s<D`.
Each isolate has no old contact, so the extension cannot alter an old contact.
All original points, including unanchored isolates, remain in the source.

If neither (1) nor (2) occurs, every original noncontact remains strictly longer
than one, every inactive pair stays strictly below D, and all old diameter pairs
weakly shorten, with at least one strict decrease. The endpoint has the same
contact graph. It is either a strict sub-D source, or another diameter-D minimizer
with the same contacts and fewer diameter pairs. Both contradict the canonical
selection. Hence (1) or (2) occurs. A pair in (1) must change and the reverse
triangle inequality gives its original length at most `1+s`.

This is an endpoint argument. No feasibility is claimed along a straight
interpolation, and no multiplier is assigned to an inactive pair.

## 6. One fixed partition gives a simultaneous counting bound

Let r proposed binary core moves have pairwise disjoint moving core sets and
amplitudes at most `s_*<gamma`. Assume each has the contact/old-diameter behavior
in Section 1. Use **the same** E and anchor map for all moves.

A fixed source point can move in at most one proposal: for an isolate this follows
from its fixed old-core anchor. Therefore a fixed source pair can change in at most
two proposals. At most `2|E|` moves can be obstructed only by an exceptional upper
pair. Choose a near-unit witness at each other move. Each such witness is reused at
most twice. The number of distinct original near-unit pairs is consequently

```math
\boxed{N_1\ge\max\{0,\lceil r/2\rceil-|E|\}.}
\tag{3}
```

In the forest branch this is at least `max(0,ceil(r/2)-d_H)`, and improves by one
when T is a forest. In the cyclic branch it is at least `ceil(r/2)` with no upper
exception. If an unpromoted rooted regime supplies `d_H=o(D)` and a linear disjoint
small ONE-SIGN population, (3) gives a linear near-unit population in either
diameter topology. Neither antecedent is asserted for all C-II sources.

## 7. Sharp forest exception regression

Take

```math
a=(0,0),\quad b=(8,0),\quad c=(3608/901,6240/901).
```

Then `|ab|=|ac|=8`, while

```math
63<|bc|^2=57600/901<64.
```

The diameter graph H is a two-edge tree with `d_H=1`; T is a triangle. There are
no isolates. Move only b by `Delta=(-1/1000,-1/100)`. Its squared amplitude is
`101/10^6<1/256=1/(4D^2)`, so the move is below gamma. The old diameter ab
strictly shortens, ac stays fixed, and the inactive pair bc becomes longer than
D. Thus no isolate adjustment can eliminate this one upper obstruction.

This is a rational feasible source with no contacts, not a global minimizer. It
refutes unconditional zero-exception forest dispatch. The one-edge exception
budget is necessary when T has a cycle, even at ultrasmall amplitude. It does not
refute the canonical global-minimizer theorem with a near-unit/exceptional fork.

## 8. Fractional isolate repair and a total-slack path certificate

We next attack the lower-distance obstruction rather than stop at counting it.
Allow an isolate displacement `lambda Delta` with `0<=lambda<=1`. Keep every
anchored branch at its anchor's prescribed binary value, and give each unanchored
long-pair component one free lambda variable; an isolate outside T has its own
free variable. This preserves every protected long pair, while all other
inactive upper pairs outside E still satisfy `L+s<D`.

For any original noncontact source pair a,b with `r=b-a` and `p=r dot Delta>0`,
put

```math
g=|r|^2-1>0,\qquad c_{ab}={g\over2p}>0.
\tag{4}
```

Impose the directed difference constraint

```math
\lambda_a-\lambda_b\le c_{ab}.
\tag{5}
```

Repeated source points in one protected component use the same variable.
Pairs with zero projection need no constraint; reversing a negative projection
gives the positive orientation. Existing unit contacts have prescribed core
displacements and are already preserved by the core move.

### Lemma 8.1 — these linear constraints strictly protect all noncontacts

Let `t=lambda_a-lambda_b`. If t<=0, the squared distance
`|r-tDelta|^2=|r|^2-2pt+s^2t^2` is at least `|r|^2>1`. If
`0<t<=g/(2p)`, it is at least `1+s^2t^2>1`. Thus (5) is a sufficient
condition for strict lower feasibility, including equality in the linear bound.
It is not claimed to be necessary for every nonlinear endpoint.

### Lemma 8.2 — weighted forcing paths are the only obstruction to (5)

Draw an arc a->b of cost c_ab between the corresponding variables. Prescribe
the anchored/core values 0 or 1. The bounded difference constraints (5) admit
a solution iff **no** directed path from a prescribed-1 variable to a
prescribed-0 variable has total cost strictly less than one.

**Proof.** Sum (5) along any such path to obtain the necessary cost bound.
Conversely, let d(x) be shortest-path distance from the prescribed-1 variables,
with infinity for unreachable vertices. Set `lambda_x=max(0,1-d(x))`.
An arc of cost c has `d(b)<=d(a)+c`, which gives
`lambda_a-lambda_b<=c`, including the cases when a or b is unreachable or
clipped to zero. Prescribed-1 vertices have value one, and prescribed-0
vertices have distance at least one and value zero. QED.

If E is empty, canonical minimality therefore forces such a path. Otherwise the
constructed fractional endpoint either has an exceptional upper obstruction or
canonical minimality forces a weighted path. This is a concrete repair attempt:
when there is no path and no exceptional obstruction, it constructs the strict
competitor/minimality contradiction explicitly.

### Cyclic corollary: one monotone chain in one actual contact face

For cyclic H, E is empty and each T isolate is a leaf anchored at a core cycle
vertex. All other isolates have individual free variables. Take a shortest
prescribed-1 to prescribed-0 path of cost less than one and trim it so it has no
prescribed variable internally. Its source realization is a chain

```math
x_0,x_1,\ldots,x_k,
```

whose internal points are distinct contact isolates outside T. Each endpoint is
either a core point or an anchored long-pair leaf; their respective core anchors
have prescribed move labels 1 and 0. Every chain edge is a previously strict
source pair and is oriented strictly forward in the Delta direction. Its exact
certificate is

```math
\boxed{\sum_{j=0}^{k-1}
{\,|x_{j+1}-x_j|^2-1\over
 2(x_{j+1}-x_j)\cdot\Delta}<1.}
\tag{6}
```

Put `ell_*=s+sqrt(1+s^2)`. Every summand is positive and less than one,
so every edge length is strictly between 1 and ell_*. Moreover

```math
\boxed{\sum_j(|x_{j+1}-x_j|-1)<s\,ell_*.}
\tag{7}
```

Indeed, with `p_j=(x_(j+1)-x_j) dot Delta`, (6) gives
`sum_j g_j < 2 max_j p_j <=2s max_j |x_(j+1)-x_j|<2s ell_*`.
Divide each g_j by its edge length plus one, which exceeds two.

For D>=2 and s<gamma, `ell_*<sqrt(2)`. All these short edges and all old contacts
are simultaneously planar: crossing short segments would be quadrilateral
diagonals opposite an angle at least pi/2 with unit-separated incident sides,
forcing a diagonal at least sqrt(2). No such short edge can pass through another
source point. Each internal isolate lies in one face of the old contact graph,
and adjacent chain edges use that same face. Therefore the whole chain lies in
one old contact face, which may be bounded or exterior. Its Delta projection
increases strictly; it is a simple monotone chain.

The total excess is O(s), independent of chain length. Thus a conditional
O(D^-2) cyclic ONE-SIGN swap forces a cofacial monotone isolate chain of total
unit-length excess O(D^-2), rather than only an arbitrarily chosen single blocker.
No chain edge is declared active or assigned positive stress. No exact triangle
or contradiction follows from (6)--(7) alone.

### Exact failure of the next shortcut

For any k>=2 and rational s>0, put
`x_j=j(1+s/(4k))` on one line, and prescribe displacements s at x_0 and zero
at x_k. The other points may receive any fractional displacement in [0,s].
The k adjacent edges have total original excess s/4 and satisfy (6). The final
span is `k-3s/4<k`, so not all k successive collinear gaps can exceed one.
There is no exact unit contact or triangle in the original chain.

This rejects `small total slack path => exact triangle` without additional
canonical contact/core/face hypotheses. It is a finite lower-constraint
regression, not a global-minimizer source. A useful repaired closing lemma must
exclude the specific cofacial anchored chain or allow nonparallel isolate
motions that resolve it while preserving every upper constraint.

### 8.3 Bounded inactive-face isolates can be transported without obstruction

Now use the actual global O-O cut geometry. Assume the connected old positive
contact graph has its usual face walks and the selected boundary trains are
global O-O: their train contact edges face only strict rhombi and the exterior
face. Then every bounded nonquadrilateral face has one constant binary core
label f on **all** of its boundary vertices. No boundary edge belongs to a
selected train cutset, so each consecutive boundary edge has equal endpoint
labels. Following the connected face walk proves the claim, including repeated
vertices and bridges; occurrences are not silently identified in a count.

Move every contact isolate inside such a face with that common label. This
simultaneously removes every lower or upper obstruction involving its interior
isolate population, for s<gamma and s<sqrt(2)-1:

- An interior point of a bounded old contact face is nonextreme. The variance
  argument in Section 2 gives **every** pair involving it length at most L.
  Any binary/fractional displacement changes a distance by at most s, so its
  upper constraints remain strictly below D.
- Any new lower obstruction had original length at most 1+s<sqrt(2). Its
  segment is cofacial with the old contact graph by short-pair planarity. A
  segment from an interior isolate cannot exit this face through an old edge,
  or pass through a third source vertex. Thus its other endpoint is another
  isolate in the same face or a boundary core vertex. Both receive the same
  displacement, so the distance is unchanged and strictly greater than one.

There is no missing quadrilateral isolate case. Put a unit rhombus's vertices
at `(+-a,0),(0,+-b)` in perpendicular diagonal coordinates, where `a^2+b^2=1`.
For any point in it choose its quadrant and write `0<=x<=a`, `0<=y<=b`.
The squared distances to `(a,0)` and `(0,b)` sum to

```math
2(x^2+y^2)-2ax-2by+a^2+b^2\le1.
```

One distance is at most `1/sqrt(2)<1`. Therefore a unit-separated source has
no additional point in the interior of an actual unit-rhombus face.

This transport is compatible with the fixed long-pair anchor construction:
bounded-face isolates have no T edge at all, so their previously free singleton
variables may be prescribed to the common face label without changing any upper
protection. Other source points and old diameters keep their original moves.

For the fractional construction, evaluate any pair whose two variables are
already prescribed **at its actual endpoint**. If it stays longer than one,
omit its conservative linear cap; if it does not, it is an actual near-unit
blocking pair. Apply Lemma 8.2 to the remaining caps, which have at least one
free endpoint. This avoids treating a conservative sufficient bound as a
necessary core-core condition.

Consequently in the cyclic, sufficiently small, global O-O ONE-SIGN branch,
only these lower obstructions survive:

1. an actual blocked diagonal of a bounded unit-rhombus face whose core vertices
   have different move labels; or
2. an exterior-face actual blocked pair, or an exterior monotone chain with a
   free isolate internally and certificate (6)--(7).

A weighted path in a bounded nonquadrilateral face cannot join prescribed labels
1 and 0, since all boundary and interior labels there are equal. A weighted path
cannot have a free interior point in a quadrilateral face, since there is no
such source point. Thus a free-isolate forcing chain is exterior. Anchored long
leaves are extreme vertices outside conv(B), and also belong to the exterior
face. The actual bounded rhombus diagonal case is kept explicit; diagonal
immunity for the selected complete rectangle does not eliminate other rhombi.

In the forest branch the same bounded-face transport applies, with E unchanged.
Exterior weighted paths may jump within an unanchored long-pair component, so
a continuous monotone source chain is not asserted there. The at-most-d_H upper
exceptions and bounded-rhombus alternatives remain.

This is an actual full-source transport theorem conditional on the stated O-O
cutset/face hypotheses. It does not delete an inactive-interface branch or the
macroscopic-container branch from C-II: those branches need not supply this
small ONE-SIGN global O-O move. It eliminates bounded **isolate-population**
blockers for a move when those hypotheses hold.

## 9. Verification, dependencies, and next attack

Run

```
python3 research/verify_target_c_forest_isolate_dispatch_2026_10_01.py
```

The integer graph verifier enumerates all labeled T graphs on 2..5 vertices with
total cycle rank at most one and every nonempty forest H subgraph, and checks
every binary assignment to the old endpoint vertices. It verifies the exception
bound and protection of every nonexceptional inactive long edge. It also checks
all distances and the finite upper obstruction in Section 7 with Fraction.
Geometric realization, contacts, vertex KKT, and global optimality are omitted
from this graph computation. The universal proof above is not replaced by it.

Canonical dependencies are local KKT equilibrium, the restored full-support
normalization, and C-WOODALL's general straight-line graph classification.
The ONE-SIGN block-transposition application is conditional on the explicitly
unpromoted October 1 cut/extraction/swap stack. Core rigidity is not extended to
isolates. No lifecycle promotion is made by this packet.

The verifier checks 10,524 graph packets and 143,852 binary label assignments,
then compares the weighted-path construction with an independent quarter-grid
feasibility oracle on 59,808 finite difference-constraint packets. It checks
the collinear slack-path regressions for k=2,10,100. The face transport and
universal geometric implications are proved above, not certified by abstract
graph enumeration.

The next exact attack is the exterior chain in (6), or a surviving bounded
rhombus diagonal: eliminate it using actual core anchors and swept-phase train
geometry, or repair it by a nonparallel isolate motion compatible with the
long-pair graph. Planarity and small total slack alone are insufficient, as
the collinear regression shows.
Few-phase/TWO-SIGN swaps, exact-phase opposed bundles, split-star, inactive
interfaces, macroscopic inactive containers/exterior caps, and other full-core
branches remain explicit and open.
