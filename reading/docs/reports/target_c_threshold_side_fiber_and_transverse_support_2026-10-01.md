> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_side_fiber_and_transverse_support_2026-10-01.md) · source SHA-256 `7c88de80e657966aec2afa44b0578b9508bf293af6224e0d180eb3275eca925d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-07224CC17DF4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold side-fiber accounting and opposite-shore switch filter

**Date:** 2026-10-01  
**Starting commit:** 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec  
**Mission:** exact-phase threshold staircase / physical endpoint lift / transverse-shore coupling  
**Status:** proof-only proved candidate; no canonical promotion; C-II and Level I remain open.

candidate lemma -> exact canonical quantity -> contradiction / strict competitor / Level I consequence

The candidate quantity here is the number of genuinely split **side-layer fibers**, not the coarser number of physical vertices above an unsigned layer label. The result below corrects the interpretation of the current threshold forest lift and then extracts new two-shore support restrictions from the complete-grid switch budget. It does not by itself reach a contradiction.

## 1. Inputs and scope

Use the current-main threshold exact-phase theorem on one retained shore

$$
A=\{\tau_1,\ldots,\tau_m\}
$$

of the fixed-star complete O--O rectangle. Let $T$ be its simple paired staircase on layer vertices $0,\ldots,m$. For each edge $\{a,b\}\in E(T)$, $a<b$, choose the two actual-diameter representatives

$$
L_aU_b,\qquad L_bU_a,
$$

and let $H_{\rm pair}$ be the resulting $2m$-edge graph. Let $h_0=za$ be the threshold parallel full-support diameter, and put

$$
H_0=H_{\rm pair}\cup\{h_0\}.
$$

Current main proves that every selected representative and $h_0$ crosses one common train $\tau_r$.

The proof uses only:

- the current threshold paired-staircase theorem;
- the current threshold forest-lift observation that common-cut diameter subgraphs are forests;
- the complete-grid joint switch budget $t_A(h)+t_B(h)\le2$;
- the complete-grid rank theorem on the opposite shore;
- the full source is retained throughout.

No unpromoted active-PR result is used.

## 2. The current $\Omega(D)$ unsigned-layer count is not extra side-fiber splitting

For $X\in\{L,U\}$ and $j\in\{0,\ldots,m\}$, let

$$
n_{X,j}
$$

be the number of distinct physical vertices of $H_{\rm pair}$ lying on hull arc $X$ at layer $j$.

Because $T$ spans all $m+1$ layers, every layer is incident with a tree edge. The paired representatives over that edge supply an endpoint on each hull arc at that layer. Hence

$$
n_{L,j}\ge1,\qquad n_{U,j}\ge1.
\tag{1}
$$

Define the genuine side-fiber split excess

$$
S:=\sum_{X\in\{L,U\}}\sum_{j=0}^m(n_{X,j}-1).
\tag{2}
$$

Thus $S=0$ means exactly one physical selected endpoint in every **side-labeled** layer fiber. This is the natural no-splitting baseline for the doubled staircase.

The hull arcs $L,U$ meet only at the endpoints $z,a$ of $h_0$. Let

$$
o\in\{0,1,2\}
$$

be the number of $z,a$ that occur in $H_{\rm pair}$ in both corresponding side fibers. Then the number of distinct physical vertices of $H_{\rm pair}$ is

$$
|V(H_{\rm pair})|=2(m+1)+S-o.
\tag{3}
$$

Every edge of $H_{\rm pair}$ crosses the common cut $\tau_r$. Thus $H_{\rm pair}$ is bipartite. A convex diameter graph has no even cycle, so $H_{\rm pair}$ is a forest. If $c_{\rm pair}$ is its number of nontrivial components,

$$
\boxed{c_{\rm pair}=2+S-o.}
\tag{4}
$$

Now let $r_0\in\{0,1,2\}$ be the number of literal endpoints $z,a$ already present somewhere in $H_{\rm pair}$. Necessarily $o\le r_0$. Adding $h_0=za$ contributes $2-r_0$ new vertices and one edge. Since $h_0$ also crosses $\tau_r$, $H_0$ remains a forest. Therefore

$$
\boxed{
c_0=3+S-o-r_0,
}
\tag{5}
$$

where $c_0$ is the number of nontrivial components of $H_0$.

This is the exact threshold analogue of the older prefix-fiber split identity.

### Consequence for the current forest-lift formula

Let $n_j$ be the current forest-lift report's number of distinct physical $H_0$-vertices in unsigned layer $j$. The layers partition $V(H_0)$, so

$$
\begin{aligned}
\sum_{j=0}^m(n_j-1)
&=|V(H_0)|-(m+1)\\
&=m+3+S-o-r_0\\
&=\boxed{m+c_0}.
\end{aligned}
\tag{6}
$$

Thus the current identity is correct, but its linear lower bound does **not** force $S=\Omega(D)$. The term $m+1$ is already present in a completely side-unsplit doubled staircase.

For example, the legal bookkeeping pattern

$$
S=0,\qquad o=0,\qquad r_0=2
\tag{7}
$$

gives

$$
c_0=1,\qquad
\sum_j(n_j-1)=m+1.
$$

So the present $\Omega(D)$ unsigned-layer excess can be attained with **zero genuine side-fiber split excess**.

This is a scope correction, not a counterexample to the threshold paired-staircase theorem or to the forest identity itself.

## 3. Exact global upper budget for genuine side-fiber splitting

Let $H(\tau_r)$ be the complete subgraph of the actual diameter graph consisting of all diameter edges crossing the common train cut $\tau_r$. It is bipartite across that cut and hence a forest. Write $c_r$ for its number of nontrivial components.

Let

$$
e_{\rm add}=|E(H(\tau_r))|-(2m+1).
$$

Starting from $H_0$, adding one edge can merge at most two old components, so

$$
c_0\le c_r+e_{\rm add}.
\tag{8}
$$

Because $H(\tau_r)$ is a forest and all its incident vertices are loaded diameter vertices,

$$
|E(H(\tau_r))|+c_r=|V(H(\tau_r))|\le q,
\tag{9}
$$

where $q$ is the total loaded diameter-endpoint count. Combining (5), (8), and (9),

$$
3+S-o-r_0
\le
q-(2m+1).
$$

Hence

$$
\boxed{
S\le q-2m-4+o+r_0
\le q-2m.
}
\tag{10}
$$

At the exact rooted endpoint $q=\pi D+o(D)$, while the extracted threshold shore currently only guarantees $m\ge(c_*-o(1))D$. Therefore (10) does not contradict the existing extraction. A closing argument must force substantially more side-fiber splitting, or force a forbidden endpoint-reuse pattern, rather than use (6) alone.

## 4. New opposite-shore switch filter

Now retain the opposite complete O--O shore

$$
B=\{\sigma_1,\ldots,\sigma_n\}.
$$

For an actual diameter edge $h$, let $t_A(h)$ and $t_B(h)$ be its internal support-switch counts on the two selected shores, as in the current joint switch-budget theorem. Current main gives

$$
\boxed{t_A(h)+t_B(h)\le2.}
\tag{11}
$$

For a paired staircase edge $e=\{a,b\}$, $a<b$, each of its two selected actual-diameter representatives has $A$-support exactly $(a,b]$. Therefore

$$
t_A(h)=
\begin{cases}
2,&0<a<b<m,\\
1,&\text{exactly one of }a=0,\ b=m\text{ holds},\\
0,&(a,b)=(0,m).
\end{cases}
\tag{12}
$$

Call a simple staircase edge **internal** when $0<a<b<m$, and let $e_{\rm int}$ be their number. Equation (11) gives, for all $2e_{\rm int}$ selected representatives over internal edges,

$$
\boxed{t_B(h)=0.}
\tag{13}
$$

Exact laminar interval support on $B$ then says that each such row is either empty on all selected $B$-cuts or full-span on all selected $B$-cuts. In particular none of these $2e_{\rm int}$ actual diameter edges is a proper-support $B$-row.

The complete-grid rank theorem gives at least

$$
N_{\rm prop}^B\ge n-2
\tag{14}
$$

distinct proper-support actual diameter edges on $B$. Since the $2e_{\rm int}$ rows in (13) are unavailable for that role and the full actual diameter graph has $h$ edges,

$$
n-2\le h-2e_{\rm int}.
$$

Therefore

$$
\boxed{
h\ge n+2e_{\rm int}-2.
}
\tag{15}
$$

If the opposite shore $B$ is itself exact-phase, its rank theorem gives $N_{\rm prop}^B\ge n-1$, strengthening this to

$$
\boxed{
h\ge n+2e_{\rm int}-1.
}
\tag{16}
$$

This is a genuine two-shore restriction: every internal edge of the threshold staircase removes two actual diameter rows from the pool capable of carrying proper support on the transverse shore.

## 5. Boundary-fan alternative

The equality classification in the threshold paired-staircase theorem contains the full-span simple edge $\{0,m\}$.

Apart from $\{0,m\}$, boundary-touching edges cannot occur on both boundary sides. Indeed, if $\{0,b\}$ with $b<m$ and $\{a,m\}$ with $a>0$ both occurred, antitonicity with $0<a$ would force $b\ge m$, a contradiction.

Let $f$ be the number of proper boundary-touching simple edges. Then

$$
\boxed{
e_{\rm int}+f=m-1,
}
\tag{17}
$$

and all $f$ edges form a one-sided boundary fan.

Combining (15) and (17) gives the exact dichotomy

$$
\boxed{
f\ge \frac{2m+n-h-4}{2}.
}
\tag{18}
$$

When the right side is positive, the opposite-shore rank forces a macroscopic one-sided boundary fan unless the internal staircase already consumes the global diameter budget. In the currently extracted rectangle the constants are not strong enough to make (18) positive uniformly, so this is not C-II closure.

## 6. Threshold--threshold overlap budget

Suppose the opposite shore $B$ is also exact phase in a threshold witness cell. Let its paired staircase have $e_{\rm int}^B$ internal simple edges and $f_B=n-1-e_{\rm int}^B$ proper boundary-fan edges. Write $e_{\rm int}^A=e_{\rm int}$ and $f_A=f$.

For the $A$-threshold selected set $H_0^A$, split its $2m+1$ actual diameter edges according to their $A$-switch count:

$$
|A_2|=2e_{\rm int}^A,\qquad
|A_1|=2f_A,\qquad
|A_0|=3.
\tag{19}
$$

The three zero-switch rows are the two physical representatives over the full-span simple edge $\{0,m\}$ and the parallel threshold diameter $h_0^A$. Similarly,

$$
|B_2|=2e_{\rm int}^B,\qquad
|B_1|=2f_B,\qquad
|B_0|=3.
\tag{20}
$$

If an actual diameter edge belongs to both selected systems, (11) applies to that same edge. Any shared edge outside $A_0\cup B_0$ therefore has positive switch count on both shores, so necessarily

$$
t_A=t_B=1.
$$

Consequently

$$
H_0^A\cap H_0^B
\subseteq
A_0\cup B_0\cup(A_1\cap B_1),
$$

and hence

$$
\boxed{
|H_0^A\cap H_0^B|
\le 6+2\min(f_A,f_B).
}
\tag{21}
$$

Taking the union inside the full actual diameter graph gives

$$
\begin{aligned}
h
&\ge |H_0^A\cup H_0^B|\\
&\ge (2m+1)+(2n+1)-6-2\min(f_A,f_B).
\end{aligned}
$$

Thus

$$
\boxed{
h\ge
2m+2n-4-2\min(f_A,f_B).
}
\tag{22}
$$

Equivalently, using $f_A=m-1-e_{\rm int}^A$ and $f_B=n-1-e_{\rm int}^B$,

$$
\boxed{
h\ge
2m+2n-4
-
2\min(m-1-e_{\rm int}^A,\ n-1-e_{\rm int}^B).
}
\tag{23}
$$

This is stronger than treating the two threshold staircases independently whenever both have a substantial internal part. It is still quantitatively compatible with the present small extracted rectangle constants.

## 7. Host localization of the transverse zero-switch rows

Use the four boundary host intervals from the complete-grid joint switch theorem, in cyclic order

$$
I_A^+,\ I_B^+,\ I_A^-,\ I_B^-.
\tag{24}
$$

Along $I_A^+\cup I_A^-$, the $A$-layer changes, while the $B$-layer is constant on each individual $A$-host interval at the two opposite extreme values. Symmetrically, the $B$-layer changes only on the $B$-host intervals.

Take one selected physical representative $h$ over an internal $A$-staircase edge. We already know $t_A(h)=2$. The proof of the joint switch theorem gives

$$
t_A(h)
\le
\#\{\text{endpoints of }h\text{ in }I_A^+\cup I_A^-\}.
$$

Since $h$ has only two endpoints, equality forces both endpoints into the $A$-host union.

There are then only two possibilities:

1. both endpoints lie in the same $A$-host interval. Their $B$-layers agree, so $h$ has empty support on the selected $B$-shore;
2. the endpoints lie in opposite $A$-host intervals. Their $B$-layers are the two extremes, so $h$ has full-span support on the selected $B$-shore.

Thus (13) sharpens to the exact geometric classification

$$
\boxed{
\text{internal \(A\)-staircase row}
\Longrightarrow
\begin{cases}
B\text{-empty},&\text{same }A\text{-host},\\
B\text{-full-span},&\text{opposite }A\text{-hosts}.
\end{cases}
}
\tag{25}
$$

Moreover all $B$-empty internal selected rows lie in one common $A$-host interval. If one such diameter chord had both endpoints in $I_A^+$ and another had both endpoints in $I_A^-$, their endpoint sets would lie in two disjoint nonalternating boundary intervals. The two diameter edges would be vertex-disjoint and would not cross, contradicting the convex diameter-thrackle property.

Therefore, after swapping signs if necessary,

$$
\boxed{
\text{every \(B\)-empty internal paired row has both endpoints in }I_A^+.
}
\tag{26}
$$

Finally, every selected paired staircase representative meets the threshold diameter $h_0=za$ in the diameter-thrackle sense: if disjoint it crosses properly, and if incident with $z$ or $a$ the same two-arc convention applies. Hence its two endpoints occupy opposite $L/U$ arc sides. If a $B$-empty internal row has both endpoints inside one connected $A$-host interval, that host interval meets both $L$ and $U$. Hence it contains $z$ or $a$. Consequently

$$
\boxed{
\text{if neither endpoint of }h_0\text{ lies in an \(A\)-host interval, then every internal paired row is \(B\)-full-span.}
}
\tag{27}
$$

This removes a diffuse empty-support escape: transverse-empty internal rows, if they exist at all, are confined to one threshold-endpoint host cap.

### Relation to the older staircase audits

The September C88/C98 staircase reports already show that the abstract paired lift is a bipartite double cover and that raw physical layer multiplicity must be measured relative to the two-sheet baseline. The September double-cover/caterpillar audit also shows that caterpillar graph shape by itself cannot contradict the paired staircase. Equations (5)--(10) are the present threshold-shore form of that physical-fiber accounting.

The genuinely new ingredient here is therefore not the observation that a paired staircase has two sheets. It is the coupling (13)--(27) to the **opposite complete O--O shore** through the October 1 joint switch budget and four-host boundary order.

## 8. Two-threshold cross-host dichotomy and endpoint budget

Assume now that the opposite shore $B$ is also threshold exact phase. Let $e_{\rm int}^A,e_{\rm int}^B$ be the internal-edge counts of the two simple staircases.

Every selected representative over an internal $A$-edge has both endpoints in the $A$-host union by Section 7. Symmetrically, every selected representative over an internal $B$-edge has both endpoints in the disjoint $B$-host union.

Hence an internal $A$-row and an internal $B$-row are always vertex-disjoint. Since both are actual diameter edges, the convex diameter-thrackle property forces them to cross properly.

Suppose $e_{\rm int}^B>0$, and choose one internal $B$-row $g$. If an internal $A$-row $h$ were $B$-empty, (25)--(26) would put both endpoints of $h$ inside one $A$-host interval, say $I_A^+$. Both endpoints of $g$ lie in the $B$-host union, entirely outside that boundary interval. Thus the endpoints of $h$ and $g$ do not alternate around the convex hull, so their chords do not cross. They share no endpoint because the host intervals are disjoint. This contradicts the diameter-thrackle property.

Therefore

$$
\boxed{
e_{\rm int}^B>0
\Longrightarrow
\text{every internal \(A\)-row is \(B\)-full-span.}
}
\tag{28}
$$

Symmetrically,

$$
\boxed{
e_{\rm int}^A>0
\Longrightarrow
\text{every internal \(B\)-row is \(A\)-full-span.}
}
\tag{29}
$$

In particular, if both internal-edge counts are positive, the two internal selected row families form two transverse complete-crossing chord families: every $A$-internal selected diameter is full-span on $B$, every $B$-internal selected diameter is full-span on $A$, and every cross-family pair crosses properly.

There is also an exact star alternative. If an internal $A$-row is $B$-empty, then (28) forces

$$
e_{\rm int}^B=0.
$$

But the $B$-staircase has $n$ simple edges on $n+1$ layer vertices, contains $\{0,n\}$, and all remaining $n-1$ edges are one-sided boundary-touching by Section 5. With no internal edge, connectivity forces the entire simple staircase to be one endpoint star:

$$
\boxed{
\{\{0,j\}:1\le j\le n\}
\quad\text{or}\quad
\{\{j,n\}:0\le j<n\}.
}
\tag{30}
$$

Thus a transverse-empty internal threshold row is possible only against a pure endpoint-star threshold staircase.

### Disjoint internal-layer endpoint budget

For the $A$-threshold paired lift, every internal layer $j=1,\ldots,m-1$ is incident with a simple staircase edge. The two physical orientations over an incident edge supply at least one selected diameter endpoint on each of the two $A$-threshold hull arcs at that layer. These are distinct physical source vertices because the two arcs meet only at the threshold endpoints, whose $A$-layers are $0,m$.

Let

$$
S_A^{\rm int}
:=
\sum_{X\in\{L_A,U_A\}}
\sum_{j=1}^{m-1}
\left(n^A_{X,j}-1\right),
\tag{31}
$$

and define $S_B^{\rm int}$ analogously. Then the selected paired systems use exactly

$$
2(m-1)+S_A^{\rm int}
$$

distinct physical diameter endpoints in internal $A$-layers, and

$$
2(n-1)+S_B^{\rm int}
$$

distinct endpoints in internal $B$-layers.

The joint four-host order makes these two physical sets disjoint. Indeed, the $A$-layer is constant at the extreme values $0,m$ on each $B$-host interval, so every source vertex of internal $A$-layer lies in the $A$-host union. Symmetrically every internal $B$-layer vertex lies in the disjoint $B$-host union.

All these vertices are loaded actual-diameter endpoints. Therefore

$$
\boxed{
q
\ge
2m+2n-4
+
S_A^{\rm int}+S_B^{\rm int}.
}
\tag{32}
$$

At the exact rooted endpoint $q=\pi D+o(D)$, this gives

$$
\boxed{
S_A^{\rm int}+S_B^{\rm int}
\le
\pi D-2m-2n+4+o(D).
}
\tag{33}
$$

Even with no genuine internal splitting, a two-threshold rectangle therefore consumes at least $2m+2n-4$ distinct loaded diameter endpoints in four disjoint host blocks.

The current fixed-star extraction constant is too small for (32) to close the branch. Its use is structural: any future argument forcing side-fiber splitting on both exact-phase shores now spends against one common global endpoint budget, with no cross-shore endpoint reuse available in the internal layers.

## 9. Regression: rigid gap-tree leaf/component release is exactly blocked

The paired staircase also explains why the most obvious finite leaf-release move cannot close the threshold branch.

Fix a non-full-span simple staircase edge

$$
e=\{a,b\}\ne\{0,m\}.
$$

Delete $e$ from the simple gap tree $T$. Because the full-span edge $\{0,m\}$ remains in $T-e$, the layer vertices $0,m$ lie in the same tree component. Let $U$ be the other component, so

$$
\varnothing\ne U\subseteq\{1,\ldots,m-1\}.
\tag{34}
$$

Let $R_U$ be the union of all source layers whose layer labels lie in $U$, and rigidly translate every source point of $R_U$ by a vector $v$, leaving the rest of the source fixed.

### 9.1 Contact motion

Every old unit contact not belonging to a selected threshold train has both endpoints on the same side of every selected cut and hence in the same selected layer. It is therefore unchanged.

A selected-train contact can move only when its adjacent layer labels have different membership in $U$. Since the exact-phase train direction is $u$, after orienting from the fixed endpoint toward the moved endpoint its unit vector is either $u$ or $-u$.

Because $U$ is nonempty but contains neither $0$ nor $m$, its indicator along the linearly ordered layers starts and ends at zero. Hence its boundary contains both an entering and a leaving transition. Thus both contact orientations $u$ and $-u$ occur among the moving boundary contacts.

Writing

$$
v=xu+yJu,
$$

preservation of the two unit lower bounds gives

$$
|u+v|^2\ge1,\qquad |-u+v|^2\ge1,
$$

so

$$
x^2+y^2\ge2|x|.
\tag{35}
$$

In particular, along any sufficiently small feasible nonzero translation,

$$
y\ne0,\qquad x=O(y^2).
\tag{36}
$$

The special choice $v=tJu$ opens every moving boundary contact strictly, to length $\sqrt{1+t^2}$.

### 9.2 The complete moving old-diameter set is one gap bundle

Take an old actual diameter edge $h$ whose endpoints have selected $A$-layers $p,q$.

If $h$ is transversely active relative to $u$, its simple gap $\{p,q\}$ is an edge of the threshold simple gap tree $T$. It moves under the $R_U$-translation exactly when one of $p,q$ lies in $U$, namely exactly when that tree edge crosses the cut $\delta_T(U)$. Since $U$ is a component of $T-e$,

$$
\delta_T(U)=\{e\}.
$$

Thus every moving transversely active old diameter has simple gap exactly $e$.

If $h$ is transversely inactive, then its diameter vector is parallel to $u$. Two distinct planar diameter edges cannot have the same projective direction: vertex-disjoint ones would have to cross, while incident collinear length-$D$ edges would coincide or put their other endpoints $2D$ apart. Hence the only such row is the threshold diameter $h_0$. Its endpoint layers are $0,m$, both outside $U$, so it is unchanged.

Therefore

$$
\boxed{
\text{the complete moving old-diameter set under this translation is exactly the physical bundle over }e.
}
\tag{37}
$$

All strict old nondiameter and noncontact inequalities remain strict for sufficiently small $v$.

### 9.3 The paired orientations block every sufficiently small rigid release

Assume $a\in U$, $b\notin U$; otherwise replace $U$ by the equivalent orientation. Orient every physical row over $e$ from layer $a$ to layer $b$, and write

$$
r_h\cdot Ju=c_h.
$$

Translating the layer-$a$ endpoint by $v=xu+yJu$ changes the squared diameter length by

$$
\Delta_h(v)
=
-2r_h\cdot v+|v|^2
=
-2(r_h\cdot u)x-2c_hy+x^2+y^2.
\tag{38}
$$

The paired-staircase theorem supplies at least one physical row $h_+$ with $c_{h_+}>0$ and one row $h_-$ with $c_{h_-}<0$.

For contact-feasible small translations, (36) makes every term except $-2c_hy$ of order $O(y^2)$. Therefore:

- if $y>0$, then $\Delta_{h_-}(v)>0$ for all sufficiently small nonzero $v$;
- if $y<0$, then $\Delta_{h_+}(v)>0$ for all sufficiently small nonzero $v$.

Hence

$$
\boxed{
\text{no sufficiently small nonzero rigid translation of a component of }T-e
\text{ can open its boundary contacts while keeping every old diameter }\le D.
}
\tag{39}
$$

For the explicit perpendicular move $v=tJu$, the obstruction is immediate:

$$
\Delta_h(tJu)=-2tc_h+t^2,
\tag{40}
$$

so the two paired orientations block the two signs of $t$.

This is not merely failure to find the correct leaf direction. The entire rigid component-translation class is locally impossible for every non-full-span tree edge.

### 9.4 Consequence for the live leaf target

The threshold tree still has a recursive leaf structure, but a successful finite leaf elimination must use a mechanism outside rigid translation of the leaf-side layer component. It must, for example, change contact combinatorics, use a non-rigid internal deformation, or couple more than one gap bundle so that the paired transverse blockers cancel.

The exact obstruction in (39) is why the current paired staircase is mechanically stronger than the earlier unpaired gap-tree picture.

## 10. Adversarial audit

The following stronger claims are **not** proved and must not be inferred:

1. Equation (6) does not imply $S=\Omega(D)$. The $m+1$ term is the doubled-hull-arc baseline.
2. An edge with $t_B=0$ need not be $B$-full-span; it may have empty $B$-support. The proof of (15) uses only that it is not proper-support.
3. The one-sided fan does not imply one physical diameter star. A boundary layer may contain many physical source vertices.
4. The degree bound $\Delta(H)=O(D^{3/4})$ would force only a sublinear number of boundary-fiber splits from a linear fan; that alone is not a contradiction.
5. The rooted endpoint relations $q,h=\pi D+o(D)$ do not make (10), (18), or (22) contradictory at the current small extraction constant $c_*$.
6. No source-preserving finite deformation is produced here.
7. Split-star O--O, inactive-interface, open-cell exact phase, nonconstant phase, and macroscopic-container branches are untouched.

## 11. Current implication chain and next obligation

The corrected threshold chain is

$$
\text{paired staircase}
\Longrightarrow
\begin{cases}
\text{exact side-fiber identity }(5),\\
S\le q-2m,\\
\text{internal rows are transverse-shore nonswitching},\\
h\ge n+2e_{\rm int}-2,\\
\text{or a one-sided boundary fan}.
\end{cases}
$$

If both shores are threshold, (22) additionally limits how much the two physical paired systems can reuse the same actual diameter edges.

The high-value next step is no longer to count the unsigned layer excess in (6). It is to use the actual contact/rhombus co-embedding to eliminate one of the two surviving mechanisms:

1. a linear internal staircase whose paired diameter rows are empty/full-span on the transverse shore; or
2. a linear one-sided boundary fan whose physical endpoint fibers split enough to respect the actual diameter-star geometry.

Either must be converted into an exact unit triangle or a source-preserving strict sub-$D$ competitor to close the threshold branch.

No computation, numerical evidence, verifier execution, or CI result is used in this report.
