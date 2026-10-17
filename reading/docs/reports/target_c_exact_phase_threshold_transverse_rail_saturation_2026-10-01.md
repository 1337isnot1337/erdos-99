> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md) · source SHA-256 `5af0523286fc97315a44519797cc7be8c5a0e9083e201d9070e844209052164e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C994C1DD3A84","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase saturates the transverse extreme rails

Date: 2026-10-01
Base main: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
Status: proof-only strengthening of the threshold exact-phase branch; C-II remains open.

Dependencies:
- docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md
- docs/reports/target_c_exact_phase_threshold_forest_lift_2026-10-01.md
- docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md
- docs/reports/target_c_global_sublinear_diameter_star_2026-09-09.md

## Theorem

Let
```math
A=\{\tau_1,\ldots,\tau_m\},\qquad
B=\{\sigma_1,\ldots,\sigma_n\}
```
be the two retained shores of the fixed-star complete O--O rectangle, and suppose
that $`A`$ is in the threshold exact-phase branch.

Let $`T`$ be the paired-staircase simple gap tree on the $`A`$-layers
$`0,\ldots,m`$. For every edge $`\{a,b\}\in E(T)`$, choose the two actual-diameter
representatives supplied by the paired-staircase theorem, one in each physical
hull-arc orientation. Add the unique $`A`$-parallel full-support diameter $`h_0`$,
and call the resulting selected diameter graph $`F`$, as in the forest-lift report.

Then:

1. every internal $`A`$-layer $`j=1,\ldots,m-1`$ contains at least two distinct
   selected diameter endpoints, one on each $`A`$-host boundary interval;
2. after orienting the $`B`$-layer coordinate suitably, those two $`A`$-host
   intervals have constant $`B`$-layers $`0`$ and $`n`$, so each internal
   $`A`$-layer meets both transverse extreme rails;
3. consequently each transverse extreme rail contains at least $`m-1`$ distinct
   selected diameter endpoints;
4. if $`\{a,b\}\in E(T)`$ has $`1\le a<b\le m-1`$, then both selected
   diameter representatives over $`\{a,b\}`$ have full support on $`B`$, hence
   cross every $`\sigma_j`$;
5. if $`c(F)`$ is the number of nontrivial components and $`n_j`$ is the number
   of distinct vertices of $`F`$ in $`A`$-layer $`j`$, then
   ```math
   \boxed{
   (n_0-1)+(n_m-1)+
   \sum_{j=1}^{m-1}(n_j-2)=c(F)+1.
   }
   \tag{1}
   
   ```

There is also a quantitative two-shore fork. Let $`e_{\rm int}`$ be the number
of tree edges of $`T`$ with both endpoints internal.

- If $`e_{\rm int}\ge m/2`$, at least $`m`$ distinct selected actual-diameter
  bars have full support on all of $`B`$.
- If $`e_{\rm int}<m/2`$, one of the two extreme $`A`$-layers contains
  ```math
  \Omega(D^{1/4})
  
  ```
  distinct selected diameter vertices.

Thus the threshold staircase cannot hide all of its forced physical splitting from
the opposite shore. It either produces a linear family of actual diameters crossing
every opposite train, or a polynomially growing collection of distinct diameter
carriers in one extreme $`A`$-layer.

## 1. Four-host coordinates

Use the four boundary host intervals from the complete-grid joint-switch theorem:
```math
I_A^+,\ I_B^+,\ I_A^-,\ I_B^-
```
in cyclic order. Let
```math
\lambda_A(x)\in\{0,\ldots,m\},\qquad
\lambda_B(x)\in\{0,\ldots,n\}
```
be the two complement-dual layer coordinates of an outer-boundary source point.

The four-host theorem gives:

- on the two $`B`$-host intervals, $`\lambda_A`$ is constant at the two extreme
  values $`0,m`$;
- symmetrically, on the two $`A`$-host intervals, $`\lambda_B`$ is constant at
  the two extreme values $`0,n`$.

Let $`h_0=za`$ be the unique diameter parallel to the common $`A`$-train direction.
It has full $`A`$-support, so after reversing the path if necessary
```math
\lambda_A(z)=0,\qquad \lambda_A(a)=m.
\tag{2}
```

Split the convex-hull boundary at $`z,a`$ into the two arcs $`L,U`$, directed from
$`z`$ to $`a`$, as in the paired-staircase proof. Every selected $`A`$-crosscut
separates $`z`$ from $`a`$, so each has one terminal on $`L`$ and one on $`U`$.
The two $`A`$-host intervals therefore lie on opposite arcs.

A boundary point with
```math
0<\lambda_A(x)<m
```
cannot lie on a $`B`$-host interval, because $`\lambda_A`$ is extreme there.
Hence an internal-layer point on $`L`$ lies on the $`A`$-host interval contained
in $`L`$, and an internal-layer point on $`U`$ lies on the other $`A`$-host
interval. Relabel the two $`A`$-host intervals so that
```math
\lambda_B=0\quad\text{on the \(L\)-host},\qquad
\lambda_B=n\quad\text{on the \(U\)-host}.
\tag{3}
```

## 2. Every internal A-layer hits both transverse rails

Fix $`j\in\{1,\ldots,m-1\}`$. Because $`T`$ is a spanning tree on
$`0,\ldots,m`$, vertex $`j`$ is incident to some tree edge $`\{j,k\}`$.
The paired-staircase theorem supplies two distinct actual-diameter representatives
over this simple edge, in the two physical orientations
```math
L_jU_k,\qquad L_kU_j.
\tag{4}
```

Thus one selected diameter endpoint lies on $`L`$ in $`A`$-layer $`j`$, and another
lies on $`U`$ in $`A`$-layer $`j`$. Since $`j`$ is internal, Section 1 puts these
on the two $`A`$-host intervals. By (3), their $`B`$-layers are exactly $`0`$
and $`n`$.

The two endpoints are distinct because $`L,U`$ meet only at $`z,a`$, whose
$`A`$-layers are $`0,m`$. Repeating this for every internal $`j`$ gives at least
$`m-1`$ distinct selected diameter endpoints on each transverse extreme rail:
vertices in different $`A`$-layers cannot coincide.

No claim is made that these diameter endpoints are train terminals or contact
vertices of the grid.

## 3. Internal tree edges are full-support on the opposite shore

Take
```math
\{a,b\}\in E(T),\qquad 1\le a<b\le m-1.
```
Its two selected representatives are
```math
L_aU_b,\qquad L_bU_a.
\tag{5}
```

All four endpoints lie in internal $`A`$-layers. Hence every $`L`$-endpoint has
$`B`$-layer $`0`$ and every $`U`$-endpoint has $`B`$-layer $`n`$. Each of the two
diameter bars therefore has exact $`B`$-support
```math
\{1,\ldots,n\},
```
so each crosses every selected $`B`$-train.

An actual diameter row has a unique pair of $`A`$-support endpoints, so representatives
belonging to different simple tree edges are distinct. Therefore $`e_{\rm int}`$
internal tree edges yield $`2e_{\rm int}`$ distinct selected diameter bars with
full opposite-shore support.

## 4. Exact refinement of the physical splitting count

Let $`n_j`$ be the number of distinct vertices of $`F`$ in $`A`$-layer $`j`$.
Section 2 gives
```math
n_j\ge2\qquad(1\le j\le m-1).
\tag{6}
```
The full-support diameter $`h_0=za`$ gives
```math
n_0\ge1,\qquad n_m\ge1.
\tag{7}
```

The forest-lift theorem gives
```math
|E(F)|=2m+1
```
and $`F`$ is a forest. Therefore
```math
|V(F)|=2m+1+c(F).
\tag{8}
```
The $`A`$-layer fibers partition $`V(F)`$, so
```math
\sum_{j=0}^{m}n_j=2m+1+c(F).
\tag{9}
```
Subtracting the mandatory baseline
```math
1+2(m-1)+1=2m
```
from (9) proves (1).

Thus every internal layer is already forced to split across the two transverse
extreme rails; only $`c(F)+1`$ selected vertices remain beyond that baseline.

## 5. Internal-heavy versus boundary-heavy staircase

If
```math
e_{\rm int}\ge\frac m2,
```
Section 3 gives at least
```math
2e_{\rm int}\ge m
```
distinct actual-diameter bars with full support on $`B`$.

Now suppose
```math
e_{\rm int}<\frac m2.
```
More than $`m/2`$ of the $`m`$ tree edges are incident to at least one of the two
extreme vertices $`0,m`$. Put
```math
d_0=\deg_T(0),\qquad d_m=\deg_T(m).
```
Then
```math
d_0+d_m>\frac m2,
```
so one extreme layer $`j_*\in\{0,m\}`$ satisfies
```math
d_{j_*}>\frac m4.
\tag{10}
```

Each tree edge incident to $`j_*`$ contributes two distinct selected actual-diameter
bars, each with exactly one endpoint in $`A`$-layer $`j_*`$. Hence more than $`m/2`$
selected diameter-edge incidences hit source vertices in that one layer.

A source vertex is incident to at most $`\Delta(H)`$ actual diameter edges, so the
number of distinct selected diameter vertices in that extreme layer is at least
```math
\frac{2d_{j_*}}{\Delta(H)}
>
\frac{m}{2\Delta(H)}.
\tag{11}
```
The source-wide star theorem gives
```math
\Delta(H)=O(D^{3/4}),
```
while the retained threshold shore has
```math
m\ge(c_*-o(1))D.
```
Therefore
```math
\boxed{n_{j_*}=\Omega(D^{1/4}).}
\tag{12}
```

## 6. Remaining bottleneck

The previous forest-lift theorem forced only aggregate endpoint-fiber splitting.
The present theorem couples that splitting to the opposite complete shore:

```math
\boxed{
\begin{array}{c}
\text{at least \(m\) selected diameter bars cross every \(B\)-train}
\\[2mm]
\text{or}
\\[2mm]
\Omega(D^{1/4})\text{ distinct selected diameter carriers occupy one extreme
\(A\)-layer.}
\end{array}}
```

The threshold exact-phase branch remains open. The next step is to exclude one of
these two alternatives using the opposite-shore exact/KKT structure, near-disk hull
geometry, or a source-preserving finite motion.

No computation, numerical evidence, verifier execution, CI result, or unexecuted
verifier code is used.
