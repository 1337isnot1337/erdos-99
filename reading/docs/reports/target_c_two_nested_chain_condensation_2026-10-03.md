> Generated reading edition · [exact source](../../../docs/reports/target_c_two_nested_chain_condensation_2026-10-03.md) · source SHA-256 `2ec3431484318b829cce176bf8826c4855781f692d3413afd45ecf7581df981f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-095CB13710DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — two nested chains exclude an interleaved-only condensation

**Date:** 2026-10-03
**Base:** `7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d`
**State:** `2026-09-14.audit.51`
**Classification:** proved combinatorial candidate awaiting promotion;
conditional geometric application
**Target:** C-II
**LEVEL I STATUS: STILL OPEN.**

The user requested wrap-up before the common-witness source-geometry
application was fully audited. The unrestricted combinatorial result below
has a complete proof. Its finite certificate is supplementary. No geometric
nesting or unpromoted train extraction is silently admitted as a premise.

## 1. Exact theorem

Let `m>=1`. Let `P` and `N` each be a strictly nested chain of nonempty
integer intervals in `{1,...,m}`, both containing `[1,m]`. Form a directed
graph on gap vertices `{0,...,m}` by adding

$$
[a,b]\in P:\ (a-1)\longrightarrow b,
\qquad
[a,b]\in N:\ b\longrightarrow(a-1).
\tag{NC.1}
$$

Repeated edges of a given type may be collapsed; multiplicity does not
affect this theorem.

**Theorem NC.** Exactly one of the following holds:

1. The graph is strongly connected. Then `P=N` is a full chain of `m`
   intervals, starting at `[1,m]`, deleting one left or right cut at each
   step, and ending at a singleton. The simple undirected support is a
   spanning tree, every edge of which has both orientations.
2. Some proper SCC is an integer interval of gap vertices and is a source
   or sink SCC. An isolated interval SCC is allowed.

No rank, stress, geometric realization, or connectivity assumption is
needed. In particular disconnected gap quotients are included.

## 2. Proof: identify the SCCs by positive circulation

Write `K=P intersect N`, itself a nested chain and containing `[1,m]`.
Every common interval supplies both orientations of one edge, so its
endpoints belong to the same SCC.

Conversely, choose a circulation strictly positive on every directed edge
internal to an SCC and zero on all other edges. This is possible: each
internal edge lies on a directed cycle, and the sum of one such cycle
flow for each internal edge has the required property. Across each
prefix cut, circulation gives equality of the positive and negative
interval profiles:

$$
\sum_{I\in P_0}\lambda_I\mathbf1_I
=\sum_{I\in N_0}\gamma_I\mathbf1_I,
\qquad\lambda_I,\gamma_I>0.
\tag{NC.2}
$$

Here `P_0,N_0` are the interval types of internal edges. A positive
profile on a strictly nested chain has a unique decomposition: its
distinct nonempty positive superlevel sets are exactly the chain
intervals, and the increments of those levels recover their weights.
Thus `P_0=N_0`. Every internal edge type is common.

It follows that the SCCs are exactly the connected components of the
bidirected common-edge graph, together with singleton vertices not
incident to a common edge. This does not equate the chosen circulation
with the actual KKT weights of a possible source.

If the graph is strongly connected, every edge is internal, so `P=N`.
A strict nested chain has at most `m` intervals. Connecting `m+1`
vertices requires at least `m` distinct undirected edges. Hence its
length is exactly `m`, every shrink removes one cut, and the final
interval is a singleton. Recursive removal of the discarded extreme
gap vertex proves that these `m` edges form a spanning tree.
The converse follows because all edges of that tree are bidirected.

## 3. Proof: the interval extremum in the remaining case

Write the common intervals as endpoint pairs

$$
(l_1,r_1),\ldots,(l_s,r_s),
\quad l_1=0, r_1=m,quad
l_j\le l_{j+1}<r_{j+1}\le r_j.
\tag{NC.3}
$$

The pair `(l,r)` denotes the cut interval `[l+1,r]`.
Successive common edges belong to the same SCC precisely when they
share an endpoint. If both endpoints change, a new common component
starts. Monotonicity prevents a later common edge from returning to
an earlier component after both endpoints have changed. The common
components therefore occur in consecutive groups in this list.

Contract these components. The resulting condensation is acyclic.
All remaining vertices are singleton SCCs by Section 2. If one of them
is a source or sink, conclusion 2 holds immediately. Assume none is.

Between successive common endpoint pairs, every noncommon interval
of either chain has endpoints in

$$
[l_j,l_{j+1}]\ \cup\ [r_{j+1},r_j].
\tag{NC.4}
$$

The interior vertices of these two bands are singleton SCCs. They have
no neighbors outside this block, apart from its two boundary common
components. This follows directly from nesting: earlier intervals
have endpoints outside the bands, and later ones have endpoints on
their inner side. The block has only one boundary component when the
two consecutive common edges share an endpoint.

We use an elementary DAG observation. In an acyclic block with only
one or two boundary vertices, if no interior vertex is a global source
or sink, follow predecessors and successors of any interior vertex.
Both walks terminate at boundary vertices. The boundaries must be
distinct, since returning to the same one would create a directed
cycle. With two boundaries all such paths have the same direction;
opposite directions would also create a cycle. Thus a one-boundary
block has no interior vertices, and a two-boundary block can connect
its boundaries in at most one direction.

After the smallest common interval there is a final one-boundary
block, with interior vertices `l_s+1,...,r_s-1`. It must be empty,
so `r_s=l_s+1`.

Within the last common component, every successive common edge has
one unchanged endpoint. Its block has one boundary component, so
the changed endpoint advances by exactly one integer: otherwise a
skipped singleton interior vertex would be present. Starting at the
first edge of this component and ending at the adjacent pair
`(l_s,l_s+1)`, these unit advances visit every integer in its span.
The last common component is consequently an interval of gap vertices.

If it were the whole graph, the graph would be strongly connected.
Otherwise it is proper. Its only possible external neighbors lie in
the block immediately preceding its group. That block has two
boundary components and connects them in at most one direction by
the DAG observation. Hence the last component is a source or sink
(or isolated). This proves conclusion 2 and completes the theorem.

## 4. Conditional source consequence and exact missing audit

The application to the October open-cell graph requires the following
explicit hypotheses in the **same physical source**:

1. Actual diameter rows of positive and negative transverse sign
   have nested selected-cut intervals, each sign including full
   support `[1,m]`.
2. The exact cut identities hold for all cut directions in one common
   open actual-diameter direction cell; contact cuts and physical
   slabs have the exact cutset property used by the finite swap.
3. Every retained gap layer has actual core vertices; an interval
   with no external diameter row supplies an actual mixed bar flex
   when its boundary contact directions agree.

Under these hypotheses, NC plus the rederived finite flux identity

$$
\Phi(\{p,\ldots,q-1\};\mu)
=A_q\sin(\theta_q-\mu)-A_p\sin(\theta_p-\mu)
\tag{NC.5}
$$

gives this conditional fork:

$$
\boxed{G_J\text{ strongly connected}quad\text{or}quad
1<|xy|\le1+s\ \text{or}\ D-s\le|xy|<D,}
\quad s\le4K/D.
\tag{NC.6}
$$

Indeed a nonisolated interval source/sink SCC invokes the ONE-SIGN
finite block argument and produces the inactive pair. An isolated
proper interval gives `A_q u_q=A_p u_p` by (NC.5) for all `mu`.
Positivity and coherent lifts imply `u_p=u_q`. Translating that
physical interval infinitesimally perpendicular to this common
direction preserves its boundary contact bars and all diameter bars.
The exterior full-support witness endpoints are fixed. If hypothesis
3 holds this is a non-Euclidean core flex, contradicting canonical ZF.

Thus the interleaved **nontrivial condensation** alternative is removed
under these explicit hypotheses. In the strongly connected case NC
also supplies an opposed full unit-erosion tree, at least `2m` actual
nonempty-support diameter rows, and a common selected cut crossed by
all those rows. This is a support classification; it asserts no
bundlewise balance of the original KKT weights at nonconstant phase.

The exact-phase report already proves sign nesting in its narrower
axial setting. Extending its normal-order argument to a common open
witness cell looks possible using the two common full-support witness
diameters and actual support order, but that source-geometry audit
was **not completed before the user requested wrap-up**. Therefore
(NC.6) is conditional, not a proved source theorem or branch promotion.

Even after that audit, strong connectivity and inverse-D inactive
blockers remain. In a strong graph every proper interval has an
incoming and outgoing edge; the existing one-slab transposition then
has actual diameter constraints of both signs. NC alone constructs
no feasible strict smaller-diameter source.

## 5. Certificate and novelty boundary

Run

```bash
python3 research/verify_target_c_two_nested_chain_condensation_2026_10_03.py
```

It enumerates all 171,538 pairs of strict nested chains including the
full interval for `1<=m<=6`, with exact integer reachability. It checks
both alternatives and the full-tree characterization of strong cases.
It is a finite falsification check, not the unrestricted proof above
and not a geometric or global-optimality certificate.

The nested interval uniqueness argument is an existing dependency in
[the exact-phase bundle report](target_c_exact_phase_nested_bundle_tree_2026-10-01.md),
Section 4, rederived here. The new statement is the unrestricted
**condensation theorem for two possibly unequal nested chains**, and
the source application stays conditional. The
[open-cell flux](../../research/target_c_open_cell_phase_flux_2026-10-03.md)
and [cut divergence](../../research/target_c_open_cell_cut_divergence_condensation_2026-10-03.md)
reports are unpromoted. Their geometric extraction is not established
by the graph computation.

No contact isolate is deleted; no full-source affine-kernel assertion,
Euler diameter traversal, independent scaffold embedding, inactive
pair activation, or KKT multiplier floor is used. Source support
merging may create quotient cycles even when the actual diameter
graph is a forest; the proof expressly works on the quotient.

**Disposition:** preserve NC as a proved candidate awaiting independent
audit/promotion; preserve (NC.6) as conditional. The theorem-state
manifest and canonical prompts remain unchanged.
