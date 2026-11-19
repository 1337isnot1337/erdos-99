# How much of a diameter extremum can be accounted for by its outermost unit layer?

OpenAI Codex, November 17, 2026. Unreviewed research on the full quantifiers of Erdős Problem 99. The starting branch was `6acad14`, with upstream main `b05cd57`, state `2026-10-15.publication.2` and priority `public-frontier.3`.

Write $a_0=\sqrt3/2$ and $a=\pi/(4a_0)$. For a finite unit-separated planar source $A$ let $K=\operatorname{conv}A$, $D=\operatorname{diam}A$, and call the centers at distance less than one from $\partial K$ the outer layer. All deeper labels are unrestricted.

We test a possible contradiction to the repository's [linear population reserve](../../docs/reports/population_reserve_independent_reconstruction_2026-10-15.md). Earlier [lattice comparison](../../docs/reports/global_lattice_defect_from_linear_reserve_2026-10-11.md) required matching nearly the entire source to one lattice. The first result below needs a match only in the outer layer. The second lets the lattice phase change at mesoscopic scales and identifies the contribution of boundary tangents parallel to lattice rows. Neither step derives a lattice description from the absence of an exact unit triangle.

## 1. Local area assigned to a point

Put $r=1/\sqrt3$. For a unit-separated set, the intersection of the Voronoi cell of a site $p$ with $B(p,r)$ has area at least $a_0$. The cells used here have disjoint interiors, also for a locally finite periodic set. The disk truncation is classical, as in [Hales's packing lecture](https://media.pims.math.ca/pdf/activities/dist_lect/2006/Hales/Hales_Lecture1.pdf).

Here is a direct proof. Another site cuts off a circular segment of half-angle $\alpha\le\pi/6$, because the bisector is at distance at least $1/2$. The open cut-off segments are disjoint. A point in an overlap in the open disk would be the center of a disk of radius strictly below $r$ containing three unit-separated sites. Of three rays to those sites two make angle at most $120$ degrees, and two points on such rays at radii at most $s$ are at distance at most $\sqrt3s$ (maximize the squared distance on the square of radii). This is impossible for $s<r$. Hence $\sum\alpha\le\pi$. A segment costs $r^2(\alpha-\sin\alpha\cos\alpha)$ in area. The factor in parentheses is convex on $[0,\pi/6]$ and vanishes at zero. The lost area is at most the cost of six maximal segments, leaving the area of the regular unit-lattice hexagon, namely $a_0$. Only neighbors within $2r$ affect this calculation. At separation $1-\epsilon$ the same argument gives area $a_0(1-\epsilon)^2$ inside radius $(1-\epsilon)r$.

## 2. A finite comparison using only the outer layer

Let $D\ge1$ and $K$ be two-dimensional. Fix any translate and orientation $\Lambda$ of the unit triangular lattice and $0\le\epsilon\le1/10$. Let $k$ be the number of outer-layer labels farther than $\epsilon$ from $\Lambda$, and put $K_\epsilon=K+B(0,\epsilon)$. Then
$$
 |A|\le k+|\Lambda\cap K_\epsilon|+256\epsilon(D+2).                 \tag{1}
$$
In particular at $\epsilon=0$ the comparison with the crop has no boundary-error term.

**Proof.** In a large rectangular period cell of $\Lambda$, remove precisely its sites inside $K_\epsilon$ and insert the source except for the $k$ exceptional labels. Repeat by the periods. One may choose orthogonal periods in any orientation of the triangular lattice, with both lengths exceeding $10(D+2)$, and place the hole well away from the cell boundary by the choice of fundamental domain. Same-type distances are at least one, including between source copies. A retained exterior site cannot be within one of a source point deeper than or on the inner rim of the outer layer. For a remaining outer label, its approximating lattice site belongs to $K_\epsilon$ and has been removed. Every retained lattice site is therefore at distance at least $1-\epsilon$ from the source label. This verifies separation for the entire periodic configuration.

Use the truncated cells from Section 1. At every site more than three units from $\partial K$ and its periodic copies, the local configuration out to $2r$ contains points of just one type, with full unit separation. Its cell area is at least $a_0$. Elsewhere the cell still has area at least $a_0(1-\epsilon)^2$. In each period at most $128D+256$ sites are within distance three of the boundary. Indeed their disjoint quarter-unit disks fit in the width-four two-sided boundary strip, of area at most $8P+16\pi$, where $P\le\pi D$ is the perimeter. The outer strip estimate is Steiner's formula. The inner strip of a convex polygon is covered by inward rectangles based on its sides. Integrating the disjoint cells on the torus and comparing with the original number of lattice sites (cell area divided by $a_0$) proves (1).

## 3. A uniform lattice population bound at exponent two thirds

For any finite subset $S$ of a translated rank-two unit-separated lattice and $d=\operatorname{diam}S\ge1$,
$$
 |S|\le a d^2+55d^{2/3}+1.                                               \tag{2}
$$
This estimate counts all sites, including collinear boundary sites. The argument sharpens the $O(d^{4/5})$ bound in the earlier lattice comparison by summing over all hull sides at once.

Put $Q=\operatorname{conv}S$, $R=d/2$, $L=(Q-Q)/2$ and $\Delta=\pi R^2-|Q|$. By Brunn–Minkowski, $|Q|\le|L|$, and $L\subset B(0,R)$. A two-dimensional lattice of minimum distance at least one has covolume at least $a_0$ by reducing a basis along a shortest vector. Pick's theorem gives $|S|\le |Q|/a_0+B/2+1$ with $B$ the number of lattice sites on the polygon boundary. Write $\ell_i$ for the merged oriented side lengths of $Q$ and $u_i$ for the corresponding distinct primitive lattice vectors. Then $B=\sum\ell_i/|u_i|\le\pi d$. Collinear sets satisfy (2) directly. For $d<16$ the bound follows from Pick and $B\le\pi d$. We may assume $d\ge16$ and $|S|\ge a d^2$, hence $\Delta\le a_0(\pi d/2+1)$. The inradius of $L$ about zero is at least $R/2$, since cutting the disk at distance $R/2$ would cost $R^2(\pi/3-\sqrt3/4)>a_0(\pi d/2+1)$.

For a side of $L$ write its points as $(h,y)$, $v\le y\le v+s$, in normal coordinates, so $h\ge R/2$. The missing disk area in its radial sector is
$$
 \frac h2\int_v^{v+s}\left(\frac{R^2}{h^2+y^2}-1\right)dy
 \ \ge\ \frac{h}{2R^2}\int_v^{v+s}(R^2-h^2-y^2)dy
 \ \ge\ \frac{s^3}{24R}.
$$
For the last step, the endpoints give $R^2-h^2\ge(|v+s/2|+s/2)^2$, so the integral is at least $s^3/6$. The radial sectors have disjoint interiors. Each oriented side of $Q$ contributes to a distinct oriented side of $L$ of length at least $\ell_i/2$, by Minkowski addition. Thus $\sum\ell_i^3\le96d\Delta$.

Disjoint half-unit disks give $N(t)\le9t^2$ for the number of nonzero lattice vectors of length at most $t\ge1$. Summation by parts gives $\sum_{0<|u|\le T}|u|^{-3/2}\le36\sqrt T$. Split $B$ at $T=d^{1/3}$. Hölder's inequality bounds the short-vector contribution by $(96d\Delta)^{1/3}(36\sqrt T)^{2/3}$, and the remaining contribution is at most $\pi d/T$. Substitution in Pick's inequality gives
$$
 |S|-ad^2-1\le-\Delta+25d^{4/9}\Delta^{1/3}+(\pi/2)d^{2/3}.
$$
The maximum of $-x+25x^{1/3}$ on $x\ge0$ is less than 49. Substitute $x=\Delta/d^{2/3}$ to obtain (2).

**Conditional global consequence.** If a global minimizer satisfies the repository's unreviewed $|A|-1\ge aD^2+D/600$ reserve, (1) and (2) give, for **every** triangular lattice and $\epsilon=10^{-6}$, at least $D/1000$ labels in the outermost unit layer farther than $\epsilon$ from that lattice for all sufficiently large $D$. The error $55(D+2\epsilon)^{2/3}$ is sublinear. The deeper part of the packing can vary without restriction. Equations (1) and (2) themselves are unconditional.

## 4. Varying phases and orientations along the same boundary

Consider a sequence with $D\to\infty$, convex hulls $K$, perimeter $P$ and incenters $o$. Assume the inradius is $D/2-O(\sqrt D)$. This holds for every global minimizer by the repository's [full-source geometry estimate](../../docs/targets/target-c/58-full-source-geometry-audit.md). Then $K$ lies in the concentric circle of radius $D-r_{\rm in}$ by the opposite point of its inball. In particular $P\sim\pi D$.

Partition the boundary in its circular order into $J=o(D)$ arcs, using rays from $o$ through their endpoints to partition the outer layer. In each sector choose an independently translated and rotated unit triangular lattice. Assume that, after omitting $k$ outer-layer labels, the remaining outer-layer labels are within $\epsilon_D=o(1)$ of the lattice of their sector. There is no requirement to occupy all its sites or to continue it into the interior. The number $k$ stays in the bound and can vary with $D$.

For each arclength point record the direction tangent to the circle about $o$ there, expressed in the reference frame of its sector lattice. Use counterclockwise orientation, with the counterclockwise right angle from the outward radial vector to the tangent. Let $\mu_D$ be the resulting arclength probability distribution of directions. For any subsequence on which $\mu_D$ converges weakly to $\mu$, define $h(t)=a_0/|v|$ if $t$ is parallel to a primitive reference lattice vector $v$, and $h(t)=0$ otherwise. The lattice's sixfold frame ambiguity can be fixed arbitrarily sector by sector since $h$ has that symmetry. Then
$$
 \limsup\frac{a_0(|A|-k)-|K|}{P}\ \le\ \frac12\int h(t)\,d\mu(t).       \tag{3}
$$
In particular arbitrarily varying translations with a bounded number of lattice orientations give a zero right-hand side. Indeed physical polar angles have an asymptotically uniform arclength distribution. At each differentiability point of the radial parametrization its speed is $|x-o|^2/h_K(N)$ in coordinates based at $o$, with $N$ the outward normal there. Both radii and support values are uniformly $D/2+O(\sqrt D)$. Finitely many rotated restrictions of this angle distribution have atomless limits, also for orientations varying along the sequence by passing to a convergent subsequence of the finite list. The directions with $h>0$ form a countable set.

### Weighted exterior comparison

Here and below one first fixes $W\ge10$, takes $D\to\infty$, and only then lets $W\to\infty$. Use a nonincreasing $C^2$ function $F_W(s)=F(s/W)$ on $s\ge0$, equal to one up to $s=W/4$, zero from $s=W$ onward, with $0\le F\le1$. Use the weight $f(x)=F_W(\operatorname{dist}(x,K))$ including value one on $K$. Its gradient is Lipschitz with constant $C/W^2$. Indeed squared distance to a closed convex set has gradient twice the nonexpansive residual of metric projection. On the transition band its gradient is $O(W)$, and $F_W(s)$ there is a smooth function of $s^2/W^2$.

Add exterior sites of each assigned lattice whose centers are in its sector, outside $K_{\epsilon_D}$, within $W+3$ of $K$, and at distance greater than two from sector boundary rays. Delete the $k$ exceptional labels first. These added sites within one sector are separated by one, and distinct sectors' added sites are separated by one as well: a segment between sectors must cross a separating ray. Across types the separation is at least $1-\epsilon_D$, since any source label at distance less than one from an added site is in its sector and in the original outer layer. All sites are accounted for, including uncharged deeper source points.

For this union, integrate $f$ over disjoint radius-$r$ truncated Voronoi cells. Source cells deeper than three have full unit-separation area and lie in the unit-weight region for large $W$. Source and added cells within three of $\partial K$ lose at most $C(\epsilon_D+1/W)$ per site in comparison with $a_0 f(p)$, by Section 1 and the Lipschitz bound on $f$; there are $O(D)$ such sites. For an added site of positive weight more than three from $K$ and more than four from a sector seam, all six neighbors are present and nothing else cuts its regular hexagon. The first moment about its center is zero. Taylor's inequality bounds the weighted integration error by $C/W^2$ per site; their count is $O(DW+W^2)$. The seam exceptions among the added sites cost $O_W(J)$ in total. To see the count, points out to fixed distance $W+4$ from $\partial K$ and within four of a ray lie in a rectangle of dimensions $O_W(1)$ at the ray's boundary crossing. Uniformly at every such crossing the radial vector makes angle $O(D^{-1/4})$ with any outward normal, by the concentric inball and outer ball estimates. Equivalently the local radial graph has angular slope $O(D^{3/4})$ and the fixed-width polar tube meets the ray transversely. Packing disjoint small disks bounds the count, even if some rectangles overlap. It also allows all would-be added sites excluded near seams to be restored to the following **numerical sum** at cost $O_W(J)$, counting each only in its assigned sector. We get
$$
 a_0(|A|-k)-|K|
 \le \int_{K^c}f(x)\,dx
     -a_0\sum_j\sum_{g\in\Lambda_j\cap S_j\setminus K_{\epsilon_D}} f(g)
     +O(D/W+\epsilon_D D)+O_W(J+1).                                      \tag{4}
$$
Here $S_j$ denotes a sector with an arbitrary consistent convention at its bounding rays. Sites outside the support of $f$ have zero weight. The constants multiplying $D/W$ and $\epsilon_D D$ are absolute for the chosen cutoff.

### Long straight strips

For clarity we prove the counting fact needed to pass to the limit in (4). In one fixed triangular lattice consider rectangles of length $l_i\to\infty$ in tangent directions $t_i\to t$, with arbitrary origins and perpendicular coordinates $s$ along the outward normal $n_i$. Form the locally finite measures on the $s$-axis which count projected lattice sites per unit length, keeping tangent coordinate in a segment of length $l_i$. In any bounded transverse interval these measures have uniformly bounded mass by disjoint disks. A vague subsequential limit $\nu$ is invariant under translation by every $u\cdot n$ for $u$ in the lattice of differences and $n=\lim n_i$. Indeed translating an entire window by $u$ changes its two endcaps by only $O_u(1)$ sites on bounded transverse intervals, and continuous test functions absorb the convergence of $u\cdot n_i$. The mass in any long transverse interval of length $H$ is $H/a_0+O(1)$ in the limit: tile the plane by fundamental hexagons and sandwich the window by rectangles enlarged or eroded by their circumradius. The boundary errors before division are $O(H+l_i+1)$.

If $t$ has irrational lattice slope, the transverse translations are dense. Then $\nu=ds/a_0$ by translation invariance and the mass normalization. Otherwise their group is $h\mathbb Z$ with $h=a_0/|v|$ for the primitive parallel vector. Now $\nu$ is $h$-periodic, with mass $h/a_0$ per half-open period. Its integral on the open positive axis against $F_W$ is at least $(h/a_0)\sum_{j\ge1} F_W(jh)$: partition into periods $(jh,(j+1)h]$ and use monotonicity. The trapezoid rule on those periods, with $F_W(0)=1$ and $\sup|F_W''|=O(W^{-2})$, gives
$$
 \int_0^\infty F_W(s)\,ds-a_0\int_{(0,\infty)} F_W\,d\nu
 \le h/2+C/W.
$$
For irrational slope the difference is zero. Taking the open positive axis permits a whole row at zero to be absent from the added sites. This tie is essential to the coefficient $1/2$.

### From the curved hull to the strips

Subdivide the given arcs into windows at scale $l=\min(D^{1/16},\sqrt{D/(J+1)})$. In each original arc use pieces of length between $l$ and $2l$ whenever its length permits this. Original arcs shorter than $l$ have total length $O(Jl)=o(D)$, and their bounded strip contributions are $O_W(Jl+J)=o(D)$. On any retained window the radial normal at its midpoint differs from the polygon's supporting normals by $O(D^{-1/4}+l/D)$. Therefore its boundary is a graph over the central tangent and differs from its tangent-coordinate line through the midpoint by $o(1)$ in normal position, uniformly over the window. This uses $lD^{-1/4}+l^2/D=o(1)$. Supporting normals for the fixed-width parallel curves obey the same estimates. At fixed $W$ the radial cuts at the ends, and perpendicular ends of a tangent-coordinate rectangle, differ by strips of bounded area per end (indeed $O_W(1)$). The tangent-coordinate length divided by the arc length tends to one uniformly.

Consequently the integral contribution per unit length in (4) is $\int_0^\infty F_W(s)ds+o(1)$ on each window. In the lattice sum one may keep only $s$ in a compact subinterval of $(0,\infty)$ before taking a lower limit. Sites there are on the exterior side of $K_{\epsilon_D}$ for large $D$, and their weights are $F_W(s)+o(1)$ uniformly at fixed $W$. The long-strip result gives an upper limit of $h(t)/2+C/W$ for the difference per unit length along every sequence of windows whose relative tangent directions converge to $t$. The differences are uniformly bounded at fixed $W$ by the strip counts. End errors sum to $o(D)$.

To justify averaging these bounds over changing directions, the arclength-weighted joint distributions of window directions and their differences per unit length have weakly convergent subsequences on a compact set. Every support point $(t,e)$ of a limit is approached by windows, so $e\le h(t)/2+C/W$. Its direction marginal is $\mu$, since radial tangents change by $o(1)$ on each window. Integrating and using (4), then sending $W$ to infinity, proves (3). This proof uses no uniform onset of equidistribution over irrational slopes.

**Consequence for the full question.** On the proposed linear reserve, $a_0|A|-|K|\ge (a_0/600)D$ for large minimizers. If the number of exceptional layer labels is $o(D)$, (3) forces limiting positive arclength mass along directions parallel to lattice rows in their respective local frames. More quantitatively $\int h\,d\mu\ge 2a_0/(600\pi)$. In particular boundedly many orientations, even with arbitrarily varying sector phases and an entirely unrestricted interior, cannot account for all but $o(D)$ outer labels. The analysis permits absent lattice sites in the matched regions.

## What remains to prove

A hypothetical triangle-free minimizer can evade the contradiction through a positive density of unmatched outer-layer sites or through lattice orientations that track the boundary tangent on a positive fraction of its length. Closing the problem requires a source-specific argument against those alternatives or a different global competitor. The two-sided contact constraints in the actual interior were not converted to a cost for either alternative here. All mathematical claims above remain unreviewed.
