> Generated reading edition · [exact source](../../../docs/reports/target_c_disjoint_attachment_cell_square_root_count_2026-10-09.md) · source SHA-256 `89b840f869d135f3ce509f8e248ce5a74c829d1aa15cbcefe5e12d54d115dced`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-984C1F3D5D1E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Disjoint attachment cells give a square-root harmonic-component count

Date: 2026-10-09. Base:
`0a71e1141c5af3b644dad858d584494556f55c5e`, state
`2026-10-09.audit.181`.

Classification: **proved candidate awaiting independent audit/promotion**.
Lifecycle: unreviewed. Canonical theorem state is unchanged.

## 1. Exact implication and dependencies

```text
uniform minimum width of every harmonic attachment cell
  + canonical interior disjointness of these actual cells
  -> a linear curvature-window count N_M=O(M+2)
  + canonical sum of harmonic graph diameters = O(D)
  -> c_I=O(sqrt(D)) in every canonical C-II branch.
```

The new bridge is the use of Section 83's actual cell disjointness
inside Section 75's finite curvature-window argument. Section 75
used an attachment occurrence count and obtained `N_M=O((M+2)^2)`;
it did not use this later disjoint-cell geometry.

Canonical dependencies are Section 62's trapping and graph-diameter
budget, Section 75's degree/strip and fat-force-hull lemmas, and
Section 83's interior-disjointness theorem. No selected-grid
embedding, KKT coefficient floor, or uniform stress radius is used.
All contact-isolated source labels remain in the full source.

## 2. A curvature budget for disjoint polygons on one convex arc

**Lemma 2.1.** Let `f` be a concave piecewise affine function on an
interval of horizontal length X, with total slope drop V. Inside
the cap between its graph and its endpoint chord, take any family
of pairwise interior-disjoint convex polygons whose vertices lie
on that graph. If each polygon has minimum width at least w,
their number is at most

```math
 \boxed{12XV/w.} \tag{2.1}
```

Constants are deliberately unoptimized. The statement allows shared
vertices or boundary chords. It is about actual planar convex cells,
not independently chosen abstract attachment lists.

### 2.1 Choose one substantial triangle per polygon

Choose a maximum-area vertex triangle T inside a given polygon Q.
For any `x in Q`, write its barycentric coefficients relative to
T as `lambda_i`. Replacing T's ith vertex by x multiplies its
oriented area by `lambda_i`; maximality implies `|lambda_i|<=1`.
Thus `lambda_i>=-1`, so Q lies in the triangle obtained from T
by a homothety of factor four about its centroid. Consequently
`minwidth(T)>=minwidth(Q)/4>=w/4`.

For a triangle of largest side a, area A, and semiperimeter s,
its minimum width is `2A/a` and its inradius is `A/s`.
Since `2s/a<=3`, its inradius is at least one third of its
minimum width. Our selected T therefore has inradius at least
`w/12`. Selected triangles have disjoint interiors because the
original polygons do.

### 2.2 Total triangle inradius is controlled by graph curvature

Extend the selected triangles to a triangulation of the cap polygon,
adding graph vertices when necessary. Noncrossing diagonals can be
completed to such a triangulation. No graph vertex is strictly
inside a selected triangle: all vertices lie on the same convex
boundary arc. Collinear redundant graph vertices may be omitted.

Root the triangulation at the endpoint chord. Every triangle has
ordered horizontal coordinates `a<b<c`, with root base `[a,c]`
and split vertex b; its two child caps lie on `[a,b]` and `[b,c]`.
Put `l1=b-a`, `l2=c-b`, and let `s1,s2` be the two graph
secant slopes. Concavity gives `s1>=s2`. The triangle area is
`l1*l2*(s1-s2)/2`; its perimeter is at least `2(l1+l2)`.
Its inradius therefore satisfies

```math
 r_T\le\tfrac12\min(l_1,l_2)(s_1-s_2). \tag{2.2}
```

Let `mu=-f''` be the nonnegative slope-drop measure. Direct
integration of the two secants gives

```math
 s_1-s_2=\int g_{a,b,c}(t)\,d\mu(t),
\quad
 g_{a,b,c}(t)=
 \begin{cases}
 (t-a)/(b-a),&a\le t\le b,\\
 (c-t)/(c-b),&b\le t\le c,\\
 0,&\text{otherwise}.
 \end{cases} \tag{2.3}
```

The two formulas agree at b; its curvature atom is integrated
once, not twice. For a fixed t, nonzero kernels occur along one
root-to-leaf chain, ending if t is a split vertex. At a node on
that chain, `min(l1,l2)` is at most the amount by which the
horizontal interval shortens upon entering the child containing t.
These charges telescope. If the chain ends at a split vertex,
its final charge is bounded by the remaining interval length.
Since each kernel is between zero and one,

```math
 \sum_T\min(l_1,l_2)g_{a,b,c}(t)\le X.
```

Integrating and using (2.2) shows
`sum_T r_T<=XV/2<=XV`. In particular the selected triangles
of inradius at least `w/12` number at most `12XV/w`.
This proves (2.1). The argument accounts for nested chord intervals
through the triangulation tree; it does not assume their spans are
pairwise disjoint. QED.

## 3. Every actual harmonic cell has minimum width at least one half

Let `I_r` be a nonempty unloaded positive-contact component, let
`A_r subset B` be its distinct actual loaded attachments, and
`P_r=conv(A_r)` its harmonic cell. Choose `x in I_r`. Its
positive-contact degree is at least three. All contact neighbors
belong to `I_r union A_r`, hence all belong to P_r by harmonic
trapping. These are actual mutually unit-separated source points.

Canonical Lemma 75.1 says that x and three unit neighbors cannot
fit in a strip of width strictly less than `1/2`. Therefore

```math
 \boxed{\operatorname{minwidth}(P_r)\ge1/2.} \tag{3.1}
```

This includes singleton components. It does not bound contact
isolates, which are not these harmonic components.

## 4. Replace the quadratic curvature-window population by a linear one

For sufficiently large canonical C-II sources, Section 75 gives,
about the source circumcenter o,

```math
 B(o,D/20)\subset F\subset B(o,11D/20).
```

Let `delta_r` be the graph diameter of I_r, and let
`N_M=#{r:delta_r<=M}`, with integer `M>=0`. Put `L=M+2`.
Harmonic trapping gives `diam(A_r)<=L`. The following improvement
holds uniformly in M:

```math
 \boxed{N_M\le12,000,000\pi\,(M+2).} \tag{4.1}
```

**Proof.** If `L>D/10^6`, the elementary attachment incidence
bound `N_M<=q<=pi D` proves (4.1). Suppose `L<=D/10^6`.
For every counted cell choose a representative `b in A_r`.
The local arc argument in Section 75, which applies already when
`L<=D/10000`, puts every other attachment within boundary
arclength `w0=22L` of b, in either direction.

Partition the convex force-hull boundary into equal arclength blocks
of length ell in `[w0,2w0]`. This is possible by taking
`floor(per(F)/w0)` blocks; the inner disk makes that number
large in the present small-L regime. Extend each block by w0
on both sides. Its resulting arc has length at most `4w0=88L`.
Assign each representative to its original block. Every attachment
of that assigned cell lies in the expanded arc.

Each expanded arc is a graph with a uniformly bounded slope. To
check this at corners as well as sides, choose a radial unit vector
e at one point of the arc. Its polar-angle variation along the arc
is at most `88L/(D/20)<=1760/10^6`. Every outward supporting
normal n at every arc point obeys
`n dot (p/|p|)>=1/11` by the fat-hull disk bounds. Hence
`n dot e>1/22`. In coordinates `x=Je`, `y=e`, tangent
projection is strictly positive, and the boundary is a concave
graph with `|f'|<=22`. Its total slope drop is at most
`485*Theta`, where Theta is the arc's actual exterior turning:
the derivative of the slope tangent function is bounded by
`1+22^2=485`, including its jumps at vertices.

The assigned cells have disjoint interiors by canonical Section 83,
have all vertices on this same convex arc, and have minimum width
at least `1/2` by (3.1). Lemma 2.1, with horizontal span at
most `88L`, bounds their number by

```math
 24\,(88L)\,(485\Theta)=1,024,320L\Theta.
```

The expanded arcs cover each boundary point at most five times,
including possible curvature atoms at cut endpoints: original
blocks have length at least w0 and only a w0 margin is added at
either end. Thus their total exterior turning is at most `10pi`.
Summing bounds N_M by `10,243,200pi L`, which is below the
constant in (4.1). All representatives are assigned once. QED.

The proof uses no area-disjointness of *normal windows*. The actual
cell polygons are disjoint, and the triangulation curvature lemma
handles all overlaps of their attachment spans inside one window.

## 5. Square-root count in both global C-II branches

**Theorem 5.1 (proved candidate awaiting independent audit/promotion).**
For every sufficiently large canonical C-II source,

```math
 \boxed{c_I=O(\sqrt D).} \tag{5.1}
```

**Proof.** The canonical graph-diameter budget used in Section 75
bounds the number of components with `delta_r>=M+1` by
`(2+2pi D)/(M+1)`. Combining it with (4.1) gives

```math
 c_I\le12,000,000\pi(M+2)+{2+2\pi D\over M+1}.
```

Choose `M=floor(sqrt D)`. The bound is `O(sqrt D)` with an
absolute, deliberately coarse constant. It applies in both the
macroscopic-container and full-core alternatives. QED.

In the exact pinned ledger this sharpens the error term to

```math
 \mu_D=q+m-k-2c_I-4=q+m-k-O(\sqrt D),
```

where `m` counts nonunit sides of the actual loaded hull and
`k=d_H+s_Z`. No inequality `g_A<=C c_I` is established here;
the stronger population reserve in the separate conflict-deletion
report cannot be treated as component payment without that bridge.

## 6. Audit boundary and remaining goal

The new step to audit is Lemma 2.1 and its local graph application.
It retains nested triangulation intervals, all curvature atoms,
shared cell vertices, and the actual attachment-cell geometry.
The full force-hull fatness and the degree/trapping/diameter budgets
are canonical premises; they have not been inferred from a scaffold.

The new error is below the candidate `D^(2/3)` population reserve,
but the canonical shell/face allowance is still linear in D. No
global residual payment, source-compatible finite endpoint, unit
triangle in every minimizer, C-II closure, or Level I solution has
been obtained. No finite computation is claimed as a certificate
of these universal geometric estimates.

LEVEL I STATUS: STILL OPEN.
