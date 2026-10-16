# Target C-II: narrow-window O--O laminarity and owner-region budget

Date: 2026-10-06.
Authority: main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1, state 2026-10-05.audit.62.
Status: proof-only Target C reduction. C-II and Level I remain open.

## Scope

Use the audit.61 O--O finite-motion system. Let \(\mathcal T\) be a finite family
of selected global stopped outer-to-outer trains and put
\[
T_{\rm OO}=|\mathcal T|.
\]
Assume their projective contact directions lie in one projective interval of width
strictly below \(\pi/3\). The selected trains carry their audited O--O shore
splits. For a non-singleton train this is the Jordan shore split of its midpoint
centerline; for an O--O singleton it is the audited outer-face bridge split.

The point of this note is that pairwise laminarity of these cuts is a consequence
of the canonical train geometry. It need not be added as a hypothesis.

## 1. Narrow-window O--O trains admit pairwise disjoint crosscuts

### 1.1 Non-singleton trains

Canonical stopped-train geometry gives two facts.

1. A non-singleton O--O train has a proper simple midpoint-centerline crosscut of
   the outer occurrence disk.
2. Two distinct complete train centerlines can meet only through a
   strict-rhombus train crossing. At such a crossing the projective contact
   directions have separation strictly greater than \(\pi/3\).

The second statement is the finite geometry behind canonical Section 142.2:
the train-crossing graph is simple and every crossing has projective separation
in \((\pi/3,\pi/2]\).

Take distinct non-singleton \(\tau,\sigma\in\mathcal T\). Their projective
directions lie in one interval of width \(<\pi/3\), so their circular
projective separation is \(<\pi/3\). They therefore cannot cross in a strict
rhombus. Since a distinct pair of train centerlines has no other kind of
intersection, their proper crosscuts are disjoint.

Thus all selected non-singleton O--O centerlines are pairwise disjoint.

### 1.2 Singleton O--O bridges

A singleton O--O train is a contact bridge whose two facial occurrences are on
the outer face. Its one contact edge is not incident with a strict rhombus:
otherwise the auxiliary stopped-train graph would link that contact edge to the
opposite edge of the rhombus and the train would not be a singleton.

Work in the standard occurrence-disk regularization of the plane contact graph.
For a singleton bridge \(e\), take a sufficiently small neighborhood of the
relative interior of \(e\) and draw a transverse dual arc \(\gamma_e\) through
the interior of \(e\), joining the two boundary copies of the two outer facial
occurrences of \(e\). This is a proper crosscut. Removing it separates the
same two core vertex shores as deleting the bridge \(e\), so \(\gamma_e\)
represents exactly the audited singleton bridge shore split.

The source is finite. Distinct contact edges have disjoint relative interiors,
and a non-singleton train centerline meets a contact edge only at a midpoint of
an edge belonging to that train. Complete stopped trains partition the contact
edges. Hence the bridge neighborhoods can be chosen so small that:

- distinct singleton dual arcs are pairwise disjoint;
- every singleton dual arc is disjoint from every selected non-singleton
  midpoint crosscut.

Consequently every train in \(\mathcal T\), singleton or not, has a proper
crosscut representative for its audited shore split, and these
\(T_{\rm OO}\) representatives are pairwise disjoint.

This is only a laminarity statement. It does not say their complement dual is a
path. In general the complement dual can branch.

## 2. Complement-dual tree and exact owner support

A family of \(T\) pairwise disjoint proper crosscuts of a disk has exactly
\(T+1\) complementary regions.

Proof: induct on \(T\). The empty family leaves one region. A new proper
crosscut, disjoint from the previous family, lies in the closure of one old
region and splits exactly that region into two. Thus every new crosscut raises
the region count by one.

Equivalently, the region/crosscut incidence dual has \(T+1\) vertices and
\(T\) edges and is a tree. This is the corrected dual-tree statement; no
linear-chain claim is used.

Root this tree at the reference region \(R_0\). Orient every train shore so
that \(R_0\) lies on its zero side. Let \(\Delta_\tau\) be the translation
increment assigned to the opposite shore. Then for every region \(R\),
\[
\boxed{
X_R=\sum_{\tau\in P(R_0,R)}\Delta_\tau,
}
\tag{1}
\]
where \(P(R_0,R)\) is the unique dual-tree path from the reference region to
\(R\).

Indeed a train separates \(R\) from \(R_0\) exactly when its dual edge lies
on that path. This is the exact shore-indicator formula specialized to the
laminar family.

More generally, for any two regions \(R,S\),
\[
\boxed{
X_R-X_S
=
\sum_{\tau\in P(R,S)}\varepsilon_\tau\Delta_\tau,
\qquad
\varepsilon_\tau\in\{+1,-1\}.
}
\tag{2}
\]
No selected train appears twice. Hence every inter-owner relative translation
is supported on one simple path of the complement-dual tree, rather than on an
arbitrary subset of selected trains.

Equation (2) is a structural reduction for the remaining outer-face
implication problem. It is weaker than a path-order theorem because the dual
tree may branch, but stronger than the unrestricted owner-contraction model
that permits arbitrary cut supports.

## 3. Moving-owner bound

Owner labels are constant on complementary regions: all vertices in one
region have the same selected-shore indicator vector, hence the same
translation. The reference region has translation zero. Every nonzero moving
core owner contains at least one core region; isolate dispatch assigns an
isolate only to an existing owner or to the fixed class.

Let \(k\) be the number of distinct nonzero moving owners. Choose one core
region carrying each moving-owner label. Distinct labels give distinct chosen
regions and none is \(R_0\). Since there are exactly
\(T_{\rm OO}+1\) regions,
\[
\boxed{k\le T_{\rm OO}.}
\tag{3}
\]

Thus unary strict-rhombus roots, outer unary clauses, implication tails,
loaded owners, and unloaded owners in this narrow-window system all spend one
common train/region bank.

Each selected O--O train has two terminal outer-face occurrences. For a
singleton bridge these are the two facial occurrences of its one bridge edge.
Different complete trains have different terminal occurrences because the
stopped-train decomposition partitions contact edges. If \(b\) is the
occurrence-counted outer contact-walk length,
\[
2T_{\rm OO}\le b.
\tag{4}
\]
Therefore
\[
\boxed{k\le T_{\rm OO}\le b/2.}
\tag{5}
\]

## 4. Original proposal family

The canonical long-pair dispatch can remove at most \(2d_H\) proposals
through the fixed inactive-upper exception set before the lower-only owner
problem. If the original pairwise-disjoint proposal family has size \(r\)
and the surviving narrow-window system has \(k\) owners, then
\[
r\le k+2d_H.
\]
Together with (5),
\[
\boxed{
r\le T_{\rm OO}+2d_H\le b/2+2d_H.
}
\tag{6}
\]

This improves the earlier conditional outer-capacity estimate
\[
r\le b+Z_{\rm out}+2d_H
\]
within the explicit narrow-window O--O regime.

## 5. Sharpness and scope

The coefficient one in (3) is sharp at the cut-topology level: \(T\)
parallel crosscuts give \(T+1\) regions, and the \(T\) nonreference regions
may carry distinct nonzero labels.

The width hypothesis is doing real work. If selected complete trains can
cross, two transverse proper crosscuts already create four regions, so three
nonreference region labels can arise from only two cuts. The conclusion
\(k\le T\) is therefore not asserted for arbitrary crossing multishears.

The proof also does not assert that the complement dual is a path, that all
owner labels are distinct region by region, or that the tree-path support in
(2) is enough by itself to make the owner implication graph acyclic.

## 6. Remaining Target C obligation

The narrow-window owner system now has two exact restrictions simultaneously:

1. its complete moving-owner population obeys
   \[
   k\le T_{\rm OO}\le b/2;
   \]
2. every relative owner displacement is supported on one simple path of the
   complement-dual tree.

The next closing step should use this tree-path support together with the
actual loaded-hull cyclic order, audit.53 loaded returns, or the audit.56
active-diameter coordinates. A useful target is to show that an unsatisfiable
outer-face implication certificate forces more distinct terminal/tree-edge
currency than the available \(T_{\rm OO}\), rather than merely counting
owners.

The crossing-multishear and macroscopic inactive-container branches remain
separate. C-II and Level I remain open.

All statements above are analytic finite proofs. No computation, verifier, CI
output, or unexecuted verifier is a premise.

## 7. Near-unit witnesses have non-singleton dual-tree bandwidth at most fourteen

The tree normal form above gives a stronger geometric restriction on the remaining
lower clauses. It generalizes the older path-only bandwidth argument to the
branching complement-dual tree.

Let \(\mathcal T_+\subseteq\mathcal T\) be the non-singleton selected O--O
trains. Delete the singleton bridge cuts and form the complement dual tree
\(\mathscr D_+\) of the remaining pairwise-disjoint midpoint crosscuts. For source
points \(x,y\), let \(d_+(x,y)\) be the number of non-singleton selected cuts
separating them, equivalently the distance between their regions in
\(\mathscr D_+\).

For any source points \(x,y\), with \(L=|x-y|\),
\[
\boxed{d_+(x,y)<4L+2\pi\sqrt3.}
\tag{7}
\]

Indeed, every non-singleton selected crosscut separating \(x\) from \(y\) is
met by the straight segment \(xy\). Choose one strict unit rhombus of that
train whose closure meets the segment. The chosen rhombi are distinct: if one
strict rhombus belonged to two selected trains, those trains would cross there,
which is impossible in the present projective window of width \(<\pi/3\).

A strict unit rhombus with angle \(\pi/3<\theta<2\pi/3\) has area
\(\sin\theta>\sqrt3/2\) and diameter strictly below \(\sqrt3\). Hence
every chosen rhombus lies in the closed \(\sqrt3\)-tube around \(xy\).
That tube has area \(2\sqrt3L+3\pi\). Distinct contact faces have disjoint
interiors, so
\[
d_+(x,y)\frac{\sqrt3}{2}<2\sqrt3L+3\pi,
\]
which proves (7).

Now let the translation-cloud diameter satisfy the audit.61 bound
\[
s<D-\sqrt{D^2-1}.
\]
If a previously strict source pair reaches the lower boundary in any selected
state, then
\[
1<|x-y|\le1+s.
\]
For \(D\ge20\),
\[
s<D-\sqrt{D^2-1}
=\frac1{D+\sqrt{D^2-1}}
<\frac1{39}.
\]
Using the elementary bounds \(\pi<22/7\) and \(\sqrt3<26/15\), (7) gives
\[
d_+(x,y)
<
4+\frac4{39}+\frac{1144}{105}
=
\frac{20472}{1365}
<15.
\]
Therefore
\[
\boxed{d_+(x,y)\le14.}
\tag{8}
\]

Thus every physical lower-clause witness in the sufficiently-large
narrow-window O--O system spans at most fourteen non-singleton selected train
cuts. This covers implication and incompatibility witnesses, and unary lower
witnesses whenever they arise from a previously strict source pair driven to
distance at most one. This is a statement on actual witness endpoints, not on
owner labels, so it does not reverse the canonical owner-contraction
regression.

Return to the full dual tree \(\mathscr D\), including singleton O--O bridge
cuts. Give a dual edge weight one if it is non-singleton and zero if it is a
singleton bridge. Contracting all zero-weight edges gives \(\mathscr D_+\).
Hence every such lower witness obeys
\[
\boxed{\operatorname{dist}_w(R_x,R_y)\le14.}
\tag{9}
\]
If the ordinary full-tree path between the endpoint regions has \(m\) edges
and contains \(s_0\) singleton edges, then
\[
m-s_0\le14,
\qquad
\boxed{s_0\ge(m-14)_+.}
\tag{10}
\]

Branching alone therefore does not create long-range near-unit clauses. Every
clause that is long-range in the full region tree must spend all range beyond
fourteen through singleton bridge cuts. In a singleton-free selected system,
every lower clause has ordinary dual-tree distance at most fourteen.

The older proof-only note
`research/target_c_high_t_tb1_short_blocker_bandwidth_t18687_2026-09-17.md`
obtained the same constant fourteen only when the O--O region dual was a path.
Equations (7)--(10) rederive the estimate in the current audit.62 geometry and
remove that path assumption.

## 8. Updated remaining Target C obligation

The narrow-window lower system now has three simultaneous exact restrictions:
\[
k\le T_{\rm OO}\le b/2,
\]
every owner relative translation is supported on one simple dual-tree path,
and every lower-clause witness traverses at most fourteen non-singleton edges
of that path.

The unresolved long-range part of an implication certificate is therefore
forced onto singleton bridge cuts. The next composition is with canonical
`C-GOOD-HULL-SINGLETON-CHARGE` and `C-FULL-FLOWER-K-PAYMENT`, while the
remaining radius-14 packets should be combined with audit.62 loaded
degree-\(\le2\) near-unit geometry and audit.53 loaded-return capacity.

This does not prove owner-graph acyclicity: owner labels may repeat across
regions, singleton chains are not bounded here, and a radius-14 graph on a
branching tree can contain SCCs. C-II and Level I remain open.

The new Sections 7--8 are analytic finite proofs. No computation, verifier,
CI output, or numerical experiment is a proof premise.
