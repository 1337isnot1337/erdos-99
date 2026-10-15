<!-- theorem-state: {"artifact_id":"ART-0043D9883A11","canonical":true,"claim_ids":["C-COUPLED-DELAUNAY-CONVEX-CONTAINER-TRANSFER"],"claim_statuses":{"C-COUPLED-DELAUNAY-CONVEX-CONTAINER-TRANSFER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.108 — coupled Delaunay transfer for convex containers

**Date:** 2026-10-07  
**Audit base:** `origin/main=8ac3c26257b24fd37e617fa7b7fb732039adb253`, state `2026-10-07.audit.107`  
**Target:** C-II; C-I is closed, C-II and Level I are open  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** not used  
**Computation:** `research/verify_target_c_coupled_container_crop_2026_10_07.py`

## 1. Starting endpoint and audit chain

The C-II macroscopic-container branch still needs a source-realized finite move that checks every old lower and actual-diameter upper constraint. The candidate geometric input is:

```text
one common saturated completion and Delaunay triangulation
-> exact Oler slack S, boundary-strip population B, and contained-triangle excess Sigma
-> O(S+p) exceptional vertices when S,p=O(D)
-> source-realized movement/payment and the Audit.64 full-source endpoint (still missing)
```

The new theorem supplies the first two arrows only. It does not make a Delaunay edge an old contact, construct a replacement packet, or yield a C-II contradiction by itself.

**Frozen source:** `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`. The report and verifier first appeared at `8a719ea78d0794124dee73718c70d9abafaa8375` and are byte-for-byte unchanged at the frozen tip.

- Source report: `docs/reports/target_c_coupled_delaunay_transfer_for_arbitrary_convex_containers_2026-10-07.md`, SHA-256 `85cb5d5dc25cf908219962f7d1bcd936ef16405af065f0cd2797dc103e8f8ab6`.
- Verifier: `research/verify_target_c_coupled_container_crop_2026_10_07.py`, SHA-256 `9194bb36e06c9ee39a057990a38a5b5c4e3025ad2f1a18ce8cc05df5a5683a9c`.

## 2. Exact theorem audited

Let $A\subset\mathbb R^2$ be any finite unit-separated source. There exists one locally finite unit-separated packing $P\supset A$ whose closed unit disks cover the plane. Choose one locally finite Delaunay triangulation of $P$; the same $P$ and triangulation are used for every container below. Only this covering-radius property is needed; no stronger maximality convention at exact distance one is used.

For a compact convex polygon $C$ with nonempty interior, write $Q=\operatorname{area}(C)$, $p=\operatorname{per}(C)$, and $z=|A\cap C|$, including source labels on $\partial C$. Put

\[
a=\frac{\sqrt3}{4},\qquad a_0=2a=\frac{\sqrt3}{2},\qquad
S=\frac{Q}{a_0}+\frac p2+1-z.
\]

Let $B=|\{x\in P\cap C:\operatorname{dist}(x,\partial C)\le2\}|$. Let $\mathcal T_C$ be the Delaunay triangles contained in $C$, and put

\[
\Sigma=\sum_{T\in\mathcal T_C}(\operatorname{area}(T)-a),
\qquad \delta=\frac{2-\sqrt3}{4}.
\]

Then:

1. $S\ge0$, and the number of auxiliary additions in $C$ is at most $\lfloor S\rfloor$.
2. $B\le20p/\pi+25$, and
   \[
   0\le\Sigma\le a_0S+28aB.
   \]
3. Among vertices of the contained-triangle complex, one can mark an exceptional set of size at most
   \[
   73B+\left(\frac{12}{\delta}+450\right)\Sigma,
   \]
   so every other vertex whose distance from $\partial C$ exceeds two has a complete six-triangle Delaunay star in $C$; all six triangles are acute and have individual excess below $1/100$. If $e_T=\operatorname{area}(T)-a$, each such triangle satisfies
   \[
   L_T-1\le5e_T,\qquad
|\alpha-\pi/3|\le50e_T
   \]
   for every side length $L$ and each angle $\alpha$ of $T$.

All original source points remain in $P$, including contact-isolated points. This is a single coupled completion, so the geometric rows for different containers come from the same triangulation. Triangle excess in overlapping containers cannot be spent twice.

## 3. Independent proof reconstruction

### Closed-unit-covering completion and Oler count

Enumerate a dense countable subset of the plane and add each proposed point when it is at distance at least one from every point already present. Starting with $A$, this gives a unit-separated set $P\supset A$. A bounded region contains only finitely many unit-separated points, so $P$ is locally finite. It covers the plane by closed unit disks: if $y$ had distance $d>1$ from $P$, choose an enumerated point $q$ with $|q-y|<(d-1)/3$. If accepted, it contradicts the definition of $d$; if rejected, an earlier point within distance less than one of $q$ is at distance less than $(d+2)/3<d$ from $y$, also a contradiction.

Every Voronoi cell lies in the radius-one disk about its site, so the cells are bounded. Their dual gives a locally finite Delaunay tiling; triangulate each co-circular face. Each Delaunay triangle has circumradius at most one because its circumcenter is within one of the nearest point of $P$. Every Delaunay edge consequently has length at most two.

The finite set $P\cap C$ is unit-separated and contained in the convex set $C$, so Oler's inequality (shared theory, Lemma 21.1) gives

\[
|P\cap C|\le Q/a_0+p/2+1=z+S.
\]

Thus $S\ge0$, and the integer number $|(P\setminus A)\cap C|$ is at most $\lfloor S\rfloor$. Boundary source labels are included in $z$; no boundary points are silently omitted.

### Boundary strip and degree

For $s=5/2$, every open disk of radius $1/2$ centered at a point counted by $B$ lies within distance $s$ of $\partial C$. These disks are disjoint. The area within distance $s$ of the boundary of a convex polygon is at most $2sp+\pi s^2$: the outside parallel strip has area $sp+\pi s^2$, and the inner strip has area at most $sp$, by integrating the nonincreasing perimeters of the inward parallel sets until the eroded set disappears. Dividing by the disk area $\pi/4$ gives

\[
B\le\frac{2sp+\pi s^2}{\pi/4}=\frac{20p}{\pi}+25.
\]

At any $x\in P$, its Delaunay neighbors are within distance two. The disjoint open radius-$1/2$ disks centered at $x$ and at all its neighbors lie in the radius-$5/2$ disk about $x$. Their area ratio is 25, so the Delaunay degree is at most 24, including in co-circular configurations after triangulation.

### Triangle excess and Euler accounting

For any Delaunay triangle, all side lengths are at least one and its circumradius $R\le1$. Since $\sin\alpha=L/(2R)$, every angle is at least $\pi/6$; hence every angle is at most $2\pi/3$. At least one angle is at most $\pi/3$, so its opposite side, which is at least one, gives $R\ge1/\sqrt3$. At fixed $R$, all angles are at least $\ell=\arcsin(1/(2R))$. Concavity of $\log\sin$ shows that the minimum area occurs when two angles are $\ell$. That area is

\[
\frac{\sqrt{4R^2-1}}{4R^2}\ge\frac{\sqrt3}{4}=a,
\]

since the function has its minimum at $R^2=1/3$ or $R^2=1$. Hence every triangle excess is nonnegative.

The union of the finitely many triangles in $\mathcal T_C$ is a finite planar simplicial complex. Let $V,E,T$ be its vertex, edge, and triangle counts; let $b_C$ be its number of edges incident to only one contained triangle; and let $\chi_C$ be its Euler characteristic. Then

\[
3T=2E-b_C,\qquad \chi_C=V-E+T,
\qquad T=2V-b_C-2\chi_C.
\]

Every point of $P\cap C$ farther than two from $\partial C$ has its whole Delaunay star in $C$, because every neighbor is within two and $C$ is convex. In particular, if $I$ is the number of deep original source points, $I\ge z-B$. Every boundary edge of the complex has both endpoints in the strip: a deep endpoint would have both Delaunay triangles across that edge contained in $C$. Every nonempty component has a strip vertex, since a finite planar union of triangles has a boundary edge. Thus $b_C\le24B$, the number of components is at most $B$, and $\chi_C\le B$. It follows that

\[
T\ge2I-26B\ge2z-28B.
\]

Contained triangle interiors are disjoint, so their total area is at most $Q$. Therefore

\[
\Sigma\le Q-aT
\le Q-a_0z+28aB
=a_0S-a_0(p/2+1)+28aB
\le a_0S+28aB.
\]

This counts all deep original points and does not discard any source isolates.

### Exceptional vertices and local shape

Mark every strip vertex and every vertex of a contained triangle incident to a strip vertex. There are at most $B+3(24B)=73B$ such vertices. Every remaining deep vertex has all its incident triangles contained in $C$, and all vertices of those triangles are deep.

If a contained triangle all of whose vertices are deeper than two from $\partial C$ is right or obtuse, let $\alpha\in[\pi/2,2\pi/3]$ be its largest angle and $L$ its opposite side. Then $L^2\ge2(1-\cos\alpha)$. The Delaunay neighbor across $L$ has a third vertex within two of an endpoint, hence lies in $C$; convexity makes that neighboring triangle contained. If its opposite angle is $\beta$, the local Delaunay inequality gives $\beta\le\pi-\alpha\le\pi/2$. The other two neighbor angles are at least $\pi/6$, so their sine product is at least $\tfrac12\sin(\beta+\pi/6)$. Its area is therefore at least

\[
\frac{L^2}{4}\left(\frac{\sqrt3}{2}+\frac12\cot\beta\right)
\ge\frac{\sqrt3}{4}(1-\cos\alpha).
\]

The original triangle's area is at least $\tfrac12\sin\alpha$. The sum of the two triangle excesses is at least

\[
\frac12\sin\alpha+\frac{\sqrt3}{4}(1-\cos\alpha)-2a
\ge\frac{2-\sqrt3}{4}=\delta,
\]

The displayed function is increasing on $[\pi/2,2\pi/3]$: its derivative is decreasing there and equals $1/8>0$ at $2\pi/3$. Thus its minimum is at $\alpha=\pi/2$. Any contained triangle is charged in at most four such pairs: once as a right/obtuse triangle and at most once for each of its three edges as a neighbor. Thus there are at most $4\Sigma/\delta$ deep right/obtuse triangles, accounting for at most $12\Sigma/\delta$ more vertices.

There are at most $100\Sigma$ contained triangles with excess at least $1/100$, accounting for at most $300\Sigma$ vertices. For every remaining deep vertex, all incident triangles are acute with excess below $1/100$.

For an acute triangle with individual excess $e<1/100$, let $L$ be its largest side. If $L\ge\sqrt2$, write $x,y$ for the squares of the other sides. Heron gives $16A^2=4xy-(x+y-L^2)^2$, a concave function on $1\le x,y\le L^2$, $x+y\ge L^2$. The polygon has vertices $(1,L^2-1)$, $(1,L^2)$, $(L^2-1,1)$, $(L^2,1)$, and $(L^2,L^2)$; the expression is at least $4(L^2-1)\ge4$ at each. Hence $A\ge1/2>a+1/100$. If $L<\sqrt2$, the altitude over $L$ is at least $\sqrt{1-L^2/4}$, so area is at least

\[
f(L)=\frac{L\sqrt{4-L^2}}4.
\]

The function $f$ is increasing on $[1,\sqrt2]$, $f(11/10)>a+1/100$, and $f'(L)=(2-L^2)/(2\sqrt{4-L^2})>1/5$ on $[1,11/10]$. Hence $L<11/10$ and $L-1\le5e$. All three sides are in $[1,11/10]$, and the segment from these side lengths to $(1,1,1)$ stays in the acute-triangle region. For any angle opposite side $a_1$ with adjacent sides $b_1,c_1\in[1,1.1]$, the cosine law gives $79/242\le\cos\alpha\le71/100$, hence $\sin\alpha>7/10$. The opposite-side angle derivative is $a_1/(2A)<1.1/(7/10)<2$; the adjacent-side derivatives are bounded by $1.42/(2(7/10))<2$. Consequently each angle differs from $\pi/3$ by at most $2\cdot3\cdot5e=30e$, which implies the stated looser bound $50e$.

At a remaining deep vertex with $k\ne6$ incident triangles, the angle sum is $2\pi$, so the sum of absolute deviations from $k\pi/3$ is at least $\pi/3$. The $50e$ bound forces its incident excess sum to be at least $\pi/150>1/50$. Summing incident excess over all vertices counts each triangle three times, so at most $150\Sigma$ such vertices remain. Together the exception bound is

\[
73B+\left(\frac{12}{\delta}+300+150\right)\Sigma
=73B+\left(\frac{12}{\delta}+450\right)\Sigma.
\]

This is local near-equilateral control only. It does not give a single global lattice chart through holes or across defect locations.

## 4. Dependency and scope audit

- Oler's inequality is the canonical shared-theory Lemma 21.1 in `docs/theory/03-oler-shell.md`. It applies directly to the finite unit-separated set \(P\cap C\).
- The completion, Delaunay degree
- The theorem applies to arbitrary finite feasible sources and arbitrary convex polygon crops. It is not a theorem about global minimizers and does not produce an admissible competitor.
- The source report's separate exterior one-site saturation proof and the asserted applications to canonical cap branches were not audited here and are not promoted.
- A Delaunay edge can have any length in $[1,2]$; it is not automatically a source contact. The defect skeleton cannot be treated as a contact graph or a packet without a source-level realization theorem.
- When $S,p=O(D)$, this gives $B,\Sigma$, and the exceptional vertex count $O(D)$. This is geometric bookkeeping, not spare packing capacity, a strict-safe site, or a diameter/contact payment.
- One completion is shared across multiple containers, but Σ from overlapping containers is not additive and cannot be charged twice. No global chart is claimed; reduced lattice-position hypotheses remain subject to the canonical bent-grid regression `C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION`.

## 5. Certificate audit

The frozen verifier was inspected and run from the immutable source worktree:

```text
PYTHONPATH=research python3 research/verify_target_c_coupled_container_crop_2026_10_07.py
```

It uses exact rational and \(\mathbb Q(\sqrt3)\) arithmetic. Six explicit lattice crops (`M=7,13,25`, with triangular and rational-rhombic cases) check finite pair-distance inequalities, strip membership, deep valence, boundary edges, components, Euler accounting, Oler allowance, triangle excess, and the asserted currency inequality. It passed on all six cases. The helper module uses exact `Fraction` arithmetic in \(\mathbb Q(\sqrt3)\).

This certificate tests six explicit lattice examples only. It does not verify arbitrary saturation, the tube estimate for arbitrary convex polygons, the universal Euler proof, canonical source geometry, a finite exchange, or global optimality. The analytic proof above carries those claims.

## 6. Regression checks and nonclaims

| Failure mode checked | Audit disposition |
| --- | --- |
| Delaunay edges silently treated as unit contacts | Rejected as an application; lengths are only bounded by two. |
| Holes, multiple components, or triangles meeting at vertices omitted from Euler accounting | Included via a finite planar simplicial complex and \(\chi\le c\). |
| Boundary edges or missing deep source labels dropped | Boundary edges have strip endpoints; every deep source label has its full star. |
| Contact-isolated source points deleted | None are deleted; the completion starts from all of (A). |
| A finite local lattice chart inferred to be one global lattice position cover | Not claimed; the canonical bent-grid regression blocks that reduced-input implication. |
| Oler allowance or positive triangle-area excess treated as a spare site | Not claimed. |
| Feasible local packing or scaffold treated as a global minimizer | Not claimed. |

No counterexample to the narrowed geometric transfer was found.

## 7. Exact frontier effect and remaining lemma

**Verdict: PASS — promote `C-COUPLED-DELAUNAY-CONVEX-CONTAINER-TRANSFER`.** This is a reusable arbitrary-container crop theorem. It gives a common near-triangular Delaunay skeleton with an exact (O(S+p)) boundary/excess budget, but it does not eliminate the macroscopic-container C-II route or change the global endpoint.

The next lemma is: from this actual common skeleton inside a canonical macroscopic container, construct one same-cardinality source competitor that retains all source isolates and checks every old lower pair, every actual-diameter upper pair, contact count, triangle-freeness, and all inserted-to-retained pairs, then either loses a contact at diameter (D), loses an actual diameter pair at equal contact count, or has diameter strictly below (D).

## 8. Promotion recommendation

Promote only the crop theorem under the exact hypotheses in Section 2. Do not promote the report's Section 5 one-site claim, its cap-source applications, a global chart, or any C-II/Level I consequence. The active Target C endpoint remains open; update the route and prompt to record this new tool and its remaining movement/payment obligation without declaring the branch closed.
