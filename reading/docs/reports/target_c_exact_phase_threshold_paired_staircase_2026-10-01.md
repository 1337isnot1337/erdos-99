> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md) · source SHA-256 `631f7fe2d5d950c47bcedd9eabf710fa4b356f9a974db69d64c965cbbbca5ebf`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-44322ED52692","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold exact-phase gap graph is a paired staircase

Date: 2026-10-01
Base main: 14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79
Status: proof-only strengthening of the threshold-cell part of the fixed-star exact-phase/TB2 branch; C-II remains open.

## Theorem

Let $`\tau_1,\ldots,\tau_m`$ be one retained exact-phase shore of the current fixed-star complete O--O rectangle, ordered along its complement-dual path, and assume the shore lies in a threshold witness cell. The threshold-cell theorem gives one actual diameter edge $`h_0=za`$, parallel to the common train direction $`u`$, crossing every retained train cut. Orient it from layer $`0`$ to layer $`m`$, so $`p_a-p_z=Du`$.

For every transversely active actual diameter $`h=xy`$, orient from the lower layer $`a_h`$ to the higher layer $`b_h`$, put
```math
c_h=(p_y-p_x)\cdot Ju\ne0,
```
and assign the gap edge $`\{a_h,b_h\}`$ on vertices $`0,\ldots,m`$. This is the same transversely active gap graph $`\Gamma_u`$ as in the current-main connectivity report, with the support interval indexed as $`(a_h,b_h]`$.

Then:

1. the positive relative-interior KKT stress gives a nowhere-zero directed circulation on $`\Gamma_u`$;
2. every simple directed circulation cycle has length two;
3. every simple unordered gap edge occurs in both physical hull-arc orientations;
4. the collapsed simple gap graph is an antitone tree with exactly $`m`$ edges, and all its intervals contain one common retained train index $`r`$;
5. its exact staircase equality is
```math
\sum_{\{a,b\}\in E_{\rm simp}}(b-a)=\frac{m(m+1)}2;
```
6. selecting one actual diameter in each physical orientation over every simple edge gives $`2m`$ distinct nonparallel diameter bars with total retained-shore support incidence
```math
\boxed{m(m+1)},
```
and all $`2m`$ cross the common train $`\tau_r`$.

The parallel full-support diameter $`h_0`$ is additional, so this threshold exact-phase shore uses at least $`2m+1`$ actual diameter edges.

## 1. Hull arcs and sign

Because $`h_0=za`$ has full support, every selected proper train crosscut separates $`z`$ from $`a`$. Split the convex-hull boundary at $`z,a`$ into arcs $`L,U`$, both directed from $`z`$ to $`a`$. Pairwise disjointness of the selected crosscuts and their dual-path order imply that each crosscut has one terminal on each arc and that the layer index is nondecreasing from $`0`$ to $`m`$ along both arcs.

Choose the sign of $`Ju`$ so that the open arc $`U`$ lies in the positive half-plane bounded by the line $`za`$. Since $`za\parallel u`$, convexity puts the open arc $`L`$ in the negative half-plane.

Take a transversely active diameter $`h=xy`$, oriented from layer $`a<b`$. If $`h`$ is disjoint from $`h_0`$, the convex diameter-thrackle property forces $`h`$ to cross $`h_0`$, so its endpoints lie on opposite hull arcs. If $`h`$ shares $`z`$ or $`a`$ with $`h_0`$, use the same arc convention at the shared endpoint. Hence
```math
c_h>0
```
exactly for physical orientation $`L_aU_b`$, and
```math
c_h<0
```
exactly for $`U_aL_b`$. The reference diameter $`h_0`$ itself has $`c_{h_0}=0`$.

## 2. Positive KKT circulation

The exact simultaneous laminar shear preserves every old unit contact. On the exact-phase shore the squared-length derivative row of $`h`$ is
```math
2c_h\mathbf 1_{(a_h,b_h]}.
```
Let $`\beta_h>0`$ be the diameter multipliers of a relative-interior normalized KKT stress. Virtual work in each retained shear coordinate gives
```math
\sum_{h:c_h\ne0}\beta_hc_h\mathbf 1_{(a_h,b_h]}=0.
\tag{1}
```
Applying the discrete prefix difference
```math
\mathbf 1_{(a,b]}\mapsto e_a-e_b
```
gives
```math
\sum_{h:c_h\ne0}\beta_hc_h(e_{a_h}-e_{b_h})=0.
\tag{2}
```

Orient every gap edge from its physical $`L`$-endpoint level to its physical $`U`$-endpoint level and assign flow
```math
f_h=\beta_h|c_h|>0.
```
By Section 1, (2) is exactly node balance. Thus every transversely active row carries strictly positive flow in a directed circulation.

## 3. Directed cycles collapse to two-cycles

Take a simple directed cycle
```math
k_0\to k_1\to\cdots\to k_{s-1}\to k_0.
```
Its physical diameter bars are $`L_{k_i}U_{k_{i+1}}`$.

At level $`k_{i+1}`$, consecutive cycle bars are $`L_{k_i}U_{k_{i+1}}`$ and $`L_{k_{i+1}}U_{k_{i+2}}`$. If they are vertex-disjoint, the diameter-thrackle crossing rule and monotone layer order on $`L,U`$ give
```math
\operatorname{sgn}(k_{i+1}-k_i)
=
-\operatorname{sgn}(k_{i+2}-k_{i+1}).
```
If they share a physical endpoint, that endpoint must lie on both $`L`$ and $`U`$, hence is $`z`$ or $`a`$; the common level is then the strict global minimum $`0`$ or maximum $`m`$. Therefore cycle levels alternate strict local minima and maxima.

Write them as
```math
a_0\to b_0\to a_1\to b_1\to\cdots\to a_{r-1}\to b_{r-1}\to a_0.
```
The even bars $`L_{a_i}U_{b_i}`$ are pairwise vertex-disjoint and hence pairwise crossing, so $`F:a_i\mapsto b_i`$ is strictly order-reversing. The odd bars similarly give a strictly order-reversing bijection $`G:b_i\mapsto a_{i+1}`$. Thus $`G\circ F`$ is an order-preserving bijection of the finite ordered set $`\{a_i\}`$, hence the identity. But it is also the cyclic shift $`a_i\mapsto a_{i+1}`$. Therefore $`r=1`$.

Every simple directed circulation cycle has length exactly two.

## 4. Pairing, antitone order, and a common cut

A finite positive circulation decomposes into directed simple cycles. Hence every used simple unordered gap edge $`\{a,b\}`$ occurs in both directions. For $`a<b`$, the two physical orientations are
```math
L_aU_b,\qquad L_bU_a.
\tag{3}
```
So every simple gap edge has at least two distinct actual diameter representatives.

Take distinct simple edges $`(a,b)`$ and $`(c,d)`$, with $`a<b`$, $`c<d`$, $`a<c`$. Choose the $`L_aU_b`$ and $`L_cU_d`$ representatives. If $`b<d`$, their endpoint orders agree on both hull arcs, so the chords do not cross; because the endpoint levels differ, they also cannot share a source endpoint. This contradicts the diameter-thrackle property. Therefore
```math
\boxed{a<c\Longrightarrow b\ge d.}
\tag{4}
```

The simple interval family is antitone. Any two intervals overlap, so one-dimensional Helly gives a common retained train index $`r`$ with
```math
a<r\le b
```
for every simple gap edge.

## 5. Connectivity forces exact staircase equality

Current main proves $`\Gamma_u`$ connected. Collapsing parallel edges preserves connectivity, so the simple graph on $`0,\ldots,m`$ has at least $`m`$ edges.

For an antitone family of pairs $`a<b`$, list distinct left endpoints $`a_1<\cdots<a_s`$, put $`B_i=\{b:(a_i,b)\in E\}`$, and $`m_i=\min B_i`$, $`M_i=\max B_i`$. Antitonicity gives
```math
M_1\ge m_1\ge M_2\ge\cdots\ge M_s\ge m_s.
```
Hence
```math
|E|
\le\sum_i(M_i-m_i+1)
\le M_1-m_s+s
\le m.
```
Thus the simple gap graph has exactly $`m`$ edges and is a tree.

Equality holds at every step. As in the earlier C87-C88 staircase equality calculation,
```math
a_i=i-1,\qquad
B_i=\{t_i,t_i+1,\ldots,t_{i-1}\},
```
for
```math
t_0=m\ge t_1\ge\cdots\ge t_s=s.
```
The same telescoping calculation gives
```math
\boxed{
\sum_{\{a,b\}\in E}(b-a)=\frac{m(m+1)}2.
}
\tag{5}
```

## 6. Exact incidence consequence

For every simple gap edge choose one diameter in each orientation from (3). These are $`2m`$ distinct actual diameter bars. A bar over $`\{a,b\}`$ has retained-shore support on exactly the $`b-a`$ trains $`\tau_{a+1},\ldots,\tau_b`$. Therefore
```math
\sum_{h\in H_{\rm pair}}
|\operatorname{supp}_{\mathcal T}(h)|
=
2\sum_{\{a,b\}\in E}(b-a)
=
\boxed{m(m+1)}.
\tag{6}
```

Every simple interval contains the common index $`r`$, so every selected bar crosses $`\tau_r`$:
```math
\boxed{N_{\tau_r}\ge2m.}
\tag{7}
```

Finally $`h_0`$ is a further actual diameter edge, parallel to $`u`$ and absent from the transverse gap graph. Hence the threshold exact-phase shore accounts for at least $`2m+1`$ actual diameter edges.

## Scope and remaining bottleneck

The threshold-cell hypothesis is essential here. The parallel full-support diameter $`h_0`$ supplies the reference chord parallel to the common train direction, making the KKT transverse sign coincide with the two physical hull-arc orientations. This argument does not apply to an exact-phase shore in an open witness cell, where no actual diameter is parallel to $`u`$.

Thus the threshold exact-phase branch is reduced to
```math
\boxed{
\text{paired antitone gap tree}
+
\text{one common train crossed by at least }2m\text{ diameter bars}
+
m(m+1)\text{ retained-shore incidences}.
}
```

The remaining threshold bottleneck is to couple that common-cut diameter load to the opposite complete O--O shore and the fixed-star endpoint structure. The open-cell exact-phase branch remains separate.

No computation, numerical evidence, verifier execution, CI result, or unexecuted verifier code is used.
