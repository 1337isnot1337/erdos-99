<!-- theorem-state: {"artifact_id":"ART-DFDF669AC3B9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Erdős Problem #99 — Seed 66: a coembedded locked, full-rank response regression

- **Date:** 2026-10-13
- **Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
- **State version:** `2026-10-10.audit.234`
- **Seed/category:** 66 / Target A: Schur deficiency and response capacity
- **Run type:** closure attack, exact regression, hostile self-verification
- **Classification:** proved candidates awaiting independent review; regression
  against the stronger implication stated below. The artifact remains unreviewed.
- **Active prompt:** `docs/prompts/erdos_problem_99_TARGET_A_CURRENT_CONTINUATION_PROMPT.md`
- **Literature:** no new import.
- **Computation:** `research/verify_target_a_seed066_locked_fullrank.py`.

## Level I status

**STILL OPEN.** No canonical endpoint is changed or promoted.

## 1. Closure attack and exact obstruction

The canonical sufficient endpoint is

\[
\zeta=|C^\partial|-\operatorname{rank}S\ge
s=\Delta_\Lambda-d_{\rm int}.
\]

Section 175 supplies the alternative sufficient inequality

\[
|O_{\rm iso}|+\sum_i(|O_i|-|C_i|)_+\ge j_*+|T_Z|.
\]

The attempted bridge was to force a positive Schur nullity from a **coembedded**
locked positive-contact network, exact maximum packing in the response hull, and
a contact fan with very few actual crossing response rows. If that bridge supplied
the full demand `s`, the canonical endpoint would contradict the Target A survivor.
The quantitative demand is an additional, indispensable hypothesis: even a positive
nullity would not automatically pay `s`.

The result below disproves the weaker prerequisite that the displayed local/container
data force even one null direction. It also defeats replacing the missing global
minimum-diameter hypothesis by optimality under every affine transformation.
It does **not** disprove the canonical endpoint, whose hypotheses include an actual
global minimum-diameter response optimum and its coupling to a triangle-free source.

## 2. Main regression theorem

Write

\[
e_1=(1,0),\quad e_2=(1/2,\sqrt3/2),\quad
\Lambda=\mathbb Ze_1+\mathbb Ze_2,
\quad Q(i,j)=i^2+ij+j^2.
\]

For every integer `m>=2`, put

\[
X_m=\{ie_1+je_2:\max(|i|,|j|,|i+j|)\le m\},
\qquad K_m=\operatorname{conv}X_m.
\]

There is a nonempty **open** set `U` of response translations, independent of `m`,
such that all of the following hold.

1. `X_m` has `n_m=3m^2+3m+1` points, is unit-separated, and is a maximum-cardinality
   packing in `K_m`. Its diameter is `2m`.
2. There is a contact/facet equilibrium with coefficient one on **every** unit
   contact and positive reactions on every active hull facet. Its fixed-hull feasible
   velocity cone is `{0}`. In particular every unit triangle is universally locked.
   The labeled placement is locally isolated among feasible packings in this hull.
3. In the actual radial conflict graph
   \[
   G_m\subseteq X_m\times Y_m,\quad
   Y_m=(\Lambda+v)\cap\operatorname{int}(K_m+\mathbb B),
   \quad xy\in E(G_m)\iff |x-y|<1,
   \]
   put `Z_m=(Lambda+v) cap int K_m` and `O_m=Y_m\setminus Z_m`.
   Then
   \[
   |Z_m|=3m^2,\quad d_{\rm int}=0,\quad
   |C^\partial|=3m+1,\quad
   \boxed{\operatorname{rank}S_m=3m+1,\quad\zeta_m=0.}
   \]
   These rank statements hold for **every assignment of nonzero real edge entries**
   to the incidence matrix, not only generic independent entries.
4. There is a positive-contact three-spoke fan from an interior unit triangle to
   three distinct hull points, with `3m+1` vertices and `3m+1` edges. Exactly **one**
   response edge properly crosses its contact edges. Its right endpoint is `v in Z_m`.
5. For every contact subgraph `Sigma`, delete its contact vertices, its actual
   crossing right vertices, and both endpoints of every basis pair so affected.
   In the resulting sector-to-exterior-sink coarse graph, every surviving Schur
   terminal has its own distinct direct sink. Its left Hall deficiency is zero.
6. Every affine image of `X_m` that is still unit-separated has diameter at least
   `2m`. Nevertheless for every `m>=32` there is an `n_m`-point unit-separated
   replacement of diameter at most `19m/10<2m`.

Thus exact fixed-container maximality, a trivial feasible velocity cone, a common
positive stress, a quadratic population, affine diameter optimality, and an actual
fan crossing bank of size one can coexist with **zero** Schur nullity.

### Scope

This is one geometric response configuration, its own hull, its own stress, and its
own lattice conflict graph. The stress and response have not been placed on separate
unrelated examples. This is stronger in that respect than the independent-gadget
regression of Section 149.

The hexagonal family contains triangles. It is not asserted to be a triangle-free
source or an actual global diameter optimum. Part 6 explicitly proves nonglobality
for every `m>=32`. No contact-isolated labels are discarded: the family has none;
every one of its `n_m` labels is counted, and the competitor has exactly `n_m` points.
Canonical roundness and the separate triangle-free-source/collar hypotheses are
absent. Those are legitimate ways a source-specific closing theorem could exclude
this regression.

## 3. Complete proof

### 3.1 Exact capacity, population, and diameter

The hexagon has axial-coordinate vertices

\[
(m,0),(0,m),(-m,m),(-m,0),(0,-m),(m,-m).
\]

Its six sides have length `m`. Its area is `3sqrt(3)m^2/2`, and its perimeter is
`6m`. Counting successive hexagonal lattice shells gives

\[
|X_m|=1+\sum_{r=1}^m6r=3m^2+3m+1.
\]

Distinct lattice differences have a positive integer squared norm `Q`, so the points
are unit-separated. The canonical finite Oler inequality, shared Lemma 21.1, gives
for any unit-separated `P subset K_m`

\[
|P|\le\frac{\operatorname{area}K_m}{\sqrt3/2}
+\frac{\operatorname{per}K_m}{2}+1=3m^2+3m+1.
\]

Thus the fixed-hull maximum is exact. The hull is a regular hexagon of circumradius
`m`, with opposite vertices `2m` apart, so its diameter is `2m`.
No equality-uniqueness theorem for Oler is used or claimed.

### 3.2 A strictly positive contact/facet certificate and local isolation

Use the six unnormalized facet covectors `+/-i`, `+/-j`, `+/-(i+j)`.
Their Euclidean gradients, in the `e_1,e_2` basis, are

\[
\nabla i=(4/3,-2/3),\quad
\nabla j=(-2/3,4/3),\quad
\nabla(i+j)=(2/3,2/3).
\]

Give every unit edge contact weight one. At a noncorner boundary point give its
single active facet weight `3/2`; at a corner give each of its two active facets
weight one. Interior points have no reaction. These unnormalized covectors can be
converted to unit normals by multiplying the reaction weights by their lengths.

The six full-lattice neighbor displacement vectors sum to zero. Therefore the force

\[
f_p=\sum_{q\in X_m:|p-q|=1}(p-q)
\]

is the sum of the **missing** outward neighbor displacements. On the side `i=m`
away from the corners it is `(2,-1)=(3/2)nabla i`; at the corner `(m,0)` it is
`(2,0)=nabla i+nabla(i+j)`. Hexagonal symmetries give all remaining boundary cases.
At every interior point it is zero. This proves equilibrium at every label.

Let `u_p` be any fixed-hull infinitesimally feasible velocity. Every unit contact has

\[
(p-q)\cdot(u_p-u_q)\ge0,
\]

and every active outward facet has `nabla phi dot u_p<=0`. Summing the contact
variations and using equilibrium gives

\[
0\le\sum_{pq\in E_1(X_m)}(p-q)\cdot(u_p-u_q)
=\sum_p f_p\cdot u_p
=\sum_{p,f}\mu_{pf}\nabla\phi_f\cdot u_p\le0.
\]

Every contact variation is consequently zero, and every positively weighted facet
variation is zero. The elementary triangular faces triangulate the hexagon. A
velocity preserving the three sides of one nondegenerate triangle is a rigid-motion
velocity. Propagating across shared triangle edges shows that the same rigid-motion
velocity holds on the entire connected triangulation. At each corner the two active
facet covectors are independent, so that corner velocity is zero. Two distinct fixed
corners force the global rigid-motion velocity to be zero. Hence the feasible cone
is `{0}`.

For completeness, this gives genuine local isolation without confusing a first-order
certificate with a finite path. If different feasible labeled placements converged
to `X_m`, normalize their displacement vectors by their positive Euclidean norm and
take a convergent subsequence. Exact linear facet inequalities and the first term of
each squared contact inequality give a unit-norm feasible limiting velocity. That
contradicts the zero cone. Thus no such sequence exists. This argument makes no claim
of global uniqueness among all packings in the hull.

### 3.3 An open phase set and the entire radial graph

Let `v=ae_1+be_2`. Take the following open set, independent of `m`:

\[
U=\{(a,b):0<a<b,\ a+b<1/10,
\quad Q(a,b)<\min(b-a,2a+b,a+2b)\}.
\]

It is nonempty: `(a,b)=(1/1000,2/1000)` belongs to it. Also `|v|<1/10`.

For any lattice difference `k`, `|k+v|<1` holds exactly for

\[
\boxed{k\in\{0,-e_1,-e_2,e_1-e_2\}.}
\]

Indeed for the three nonzero displayed differences the squared norms are respectively

\[
1-(2a+b)+Q(v),\quad
1-(a+2b)+Q(v),\quad
1+(a-b)+Q(v),
\]

all strictly below one. The opposite unit directions have squared norm strictly above
one. Every other nonzero lattice vector has length at least `sqrt(3)`, so the reverse
triangle inequality gives length greater than one after adding `v`. This also proves
no source-to-lattice distance is zero or one.

Every right vertex `z+v` therefore has source neighbors among

\[
z,\quad z+e_1,\quad z+e_2,\quad z-e_1+e_2,
\]

with precisely those belonging to `X_m` retained. Equivalently every left source
point has all four strict lattice neighbors. They all lie in `Y_m`, because their
distance to that source point is below one. Thus there is no left-neighborhood
truncation.

An integer lattice point outside `K_m` violates one of its six axial inequalities
by at least one. The translation changes each axial coordinate or coordinate sum
by less than `1/10`. Consequently no such point can translate into `K_m`. Among
points of `X_m`, precisely the three positive sides `i=m`, `j=m`, `i+j=m` translate
outside the hull. Each side has `m+1` lattice points; the two neighboring corner
overlaps are `(m,0)` and `(0,m)`, and there is no third overlap. Hence

\[
B=\{z\in X_m:z+v\in\operatorname{int}K_m\},\quad
|X_m\setminus B|=3m+1,\quad |Z_m|=|B|=3m^2.
\]

There are no response lattice sites on the hull boundary: each of `a,b,a+b` lies
strictly between zero and one, while the old axial coordinates are integers.

### 3.4 Full Schur rank for every nonzero edge weighting

Match each `x in X_m` to its own distinct row `x+v`. All these edges have length
`|v|<1`, and all their right endpoints belong to `Y_m`. Restricting this matching
to `B` is a perfect `Z_m`-basis matching.

There is a stronger matrix certificate. Order the source indices and their own rows
by the integer functional

\[
\ell(i,j)=i+2j,
\]

breaking ties arbitrarily but identically on rows and columns. The selected square
matrix with columns `X_m` and rows `X_m+v` is upper triangular. Its diagonal entries
are the own-row edge weights, and every other possible neighbor increases `ell` by
`1`, `2`, or `1`. Its determinant is therefore exactly the product of its nonzero
diagonal weights. The `Z_m` by `B` submatrix has the same triangular property.

Every deep column belongs to `B`: otherwise its own row is exterior, contradicting
deepness. Since the entire selected matrix is invertible, all deep columns are
independent. This is a valid Section-102 basis choice extending the deep basis, with
`d_int=0` and `C^partial=X_m\setminus B`.

Apply the Schur determinant identity to the exterior rows

\[
O_0=(X_m\setminus B)+v\subset O_m.
\]

The square Schur minor on `O_0,C^partial` has determinant, up to the ordering sign,

\[
\det S_m[O_0,C^\partial]
=\pm\frac{\det A[X_m+v,X_m]}{\det A[Z_m,B]}\ne0.
\]

Thus `rank S_m=|C^partial|=3m+1` for every nonzero edge weighting. In particular the
canonical generic matrix and its alternating gammoid have zero nullity. No KKT or
conductance weights have been identified with the generic matrix entries.

### 3.5 A locked fan with one actual crossing row

Take the triangle with axial vertices `(0,0),(1,0),(0,1)`. Use these three spokes:

\[
(0,0),(-1,0),\ldots,(-m,0);
\]
\[
(1,0),(2,0),\ldots,(m,0);
\]
\[
(0,1),(-1,2),\ldots,(1-m,m).
\]

They are vertex-disjoint, including their three distinct starting points. Each stops
at its first hull vertex. The triangle vertices are interior when `m>=2`. Together
with the triangle sides these paths form a connected unicyclic fan with `3m+1`
vertices and edges. All its contacts have positive weight in the equilibrium above.

The four possible old neighbors of a row `z+v` form the unit lozenge with vertices
`z,z+e_1,z+e_2,z-e_1+e_2`. Since `a,b>0` and `a+b<1`, `z+v` lies in the interior
of the elementary triangle `z,z+e_1,z+e_2`. Its three radial segments from that
triangle's vertices lie in that triangle and properly cross no old lattice contact.
The radial segment from `z-e_1+e_2` crosses exactly the short lozenge diagonal
`[z,z+e_2]`; in axial coordinates the crossing point is

\[
z+\frac{a+b}{1+a}e_2,
\]

strictly inside that diagonal. If this fourth old neighbor is absent, the crossing
edge is simply absent. These are all radial edges, so this classifies **all** their
proper crossings with the entire old contact graph.

Every spoke uses only `e_1` or `e_2-e_1` contacts. The fan's only `e_2` contact is
the triangle side `[(0,0),(0,1)]`. The point `(-1,1)` belongs to `X_m` and is not
on the fan. Its response edge to `v` crosses that triangle side. Hence the fan has
exactly one crossing edge and one crossing right vertex, `v in Z_m`.

### 3.6 Zero coarse left deficiency after actual crossing deletion

This conclusion uses an actual-crossing shield, not the larger Section-177 union
of all edge lenses or the Section-175 full tube. Their deficiency quantities must
not be identified.

For any contact subgraph `Sigma`, the crossing classification shows that every
crossing right row is `p+v` for an endpoint `p in V(Sigma)` of a vertical contact.
Delete those rows and all contact vertices. Close these deletions under the own-row
`B <-> Z_m` matching by removing both endpoints of every affected basis pair.

If `c in C^partial\setminus V(Sigma)`, its own row `c+v` lies in `O_m`, is not a
deleted crossing row, and is not the row of any deleted basis contact vertex. The
short segment `[c,c+v]` stays inside one elementary source triangle and properly
crosses no old contact. It cannot meet a distinct source vertex, because its length
is below one. The unchanged direct edge is therefore allowed in the sector of `c`.

Distinct surviving terminals have distinct own exterior sinks. These direct edges
give a matching saturating the left shore of the coarse sector-sink graph, including
when exterior sinks have other sector neighbors. Hall's left deficiency is exactly
zero. This argument applies to every finite contact subgraph, not just the chosen
fan. It does not claim sector uniqueness for exterior sinks.

### 3.7 Affine optimality and an explicit whole-population replacement

Let `L` be the linear part of an affine map whose image of `X_m` is unit-separated.
The source contains unit pairs in each direction `e_1,e_2,e_1-e_2`. Thus

\[
|Le_1|,|Le_2|,|L(e_1-e_2)|\ge1.
\]

It also contains opposite hexagon corners whose differences are `2m` times those
three directions. The image diameter is at least `2m`. This is an exact restriction
on **all** feasible affine maps, not a first-order assertion.

Now set `R=19m/20`. Unit triangular-lattice Voronoi cells have area `a_0=sqrt(3)/2`
and covering radius `r_0=1/sqrt(3)`. The cells of lattice sites in the closed disk
`B(0,R)` cover `B(0,R-r_0)`: a nearest lattice site to any point in the latter disk
is at distance at most `r_0` and has norm at most `R`. Therefore

\[
\#(\Lambda\cap\overline B(0,R))\ge
\frac{\pi(R-r_0)^2}{a_0}.
\]

Use the elementary strict bounds `pi>25/8`, `sqrt(3)<7/4`, and `r_0<3/5`. For
`m>=32` this gives

\[
\#(\Lambda\cap\overline B(0,19m/20))
>\frac{25}{7}\left(\frac{19m}{20}-\frac35\right)^2
=\frac{(19m-12)^2}{112}.
\]

The difference between the last quantity and `n_m` is

\[
\frac{25m^2-792m+32}{112}>0\qquad(m\ge32).
\]

At `m=32` its numerator is `288`; its successive increment is `50m-767>0` for
`m>=32`. Select any `n_m` sites in this disk. They are unit-separated and have
diameter at most `2R=19m/10<2m`. For a reproducible choice, order the disk sites
by `(Q(i,j),i,j)` and take the first `n_m`.
For a labeled competitor, pair these ordered new sites with the lexicographically
ordered old axial labels. This is a specified bijection retaining every label.

This is a complete replacement, including all labels by cardinality. It has no fixed
old diameter pair, no refill assumption, and no incompatible local exchange. It
proves that the large regression configurations fail actual global optimality even
though they are optimal against every affine map and rigid in their own hull.

## 4. Three mechanisms and their exact outcomes

1. **Crossing-only geometric separator.** The unit-contact midpoint confinement
   already present in the repository permits at most one crossing right row per unit
   contact. This is a useful cost reduction but does not supply sector population
   surplus or remove the cost of contracted basis contact vertices. No new constant
   refinement is offered as a closing result.
2. **Positive-stress/container coupling.** Exact capacity and the trivial feasible
   cone were used as a proposed replacement for the missing global source information.
   The coembedded theorem falsifies that bridge: the Schur nullity is zero for every
   nonzero edge weighting. Even the actual-crossing coarse Hall deficiency is zero.
3. **Global optimality via finite comparison.** Uniform affine strain is completely
   ineffective on this same family. A nonaffine whole-population replacement succeeds
   for all `m>=32`. Thus the global hypothesis has concrete content absent from both
   the stress and affine tests. Applying this replacement to an arbitrary canonical
   response/source pair would require a population bound in a suitable disk; none is
   established by this argument.

The third mechanism is a strict diameter competitor for the regression family, not
for an actual Target A survivor.

## 5. Dependencies, originality, and regressions

The only load-bearing canonical input to the construction is the finite Oler
inequality in `docs/theory/03-oler-shell.md`, Lemma 21.1. Response terminology and
the comparison to the live frontier use Section 102 in
`docs/targets/target-a/02-scaffold-and-hall.md`, Section 113 in
`docs/targets/target-a/03-source-response.md`, and Sections 169, 172, 175, 177.
The matrix proof above does not require a generic-rank assertion as an additional
premise: it exhibits the determinant explicitly.

No theorem from an unpromoted PR is a premise. Open PR #953 concerns source-arm
localization and source-gate bounds; this family instead couples positive locked
stress to its own exact hull and its own full radial response. The prior Section-149
no-go uses independently placed source and response gadgets. Here they are one
geometric object, at unbounded population, with exact hull saturation and an open
phase set. The new assertions are the joint family theorem, universal nonzero-weight
Schur minor, actual one-row fan, and its global/affine comparison, rather than the
previously known midpoint crossing lemma.

| Guard | Check / limitation |
| --- | --- |
| Local or jammed versus global minimum | Whole-source sub-`2m` competitor proves nonglobality for `m>=32` |
| Source versus response versus scaffold | Only `X_m` and its own response lattice are coembedded; no triangle-free source is supplied |
| Simultaneous feasibility | Competitor is one finite lattice set of exactly `n_m` points; all its pairs are unit-separated |
| First-order versus finite | Cone calculation is separate from local-isolation proof and finite competitor |
| Generic rank versus KKT weights | Schur minor is nonzero for every nonzero edge weighting; no unjustified weight identification |
| Exterior sector overlap | Retained in the actual-crossing coarse graph; a direct matching proves zero deficiency |
| Section-166 SDR collision / independent source matchings | No SDR upgrade or identification of the two source matchings is used |
| Contact isolates / ZR-ZF core scope | Every regression label is counted; no full-source extension of a core theorem is used |
| Boundary and integer errors | Exact `3m^2`, `3m+1`, and threshold `m>=32`; no boundary term dropped |
| Oler / RSR equality uniqueness | Capacity only; no equality-uniqueness conclusion |

## 6. Computation and hostile checks

Run

```text
python3 -I -O -B research/verify_target_a_seed066_locked_fullrank.py
```

The verifier uses integer axial coordinates and `fractions.Fraction`; squared
distances and segment crossings are exact. It checks complete source pair ledgers,
the positive stress at every source label, integer-rigidity full rank modulo a prime
(a certificate of rational full rank), the full response shore, the selected
triangular matrix and explicit Schur elimination, and every fan/response crossing.
It separately constructs the disk replacement at `m=32` and checks all its pairs.
For the specified label bijection it records all retained, removed, and created unit
contacts; all three old diameter pairs are strictly shortened. New unit contacts and
triangles are permitted in a competitor to unrestricted minimum diameter.
Negative controls remove an own-row edge, violate the open-phase inequalities,
remove a reaction, change a contact weight, omit a competitor label, and duplicate a
replacement label. Each is required to fail its advertised certificate.

Finite checks corroborate the formulas; the proof in Section 3 establishes all-`m`
and all-`v in U` quantifiers. Passing tooling checks or these finite checks is not an
independent mathematical audit or proof of global optimality.

## 7. Frontier effect and precise remaining gap

**Canonical frontier unchanged.** This closes an overstrong stress/container-only
shortcut, including its crossing-sparsity and affine-optimality variants. It gives no
canonical source motion and does not eliminate the actual locked or zero-slack branch.

The smallest exact closing obligation remains: for a genuine Target A survivor, use
the actual global-minimizer and triangle-free-source coupling to produce one generic
phase and stress-generated fan with

\[
\boxed{|O_{\rm iso}|+\sum_i(|O_i|-|C_i|)_+\ge j_*+|T_Z|,}
\]

or a same-cardinality strict-sub-diameter competitor. The independent zero-slack
branch still needs its source-to-Schur or finite-descent bridge. The family supplies
neither the source collar demand nor the global optimum hypothesis, and therefore
cannot decide either branch.

## 8. Claim classification and review disposition

| New assertion | Classification | Reason |
| --- | --- | --- |
| Joint coembedded family, Parts 1–5 | proved candidate awaiting independent review; regression | Complete all-`m` proof plus exact finite certificate; not independently audited |
| Nonzero-weight full Schur minor | proved candidate awaiting independent review | Explicit triangular determinant quotient |
| Affine restriction and disk replacement, Part 6 | proved candidate awaiting independent review | Full-source analytic pair/population argument and exact finite replay |
| Stress + own-hull maximality + sparse actual crossings forces a Schur kernel | rejected by regression | `zeta_m=0` for the family above |
| The same claim with affine optimality added | rejected by regression | Part 6 adds this hypothesis without creating nullity |
| Canonical global source coupling closes Target A | unresolved | The regression intentionally lacks those hypotheses |

No promotion is requested without independent mathematical review. In particular no
state-version increment, route-map change, or continuation-prompt rewrite is justified.
