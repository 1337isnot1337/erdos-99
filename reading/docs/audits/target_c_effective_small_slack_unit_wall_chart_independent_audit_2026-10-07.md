> Generated reading edition · [exact source](../../../docs/audits/target_c_effective_small_slack_unit_wall_chart_independent_audit_2026-10-07.md) · source SHA-256 `8e96dddf515ea48998cfb76dc2176a9441528300673e31c62e2dd218a3c784cb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 7 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-5CAB5EAF1139","canonical":true,"claim_ids":["C-ARITHMETIC-SIX-WALL-UNIFORM-CHART","C-UNIT-WALL-LOW-SLACK-TRIANGULAR-CHART"],"claim_statuses":{"C-ARITHMETIC-SIX-WALL-UNIFORM-CHART":"canonical","C-UNIT-WALL-LOW-SLACK-TRIANGULAR-CHART":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — effective chart from small Oler slack

**Audit base:** `origin/main=e63281db62bde8b41402efb6be00b72c82c145a0`,
state `2026-10-07.audit.81`.

**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at
`f65456766477da03711b1316ffde13e27acf70aa`. The effective-chart report,
verifier, and certificate first appeared at `8af7e411ae1c1797dbd624c96729c36d3885367e`
and are byte-for-byte unchanged at the frozen tip. The separate quarter-fold
report added at `f6545676` is outside this audit.

## Exact claims promoted

Fix a convex polygon (F) with (b) cyclic unit sides and vertices, and a
finite set (X) consisting of those (b) boundary vertices and (z) strict
interior points. Assume every pair in (X) is at distance at least one. Set
(a=\sqrt3/4) and

```math
\sigma=\operatorname{area}(F)-a(2z+b-2).
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
1. **Low-slack effective chart.** If (0\le\sigma\le1/1000), then a
   Delaunay triangulation of (X) has (2z+b-2) triangles, all acute. Each
   triangle (T) has area (a+\sigma_T), with $`\sigma_T\ge0`$ and
   $`\sum_T\sigma_T=\sigma`$. Each side of (T) has length in
   $`[1,1+5\sigma_T]`$, and each angle differs from $`\pi/3`$ by at most
   $`50\sigma_T`$. Interior vertices have six incident triangles and
   boundary vertices have one, two, or three. Replacing the triangles by
   unit equilateral triangles gives a convex triangular-lattice polygon with
   the same triangulation, at most six nonstraight corners, and all lattice
   sites in that polygon present. After aligning one boundary unit edge,
   every point of (X) is within (60b\sigma\) of its developed lattice
   point.
2. **Uniform arithmetic-wall chart.** Fix (M\ge3),
   (N=3M^2-3M+1), and the specified six-direction arithmetic wall whose
   side-rate multiset is
   $`\{M-1,M-3,\ldots,1-M\}`$, with consecutive side turns (2\theta\)
   and corner turns $`\pi/3-2(M-1)\theta`$. For
   (0<\theta\le1/(10000M^3)), every pairwise unit-separated union of all
   (6M) wall vertices and (N) strict-interior points has
   $`\sigma<1/1000`$. Its developed polygon is exactly (H_M), and after
   matching the standard orientation and translation every wall/cloud point
   is within (1000M^4\theta) of its corresponding point in (P_M).
```



These claims concern feasible finite packings in a fixed container. The
auxiliary plane packing used below is only a triangulation device. No source
optimality, triangle conclusion, deficit-one classification, source-to-wall
extraction, or C-II/Level I conclusion is promoted.

## Oler saturation and the auxiliary packing

Write (n=b+z). Oler's bound for a unit-separated set in a convex container
is

```math
n\le {2\over\sqrt3}\operatorname{area}(F)+{b\over2}+1
 = n+{2\over\sqrt3}\sigma.
```
Thus $`\sigma\ge0`$. If a point could be added to (X) inside (F) while
remaining unit-separated, Oler applied to the enlarged set would give

```math
n+1\le n+{2\over\sqrt3}\sigma<n+1,
```
since $`\sigma\le1/1000`$. So (X) is saturated inside (F).

Enumerate a dense countable set in the plane and greedily add points at
distance at least one from the current set, starting with (X). No accepted
point lies in (F), by saturation. The resulting packing is locally finite
and has covering radius at most one: if some point (y) had distance
(d>1) from the final packing, choose an enumerated point within
$`(d-1)/3`$ of (y). If accepted it would be within one of (y); if rejected,
an earlier accepted point within one of it would be closer to (y) than
(d). Either contradicts the definition of (d).

The bounded Voronoi cells therefore give a locally finite Delaunay
triangulation. Every Delaunay circumradius is at most one by the covering
radius. Each wall edge is a Delaunay edge: at its midpoint the two endpoints
are at distance (1/2), while any other unit-separated point is at distance
at least $`\sqrt3/2`$. Hence the wall cycle bounds a triangulated disk with
exactly the vertices (X). Euler gives (T=2z+b-2). Boundary wall-wall
pairs cause no hidden assumption: they are included in the initial
unit-separation hypothesis.

## Triangle area, curvature and acute pairing

For a Delaunay triangle with circumradius (R\le1), all three sides are at
least one. If $`\ell=\arcsin(1/(2R))`$, each angle is at least $`\ell`$.
The angle sum forces (R\ge1/\sqrt3). At fixed (R), concavity of
$`\log\sin`$ makes the area smallest at angles
$`(\ell,\ell,\pi-2\ell)`$, giving

```math
\operatorname{area}(T)\ge {\sqrt{4R^2-1}\over4R^2}\ge {\sqrt3\over4}=a.
```
The last function has equal endpoint minima on
(R^2\in[1/3,1]) and one interior maximum. Consequently every triangle
excess $`\sigma_T=\operatorname{area}(T)-a`$ is nonnegative, and their sum
is exactly $`\sigma`$.

Suppose a triangle has largest angle $`\alpha\ge\pi/2`$. Then
$`\alpha\le2\pi/3`$, and its opposite edge satisfies
$`L^2\ge2(1-\cos\alpha)`$, so that edge is internal. Let $`\beta`$ be
the opposite angle in the Delaunay neighbor. Local Delaunay gives
$`\beta\le\pi-\alpha\le\pi/2`$. The neighbor's other angles are at least
$`\pi/6`$, so their sine product is at least
$`\tfrac12\sin(\beta+\pi/6)`$. Its area is at least

```math
{L^2\over4}\left({\sqrt3\over2}+{1\over2}\cot\beta\right)
\ge {\sqrt3\over4}(1-\cos\alpha).
```
The first triangle has area at least $`\tfrac12\sin\alpha`$. Together the
pair exceeds the two-triangle baseline (2a) by at least
$`(2-\sqrt3)/4>1/1000`$, contradicting the total slack. Thus all triangles
are acute.

## Quantitative near-equilateral bounds


**Source formatting excerpt (unbalanced inline math in the original):**

```text

Let (L) be an acute triangle's largest side and (x,y\) the squares of the
other sides. If (L\ge\sqrt2\), the Heron expression
$`16A^2=4xy-(x+y-L^2)^2`$ is concave on
$`1\le x,y\le L^2,\ x+y\ge L^2`$. Its minimum at a vertex is at least
$`4(L^2-1)`$, hence (A\ge1/2). But
$`A=a+\sigma_T\le a+1/1000<1/2`$, a contradiction.
```



If (L<\sqrt2), the acute projection onto its base lies inside the segment.
Since both other sides are at least one, the height is at least
$`\sqrt{1-L^2/4}`$, so

```math
A\ge f(L)={L\sqrt{4-L^2}\over4}.
```
This function increases on $`[1,\sqrt2]`$, and
$`f(11/10)>a+1/1000`$, so (L<11/10). On $`[1,11/10]`$,
$`f'(L)>1/5`$. Since (f(1)=a), this yields
$`L-1\le5\sigma_T`$. All three sides lie in $`[1,11/10]`$. On this
cube every angle has sine greater than (4/5), and each partial derivative
of its cosine with respect to a side is less than two in absolute value.
The mean-value bound therefore gives
```math
|\angle-\pi/3|\le {5\over2}\sum_{e\subset T}(|e|-1)
\le 50\sigma_T.
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
At an interior vertex, the incident angles sum to (2\pi), while their
total deviation from (k\pi/3) is at most (50\sigma\le0.05<\pi/3\);
therefore (k=6). At a boundary vertex the sum is at most $`\pi`$, giving
(1\le k\le3). The boundary turning angles in the equilateral development
are $`(3-k)\pi/3`$, are nonnegative, and sum to (2\pi). There are at
most six nonzero turns.
```



## Development and displacement

Replace each actual Delaunay triangle by an equilateral unit triangle and
develop across shared edges. Six triangles around each interior vertex give
zero holonomy there. Since the triangulated region is a disk, this develops
single-valuedly. Its boundary has unit lattice edges, nonnegative turns
(0,\pi/3,2\pi/3), and total turn (2\pi), so it is a convex lattice
polygon. The development has positive orientation and degree one; hence it
is one-to-one and covers that polygon. Every triangular-lattice site in the
polygon is a vertex of an elementary face or edge, so none can be missing.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
Anchor one boundary unit edge. Across a simple dual path, the orientation
error is at most the sum of its triangle angle errors, hence at most
(50\sigma\). An edge-length error is at most (5\sigma\), so corresponding
edge vectors differ by at most (55\sigma\). In a convex lattice polygon the
coordinates (i,j,i+j) each have boundary range at most (b/2): one unit
boundary step changes each coordinate by at most one, and a closed boundary
must traverse every range twice. Hex-lattice shortest paths can be chosen to
keep all three coordinates between their endpoint values, so every vertex
can be joined to the anchor in at most (b) lattice edges while remaining
inside the polygon. Summing the edge errors gives the stated looser bound
(60b\sigma\).
```



## Uniform arithmetic-wall identification

For the specified arithmetic wall, put `u=1`, `v=exp(i*pi/3)`, and
`z_h=exp(i*(M-1-2h)*theta)` for `0<=h<M`. Set
`S_r=sum_(h<r) z_h`; in one fundamental sector the wall vertices are
`P(a,b)=S_a*u+(S_(a+b)-S_a)*v`, with `a,b>=0` and `a+b<=M`.
Since `|z_h-1|<=|M-1-2h|*theta<=(M-1)*theta`, we have
`|S_r-r|<=r*(M-1)*theta`. Thus
`|P(a,b)-(a*u+b*v)|<=((a+b)*(M-1))*theta<=M^2*theta`.
Rotating the six sectors gives the same bound for every labeled wall
vertex. Hence `W_theta=conv(wall vertices)` lies in `H_M+B_delta`,
where `delta=M^2*theta`. Steiner's parallel-body formula gives
```math
\operatorname{area}(W_\theta)\le {3\sqrt3\over2}M^2+6M\delta+\pi\delta^2.
```
Since $`a(2N+6M-2)=\operatorname{area}(H_M)`$,

```math
\sigma\le6M^3\theta+\pi M^4\theta^2
\le M^3\theta(6+\pi M\theta)<7M^3\theta\le7/10000<1/1000.
```
Thus the low-slack chart theorem applies.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
In this wall, every side vertex has actual interior angle within (2\theta)
of $`\pi`$; each of the six labeled corners has angle within
(2(M-1)\theta) of (2\pi/3\). Both errors are far below the (0.05)
angle-classification margin above. So side vertices develop with three
incident triangles and corners with two. The developed polygon has exactly
six corners and (M) unit edges on each side, hence is (H_M).
```





**Source formatting excerpt (unbalanced inline math in the original):**

```text
For comparison to the fixed flat (P_M), the anchor edge orientation differs
by at most $`(M-1)\theta`$, the anchor corner by at most (M^2\theta\), and
a vertex of (H_M) is at graph distance at most (2M) from that corner.
The development edge error then gives
```



```math
M^2\theta+2M\big((M-1)\theta+55\sigma\big)
\le1000M^4\theta.
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
This is uniform in (M\) and in the feasible (N)-point cloud on the fixed
specified wall.
```



## Certificate audit and scope corrections

The frozen companion verifier was inspected and rerun. Its JSON matched the
saved certificate byte-for-byte (SHA-256
`1e9e96a72393511200888aa26b8343886ab059d68c531036964137bade2d1cfc`). It
checks five exact sorting examples at (M=4,5,6,8,10), including triangle
areas, acute angles, bounded circumradii, internal Delaunay inequalities,
all source-pair distances, and the stated chart displacement. This is finite
corroboration only; the analytic argument above proves the arbitrary-wall
claim.

The source certificate also prints several `one_deficit_constants`. They
are not part of the promoted theorem: the report explicitly makes no
one-deficit classification, and those finite examples do not prove one.
For a fixed wall, decreasing (z) by one raises the defined $`\sigma`$ by
$`\sqrt3/2`$ relative to the same-wall (z)-count, but the small-slack
hypothesis applies to the actual (z) and says nothing about an arbitrary
lower-population wall whose area has shifted accordingly.

**Verdict: PASS — promote** `C-UNIT-WALL-LOW-SLACK-TRIANGULAR-CHART` and
`C-ARITHMETIC-SIX-WALL-UNIFORM-CHART` only. The arithmetic conclusion is
localization at uniform scale. It does not identify the cloud's sorting
permutation, force a triangle at positive curvature, or resolve the residual
finite-classification/source-extraction obligation.
