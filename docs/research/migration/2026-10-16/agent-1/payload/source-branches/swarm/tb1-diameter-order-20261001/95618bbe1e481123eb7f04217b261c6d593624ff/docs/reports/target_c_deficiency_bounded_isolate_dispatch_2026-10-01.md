<!-- theorem-state: {"artifact_id":"ART-03E83595338F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — a rooted isolate forest leaves at most d_H upper blockers

`multi-root isolate dispatch -> at most d_H inactive upper-distance exceptions -> common-swap blocker tree has at least r-d_H near-unit labels -> source-level lower-constraint release still required`

**Date:** 2026-10-01  
**Shared starting HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`  
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`  
**State version:** `2026-09-14.audit.51`  
**Mission / branch:** TB1 augmented inactive-system closure; `swarm/tb1-diameter-order-20261001`.  
**Classification:** proved candidate awaiting promotion; conditional actual-train application; exact forest regression. Artifact lifecycle is unreviewed.  
**Level I / C-II:** OPEN / OPEN.

## 1. Finite dispatch theorem, including the forest branch

Use a canonical C-II source A with C=C_* and H=H_*. Write V for its
nonisolated contact core, Z=A\V, B for all actual diameter endpoints,
q=|B|, h=|H|, and d_H=q-h. Let D>=2 and

\[
 L=\sqrt{D^2-1},\qquad \gamma=D-L.
\]

Let a finite core move p->p+v_p have displacement oscillation

\[
 \rho=\max_{p,q\in V}|v_p-v_q|<\gamma.
\]

There is an explicit displacement assignment to **every** isolate, using only
the old diameter-endpoint displacements, and an original inactive-pair set R,
independent of the move, such that

\[
 \boxed{|R|\le d_H,\qquad
 \text{every original nondiameter pair outside R stays strictly below D}.} \tag{1}
\]

Every old contact is affected exactly as in the original core move. Every old
diameter is affected exactly as in that move. No point is removed or added.
The theorem does not assert lower-distance feasibility or unchanged inactive
pairs in R. Unlike the unique-partner cyclic dispatch, it applies when H is a
caterpillar forest as well.

## 2. Build the long-pair forest before choosing the move

Draw T^+ containing all source pairs longer than L. The standalone
[strict near-diameter theorem](target_c_strict_near_diameter_capacity_2026-10-01.md)
gives extreme endpoints, a convex straight-line thrackle, and |E|<=|V| for
every subgraph. H is contained in T^+.

Every T^+ endpoint outside B is a contact isolate: by canonical
[Theorem 6.1](../theory/01-local-structure.md), a nonisolated nondiameter point
is strictly surrounded by contact neighbors, so is not extreme. Actual H
endpoints belong to V by C=C_*, H=H_* and positive source equilibrium.

Let F=T^+\H, retaining its incident vertices, including its B vertices.
Separate the components of F that touch B from those that do not. Let F_B
be the union of the former, and let Z_B be its vertices outside B.
Every z in Z_B has finite F_B distance to B.

For each z, choose one adjacent vertex at distance one less from B. Direct the
chosen edge toward that vertex. These |Z_B| edges form a forest K_B whose
components each have exactly one B root: distances strictly decrease, every
z has exactly one outgoing edge, and every path ends at a root in B.

Set

\[
 R=E(F_B)\setminus E(K_B). \tag{2}
\]

Apply the thrackle edge bound to the subgraph H union F_B on B union Z_B:

\[
 h+|E(F_B)|\le q+|Z_B|.
\]

Since K_B has exactly |Z_B| edges,

\[
 \boxed{|R|=|E(F_B)|-|Z_B|\le q-h=d_H.} \tag{3}
\]

This is the crucial count. Applying the bound to all T^+ at once would add
spurious slack from isolate-only components. The induced subgraph H union F_B
removes that loss without dropping any point from the source motion.

## 3. The explicit full-source assignment

For z in Z_B, let b(z) be its unique root in K_B and put v_z=v_b(z).
Choose one reference b_0 in B and give every other isolate v_b_0. Each
isolate-only F component then translates rigidly. Every edge in K_B receives
equal endpoint displacements, as does every long edge in an isolate-only
component. Therefore every inactive long pair outside R is unchanged.

Every remaining inactive pair outside T^+ has original length at most L.
Every assigned displacement was already in the old core displacement cloud,
so relative displacement is at most rho, and the pair's new length is at most
L+rho<D. This proves (1). Isolates have no old
contacts and no old diameters; the assignment changes neither of those
constraint families beyond the stated core move.

The forest K_B and the exception set R are chosen once, from original source
geometry. The theorem therefore handles any finite displacement cloud, not
only a binary swap. For a binary move v_p=f(p)Delta, rho<=|Delta|. To make
the assignment commute with unions, use 0 as the common displacement of
unattached isolates, or adjoin an empty fixed class when all core points move.
This never increases the binary cloud diameter beyond |Delta|.

### 3.1 Bounded-face following is compatible with the same forest

Suppose additionally that the core displacement is constant on the
boundary of each bounded nonquadrilateral contact face. Give every
isolate inside such a face that boundary displacement, instead of the
reference displacement. Equation (1) and its same fixed exception set
R remain valid. Every pair contained in that bounded face is now
unchanged, including its isolated source population.

Indeed, a point strictly inside a convex bounded contact face is
nonextreme in the source hull. The strict long-pair theorem therefore
excludes every T^+ edge incident with it. It has no forest constraint
to satisfy. Its chosen boundary displacement belongs to the original
core cloud, so every pair still has relative displacement at most rho.
The upper estimate for nonlong pairs is unchanged. Its absence from
C and H also preserves every old active constraint. Unit separation
precludes a distinct source point on the interior of a unit boundary
edge, so no boundary-isolate exception is hidden here.

For a family of complete global stopped O-O cuts, each bounded
nonquadrilateral face is in one layer. No selected train edge can
border that face: such an edge would terminate the train there,
contrary to both of its ends being outer. Its connected contact
boundary consequently crosses no selected cut. Thus face following
commutes with every common-vector union or arbitrary layerwise cloud
move. In the common-swap tree, all bounded nonquadrilateral-face
isolates can be assigned to their boundary's module before any
subset of modules is selected.

By cofaciality, every non-rhombic lower tree label is then in the old
outer contact face. Outer pockets inside the force hull are included
in that face; this is not a claim that every such label is outside
the force hull.

This compatible refinement was checked against the independent
face-following proof on PR #599 at
[`b0578956`](https://github.com/1337isnot1337/e-99/blob/b0578956346fbfcf98e7862c49c83ab105b19efb/docs/reports/target_c_face_following_exterior_cap_blockers_2026-10-01.md)
and the joint localization on PR #600 at
[`c165fee5`](https://github.com/1337isnot1337/e-99/blob/c165fee5c82b4ab17490e42d9fd5b27f77b84864/docs/reports/target_c_joint_swap_horn_and_loaded_defects_2026-10-01.md).
The standalone compatibility proof is above; neither research packet
is promoted by this cross-check. A mixed O-F transposition passes
through its bounded terminal face and need not move that face rigidly,
so this protection cannot be carried into that move without an
additional chamber argument.

## 4. Combine with the common-swap blocker tree

Suppose r disjoint core modules L_1,...,L_r admit the same nonzero swap vector
Delta, with s<=1/(2D), and each individual swap preserves every old contact,
strictly shortens every changed old diameter, and changes at least one diameter.
These are the precise hypotheses of the
[source-anchored blocker-tree theorem](target_c_common_swap_blocker_arborescence_2026-10-01.md).

Enlarge L_i by all z whose root b(z) is in L_i. Put all other isolates in L_0.
When using Section 3.1, also assign each bounded-face isolate to the
module of that face's boundary; it is not incident with T^+ and has
no conflicting root assignment. Put only the remaining isolates in L_0.
The enlarged sets are disjoint and use the same displacement. Thus every
nonempty union still preserves all old contacts and shortens at least one
old diameter, with none increased. By Section 3, any upper-blocker arc is
labelled by a pair in the fixed set R.

The blocker tree has r distinct actual pair labels. At most |R|<=d_H can be
upper blockers, so its near-unit label count satisfies

\[
 \boxed{N_1\ge\max\{0,r-d_H\},\qquad
 1<|xy|\le1+s.} \tag{4}
\]

For D>=2 these edges form a simultaneous planar Gabriel augmentation of the
old contact graph and are cofacial in it. They may involve dispatched isolates.
Their layer labels form a tree toward the fixed **actual source**, not a tree
of imposed positive stresses.

In the cyclic branch d_H=0, (3) forces R empty and gives N_1>=r. In a forest
branch with d_H=o(D) and r>=cD-o(D), the same conclusion holds to first order:

\[
 \boxed{N_1\ge(c-o(1))D.} \tag{5}
\]

This uses d_H alone, not the stronger h=pi D-o(D) hull saturation hypothesis.
The current rooted ledger supplies d_H<=k=o(D) conditionally, but arbitrary
canonical forest sources need not have sublinear d_H.

For a single binary core move, (1) supplies a sharpened alternative: a lower
blocker, or one of at most d_H explicit inactive upper pairs. No linear
population of common-vector swaps is inferred from this statement.

## 5. Forest residue is necessary

There are unit-separated geometric sources with q=3, h=2, d_H=1 and one inactive
long pair between old B vertices. Put a=(0,0), b=(10,0), and rotate
c=(5,5 sqrt(3)) clockwise by angle 2 arctan(t), t=1/10000, about a. Then
|ab|=|ac|=10 and 99<|bc|^2<100. Thus H is the two-edge star at a, while T^+
is the triangle. There are no new long vertices to dispatch: F_B is the
single edge bc, K_B has no edges, and R={bc} has size exactly d_H.

With C_t=(1-t^2)/(1+t^2), S_t=2t/(1+t^2),

\[
 |bc|^2=200-100C_t-100\sqrt3 S_t.
\]

The exact inequalities 1<sqrt(3)<2 certify the displayed interval using
rational arithmetic; C_t^2+S_t^2=1 certifies the two radii. This is a
geometric sharpness regression, not a canonical-source or global-optimality
certificate. It prohibits replacing '|R|<=d_H' with 'R empty' for every
forest by an isolate-only assignment.

## 6. Durable synthesis and exact proof dependencies

This generalization followed checking
[PR #600](https://github.com/1337isnot1337/e-99/pull/600), commit
`eddd8826f23776ab44825fa25183effb23e7a7b6`, whose cyclic unique-partner dispatch
is rederived as the d_H=0 specialization. The new multi-root construction and
subgraph count above replace unique-partner classification in the forest branch.
No Woodall classification beyond the canonical definition of d_H is needed
for (1)–(4); the convex thrackle bound is proved in the first report.

Canonical premises: contact-minimal local trapping (shared Theorem 6.1), C-I
normalization, and actual-source core conventions. New unpromoted premises:
the standalone strict-long theorem and the common-vector blocker-tree candidate.
Actual-train application additionally uses the unpromoted October 1 block
transposition and its witness-cell hypotheses. The whole extraction ancestry
is not promoted here.

The [exact verifier](../../research/verify_strict_near_diameter_capacity_2026_10_01.py)
checks abstract multi-root forests and every binary root assignment for selected
finite graph sizes, as well as the exact forest residue. These checks encode
the graph edge budget, not a geometric thrackle or a canonical/global source.
The analytic proof supplies those hypotheses and the universal conclusion.

The remaining closing problem is now the lower-constraint tree, with at most
d_H upper exceptions for arbitrary small-oscillation finite core moves. Its strict near-unit edges
have no asserted KKT multipliers; no exact triangle or finite release is
proved. Common-vector extraction, TWO-SIGN, exact-phase, split-star O-O,
inactive-interface, macroscopic-container and other full-core regimes remain
explicit. C-II and Level I are not settled; canonical state is unchanged.
