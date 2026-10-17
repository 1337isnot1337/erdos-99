> Generated reading edition · [exact source](../../../docs/reports/target_c_convex_shared_witness_outer_occurrences_2026-10-02.md) · source SHA-256 `825ad8d18fbf9a917c67a55e3012e66a4bbd4839e27b0ddfc6cfda72d4ca31f9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C57607D612D4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: convex shared-witness paths consume outer-walk occurrences

`shared singleton witnesses -> strictly convex source paths and distinct exterior
incidences -> canonical outer-walk excess x_B=b-q -> a source-level multiplicity
bound; a finite release of the remaining exterior sites is still required`

**Date:** 2026-10-02. **Starting branch HEAD:**
`3625ec5e8bbf9e1530377528714ef0ed351cd8db`.
**Starting main:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.
**Inspected current main:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
The state files and Target C route did not change between these main commits.
**State version:** `2026-09-14.audit.51`.
**Branch:** `swarm/root/c2-gap-cut-20261001`.
**Mission:** release or charge the nonconstant-phase exterior source obstruction.
**Classification:** proved candidates awaiting promotion; conditional stopped-train
and near-disk applications; exact regression. Artifact lifecycle unreviewed.
**Level I OPEN; C-I CLOSED; C-II OPEN.**

## 1. Dependencies, with scopes retained

The exact disjoint-move source setup and phase-separation theorem are proved in
[the preceding report](target_c_aligned_swap_horn_and_axial_bracket_2026-10-01.md),
Theorems 1--5. The earlier source compiler retains every source pair.

Canonical inputs for the source consequence are contact-minimal/diameter-pair-
minimal normalization, full positive active support, and
[local trapping](../theory/01-local-structure.md): every nonisolated source point
outside the diameter endpoint set B is strictly surrounded. Canonical
[Section 67](../targets/target-c/67-rhombus-population-transport-audit.md) supplies
the connected positive-contact core G and the occurrence-counted outer length b.
Canonical [Section 85](../targets/target-c/85-train-boundary-interface-currency-audit.md)
supplies

$$
 b=q+x_B,\quad q-x_B=Q_{\rm global}+2\kappa,
 \quad\kappa=d_H+s_Z,\quad q=|B|.                 \tag{1}
$$

Q_global is the full contact-face deficiency. It is not the defect of one induced
harmonic-cell graph. No small bound on x_B or Q_global is inferred here.

The source-pair exterior localization uses the explicitly unpromoted, inspected
Theorem 8 of
[PR #600 at 9ddd9538](https://github.com/1337isnot1337/e-99/blob/9ddd9538/docs/reports/target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md).
That proof uses actual global O--O stopped train cutsets, a connected contact core,
and convex unit-edge face boundaries. Its finite face-following construction is
checked in Section 2 below; it is not imported for arbitrary local cuts.

The near-disk consequence adds the explicit hypotheses D^-1 conv B converging,
after translations, to the radius-1/2 disk and E=per(conv B)-q=o(D). These are
the unpromoted rooted-endpoint focus, not hypotheses on every C-II minimizer.
The relevant angular-cap and isolate bounds in
[PR #600's loaded-pair report at 9ddd9538](https://github.com/1337isnot1337/e-99/blob/9ddd9538/docs/reports/target_c_loaded_near_unit_hull_adjacency_2026-10-01.md)
were inspected; the direction-window proof needed for internal loaded vertices
is reproduced in Section 6. This packet does not import its other conclusions.

## 2. Full-source setup and exterior localization

Keep k' coherent ONE-SIGN swaps after the fixed upper forest/freezing. Their
moving sets are disjoint; all old contacts stay unit for every binary assignment;
every nonempty assignment shortens an old diameter; all inactive upper distances
stay strict. Let Delta_i=s_i Jm_i, with one coherent ordinary orientation and
s_i=2 sin(epsilon_i/2). Their lifted boundary intervals I_i lie in one phase
window J of width W<=1/10. Assume s_i<=s<=1/10 and 2s<gamma_D.

Let U consist of the old noncontact source pairs that block two different
singleton moves. Each such pair has endpoints in those two moving sets. The
preceding Theorem 5 gives its direction strictly between disjoint I_i,I_j,
length 1<R<=1+s, and gap R-1<2s sin W. U is a linear forest on source points.

For the actual stopped-train specialization use the same face-following dispatch
as follows. A selected O--O stopped train uses no boundary edge of a bounded
nonrhombic face. Every contact edge on that boundary consequently has equal cut
indicators at its ends. The entire boundary has one motion owner. Assign every
isolate strictly inside that face the same owner. Such an isolate is nonextreme,
so no strict-long source pair is incident to it; changing its ownership preserves
the upper forest and its exception set. Remaining short upper constraints use
the simultaneous bound L_D+2s<D. Every short lower pair involving that isolate
lies in the same face and has unchanged relative displacement.

A strict unit rhombus has no interior source point. The selected phase window
has width less than pi/3, while the two projective directions of a strict source
rhombus differ by more than pi/3. At most one selected shore train crosses it.
If its two relatively moving ownership classes were distinct nonzero variables,
some old unit side would join them. Preserving that side under 00,10,01,11 would
give Delta_i dot Delta_j=0 by taking differences of squared lengths. The coherent
acute displacement cone excludes this. Thus a moving rhombus diagonal has one
moving owner and one fixed owner, and cannot belong to U.

All short source pairs draw without crossing old contacts: crossing two segments
shorter than sqrt(2) gives a quadrilateral angle of at least pi/2 and an opposite
diagonal of length at least sqrt(2). A short segment also cannot pass through a
third source point. It therefore lies in one face of G. The preceding rigid-face
and rhombus arguments show that every U segment lies in the old outer face.

No source point is deleted. A moving isolate in that outer face is incident to
the original strict-long graph, except for a loaded isolate if one were allowed.
Full-support source equilibrium actually excludes a loaded isolate: at an
extreme source point all vectors to its diameter partners lie in one open
half-plane, and a strictly positive combination cannot be zero without contact
forces. Thus B is in the positive-contact core. Every exterior moving isolate
counted below is an extreme vertex outside B. Fixed exterior isolates may still
give unary constraints; this section does not remove them.

## 3. Every shared-witness path is strictly convex and phase ordered

Orient each U edge forward in a common direction u inside J. Let p_0,...,p_l
be one component in that order, let theta_j be the phase of p_{j+1}-p_j, and
let I(v) denote the phase interval of the owner of v. The singleton inequalities
give exactly

$$
 \sup I(p_j)<\theta_j<\inf I(p_{j+1}).              \tag{2}
$$

Consequently at every internal vertex

$$
 \theta_{j-1}<\inf I(p_j)<\sup I(p_j)<\theta_j.     \tag{3}
$$

**Theorem 1.** A U component has strictly increasing edge phases, hence is a
strictly convex polygonal arc. Its owners are all distinct, their phase intervals
are strictly ordered and pairwise disjoint, and

$$
 \sum_{j=0}^l\varepsilon_{\operatorname{owner}(p_j)}\le W.
\tag{4}
$$

An opposite common swap orientation reverses the inequalities and the sign of
turning; the unoriented convex-arc conclusion and distinctness remain.

**Proof.** Apply the exact two-singleton inequality to each edge, orienting r
forward in u. In the Delta=+Jm convention the owner phases are ordered as in
(2). Chaining those strict inequalities gives (3), disjointness of all successive
owner intervals, and their transitive strict ordering. No owner can repeat.
Their disjoint intervals lie inside J, proving (4). Equation (3) makes every
turn have one strict sign. QED.

Let L be the Euclidean length of the arc. Projection along u gives

$$
 l<L\le\frac D{\cos W},\qquad
 \operatorname{width}_{Ju}(\text{arc})\le D\tan W,
\tag{5}
$$

and, writing c for its endpoint chord length,

$$
 0\le L-c\le\frac{D(1-\cos W)}{\cos W},\qquad
 \sum_{e\in\text{arc}}(|e|-1)<2Ds\tan W.          \tag{6}
$$

Indeed each edge has positive u projection at least its length times cos W;
the endpoint projection is at most D. The normal variation and chord estimates
follow from the same projection bounds. The last estimate sums the exact gap
bound R-1<2s sin W over fewer than D/cos W edges.

For W=O(D^-1), these arcs have normal width O(1) and detour O(D^-1). For
s=O(D^-2), their total excess above unit spacing is O(D^-2). These metric facts
do not integrate a contact-preserving contraction.

## 4. One shared-witness incidence per unloaded outer occurrence

Use a common unit axis u such that every direction in J is within Euclidean
distance 1/10 of u. Let w=Ju. At a source point p incident to two U edges, their
outgoing directions d_+,d_- are within 1/10 of u,-u, respectively, and their
lengths R_+,R_- are at most 11/10.

For every old unit-contact vector a at p, unit separation from the two U
neighbors gives

$$
 a\cdot d_+\le R_+/2,\qquad a\cdot d_-\le R_-/2.
$$

Thus

$$
 \boxed{|a\cdot u|\le\frac{13}{20}.}              \tag{7}
$$

All unit-contact directions lie in the two disjoint arcs centered at w,-w
with |a dot u|<=13/20. Each such arc has width 2 arcsin(13/20)<pi. The two
inactive rays lie in the opposite complementary arcs around u,-u, because
their absolute u projections are at least 1-(1/10)^2/2=199/200>13/20.

**Lemma 2.** If p is strictly surrounded by its old contacts, the two U rays
cannot lie in the same contact-free angular sector between consecutive old
contact rays.

**Proof.** A connected angular sector containing both complementary horizontal
rays must contain one whole allowed vertical contact arc. That arc can contain
no contact ray. All contacts would therefore lie in the other vertical arc,
whose aperture is less than pi, and could not positively span the plane.
This contradicts strict surrounding. QED.

A U ray cannot coincide with an old unit contact ray: the third source point at
distance one on that ray would be less than one from its U neighbor at distance
R<2. Thus every U incidence lies strictly inside a face sector.

Let mu_out(p) count occurrences of p on the old outer contact walk, with
multiplicity. Each occurrence is one exterior angular sector. By Lemma 2 and
d_U(p)<=2,

$$
 \boxed{d_U(p)\le\mu_{out}(p)\quad(p\in V(G)\setminus B).}
\tag{8}
$$

In particular an unloaded internal U vertex occurs at least twice on the outer
walk. It is a contact articulation vertex: in a connected plane graph, distinct
occurrences in one facial walk require a separation at that vertex. This is
not an assertion that all outer-walk vertices are distinct or that U is a contact
path. Loaded vertices need not be strictly surrounded and are excluded from (8).

## 5. Exact canonical multiplicity charge

Let z be the number of moving exterior contact isolates. Let l_B and i_B count
loaded vertices of U-degree one and two, respectively. All loaded vertices are
core vertices incident to the old outer face, and occur at least once there.
Therefore

$$
 \sum_{p\in V(G)\setminus B}\mu_{out}(p)
 = b-\sum_{b\in B}\mu_{out}(b)\le b-q=x_B.
$$

Summing (8), retaining the loaded incidences and at most two incidences per moving
isolate, proves

$$
 \boxed{2|U|\le x_B+l_B+2i_B+2z.}                 \tag{9}
$$

The singleton witness count in the preceding packet satisfies N_1+|U|>=k',
so

$$
 \boxed{N_1\ge k'-\frac{x_B+l_B}{2}-i_B-z.}       \tag{10}
$$

This is an actual source population charge to the canonical outer excess x_B.
It does not suppress loaded endpoint occurrences or isolate coordinates.
Using (1), x_B=q-Q_global-2kappa. Neither Q_global=o(D) nor x_B=o(D) follows
from the local harmonic-cell defect. The exact remaining residues in (9) are
loaded path endpoints, internal loaded points, and moving exterior isolates.

## 6. Internal loaded vertices at a conditional near-disk endpoint

Suppose D^-1 conv B converges after translations to the radius-1/2 disk and
W=O(D^-1). First exclude internal loaded vertices adjacent to a moving exterior
isolate; there are at most 2z of them. Every remaining U neighbor lies in the
contact core. Local trapping puts conv V(G)=conv B, so every outward support
normal n at the loaded vertex satisfies n dot d_+<=0 and n dot d_-<=0.
Using a support normal of conv B on an exterior isolate would be invalid;
these incidences are kept separately. The two near-opposite directions
then force |n dot u|<=1/10 at the fixed-scale level, and, more precisely, force
the entire normal cone into one window of width O(W) about w or -w.
Both adjacent loaded-hull side normals lie in that window.

Here is the needed small-window count. Let delta_D be the normalized Hausdorff
error from the disk, and let eta_D tend to zero. A normalized hull-side endpoint
whose outward side normal is within eta_D of n_0 has

$$
 p\cdot n_0\ge\frac12-\delta_D-(\frac12+\delta_D)\eta_D.
$$

Its tangential coordinate is O(sqrt(delta_D+eta_D)). Side normals in the window
occur on a contiguous convex boundary arc. The projection of each oriented side
onto the reference tangent is at least cos(eta_D) times its length, so the total
original arc length is O(D sqrt(delta_D+eta_D))=o(D). Every loaded hull side
has length at least one. Assign each internal loaded vertex its preceding hull
side; this is injective and lies in the same pair of small direction windows.
It follows that the number i_B^good of retained internal loaded vertices is

$$
 \boxed{i_B^{good}=o(D),\qquad i_B\le i_B^{good}+2z.} \tag{11}
$$

This includes loaded internal vertices whose two U neighbors are unloaded, so it
is not just a count of loaded-loaded near-unit edges.

For z, the inspected loaded-hull cap argument gives the explicit bound
z<=24E/sqrt(39) when D>=6, 1+E<=D/4, and E=per(conv B)-q. Its hypotheses
hold eventually if E=o(D). Briefly, every source-hull cap beyond a loaded side
of length ell<=1+E has two actual diameter-disk tangent bounds. A nonempty cap
requires ell>3/2; its outer arc is at most 8ell/sqrt(39). Each added extreme
source vertex spends a unit of arc length, and ell<=3(ell-1) on a nonempty cap.
Summing the disjoint caps gives the stated bound. Moving exterior isolates are
extreme, so z=o(D) and consequently i_B=o(D). This argument does not count an
arbitrary exterior cloud.

Let c_U be the number of nontrivial U path components. Since l_B<=2c_U, (9)
becomes

$$
 \boxed{|U|\le\frac{x_B}{2}+c_U+o(D).}            \tag{12}
$$

No sublinear component bound is claimed. A matching of many separate unloaded
outer-pocket witnesses remains possible under these estimates. The phase widths
on distinct components can overlap, so (4) cannot be summed globally without
a new source compatibility theorem.

## 7. Failed closure and exact remaining obligation

The attempted inference "a convex, almost-unit inactive path can be contracted
while preserving the source contacts and fixing the other source vertices" is
false even if both ends are strictly trapped. The verifier gives an exact
twelve-point regression.

Put t=1/1000, let cm,hm be the rational unit-circle parameters at t, and let
s=4t^2/(1+t^4). Let cr,sr be those unit-circle parameters at t^4. Put
c=120/241, h=209/241, and R=1+4h sr. Take p=0,q=(R,0). The three unit contacts
at p have vectors

$$
 a_+=(-c\,cr+h\,sr,h\,cr+c\,sr),\quad
 a_-=(c\,cr+h\,sr,-h\,cr+c\,sr),\quad (-1,0),
$$

and those at q have vectors

$$
 b_+=(-c\,cr-h\,sr,h\,cr-c\,sr),\quad
 b_-=(c\,cr-h\,sr,-h\,cr-c\,sr),\quad (1,0).
$$

All six neighbors are separate source points. At p the positive weights
(h cr-c sr,h cr+c sr,2cr sr) give exact contact balance; at q interchange the
first two weights. Both points are strictly trapped. Add remote actual
diameters (-6,-8)--(6,8) and (6,-8)--(-6,8). Assign p and its contact star plus
(-6,-8) to Delta_1=(s hm,s cm), and q and its star plus (6,-8) to
Delta_2=(-s hm,s cm). These are exact unit-direction chords in separated
phase intervals. Their private diameters strictly shorten; all old contacts
are preserved for every choice. The only lower blockers are pq, the pair
p+a_+ to q+b_+, and the pair p+a_- to q+b_-. Each forbids 10,01,11.
All 66 source pairs and local binary states are checked rationally.

The inactive edges form three separate one-edge source paths. The axial anchors
(-1,0),(R+1,0) are not in U. If they stay fixed and their old unit bars to p',q'
stay unit, then p'_x<=0 and q'_x>=R. Hence |p'-q'|>=R>1 under **every finite
move**, even when the other four U vertices are allowed to move. Snapping the
inactive path to unit length is impossible with these constraints.

The source lacks canonical global normal form and full KKT: its loaded points
are contact-isolated and its two contact stars are disconnected. A twelve-point
unit line has diameter eleven, below twenty, so it is not a Level I
counterexample. Opening the axial contacts or moving their source branches is
outside the rejected fixed-rest/contact-preserving claim and remains a possible
closing route. Formula (6) controls metric slack but does not supply bar
compatibility. The canonical source needs a new branch-motion argument.

The more specific closing target is now: use actual contact-block geometry and
full positive KKT to release a repeated exterior sector, or pay the number of
separate outer-pocket components by the source defect ledger strongly enough to
force a surviving Horn seed. The canonical identity (1) alone does not do this.

Exact phase, TWO-SIGN, split-star O--O, inactive-interface, macroscopic inactive
containers/exterior caps, and full-core branches outside this extraction remain.
This report does not replace the all-minimizers quantifiers with a normal-form
subclass conclusion.

## 8. Certificate scope

The [companion exact verifier](../../../docs/research/migration/2026-10-16/shards/01/support/research/verify_convex_shared_witness_outer_occurrences.py)
checks a strictly convex two-edge shared-witness path with three ordered
unit-chord moves. Its internal vertex has three exact
unit contacts and a positive local contact balance. The two exterior inactive
rays lie in different outer sectors, so it is a regression against dropping
repeated occurrences. A remote extension gives private old diameters and exact
all-source distance checks. It is not a global minimizer or a full-source KKT
framework. The source-isolated loaded points, the disconnected contact core,
and the other nontrapped contact vertices are explicit omissions. Its contact
star has three outer occurrences at the central vertex. No canonical identity
such as b=q+x_B is assigned to that regression.

The proofs above, rather than finite sample survival, establish the real-coordinate
lemmas. The verifier does not establish the near-disk hypotheses, actual stopped
train cutsets, a source-preserving path contraction, or C-II/Level I closure.
