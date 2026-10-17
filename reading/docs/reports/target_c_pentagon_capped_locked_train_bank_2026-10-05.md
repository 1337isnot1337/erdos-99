> Generated reading edition · [exact source](../../../docs/reports/target_c_pentagon_capped_locked_train_bank_2026-10-05.md) · source SHA-256 `d8d28cc946bbfeda2c19238ce058cc03f9b286000478003eae3a12e82dce7e89`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0CA6240472B0","canonical":false,"claim_ids":["C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION"],"claim_statuses":{"C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C — frustrated pentagon train banks can still have no wall surplus

Date: 2026-10-05. Research base:
`3c94a1a93641a5f8fa24d43068d487594d3e38cd`, audit.57.
Owned branch: `research/target-c-residual-closure-20261005`.
Classification: **regression, awaiting independent audit**; artifact remains
**unreviewed**. Level I and C-II remain open.
No external literature is imported. The packing bound and wall shield are
canonical inputs; the decorated-source construction is new to this report.

## 1. The proposed coupling tested

```
quadratic actual train crossings + linear long trains
+ disjoint, uniformly direction-frustrated pentagon terminal walls
-> one strict wall-refill spare site
-> canonical contact-minimality contradiction.
```

The first implication is false without additional actual diameter-load or
global-minimizer hypotheses. The family below has all the listed geometry,
positive pinned equilibrium in its quadratic grid interior, and linear
vertex-disjoint long contact returns to distinct boundary pins. Nevertheless
**no bank of actual contact-wall packets has positive aggregate surplus**.
This includes composite walls, not only the separate pentagons.

The boundary pins are not asserted diameter-loaded. The sources are not
asserted global minimum-diameter configurations, do not have a certified
canonical stress, and are not a regression against the full canonical
Target C stack. The result identifies exactly what the proposed geometric
coupling would have to add.

## 2. Explicit capacity-optimal grid

Let M>=24, u=(1,0), a0=sqrt(3)/2, and put

    t=1/(200 M^3),
    delta=2 arctan(t),
    phi=pi/3+delta,
    v=(cos phi,sin phi).

Let

    X={iu+jv: 0<=i,j<=M},
    Q=conv X, N=(M+1)^2.

Canonical `C-LARGE-WALL-LOCK-REGRESSION`, Section 6 of its
[report](target_c_large_near_triangular_fixed_wall_lock_2026-10-05.md),
gives the exact residual

    r=M^2(sin(phi)/a0-1)
      =M^2(cos(delta)-1+sin(delta)/sqrt(3)),
    0<r<1/(100M)<1.

Consequently the finite Oler bound gives

    packing_number(Q) <= floor(N+r)=N.                (1)

The grid itself supplies N points, so this container capacity is exact.
Contacts are precisely the two unit grid directions and the grid is
triangle-free. Each interior vertex has opposite u and v neighbors;
unit coefficients give positive equilibrium. The pinned grid rank is
full by the canonical grid argument. None of this assigns diameter loads
to its boundary vertices.

## 3. Attach separated regular pentagon caps

Select the grid edge indices

    I_M={8+6j: j>=0, 8+6j<=M-9}.

For each selected index attach a regular unit pentagon externally to the
corresponding edge on EACH of the four grid sides. A cap shares exactly
one edge ab with the grid. With w=b-a the oriented unit side and n the
unit outward normal, its cyclic vertices are

    a, b,
    c=b+cos(2pi/5) w+sin(2pi/5) n,
    d=a+(1/2)w+[sin(2pi/5)+sin(pi/5)]n,
    e=a-cos(2pi/5)w+sin(2pi/5)n.                       (2)

All five edges in (2) have length one, all its diagonals have golden-ratio
length >1, and its three new vertices lie outside the grid half-plane.

### Full-source separation

For c and e the outward normal depth is sin(2pi/5)>9/10. Any old grid
point off the supporting boundary row has inward depth at least
sin(phi)>sqrt(3)/2, so its distance to these cap vertices is >1. The
normal depth of d is sin(2pi/5)+sin(pi/5)>1, giving the same conclusion
against every old grid point.

For c against the supporting integer row, b is the unique unit neighbor;
the next row point in the outward tangential direction has squared
distance 2-2cos(2pi/5)>1. Every other row distance is larger. The check
for e is symmetric. The old anchors a,b are already source points.

Every cap vertex is within distance two of its shared-edge midpoint.
On a single grid side, distinct selected midpoints are separated by six.
Across adjacent sides, their distances from the corner are at least
8+1/2; since phi lies between pi/3 and pi/2, resolving along the two
side directions gives midpoint separation at least 8+1/2. Across
opposite sides, perpendicular separation is M sin(phi)>20. Thus every
pair of cap midpoints is separated by at least six, and every pair of
vertices on different caps is separated by more than two. There are
no unintended contacts or cap intersections.

The complete decorated source A_M therefore has

    |A_M|=(M+1)^2+12|I_M|,
    |C(A_M)|=2M(M+1)+16|I_M|.

Its contact graph is exactly the grid plus the regular pentagon cycles,
sharing only their prescribed edge. It is triangle-free. Grid faces are
strict rhombi and every cap is an actual bounded pentagon contact face.

The union P of Q with the caps is a topological disk with a simple outer
unit-contact cycle. Every original grid boundary vertex and every cap
vertex remains on this outer cycle. Thus all new cap vertices are boundary
pins; the entire old interior population is still (M-1)^2 grid vertices.

## 4. Actual wall-disjoint quadratic train bulk

A selected u-edge index i has a complete stopped train through the M
successive grid rhombi along the v direction. Its endpoints are the
regular pentagon caps on the two opposite u sides. Similarly, each
selected v-edge index j gives a complete train in the u direction with
pentagon endpoints on the other two sides.

There are 2|I_M| selected trains. Each pair from opposite families crosses
at exactly one actual rhombus, indexed by (i,j). Hence

    R_selected=|I_M|^2,
    |I_M|=M/6+O(1).

Each train's terminal-edge midpoints are distance exactly M apart. All
selected terminal pentagon walls are source-vertex-disjoint: indices are
six apart on each side and the corner buffers separate different sides.
The source diameter is between M and 2M+4, so these counts are respectively
Omega(D), Omega(D^2), and Omega(D) train length in source coordinates.

The directions of a regular pentagon modulo pi/3 occupy five equally
spaced reduced phases, separated by pi/15. No one reduced phase can cover
all five within any tolerance smaller than pi/30. Thus the selected
terminal faces are uniformly direction-frustrated independently of M
and independently of the vanishing grid angle excess.

There are also |I_M| disjoint actual unit-contact row paths from the
middle of the grid to distinct side pins, each of length at least M/3
for large M. They can be selected on distinct rows and so share no source
vertex. These pins are boundary labels, NOT certified diameter loads.
The new family does not assert the canonical reciprocal train realization.

## 5. No actual contact-wall bank has positive surplus

Let C_1,...,C_b be ANY simple contact cycles in the decorated graph with
disjoint polygon interiors. Let S be the union of their old interior
populations. Take finite unit-separated packets Y_l subset W_(C_l).

Every vertex on the outer cycle of P is incident to the unbounded face
of the contact graph. Such a vertex cannot lie strictly inside any
simple contact cycle: points in its exterior wedge connect to infinity
without crossing the graph and hence cannot be enclosed by that cycle.
Therefore S contains neither original grid boundary vertices nor cap
vertices. All its labels belong to X intersect int(Q).

Every point enclosed by a contact cycle lies in P, since the complement
of P connects to infinity without crossing the graph. By canonical
`C-EMBEDDED-WALL-REFILL`, a packet point is strictly unit-clear from every
old source vertex outside its wall interior, including ALL cap vertices.
But no point inside a regular unit pentagon is strictly unit-clear from
all five of its vertices, by canonical `C-SHORT-WALL-ZERO-CAPACITY`.
Thus no packet point lies in a cap interior. A shared unit edge is also
excluded, since its anchors remain outside the wall interior and every
point on that edge is within one of an anchor. Outer boundary points
cannot lie inside any contact cycle. Consequently all packet points
lie in int(Q).

The simultaneous wall shield makes the entire packet union Y unit-
separated and strictly separated from X\S. Hence

    (X\S) union Y

is a unit-separated packing in Q of cardinality N-|S|+|Y|. Equation (1)
forces

    |Y| <= |S|.                                       (3)

Thus **no choice of actual contact walls, including arbitrary composite
cycles and independently translated compatible packets, produces one
spare point** in this family.

For a stronger non-effective variant, choose phi-pi/3 inside the canonical
uniqueness window of Theorem L.2 for this fixed M. The same decoration and
separation proof applies. In that variant a packet in the outer wall of
P cannot even strictly refill its full (M-1)^2 interior population: it
would give a different full fixed-grid-wall packing, contradicting L.2.
The explicit t above is NOT asserted to lie in that unknown window.

## 6. What the regression changes

This strengthens the pure-grid lock regression by retaining actual
quadratic pentagon-to-pentagon train crossing structure and a linear
bank of definite physical phase frustration. The obstruction is not
removed merely by attaching disjoint frustrated stopping faces or by
combining them into larger contact cycles.

It refutes only implications based on those geometries and boundary
pinning. It does not refute a theorem using actual loaded-return ends,
full-core disk geometry, canonical positive KKT stress, or global
minimum-diameter optimality. In particular many cap vertices have contact
degree two and are NOT certified loaded; canonical unloaded-degree
hypotheses would forbid treating them as a canonical C-II core. This
missing loading premise is explicit, not silently removed.

The closing attack must spend actual diameter-load coupling or move/break
the outer guard vertices. Fixed original contact-wall capacity cannot be
forced from the listed banks alone.

## 7. Certified finite arithmetic

`research/verify_target_c_pentagon_capped_lock_2026_10_05.py` builds the
M=24,30,36 explicit sources. Integer interval arithmetic with denominator
10^24 rigorously bounds sqrt(3), sqrt(5), and the regular-pentagon radicals.
All noncontact pair distances have certified lower bounds >1. The prescribed
contacts have exact length one by the algebraic unit-vector construction;
interval checks also enclose one. The script checks triangle-freeness,
cap support disjointness, contact counts, interior neighbor rosters, selected
crossing cells, cap support radii and midpoint separation. Exact rational
radical bounds verify 0<r<1 and hence the explicit Oler capacity margin.

It does not computationally certify an unknown uniqueness window, actual
diameter loads, full canonical hypotheses, global optimality, or Level I.
The universal no-surplus conclusion is the analytic shield/Oler argument
in Section 5, not a numerical packing search.

## 8. Classification

| Claim | Classification | Scope |
| --- | --- | --- |
| Decorated geometry and no wall surplus | Regression awaiting audit | Actual finite unit-separated sources |
| Quadratic crossings and frustrated disjoint terminals | Regression awaiting audit | Actual contact train banks |
| Canonical loaded/global source with no spare | Not claimed | Load and global-optimality premises are missing |
| Coupled fixed-wall activation using only the listed banks | Rejected formulation | Exact construction above |

No authoritative theorem state, route map or prompt is changed.

## 9. Strengthening: positive equilibrium and full pinned rank on every unpinned vertex

The regression can also satisfy positive equilibrium and full contact
rigidity **after pinning**, including all pentagon vertices. This further
separates arbitrary pinning from actual diameter loading.

Use spacing eight rather than six, with

    I_M={8+8j: j>=0, 8+8j<=M-9}.

For each cap in (2), add four exterior source points. The first three
are the outward radial extensions of c,d,e by unit length:

    c'=c+sin(2pi/5)w+cos(2pi/5)n,
    d'=d+n,
    e'=e-sin(2pi/5)w+cos(2pi/5)n.

The fourth is

    x'=d+(15/17)w+(8/17)n.

Add the four unit bars cc',dd',ee',dx'. All four new vertices are pinned
pendant leaves. There are no other new contacts. Their positions all lie
within distance three of the shared-edge midpoint; spacing eight and
corner buffers give pairwise cap midpoint separation greater than seven.
Different decorated supports are therefore unit-separated. Within one
cap, the extra point x' is strictly farther than one from every vertex
except its prescribed neighbor d: its distance to d' has squared length
306/289>1, and its other cross-pairs are strictly clear. The radical
coordinate construction and certified finite checks below verify this
last local assertion; the formulas are independent of M up to a rigid
motion. All these leaves lie outside Q. The original contact cycles,
bounded physical faces and pentagon-to-pentagon train banks are unchanged.

### Exact positive equilibrium

Set gamma=1/100, C=cos(pi/5), S=sin(pi/5), and

    L1=1,
    L2=1+gamma*(15/17)/C.

Give bc,cd weight L1 and de,ea weight L2. Give the radial bars cc',ee'
weights 2S L1, 2S L2 respectively. Give dx' weight gamma and dd' weight

    S(L1+L2)-gamma*(8/17)>0.

At c and e the two unit pentagon forces have radial resultant of magnitude
2S times their common weight. At d their tangential resultant is
C(L1-L2), canceled by gamma*(15/17); their inward normal resultant is
S(L1+L2), canceled by the two outward pin forces. Thus all three vertices
have exact positive equilibrium. Their degrees are three, four, three.

Remove the two shared anchors a,b from the pin set as well. On each grid
column corresponding to a selected cap pair, give all v-edges weight
sin(2pi/5)L2/sin(phi) on the first anchor column and
sin(2pi/5)L1/sin(phi) on the second. Similarly give u-edges these weights
on the selected cap rows. Other interior-direction weights are one.
Opposite edge weights agree at every grid interior vertex, so its positive
equilibrium remains exact.

The boundary tensions complete the force balance at a,b. Let z be the
inward grid direction at the chosen side, and put z dot w=d_w, where
d_w=+cos(phi) on the bottom and left sides and -cos(phi) on the top and
right sides. In all cases z dot n=-sin(phi). Define

    beta_a=sin(2pi/5)L2/sin(phi),
    beta_b=sin(2pi/5)L1/sin(phi),
    N_a=beta_a d_w-L2 cos(2pi/5),
    N_b=beta_b d_w+L1 cos(2pi/5).

Give ab weight two, the preceding boundary contact at a weight 2+N_a,
and the following boundary contact at b weight 2-N_b. They are positive
throughout this near-triangular family. Normal components cancel by the
choice of beta; tangential components cancel by the two boundary tensions.
Spacing prevents these assignments from colliding. Every unpinned source
vertex now has degree at least three and strictly positive contact
equilibrium. The remaining pins are the unselected old grid-boundary
vertices and the four exterior leaves of every cap.

### Full pinned contact rank

Let an infinitesimal contact flex vanish at all those pins. Each grid
row fixes its u-projection along that row, and each grid column fixes its
v-projection along that column. Pinned corners imply u-projection zero
on the two horizontal boundary rows and v-projection zero on the two
oblique boundary columns. Hence a shared anchor can move only normally
to its supporting grid side.

The two fixed pin neighbors d',x' give two independent bar directions
at d, forcing its velocity to zero. At c, its fixed pin c' and now-fixed
neighbor d give two independent directions; c is fixed. The same argument
fixes e. The bc and ea contacts have nonzero normal components and then
fix the normally moving anchors b,a. Thus every old grid-boundary vertex
is fixed. Propagation along grid rows and columns fixes every interior
vertex as well. There is no nonzero pinned contact flex.

This proves full rank on all unpinned coordinates, without treating a pin
as an actual diameter endpoint or importing generic rigidity.

### Capacity is still unavailable

Every newly added edge is a pendant bridge to a pinned leaf. It creates
no new contact cycle and no new bounded face. All old outer-cycle vertices
remain incident to the unbounded face. Therefore every contact-wall packet
still lies inside Q and all its removed interior labels still belong to
X intersect int(Q). Section 5 applies verbatim: no actual contact-wall
bank has positive surplus. The added exterior pins are never silently
counted as interior population.

This stronger regression has positive equilibrium at every unpinned
vertex, minimum unpinned degree three, full pinned rank, definite pentagon
frustration and quadratic complete train crossings. It still has no
certified actual diameter loads. The prescribed pin set contains many
vertices that are not extreme vertices of its convex hull, which prevents
it from being identified with the canonical loaded set. Thus actual
loaded extremality and diameter reaction balance remain substantive
missing premises, even after these local rank/equilibrium conditions
are added.

The verifier includes M=32,40 instances of this radial-pin variant. The
contacts are exact by the unit-vector formulas, all other pair distances
are rigorously >1, and interval enclosures are consistent with the exact
analytic force identities above. The universal pinned-rank assertion is
proved above; it is not inferred from a numerically computed rank.

## 10. Actual loading fails by an unbounded hull-population deficit

The absence of actual loads is quantitative. In the radial-pin variant,
the convex hull of the entire source has at most 60 extreme vertices,
independently of M and of the number of selected caps. In the original
variant it has at most 28. Consequently neither family with M>60 can
satisfy the canonical diameter population bound h>=ceil(D), even if one
is allowed to choose a different subset of its existing vertices as loads.
This is a proved finite limitation of the regression, not a source
exclusion theorem for general C-II configurations.

To prove the counts, fix one grid side and its oriented frame w,n. Each
cap contributes a translate of the same finite set T of new vertices:
|T|=3 in the original variant and |T|=7 in the radial-pin variant. All
translation vectors lie on a line parallel to w. The convex hull of
their union is therefore

    conv(T)+[a_min,a_max]w.

Indeed a convex combination of translated template points belongs to this
Minkowski sum. Conversely, each endpoint translate of conv(T) belongs to
the hull of the actual template copies, and their convex hull is the sum.
Its extreme vertices are among the two endpoint translates of T, so there
are at most 2|T|. This argument also applies when a side has just one cap;
an empty side contributes nothing. The grid itself has just four extreme
vertices. The convex hull of a union of finitely many polygons has extreme
vertices among their extreme vertices. Summing over the four sides gives

    4+4*(2*3)=28,       4+4*(2*7)=60.

Every endpoint of an actual diameter pair is an extreme vertex of the
whole source hull. For completeness, if p is a nontrivial convex
combination of distinct source points p_i and |p-q|=D, strict convexity
of squared Euclidean norm gives

    |p-q|^2 < sum_i lambda_i |p_i-q|^2 <= D^2,

a contradiction. Thus any hypothetical canonical loaded set on the
radial-pin source would have q<=60. Canonical Woodall topology gives
h<=q, whereas the canonical core ledger gives h>=ceil(D). The grid has
two source points M apart, so D>=M. For M>60 these inequalities contradict
one another. The original family similarly fails for M>28.

Adding further caps or translating the existing templates along the same
four straight sides cannot repair this deficit. A completion into a
canonical source must change the hull geometry or add genuinely new
extreme source vertices. This proof does not show that such a completion
is impossible, nor that it preserves the fixed-wall capacity lock. In
particular the capacity regression does not test the canonical linear
population of actual loaded endpoints or its coupling to returning trains.
