<!-- theorem-state: {"artifact_id":"ART-09F6D76BBF3C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase couples to the opposite O--O shore

Date: 2026-10-01  
Starting main: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec  
Branch: swarm/sol/transverse-staircase-support-20261001  
Status: unreviewed proved candidate under the explicitly listed October 1 hypotheses; C-II and Level I remain open.

~~~text
threshold paired staircase + complete O--O four-host order
  -> interior staircase bundles are full-support on the transverse shore
  -> exact two-sheet lift over the interior terminal subtree
  -> either linear transverse extreme-layer populations or a linear boundary-star run
  -> target: exclude the surviving extreme-fiber / boundary-run source geometry
  -> strict same-cardinality sub-D competitor or exact unit triangle
~~~

This report supplies a direct coupling between the threshold staircase on one retained
shore and the opposite complete O--O shore. It does not promote any October 1
proof-only input and does not claim C-II closure.

## 1. Inputs and notation

Let

\[
\mathcal A=\{\tau_1,\ldots,\tau_m\},\qquad
\mathcal B=\{\sigma_1,\ldots,\sigma_n\}
\]

be the two shores of the current complete global O--O rectangle. Use the four
boundary host intervals from
target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md, in cyclic order

\[
I_A^+,\ I_B^+,\ I_A^-,\ I_B^-.
\tag{1}
\]

The A-layer map \(\ell_A\) varies through \(0,\ldots,m\) on the two A-host
intervals and is constant at its two extreme values on the B-host intervals.
Symmetrically, \(\ell_B\) varies on the B-host intervals and is constant at
\(0,n\) on the two A-host intervals. The two A-host intervals carry opposite
B-extreme values.

Assume \(\mathcal A\) is in the threshold exact-phase case of
target_c_exact_phase_threshold_paired_staircase_2026-10-01.md.
Thus there is a full-support diameter \(h_0\), parallel to the common A-train
direction, whose endpoints have A-layers \(0,m\). Splitting the convex-hull
boundary at those endpoints gives arcs \(L,U\), both ordered from A-layer \(0\)
to A-layer \(m\).

The simple A-gap graph is the exact staircase tree with cells

\[
C_t=(a_t,b_t),\qquad 0\le a_t<b_t\le m,\qquad t=1,\ldots,m,
\]

starting at \(C_1=(0,m)\), ending at \((r-1,r)\), and taking unit steps

\[
(a,b)\mapsto(a+1,b)\qquad\hbox{or}\qquad(a,b-1).
\tag{2}
\]

Every cell has actual diameter representatives in both physical orientations

\[
L_aU_b,\qquad L_bU_a.
\tag{3}
\]

For the forest statements choose one representative in each orientation over
each cell, as in
target_c_exact_phase_threshold_forest_lift_2026-10-01.md.

All three October 1 reports just named are proof-only/unpromoted at the starting
state. The result below is conditional on their explicit hypotheses. The only
additional canonical input used later is C-WOODALL.

## 2. The two threshold arcs use opposite A-host intervals

### Lemma 1

Every source endpoint of an A-staircase diameter with internal A-layer

\[
0<\ell_A<m
\]

lies on an A-host interval. Moreover the internal-layer points of \(L\) lie on
one A-host interval and the internal-layer points of \(U\) lie on the other.

### Proof

By the four-host description, the B-host intervals have constant A-layer equal
to \(0\) or \(m\). Hence every boundary source point of internal A-layer lies in
\(I_A^+\cup I_A^-\).

The full-support segment \(h_0\) separates the endpoints of every selected
A-crosscut. Therefore each of the two boundary arcs \(L,U\) contains one endpoint
of every selected A-crosscut. The two endpoints of an A-crosscut lie on the two
different A-host intervals. Along both \(L\) and \(U\), the A-layer is
nondecreasing from \(0\) to \(m\).

An arc cannot change from one A-host interval to the other while carrying
internal A-layers. Between the two A-host intervals it traverses a B-host
interval on which the A-layer is already one of the extremes; continuing into
the other A-host would require the opposite traversal of the nested A-layer
order. Equivalently, all ordered A-crosscut endpoint transitions on one of the
two \(0\)-to-\(m\) boundary arcs belong to one host interval. Since each
A-crosscut has one endpoint on each A-host, the two arcs use opposite A-hosts.

Thus all internal A-layers on one of \(L,U\) lie in \(I_A^+\), and all internal
A-layers on the other lie in \(I_A^-\). QED.

## 3. Interior staircase cells are full-span on the opposite shore

For an actual diameter \(h\), let \(t_A(h)\) and \(t_B(h)\) be the numbers of
internal incidence switches on the selected A and B paths, as in the joint
switch-budget theorem.

### Theorem 2 (transverse-support normal form)

For every actual diameter representative over an A-staircase cell \(C=(a,b)\):

1. If
   \[
   0<a<b<m,
   \tag{4}
   \]
   then its two endpoints have B-layers \(0,n\). Hence its B-support is full:
   it crosses every selected B-cut and
   \[
   t_B(h)=0.
   \tag{5}
   \]

2. If \(C\) is proper and touches exactly one A-extreme,
   \[
   a=0<b<m\qquad\hbox{or}\qquad 0<a<b=m,
   \tag{6}
   \]
   then \(t_A(h)=1\), so the joint switch bound
   \[
   t_A(h)+t_B(h)\le2
   \tag{7}
   \]
   gives \(t_B(h)\le1\). Its B-support is therefore empty, full, a prefix, or a
   suffix. It cannot be a proper two-sided B-interval.

3. Only representatives over the full cell \((0,m)\), together with the
   additional parallel full-A diameter \(h_0\), can have two B-switches inside
   this selected threshold system.

### Proof

For (1), both endpoint layers are internal. By Lemma 1 the two physical
orientations in (3) join opposite A-host intervals. The B-layer is constant at
opposite extreme values \(0,n\) on those two A-host intervals. Exact laminar
support on the B path is therefore the full interval.

For (2), a proper A-interval touching one extreme changes incidence at exactly
one internal A-interface, so \(t_A(h)=1\). Equation (7), already proved for every
actual diameter in the complete rectangle, gives \(t_B(h)\le1\). Exact laminar
B-support then has only the four stated possibilities.

For (3), an A-support interval has \(t_A=0\) only when it is empty or full.
Every staircase cell is nonempty, and the unique full staircase cell is
\((0,m)\). The separate threshold diameter \(h_0\) is also full on A. QED.

The conclusion is for every actual representative over a staircase cell, not
only for the two representatives selected into the forest lift.

## 4. Boundary cells form one initial run

### Lemma 3

The staircase cells touching an A-extreme form one initial run. More precisely:

- if the first step in (2) is \((0,m)\mapsto(0,m-1)\), every boundary cell before
  the first interior cell has \(a=0\);
- if the first step is \((0,m)\mapsto(1,m)\), every such boundary cell has \(b=m\).

Once a cell is interior, every later cell is interior.

If there is no interior cell, the whole simple gap tree is a star centered at
gap vertex \(0\) or at gap vertex \(m\).

### Proof

Both coordinates move monotonically: \(a\) can only increase and \(b\) can only
decrease. Once \(a>0\) and \(b<m\), neither equality can ever return. Before both
strict inequalities hold, after the first step exactly one of \(a=0\), \(b=m\)
can persist. If both move types ever occur, their second first-occurrence creates
the first interior cell. If one move type never occurs, all cells share one
extreme gap vertex, giving the stated star. QED.

Let \(s\) be the number of boundary cells and put

\[
I:=m-s
\tag{8}
\]

for the number of interior cells. Since every staircase step lowers interval
length by one, the terminal interior cells have lengths

\[
I,I-1,\ldots,1.
\tag{9}
\]

Therefore Theorem 2 gives exactly \(2I\) selected paired diameter bars that are
full on the B shore, with total A-support incidence

\[
\boxed{I(I+1)}.
\tag{10}
\]

## 5. Exact two-sheet lift over the interior subtree

Let \(T_{\rm int}\) be the simple gap subgraph consisting of the \(I\) interior
cells.

### Theorem 4 (transverse extreme-layer lift)

If \(I>0\), then \(T_{\rm int}\) is a connected tree with \(I+1\) gap vertices.
Let \(F_{\rm int}\) be the \(2I\) selected physical representatives over those
cells. Then:

1. each gap vertex of \(T_{\rm int}\) has at least one physical endpoint on
   \(L\) and at least one on \(U\);
2. one of those two endpoint sheets lies in B-layer \(0\), the other in B-layer
   \(n\);
3. consequently
   \[
   \boxed{
   |V(F_{\rm int})\cap\{\ell_B=0\}|\ge I+1,\qquad
   |V(F_{\rm int})\cap\{\ell_B=n\}|\ge I+1;
   }
   \tag{11}
   \]
4. in particular
   \[
   \boxed{|V(F_{\rm int})|\ge2I+2.}
   \tag{12}
   \]

More exactly, for each gap vertex \(k\in V(T_{\rm int})\), let
\(\nu_k^L,\nu_k^U\) be the numbers of distinct selected physical endpoints in
A-layer \(k\) on the two threshold arcs. Put

\[
S_{\rm int}
=
\sum_{k\in V(T_{\rm int})}
\bigl[(\nu_k^L-1)+(\nu_k^U-1)\bigr].
\tag{13}
\]

Then

\[
\boxed{
|V(F_{\rm int})|=2(I+1)+S_{\rm int}.
}
\tag{14}
\]

Because \(F_{\rm int}\) is a forest with \(2I\) edges,

\[
\boxed{
\operatorname{comp}(F_{\rm int})=2+S_{\rm int}.
}
\tag{15}
\]

Thus the unsplit physical realization is exactly a two-component lift at this
counting level; every additional same-sheet layer split creates one additional
component in the selected interior diameter forest.

### Proof

The interior cells are a terminal consecutive portion of the staircase order.
Consecutive cells share one gap coordinate, so their simple edge set is
connected. It is a subgraph of the simple gap tree, hence is itself a tree with
\(I+1\) vertices.

Take an interior cell \((a,b)\). Its two selected representatives are
\(L_aU_b\) and \(L_bU_a\). Therefore each endpoint label \(a\) and \(b\) occurs
once on the \(L\) sheet and once on the \(U\) sheet. Since every gap vertex of
\(T_{\rm int}\) is incident to an interior cell, every one of its \(I+1\) layer
labels has at least one selected physical endpoint on each sheet.

Lemma 1 puts the two sheets in opposite A-host intervals, and Theorem 2 puts
those two A-hosts in opposite B-extreme layers. Distinct A-layer labels are
distinct physical source vertices. This proves (11)-(12).

Every endpoint of every edge of \(F_{\rm int}\) is counted by exactly one
\(\nu_k^L\) or \(\nu_k^U\), giving (14). The forest-lift theorem makes
\(F_{\rm int}\) a forest. With \(2I\) edges, the forest identity
\(|V|-|E|=\operatorname{comp}\) gives (15). QED.

### Woodall reconnection tax

Let \(H\) be the full loaded diameter graph. Canonical C-WOODALL says either
\(H\) is connected odd-unicyclic (\(d_H=0\)) or it is a caterpillar forest with
exactly \(d_H\) components.

Contract the components of \(F_{\rm int}\). In the cyclic case, connecting all
of them inside \(H\) requires at least

\[
\boxed{1+S_{\rm int}}
\tag{16}
\]

diameter edges of \(H\setminus F_{\rm int}\). In the forest case, at most
\(d_H\) global components can contain the \(2+S_{\rm int}\) components of
\(F_{\rm int}\), so at least

\[
\boxed{\max\{0,\,2+S_{\rm int}-d_H\}}
\tag{17}
\]

diameter edges of \(H\setminus F_{\rm int}\) are required merely to reconnect
those selected pieces. Paths through additional diameter vertices can only
increase this count.

Equations (16)-(17) do not close the branch, but they show that physical
splitting beyond the mandatory two-sheet lift is not free.

## 6. Opposite-shore rank residue and the exact dichotomy

The B-shore rank theorem gives at least \(n-2\) actual diameters with nonempty
proper B-support, or at least \(n-1\) if B is also exact phase.

Among the selected A-threshold forest, Theorem 2 permits proper B-support only
on the \(2s\) paired representatives over boundary cells and on \(h_0\).
Therefore at least

\[
\boxed{\max\{0,n-2s-3\}}
\tag{18}
\]

proper B-support diameter edges lie outside the selected A forest. If B is exact
phase this improves to

\[
\boxed{\max\{0,n-2s-2\}}.
\tag{19}
\]

More importantly, since \(I+s=m\), one of the following holds exactly:

1. transverse extreme-fiber concentration:
   \[
   I\ge m/2,
   \]
   and each B-extreme layer contains at least
   \[
   \boxed{m/2+1}
   \]
   distinct selected physical diameter endpoints;

2. one-sided boundary staircase:
   \[
   s>m/2,
   \]
   and more than half of the simple A-gap edges form one initial star run
   incident to the same extreme gap vertex \(0\) or \(m\).

At the current fixed-star extraction \(m=\Omega(D)\), so this is a genuine
linear dichotomy.

## 7. Scope audit and next target

This eliminates a previously hidden possibility in the threshold handoff:
physical layer splitting cannot remain arbitrary while the opposite shore is
ignored. Interior staircase structure is forced into an exact two-sheet lift
over the two transverse extreme layer fibers. Additional physical splitting
pays a Woodall reconnection tax. The only way to avoid a linear interior
extreme-fiber population is for the collapsed A-gap tree itself to contain a
linear initial boundary-star run.

The theorem does not show that either alternative is impossible. A convex
diameter thrackle can have large caterpillar/star pieces, and no uniform lower
bound on transverse contact KKT weights is assumed. In particular the known
degree-four rhombus stress regression prevents replacing the argument by a
claim that the complete grid makes cut-contact masses approximately constant.

The next exact obligation is narrower:

\[
\boxed{
\text{exclude the two-sheet linear extreme-fiber lift}
\quad\text{or}\quad
\text{exclude the linear one-sided boundary-star run}.
}
\]

A valid exclusion must use the actual full-source KKT equilibrium,
lexicographic minimality, source co-embedding, or a finite source-preserving
move. Endpoint counts or projected gap-graph rank alone are not enough.

No computation, numerical experiment, new external literature, or unexecuted
certificate is used in this report.


## 8. Opposite proper rows collapse to full-transverse or corner-local

The previous sections identify actual A-staircase diameters joining the opposite
A-host intervals \(I_A^+\) and \(I_A^-\). Once one such diameter has internal
A-layer endpoints, the four-host thrackle geometry also constrains *every*
proper-support row required by the B-shore rank theorem.

### Lemma 5 (same-host exclusion)

Let \(e=xy\) be an actual diameter edge with

\[
x\in I_A^+,\qquad y\in I_A^-.
\tag{20}
\]

Then no actual diameter edge has both endpoints in \(I_B^+\), and none has both
endpoints in \(I_B^-\).

### Proof

The four host intervals occur cyclically as

\[
I_A^+,\ I_B^+,\ I_A^-,\ I_B^-.
\]

The endpoints \(x,y\) divide the boundary into two arcs. The whole interval
\(I_B^+\) lies on one of those arcs and the whole interval \(I_B^-\) lies on the
other. A chord with both endpoints in one \(I_B\)-host therefore has both
endpoints on the same boundary arc cut off by \(x,y\). Its segment does not
cross the segment \(xy\).

The two edges cannot share a source endpoint because the host intervals are
disjoint. This contradicts the convex diameter-thrackle property: two
vertex-disjoint actual diameter edges must cross. QED.

By symmetry, an actual diameter joining \(I_B^+\) to \(I_B^-\) excludes any
actual diameter whose two endpoints lie in one A-host interval.

### Lemma 6 (two-switch rows become transverse full-span rows)

Assume \(I>0\), so Theorem 2 supplies an actual diameter joining
\(I_A^+\) to \(I_A^-\). If an actual diameter \(g\) satisfies

\[
t_B(g)=2,
\]

then its two endpoints lie on the two different B-host intervals. Consequently
its A-support is full:

\[
\boxed{t_B(g)=2\Longrightarrow g\text{ is full-support on A}.}
\tag{21}
\]

### Proof

The joint-switch proof gives

\[
t_B(g)\le
\#\{\text{endpoints of }g\text{ on }I_B^+\cup I_B^-\}.
\]

Thus \(t_B(g)=2\) puts both endpoints on B-host intervals. Lemma 5 forbids the
same B-host, so one endpoint lies on \(I_B^+\) and the other on \(I_B^-\).
The A-layer is constant at opposite extremes \(0,m\) on those two hosts.
Therefore the A-support is the full interval. QED.

The next lemma rules out the remaining A-empty possibility for a one-switch
proper B-row.

### Lemma 7 (one-switch A-constant rows are also A-full)

Assume \(I>0\). Let \(g\) have nonempty proper B-support, \(t_B(g)=1\), and
\(t_A(g)=0\). Then \(g\) is full-support on A.

### Proof

Since \(t_A(g)=0\), exact laminar A-support is either empty or full. Suppose it
is empty. Then both endpoints of \(g\) have one common A-layer.

Because \(g\) has proper B-support and \(t_B(g)=1\), at least one endpoint has
an internal B-layer and hence lies on a B-host interval. On a B-host the
A-layer is one of the two extreme values \(0,m\). Therefore an A-empty \(g\)
must have both endpoints in the same extreme A-layer.

Choose any interior staircase representative \(e\) from Theorem 2. Its
endpoints lie on the two A-host intervals at internal A-layers. The boundary
portion of A-layer \(0\) is entirely contained in one of the two boundary arcs
between the endpoints of \(e\): it consists of the layer-0 B-host together
with the layer-0 end portions of the two A-hosts. The A-layer \(m\) portion is
entirely contained in the other boundary arc. Hence both endpoints of the
hypothetical A-empty \(g\) lie on the same boundary arc between the endpoints
of \(e\).

Thus \(g\) does not cross \(e\). Their endpoints are distinct because \(e\)
has internal A-layers while \(g\) has an extreme A-layer. This again contradicts
the convex diameter-thrackle property. The empty case is impossible, so
\(g\) is A-full. QED.

### Theorem 8 (full-transverse / corner dichotomy for the opposite rank rows)

Assume \(I>0\). Every actual diameter with nonempty proper B-support belongs to
exactly one of the following two classes:

1. it is full-support on A; or
2. it has
   \[
   t_A=t_B=1,
   \]
   hence is one of the four shared-switch corner types from the joint-switch
   theorem.

In particular, if

\[
N_{\rm full}^A
\]

counts actual diameters full on A and

\[
N_{\rm corner}
\]

counts proper B-support diameters with \(t_A=t_B=1\), then the opposite-shore
rank theorem gives

\[
\boxed{
N_{\rm full}^A+N_{\rm corner}\ge n-2.
}
\tag{22}
\]

If B is exact phase, this strengthens to

\[
\boxed{
N_{\rm full}^A+N_{\rm corner}\ge n-1.
}
\tag{23}
\]

Consequently, in the general case,

\[
\boxed{
N_{\rm full}^A\ge\frac{n-2}{2}
\quad\text{or}\quad
N_{\rm corner}\ge\frac{n-2}{2}.
}
\tag{24}
\]

All corner rows occupy at most two adjacent corner types and therefore share
one common host interval, by the already-proved joint-switch corner theorem.

### Proof

A nonempty proper B-support interval has \(t_B=1\) or \(2\).

If \(t_B=2\), Lemma 6 makes the row A-full.

If \(t_B=1\), the joint switch budget gives \(t_A\le1\). When \(t_A=0\),
Lemma 7 makes the row A-full. When \(t_A=1\), the row is shared-switch and
therefore corner-local.

The two classes are disjoint because an A-full row has \(t_A=0\), whereas a
corner row has \(t_A=1\). The B-rank theorem supplies at least \(n-2\) proper
rows, or \(n-1\) in exact B phase, proving (22)-(24). QED.

### Frontier effect

This sharpens the opposite-shore handoff when the A staircase has even one
interior cell. The B-rank rows cannot be an arbitrary family of proper support
intervals. A linear B-rank requirement must be paid by

\[
\boxed{
\text{linear full-A transverse diameters}
\quad\text{or}\quad
\text{linear corner-local diameters on one boundary side}.
}
\tag{25}
\]

The first alternative creates two macroscopic transverse full-support diameter
systems when \(I=\Omega(D)\). The second localizes a macroscopic fraction of the
opposite rank to at most two adjacent physical grid corners. Neither alternative
is yet contradictory: a straight-line thrackle can support large transverse
caterpillar pieces, and a large corner matching is geometrically possible.
The remaining step must use the actual contact/KKT co-embedding or a finite
source-preserving competitor, not chord order alone.


## 9. Corner rows are multiplicity on the one-sided A-boundary fan

The corner-local alternative in Theorem 8 is not independent of the A-staircase.
Exact phase forces every such row back onto one of the staircase's proper boundary
support classes.

### Lemma 9 (unique parallel diameter)

The threshold bar \(h_0\parallel u\) is the only actual diameter parallel to the
A-train direction \(u\).

### Proof

Two distinct parallel actual diameter segments cannot be vertex-disjoint, since
parallel segments do not cross and the convex diameter-thrackle property requires
every two vertex-disjoint diameter edges to cross. They also cannot share one
endpoint: on the same ray the other endpoints would coincide because both lengths
are \(D\), while on opposite rays their two other endpoints would be at distance
\(2D>D\). Thus there is at most one actual diameter parallel to \(u\), namely
\(h_0\). QED.

### Lemma 10 (every A-proper row uses a staircase edge)

Let \(g\) be an actual diameter with nonempty proper A-support. Then its transverse
coefficient relative to the exact A direction is nonzero, so its gap edge belongs
to the transversely active graph \(\Gamma_u\). Consequently its collapsed support
edge is an edge of the simple staircase tree \(T\).

### Proof

If the transverse coefficient vanished, \(g\parallel u\). Lemma 9 would give
\(g=h_0\), but \(h_0\) has full A-support. Therefore \(g\) is transversely active.
The threshold paired-staircase theorem defines \(\Gamma_u\) from all such actual
diameters, and \(T\) is exactly its collapsed simple graph. QED.

### Theorem 11 (corner rows live on the boundary fan)

Assume \(I>0\). Every corner row in Theorem 8 has A-support equal to one of the
proper boundary edges of the staircase tree. All of those support classes lie on
the same side:

\[
\boxed{
\{0,b\}\text{ for varying }b<m
\quad\text{or}\quad
\{a,m\}\text{ for varying }a>0.
}
\tag{26}
\]

Thus the B-rank handoff sharpens from

\[
\text{A-full rows or corner-local rows}
\]

to

\[
\boxed{
\text{A-full rows}
\quad\text{or}\quad
\text{multiplicity over one one-sided A-boundary fan}.
}
\tag{27}
\]

### Proof

A corner row has \(t_A=1\), so its A-support is nonempty proper and touches
exactly one A-extreme. By Lemma 10 its support edge lies in \(T\). Hence it is
one of the proper boundary staircase edges.

Lemma 3 already proves that, once the staircase leaves one boundary side and
enters the interior, it never returns to either boundary. Equivalently all proper
boundary cells before the interior suffix share one extreme gap vertex. This gives
exactly the two alternatives in (26). QED.

Write \(f=s-1\) for the number of proper simple boundary-fan edges. For each such
simple support class \(e\), let \(\mu_e^{\rm corner}\) be the number of actual
corner rows collapsed onto it. Then Theorem 8 becomes the exact multiplicity ledger

\[
\boxed{
N_{\rm full}^A
+
\sum_{e\in E_{\rm fan}}\mu_e^{\rm corner}
\ge n-2,
}
\tag{28}
\]

or \(n-1\) when B is exact phase.

If the fan is centered at gap \(0\), every corner row has one endpoint in the
A-layer-0 boundary region and one endpoint in an internal A-layer on an A-host.
If the fan is centered at gap \(m\), replace layer \(0\) by layer \(m\). This follows
directly from the four-host definition of a corner row.

### Corollary 12 (support-class concentration)

For any integer \(M\ge1\), if

\[
N_{\rm full}^A<M,
\]

then some one-sided boundary support class carries at least

\[
\boxed{
\frac{n-2-M+1}{f}
}
\tag{29}
\]

corner rows whenever \(f>0\), with the obvious floor/ceiling interpretation.
In particular, if the full-A alternative is sublinear and \(f=o(D)\), some single
boundary gap edge carries unbounded physical multiplicity.

This is not yet a contradiction. A quotient support class can contain many physical
diameter representatives. The remaining source-level problem is now exact: either
there are linearly many A-full diameters, or one must control multiplicity of actual
diameter bars over a one-sided boundary fan. Any such multiplicity theorem must retain
physical endpoint splitting rather than collapse one gap layer to one source vertex.
