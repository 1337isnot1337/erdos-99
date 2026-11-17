# Radial replacements and near-unit paths from diameter endpoints

AI-assisted research by OpenAI Codex, November 17, 2026. Unreviewed proof candidate. Baseline `b05cd57b15252fe99577de3edb0b73070e79544f`, theorem state `2026-10-15.publication.2`, priority `public-frontier.3`.

The question is whether every sufficiently large diameter minimizer contains a unit equilateral triangle. Here the comparison retains all labels. It gives a strict competitor for a class that defeats every two-similarity replacement. For a general putative triangle-free minimizer it forces long paths of nearly touching points from every diameter endpoint. The universal contradiction is open.

## 1. Exactly three similarity copies suffice for the separated regular odd rim

Take the vertices of a regular unit-sided odd polygon with $q\ge33$ vertices, center $o$, circumradius $R=1/(2\sin(\pi/q))$ and diameter $D=2R\cos(\pi/(2q))$. Add any unit-separated set strictly inside the polygon with every rim-to-interior distance at least $1+3/R$. The number, minimum internal slack and contact graph of the interior set are arbitrary.

Keep one rim vertex and all interior points fixed. In cyclic order on the remaining even-length path, alternately replace $p$ by $o+(1-a/R^2)(p-o)$ for $a=1,3$. Write $a=0$ for the identity. This uses three common similarities, with maximum displacement $3/R$. The resulting set is unit-separated and has strictly smaller diameter.

Indeed, for two rim points originally at distance $l$, the new squared distance is
$$
 (a-b)^2/R^2+(1-a/R^2)(1-b/R^2)l^2.
$$
If $a\ne b$ in $\{0,1,3\}$ then $(a-b)^2\ge a+b$. Since $l\ge1$, the displayed quantity is at least one. Same-class distinct rim points are nonconsecutive and have original distance at least $2\cos(\pi/q)$. Since $R>5$, their new distance is at least $(1-3/25)2\cos(\pi/33)>1$. Interior pairs retain their lengths. The stated rim-to-interior clearance pays the largest displacement. Every moved point is strictly inside the original hull. An interior point of a diameter-$D$ convex body is strictly less than $D$ from every point in the body, by extending their joining ray a little past the interior point. Only one rim vertex stays fixed. This proves the strict upper bound for every pair.

Two arbitrary similarities cannot achieve this endpoint. Both the unit rim edges and the longest rim diagonals form odd cycles, the latter because $\gcd(q,(q-1)/2)=1$. If both copies are contracting the contact cycle would have to be bipartite. If neither is contracting the diameter cycle would have to be bipartite. In the mixed case each copy can contain at most $(q-1)/2$ rim labels, by independence in its respective cycle. This reconstructs the repository's [two-copy obstruction](../../docs/reports/global_two_copy_similarity_obstruction_2026-10-12.md). Its full family has rim-to-interior distances greater than four and meets the clearance above.

The displacement order is sharp even for arbitrary labeled planar replacements. If every rim label moves less than $1/(4R)$, each remains uniquely exposed by its original outward radial normal. Its initial lead over every other rim label in that direction is at least $R(1-\cos(2\pi/q))=1/(2R)$. The rim labels therefore still form a convex $q$-gon, whose perimeter is at least $q$ by unit separation. The polygonal perimeter bound $P\le2q\sin(\pi/(2q))\operatorname{diam}$ gives diameter at least $D$. The [odd-rim report, Section 2](../../docs/reports/global_convexity_exit_barrier_2026-10-12.md) proves the perimeter bound using the difference polygon. This argument concerns the endpoint itself and needs no continuous path.

## 2. Ordering the radial changes when the interior is occupied

Here is a necessary condition for the full problem. Fix a noncollinear triangle-free global minimizer with the fewest contacts among such minimizers at its cardinality, then the fewest actual diameter pairs. These successive integer minima exist if a counterexample exists. Let $D$ denote its diameter and take **any** interior origin $o$ with $\max_i |p_i-o|\le9D/10$. Such an origin exists. Every source point is within $\sqrt3 D/2$ of the midpoint of a diameter, by the parallelogram identity, and interior points approach that midpoint.

Fix $0<\epsilon\le1/2$ and $L=\lfloor\sqrt{D\epsilon}/64\rfloor\ge1$. On every source label put the graph of distances at most $1+\epsilon$. Split radii into bins of width $w=1/(32D)$ using the index $\lfloor |p_i-o|/w\rfloor$. Order the labels by decreasing bin, breaking ties in **any** total order. Orient graph edges from earlier to later labels.

**Claim.** From **every** actual diameter endpoint there is a directed path with at least $L$ edges. One can choose the order so every such path visits at least $\lceil(L+1)/16\rceil$ distinct radial bins.

**Proof.** Suppose an actual diameter endpoint $p$ has no such path. Move the labels reachable from $p$, including $p$ itself. Give each reachable label $i$ the integer $k_i$ equal to one plus the longest path length from $p$ to $i$, so $1\le k_i\le L$. Give every other label index zero. On any graph edge incident with the moved set, the earlier endpoint has strictly smaller index. Indeed, the successor of any reachable predecessor is reachable and its longest path is longer. An unreachable predecessor of a reachable label has index zero.

Put $r=D/16$, $T_k=k(k+1)/2$, and $\lambda_k=1-2T_k/r^2$. Replace every $p_i$ by $o+\lambda_{k_i}(p_i-o)$. All moved points, and their graph neighbors, have radius at least $r$. In fact $|p-o|\ge D/10$ since a diameter partner has radius at most $9D/10$. Each relevant point is within $(1+\epsilon)L\le3L/2$ of $p$. The definitions imply $3L/2\le3D/80$. Also $0<\lambda_k\le1$ and every displacement is at most $512L^2/D\le\epsilon/8$. For positivity one can use $2T_k/r^2\le512L^2/D^2\le\epsilon/(8D)<1$. Thus even the sum of two displacements is less than $\epsilon$. Every original distance exceeding $1+\epsilon$ stays strictly greater than one.

Consider a remaining pair incident to the moved set. Write $a<b$ for its indices in forward order, $s_a,s_b$ for its original radii, and $l\ge1$ for its length. Its new squared length is exactly
$$
 \lambda_a\lambda_b l^2+
 (\lambda_a-\lambda_b)(\lambda_a s_a^2-\lambda_b s_b^2).
$$
We have $s_a^2-s_b^2\ge-2Dw$ even when the within-bin order is opposite to radius order. With $d=T_b-T_a$ and $\delta=\lambda_a-\lambda_b=2d/r^2$, the second summand is at least
$$
 \delta^2 r^2-2Dw\delta=(4d^2-4Dw d)/r^2.
$$
Here $d^2\ge T_a+T_b$ for distinct nonnegative integer indices. Equality holds for consecutive indices, by $T_{a+1}+T_a=(a+1)^2$, and increasing $b$ only increases the difference of the two sides. Since $d\ge1$ and $4Dw=1/8$, the last lower bound strictly exceeds $2(T_a+T_b)/r^2\ge1-\lambda_a\lambda_b$. The new pair is strictly longer than one. Unmoved pairs retain their lengths. This checks contacts, near contacts, and contact-isolated labels.

Every moved point is now strictly inside the old convex hull. Consequently all pairs incident with a moved label have distance strictly less than $D$, even if both labels moved. No new contact or diameter pair appears, and at least one old diameter pair disappears at $p$. The endpoint remains triangle-free. If its diameter decreased it contradicts global minimality. Otherwise it contradicts the successive integer minima. This proves the path claim.

Finally, each vertex and all its graph neighbors have disjoint open half-unit disks inside a disk of radius two. Their number is at most 16 by area. Greedily color the graph with 16 colors. Break within-bin ties by increasing color and then by label. A path cannot spend more than 16 consecutive vertices in a bin or return to it after leaving. This proves the bin count.

### A consequence for every global minimizer

For any noncollinear global minimizer, with or without triangles, and for **every** allowed origin, tolerance and order above, there is an actual diameter pair both of whose endpoints start paths of at least $L$ edges. Indeed, otherwise the short-path endpoints cover the diameter graph. Use all of them as starting labels simultaneously. On their union of forward closures use one plus the longest path length from any starting label. The same bound $L$, radius bound, and pair calculation hold verbatim, since every reachable label has a starting endpoint within $(1+\epsilon)(L-1)$. Every old diameter now has a moved endpoint. The new diameter is strictly smaller, with no need to select a lexicographically minimal representative.

### Dense sources that meet this condition for every order

The existence of these paths does not characterize globality even to linear accuracy in disk population. Start with **any** $M$ unit-separated points in a radius-$R$ disk, $R$ sufficiently large and $M\ge R$. About its center, dilate by $1+R^{-2}$. Put $S=R+2/R$, $D=2S$, and $m=\lceil\sqrt D\rceil$. Insert the two horizontal unit chains
$$
 (S-j,0),\quad(-S+j,0),\qquad 0\le j\le m.
$$
First delete all dilated labels at distance at most one from either chain. This costs $O(m)$ labels with an absolute constant: disjoint half-unit disks about the deleted points lie in the union of the radius-$3/2$ neighborhoods of two segments of length $m$. If necessary, delete additional old labels until the final cardinality is at most $M$. This costs at most $2(m+1)$ more, and enough old labels exist since $M\ge R$. Thus the resulting cardinality is between $M-O(\sqrt D)$ and $M$. Its contact graph consists of the two paths and isolated vertices. Only the two outer tips lie on the radius-$S$ circle, so they form the unique diameter pair. An equal-cardinality subset of the original input has diameter at most $2R<D$.

Nevertheless, for **every** permitted origin $o$ the entire two chains are directed paths inward for **every** within-bin order. Their outer tips force $|o_x|\le0.8S$ from the bound $\max_i|p_i-o|\le1.8S$. On the right chain a step left from coordinate $x$ decreases squared distance to $o$ by $2(x-o_x)-1\ge2(0.2S-m)-1$. Dividing by the sum of the two radii, at most $3.6S$, gives a radial decrease greater than $1/32$ for all sufficiently large $S$. The left chain satisfies the reflected bound. This exceeds the bin width. Actual unit edges qualify for every positive tolerance and $m\ge L$. Thus the same pair passes the global path test in every permitted ordering.

One can start from a maximum-cardinality disk packing. In particular, if one uses the repository's [linear disk population lower-bound candidate](../../docs/reports/population_reserve_independent_reconstruction_2026-10-15.md), this construction preserves its asymptotic linear reserve coefficient, since the area change is $O(1)$ and the population loss is $O(\sqrt D)$. The construction and its strict nonglobality do not depend on that external-to-this-proof estimate.

## 3. How far a single translation can propagate

The preceding reachability argument uses a different scale factor at each index. There is also a full-distance consequence for one fixed translation. In the same lexicographic source let $B(o,r_0)\subset K=\operatorname{conv}A$, let $p$ be any actual diameter endpoint, and let $N=(p-o)/|p-o|$. For any $0<t<r_0$ put an arc $x\to y$ between distinct labels when $|x-tN-y|\le1$. Then some directed path from $p$ reaches a point at Euclidean distance at least $r_0-t$ from $p$. Each of its edges has length at most $1+t$ and decreases projection onto $N$ by at least $t/2$. In particular the path has at least $(r_0-t)/(1+t)$ edges. For global minimizers [the repository's inradius and circumradius estimate](../../docs/targets/target-c/58-full-source-geometry-audit.md) gives an inball with $r_0>D/2-3^{1/4}\sqrt D$.

To prove this, translate precisely the forward closure of $p$ by $-tN$. Every pair across the cut now has distance greater than one, and all same-side distances are unchanged. If every translated point were in the interior of $K$, all diameter pairs incident with translated points would be absent at the endpoint, with no new diameter pairs elsewhere. This would give the same lexicographic contradiction. Hence some reachable $y$ has $y-tN$ outside the interior. Take $o$ as origin. A separating or supporting unit normal $m$ obeys $m\cdot(y-tN)\ge h_K(m)\ge r_0$. Since $y\in K$, $m\cdot N\le0$, and thus $m\cdot p\le0$. It follows that $|y-p|\ge m\cdot(y-p)\ge r_0-t$. Squaring the arc test and using $|x-y|\ge1$ gives $(x-y)\cdot N\ge t/2$. The triangle inequality gives the edge-length bound. No generic translation or removal of rattlers is required. The repository's [two-state blocker theorem](../../docs/reports/global_discrete_isometry_blocker_closure_2026-10-12.md) treats upper and lower blockers together.

### From an actual hull vertex into the interior and across half the source

One can force the first blocker to be strictly inside the **full** hull at inverse-boundary-population scale. Let $q$ count actual diameter endpoints of the lexicographic source. For all sufficiently large $D$ and $q$, at least $q/2$ distinct endpoints start a path with the following three properties:

1. Its first neighbor belongs to $\operatorname{int}K$.
2. All its edges have length in $[1,1+15000\pi/q]$.
3. Its net inward displacement, projected onto the inward normal chosen at its start, is at least $D/2-O(D^{3/4})$.

Take the incenter as origin and the inradius as $r_0$. Then $K\subset B(o,R_0)$ with $R_0=D-r_0$, by comparison with the opposite point of the inball. The repository's inradius bound above gives $r_0>D/2-3^{1/4}\sqrt D$, so $R_0/r_0\le2$ eventually. Put $\theta_p$ equal to the sum of exterior angles of hull vertices within distance 13 of $p$. At most $27^2$ unit-separated endpoints are within 13 of any vertex, by disjoint half-unit disks. Total convex turning is $2\pi$, so $\sum_p\theta_p\le1458\pi$. At least $q/2$ endpoints have $\theta_p\le2916\pi/q$.

For such a $p$, the boundary arc from $p$ to any boundary label $z$ with $|p-z|\le2$, taken along the shorter interval of polar angles, lies in $B(p,13)$. In fact on each polygon side the radial parametrization has speed at most $R_0^2/r_0$ per unit polar angle: in normal coordinates the radial distance is $h/\cos\phi$, and the speed is $h/\cos^2\phi\le R_0^2/r_0$. For angular gap $\beta\le\pi$, the chord is at least $2r_0\sin(\beta/2)\ge2r_0\beta/\pi$. The arc length is thus at most $(\pi/2)(R_0/r_0)^2 |p-z|\le4\pi<13$. Every outward normal $N$ at $p$ differs in Euclidean norm by at most $\theta_p$ from any chosen outward normal at $z$, since all the intervening turn, including the endpoint cones, is counted. Using the support inequality at $z$ gives $(p-z)\cdot N\le2\theta_p$.

Choose $t=15000\pi/q$, eventually less than one. For each such $z$,
$$
 |p-tN-z|^2\ge 1+t^2-4t\theta_p>1.
$$
More distant boundary labels cannot block either. Build the forward closure as above, now translating by the fixed normal $-tN$ at $p$. Lexicographic minimality again supplies a reachable $y$ with $y-tN$ outside the interior. A supporting normal $m$ at separation has $m\cdot N\le0$ and $m\cdot y\ge r_0-t$. Hence $N\cdot y\le\sqrt{R_0^2-(r_0-t)^2}$ by orthogonal decomposition along $m$, whereas $N\cdot p\ge r_0$. The projected drop is at least $r_0-\sqrt{R_0^2-(r_0-t)^2}=D/2-O(D^{3/4})$. It is positive for large $D$, so the path is nonempty and the first label it reaches must be interior. Squaring the arc condition gives strict forward progress on every edge. This proof permits the path to pass through other contact-core vertices. It does not require independent paths for different starts.

In the repository's normalized large-source setting the [canonical boundary count quoted in Section 57](../../docs/targets/target-c/57-zr-zf-rigidity-audit.md) gives $q\ge(\lceil D\rceil+2)/2$. With that input the tolerance in item 2 is $O(1/D)$ and the number of starts is $\Omega(D)$. The preceding finite curvature argument uses the actual $q$ and is independent of that count. The common graph of these paths is planar once $1+t<\sqrt2$: two properly crossing edges are diagonals of a convex quadrilateral with all sides at least one, and an interior angle of at least $90$ degrees forces the opposite diagonal to have length at least $\sqrt2$. Collinear overlap of distinct edges and a vertex on an edge are excluded by unit separation for edges shorter than two. Planarity still permits paths to share edges, and triangles in the near-unit graph may have sides strictly longer than one.

### A disjoint-path theorem from replacing the points of a cut

There is a different conclusion when the translation is large enough to place two unit-separated copies of a starting label. Fix a unit vector $N$ and a step $t>1$. On all labels draw the same arcs $x\to y$ for $x\ne y$ and $|x-tN-y|\le1$. Let $E$ be the labels $y$ with $y-tN\notin\operatorname{int}K$. Let $S$ be any subset of source labels with pairwise distances strictly greater than one and $\operatorname{dist}(s,K-tN)>1$ for every $s\in S$.

**Claim.** There are $|S|$ vertex-disjoint directed paths from $S$ to $E$, allowing a path of length zero at a common vertex. The setting is the same lexicographically selected triangle-free global source.

**Proof.** By the finite directed vertex version of Menger's theorem it suffices to check all vertex cuts, including cuts containing terminals. Equivalently split every vertex into an in-node and an out-node connected by a unit-capacity arc, give original arcs and superterminal connections capacity $n+1$, and apply integral max-flow/min-cut. Suppose deleting $U$ separates $S$ from $E$ and $|U|<|S|$. In the remaining graph let $M$ be the vertices reachable from $S\setminus U$, and let $F=A\setminus(U\cup M)$. Place $M-tN$, $F$, and **all the original sites $S$** in the plane. The first set lies in $\operatorname{int}K$, and its distances to $F$ are strictly greater than one by closure after deletion. Its distances to $S$ are strictly greater than one by hypothesis. The other layer $F\cup S$ is an unchanged subset of $A$, with $F\cap S$ empty. Hence the population is $n-|U|+|S|>n$. Both layers are triangle-free and there are no contacts between them. Their total contact count is at most the old count: an old edge counted in both layers would have both endpoints in $M\cap S$, whereas $S$ is independent. All sites belong to $K$.

The original contact count is positive, since a finite optimum with minimum distance greater than one can be scaled down. If the new count equals the old one, delete an endpoint of a contact first. Trim to $n$ labels. The resulting triangle-free source has strictly fewer contacts and diameter at most $D$, a contradiction. This proves the cut bound. This argument is specific to equal-diameter contact minimality and uses every source label, including labels used to refill the cut.

For an explicit application take $t=2$. Choose an outward unit normal $b_p$ at each actual diameter endpoint. Averaging $N$ over the circle selects at least $q\arccos(3/4)/\pi$ endpoints with $b_p\cdot N\ge3/4$. Any such $p$ is at distance at least $2b_p\cdot N\ge3/2$ from $K-2N$, by its supporting line. The unit-contact graph has maximum degree six by angular separation, so a greedy independent subset $S$ has size at least $q\arccos(3/4)/(7\pi)$. The claim supplies this many **mutually vertex-disjoint** paths, in one common direction.

These paths cross a macroscopic distance. With the incenter and $R_0,r_0$ as above,
$$
 N\cdot p\ge3r_0/4-\sqrt{R_0^2-r_0^2}
$$
by decomposing $p$ along $b_p$. At an exit, $N\cdot y\le\sqrt{R_0^2-(r_0-2)^2}$ by the same supporting-normal calculation as before. Thus each path has projected span at least $3D/8-O(D^{3/4})$. Each edge has length at most three, so every path has at least $D/8-O(D^{3/4})$ edges. The resulting family controls a quadratic number of distinct labels when $q$ is linear in $D$. The disjoint paths have step bound three. The near-unit paths of the preceding result are obtained at a smaller translation; its proof does not furnish the same disjointness. In particular the unit separation between the two copies of each starting site is essential to the cardinality calculation.

## 4. Counting pairs that can reach the upper bound

If every label moves by at most $s/2$, only original pairs of length at least $D-s$ can reach $D$. For every planar unit-separated set of diameter $D\ge8$ and $0\le s\le1$, their number is $O(D(1+\sqrt{Ds}))$ with an absolute constant.

Partition projective directions into $O(1/h)$ intervals of length at most $h=\max(1/D,\sqrt{s/D})$. Orient each pair in its bin toward the central unit vector $e$. Its projected length is at least $D-w'$, where $w'=s+Dh^2/2$. For a nonempty bin the high and low endpoints each lie in a strip of width $w'$ against the corresponding support line normal to $e$. Moreover **any** high and low endpoints in the bin have projected separation at least $D-2w'$, because the entire projection width is at most $D$. Their transverse separation is thus at most $2\sqrt{Dw'}$. Fixing one endpoint on the opposite side puts each class in a rectangle of sides $w'$ and $4\sqrt{Dw'}$. Disjoint half-unit disks give $O(1+\sqrt{Dw'})$ points per rectangle since $w'\le3/2$. Multiply the two counts and sum the bins, using $w'\le3Dh^2/2$ and $Dh\ge1$, to obtain the stated order.

It is sharp up to constants along regular even unit-sided polygons with $m$ vertices, $D=1/\sin(\pi/m)$. Offsets $j$ from an antipode give deficit $D(1-\cos(j\pi/m))\le D(j\pi/m)^2/2$. Summing $0\le j\le\lfloor(m/\pi)\sqrt{2s/D}\rfloor$ gives $\Omega(D(1+\sqrt{Ds}))$ unordered pairs, allowing for double counting. The estimate includes exact diameter pairs at $s=0$.

## Remaining proof obligation

These are necessary restrictions on a potential counterexample. A dense interior can block a radial change at the first inward layer. At the near-unit scale the paths can share labels. The disjoint family obtained at step two permits edges as long as three and its population lower bound fits inside the available disk population. A near-unit edge can be strictly longer than one. The missing implication is that in every sufficiently large triangle-free global source there is a realizable change that preserves all lower constraints and removes the requisite upper constraints. The arguments above give such changes under stated hypotheses and do not establish that implication. The exact finite checks are run with `python research-packages/radial-diameter-competitor/check.py`. Repository-wide theorem promotion has not been requested.
