> Generated reading edition · [exact source](../../../docs/reports/target_c_midpoint_bulk_braid_2026-10-02.md) · source SHA-256 `bfba89224ba5c153c4ddcbc48a5b244527c751f49e685c25b9988f7deef8e76b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C341CBF7AFCB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: a square-root-centered bulk of actual diameters

`completion midpoint energy -> a linear bulk of actual diameters centered to
O(sqrt(D)) -> an actual Omega(sqrt(D)) crossing braid with the same center ->
requires a contact/force transfer or strict full-source competitor -> Level I
only after all remaining branches are excluded`.

**Date:** 2026-10-02.\
**Shared starting HEAD:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.\
**Research base:** `46cdb4fd3cb5f078f298fa51857e23e321ac9204`.\
**State:** `2026-09-14.audit.51`.\
**Branch/mission:** `swarm/sol/stress-support-curvature-20261002`; global
source-support concentration, distinct from the current leaf-fan packets.\
**Classification:** proved candidates awaiting independent audit/promotion;
artifact lifecycle **unreviewed**. Section 6 is a **regression**. Section 5's\
stress consequence is **conditional** on an explicitly stated weight bound.\
**Level I and C-II:** OPEN. No canonical state is changed.

## 1. Inputs, prior work, and exact new result

Canonical inputs are [full-source Section 58, §1](../targets/target-c/58-full-source-geometry-audit.md),
[Section 57, §4](../targets/target-c/57-zr-zf-rigidity-audit.md), and
[C-WOODALL](target_c_woodall_diameter_topology_2026-09-10.md). They supply,
respectively, the full-hull area allowance, `h>=ceil(D)` for the canonical
triangle-free contact-minimal then diameter-pair-minimal source, and the
odd-unicyclic/forest topology of its **actual** diameter graph.

The earlier unpromoted [midpoint-energy report](target_c_full_source_midpoint_energy_2026-10-02.md)
proves uniform O(D^(2/3)) midpoint localization. Its Fourier/support identities
are rederived below; its force conclusions are not premises. The unpromoted
[cubic star report](target_c_global_diameter_star_cubic_budget_2026-10-02.md)
and [square-root braid](../../research/target_c_woodall_vertex_cover_sqrt_braid_2026-10-02.md)
were checked for overlap. **The new braid proof needs no cubic star inequality.**
It instead uses the degree bound inside the centered bulk.

The only literature import is existence of a constant-width-D planar completion
of a diameter-D set. The original Kupitz--Martini--Wegner paper, *A Linear-Time
Construction of Reuleaux Polygons*, Beitr. Algebra Geom. 37 (1996), 415–427,
p. 421 explicitly states this existence theorem, citing its reference [5],
Theorem 54, p. 126. [Original paper](https://emis.de/ft/11518). No uniqueness
or Hamiltonian-diameter hypothesis is imported.

Put
```math
a_D=2\arcsin\frac1{2D},\quad b_D=\frac{D a_D}{4},\quad
C_0=\sqrt{\frac{5\pi\sqrt3}{16}}.
```
For every `0<epsilon<1`, one point s satisfies
```math
\boxed{\#\{pq\in H: |(p+q)/2-s|>b_D+C_0\sqrt{D/\epsilon}\}<\epsilon D.}
\tag{BC.1}
```
This statement is uniform over **every global minimizer**, with all isolates
retained in its hull. For a canonical C-II source, the retained edges contain a
properly crossing matching of size
```math
\boxed{\left(\frac{(1-\epsilon)\sqrt\epsilon}{4C_0}-o(1)\right)\sqrt D.}
\tag{BC.2}
```
Every midpoint of that matching is in the **same** ball of radius
`b_D+C_0 sqrt(D/epsilon)`. Choosing `epsilon=1/3` gives radius
`sqrt(15 pi sqrt(3)/16) sqrt(D)+1/4+o(1)` and matching constant
`1/(6 sqrt(3) C_0)`. Unlike the older braid, its normalized central-reflection
error is O(D^(-1/2)), rather than O(D^(-1/3)).

## 2. Completion midpoint curve and its energy

Let A be a finite planar unit-separated source of diameter D>=1, K=conv(A),
and `delta=pi D^2/4-area(K)`. Choose a constant-width-D completion W containing
K. Translate its Steiner point to s and write its support function
```math
h(\theta)=D/2+f(\theta),\qquad f(\theta+\pi)=-f(\theta).
```
The first cosine/sine harmonics of f vanish. Its curvature measure satisfies
`rho=h+h''>=0` and `rho(theta)+rho(theta+pi)=D`; hence rho has a density in
[0,D], and h is in W^(2,infinity). Its support point is uniquely
```math
x(\theta)=s+h(\theta)n(\theta)+h'(\theta)Jn(\theta).
```
The midpoint curve is pi-periodic:
```math
c(\theta)=\frac{x(\theta)+x(\theta+\pi)}2-s
 =f(\theta)n(\theta)+f'(\theta)Jn(\theta),\qquad
c'=(\rho-D/2)Jn\quad\text{a.e.}
\tag{BC.3}
```
In particular c is D/2-Lipschitz on the projective angular circle.

The support-area identity, by integration by parts in the boundary area, is
```math
\delta_W=\frac12\int_0^{2\pi}(f'^2-f^2)\le\delta.
```
Only odd Fourier modes k>=3 remain. For each, the ratio of the midpoint-energy
coefficient to the deficit coefficient is
`(k^2+1)/(k^2-1)<=5/4`. Parseval therefore gives
```math
\boxed{E:=\int_0^\pi |c(\theta)|^2\,d\theta\le\frac54\delta_W\le\frac54\delta.}
\tag{BC.4}
```
Translations are removed before this estimate: it is false with an arbitrary
origin and unchanged deficit.

If pq is an original diameter pair and n=(p-q)/D, then every z in W obeys
```math
n\cdot(z-p)\le-|z-p|^2/(2D).
```
Thus p and q are precisely the unique support points x(theta) and x(theta+pi).
Consequently their actual source midpoint is s+c(theta). No completion point
is substituted for an original source vertex.

## 3. Actual diameter directions and the finite tail bound

### Lemma BC.1: projective separation

Distinct actual diameter edges have projective angular separation at least a_D.

**Proof.** Orient their vectors Du,Dv with angle theta in [0,pi/2], and write
their endpoints as `m_1 +/- Du/2` and `m_2 +/- Dv/2`. Put z=m_1-m_2. The two
cross-pair upper bounds yield
```math
|z\pm D(u+v)/2|\le D\quad\Longrightarrow\quad
|z|\le D\sin(\theta/2).
```
The two same-sign endpoint differences have norm at most
`|z|+D|u-v|/2<=2D sin(theta/2)`. At least one is a difference of distinct
source vertices; otherwise the two edges coincide. Unit separation gives
`1<=2D sin(theta/2)`, proving the assertion, including shared-endpoint edges.
QED.

Around each projective diameter direction theta_h take the angular interval
I_h of length a_D, centered at theta_h. These intervals have disjoint interiors
on the projective circle. On I_h, (BC.3) gives
```math
|c(\theta)|\ge(|c(\theta_h)|-b_D)_+.
```
For any T>b_D, integration and (BC.4) yield the **finite source theorem**
```math
\boxed{\#\{h: |m_h-s|>T\}<\frac{5\delta}{4a_D(T-b_D)^2}}
\tag{BC.5}
```
when the right-hand side is positive; with zero deficit there are no such
edges. The strict inequality comes from the strictly high midpoint values.

For a global minimizer Section 58 gives
`delta<(pi sqrt(3)/4)D`. Set `T=b_D+C_0 sqrt(D/epsilon)` and use a_D>=1/D.
Then the right-hand side of (BC.5) is less than epsilon D. This proves (BC.1).
The loss is an actual edge count, not a multiplier mass or a source population.

## 4. Braid extraction without the cubic incidence theorem

Let H_T consist of the actual edges with midpoint distance <=T. For a canonical
C-II source, (BC.1) and ZF give
```math
h_T>(1-\epsilon)D.
\tag{BC.6}
```
For any vertex p of H_T, its partners q=2m_h-p lie in the ball B(2s-p,2T).
Hence any two such partners are at distance <=4T. For sufficiently large D,
T<D/2, so their radius-D directions have angular separation at most
`2 arcsin(2T/D)`. The whole star lies in an ordinary arc of width <=pi/3
(each pair of partners has distance <=D). Ordering the star rays and using
unit separation gives
```math
\boxed{\Delta(H_T)\le1+\frac{2\arcsin(2T/D)}{a_D}=4T+o(\sqrt D).}
\tag{BC.7}
```
This bounds only the retained star; discarded diameter partners remain source
points and are not asserted to satisfy this radius bound.

Every subgraph of canonical H has at most one cycle, which, if present, is odd.
For a forest, the leaf induction proof of the matching/vertex-cover equality
gives tau=nu. In the odd-unicyclic case delete one cycle vertex, cover the
remaining forest, then add that vertex: tau<=nu+1. This applies to H_T even
if edge deletion disconnects it.

A minimum vertex cover of H_T has at most nu(H_T)+1 vertices, and each covers
at most Delta(H_T) edges. Therefore
```math
\nu(H_T)\ge h_T/\Delta(H_T)-1.
```
Substitution of (BC.6)–(BC.7) proves (BC.2). The retained matching consists of
disjoint actual diameters, so any two cross properly. Its endpoints are actual
strict hull vertices. If its 2k endpoints are cyclically x_0,...,x_(2k-1), every
chord has k-1 selected endpoints on each side (each other chord crosses it).
Thus the matching is exactly `{x_i x_(i+k):0<=i<k}` after cyclic relabeling.
For every pair,
```math
|x_{i+k}-(2s-x_i)|\le2T=O(\sqrt D).
\tag{BC.8}
```
The optimization of (1-epsilon)sqrt(epsilon) gives epsilon=1/3. All estimates
are sequence-uniform; no phase, fixed-star, or full-core hypothesis is used.

## 5. Pushing the result toward a stress transfer

An edge-count loss does **not** imply a small KKT-weight loss. Here is the
precise conditional lift, rather than such an inference.

Let beta_h>=0 sum to one on actual diameters. Suppose
```math
\boxed{\beta_h\le L a_D\quad\text{for every }h.}
\tag{BC.9}
```
For Q_h=(a_D^(-1) integral_(I_h)|c|^2)^(1/2), the Lipschitz bound gives
`|m_h-s|<=Q_h+b_D`. Since the intervals are disjoint,
`sum beta_h Q_h^2<=L E`. Minkowski's inequality yields
```math
\boxed{Q_\beta:=\sum_h\beta_h|m_h-s|^2
 \le(\sqrt{5L\delta/4}+b_D)^2.}
\tag{BC.10}
```
For a normalized actual KKT stress, for each loaded endpoint `b` put
`s_b=sum_k beta_bk>0` and `g_b=sum_k beta_bk(p_b-p_k)`. Then
```math
\sum_b|g_b-2s_b(p_b-s)|\le4\sqrt{Q_\beta}.
\tag{BC.11}
```
For each loaded endpoint define the scaled partner variance
```math
V_b:=s_b^2D^2-|g_b|^2
=s_b\sum_k\beta_{bk}|p_k-\bar p_b|^2,
\qquad
\bar p_b:=s_b^{-1}\sum_k\beta_{bk}p_k.
```
The partner variance identity then gives
```math
\sum_b V_b/s_b\le8Q_\beta,\qquad
0\le2D-\sum_b|g_b|\le8Q_\beta/D.
\tag{BC.12}
```
Indeed a partner is `2m_h-p_b`; its weighted variance is four times the
midpoint variance, bounded by four times its second moment about s. Summing
over b counts each edge twice. Finally
`D s_b-|g_b|=(V_b/s_b)/(D+|g_b|/s_b)<=V_b/(D s_b)`.

If L=O(1), the coordinate-response error in the source Dirichlet identity
is O(D^(-1/2)), and reciprocal-force perimeter loss is O(1). This would improve
the earlier uniform O(D^(-1/3)) and O(D^(1/3)) estimates. **(BC.9) is not
canonical or proved here.** Relative-interior positivity supplies no such
upper atom bound. The attempt to substitute cardinality concentration for
weighted concentration fails precisely at this missing hypothesis. Even the
conditional bounds do not themselves construct a strict source competitor.

## 6. A dense full-source regression for improving the bulk radius

This explicitly tests the proposed repair `retain a positive fraction of H
with midpoint radius o(sqrt(D))` from full-source density/roundness alone.

Let k=4r+1>=101, D=k^2, a=D/[16(k^2-1)], and define a smooth body W_k by
```math
h(\theta)=D/2+a\cos(k\theta).
```
Its curvature radius is
```math
\rho=D/2-(D/16)\cos(k\theta)\in[7D/16,9D/16].
```
Thus it is strictly convex, has constant width D, has Steiner point zero, and
```math
\delta_W=\pi D^2/[512(k^2-1)]=O(D).
\tag{BC.13}
```
Put t=(5k-1)/4, N=kt, and choose the projective normals
```math
\theta_j=\pi j/N,\quad 0\le j<N,\quad
\frac1{12}\le\frac{j\bmod t}{t}\le\frac{11}{12}.
\tag{BC.14}
```
Include both boundary points x(theta_j),x(theta_j+pi) for each chosen j.
There are
```math
M=k(\lfloor11t/12\rfloor-\lceil t/12\rceil+1)
 \ge 5N/6-2k>D
```
chosen diameters. The final strict inequality follows from k>=101 and
`5N/6-2k=25k^2/24-53k/24`.

For two boundary points with smaller normal separation Delta<=pi, projection
of their boundary integral onto the midpoint tangent gives
```math
|x(\theta+\Delta)-x(\theta)|\ge2(7D/16)\sin(\Delta/2).
```
Selected normals on the full circle have minimum spacing pi/N. Consequently
every distinct boundary pair has distance at least
```math
(7D/8)\sin(\pi/(2N))>1.
\tag{BC.15}
```
For example this is certified with `3<pi<22/7` and `sin z>=z-z^3/6`.
No boundary contact exists. The only diameter pairs are the selected antipodal
ones: a diameter chord must be normal at each endpoint, whose outward normal
is unique. Their midpoints are
```math
c_j=a\cos(k\theta_j)n_j-ak\sin(k\theta_j)Jn_j,
\quad |c_j|\ge ak\sin(\pi/12)>k/64=\sqrt D/64.
\tag{BC.16}
```

The midpoint set is invariant under rotation by 2pi/k. Each orbit has k points
on a circle of radius >=sqrt(D)/64. A ball of radius R'<sqrt(D)/64 meets such
an orbit in at most
`k arcsin(64 R'/sqrt(D))/pi+1` points: its circle intersection is an arc of
angular width at most twice that arcsine. Hence every common-center ball of
radius o(sqrt(D)) contains only o(M) selected midpoints. This rejects an
o(sqrt(D)) radius retaining a positive fraction of the actual diameters.
It does **not** reject an improvement for a smaller selected matching.

The largest normal gap in the selected boundary set is at most
`Delta_max=pi/(6k)+2pi/N`. For an arc gap of width Delta, the cap-area formula
is `1/2 integral_(s<t) rho(s)rho(t) sin(t-s) ds dt`, at most
`(9D/16)^2 Delta^3/12`. Since gap widths sum to 2pi, the hull P of the
selected boundary points satisfies
```math
\delta_P\le\delta_W+\frac\pi6(9D/16)^2\Delta_{max}^2=O(D).
\tag{BC.17}
```
For k>=101, N>=k^2 and `1/6+2/k<1/5`, so Delta_max<pi/(5k).
Using `pi<22/7`, `pi^3<32` and `k^2/(k^2-1)<2`, the displayed bound divided
by D is less than `pi/256+81 pi^3/38400<1`. Thus it is less than D for
every member of the infinite family, and meets the canonical numerical
area allowance since `pi sqrt(3)/4>1`. The support deficit of an individual
chord gap is at most `(9D/16) Delta_max^2/8`; hence P contains a centered disk
of radius `D/2-a-(9D/16) Delta_max^2/8>D/2-1/6`: indeed a<1/8 and the
second loss is less than `9 pi^2/3200<9/320`.

To obtain quadratic **actual source** population, take a translate of the
triangular lattice scaled by `1+D^(-3)` in the open depth-two body of W_k.
Translation averaging and inner-parallel coarea give at least
```math
\frac{\operatorname{area}(W_k)-2\pi D}
 { (\sqrt3/2)(1+D^{-3})^2}
=\frac{\pi}{2\sqrt3}D^2-O(D)
\tag{BC.18}
```
sites. Add them to the boundary source. Their internal distances are >1,
and distances to boundary points are >2. They are not new diameter endpoints,
since they are interior points of a diameter-D body. The complete source is
triangle-free, unit-separated, quadratically populated, diameter D, has more
than D actual diameters, has hull inradius D/2-O(1), and satisfies the displayed
area allowance. All its contacts are absent.

It is rigorously **nonglobal**: its finite minimum pair distance sigma is >1,
so scaling the entire source by 1/sigma gives the same cardinality and a strictly
smaller diameter. It has no positive source KKT stress or nonisolated contact
core. Adding density to a geometric support argument cannot supply those
missing hypotheses. No triangle-free global minimizer is asserted.

## 7. Verification, self-audit, and exact remaining obligation

[The exact verifier](../../../research/verify_midpoint_bulk_braid_2026_10_02.py)
uses rational arithmetic for Fourier coefficient inequalities, discrete energy
sampling, the projective-gap calculation, and finite witnesses k=101,105,201.
It checks the exact integer normal selection, the certified separation bound,
midpoint lower bound, cap-area allowance, inradius bound, and quadratic lattice
count lower bound. It neither constructs a global minimizer nor verifies KKT
for the regression. The analytic infinite-family proofs above are independent
of finite numerical survival.

Stars and paths satisfy the new conclusions; neither connectivity nor a
spanning-tree basis is used to claim a release. The braid is an actual-source
matching, not a train scaffold. Its force mass is unproved. All full-core,
nonconstant-phase, inactive-interface, split-star and macroscopic-container
branches retain their canonical open status.

| Claim | Classification | Exact limit |
| --- | --- | --- |
| BC.1 and finite tail BC.5 | proved candidate awaiting promotion | actual edge count, not stress mass |
| BC.2 and BC.8 | proved candidate awaiting promotion | centered crossing braid, no finite release |
| BC.10–BC.12 | conditional | requires beta_h<=L a_D |
| Positive-fraction bulk radius o(sqrt(D)) from density/roundness | rejected by regression | no KKT/global-optimality premise in the rejected claim |
| C-II / Level I closure | not proved | no exact triangle or strict canonical-source competitor |

Promotion recommendation: preserve as **unreviewed** pending independent audit;
do not change the manifest or active prompt. The precise next source theorem
is a contact/force transfer for the actual centered braid: either establish a
stress distribution bound sufficient for BC.10 and couple its bounded force
loss to canonical contact/face currency, or construct a full-source finite
competitor using its ordered endpoints. The regression prevents substituting
quadratic population and roundness for that transfer.

The [continuing fan-reflection packet](target_c_centered_fan_simultaneous_reflections_2026-10-02.md)
tests a concrete competitor: simultaneous independent fan reflections remove
exactly |S| diameter pairs and leave only unary fixed-point lower blockers.
Their selected blockers are distinct under the stated radius condition, giving
a canonical `ceil(2U/5)` inactive matching for D>=10000. One-/two-isolate repairs
are checked exactly, including collision transfer when only the first blocker
moves. A universal repair of those points remains missing.
