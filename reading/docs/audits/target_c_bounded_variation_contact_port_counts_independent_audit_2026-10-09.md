> Generated reading edition · [exact source](../../../docs/audits/target_c_bounded_variation_contact_port_counts_independent_audit_2026-10-09.md) · source SHA-256 `26bbd0d6babd39504c188af493cb43ef5b6d9c3a89c202857f044f1b426bcaeb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9308FD0CE136","canonical":true,"claim_ids":["C-BOUNDED-VARIATION-DOUBLE-PORT-COUNT","C-BOUNDED-VARIATION-LEAF-PORT-COUNT","C-NEAR-BOUNDARY-LATTICE-LOCAL-CAPACITY","C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY"],"claim_statuses":{"C-BOUNDED-VARIATION-DOUBLE-PORT-COUNT":"canonical","C-BOUNDED-VARIATION-LEAF-PORT-COUNT":"canonical","C-NEAR-BOUNDARY-LATTICE-LOCAL-CAPACITY":"canonical","C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.216 — contact ports into bounded-variation charts

Date: 2026-10-09. Audit base: `origin/main=92e7a345d3ea56af0174c711317aa2c41812b54c`, state `2026-10-09.audit.210`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate: Section 14 of `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`.
- Verdict: **PASS — promote** `C-NEAR-BOUNDARY-LATTICE-LOCAL-CAPACITY`, `C-POSITIVE-LEAF-ANCHOR-INNER-BALL-BOUNDARY`, `C-BOUNDED-VARIATION-LEAF-PORT-COUNT`, and `C-BOUNDED-VARIATION-DOUBLE-PORT-COUNT`.
- The leaf bound is restricted to a unique actual unit contact whose coefficient is positive in at least one normalized full-source KKT stress of that source. The double-port bound needs no optimality or stress hypothesis.

## Exact claims

Let a rectangular additive chart be

$$
p_{ij}=p_{00}+iu_0+jv_0+a_i+b_j,\qquad 0\le i\le m,\quad 0\le j\le n,
$$

where $u_0,v_0$ are unit vectors with angle in $[\pi/3,2\pi/3]$, $a_0=b_0=0$, and

$$
\sum_{i=1}^m|a_i-a_{i-1}|+\sum_{j=1}^n|b_j-b_{j-1}|\le M
$$

for a fixed $M$. Any occupied chart positions are distinct points of the full unit-separated source. The source may contain arbitrary additional points, including contact isolates. The number $J$ of charts and $M$ are fixed uniformly along the sequence.

### Near-boundary lattice capacity

Let $E_D$ be an intersection of finitely many disks, with

$$
\overline B(o,c_1D)\subset E_D\subset\overline B(o,C_2D),
$$

and every defining disk radius at most $C_1D$, for fixed positive constants $c_1,C_1,C_2$. For $c\in\partial E_D$, $\sqrt D\le r\le D$, $0\le\epsilon\le1/8$, and $0\le\rho\le1$, let $X$ be a unit-separated set in $\overline B(c,r/2)$ with $\operatorname{dist}(x,\partial E_D)\le\rho$ for every $x\in X$. If all points of $X$ are within $\epsilon$ of one translate of a unit rhombic lattice, then

$$
|X|\le C\bigl(r(\epsilon+\rho)+(Dr)^{1/3}+1\bigr),
$$

where $C$ depends only on $c_1,C_1,C_2$.

### Positive leaf anchors

Let $A$ be any noncollinear global minimum-diameter source with diameter $D$, and retain every point of $A$. Define

$$
K_D=\bigcap_{x\in A}\overline B(x,D-1).
$$

For all sufficiently large $D$, if $p$ is an actual diameter endpoint with unique actual unit neighbor $a$, and the contact $pa$ has positive coefficient in some normalized full-source KKT stress of that source, then

$$
\operatorname{dist}(a,\partial K_D)\le C D^{-1/2}.
$$

The constant is absolute. In particular, no contact-isolated source point is omitted from the disks defining $K_D$.

### Leaf and double ports

For a canonical post-ZF Target C-II sequence of noncollinear triangle-free global minimizers, $D\to\infty$, suppose the full source contains at most $J$ charts as above. A leaf port is a counted actual diameter endpoint $p$ whose unique actual unit neighbor is an occupied chart point and whose contact coefficient is positive in some normalized full-source KKT stress of that source. A double port is a counted actual diameter endpoint with two distinct actual unit neighbors occupying positions in the same chart. Then

$$
\#\{\text{leaf ports}\}=O_{J,M}(D^{4/5}),\qquad
\#\{\text{double ports}\}=O_{J,M}(D^{6/7}).
$$

The double-port conclusion holds for every finite unit-separated planar source, without global optimality, triangle-freeness, or KKT hypotheses. For either count, chart positions may be unoccupied; there is no full-grid occupancy assumption.

## Independent reconstruction

### Local count near a curved boundary

Put $P_D=E_D\cap\overline B(c,r)$. Since $E_D$ contains a disk of radius $c_1D$, homothety from the boundary point $c$ toward that disk gives an inball of radius $\kappa r$ in $P_D$, for a positive $\kappa$ depending only on $c_1,C_2$. Also $\operatorname{per}(P_D)=O(r)$. Its boundary consists of circular arcs and convex corners, with $ds\le C D\,d\theta$, where $\theta$ is tangent angle. These bounds remain valid for the inner erosion and outer parallel body at bounded distance $t$; the inball ensures the erosion is nonempty for large $D$.

For a convex body $F$ with these arc bounds, the divergence theorem gives
$$
|\widehat{\mathbf 1_F}(\xi)|\le C\sqrt D\,|\xi|^{-3/2}.
$$
Indeed, after the divergence prefactor 1/|xi|, the portions where the phase derivative is at most eta have arclength O(D eta); on the remaining monotone tangent-angle ranges, integration by parts gives O(1/(|xi| eta)). Stieltjes integration handles corner jumps: their total tangent variation is at most 2 pi, so no factor depends on the number of arcs. Taking eta=(D|xi|)^(-1/2) yields the displayed estimate; the low-frequency range follows from the perimeter bound. The rhombic dual lattices have uniform separation, so dyadic summation and Poisson summation after smoothing at scale s<=1 give discrepancy O(sqrt(D) s^(-1/2)), uniformly over the permitted lattice bases and translations.

Round each $x\in X$ to a lattice point $\ell_x$. This is injective because the lattice minimum separation is one, $X$ is unit-separated, and $2\epsilon\le1/4$. Choose a nearest boundary point $q_x\in\partial E_D$. For large $D$, $q_x$ lies strictly inside the local patch disk, so it is on $\partial P_D$ and has a supporting line inherited from $E_D$. With $s=(D/r^2)^{1/3}$ and $t=\epsilon+\rho+s$, the open $s$-ball around $\ell_x$ lies in the outer parallel body $P_D+tB$ and lies strictly beyond the supporting line of the inner erosion $P_D\ominus tB$. Thus the smoothed indicator difference equals one at every $\ell_x$ and is nonnegative everywhere.

The area gap is $O(rt+1)$: the outer Steiner formula contributes $t\operatorname{per}(P_D)+\pi t^2$, and inner parallel coarea bounds the lost area by $t\operatorname{per}(P_D)$. The smoothed lattice discrepancy contributes $O(\sqrt D\,s^{-1/2})$. Since $rs=\sqrt D\,s^{-1/2}=(Dr)^{1/3}$, the near-boundary capacity follows.

### Anchor localization

Take the full-source circumcenter as origin and write $\eta=3^{1/4}\sqrt D$. By canonical $C$-FS-GEOM, every source point has norm at most $R\le D/2+\eta$. For a diameter endpoint $p$, $|p|\ge D-R$. Set $e=p/|p|$, $n=p-a$, and $d=|p-x|$. For any $x\in A$ with $d\ge D-2$, the cosine identity gives

$$
\frac{p-x}{d}\cdot e
=\frac{|p|^2+d^2-|x|^2}{2d|p|}
\ge1-t_D,\qquad t_D=\frac{4(\eta+1)}D.
$$

Here the numerator is bounded below using $|p|^2-|x|^2\ge D^2-2DR$ and $d^2\ge(D-2)^2$, while $2d|p|\le2DR$. The KKT equilibrium at $p$, with its sole contact coefficient positive, expresses $n$ as a positive combination of the actual diameter normals. Hence $n\cdot e\ge1-t_D$. Each diameter normal above is within $\sqrt{2t_D}$ of $e$, so its dot product with $n$ is at least $1-4t_D$. Therefore

$$
|a-x|^2\le(d-1)^2+8dt_D\le(d-1+8t_D)^2.
$$

If $d<D-2$, the triangle inequality gives $|a-x|<D-1$. Thus $a$ lies in every disk of radius $D-1+8t_D$ centered at a source point.

Let $o$ be an actual diameter-pair midpoint and $c_*=1-\sqrt3/2$. The two diameter disks imply $|x-o|\le\sqrt3D/2$ for every source point $x$, and $\overline B(o,c_*D-1)\subset K_D$. Also $K_D+\overline B(0,1)\subset W=\bigcap_{x\in A}\overline B(x,D)$. Since the positive KKT combination supports $W$ at $p$ in direction $n$,

$$
h_{K_D}(n)\le h_W(n)-1=n\cdot p-1=n\cdot a.
$$

So $a$ is on or beyond a supporting line of $K_D$. Contract $a$ toward $o$ by the factor
$$
\theta=\frac{c_*D-1}{c_*D-1+8t_D}.
$$
For every $x\in A$, convexity of the norm gives
$$
|\theta a+(1-\theta)o-x|
\le\theta(D-1+8t_D)+(1-\theta)\sqrt3D/2
=D-1.
$$
The contracted point lies in $K_D$. Since $|a-o|\le|p-o|+1\le R+1=O(D)$, its distance from $a$ is $O(t_D)=O(D^{-1/2})$. The support-line relation then proves the asserted boundary distance. This argument uses every source point, including isolates.

### Chart cuts and leaf ports

Set $\delta=r/(16D)$. Greedily divide each chart shore into consecutive blocks of total within-block displacement variation at most $\delta$. The number of cuts across the fixed $J$ charts is $O_{J,M}(D/r+1)$. Dual coordinates for $u_0,v_0$ have norm at most two. A chart position differs from its reference lattice coordinate by at most $M$; an attached loaded endpoint adds at most one unit. Remove counted endpoints in physical strips of fixed width $O_M(1)$ around every half-integer cut. The canonical actual-endpoint strip bound charges $O_M(\sqrt D)$ endpoints per strip, hence the total removed count is $O_{J,M}(D^{3/2}/r+D^{1/2})$.

The remaining counted endpoints are vertices of their convex hull: if q has diameter partner y, then q lies on the radius-D circle about y, while every nontrivial convex combination of distinct source points in that disk lies strictly inside it. Thus q is strictly exposed in the full-source hull and remains extreme in every endpoint sub-hull. This hull has perimeter at most pi D, lies in W, and its cut strips divide the boundary into O_{J,M}(D/r+1) arcs. Subdivide each arc into patches of scale r. On each patch all chosen anchors use the same shore-block pair and lie within 2delta of one translate of the reference lattice.

For leaf ports, anchors are distinct unit-separated source points and each is within $O(D^{-1/2})$ of $\partial K_D$. Within one loaded patch their anchors lie in a ball of radius $O(r)$; choose a nearest boundary point for one anchor and use a constant-factor larger patch of $K_D$. The near-boundary capacity bounds their number by
$$
O_M\!\left(r\delta+rD^{-1/2}+(Dr)^{1/3}+1\right).
$$
At most six unit-separated loaded endpoints can share one anchor, by circular packing. Summing over $O_{J,M}(D/r)$ patches and adding the removed strips gives
$$
O_{J,M}\!\left(r+\sqrt D+D^{4/3}r^{-2/3}+D^{3/2}/r\right).
$$
Taking $r=D^{4/5}$ proves the $O_{J,M}(D^{4/5})$ leaf bound.

### Double ports without a midpoint guard

For two chart anchors $a,b$ of one counted endpoint $p$, unit separation gives $1\le|b-a|\le2$. Their chart-label difference $w_0=iu_0+jv_0$ is within $4\delta$ of $b-a$. Thus $|w_0|\le3$ for large $D$. The rhombic Gram bound $|iu_0+jv_0|^2\ge(i^2+j^2)/2$ leaves only the fixed finite family $i^2+j^2\le18$.

For each such label difference, clip $w_0$ radially to length at most two. The actual circle-intersection formula
$$
p-a=\frac w2\ \mathord\pm\ \frac{Jw}{|w|}\sqrt{1-|w|^2/4},\qquad w=b-a,
$$
and the one-half-Hölder bound for square root place $p$ within $O(\sqrt\delta)$ of one of at most two fixed offsets from a translated chart lattice. The lower bound $|w|\ge1$ keeps normalization uniformly Lipschitz; clipping changes the reference vector by at most $4\delta$. The error tends to zero, so rounding is injective within each offset group. Applying the canonical local curved-boundary capacity to actual diameter endpoints in each offset group bounds one patch by
$$
O\!\left(r\sqrt\delta+(Dr)^{1/3}+1\right).
$$
After summing $O_{J,M}(D/r)$ patches and adding the cut strips, the total is
$$
O_{J,M}\!\left(\sqrt{Dr}+D^{4/3}r^{-2/3}+D^{3/2}/r\right).
$$
Taking $r=D^{5/7}$ gives $O_{J,M}(D^{6/7})$; the cut-strip term has order $D^{11/14}$.

## Hostile checks and scope

- The inner ball hull uses all source points, including contact isolates. Neither the anchor estimate nor any count deletes or moves a source point.
- The positive-contact coefficient is load-bearing only for leaf anchors. The double-port count is a packing and boundary count for arbitrary unit-separated sources.
- The two double-port anchors need only be in the same chart; no triangular-lattice restriction, midpoint occupancy, chart extraction, or finite source move is used. Near tangency is retained with its square-root positional loss; without full occupancy no uniform gap from anchor separation two is claimed.
- The full-source strip theorem is applied only to actual diameter endpoints. The curved-boundary lattice count is applied only to actual diameter endpoints in $W$; the new near-boundary version is applied to unit-separated anchors near $\partial K_D$.
- The finite offset family is bounded by the explicit Gram inequality, not by the narrower 48-offset triangular classification from the source report's Section 9. No unoccupied lattice midpoint is treated as an actual source point.
- No finite verifier encodes these analytic implications. The registered certificates were rerun as part of the promotion gate; they are repository checks, not proof of the estimates above.

## Canonical disposition

Promote the generalized local capacity, the positive-leaf anchor localization, and the two exact port-count theorems. These bounds do not extract bounded-variation charts from a canonical source, and they do not imply a finite competitor or strict diameter decrease. Target C-II and Level I remain open. Section 15's stronger double-port bound under full rectangular occupancy is an independent claim and is not included in this audit.

**Frontier effect:** none. The port bounds reduce the number of loaded endpoints that can use these specified bounded-variation chart contacts; the remaining chart-extraction or source-competitor bridge is unchanged.

**Promotion transaction:** PR #920 head 09bc901564fe77466aad9a655d649a0b8de627e9 merged as 096cc109dfe6b56a82389c2422bb06dd160a701f. Protected state-consistency run 37997561053 passed in 6m54s, including the registered theorem-certificate step and patch-whitespace check. The merged tree 555e1f5fd562629472a908f004be9dbed3d9823f exactly matches the audited head tree; the independent-audit branch was deleted after verification.

Discovery-worker protection: audited only Section 14 at the frozen source commit. No discovery branch or worktree was modified.
