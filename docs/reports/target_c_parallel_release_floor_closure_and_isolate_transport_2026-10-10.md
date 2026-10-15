<!-- theorem-state: {"artifact_id":"ART-982CE41762F7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — finite parallel release, floor closure, and isolate transport

**Date:** 2026-10-10. **Worker:** Slot 01.\
**Starting main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.\
**Starting owned checkpoint:** `4d6b30a107df49fa954daa092fe7fc72eaa7cc4a`.\
**Theorem state:** `2026-10-10.audit.234`.\
**Branch:** `research/sol61-slot01-outer-motion-20261010`.\
**Classification:** proved candidates awaiting independent audit; conditional
source endpoints; exact nonglobal regression. This report is unreviewed and
noncanonical. **C-II and Level I remain OPEN.** External theorem imports: none.

## 1. What is new and the exact closure chain

The preceding Slot 01 report gives a common-translation implication criterion.
This report replaces common height by independently chosen nonnegative heights
on a supplied family of core groups, and allows retained contact isolates their
own variables. There is no requirement that each core singleton already pass
the actual diameter constraints or that isolates follow a fixed anchor.
Every full-source upper constraint is included directly.

The new exact theorem solves the resulting endpoint problem by shortest-path
upper bounds and a finite elimination of groups whose contact-opening floor
cannot be cleared. It is complete for the precisely specified endpoint class:
every active contact cut opens, and every old noncontact with transverse
distance at most one retains its old projected order.

```text
supplied actual source groups with no contacts between positive groups
 -> actual contact-opening floors and full-source pair costs
 -> a core group survives shortest-path floor closure
 -> explicit heights satisfying every old and newly active pair
 -> same-cardinality triangle-free contact-loss competitor at diameter <=D.
```

The final source-extraction/nonempty-core-support assertion is not proved.
The theorem is an actual finite coordinate criterion, not a claim that an
arbitrary abstract graph is geometrically realized.

An exact source extension demonstrates why common height is too restrictive:
with one retained isolate held fixed, every nonzero common translation of the
two original owners in the sharp small cloud fails, in every direction. Unequal
heights succeed. Giving that same isolate a free zero-floor variable also
produces a certified endpoint. The sources are explicitly nonglobal and lack
the positive full-contact KKT equilibrium; they are not canonical survivors.

## 2. Source data and exact pair inequalities

Let A be a finite unit-separated planar source of diameter D, and fix a unit
direction v with perpendicular Jv. Partition every source label into fixed
group G_0 and disjoint nonempty groups G_1,...,G_r. G_0 is nonempty. Assume no
old unit contact joins two different positive groups. Internal contacts are
unchanged by a group's translation. Isolates may have separate singleton
groups, may be assigned to core groups, or may remain in G_0; every label is
retained.

Translate group i by s_i v with s_0=0 and

\[
 0\le s_i\le U_i,\qquad U_i>0.
\]

For a crossing old contact from group i to G_0, orient its unit vector r from
the group to the fixed label. Its squared lower slack is

\[
 |r+s_i v|^2-1=s_i(s_i+2r\cdot v).
\]

Define the exact release floor

\[
 F_i=\max\bigl(\{0\}\cup
       \{-2r\cdot v:r\text{ is an old contact from }G_i\text{ to }G_0\}\bigr).
                                                        \tag{2.1}
\]

Our allowed domain is `s_i=0 or s_i>F_i`. Every active old contact cut then
strictly opens. An isolate-only group has F_i=0. If a supplied parallel
contact-preserving O–O proposal is d_i=delta_i v, exact old-contact preservation
gives `r dot v=-delta_i/2` on every cut contact, hence F_i=delta_i. This is a
specialization, not a required hypothesis of the theorem.

For a source pair p in group i, q in group j, put

\[
 a=(p-q)\cdot v,\quad z=(p-q)\cdot Jv,\quad
 d'=a+s_i-s_j.
\]

Its endpoint squared distance is exactly `z^2+(d')^2`.

### Every upper pair, including inactive pairs

Let `u=sqrt(D^2-z^2)`. Since the old pair is at most D, `u>=|a|`. The complete
upper constraint is precisely

\[
 s_i-s_j\le u-a,\qquad s_j-s_i\le u+a.             \tag{2.2}
\]

Both costs are nonnegative. Equality is permitted: contact loss makes a new
diameter pair harmless to the contradiction. No weighted-diameter average
or small-cloud assumption is used. Internal-group pairs are unchanged.

### Old noncontacts with transverse separation at most one

If |z|>1, the lower bound is always strict whatever the heights. If |z|<=1,
put `ell=sqrt(1-z^2)`. For an old noncontact, `|a|>ell`, so a!=0. Retaining its
old projected order and strict unit clearance is exactly

\[
 \begin{cases}
 s_i-s_j<-a-\ell,&a<0,\\
 s_j-s_i<a-\ell,&a>0.
 \end{cases}                                      \tag{2.3}
\]

The relevant cost is strictly positive. At |z|=1 this keeps the height
difference nonzero; ignoring this boundary case would create a unit contact.
Other endpoints that reverse these old noncontact orders are outside this
criterion, even if they are unit-separated.

Make a directed arc i->j of cost c for every inequality `s_i-s_j<=c` from
(2.2), and for the weak relaxation of (2.3). Include i->0 of cost U_i. All
costs are nonnegative; old-noncontact arcs have strictly positive cost. There
can be several actual pair witnesses for an arc; retain the smallest cost and
one actual witness attaining it. All source pairs, including isolate pairs,
enter this construction.

## 3. Candidate FC: exact shortest-path floor closure

Start Z={0}. At each round, let c_i be the shortest directed path cost from i
to any vertex of Z, with the height-bound arcs included. The zero vertices
have c_i=0 and all costs are finite, because i->0 of cost U_i is present.
Adjoin to Z every positive group with `c_i<=F_i`. Repeat until no new group
is adjoined; at most r nonempty deletion rounds occur. Write I for the final
positive groups outside Z.

**Theorem FC.** There exists an endpoint in the domain
`s_i=0 or s_i>F_i`, satisfying all upper constraints and all strict original-
order noncontact constraints, with at least one contact-bearing group active,
if and only if I contains such a group. More generally I is the largest
possible active support of any endpoint in this class.

If I is nonempty, choose one common scaling factor

\[
 \max_{i\in I}{F_i\over c_i}<\lambda<1,
 \qquad s_i=\lambda c_i\ (i\in I),\quad s_i=0\ (i\in Z). \tag{FC.1}
\]

This is an explicit feasible coordinate endpoint. A contact-bearing group
means a group with at least one old contact to G_0. In the canonical connected
positive core with proper disjoint core groups, every core group is contact-
bearing; supplementary isolate groups are not.

### Necessity and preservation through the elimination rounds

For any feasible endpoint, a path from i to a currently forced-zero vertex z
gives `s_i<=sum path costs`, by adding its difference inequalities. A path
ending through a height-bound arc is equally valid. Thus `s_i<=c_i`.
If `c_i<=F_i`, the allowed domain forces s_i=0. Induction over rounds proves
that every group added to Z is zero in every feasible endpoint. Therefore no
feasible active support can exceed I. Strict lower arcs only strengthen this
argument; their weak relaxation cannot falsely eliminate a feasible endpoint.

### Sufficiency and strictification

Final shortest distances satisfy `c_i<=c_j+c_ij` for every source arc. They
also satisfy `c_i<=U_i`. For i in I, final c_i>F_i>=0. Consequently the maximum
ratio in FC.1 is strictly below one. Set c_z=0 at final zero groups; shortest
distances have that value, and their triangle inequalities still hold across
all arcs.

Scaling by lambda preserves every weak inequality:
`lambda(c_i-c_j)<=lambda c_ij<=c_ij`, including zero-cost diameter arcs. It
makes every old-noncontact arc strict, because its cost is positive and
`lambda c_ij<c_ij`. It also gives `s_i>F_i` on every active group and respects
all height bounds. Equations (2.1)–(2.3) now check every old contact, every old
noncontact, every actual diameter, every previously inactive upper pair, and
every retained isolate. This proves sufficiency, maximal support, and the
explicit endpoint formula. QED.

### Signed heights need only two nonnegative solves

The restriction to nonnegative heights does not lose a contact-loss endpoint
with mixed signs in this same order-preserving class. Suppose an endpoint has
arbitrary signed heights t_i, t_0=0, strictly opens every active old contact
cut, and satisfies (2.2) and the strict original-order conditions (2.3).
Replace its heights by `t_i^+=max(t_i,0)`. For any difference inequality
`t_i-t_j<=c` with c>=0,

\[
 \max(t_i,0)-\max(t_j,0)\le\max(t_i-t_j,0)\le c.
\]

For a strict noncontact cost c>0, the new difference is either zero, hence
strictly below c, or positive and at most the old strict difference. Thus
all upper and noncontact constraints survive clipping. A positive active
group keeps its heights and opened cut contacts. A negative group returns
to zero and restores its old contacts; no old contact joins different moving groups,
so this does not create a new coupling. Cardinality and every source pair
remain checked.

If the signed endpoint has a positive contact-bearing group, this produces
a nonnegative contact-loss endpoint. If its contact-bearing groups are all
negative, reverse v, negate the heights, and apply the same clipping argument.
Therefore running FC in directions v and -v is necessary and sufficient for
the existence of **any signed-height contact-loss endpoint in this strict-cut,
original-noncontact-order class**, with the corresponding positive and negative
height bounds. Using U_i=2D in both solves includes every possible signed
height compatible with the fixed reference and diameter D. The condition
of no old contact between different moving groups is essential to clipping;
it is not asserted for arbitrary mutually contacting variables.

### Global consequence and precise limits

If A is triangle-free and I has a contact-bearing group, the endpoint loses
an old contact and creates none. Its contact graph is a strict subgraph of
the old graph, still triangle-free. Its cardinality is unchanged and its
diameter is <=D. For a canonical global contact-minimal source this contradicts
globality if the diameter is smaller, and contact minimality otherwise.
Hence every supplied canonical family must collapse all contact-bearing
groups under FC. An endpoint moving only isolates gives no such contradiction.

There is no need to infer isolate motion from an affine-kernel theorem or an
area allowance. Isolate variables participate in the same actual pair ledger.
When their variables are independent, protected long pairs need not share
displacements, so **all upper pairs must remain in the graph**; one may not
reuse the bounded E ledger without separately retaining its anchor conditions.

The theorem provides a finite replacement, not a feasible straight interpolation.
An active old contact may be shorter than one between the old and new endpoints.
No continuous unit-separated trajectory is asserted or needed to contradict
global minimum diameter with the verified endpoint.

With one fixed source label, every nonnegative height in any diameter-D endpoint
is <=2D: its projected separation from that fixed label is at most D, while
the old projected separation is at least -D. Thus U_i=2D gives a complete test
for this endpoint class without an arbitrary small-cloud restriction. Smaller
U_i give the corresponding exact bounded-box criterion. The class excludes
active cuts that remain exactly unit, order reversals of old noncontacts,
nonparallel moves, and different discrete replacements.

## 4. Actual witness certificates for collapse

Each group removed in a round has an actual shortest-path certificate of cost
at most F_i to a group already forced zero, or to a height-bound terminal.
Arc witnesses are actual pairs from the original source, with exact expressions
from (2.2) or (2.3). A shortest path can be chosen simple after zero-cost cycles
are removed. This is an owner-variable path of source-pair witnesses, **not**
a physical source-point path: successive arcs can use different labels inside
one group. Lifting such a path to a geometric train remains a separate issue.

For a path of total cost <=F_i, every lower-order witness has old distance
<=1+F_i. Indeed moving its lower endpoint by its own arc cost reaches unit
distance, and reverse triangle inequality bounds its old length by one plus
that cost. Every inactive upper witness has old distance >=D-F_i, by the
same argument at its upper boundary. Zero-cost upper witnesses are actual
diameters. These statements locate the actual small-margin pairs without
claiming disjointness, capacity, or an affordable physical route.

The floor-closure obstruction is stronger than an unweighted unary-root path:
its total geometric difference cost must fit the removed group's contact
floor. No multiplicity or boundary loss has been dropped. A canonical theorem
that prevents all such cost certificates for one supplied group would give
an actual finite endpoint by FC; existence of a source-free path does not.

## 5. Exact common-translation obstruction with an unequal-height repair

Use the eight-train source from the preceding Slot 01 report, with integer
H>=30, t=1/(100H^2),

\[
 a_A={1-9t^2\over1+9t^2},\quad
 a_B={1-t^2\over1+t^2},\quad
 \delta_A={12t\over1+9t^2},\quad
 \delta_B={4t\over1+t^2},\quad D^2=H^2+25.
\]

Retain every original label and add one contact-isolated fixed guard

\[
 U=(5,3+g),\qquad g=5\delta_B/2.
\]

The original right top moving label is Rm2=(5,2). The adjacent fixed connector
label RCvert1 is `(5-a_B,3+delta_B/2)`. Consequently U is strictly separated
from both: its squared distances are `(1+g)^2` and `1+15delta_B^2/4`.
All other old and endpoint pairs are checked below. The source has H+80 labels,
the same contact core and eight O–O trains, and one retained isolate.

### A direction-independent obstruction in the small cloud

Put S=2delta_A. For this family,

\[
 a_A,a_B>0.9,\quad S<1/1000,\quad
 11\delta_B/4<\delta_A<3\delta_B,\quad
 \delta_B<1/1000,\quad S<\gamma_D.
\]

**Regression CTG.** No nonempty binary choice of original owners A,B translated
by one common nonzero vector b=(x,y), |b|<=S, satisfies every source lower and
upper bound. This permits any direction of b. Guard U and all old zero labels
remain fixed. It does not assert failure when U is also allowed to move.

For a selected owner i, its actual rungs include both contact vectors
`(plus-or-minus a_i,-delta_i/2)`. Their weak unit lower bounds require

\[
 x^2+y^2-\delta_i y\ge2a_i|x|.                  \tag{CTG.1}
\]

Since x^2<=S|x| and 2a_i-S>1, if y<=0 this implies
`|x|<=3delta_A|y|`. Its old bottom diameter to q=(0,H) requires
`x^2+y^2<=10|x|+2Hy`. For y<0 the right side is at most
`(30delta_A-2H)|y|<0`, impossible. If y=0, CTG.1 forces x=0. Thus any admissible
nonzero b has y>0. Equation CTG.1 then gives

\[
 y(y-\delta_i)\ge(2a_i-S)|x|\ge0,
 \qquad y\ge\delta_i,
 \qquad |x|<S^2<36\delta_B^2.                   \tag{CTG.2}
\]

If only A is selected, the old vertical pair Am0:Bm0 has gap
`1+delta_A-delta_B/2`; CTG.2 makes its new positive vertical separation at most
`1-delta_B/2`. If only B is selected, Cm0:Dm0 has old gap `1+delta_B/2`, and
its new positive vertical separation is at most `1-delta_B/2`. If both are
selected, Rm2:U has old gap `1+5delta_B/2`; y>=delta_A makes its new positive
vertical separation less than `1-delta_B/4`. In all cases its horizontal
separation is |x|, and

\[
 |x|^2+(1-\delta_B/4)^2
 <1296\delta_B^4+(1-\delta_B/4)^2<1.
\]

The last inequality follows from delta_B<1/1000. Each case has a strict
lower violation. This proves CTG, conditional only on the directly checked
old contact and actual diameter data, not on a KKT assertion. QED.

### Unequal core heights, retaining U fixed

Instead set

\[
 s_A=\delta_A+\delta_B/4,\qquad s_B=2\delta_B,
 \qquad s_U=0.                                  \tag{5.1}
\]

Every old rung opens: its squared slack is `s_i(s_i-delta_i)>0`. Exactly 24
old contacts are removed. The two old implication gaps remain strictly above
one, with new vertical separations `1+5delta_B/4` and
`1+delta_A-5delta_B/4`. For each Emj:Fmj, the horizontal distance is
`d=1-delta_B^2/4` and the residual vertical separation is `3delta_B/4`, giving

\[
 d^2+(3\delta_B/4)^2-1
 ={\delta_B^2+\delta_B^4\over16}>0.
\]

Rm2:U has new distance `1+delta_B/2>1`. These identities repair the specific
blocking pairs; the certificate checks all other source pairs. The exact new
squared diameter is the old right pair's

\[
 D^2-4H\delta_B+4\delta_B^2<D^2.                \tag{5.2}
\]

Thus independent heights escape a geometric obstruction that excludes every
small common vector, while retaining the guard label and cardinality.

### Shortest-path construction with the fixed guard

With height bounds U_A=U_B=S, the only small binding arcs are

\[
 B\to0:\ g=5\delta_B/2,\qquad
 A\to B:\ c=\delta_A-\delta_B-\ell,\qquad
 B\to A:\ \delta_B/2,
\]

where `ell=sqrt(1-(1-delta_B^2/4)^2)`. Actual H also gives zero-cost arcs
`0->A` and `0->B`, which do not limit positive heights. The A->B cost comes
from Em0:Fm0 and supersedes the larger Am0:Bm0 cost. The actual full-pair
compiler verifies that no other pair gives a tighter cost below S.

Final exact caps are `c_B=g` and `c_A=g+c`. Both exceed their release floors
delta_B and delta_A for small t. Scaling by 9/10 gives an endpoint by FC.
The checker conservatively lowers algebraic costs using rational enclosures,
so its computed c_A is a rigorous lower bound on the exact cap, while c_B=g
is exact. It verifies `s_A>delta_A`, `s_B=9delta_B/4`, all 24 contact losses,
strict original noncontact orders, and the exact new maximum

\[
 D^2-{9\over2}H\delta_B+{81\over16}\delta_B^2<D^2. \tag{5.3}
\]

### Adaptive transport of the retained isolate

Give U its own variable, with F_U=0 and U_U=S. The guard arc is now B->U of
cost g rather than B->0. The reverse lower arc at RCvert1:U points 0->U and
does not limit upward U motion. Full-source compilation gives final caps S
for A,B,U. Set

\[
 s_A=s_B=s_U=9\delta_A/5.                       \tag{5.4}
\]

This retains and transports the isolate. All 24 old rung contacts open,
every old noncontact remains strict, and both old diameter pairs attain the
new maximum `D^2-(18/5)H delta_A+(81/25)delta_A^2<D^2`. No bounded-face
embedding or unproved anchor reassignment is used: every pair involving U
is evaluated explicitly. This does not establish isolate transport in every
canonical source; it certifies the additional freedom handled by FC.

### Exact signed endpoint and its positive clipping

Use the manual core heights (5.1) and give U height `-delta_B/4`. This is a
mixed-sign endpoint with the same 24 contact losses and the same maximum
(5.2). Rm2:U has new separation `1+delta_B/4`; RCvert1:U has squared lower
slack `45delta_B^2/16>0`. All other pairs are checked by the certificate.
Clipping the negative U height to zero recovers precisely the already verified
manual endpoint. This is a source-realized check of the signed-clipping
argument, rather than an arbitrary graph example. In the opposite direction
the actual old diameter pairs give zero-cost upper arcs A->0 and B->0,
eliminating both core groups at the first floor-closure round. The isolate
alone can retain a positive cap but supplies no contact-loss contradiction.

## 6. Analytic unbounded nonglobal family and exact certificates

At t=0 the preceding fixture has eleven critical noncontact pairs. Adding U
gives two more, Rm2:U and RCvert1:U. Every other low-cluster noncontact is
strictly separated at t=0. Symbolic rational expressions give these relevant
leading squared lower slacks in the old, manual unequal, transported isolate,
and mixed-sign endpoints, respectively:

| Pair | Old | Manual unequal | Isolate transport | Mixed signs |
| --- | --- | --- | --- | --- |
| Am0:Bm0 | 20t | 10t | 20t | 10t |
| Cm0:Dm0 | 4t | 14t | 4t | 14t |
| Emj:Fmj, j=0,1,2 | 56t^2 | t^2 | 56t^2 | t^2 |
| Rm2:U | 20t | 4t | 20t | 2t |
| RCvert1:U | 60t^2 | 60t^2 | (21804/25)t^2 | 45t^2 |

The other six critical pairs retain positive leading terms from the predecessor
or are unaffected. The checker verifies all thirteen signs, positive limiting
denominators, and 5,858 strict limiting noncontacts. A single small positive
t interval therefore works for every critical pair; finitely many other
low-cluster pairs remain strict by continuity. Later vertical-chain labels
are uniformly separated from the low cluster, with old vertical contacts
unchanged. Thus the old source and the manual/transport endpoints are valid
for every sufficiently large H. H=30,31,100 are individually certified; no
uniform lower-feasibility onset H=30 is asserted.

For upper bounds all low labels, including U and its transported position,
remain in [-6,6]x[0,23]. The endpoint heights are below S. Internal low-cluster
squared lengths are at most 673. Pairs with one high chain label and a low
label of height >=1 have squared distance at most `(H-1)^2+36`, below each
stated maximum for H>=30. The only low labels below height one are the old
bottom moving labels and their fixed counterparts. Substitution identifies
the stated maxima; the fixed counterparts have squared gap greater than eight
below those maxima by the predecessor's uniform estimate
`25-4.1^2-4H delta_A-delta_A^2/4>8`. Chain internal distances are smaller.
These cases check the actual maximum, not only old diameter shortening.

An independent square-grid source of the same H+80 cardinality has squared
diameter at most `2(H+80)<H^2+25` for H>=30, using a square of side
`ceil(sqrt(H+80))` lattice sites. Thus the original sources are strictly
nonglobal whenever valid. Their old core also retains the positive-contact
KKT failure identified in the predecessor. Neither globality nor canonical
stress is inferred from the preserved contacts and actual O–O trains.

Run:

```sh
python3 research/verify_target_c_unequal_height_release_2026_10_10.py \
  --heights 30 31 100 --symbolic-limit
```

The checker uses exact SymPy contact identities and 120-bit rational root
enclosures for strict comparisons. It checks 225,680 full pair-state instances
in eight states, the original source, three common-height failures, the manual
unequal endpoint, the shortest-path endpoint, and the transported-isolate
endpoint and mixed-sign endpoint. It verifies contact losses, all new maxima, every retained isolate
pair, relevant projected orders, and the thirteen symbolic critical signs.
Saved output:
`research/certificates/target_c_unequal_height_release_2026_10_10.jsonl`.

The implementation's conservative rational costs make a successful computed
endpoint rigorous. Failure of conservative lower-enclosure costs is **not**
an exact infeasibility certificate for arbitrary algebraic source data; FC's
exact necessity statement uses exact costs. The direction-independent CTG
regression and the universal floor-closure proof are analytic arguments, not
inferences from a finite search. No independent audit is claimed.

Local repository validation passed: theorem-state consistency, the PR transaction
check against origin/main, active-route summaries, Ruff check/format, and the
full-branch whitespace check. The predecessor's complete symbolic-limit
certificate is unchanged after making its helper's parameter explicit. No
canonical theorem dependency or state version changed; the registered canonical
certificate suite was not rerun for this candidate-only checkpoint. Repository
checks validate the ledger and code conventions, not the analytic proof or the
unextracted canonical source family.

## 7. Remaining source theorem

Prove that every sufficiently large canonical triangle-free C-II source admits
a direction v and disjoint proper contact-core groups, with no old contact
between different moving groups, for which FC leaves at least one contact-
bearing group active when every contact isolate is retained as a free variable
and every source pair enters the cost graph. Actual stopped-train groups are
the preferred extraction mechanism, but singleton actual-upper safety and
one common height are no longer required.

Equivalently, extract a source family for which its actual geometric costs
cannot support a full floor-collapse certificate. This needs a source-specific
inequality or endpoint construction; generic graph reachability and an owner-
level path without a geometric bound do not prove it. FC then supplies a
complete finite contact-loss contradiction. No canonical obstruction or
theorem-state entry is promoted by this report.
