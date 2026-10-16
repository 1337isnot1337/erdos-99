<!-- theorem-state: {"artifact_id":"ART-4623F8727B01","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: a weak pivot forces macroscopic axial pressure

```text
weak-pivot hull sides + actual diameter rails -> axial cut pressure Omega(D)
 -> a strict competitor if that pressure can be proved o(D);
actual complete-grid equilibrium -> any pressure jump is exterior contact stress.
The pressure-spreading shortcut is false for the encoded diameter/cut data.
Actual exterior load transmission remains the bridge to C-II and Level I.
```

**Date:** 2026-10-02.
**Starting checkout:** `539f5187b3cac9287f6b30cdf6b36aafb1763c5a`.
**Research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
**Continuation base:** `d4552892e0b136157cf1938dc7bfd1b5d4739e94`.
**State:** `2026-09-14.audit.51`.
**Owned branch:** `swarm/sol/threshold-global-moment-20261002`.
**Mission:** actual four-host geometry behind the cross-shore correction force.
**Classification:** proved candidates awaiting independent audit/promotion;
conditional threshold application; exact regression against pressure spreading.
Artifact lifecycle is unreviewed. **Level I OPEN; C-I CLOSED; C-II OPEN.**

## 1. Authority and dependency scopes

The state lock, theorem manifest, Target C route and current-frontier files are
byte-identical to the research base. No canonical state or prompt is changed. Metadata regeneration also registers
five already-existing unpromoted artifacts on the continuation base; their
mathematical text and authority are unchanged.
The canonical quantity is the actual normalized KKT contact-cut reaction, with
all source points retained. [Theory 01, Theorem 4.1](../theory/01-local-structure.md)
supplies vertex equilibrium, `sum beta=1`, and the contact stress trace `D^2`.
Its Lemma 5.1 supplies extremality of actual diameter endpoints.

The finite theorem below states its boundary/layer hypotheses explicitly. It
does not require global optimality, a stress kernel, or an unproved attachment
of diameter endpoints to grid vertices. Its threshold application is conditional
on the unpromoted [paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md),
[transverse rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md)
and [four-host theorem](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md).

The earlier [weak-packet report](target_c_weak_packet_correction_mass_2026-10-02.md)
supplies the finite weak-pair estimates, re-used in Section 3. The needed
strip-capacity proof from [PR #613's report](target_c_threshold_rail_deep_attachment_2026-10-02.md)
is short and rederived in Section 4; its population claims are not imported.

PR #618 at exact head `9e042ddb7144cbc2f47baac0fa63e9a8ac316761` was inspected,
including the midpoint lens bound, the short-chord hull-side argument, and the
internal-layer localization. Its [packet reaction report](https://github.com/1337isnot1337/e-99/blob/9e042ddb7144cbc2f47baac0fa63e9a8ac316761/docs/reports/target_c_threshold_packet_reaction_floor_2026-10-02.md),
Sections 4--6, is an **unpromoted** dependency only for producing the two hull
sides and their adjacent pivot from a subunit pair in a global threshold source.
It uses canonical [FS.1](../targets/target-c/58-full-source-geometry-audit.md).
The theorem below assumes the precise resulting geometry rather than promoting
that PR or silently treating its entire report as canonical.

No literature theorem or numerical optimizer is used. The only imported
geometric facts are elementary and are proved at the point of use below.

## 2. Exact finite hypotheses

Let `P` be a finite unit-separated source of diameter `D>=3`, with actual
diameter `za` of vector `Du`. Write `e=Ju` and split the source-hull boundary
at `z,a` into the lower and upper arcs `L,U`, both directed from `z` to `a`.
Thus every point on the open `L` arc has negative `e` coordinate relative to
the line `za`; every point on open `U` has positive coordinate. Both arcs have
strictly increasing `u` projection. To see the latter, take `z=(0,0),a=(D,0)`:
the two radius-`D` bounds force every other source point into `0<x<D`, and
the two arcs of a convex hull between its unique projection extrema are
graphs over that projection.

Let integer boundary labels `lambda_A in {0,...,m}` be nondecreasing on both
arcs, with `lambda_A(z)=0, lambda_A(a)=m`. Require `m>=7` and at least one
actual diameter endpoint on **each** arc in every internal layer
`j=1,...,m-1`. Let `lambda_B in {0,...,n}` satisfy

\[
0<\lambda_A(x)<m\Longrightarrow
\begin{cases}
\lambda_B(x)=0,&x\in L,\\
\lambda_B(x)=n,&x\in U.
\end{cases} \tag{H1}
\]

These are the exact rail/four-host consequences, without identifying endpoints
with contact ports. In particular no value of `lambda_B` on extreme A-layers
is prescribed.

For an **internal** pivot `2<=r<=m-1`, require four distinct actual diameter
endpoints `L_a,L_b on L`, `U_a,U_b on U`, with A-layers `r-1,r` on each arc.
The chords `L_a L_b` and `U_a U_b` must be sides of the full source hull, of
length at most `3/2`. Require actual diameter vectors

\[
R_p=U_b-L_a=d_pu+q_pe,\qquad
R_n=L_b-U_a=d_nu-q_ne,\qquad q_p,q_n>0. \tag{H2}
\]

Let actual diameter coefficients `beta_h>=0` sum to one. Choose positive
subcoefficients `w_p<=beta_p,w_n<=beta_n` with

\[
w_pq_p=w_nq_n,\qquad
M=w_p+w_n,\qquad
\rho={w_pd_p+w_nd_n\over M}<1,\qquad d_p+d_n\ge0. \tag{H3}
\]

For any one B-cut `k`, orient its crossing diameters from B-layer below `k`
to B-layer at least `k`, and assume the **actual cut equation**

\[
F_k=\sum_{h\text{ crossing }k}\beta_h\widehat R_h=C_kv,
\quad C_k\ge0,\quad v=cu+se,\quad c\ne0,\ s>0,
\quad c^2+s^2=1. \tag{H4}
\]

It is enough to assume (H4) algebraically for the finite bound. In its source
application it follows by summing vertex KKT when every unit contact crossed
by this actual train cut has oriented vector `v`. Define

\[
Q=\sqrt{D^2-9/4},\qquad T={s\over|c|},\qquad
\ell={ (m+1)^2\over256(D+m+1)}. \tag{1}
\]

Let `N` be the total coefficient of A-pivot-empty diameters and put

\[
A_r=\sum_{h\text{ crossing pivot }r}\beta_h
             (R_h^{A}\cdot u), \tag{2}
\]

where `R_h^A` points from the lower A-layer to the higher one. If the pivot
is an actual unit-contact train cut, (2) equals its total contact stress by
the exact KKT cut law. No full-source stress kernel is assumed.

## 3. Hull-side isolation of the weak pivot

The weak-pair estimates give

\[
{1\over2}-{1\over4D^2}<d_p,d_n<{3\over2},\qquad
q_p,q_n\ge Q. \tag{3}
\]

Here is the additional positivity check, since absolute component bounds alone
would not suffice. In the earlier report's angle notation
`A=(theta+psi)/2`, `t=(theta-psi)/2` and
`kappa=sqrt(1-1/(4D^2))`, one has
`D cos A>=kappa`, `cos t>kappa`, `D|sin t|<1/2`, and

\[
d_p=D\cos A\cos t-D\sin A\sin t,\qquad
d_n=D\cos A\cos t+D\sin A\sin t.
\]

Each first term exceeds `kappa^2`, and each absolute second term is below
`1/2`. This proves the lower bound in (3). The upper bound and the `Q`
bound were proved in the weak-packet report. In particular, **both** weak
lower-layer endpoints have smaller `u` projection than **both** upper-layer
endpoints. The other two comparisons follow from monotone projection on
each hull arc.

### Lemma 1 — at most one diameter misses the pivot

Every actual diameter crosses the A-pivot except possibly

\[
L_aU_a\quad\text{or}\quad L_bU_b, \tag{4}
\]

and both exceptions cannot occur. Every pivot-crossing diameter has strictly
positive A-oriented `u` component. A possible exceptional diameter crosses
**every** B-cut, with positive `e` component at least `Q` and absolute `u`
component below `3/2`.

Proof. Actual diameter endpoints are extreme. Two vertex-disjoint diameter
chords in a convex hull must cross: if their four endpoints were in the
nonalternating order `x,y,z,w`, the intersecting diagonals `xz,yw` and their
intersection `o` would give
`|xy|+|zw|<|xz|+|yw|<=2D`, contradicting `|xy|=|zw|=D`.

The two weak hull sides have no source vertices between their endpoints.
They separate the boundary vertices into one closed left arc, from `U_a`
through `z` to `L_a`, and one right arc, from `L_b` through `a` to `U_b`.
Monotone layer order makes these exactly the two sides of the pivot cut.
A diameter lying entirely on the left cannot cross either weak diameter.
It must share an endpoint with each, forcing `L_aU_a`. The same argument
on the right forces `L_bU_b`. The two candidates are disjoint noncrossing
chords, so cannot both be diameters.

For a diameter joining the two sides of the cut, monotone projection on its
endpoint arcs bounds its A-oriented `u` component below by one of
`d_p,d_n,(L_b-L_a).u,(U_b-U_a).u`, all strictly positive.

An exceptional side joins internal L/U layers, hence B-layers `0,n` by (H1).
Its B orientation is L to U. Write `X=L_b-L_a`. Then
`(U_a-L_a).u=X.u-d_n`, with both `X.u,d_n` in `(0,3/2)`.
Likewise `(U_b-L_b).u=d_p-X.u` lies in `(-3/2,3/2)`.
Length `D` now gives the claimed transverse bound. This proves the lemma.

### Lemma 2 — negative transverse B-force spans the whole A shore

Every B-crossing diameter whose B-oriented `e` component is negative has
A-endpoint levels `0,m`.

Proof. A diameter disjoint from `za` crosses it by the preceding crossing
fact, and therefore joins L and U. If either endpoint has internal A-layer,
(H1) forces its B orientation to be L to U whenever it crosses the chosen
B-cut, giving a positive `e` component. If it shares `z` or `a` with the
reference diameter, an internal L-endpoint has B-layer `0` and lies below
the reference line; its B-crossing orientation toward the reference endpoint
again has positive `e` component. The internal U case is the reverse and
also positive. The reference diameter has zero transverse component.

Thus both endpoints of a negative row have extreme A-layers. They cannot
have the same A-layer: Lemma 1 would make it one of (4), whose endpoints
instead have internal layers and whose B transverse component is positive.
They consequently have levels `0,m`. Notice that no near-circular angle
estimate or lower bound on an individual multiplier was used.

## 4. A full-span diameter has macroscopic axial component

### Lemma 3 — endpoint strip capacity and its use here

A strip of width `t` contains at most

\[
4\sqrt{2Dt}+4t+4 \tag{5}
\]

actual diameter endpoints of a unit-separated diameter-`D` source. A set of
`b>=8` such endpoints therefore has minimum strip width strictly exceeding
`b^2/[256(D+b)]`.

Proof, following and rederiving the scoped PR #613 lemma. Measure along the
strip and let `x_0,x_1` be the extrema of the selected endpoints. For an
endpoint `q` at coordinate `x`, interpolate `q_*` between extrema with the
same coordinate, so `|q-q_*|<=t`. For a diameter partner `p` of `q`, the
weighted-square identity and the two partner distance bounds give

\[
(x-x_0)(x_1-x)\le D^2-|p-q_*|^2\le2Dt.
\]

Consequently all projections lie within `sqrt(2Dt)` of one of the two
extrema. Each group lies in a rectangle of sides `sqrt(2Dt),t`. All its
points are vertices of its convex hull, because each is an extreme source
vertex. Their unit-separated cyclic hull edges give cardinality at most
the rectangle's perimeter, with an extra two for groups of size at most two.
This proves (5). Substitution of `t<=b^2/[256(D+b)]` into (5) gives at most
`(sqrt(2)/4+1/64)b+4<b` for `b>=8`, a contradiction.

Now let `xy` be **any** diameter with A-levels `0,m`, oriented from `x` to
`y`. Its axial component obeys

\[
\boxed{(y-x)\cdot u>\ell.} \tag{6}
\]

Choose an endpoint on each internal layer `j<r` on the arc containing `x`,
and on each layer `j>=r` on the arc containing `y`. (If `x` or `y` is a
reference endpoint, either arc can be used.) The first group lies between
`x` and that arc's left weak vertex; the second lies between that arc's
right weak vertex and `y`. By (3) and same-arc monotonicity, both left weak
vertices project before both right weak vertices. Hence **all** the chosen
internal endpoints, together with `x,y`, lie in the strip of `u` projection
width `(y-x).u`. These are `m+1` distinct actual diameter endpoints, one
per distinct layer. Apply (5) with strip normal `u` and `b=m+1`. This is a
strip of actual endpoints, not a strip of lattice markers or contact ports.

## 5. Axial pressure theorem

Under (H1)--(H4),

\[
\boxed{
A_r\ \ge\
{Q M+(Q-\tfrac32 T)N\over T+D/\ell}.
} \tag{7}
\]

Proof. Put `b_-` equal to the total coefficient of negative-transverse
B-crossing diameters. Lemmas 1--3 and positivity of all pivot axial
components give

\[
b_-\le A_r/\ell,
\qquad |F_k\cdot u|\le A_r+\tfrac32 N. \tag{8}
\]

The first inequality uses actual full-span support. The second allows either
B orientation for a pivot-crossing bar and bounds its absolute longitudinal
component by the positive A-oriented one. The sole possible empty side is
handled by Lemma 1. Thus the formal assignment of a macroscopic oblique
corrector to an A-empty row is geometrically unavailable.

The selected weak coefficients contribute at least `QM` to `F_k.e`; the
possible empty side contributes at least `QN`. All negative rows together
contribute no less than `-Db_-`; other rows contribute nonnegatively. Hence

\[
Q(M+N)\le F_k\cdot e+Db_-
=T|F_k\cdot u|+Db_-
\le(T+D/\ell)A_r+\tfrac32 TN.
\]

This is (7). It does not count a reused correcting diameter once per B-cut.

For a sequence with `m>=c_*D+o(D)`, `M+N>=delta>0`, and projective shore
angle `pi/3+O(1/D)`, (7) gives

\[
\boxed{
\liminf {A_r\over D}\ge
{\delta\over\sqrt3+256(1+c_*)/c_*^2}>0.
} \tag{8a}
\]

Thus a source theorem giving `A_r=o(D)` in this weak-mass subbranch would
exclude it. Neither such a bound nor a universal floor on `M` is claimed.
Boundary pivots and sources without a weak pair are outside this theorem.

## 6. A tested next step: pressure does not automatically spread

The attempted repair was to infer an order-`D` axial reaction on a positive
fraction of A-cuts from (7), actual rail occupancy and the paired staircase.
It fails for those data alone. The exact certificate gives rational sources
with the following simultaneous properties:

- every point is a source-hull vertex, every pair is strictly longer than one
  and at most the actual diameter `D`;
- the two weak same-arc hull sides have length `1+t^2>1`, the weak reaction
  is `1-t^2<1`, and their endpoints are in internal layers;
- actual internal rail endpoints occur on both arcs in every layer;
- the A transverse graph is a connected paired antitone tree, hence its
  derivative rank is exactly `m`;
- all actual diameter weights are positive and sum to one; every formal
  A-cut has a positive axial resultant and every repeated B-cut has a
  positive resultant parallel to the same rational `v`;
- weak mass exceeds `2/5`, while the pivot reaction exceeds `D/3` and all
  other A reactions are less than `D^-2`.

This refutes pressure spreading **from the listed data**. It is not a source
KKT counterexample: there are **no actual unit contacts**, the A/B cuts are
boundary-label cut equations, and B transverse rank is one rather than the
rank required for a long exact-phase B shore. Vertex equilibrium, actual
train realization, mixed stress/PSD and global optimality are omitted.
For the certified cases a unit line with the same cardinality has smaller
diameter. Nothing here constructs triangle-free global minimizers.

### Exact construction and force calculation

Set `t=1/k` and

\[
D={(1+t^2)^2\over4t},\quad d=1-t^2,\quad q=D-2t,\quad a=2t,
\quad o=(0,a/2).
\]

Use the four weak points
`(-d/2,-q/2),(d/2,q/2),(-d/2,q/2+a),(d/2,-q/2+a)` and reference
`o+(-D/2,0),o+(D/2,0)`. Their weak diameters have vectors `(d,q),(d,-q)`,
their short sides have length `1+t^2`, and one other vertical pair has
length `D`. These identities are exact.

Add two asymmetric antipodal circle diameters through `o`, with A-oriented
unit vectors

\[
n_1=(24/25,7/25),\qquad n_2=(5/13,-12/13).
\]

Give both the same adjacent pivot support as the weak bars. With
`f_1=(12/13)/(7/25+12/13)` and `f_2=1-f_1`, their A transverse forces
cancel. Their B-oriented export per unit mass is `D(x_p,y_p)` with

\[
x_p=f_1(24/25)-f_2(5/13),\qquad
y_p=f_1(7/25)+f_2(12/13).
\]

For `v=(8/17,15/17)=(c,s)` one has `s x_p-c y_p>0`. Mix these bars with
the weak balanced pair; both packets lie at the same short A interval.

For the other layers use actual antipodal circle points with rational unit
vectors `(2h/(1+h^2),(1-h^2)/(1+h^2))`,
`h=4/5+4j/D`, `1<=j<=2P`, `P=floor(D/1000)`. The script assigns their
lower/upper endpoints monotonically to a double-star staircase with
`r=P+2`, `m=2P+2`. A further circle pair in directions
`(9999/10001,+/-200/10001)` supplies the full-span transverse tree edge.
All these other diameter coefficients, including the reference and possible
empty side, equal `eta=1/(100D^4)`.

Write their total mass as `b_0` and B-resultant as `(X_0,Y_0)`. Choose
strong packet mass `G` and weak mass `M` by

\[
G={c q(1-b_0)+cY_0-sX_0\over D(sx_p-cy_p)+cq},
\qquad M=1-b_0-G. \tag{9}
\]

Then the B-cut equation is exact. Each A tree edge has balanced transverse
flow, so all A equations are exact as well. The pivot includes the strong
packet's order-`D` axial reaction. Every other cut sees only the tiny
coefficients. The finite verifier checks **all** source distances, full hull
adjacency, every actual diameter, positivity, all layer orders, rail occupancy,
tree connectivity/pairing, every A vector equation, the B vector equation,
and the bounds stated above. It certifies three finite regressions; it does
not assert an unbounded globally optimal family or import omitted source
hypotheses from numerical survival.

## 7. The repaired actual-grid statement: pressure jumps are exterior

### Lemma 4 — longitudinal stress is constant through a complete grid

Suppose an actual source contains an affine unit grid

\[
p_{ij}=p_{00}+iu+jv,\quad0\le i\le a,\quad0\le j\le b,
\quad\pi/3<\angle(u,v)<2\pi/3.
\]

At each interior vertex, the four displayed grid neighbors exhaust its unit
contacts. Indeed a new unit neighbor would need angular separation at least
`pi/3` from each of the four. Every gap in this four-direction star is less
than `2pi/3`, so such a neighbor cannot fit. The vertex is inside the convex
hull of its displayed neighbors and cannot be an actual diameter endpoint.
Its KKT contact equilibrium is consequently

\[
(\alpha_{i,j}^{u}-\alpha_{i-1,j}^{u})u+
(\alpha_{i,j}^{v}-\alpha_{i,j-1}^{v})v=0.
\]

Linear independence gives equality of the two opposite u stresses and of
the two opposite v stresses. Thus on each internal grid row `j=1,...,b-1`,
all `a` u-edge coefficients are one common value `g_j`.

If actual A-train cuts cross the consecutive u columns of this grid, let

\[
G_A=\sum_{j=1}^{b-1}g_j.
\]

Every such cut has **exactly the same** internal-grid stress contribution
`G_A`. Its full cut reaction satisfies

\[
C_i=G_A+E_i,\quad E_i\ge0,
\qquad G_A\le\min_i C_i,
\qquad aG_A\le D^2. \tag{10}
\]

The remainder `E_i` includes all other crossed contacts, including boundary
grid rows. The trace bound in (10) counts actual distinct grid edges.

Combining (7) with (10), a pivot column of such a grid obeys

\[
\boxed{
E_r\ge {QM+(Q-\tfrac32 T)N\over T+D/\ell}-\min_i C_i.
} \tag{11}
\]

The exact difference `C_i-C_j=E_i-E_j` also holds. If the axial pressure is
concentrated as in Section 6 and an actual grid is realized, its common grid
stress is tiny and its macroscopic pivot load must travel through exterior
contacts. This is a source consequence, not an assertion that the formal
regression realizes those contacts.

The next attempted inference, that the macroscopic pivot reaction itself
forces a fixed positive share of stress into grid edges, therefore does not
follow from equilibrium at the four-contact grid vertices. Equation (10)
provides an upper bound by the minimum cut reaction. Positivity alone does
not provide a quantitative lower bound. Nearly zero coefficients cannot be
replaced by zero coefficients for a finite-release argument.

## 8. Computation, remaining bridge, and Level I accounting

Run [the exact verifier](../../research/verify_weak_pivot_pressure_2026_10_02.py).
It also checks a 48-point actual oblique grid, all 82 contacts, absence of
other contacts and every interior vector balance for rational row/column
stresses. Its prescribed boundary loads are not claimed to arise from actual
diameter equilibrium. B-rank and actual contact-cut realization remain
explicit omissions in the pressure-spreading regression.

The useful new quantity is an actual pivot stress of order `D`, forced by a
weak internal packet of fixed normalized mass. The repaired continuation is
to rule out or finitely release the **exterior contact load** in (11), or to
obtain a source-specific lower bound on the actual grid contribution. Actual
near-unit blockers and positive but arbitrarily small stresses must be kept.
The diameter-only/ordered-cut model cannot supply that bridge.

No unconditional contradiction in the threshold branch has been proved.
The no-weak-pair branch, boundary weak pivots, open-cell exact phase,
nonconstant phase, split-star O--O, inactive interfaces, macroscopic inactive
containers/exterior caps, and remaining full-core sources are not eliminated.
The exact quantifiers `exists n0 forall n>=n0 forall global minimizers` remain
unproved. No canonical promotion is requested.
