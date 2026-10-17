> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_edgewise_kkt_balance_2026-10-02.md) · source SHA-256 `71208b1e14d84c69afee63335d12c15c02f690ff2f97fa7e518c5162f519cfbf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C1E0FE63F482","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — edgewise KKT balance in the threshold staircase

Date: 2026-10-02
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5
Status: proof-only; C-II remains open.

## Statement

Let $`A=\{\tau_1,\ldots,\tau_m\}`$ be the threshold exact-phase shore from
\`target_c_exact_phase_threshold_paired_staircase_2026-10-01.md\`, with common
train direction $`u`$. Let $`T`$ be its simple staircase tree on gap vertices
$`0,\ldots,m`$.

For $`e=\{a,b\}\in E(T)`$, $`a<b`$, let $`H_e`$ be all transversely active actual
diameter rows with support endpoint pair $`\{a,b\}`$. Orient each row from lower
to higher $`A`$-layer and put
```math
c_h=r_h\cdot Ju,\qquad \beta_h>0.
```
Then
```math
\boxed{
\sum_{\substack{h\in H_e\\c_h>0}}\beta_h c_h
=
\sum_{\substack{h\in H_e\\c_h<0}}\beta_h(-c_h)
>0.
}
\tag{1}
```
Equivalently,
```math
\boxed{\sum_{h\in H_e}\beta_h c_h=0}
\tag{2}
```
for every simple support type separately.

Thus the KKT cancellation on the exact $`A`$-shore factorizes edge-by-edge over the
staircase tree; different support intervals do not need to cancel one another.

## Proof

The paired-staircase theorem converts the exact $`A`$-shear stationarity identity
into a positive directed circulation on the gap multigraph. For a row over
$`e=\{a,b\}`$, $`a<b`$,

- physical orientation $`L_aU_b`$ has $`c_h>0`$, directed gap edge $`a\to b`$;
- physical orientation $`U_aL_b`$ has $`c_h<0`$, directed gap edge $`b\to a`$;

and its positive flow is $`f_h=\beta_h|c_h|`$.

Collapse parallel edges. Current main proves that the resulting simple graph is
exactly the tree $`T`$. Delete $`e`$ and let $`S`$ be one component of $`T-e`$.
Summing node balance over $`S`$, all internal directed edges cancel. Since $`T`$ is
a tree, the only multiedges crossing $`(S,S^c)`$ are the rows in $`H_e`$.
Therefore total flow over $`e`$ in one direction equals total flow in the other,
which is (1). Both sums are nonempty and positive because the paired-staircase
theorem already forces both physical orientations over every simple edge. Equation
(2) follows.

No multiplier lower bound is used.

## Bounded packet consequence

Write $`\mu_e=|H_e|`$, and let $`h`$ be the total number of actual diameter edges.
The packets are disjoint, so
```math
\sum_{e\in E(T)}\mu_e\le h.
\tag{3}
```
Hence at least $`m/2`$ tree edges satisfy
```math
2\le\mu_e\le {2h\over m}.
\tag{4}
```
At the exact rooted endpoint, current main gives $`h=\pi D+o(D)`$ and
$`m\ge(c_*-o(1))D`$. Therefore, for all sufficiently large $`D`$, at least $`m/2`$
simple support types have uniformly bounded multiplicity
```math
2\le\mu_e\le M_*,
\qquad
M_*:=\left\lceil{4\pi\over c_*}\right\rceil.
\tag{5}
```

Among these bounded packets, either at least $`m/4`$ have both layer endpoints
internal, or one extreme layer $`0`$ or $`m`$ is incident to at least $`m/8`$
distinct bounded packets. This is just pigeonhole: if fewer than $`m/4`$ bounded
edges are internal, more than $`m/4`$ touch an extreme layer, and one of the two
extremes receives at least half of those incidences.

## Cross-shore consequence for an internal packet

Now let $`e=\{a,b\}`$ be internal:
```math
1\le a<b\le m-1.
```
The transverse-rail theorem implies that every row in $`H_e`$, not only the two
selected representatives, joins the two $`A`$-host intervals and therefore has full
support on the opposite shore $`B`$.

Orient each such row from $`B`$-layer $`0`$ to $`B`$-layer $`n`$, obtaining
$`\widehat r_h`$. The two physical orientations give
```math
\widehat r_h\cdot Ju=|c_h|.
\tag{6}
```
Define
```math
P_e=\sum_{h\in H_e}\beta_h\widehat r_h.
```
Using (1),
```math
\boxed{
P_e\cdot Ju
=
\sum_{h\in H_e}\beta_h|c_h|
=
2\sum_{\substack{h\in H_e\\c_h>0}}\beta_h c_h
>0.
}
\tag{7}
```

Thus an internal packet is exactly balanced in the $`A`$-shear equation but exports
a fixed nonzero KKT load to every cut of the opposite shore. Since its $`A`$-support
has two internal endpoints, its signed $`A`$-incidence switches twice:
$`t_A(h)=2`$. The current joint-switch theorem then forces $`t_B(h)=0`$.

Therefore the internal-heavy side of the threshold staircase contains a linear
family of bounded KKT packets that are simultaneously

```math
\boxed{
\text{edgewise balanced on \(A\)}
\;+\;
\text{full-support and switch-inert on \(B\)}
\;+\;
\text{strictly positive in the common \(Ju\) load component.}
}
```

## Remaining bottleneck

The new information is KKT-structural rather than only combinatorial. The next step
is to show that the opposite-shore cut equations cannot absorb a linear family of
these fixed positive packet loads using only the remaining boundary-touching or
layer-local diameter rows, or to exclude the alternative linear family of bounded
packets incident to one extreme $`A`$-layer.

No computation, verifier execution, numerical evidence, or CI result is used.

## Recovery provenance — Slot 1, 2026-10-05

Copied to fresh `main` from `research/threshold-edgewise-kkt-balance-2026-10-02-r14` at exact tip `586a7b472f9cf0c5887cbfefd1293abddf7ff2b4`. This report remains an unreviewed, proof-only candidate; no theorem status or Target C route state is promoted. Its listed staircase, transverse-rail, and exact-multishear dependencies are present on the salvage base. The source artifact contains no verifier or computational certificate.
