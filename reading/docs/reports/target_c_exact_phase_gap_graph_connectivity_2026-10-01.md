> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_gap_graph_connectivity_2026-10-01.md) · source SHA-256 `dff7efd4a3c89d3dfbd6d735dac0701f237a52e09d4f1ec2f00162d86f545cc3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C1A665A66DD1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- exact-phase diameter rank is a connected gap graph

Date: 2026-10-01  
Base main: 5ff8caddec4bd2b56b1934abe8602f071b0c61ba  
Status: proof-only strengthening of the fixed-star exact-phase/TB2 branch; C-II remains open.

## Theorem

Let $\tau_1,\ldots,\tau_m$ be one retained exact-phase shore of the current fixed-star complete O--O rectangle, in complement-dual path order. Use the coherent orientation from the current exact-phase rank theorem, so
$$
u_1=\cdots=u_m=:u.
$$

For an actual diameter edge $h$, exact laminar support gives either empty support or
$$
\varepsilon_h=\sigma_h\mathbf 1_{[a_h,b_h]},
\qquad
1\le a_h\le b_h\le m,
\qquad
\sigma_h\in\{\pm1\}.
$$
Its diameter-derivative row is
$$
M_h=c_h\mathbf 1_{[a_h,b_h]},
\qquad
c_h:=\sigma_h(r_h\cdot Ju).
\tag{1}
$$

Discard rows with $c_h=0$. Define a multigraph $\Gamma_u$ on the ordered gap vertices $0,1,\ldots,m$ by assigning to every remaining row the edge
$$
e_h=\{a_h-1,b_h\}.
\tag{2}
$$

Then
$$
\boxed{\operatorname{rank}M=m+1-\operatorname{comp}(\Gamma_u).}
\tag{3}
$$

Current main proves $\operatorname{rank}M=m$ on an exact-phase retained shore. Hence
$$
\boxed{\Gamma_u\text{ is connected}.}
\tag{4}
$$

Equivalently, there are exactly $m$ actual diameter rows whose support-endpoint edges form a spanning tree on the $m+1$ ordered gap vertices and whose rows form a basis of the exact-phase diameter derivative matrix.

## Proof

Define
$$
L:\mathbb R^m\to H:=\left\{y\in\mathbb R^{m+1}:\sum_{j=0}^m y_j=0\right\}
$$
by
$$
L(x_1,\ldots,x_m)
=
\bigl(x_1,x_2-x_1,\ldots,x_m-x_{m-1},-x_m\bigr).
\tag{5}
$$
This is an isomorphism. For an interval indicator,
$$
L(\mathbf 1_{[a,b]})=e_{a-1}-e_b.
\tag{6}
$$
Multiplying a nonzero row by $c_h$ does not change rank, so
$$
\operatorname{rank}M
=
\operatorname{rank}\{e_p-e_q:\{p,q\}\in E(\Gamma_u)\}.
\tag{7}
$$

For a multigraph on $n$ vertices with $c$ connected components, the span of the oriented edge vectors $e_p-e_q$ has dimension $n-c$: its orthogonal complement is exactly the space of vectors constant on each connected component. Taking $n=m+1$ proves (3). Since current main gives rank $m$, (4) follows.

A connected graph on $m+1$ vertices contains a spanning tree with $m$ edges. The corresponding edge vectors are independent, so their inverse images under $L$, and hence the associated nonzero rows of $M$, form a basis.

## Consequences

This recovers and strengthens the current exact-phase switching statement.

- Every internal gap vertex $j\in\{1,\ldots,m-1\}$ is incident to an edge of $\Gamma_u$. Therefore some transversely active actual diameter interval ends at $j$ or starts at $j+1$: every adjacent interface switches.
- The exterior gap vertices $0$ and $m$ are nonisolated even after all diameter rows parallel to $u$ are removed.
- More strongly, for every nonempty proper $S\subset\{0,\ldots,m\}$, some transversely active actual diameter has one support-endpoint gap in $S$ and the other outside $S$.
- A spanning-tree basis admits leaf elimination: at each stage one can choose a basis diameter row with a private leaf gap vertex. Thus the exact-phase rank can be represented by a recursively pivotal family of actual diameter supports.

The current theorem $\operatorname{rank}M=m$ previously yielded only $N_{\rm prop}\ge m-1$ and $s\ge m-1$. Equation (3) identifies the complete linear-algebraic obstruction: in exact phase, mixed rigidity is equivalent to connectivity of the transversely active support-endpoint graph.

## Remaining bottleneck

Connectivity itself is not contradictory; paths and stars on the ordered gap vertices have full graphic rank. The next target is to combine a spanning-tree basis of $\Gamma_u$ with the convex diameter-thrackle property and the exact positive two-bar axial reactions at every interface. A closing argument must rule out such a connected ordered gap graph with those geometric/force labels, or extract a source-preserving strict diameter decrease from a tree leaf.

No computation, verifier execution, CI result, or unexecuted verifier code is used.
