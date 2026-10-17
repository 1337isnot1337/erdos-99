> Generated reading edition · [exact source](../../../docs/reports/target_c_owner_component_anchoring_and_source_realized_sink_2026-10-10.md) · source SHA-256 `a8e3e9a42129eef055bbc6b494322fefaa749b2f373ea76631fe5d3fb7620eff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E5AE020CD36C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — component anchoring, strict stress gain, and a source-realized owner sink

**Date:** 2026-10-10. **Worker:** Slot 01.\
**Starting main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.\
**Theorem state:** `2026-10-10.audit.234`.\
**Branch:** `research/sol61-slot01-outer-motion-20261010`.\
**Classification:** proved candidates awaiting independent audit; exact regression. The artifact is unreviewed and noncanonical.\
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.\
**External theorem imports:** none. **Level I and C-II remain OPEN.**

## 1. Endpoint and claims

The assigned endpoint is an actual same-cardinality full-source finite move,
passing every lower and upper pair and removing an old diameter or contact.
The relevant promoted reductions are `C-OO-LOWER-BLOCKER-LOCALIZATION`,
`C-DISJOINT-SWAP-2SAT`, `C-OO-TERMINAL-OWNER-CAPACITY`,
`C-OO-OVERLAP-AWARE-ROOT-RUN-CAPACITY`, and the Audit.184/185 sink results.
They do not extract a feasible shortening assignment.

This report supplies three canonical-source **candidate deductions**, and a
separate exact nonglobal source construction:

1. Every contact component of an independently translated owner, and every
   contact component of its complement, must contain an actual diameter
   endpoint. A sharper resultant identity holds component by component.
2. In the canonical acute independent-owner model, **every nonzero binary
   selection has strictly positive weighted old-diameter deficit**. Thus an
   additional hypothesis saying that a nonzero selection strictly shortens at
   least one old diameter can be removed. Upper feasibility still must be
   checked pair by pair.
3. After deleting at most `2d_H` supplied parent owners, their mixed
   contact/diameter components give a refined actual O–O family in which every
   binary state passes every full-source upper constraint. Singleton actual
   diameter safety, acuteness, the canonical small-cloud/dispatch rules, and
   parent unary safety suffice; no nonzero lower-feasible state is asserted.
4. Connected geometric realization, disjoint actual O–O cuts, unary rhombus
   safety, the sharp small-cloud bound, and complete upper safety do not alone
   make an owner Horn system feasible. An explicit family realizes
   `A => B`, `B => A`, `not(A and B)`. The same sources have an exact strict
   sub-diameter endpoint after splitting the repeated owner regions. They lack
   the canonical positive KKT equilibrium.

The implication chain for claims 1–3 is

```text
positive KKT equilibrium + exact contact-preserving owner selection
 -> loaded port in every moving contact component
 -> source stress gain for every nonzero core selection
 -> any fully lower/upper-admissible nonzero selection is a finite contradiction.
```

This leaves the assignment/extraction obligation open. Claim 4 prevents
replacing that obligation by geometric realization alone, and demonstrates why
owner-component refinement must preserve the actual upper ledger.

## 2. Candidate: every moving contact component has an actual diameter port

### Statement CA

Let a finite source have unit-contact graph C on a connected core V, actual
diameter graph H, and a KKT equilibrium

$$
 \sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
 =\sum_{j:ij\in H}\beta_{ij}(p_i-p_j),
 \qquad \alpha_{ij}>0,\quad\beta_{ij}\ge0.
$$

All diameter endpoints considered here lie in V. Suppose a nonempty proper
subset G can be translated by a nonzero vector d while its complement is fixed,
preserving every contact exactly. No upper or inactive-lower feasibility is
assumed.

Then every connected component W of C[G] and every connected component of
C[V minus G] is incident with an H-edge leaving that component, with positive
beta. In particular each contains an actual diameter endpoint.
For a component W of C[G], write

$$
 a_W=\sum_{ij\in\delta_C(W)}\alpha_{ij},
 \qquad b_W=\sum_{ij\in\delta_H(W)}\beta_{ij}.
$$

Orient its crossing pairs from W to its complement. Then

$$
 \sum_{ij\in\delta_H(W)}\beta_{ij}(p_i-p_j)\cdot d
 =-{\lVert d\rVert^2\over2}a_W<0.                 \tag{CA.1}
$$

### Proof

No contact joins W to another component of C[G]. Every crossing contact joins
W to V minus G, so exact preservation under the translation gives

$$
 1=|p_i-p_j+d|^2=1+2(p_i-p_j)\cdot d+|d|^2.
$$

Thus every crossing contact has projection `-|d|^2/2` on d.
Summing equilibrium over W cancels all internal contact and diameter forces.
Taking its scalar product with d proves (CA.1). Connectedness and properness
ensure a crossing contact; positivity gives a_W>0. Consequently the right-hand
diameter sum is nonzero, and has an actual crossing diameter edge with positive
weight. This proves the assertion for W.

For a component of the complement, translating that component by -d preserves
its crossing contacts: these are precisely the contacts to G, and their
relative change is the negative of the original G translation. Repeat the same
argument. No isolate has been deleted; this statement concerns core components,
not components consisting entirely of contact isolates. QED.

### Refinement and parallel-region corollaries

In the acute independent-owner model no contact joins distinct nonzero owners.
Indeed the mixed difference of the four squared contact lengths is
`-2 d_i dot d_j`, whereas all four equal one. Their positive dot product makes
such a contact impossible. An owner can therefore be split into its contact
components while preserving all old contacts in every refined binary state.
Applying CA to each component shows that every refined core owner has a loaded
port. Every owner's complement also has one, so its loaded-hull word has a
nonempty complement.

For parallel positive translations `d_i=s_i v`, every zero-label contact
component has a loaded port as well. A crossing contact oriented from zero to
owner i has projection `s_i/2>0` on v. Summing equilibrium over the zero
component gives a strictly positive diameter resultant. Nonzero components have
the strictly negative resultant in (CA.1). This is a source-level condition on
actual diameter reactions, beyond the abstract region-tree bank.

**Important limit:** refinement does not preserve upper feasibility. If an old
diameter joins two components formerly moved by the same d, moving either one
alone gives squared changes `2 r dot d+|d|^2` and `-2 r dot d+|d|^2`.
Their sum is `2|d|^2>0`; at least one refined singleton lengthens that diameter.
The refined actual-diameter clauses must be recomputed.

CA extends the canonical ZGS.3 cut-resultant identity from a single parallel
O–O train shore to every contact component of an arbitrary exact rigid
translation. It does not extract a translating set or guarantee an upper-safe
state. Dependencies are KKT equilibrium and positivity; PSD is not used.

## 3. Candidate: strict weighted gain is automatic for acute core owners

### Statement SG

Use the canonical C-II source with D>=9 and connected nonisolated core V.
Choose its relative-interior KKT stress

$$
 \Omega=L_C(\alpha)-L_H(\beta)\succeq0,
 \quad \Omega P=0,
 \quad\ker\Omega=\operatorname{span}\{1,P_x,P_y\},
 \quad \sum_H\beta_h=1,\quad\sum_C\alpha_e=D^2.
$$

Let nonempty proper pairwise disjoint core sets G_i have nonzero prescribed
translations d_i with `d_i dot d_j>0`. Suppose every original contact is
preserved in every binary owner selection. Assigned contact isolates may follow
these owners; all of them remain subject to the separate full-source ledger.
Set

$$
 \kappa_i=1_{G_i}^{T}\Omega1_{G_i},\qquad
 b_{ij}=\sum_{h\in H[G_i,G_j]}\beta_h.
$$

For a selection x, its core placement Q satisfies the exact identity

$$
 \sum_{h\in H}\beta_h\bigl(D^2-|Q_h|^2\bigr)
 =\sum_i x_i\kappa_i|d_i|^2
  +2\sum_{i<j}x_i x_j b_{ij}(d_i\cdot d_j).       \tag{SG.1}
$$

Every kappa_i is strictly positive. Consequently every nonzero selection
strictly shortens at least one actual diameter edge, quantitatively by at least
`sum_i x_i kappa_i |d_i|^2` in squared length. This conclusion does not say that
all actual diameter edges shorten.

### Proof

As above, no contact joins distinct moving owners. The off-diagonal stress sum
between disjoint G_i,G_j is therefore `1_Gi^T Omega 1_Gj=b_ij>=0`.

If kappa_i=0, PSD implies `1_Gi` belongs to the affine kernel. Since it takes
only the values zero and one and is nonconstant, all core points would lie on
two parallel lines. Their convex hull has at most four vertices. Canonical
full-source force-hull geometry puts every loaded endpoint among the core hull
vertices; canonical Woodall and ZRF give

$$
 q\ge h\ge\lceil D\rceil\ge9.
$$

This contradicts the four-vertex bound. Thus kappa_i>0.

Writing `U=Q-P=sum_i x_i 1_Gi d_i`, equilibrium cancels the cross term:
`tr(Q^T Omega Q)=tr(U^T Omega U)`.
Contact preservation and the virial normalization give

$$
 \operatorname{tr}(Q^T\Omega Q)
 =D^2-\sum_h\beta_h|Q_h|^2.
$$

Expanding the quadratic form in U proves (SG.1). Its diagonal terms are
strictly positive whenever selected, and its mixed terms are nonnegative.
Since the beta weights sum to one, some old diameter squared deficit is at
least their weighted average, which is bounded below by the stated diagonal
sum. QED.

Thus, for a family satisfying these hypotheses, a fully admissible nonzero
state already has the strict old-diameter row required by
`C-DISJOINT-SWAP-2SAT`. No separate pinned-shortening search is needed. Actual
upper inequalities, inactive upper strictness, every lower pair, and isolate
transport remain indispensable.

Dependencies: restored C-I PSD; `C-ZRF`; canonical virial normalization;
`C-FS-GEOM`/force-hull geometry; `C-WOODALL`; `C-MIXED-CORE-FINITE-RIGIDITY`
provides compatible finite-equality context but is not required in the proof.
No affine-kernel conclusion is applied to contact isolates.

## 3.1. Candidate RM: upper-safe refinement along actual mixed components

### Statement

Take a **supplied**, subfamily-stable actual disjoint-owner O–O system in the
canonical source, with nonempty proper core owners G_i, mutually acute d_i,
contact preservation under every binary choice, and translation cloud

$$
 s=\operatorname{diam}\{0,d_1,\ldots,d_r\}
 <\min\{D-\sqrt{D^2-1},\sqrt2-1\}.
$$

Assume each parent singleton weakly shortens every actual diameter, and passes
all its unary strict-rhombus tests. Use one fixed canonical long-pair dispatch
and its set E of at most d_H inactive exceptional upper pairs; use compatible
bounded-face transport. No lower feasibility is assumed.

Discard every parent owner containing a core endpoint or an isolate anchor of
an exceptional pair. At most 2|E|<=2d_H parent owners are discarded. Among each
remaining G_i, take the connected components of the induced **actual** mixed
graph `(C union H)[G_i]` as new core owners, retaining d_i on each. Assign every
bounded-face isolate to its face's refined owner, every anchored exterior
isolate to its anchor's refined owner, and keep unanchored isolates fixed.

Then every binary selection of the refined owners:

1. preserves every old contact;
2. weakly shortens every actual diameter;
3. keeps every inactive upper pair strictly shorter than D;
4. passes every unary rhombus test;
5. retains every source label and has strictly positive weighted old-diameter
   deficit if it is nonzero.

Its remaining lower clauses are actual outer-contact-face near-unit pairs.
Thus the source has a finite lexicographic contradiction if and only if this
refined family has a nonzero strict lower-admissible selection. The refinement
itself does **not** prove such a selection exists.

The old arbitrary identifications between contact components can now be
retained only through actual diameter edges internal to the parent owner. A
mixed component can still contain several contact components and several loaded
runs. There is no assertion that owner recurrence disappears.

### Complete proof

**Exceptional-owner deletion.** For an E endpoint that is core, mark its parent
owner, if any. For an anchored isolate endpoint mark the parent containing its
anchor; an unanchored endpoint is fixed. Each pair marks at most two parent
owners. Bounded-face isolates have all pair distances at most
`sqrt(D^2-1)`, by the canonical variance bound, so they are not E endpoints.
After deletion both endpoints of every E pair are fixed under every refined
state. This deletes proposals, not source labels.

**Contacts.** No old contact joins distinct moving parents, by the acute mixed
norm identity. A contact internal to one parent is an edge in its induced mixed
graph and hence has its two endpoints in the same refined owner. A contact
from that parent to the fixed source undergoes one of its original singleton
states. Every old contact remains unit. A complete selected train has the same
refined owner on its moving shore throughout: its successive moving vertices
are joined by the other sides of its rhombi. Thus refinement does not break a
train into unrelated edge selections, and retains actual stopped O–O cuts.

**Actual diameter pairs.** If both endpoints belong to one parent, the actual
H edge puts them in the same refined owner; their distance is unchanged. If
only one endpoint moves, the length is the parent's singleton length, assumed
at most D. If two different parents move, orient the old diameter vector r from
the second endpoint to the first. The two singleton squared changes are

$$
 g_i=2r\cdot d_i+|d_i|^2\le0,
 \qquad g_j=-2r\cdot d_j+|d_j|^2\le0.
$$

Their joint squared change is

$$
 g_{ij}=g_i+g_j-2d_i\cdot d_j<0.
$$

This checks every possible refined state of every old diameter. It also proves
that acute parent singleton safety suffices for simultaneous actual-diameter
safety; this fact is specific to old pairs already at D, not inactive uppers.

**Inactive upper pairs.** Let `L=sqrt(D^2-1)`. The canonical long-pair proof in
`C-LONG-PAIR-ISOLATE-DISPATCH` shows that every endpoint of a pair longer than L
outside the loaded set is an isolate. Outside E, each such inactive pair has
equal prescribed endpoint displacements: its endpoints have one common anchor
or are both unanchored. There is no protected inactive core-core long pair.
The same statement holds after refinement because anchor identity is retained.
The E pairs were fixed by deletion. Every remaining inactive pair has old
length at most L and relative displacement at most s, so its endpoint length
is at most `L+s<D`. This proves the full upper ledger, including isolates.
The general-cloud argument is the promoted small O–O multishear extension of
`C-OO-LOWER-BLOCKER-LOCALIZATION`; it is not an assumption that all d_i coincide.

**Bounded-face transport and unary tests.** Every bounded nonquadrilateral
contact-face boundary is uncut in an O–O system, connected by actual contacts,
and therefore lies in one refined owner. Its assigned isolates move with that
owner. The canonical near-unit cofaciality/variance argument gives no new lower
or upper blocker there. A parent-active strict rhombus has two adjacent moving
vertices of one owner and two fixed vertices; the moving adjacent vertices are
joined by a contact, hence remain in one refined owner. Its local state is
exactly the old parent state and passes the stipulated unary test. All other
rhombi are unchanged or translate rigidly. Canonical O–O localization now puts
every remaining lower clause in the actual outer face.

**Strict gain and consequence.** The refined translations remain mutually
acute, including equal vectors on split components. Their core sets are
nonempty, proper, and disjoint. SG proves a positive weighted old-diameter
deficit for every nonzero choice. When its outer lower clauses also pass, the
endpoint has the exact old contact graph, no new diameter pair, and a strictly
shortened old diameter. It contradicts global diameter minimality or secondary
actual-diameter-pair minimality. All points, including all isolates, remain.
QED.

### Scope and exact improvement

RM upgrades **supplied parent singleton actual-upper safety** to an actual
refined family with all-state full-source upper safety after a bounded deletion.
It isolates the owner identifications that the actual mixed graph forces, and
makes the unreviewed source-free contraction of distant labels unnecessary.
It supplies neither the parent family nor lower satisfiability. In particular
it cannot turn the source-rich SR regression into a canonical counterexample:
SR lacks the positive KKT/long-pair hypotheses used in RM.

A useful count consequence is now expressed in actual source components. Let K
be the total number of induced `(C union H)` components in the surviving parents.
For sufficiently large D, applying canonical
`C-OO-LOWER-WITNESS-OWNER-CAPACITY` to the refined singleton proposals gives

$$
 K\le2m_B+3(x_B+Z_{\rm out}),
 \qquad K\le147(x_B+m_B)\quad\hbox{in Type II}.
$$

The refinement has singleton upper safety, unary safety, strict old-diameter
gain, fixed isolate assignment, and canonical outer-face witnesses, exactly the
hypotheses of that count. No arbitrary owner-label identification enters K.
At least `r-2d_H` parent owners survive, but neither bound extracts r or proves
that a nonzero simultaneous state exists.

Dependencies: CA and SG as candidates in this report; canonical
`C-LONG-PAIR-ISOLATE-DISPATCH`, `C-OO-LOWER-BLOCKER-LOCALIZATION`,
`C-NEAR-UNIT-CONFLICT-GEOMETRY`, and `C-DISJOINT-SWAP-2SAT`. The algebra for old
actual diameters is proved above. No theorem-state promotion is requested on
this author's authority.

## 4. Exact source-realized Horn sink and an explicit refined endpoint

### Statement SR — regression and proved construction

For all sufficiently large integer H there are connected, triangle-free,
unit-separated planar sources of `H+79` labels, diameter `sqrt(H^2+25)`, and
exactly two actual diameter pairs. They admit two independent acute owner
translations with these properties:

- their cloud diameter is below `D-sqrt(D^2-1)`;
- all four binary states preserve every old contact;
- the active contact cuts are eight pairwise disjoint actual stopped O–O
  trains, each passing through two strict rhombi;
- all unary rhombus tests and all full-source upper constraints pass in every
  state, and every nonzero state shortens an old diameter;
- their complete lower formula is exactly
  `A => B`, `B => A`, and `not(A and B)` (the last clause has three physical
  witnesses), so only zero is feasible;
- splitting the repeated owners and moving just the two loaded column regions
  gives a triangle-free same-cardinality source with diameter squared
  `H^2+25-2H*delta_B+delta_B^2 < H^2+25`.

These sources are nonglobal and do not possess strictly positive contact KKT
weights. This is a regression against **the listed reduced hypotheses implying
Horn feasibility**, not against an endpoint theorem using canonical KKT,
rigidity, population, or diameter density.

### Coordinates and exact construction

Let `t=1/(100 H^2)`, initially allow any sufficiently small positive t, and put

$$
 a_A={1-9t^2\over1+9t^2},\quad\delta_A={12t\over1+9t^2},
 \qquad a_B={1-t^2\over1+t^2},\quad\delta_B={4t\over1+t^2},
 \qquad d=1-\delta_B^2/4.
$$

A strip with owner I, base `(x,y)`, side sigma in {-1,1}, and three consecutive
levels J has moving vertices `(x,y+j)` and fixed vertices
`(x+sigma*a_I,y+delta_I/2+j)` for j in J. Join successive vertices in each
column and corresponding vertices across it. Its rungs have length one;
translation `(0,delta_I)` flips their vertical component and retains unit
length. Its two four-faces have diagonal squared lengths `2 +/- delta_I`,
strictly greater than one for small t.

Use these eight strips:

| Strip | Owner | Base | Fixed side | Levels |
|---|---|---|---|---|
| L | A | (-5,0) | +1 | 0,1,2 |
| R | B | (5,0) | -1 | 0,1,2 |
| A | A | (0,4) | -1 | -2,-1,0 |
| B | B | (0,5+delta_A-delta_B/2) | -1 | 0,1,2 |
| C | B | (0,11) | +1 | -2,-1,0 |
| D | A | (0,12+delta_B/2) | +1 | 0,1,2 |
| E | A | (0,18) | -1 | 0,1,2 |
| F | B | (d,18+delta_A-delta_B) | +1 | 0,1,2 |

The reproducible construction connects their fixed columns by unit paths and
adds the fixed chain `(0,k)`, k=22,...,H. The exact path definitions and all
coordinates are in
`research/verify_target_c_source_realized_owner_sink_2026_10_10.py`, class
`Source.build`. Each two-edge cap joining rational endpoints p,q with
`1<|q-p|<2` uses the algebraic middle point

$$
 {p+q\over2}\ \pm\sqrt{1/|q-p|^2-1/4}\,J(q-p).
$$

The four-edge lower connector between the E/F fixed columns uses two repetitions
of each vector `(q-p)/4 +/- sqrt(1/|q-p|^2-1/16) J(q-p)`.
All remaining connector steps are horizontal or vertical unit steps. These
form a tree between the eight strips. The graph has `H+94` contact edges and
`H+79` vertices, hence sixteen bounded faces, exactly the two rhombi per strip.
The eight three-rung train curves end in the outer face and are disjoint proper
crosscuts. Removing their 24 contacts gives one fixed component and eight
moving column components. Every owner recurs on four of these components.

### Complete lower proof, including the infinite-family claim

At t=0 all noncontact limiting pairs have distance at least one. Exactly eleven
have distance one; the symbolic certificate lists every one. Their squared
lower slacks have the following nonzero leading terms, with states ordered
`00,10,01,11`:

| Physical pair | Order | Leading coefficients |
|---|---:|---|
| Af-2 / LAstraight2 | t^2 | 72,72,72,72 |
| Am0 / Bm0 | t | 20,-4,28,4 |
| Af0 / Bf0 | t | 12,12,12,12 |
| Cf-2 / RCstraight2 | t^2 | 8,8,8,8 |
| Cm0 / Dm0 | t | 4,28,-4,20 |
| Cf0 / Df0 | t | 12,12,12,12 |
| Emj / Fmj, j=0,1,2 | t^2 | 56,8,136,-8 |
| DFarmB2 / DFvertical5 | t | 4,4,4,4 |
| FQleft1 / (0,22) | t^2 | 88,88,88,88 |

These eleven slacks are rational functions of t; their denominators have
positive limit and the exact numerator leading coefficients are nonzero.
Thus their signs are as shown for every sufficiently small positive t.
All other noncontact limiting pairs have strict positive slack and remain
strict by continuity. There are only finitely many low-cluster pairs, so one
common positive onset works. No interchange with an infinite pair set is
used: the growing high chain has x=0, unit-spaced heights at least 22; its
lower checks with the finite cluster reduce to its first two heights, and
its internal checks are immediate. The code's symbolic limit certificate
checks the 109-point H=30 truncation, which includes both those heights.

Consequently only 10 fails Am0/Bm0, only 01 fails Cm0/Dm0, and only 11 fails
the three E/F pairs. This proves the stated full lower formula for every
sufficiently small positive t. The stable connector step counts used by
`Source` agree with those of `SymbolicSource` in this range. Since t_H tends
to zero, the family exists for all sufficiently large H; **the general proof
does not claim a uniform onset H=30**. The three explicit heights below are
separately certified.

### Complete upper proof

For sufficiently small t, the finite cluster is in `[-6,6] x [0,23]` in every
state. Cluster points below height one are the bottom-strip points, with
absolute x at most five. The growing fixed high chain has x=0 and heights
22,...,H. Thus:

- cluster pairs have squared distance at most `12^2+23^2=673<D^2`;
- a cluster point of height at least one is at squared distance at most
  `(H-1)^2+36 < H^2+25` from any high-chain point, for H>=30;
- a cluster point below one is at squared distance at most `H^2+25`, with
  equality only at `(+-5,0)` against `(0,H)` in an unselected bottom strip;
- high-chain internal pairs are strictly shorter than D.

This proves all upper checks, including formerly inactive pairs. The two
actual diameter pairs are `(0,H)` with `(-5,0)` and `(5,0)`. Selecting owner I
reduces its pair's squared length by `2H delta_I-delta_I^2>0`.
Also `delta_A<12/(100H^2)` and `D<H+1`, so `2D delta_A<1` for H>=30;
therefore `delta_A<1/(2D)<D-sqrt(D^2-1)`.

### Refined finite endpoint and exact failure of KKT

Move only the L moving column by delta_A and the R moving column by delta_B,
leaving all six gadget columns fixed. Contacts remain exactly unit. Every
gadget lower pair is in its original good state; cross pairs involving the
bottom columns have positive limiting slack except their already preserved
rungs. The same full upper proof applies and both actual diameter pairs
strictly shorten. For sufficiently small t the longest new pair is the old
R pair, with the squared diameter in Statement SR. The finite certificate
checks every pair and verifies that it is indeed the new maximum.

Each of the six gadget moving columns is a contact component without an actual
diameter endpoint. Summing its KKT equilibrium gives zero diameter resultant
but a nonzero contact resultant unless the total weight of its three rungs
vanishes. With nonnegative alpha, every one of those rung weights must be zero.
Thus no KKT stress has positive coefficients on every old contact. CA pinpoints
this failure exactly. Moreover a square grid accommodating H+79 labels has
strictly smaller diameter; the finite verifier checks the explicit grid bound.
Neither the source nor its refined endpoint is asserted globally optimal.

## 5. Verification and scope

Run with Python and SymPy:

```bash
python3 research/verify_target_c_source_realized_owner_sink_2026_10_10.py \
  --heights 30 31 100 --symbolic-limit
```

The committed output is
`research/certificates/target_c_source_realized_owner_sink_2026_10_10.jsonl`.
It certifies 29,430, 29,975, and 79,655 full pair/state checks, totaling 139,060,
including the refined endpoint. Contact equalities are verified symbolically;
all strict signs use exact rational square-root enclosures with 120 binary
fractional bits. Floor choices use integer/rational arithmetic. No floating
point decision is used. The symbolic limit computation checks 5,762
noncontact pairs, of which 5,751 have strict limiting slack and eleven have
the displayed exact leading terms.

The relevant existing `verify_target_c_hub_owner_systems_2026_10_06.py` and
`verify_near_unit_face_conflicts_2026_10_01.py` passed. The hub checker reports
14,182 tree-bank, 110,887 Horn/pinning, and 72 binary-packet checks.
`python3 tools/check_theorem_state.py`, Ruff, and `git diff --check` passed.
Main was refreshed before submission and remained at the starting SHA; PR #947
was still open. No canonical dependency or theorem-state claim was changed.

The numerical exploration preceded the certificate and is not proof evidence.
There is no independent mathematical audit of CA, SG, RM, or SR yet. Repository
checks test bookkeeping and executable contracts, not the missing C-II theorem.

## 6. Failed attacks and exact limits

- **Owner-level monotone potential:** equal-displacement implications increase
  a source-coordinate projection, but contraction can identify separated
  source components. The canonical owner-cycle regression already rejects
  forgetting those identifications. SR adds an actual connected O–O source,
  upper safety, and an explicit refinement endpoint. It does not supersede the
  narrower historical regression.
- **Common-angle pair reduction:** already canonical in Audit.151 and the
  amplitude obstruction in Audit.97. Re-deriving it adds no endpoint.
- **Topological equalizer/parity:** source-local contact regularity does not
  give a compact globally regular quotient without singular or boundary
  strata. Reflection can also supply a congruent second realization. No
  global degree argument or continuation endpoint is claimed.
- **Automatic refinement feasibility:** false on an old diameter joining
  repeated components, as the exact two-singleton identity above shows.
- **Weighted work implies maximum descent:** not used. SG gives at least one
  strictly shortened old diameter; the rest and every inactive upper pair
  require explicit checks.

No literature theorem is imported. Differential-topology and disk-rigidity
sources were inspected as leads, and supplied no missing global regularity or
full-source endpoint theorem.

## 7. Frontier effect and next exact obligation

CA removes contact-unloaded components from the canonical acute rigid-owner
model, even before upper safety is assumed. RM gives an upper-safe mixed-component
refinement after at most 2d_H parent deletions. SG makes strict old-diameter gain
automatic for any nonzero selection with a proper nonempty core owner. None
proves that a source supplies such a family or that its lower and upper clauses
have a nonzero model. The canonical state is unchanged.

**Next theorem to pursue:** in every sufficiently large canonical full-core
C-II survivor, extract a subfamily-stable disjoint O–O parent system satisfying
RM's contact, acute-cloud, singleton actual-diameter, and unary hypotheses,
with more than 2d_H nonempty core owners, and prove that the resulting mixed-
component outer-face lower formula has a nonzero model. RM would then give
complete upper safety and SG strict old-diameter gain, hence an actual finite
lexicographic contradiction. This extraction/lower-feasibility theorem is not
proved here. A source-compatible face-coupled replacement remains an alternative
if such an O–O system cannot be extracted; the macroscopic-container branch is
separate and remains open.

**Promotion recommendation:** preserve for independent audit. Do not change
`state_version`, Level I status, or C-II status on this author's proof alone.
