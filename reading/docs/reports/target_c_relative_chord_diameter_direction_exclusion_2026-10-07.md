> Generated reading edition · [exact source](../../../docs/reports/target_c_relative_chord_diameter_direction_exclusion_2026-10-07.md) · source SHA-256 `9b57a1ba61569c684f1fc1a79c8b21eee9d2e89b344261ed0d796f6431fec769`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-329D33AED974","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: relative chord arithmetic and diameter-direction exclusion

Date: 2026-10-07.
Research base: 0f970f223f1b6019c36eaee38dfba7c409b900b4.
Canonical state: 2026-10-08.audit.128.
Classification: proved candidate awaiting independent audit and promotion.
Lifecycle: unreviewed, noncanonical.
C-II and Level I remain open.

## 1. Global comparison being attempted

The proposed route is a global count of actual diameter edges:

1. establish additive physical charts on almost all actual loaded endpoints;
2. use short-chord arithmetic to restrict their diameter normals;
3. prove $`h=o(D)`$ and contradict canonical $`h\ge\lceil D\rceil`$.

The theorem below proves Steps 2--3 from exact chart hypotheses. Step 1 is not
established for arbitrary canonical sources. In particular, neither the
full-core branch nor the macroscopic-container branch is closed.

The key distinction from
[Audit.91](../audits/target_c_loaded_attachment_lattice_independent_audit_2026-10-07.md)
is that accumulated positional error may stay bounded away from zero or grow.
Only the increments in each additive chart must have narrow direction windows.
The proof uses the normal-cone and actual-diameter counting mechanism of that
audit, with a new relative-chord hypothesis and with a growing number of charts.

## 2. Additive charts and short physical chords

An additive chart consists of two finite sequences of unit vectors
$`u_a,v_b`$, cumulative sums

```math
U_i=\sum_{a<i}u_a,\qquad V_j=\sum_{b<j}v_b,
```

and a translation $`c`$. A set of actual physical points is represented in this
chart if every one of its points has coordinates

```math
p=c+U_i+V_j
```

for assigned integer indices $`(i,j)`$. The represented indices may be only a
subset of the rectangular index range; the missing points need not belong
to the source. This is an exact physical coordinate representation, not a
combinatorial train labeling or a scaffold.

Suppose two unit vectors $`u,v`$ give a basis matrix $`T=[u\ v]`$ with
$`\|T^{-1}\|\le K`$, and

```math
|u_a-u|\le\eta,\qquad |v_b-v|\le\eta,\qquad
0\le\eta<\frac{1}{2\sqrt2 K}.
```

For two represented points $`p,q`$, put $`z=(i-k,j-l)\in\mathbb Z^2`$ and
$`r=p-q`$. Telescoping the increments gives

```math
|r-Tz|\le\eta(|z_1|+|z_2|)\le\sqrt2\eta|z|.
```

Consequently,

```math
|r|\ge(1/K-\sqrt2\eta)|z|>\frac{|z|}{2K},
\qquad
|r-Tz|\le 2\sqrt2K\eta|r|.
```

For distinct points $`z\ne0`$. If $`|r|\le L`$, then $`|z|\le2KL`$.
Let

```math
\delta=\arcsin(2\sqrt2K\eta),\qquad
M_L=(2\lfloor2KL\rfloor+1)^2-1.
```

The angle between $`r`$ and $`Tz`$ is at most $`\delta`$. To check its orientation,
the error is strictly smaller than $`|r|`$, so $`r\cdot Tz>0`$; the angle is acute.
The distance from $`r`$ to the line through $`Tz`$ is at most $`|r-Tz|`$, proving
the asserted sine bound.

There are at most $`M_L`$ possible nonzero integer vectors $`z`$ with these
coordinate bounds. Thus every short chord has its normal in one of at most
$`M_L`$ angular intervals of width $`2\delta`$.

No bound on $`|U_i-iu|`$ or $`|V_j-jv|`$ was used. Those accumulated errors can
be large. The short physical chord itself bounds the difference of its
indices, which is the reason the local arithmetic survives bending.

## 3. Finite diameter-direction estimate

Let $`A`$ be any finite planar unit-separated source of diameter $`D\ge2`$.
Let $`H`$ be its full actual diameter graph, $`B`$ its actual diameter-endpoint
set, and $`h=|H|`$. Partition

```math
B=B_0\sqcup E_1\sqcup\cdots\sqcup E_J.
```

Suppose each $`E_j`$ has an additive chart from Section 2, with the same bound
$`K`$ on its inverse basis norm and with increment error $`\eta_j`$ satisfying
the displayed strict threshold. Set

```math
\delta_j=\arcsin(2\sqrt2K\eta_j),\qquad
P_j=\operatorname{per}(\operatorname{conv}E_j),\qquad
\delta_D=2\arcsin\frac1{2D}.
```

The perimeter of a segment is twice its length; the perimeter of a singleton
is zero. For every $`L\ge1`$,

```math
\boxed{
h\le |B_0|+\frac2L\sum_jP_j
       +J(2M_L+2)
       +\frac{2M_L}{\delta_D}\sum_j\delta_j.
}
```

### Proof

Every actual diameter endpoint is an extreme point of the full source hull.
Indeed, a nontrivial convex combination of other source points, paired with
a diameter partner, contradicts strict convexity of the squared norm.
Hence every member of $`E_j`$ is a vertex of its own convex hull.

For a carrier with at least three points, order its hull edges cyclically.
There are at most $`P_j/L`$ long edges; at most $`2P_j/L`$ vertices touch them.
The normals of all short edges lie in a union $`W_j`$ of at most $`M_L`$
closed intervals, each of width $`2\delta_j`$, by Section 2.

A vertex with two short incident edges has the endpoints of its outward
normal cone in $`W_j`$. If this cone is not contained in $`W_j`$, its interior
contains a full component of the open complement of $`W_j`$. Distinct vertex
normal-cone interiors are disjoint. There are at most $`M_L`$ complementary
components. Mark these exceptional vertices and all long-edge vertices bad.
Carriers with one or two points contribute at most two additional bad
vertices. The total number of bad vertices, including $`B_0`$, is therefore
at most

```math
|B_0|+\frac2L\sum_jP_j+J(M_L+2).
```

At every remaining endpoint $`p\in E_j`$, any actual diameter normal
$`n=(p-q)/D`$ is in its hull normal cone, and therefore in $`W_j`$.
For any other source point $`x`$,

```math
|x-q|^2\le D^2=|p-q|^2
\quad\Longrightarrow\quad
n\cdot(x-p)\le-\frac{|x-p|^2}{2D}<0.
```

Thus $`p`$ is the unique support point in that direction.

Canonical DB.3 separates distinct actual diameter directions projectively
by at least $`\delta_D`$. There is at most one diameter pair per projective
direction, as also reconstructed in Audit.91. Projecting $`W_j`$ modulo
$`\pi`$, its at most $`M_L`$ arcs contain at most
$`M_L(1+2\delta_j/\delta_D)`$ actual diameter directions. Summing this count
bounds all diameter edges with a good endpoint.

All remaining edges belong to the diameter graph induced on the bad
endpoints. The diameter-graph edge bound is hereditary and gives at most
as many edges as vertices, by canonical Woodall topology. Adding the two
counts proves the estimate. This is the same exact normal-cone argument as
Audit.91; its positional hypothesis has been replaced by Section 2.

## 4. Growing-chart exclusion

For a sequence with $`D\to\infty`$, suppose

```math
|B_0|=o(D),\qquad J=o(D),\qquad
\sum_jP_j=O(D),\qquad \sum_j\delta_j=o(1),
```

with uniform $`K`$. Fix $`L`$ first. Since $`D\delta_D\to1`$, the finite estimate
gives

```math
\limsup\frac hD\le\frac{2C_P}{L},
```

where $`C_P`$ is any eventual bound on $`\sum P_j/D`$. Send $`L\to\infty`$.
Then $`h=o(D)`$.

In the canonical C-II normal form, $`h\ge\lceil D\rceil`$, so these chart
hypotheses are impossible. This contradiction applies in either exhaustive
branch. It uses the actual diameter graph, rather than a selected stress
support, and moves or drops no source point.

Two useful special cases are:

- fixed $`J`$, uniformly conditioned charts, increment errors tending to
  zero, and $`|B_0|=o(D)`$; here $`\sum P_j\le J\pi D`$;
- charts for all relevant harmonic attachment sets, uniformly conditioned,
  with increment errors $`O(1/D)`$ and unused loaded endpoints $`o(D)`$.
  Canonical $`c_I=O(D^{2/3})`$ and the attachment perimeter sum $`O(D)`$ give
  $`J=o(D)`$ and $`\sum\delta_j=O(D^{-1/3})=o(1)`$.

The second case is conditional on the exact physical charts for those
attachment sets. The existing dense inverse-phase theorem supplies a
complete near-triangular grid inside one macroscopic carrier; it does not
give these charts on every actual attachment set.

## 5. Bending and the remaining universal bridge

The canonical
[bent-grid regression](../audits/target_c_bent_grid_positional_transport_independent_audit_2026-10-07.md)
has an exact additive representation with horizontal increments in a window
of width below $`1/M`$ and one fixed vertical direction. Its basis has uniformly
bounded inverse norm. Thus its relative short-chord arithmetic satisfies
Section 2, despite the proven positive absolute lattice-approximation error.
Its pins are not actual diameter endpoints and it is not globally optimal;
no additional status is inferred for that family.

This removes the need to prove absolute positional convergence for additive
charts. It does not show that a coherent physical grain has an additive chart.
Three train families, exceptional face returns, holes, and attachments outside
the extracted grid must be treated in the actual source, not silently copied
onto an abstract grid.

Most importantly, a bulk area cover does not give an $`o(D)`$ exceptional
loaded set. Small boundary carriers may contain a linear number of loaded
endpoints while occupying $`o(D^2)`$ area. Their phase widths need not satisfy
$`\sum\delta_j=o(1)`$. The macroscopic-container branch does not supply the
chart hypotheses either.

The full-source chart or relative-direction bridge remains an unreviewed
research obligation. No universal statement about global minimizers, and
no Level I proof or disproof, follows without that bridge.

## 6. Dependencies and verification

Used exact canonical inputs: DB.3 in
[the difference-body audit](../targets/target-c/59-difference-body-density-audit.md),
[Woodall topology](target_c_woodall_diameter_topology_2026-09-10.md),
the C-II count in
[ZR/ZF](../targets/target-c/57-zr-zf-rigidity-audit.md),
and the normal-cone proof in Audit.91. The attachment special case additionally
uses the existing component-count and perimeter ledgers.

The analytic proof does not rely on finite samples. The exact checker
[verify_target_c_relative_chord_arithmetic_2026_10_07.py](../../../research/verify_target_c_relative_chord_arithmetic_2026_10_07.py)
checks 3,640 boundary pairs in the existing bent-grid family at M=8,12,16.
It certifies unit separation, uniform inverse-basis control, increment error,
integer-index bounds, and the angular sine inequality over the exact field
Q(sqrt(3)). The midpoint bow stays greater than 1/10, while the increment
errors are bounded by 1/M. There are 624 chords of length at most four.
These samples certify neither the analytic normal-cone theorem nor actual
diameter loading, canonical chart coverage, or global optimality.

There has been no independent audit, certificate registration, or promotion.
