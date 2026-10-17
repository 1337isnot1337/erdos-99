> Generated reading edition · [exact source](../../../docs/reports/target_c_aligned_swap_horn_and_axial_bracket_2026-10-01.md) · source SHA-256 `410f0816e3d36fa6a7f0cc646a6587002e45124c2b630e4a4e538f4b1c95dad5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5192AD2B069A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: aligned varying-amplitude swaps and axial brackets

`coherently oriented ONE-SIGN swaps -> exact Horn obstructions after full-source
upper dispatch -> a finite strict competitor or canonical pair-count contradiction
if a positive closure avoids forced-zero sites and incompatible endpoint pairs`

**Date:** 2026-10-01; continued 2026-10-02. **Starting main:**
`14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.
**Continuation HEAD:** `96bf6bc382effb50d4220c618cffe106dcd6084e`.
**State version:** `2026-09-14.audit.51`.
**Branch:** `swarm/root/c2-gap-cut-20261001`.
**Mission:** simultaneous source-preserving finite swaps with differing amplitudes.
**Classification:** proved candidates awaiting promotion for the abstract source
theorems; conditional for their TB1 specialization; regression for Section 7.
The artifact lifecycle remains unreviewed. **Level I and C-II remain OPEN.**

## 1. Dependencies and exact scope

Canonical inputs are the contact-minimal, then diameter-pair-minimal triangle-free
global representative, retention of every source point, and
[Theorem 6.1](../theory/01-local-structure.md): a nonisolated point outside the
actual diameter endpoint set is strictly surrounded by its unit contacts.
The exact global quantifiers are those in [the problem statement](../problem/statement.md).

The standalone binary distance compilation was proved in
[the preceding packet](target_c_simultaneous_disjoint_swaps_exact_2sat_2026-10-01.md).
Its finite source hypotheses are retained here. The proofs below do not infer
source optimality or KKT from a supplied point set.

The conditional train application uses the unpromoted
[arbitrary block-transposition theorem](target_c_open_cell_block_transposition_2026-10-01.md)
at main commit `5ff8cadd`. The cutset, midpoint-axis, non-grazing, and finite
ONE-SIGN claims were inspected in its Sections 1--3. A usable family must have
disjoint private slab boundaries and one common orientation of its swap axes.
Neither a large ONE-SIGN population nor a common phase pair is assumed to follow
from the canonical route.

The multi-root upper dispatch extends the inspected Section 5.1 of
[PR #600 at commit 5b876870](https://github.com/1337isnot1337/e-99/blob/5b876870268116d0f1d8c5fbf820b856f09171a4/docs/reports/target_c_ultrasmall_swap_isolate_dispatch_2026-10-01.md).
That result is unpromoted. Section 3 supplies the proof actually needed, including
the factor two required for simultaneous unequal translations. No other claim
on that branch is an input. The common-vector predecessor in
[PR #598 at commit 0296b3e8](https://github.com/1337isnot1337/e-99/blob/0296b3e86d079bb73421b2af7d155a091a126d05/docs/reports/target_c_common_swap_blocker_arborescence_2026-10-01.md)
was inspected; it does not prove the varying-amplitude statement.

All new arguments below are finite and retain isolates. They neither discard
boundary terms nor use an Euler-path interpretation of an interval graph.

## 2. Coherent ONE-SIGN swaps have no shared moving diameter

Let A have diameter D. Let L_1,...,L_k be disjoint source subsets with nonzero
translations Delta_i. Assume all old contacts are preserved for every binary
assignment. Assume each individual swap strictly shortens every old diameter
whose relative vector it changes, and changes at least one old diameter.

Impose the following sign-coherence hypothesis:

> For every oriented actual diameter vector r, the numbers r dot Delta_i have
> one common, nonzero sign as i varies.

**Theorem 1.** No old diameter joins two different L_i. Every nonempty union of
the swaps weakly shortens every old diameter and strictly shortens at least one.

**Proof.** Suppose p in L_i and q in L_j, i != j, form an old diameter, and put
r=q-p. The individual i move gives r-Delta_i and strict shortening implies

```math
 r\cdot\Delta_i>\frac{|\Delta_i|^2}{2}>0.
```

The individual j move gives r+Delta_j and strict shortening implies

```math
 r\cdot\Delta_j<-\frac{|\Delta_j|^2}{2}<0.
```

This contradicts coherence. Thus an old diameter has both endpoints in one
moving subset, both fixed, or exactly one moving endpoint. In the first two
cases its vector stays unchanged. In the last case its vector under a union
is exactly its vector under the corresponding individual move and strictly
shortens. Each selected swap has such an edge, proving the claim. QED.

For the TB1 specialization, write Delta_i=-s_i Jm_i after selecting one coherent
orientation, where s_i>0 and m_i is the consistently lifted midpoint phase.
All m_i lie in one connected open witness cell containing no projective direction
of an actual diameter. For a fixed actual diameter r, r dot Jm can change sign
only where [m]=[r]. It therefore has one nonzero sign on that cell. This proves
the coherence hypothesis even when the amplitudes and midpoint phases differ.

The individual ONE-SIGN/non-grazing conclusion supplies strict shortening.
Its positive-contact KKT boundary sum supplies a changed diameter. These are
conditional application inputs, not conclusions of Theorem 1.

This replaces the common-vector restriction for the old-active-diameter part of
the simultaneous argument. It does not establish feasibility of inactive pairs.

## 3. Full-source upper dispatch for unequal simultaneous translations

Let B be all old diameter endpoints, H all old diameter pairs, q=|B|, h=|H|,
and d_H=q-h. Put

```math
 L_D=\sqrt{D^2-1},\qquad \gamma_D=D-L_D.
```

Assume D>1. Original moving subsets can include contact isolates. All individual
move amplitudes are at most s, with

```math
 \boxed{2s<\gamma_D.}                                      \tag{1}
```

Define T to contain every source pair strictly longer than L_D.

Here are the geometric facts used. If p is not extreme, represent it as a convex
combination of other source points a_j. The variance identity and unit separation
give |p-z|^2 <= D^2-sum_j lambda_j|a_j-p|^2 <= D^2-1 for every z. Thus all T
endpoints are extreme. Two disjoint T edges that fail to cross are opposite sides
of a strictly convex quadrilateral. At an angle of at least pi/2 the adjacent
lengths include one length >L_D and another length >=1. The opposite diagonal
would exceed D, a contradiction. Hence T is a convex straight-line thrackle.

For completeness, its edge bound is elementary in convex position. At every
incident hull vertex choose its first incident ray in clockwise order in the
strict wedge of rays toward the other hull vertices. If an edge uv is chosen at
neither end, the preceding chosen rays at u and v go into opposite open
half-planes of the line uv. Those two edges are disjoint, violating the thrackle
property. Every edge is therefore chosen at an endpoint, so |E(T)|<=|V(T)|.
The same bound applies to any induced union of its components.

Every T endpoint outside B is a contact isolate: otherwise canonical local
trapping strictly surrounds it, contrary to extremality. Let G be the union
of T components meeting B and Z=V(G) minus B. Start a simultaneous graph search
from all B vertices, adding one parent edge per newly reached z in Z. This
constructs a forest F with exactly |Z| edges and one designated B root r(z) for
each z. No H edge is in F. Define once at the original source

```math
 J=(E(G)\setminus H)\setminus E(F).
```

The edge bound gives

```math
 \boxed{|J|=|E(G)|-h-|Z|\le q-h=d_H.}                      \tag{2}
```

Retain the original assignment of every B vertex and every nonisolated point.
Overwrite the assignment of each z with the binary displacement of r(z),
including its exact variable and its particular Delta_i. Fix every T component
not meeting B and every remaining isolate outside B. This reassigns disjoint
moving sets without altering an old contact or an old diameter's endpoint
assignment. Every F edge has identical displacements at its endpoints, for
every binary assignment. Every inactive T edge outside J is consequently
unchanged. Every remaining inactive source pair has old length at most L_D and
relative displacement at most 2s. Its new length is strictly below D by (1).

**Theorem 2.** After this one motion-independent full-source dispatch, at most
d_H actual inactive source pairs can supply upper constraints for any binary
combination of the unequal moves. Freezing to zero every variable assigned to
an endpoint of J, at most 2d_H variables, makes all inactive upper constraints
strict for every assignment of the remaining variables.

**Proof.** The preceding construction proves that only J can fail the upper
bound. Each pair in J has at most two endpoint variables. Freezing them makes
both endpoint displacements zero and keeps the original strict distance.
All other pairs remain covered by the same argument. QED.

The cyclic case d_H=0 loses no variables and has no upper constraints at all.
For either topology the convenient sufficient bound is s<=1/(4D), because
2s<=1/(2D)<1/(D+sqrt(D^2-1))=gamma_D. Using s<gamma_D without the factor two
would not prove the simultaneous statement.

This theorem does not claim d_H=o(D) universally. Losing at most 2d_H variables
can exhaust a short family. If the original family satisfies Theorem 1, its
remaining nonempty subfamilies still shorten an old diameter after freezing.

## 4. The exact remaining finite system is Horn

For disjoint translations and strict-inactive admissibility, each source pair
depends on at most two variables. The original all-zero assignment is feasible.
Consequently a bad two-variable pattern can only be 10, 01, or 11. Its clause is,
respectively,

```math
 x_i\Rightarrow x_j,\qquad
 x_j\Rightarrow x_i,\qquad
 \neg(x_i\wedge x_j).                                     \tag{3}
```

A bad one-variable pattern forces that variable to zero. These are exactly
zero-satisfiable Horn clauses of length at most two. This observation applies to
the full original compiler, even before upper dispatch. A 2-SAT solver is valid
but more general than necessary.

Let R be the forced-zero variables, let E be the implications, and let K be the
unordered incompatible pairs from the last clause in (3). For each i let C(i)
be all variables reachable from i along E, including i itself.

**Theorem 3.** A feasible assignment with x_i=1 exists if and only if

```math
 C(i)\cap R=\varnothing
 \quad\hbox{and}\quad
 \text{no pair of K has both endpoints in C(i).}             \tag{4}
```

When (4) holds, the indicator of C(i) is the least such assignment. When it
fails, a path i -> r in R, or two paths from i to the ends of a pair in K, is
an exact obstruction certificate.

**Proof.** Any assignment with x_i=1 must set all C(i) to one. A forced-zero
vertex or an incompatible pair inside C(i) makes this impossible. Conversely,
the indicator of C(i) satisfies every implication because C(i) is closed under
outgoing implications. Under (4) it satisfies every unit and incompatible-pair
clause too. Its inclusion in every other positive assignment proves leastness.
QED.

Under Theorems 1--2 and canonical minimality, the lower-distance Horn formula
has exactly one model, zero. Otherwise its nonzero model is a finite source
competitor preserving every old contact and every old noncontact strictly,
introducing no new diameter pair, and shortening an old diameter. If every old
diameter shortens, global optimality fails. Otherwise the same-contact triangle-
free global representative has fewer diameter pairs, contradicting its selection.

Therefore **every variable has a root-return or a branching incompatibility
certificate**. With identical translations both endpoints moved together keep
their old relative vector, so a bad 11 pattern never occurs. This reduces to
the earlier return-to-fixed implication theorem. With unequal translations the
branching alternative cannot be discarded; Section 7 provides an exact source
pair regression at arbitrarily small amplitudes.

After dispatch, any blocking lower pair has old length <=1+2s by the reverse
triangle inequality. If 1+2s<sqrt(2), these pairs are Gabriel edges and lie in
the closure of a face of the old contact drawing: any third point in the open
diametral disk would have squared distances to both endpoints summing to less
than (1+2s)^2<2, violating unit separation. Proper crossing of two such edges
likewise creates an angle at least pi/2 with an opposite diagonal shorter than
sqrt(2) but two adjacent source distances at least one. These source facts do
not turn the edges into actual contacts or create a global Schur kernel.

## 5. Axial brackets exclude genuine incompatible-pair clauses

The next statement uses no optimality, KKT, train embedding, or diameter.
Let u,w be perpendicular unit vectors. Let

```math
 \Delta_i=s_i w_i,\quad \Delta_j=s_j w_j,
 \qquad 0<s_i,s_j\le\frac1{10},
 \qquad |w_i-w|,|w_j-w|\le\frac1{10},
```

where w_i,w_j are unit vectors. Let p,q be an old noncontact in a unit-separated
source, with r=q-p. Their four lower-distance states have vectors

```math
 r,\quad r-\Delta_i,\quad r+\Delta_j,
 \quad r+\Delta_j-\Delta_i.                                \tag{5}
```

Call p **axially bracketed** if it has unit neighbors p+a_+ and p+a_- such that
|a_+-u|<=1/10 and |a_-+u|<=1/10. The same definition applies at q.

**Theorem 4.** If at least one endpoint is axially bracketed, the lower-distance
bad-pattern set cannot be exactly {11}, and cannot contain both 10 and 01.
After simplifying clauses from that pair it gives only an implication, a
forced-zero variable, or no constraint. Thus every genuine incompatible-pair
clause in the aligned lower Horn system has two unbracketed source endpoints.

**Proof of the joint-only case.** Suppose the 11 length is at most one while
both single-move lengths are strictly greater than one. Subtracting squared
distances gives

```math
 |r+\Delta_j-\Delta_i|^2-|r-\Delta_i|^2
 =2s_j r\cdot w_j+s_j^2-2s_i s_j w_i\cdot w_j<0,
```

```math
 |r+\Delta_j-\Delta_i|^2-|r+\Delta_j|^2
 =-2s_i r\cdot w_i+s_i^2-2s_i s_j w_i\cdot w_j<0.
```

Hence r dot w_j < s_i <=1/10 and r dot w_i > -s_j >=-1/10.
Also R=|r|<=1+|Delta_j-Delta_i|<=6/5. Consequently

```math
 |r\cdot w|<\frac1{10}+\frac{R}{10}\le\frac{11}{50}.
\tag{6}
```

Since R>1, orthogonality gives |r dot u|^2>1-(11/50)^2>(19/20)^2.
Choose the unit neighbor vector a at a bracketed endpoint directed toward the
appropriate sign of r dot u. If that endpoint is p, then

```math
 r\cdot a>\frac{19}{20}-\frac{R}{10}\ge\frac{83}{100},
```

```math
 |q-(p+a)|^2=R^2+1-2r\cdot a
 <\frac{36}{25}+1-\frac{166}{100}=\frac{39}{50}<1.
```

The neighbor differs from q because pq is an old noncontact. This contradicts
source unit separation. If q is bracketed, use -r and its neighbor toward p;
the same bounds apply.

**Proof when both singles are bad.** If |r-Delta_i|<=1 and |r+Delta_j|<=1,
then R<=1+s_i<=11/10, r dot w_i>0, and r dot w_j<0 because R>1. Therefore
|r dot w|<=R/10<11/50. The same neighbor argument gives the contradiction.

There are only seven nonempty subsets of {10,01,11}. The excluded cases are
{11} and every set containing both singles. The remaining sets are {10},
{01}, {10,11}, and {01,11}. The first two are implications. Forbidding both
10 and 11 forces x_i=0; forbidding both 01 and 11 forces x_j=0. QED.

**Corollary 4.1: physical orientation of a bracketed implication.** Suppose a
bad 10 state has a bracketed endpoint. Then r dot w>1/2.
Indeed r dot w_i>0 and R<=11/10. If r dot w<=1/2, its lower bound is -R/10,
so |r dot w|<=1/2. Then |r dot u|>sqrt(3)/2>17/20 and the appropriate unit
neighbor has projection onto r greater than 17/20-11/100=74/100. Its distance
to the other endpoint is squared less than 121/100+1-148/100=73/100<1,
a contradiction. A bad 01 gives the reversed orientation.

Thus each bracketed implication runs upward by more than one half in the
physical w coordinate. This does **not** make the layer quotient acyclic:
different implication edges may use different sites of one slab, and a slab
can span Theta(D) in that coordinate. Identifying these sites would discard
the source geometry. The repaired physical order statement is the corollary,
not a global layer-height potential. The final regression in Section 7 realizes
this failure in an actual contact-preserving, ONE-SIGN finite source family.

## 6. Precise new obstruction after the repair

For a coherent ONE-SIGN family satisfying s<=1/(4D), after losing at most
2d_H variables by the fixed forest exceptions, canonicality demands that each
remaining variable reach either:

1. a lower-distance forced-zero constraint; or
2. both ends of a lower-distance incompatible pair with two axially unbracketed
   source endpoints.

The second alternative is absent if every potentially blocking pair has at
least one bracketed endpoint. The system then has only directed implications
and forced-zero sites, despite differing phase gaps and midpoint phases.

This isolates a geometric defect class; it does not bound it. Loaded hull
sites, grid boundary sites, and dispatched isolates can be unbracketed. The
canonical route does not supply a theorem making their obstruction system
empty. The pointwise upward order also supplies no layer potential without
a bound on the internal w span or a compatible transport theorem.

The next closing obligation is to release a forced-zero site or an unbracketed
incompatible pair while preserving the other full-source constraints, or show
that every positive implication closure cannot encounter those obstructions.
Near equality and a planar drawing alone do not establish that obligation.

The TWO-SIGN population, exact-phase finite motions beyond the witness rays,
split-star O--O, inactive interfaces, macroscopic inactive containers/exterior
caps, and full-core branches outside the fixed-star extraction remain open.
No statement here eliminates them or weakens the Level I quantifiers.

### 6.1 Two individual obstructions require disjoint phase intervals

For actual unit-direction swaps there is a sharper conclusion than small-axis
alignment. Choose the common orientation so

```math
 \Delta_i=s_i Jm_i,\qquad s_i=2\sin(\varepsilon_i/2),
```

where the consistently lifted midpoint phase is mu_i and the boundary phase
interval is I_i=[mu_i-epsilon_i/2,mu_i+epsilon_i/2]. Assume all boundary phases
lie in one real interval J of width less than 1/10, and 0<s_i<=1/10.

**Theorem 5.** If one old noncontact pair blocks the individual i move and also
the individual j move, its projective direction lies strictly between the two
boundary phase intervals. In particular I_i and I_j are disjoint.

**Proof.** Orient r from its endpoint in L_i to its endpoint in L_j. Blocking
both singles gives

```math
 r\cdot Jm_i\ge\frac{R^2-1+s_i^2}{2s_i}>0,
 \qquad
 r\cdot Jm_j\le-\frac{R^2-1+s_j^2}{2s_j}<0,
 \quad R=|r|>1.
```

As the midpoint phase moves between mu_i and mu_j, the transverse scalar must
vanish at [r], so [r] lies in that subinterval of J. Reverse r and exchange
i,j if necessary, giving an ordinary lifted phase theta with mu_i<theta<mu_j.
Then

```math
 \sin(\theta-\mu_i)
 \ge\frac{R^2-1+s_i^2}{2Rs_i}>
 \frac{s_i}{2}=\sin(\varepsilon_i/2).                 \tag{7}
```

The strict inequality is exactly
(R-1)(R+1-s_i^2)>0. All angles are in (0,1/10), where sine is increasing,
so theta>mu_i+epsilon_i/2. The other individual obstruction analogously gives
theta<mu_j-epsilon_j/2. Thus theta lies in the strict gap between the intervals.
For the opposite common swap orientation the order reverses; disjointness is
unchanged. QED.

**Corollary 5.1.** Let k' nonempty coherent ONE-SIGN variables survive the upper
dispatch/freezing in Theorem 2. If their boundary phase intervals have a common
point, their individual obstructions require at least k' distinct near-unit
source pairs. The convenient explicit estimate is

```math
 \boxed{N_1\ge k'\ge\max\{0,k-2d_H\}.}                \tag{8}
```

Indeed every singleton move must violate a lower constraint by canonicality,
and a source pair can change under at most two singleton moves. Theorem 5
prevents that pair from blocking two of this common-point family. This extends
the common-vector witness count to distinct midpoint phases and amplitudes.
Joint-only incompatible pairs can still occur, as Section 7 proves; the corollary
does not turn the entire formula into directed implications.

More generally let N_1 be the number of distinct source pairs blocking at least
one surviving singleton, and U the subset blocking two. Counting singleton/pair
incidences gives

```math
 \boxed{N_1+|U|\ge k'.}                               \tag{9}
```

Every pair in U has two unbracketed endpoints by Theorem 4, direction in J by
Theorem 5, and old length at most 1+s. The graph of U on actual source points
is a **linear forest**, provided every lifted direction in J is within Euclidean
distance 1/10 of one unit vector u. At a vertex there is at most one neighbor
in the forward u direction: two would be at distance at most
s+(1+s)(2/10)<=8/25<1. The same holds backward. A graph cycle has a vertex of
maximum u coordinate, with two backward neighbors, which is impossible.
Thus its components are paths. This is a source-point statement, not a layer
quotient statement, and says nothing about the actual contact graph being a path.

The paired-singleton case also has an extra slack factor. If W is the width of
J, equation (7) before normalization and theta-mu_i<W give

```math
 R^2-1\le2s_iR\sin W-s_i^2,
 \qquad 0<R-1<2s\sin W.                              \tag{10}
```

For W=O(D^{-1}) and s=O(D^{-2}) these two-hit pairs are O(D^{-3})-near-unit.
They are still inactive; this stronger proximity does not provide an exact
multiplier or a finite release.

The next attempted closure would snap or jointly displace these inactive axial
paths. The obstacle is exact: their vertices can have other unit contacts, and
changing a path to unit spacing need not preserve those contacts or the diameter
bounds. The linear forest does not supply that motion. A large common-point
family also needs a phase-distribution theorem; it is not supplied merely by
the number of distinct retained phases in the whole window.

## 7. Exact regressions and verification

Let 0<t<=1/100 and set

```math
 s_1=\frac{4t}{1+t^2},\qquad
 s_2=\frac{8t}{1+4t^2},\qquad a=s_2-s_1,
```

```math
 \Delta_1=(0,s_1),\quad\Delta_2=(0,s_2),
 \qquad r=(1-a^2/4,-a).
```

Here 0<a<s_1. Each Delta_i is the difference of exact unit vectors symmetric
about one common horizontal midpoint phase. Thus the translations are parallel,
coherently oriented, and arbitrarily small. The old pair and the two single
states have squared distances, respectively,

```math
 (1-a^2/4)^2+a^2>1,
 \quad(1-a^2/4)^2+s_2^2>1,
 \quad(1-a^2/4)^2+s_1^2>1.
```

The joint state has squared distance (1-a^2/4)^2<1. Embed the pair as p=0,q=r
along with fixed source points (-10,0),(10,0). All four points are unit-separated;
the old diameter is 20 and all four pair states stay below 20. The exact lower
formula is the one clause not(x_1 and x_2), with both one-bit models feasible.
Neither moving endpoint is axially bracketed. There are no old contacts, no
moving diameter, and no KKT/train/global-optimality claim. This falsifies the
universal assertion that coherent unequal swap vectors permit only implication
arcs. It does not falsify Theorem 1 or the canonical conclusion in Section 4.

A failed intermediate estimate was also preserved. Even for parallel vectors,
joint-only blocking does not imply |r|^2-1<=2 Delta_1 dot Delta_2. Use

```math
 r=(1-1/20000000,-124/1250),\quad
 \Delta_1=(0,1/1000),\quad\Delta_2=(0,1/10).
```

The same bad-pattern set is exactly {11}, but the old slack exceeds the proposed
bound. The proof of Theorem 4 uses differences of the joint and single squared
distances and does not use this false estimate.

Theorem 5's disjoint-interval exception is real. Let
c=(1-t^2)/(1+t^2), h=2t/(1+t^2), and let ce,he be the same unit-circle
parameters at t^2, for 0<t<=1/100. The midpoint vectors (c,-h),(c,h) have
strictly separated boundary intervals after rotation by the unit half-angle
(ce,he), because h ce>c he. Put s=2he and

```math
 \Delta_1=(sh,sc),\quad\Delta_2=(-sh,sc),
 \qquad r=(1+sh/4,0).
```

The two translations are exact unit-direction differences with the common
orientation. The old pair is strict; both single states and the joint state
have length less than one. Its old distance slack is sh/4=Theta(t^3), whereas
s=Theta(t^2) and the phase-window width is Theta(t). The same four-point
source embedding with fixed (-10,0),(10,0) is unit-separated and has unchanged
old diameter. It has no contacts, no source KKT, and no moving diameter. It
proves that separated intervals can share a singleton witness and that the
extra proximity in (10) cannot be turned into exact activity. The exact verifier
checks this at t=1/100,1/1000,1/10000.

The same verifier also strengthens each two-hit example to an eight-point
source. Retain p=0,q=r, add the two actual diameter pairs joining
(-6,-8) to (6,8) and (6,-8) to (-6,8), and add fixed unit-contact points
(0,3),(1,3). Assign p and (-6,-8) to the first move, and q and (6,-8) to
the second. Every old contact is preserved; each individual move strictly
shortens its private diameter; all inactive upper constraints stay strict for
every binary assignment. The one near-unit pair pq blocks 10,01,11, so the
exact Horn formula has only zero as a model. There is a common open actual-
diameter direction cell containing the four boundary phases, but no actual
TB1 contact train or positive full-source KKT. The remote loaded points are
contact isolates and the fixed unit-contact endpoints violate canonical local
trapping. The eight-point unit-spaced line has diameter seven, explicitly less
than this source's diameter twenty. Thus coherent signs, contact preservation,
strict upper feasibility, and private shortened diameters alone do not exclude
the obstruction; actual source normal form and private train-contact forces
must enter a closing proof.

The attempted next lemma, "bracketed upward implications make the layer quotient
acyclic," is also false. Take horizontal unit-contact rows at heights
0, 101/100, 3, and 401/100, each containing x=-1,0,1. Add four source points
(-6,-8),(6,-8),(6,8),(-6,8). The only two old diameter pairs join opposite remote
points, and both have length 20. Let L_1 consist of the lowest and highest rows
and (-6,-8); let L_2 consist of the two middle rows and (6,-8). Translate either
set by (0,1/20). Every original contact is preserved for all four choices, and
each individual swap strictly shortens its private old diameter. The lower gap
between the first two rows forbids 10; the upper gap between the last two rows
forbids 01. The two central-row witness pairs are axially bracketed and point
upward by 101/100. Thus the layer graph contains 1 -> 2 -> 1.

The union 11 preserves all contact and strict inactive constraints and has new
diameter squared 159361/400<400. The source is explicitly nonoptimal, its loaded
points are contact isolates, and its layer sets are not physical TB1 slabs.
It is a regression against deriving a quotient potential from pointwise order
and finite swap feasibility alone. It leaves the actual train/KKT co-embedding
as the necessary new hypothesis rather than falsely rejecting that hypothesis.

The extended [binary compiler](../../../research/verify_binary_contact_swap_2sat.py)
now exports least positive Horn models and path/branching obstructions. Every
one of the 4096 zero-satisfiable three-variable Horn systems is checked against
an independent full truth table, in addition to the previous 176 two-variable
2-CNF checks and actual source fixtures.

[The new exact verifier](../../../docs/research/migration/2026-10-16/shards/01/support/research/verify_aligned_swap_horn_obstructions.py)
checks the four rational joint-only and three two-hit unit-chord regressions,
the failed slack estimate,
the rational contradiction constants, 2934 independent bracketed pair/move
fixtures, and an actual source with two coherent unequal finite moves shortening
private old diameters. It also verifies all source constraints of the bracketed
layer-cycle regression and its strict finite competitor. These samples are
regressions and implementation checks;
the real-coordinate theorem is proved above. They do not encode global
optimality, source KKT, train extraction, or every C-II branch.

Canonical state and prompts are unchanged. Promotion requires an independent
audit and the repository's state contract.
