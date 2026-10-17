> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_edgewise_flux_packets_2026-10-02.md) · source SHA-256 `d71238a6a82b780e358ce59614cdb89a397828495c75d6387f3f9452864a1f22`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9F3360394E18","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase KKT circulation splits edgewise

Date: 2026-10-02  
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5  
Status: proof-only strengthening of the threshold exact-phase branch; C-II remains open.

Dependencies:
- docs/reports/target_c_exact_phase_gap_graph_connectivity_2026-10-01.md
- docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md
- docs/reports/target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md
- docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md

## Theorem

Let $A=\{\tau_1,\ldots,\tau_m\}$ be a retained shore in the threshold exact-phase branch on current main. Let $T$ be the collapsed simple gap graph from the paired-staircase theorem, hence an antitone spanning tree on gap vertices $0,\ldots,m$.

For each tree edge $e=\{a,b\}$, $a<b$, let $\mathcal H_e$ be all transversely active actual diameter rows whose exact $A$-support is $(a,b]$. Split this class into the two physical hull-arc orientations $\mathcal H_e^+$ and $\mathcal H_e^-$, according to the sign of
$$
c_h=(p_y-p_x)\cdot Ju
$$
when $h$ is oriented from $A$-layer $a$ to $A$-layer $b$. Let $\beta_h>0$ be a relative-interior normalized KKT multiplier vector and define
$$
W_e^+=\sum_{h\in\mathcal H_e^+}\beta_h|c_h|,
\qquad
W_e^-=\sum_{h\in\mathcal H_e^-}\beta_h|c_h|.
$$

Then
$$
\boxed{W_e^+=W_e^->0\quad\text{for every }e\in E(T).}
\tag{1}
$$

Thus the exact-phase transverse KKT circulation splits edgewise: after grouping the stationarity identity by simple staircase support type, every group vanishes separately.

Put
$$
M_*=\left\lceil\frac{2\pi}{c_*}\right\rceil.
\tag{2}
$$
At least
$$
\boxed{\left(\frac{c_*}{2}-o(1)\right)D}
\tag{3}
$$
tree edges satisfy
$$
2\le |\mathcal H_e|\le M_*.
\tag{4}
$$
Every such support class is a bounded-cardinality exact KKT packet containing both physical orientations and satisfying (1).

Consequently one of the following holds.

**INTERNAL PACKETS.** At least
$$
\boxed{\left(\frac{c_*}{4}-o(1)\right)D}
\tag{5}
$$
distinct internal tree edges $e=\{a,b\}$, $1\le a<b\le m-1$, carry bounded edgewise-balanced packets. Every row in every such packet has full support on the opposite retained $B$-shore.

**BOUNDARY PACKETS.** One extreme $A$-layer $j_*\in\{0,m\}$ is incident to at least
$$
\boxed{\left(\frac{c_*}{8}-o(1)\right)D}
\tag{6}
$$
distinct tree edges whose diameter support class is a bounded edgewise-balanced packet.

## 1. Edgewise balance

The paired-staircase theorem gives
$$
\sum_h\beta_hc_h\mathbf 1_{(a_h,b_h]}=0.
\tag{7}
$$
Applying the prefix-difference isomorphism
$$
\mathbf 1_{(a,b]}\longmapsto e_a-e_b
$$
gives
$$
\sum_h\beta_hc_h(e_{a_h}-e_{b_h})=0.
\tag{8}
$$

Orient each multiedge by its physical hull-arc orientation and assign positive flow
$$
f_h=\beta_h|c_h|>0.
$$
Equation (8) is node balance for a positive directed circulation on the gap multigraph. Its collapsed simple graph is the tree $T$.

Fix $e\in E(T)$. Removing $e$ disconnects $T$ into $S$ and $S^c$. Sum node balance over $S$. All multiedges supported strictly inside $S$ cancel, and supports inside $S^c$ do not enter the sum. Because $T$ is a tree, the only simple support crossing $S\mid S^c$ is $e$. Hence total positive flow over copies of $e$ in one direction equals total positive flow over copies in the other direction. These two totals are $W_e^+$ and $W_e^-$, proving (1).

The common value is positive because $e$ occurs in the collapsed graph and every used multiedge has positive flow. Hence every support class contains at least one row of each physical orientation:
$$
|\mathcal H_e|\ge2.
\tag{9}
$$

## 2. Linear many packets have bounded multiplicity

Let
$$
\mu_e=|\mathcal H_e|.
$$
The support classes partition the transversely active diameter rows on this shore, so
$$
\sum_{e\in E(T)}\mu_e\le h,
\tag{10}
$$
where $h$ is the total number of actual diameter edges.

At the exact rooted endpoint, current main gives
$$
h=(\pi+o(1))D,
\tag{11}
$$
while the retained threshold shore has
$$
m=|E(T)|\ge(c_*-o(1))D.
\tag{12}
$$

Call $e$ bad if $\mu_e>M_*$. Then
$$
\#\{\text{bad }e\}\le \frac{h}{M_*+1}.
\tag{13}
$$
Since $M_*+1>2\pi/c_*$, equations (11)--(13) give
$$
\#\{\text{bad }e\}<\left(\frac{c_*}{2}+o(1)\right)D.
\tag{14}
$$
Subtracting from (12) proves (3), and (9) gives the lower bound in (4).

This is a support-type theorem, not a KKT weight floor. The positive common values $W_e^+=W_e^-$ may vary arbitrarily and may tend to zero.

## 3. Internal packets span the whole opposite shore

Take a good internal edge $e=\{a,b\}$ with $1\le a<b\le m-1$. Every row in $\mathcal H_e$ has both $A$-layer endpoints internal.

The threshold reference diameter $h_0$ splits the hull into the two monotone arcs $L,U$. The paired-staircase sign proof shows that every transversely active diameter over $e$ joins one arc to the other. The four-host theorem used in the transverse-rail report says that every internal $A$-layer boundary point lies on an $A$-host interval, while the two $A$-host intervals have constant $B$-layers $0$ and $n$.

Therefore every row in $\mathcal H_e$ joins $B$-layer $0$ to $B$-layer $n$. Its exact $B$-support is the entire retained $B$-shore.

This applies to every row in the support class, not only to two selected representatives.

## 4. Internal-versus-boundary packet fork

Let $G$ be the good-edge set from (3). If at least half of $G$ consists of internal edges, then (5) follows and Section 3 gives INTERNAL PACKETS.

Otherwise at least
$$
\left(\frac{c_*}{4}-o(1)\right)D
$$
good edges touch one of the two extreme vertices $0,m$. Apart from the single possible edge $\{0,m\}$, each such edge touches exactly one extreme. Pigeonholing between $0$ and $m$ gives one extreme layer incident to at least
$$
\left(\frac{c_*}{8}-o(1)\right)D
$$
distinct bounded edgewise-balanced support classes. This is BOUNDARY PACKETS.

## Remaining bottleneck

The threshold branch now has a stress-level fork rather than only a support-count fork.

- In the internal alternative, linearly many distinct bounded KKT packets each span the entire opposite shore and balance exactly within their own support type.
- In the boundary alternative, one extreme layer carries a linear ordered family of distinct bounded KKT packets with the same exact edgewise balance.

The next target is to combine these packetwise identities with the opposite-shore shear equations. The internal branch is especially rigid: every member of every selected packet has full opposite-shore support, so any surviving stationarity must come from the ordinary direction projections of these bounded dipoles onto the $B$-train directions.

No computation, numerical evidence, verifier execution, CI result, or unexecuted verifier code is used.
