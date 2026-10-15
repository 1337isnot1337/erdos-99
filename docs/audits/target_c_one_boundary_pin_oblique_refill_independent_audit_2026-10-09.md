<!-- theorem-state: {"artifact_id":"ART-690EC0C075F0","canonical":true,"claim_ids":["C-OBLIQUE-ONE-PIN-STRICT-REFILL","C-ONE-PIN-OBLIQUE-WALL-OLER-RESIDUAL","C-ONE-PIN-OBLIQUE-WALL-POPULATION","C-TRIANGULAR-ONE-PIN-DISPLACEMENT-GAP-REGRESSION","C-UNIT-SIDE-CROSSING-SEPARATION"],"claim_statuses":{"C-OBLIQUE-ONE-PIN-STRICT-REFILL":"canonical","C-ONE-PIN-OBLIQUE-WALL-OLER-RESIDUAL":"canonical","C-ONE-PIN-OBLIQUE-WALL-POPULATION":"canonical","C-TRIANGULAR-ONE-PIN-DISPLACEMENT-GAP-REGRESSION":"regression","C-UNIT-SIDE-CROSSING-SEPARATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C Audit.187 — one-pin oblique full-interior refill

**Date:** 2026-10-09
**Audit base:** origin/main=0fde3ae454a71103945b8daac3274b278218a86f, state 2026-10-09.audit.180
**Frozen source:** origin/research/sol/target-c-level1-gpt61-2026-10-04 at 9875cd6a77939bb6347353fc798ab8f9ab03ec3e
**Source report:** docs/reports/target_c_one_boundary_pin_oblique_refill_2026-10-05.md, SHA-256 e6b5cbafce8acfb2744b189c992e56768fe7bff2b37215fd92a9a3515f79727b
**Source verifier:** research/verify_target_c_one_boundary_pin_oblique_refill_2026_10_05.py, SHA-256 ed32673b81d8764905003f6486a5228fc8d4caa516c9b2bf4818bff1b261e9b0
**Classification:** independent reconstruction; **PASS — promote the explicit strict refill, the scoped actual-wall population theorem, its convex-wall residual bound, and the triangular pinned-motion regression.**
**Target:** C-II. C-II and Level I remain open.

## Refreshed field and audit unit

The refreshed remote research branch still has the frozen source tip above. The current open mathematical PR is #737 on the owner-order branch; no discovery branch or source worktree was modified. Main already contains the separate Audit.183–.186 results. They do not imply this theorem: the claim below is a concrete finite source replacement for a strictly oblique rectangular lattice wall, while those audits concern macroscopic cap capacity, owner sinks, and loaded returns.

The candidate's proposed chain was

explicit oblique one-pin refill
→ one actual near-frame wall label pays for a strict full-interior replacement
→ every interior source population in that wall is at least $(m-1)(n-1)$
→ convex-wall residual is bounded by angular area excess plus the explicit wall error.

The last implication is only local to a qualifying wall. No theorem extracts such a wall from a general canonical source, and no overlap or global residual-capture statement is included.

## Exact promoted statements

Let $m,n\ge3$, $L=m+n$, $u=(1,0)$, $v=(c,a)=(\cos\phi,\sin\phi)$, with $\pi/3<\phi\le\pi/2$, and $\delta=1-2c\in(0,1]$. Put $p_{ij}=iu+jv$ for $0\le i\le m$, $0\le j\le n$. Remove the boundary label $p_{1,0}$, keep all other boundary labels fixed, and regard the $K=(m-1)(n-1)$ interior labels as movable.

**C-OBLIQUE-ONE-PIN-STRICT-REFILL.** There is an explicit two-stage continuous motion of all $K$ interior labels, with every other retained label fixed, which keeps all pair distances at least one throughout and makes every pair involving a moved label strictly longer than one at the endpoint. The targets stay inside the reference parallelogram and move by less than $1/100$. A uniform endpoint squared-separation margin is

\[
s=\frac{\delta}{100L^2},\qquad h=\frac{s^2}{100L^3},\qquad \beta=\frac1{10L^3},\qquad
g=4\beta^2h^2=\frac{\delta^4}{25{,}000{,}000{,}000{,}000L^{20}}.
\]

Every endpoint pair involving a moved label and a retained label has squared distance at least $1+g$. The deleted $p_{1,0}$ is not a retained label.

**C-UNIT-SIDE-CROSSING-SEPARATION.** If $AB$ is a unit segment, $X,Y$ lie on opposite sides of its line, segment $[X,Y]$ crosses segment $[A,B]$, and all four distances from $X,Y$ to $A,B$ are at least $t\in[1/\sqrt2,1]$, then

\[
|X-Y|\ge\sqrt{4t^2-1}.
\]

**C-ONE-PIN-OBLIQUE-WALL-POPULATION.** Let $A$ be a triangle-free contact-minimal global minimum-diameter configuration, with contact-minimality taken within the triangle-free global-minimizer class. Suppose $A$ contains a simple unit-contact cycle $W$ of $2L$ distinct vertices, in the boundary order of the above reference frame, and after one Euclidean isometry every corresponding wall vertex is within

\[
\eta=\frac{g}{4(L+1)}
\]

of its reference vertex. Convexity of $W$ is not assumed. If $z=|A\cap\operatorname{int}(W)|$, then $z\ge(m-1)(n-1)$. The theorem counts every source point in the interior, including contact isolates; under the replacement all deleted labels are reassigned to target sites, and exterior labels (including isolates) are retained at their original coordinates.

**C-ONE-PIN-OBLIQUE-WALL-OLER-RESIDUAL.** If the actual wall $W$ in the preceding statement is convex, has area $A_W$, and $a_0=\sqrt3/2$, define $r_W=A_W/a_0-L+1-z$. Then

\[
r_W\le mn\left(\frac{\sin\phi}{a_0}-1\right)+\frac{2L\eta+L\eta^2}{a_0}.
\]

This is an exact one-wall estimate. Summing it over frames gives a contradiction only when a separate argument supplies a summed framed residual lower bound and controls overlap; this audit supplies neither.

**C-TRIANGULAR-ONE-PIN-DISPLACEMENT-GAP-REGRESSION.** At $\phi=\pi/3$, with $p_{1,0}$ deleted and the rest of the boundary fixed, every unit-separated alternative of the $K$ interior labels has maximum displacement $\rho=0$ or $\rho\ge a_0/(2L)$. Thus every continuous feasible motion starting at the reference chart is constant. This refutes an angle-independent small one-pin strictification in this pinned chart. It does not rule out distant alternatives and is not a global-minimizer or Level I counterexample.

## Independent proof of the oblique refill

Set $e_y=(0,1)$, $f_0=f_n=0$, and

\[
f_j=j(n-j)(1+\beta j),\qquad r=(1,-c/a).
\]

First move $p_{1j}$, $1\le j<n$, by $-s(n-j)e_y$. Next keep column 1 and the wall fixed and move $p_{ij}$, $2\le i<m$, $1\le j<n$, by $-h(m-i)f_jr$. The identities $u\cdot r=1$, $v\cdot r=0$, and $|r|=1/a\ge1$ control the contact edges.

For the first stage, a horizontal unit edge incident to column 1 has squared length $1+s^2(n-j)^2\ge1+s^2$. A vertical edge in column 1 has vector $v+s e_y$, hence squared length $1+2as+s^2\ge1$. The missing $p_{1,0}$ is exactly the bottom vertical edge that would otherwise move inward; all other retained contacts are feasible.

In the second stage, every horizontal block contact, including the right-wall contact, changes to $u+h f_jr$ and has squared length at least $1+2h$. For a vertical block contact the change is a multiple of $r$ orthogonal to $v$, so its squared excess is

\[
h^2(m-i)^2(f_j-f_{j-1})^2/a^2.
\]

The integer part of $f_j-f_{j-1}$ is $n-2j+1$, and its correction is $\beta(2nj-n-3j^2+3j-1)$, whose magnitude is below $1/2$ for $n\le L$ and $L\ge6$. When the integer part is zero, $n=2j-1$ and the correction equals $\beta j(j-1)\ge2\beta$. At the two endpoints, $f_1,f_{n-1}\ge2\ge2\beta$. Therefore

\[
|f_j-f_{j-1}|\ge2\beta
\]

for every $1\le j\le n$, giving squared excess at least $4\beta^2h^2=g$ on all vertical block contacts, including the top and bottom walls.

The stage-two displacement of any point is less than $3hL^3=3s^2/100$. The only contact whose first-stage gap is spent by stage two is the interface from column 1 to column 2. At the start of stage two its squared excess is at least $s^2$, its length is below $101/100$, and stage two reduces squared length by less than $2(101/100)(3s^2/100)<s^2/2$. It stays strictly feasible. All other contacts either have the first-stage gap above or lengthen in stage two.

For integer lattice difference $ru+tv\ne0$, the squared norm is $r^2+t^2+2rtc$. In the strict-angle range its only unit vectors are $\pm u,\pm v$; every nonbasis difference has squared norm at least $1+\delta$. Every point moves by less than $\delta/(50L)$ over both stages, and reference pair lengths are at most $L$. A noncontact pair therefore loses less than $2\delta/25$ in squared length and remains above $1+23\delta/25$, which is greater than $1+g$. Boundary-boundary pairs are fixed. The formulas for displacement in the $u,v$ coordinates and the same displacement bound show that every moving point stays in the open reference parallelogram and moves less than $1/100$. This proves the stated endpoint margin and the full path feasibility; it does not infer a source placement from an auxiliary chart.

## Crossing bound and actual-wall source replacement

For the crossing lemma, let $\alpha=\angle AXB$, $\beta'=\angle AYB$. From the cosine rule, if $r_1=|XA|$, $r_2=|XB|$, and both are at least $t$, then

\[
\cos\alpha=\frac{r_1^2+r_2^2-1}{2r_1r_2}\ge1-\frac1{2t^2},
\]

so $\alpha\le2\arcsin(1/(2t))$, and the same holds for $\beta'$. Since $AB$ and $XY$ cross internally, $A,X,B,Y$ form a convex quadrilateral. Its angles at $A,B$ sum to $2\pi-\alpha-\beta'$, so at least one is at least $\pi-2\arcsin(1/(2t))$. Applying the cosine rule there, with both incident lengths at least $t$, gives

\[
|X-Y|^2\ge 2t^2\left(1+\cos(2\arcsin(1/(2t)))\right)=4t^2-1.
\]

Now align the actual simple cycle to the ordered reference frame. The boundary homotopy obtained by linear interpolation of corresponding vertices stays within $\eta$ of the reference boundary. Each reference interior point is at distance at least $a=\sin\phi\ge\sqrt3/2$ from each side; each target moves by less than $1/100$, and $\eta\ll1/100$. Thus every target remains inside $W$ by winding number. It is consequently an interior point of $\operatorname{conv}(A)$.

Every target has squared distance at least $1+g$ from each retained reference wall vertex. Replacing that vertex by its actual position changes the squared distance by at most $2(L+1)\eta=g/2$, so every target-wall distance is strictly greater than one. The deleted wall vertex is excluded from this lower-constraint check. No other source label can lie on a side of $W$: every side has length one, and any point on that segment is within $1/2$ of an endpoint. Thus every nonwall source point is either inside or outside the cycle. For an old exterior source point $x$, take a target's reference point $q$. The point $q$ is at least $1-\eta\ge19/20$ from every actual wall vertex; $x$, being a distinct source point, is at least one from each. The segment from $q\in\operatorname{int}(W)$ to the exterior point crosses a unit side. If the intersection is at a vertex, perturb $x$ slightly within the open exterior, apply the crossing bound to a generic side-interior crossing, and pass to the limit. With $t=19/20$,

\[
|q-x|\ge\sqrt{261}/10>8/5.
\]

The target displacement is less than $1/100$, so the final target is more than $3/2$ from every exterior source point. This includes all exterior contact isolates.

Suppose $z\le K-1$. Delete the $z$ interior source points and the wall label corresponding to $p_{1,0}$, then assign these $z+1$ deleted labels bijectively to any $z+1$ of the $K$ strict targets. The cardinality is unchanged. All retained pairs keep their old distances, and every pair involving a target is strictly above one. The diameter of $\operatorname{conv}(A)$ is $D$. Each target is an interior point of this convex hull, so its distance to every point of $\operatorname{conv}(A)$, including retained source points and other targets, is strictly less than $D$: if equality held, moving the target a small amount away from that point while staying inside the hull would produce a pair farther than $D$. The new maximum is therefore at most $D$. A smaller maximum contradicts global optimality. If it equals $D$, the new configuration is still triangle-free: no target has any unit contact, and the retained source pairs are unchanged. It has fewer contacts, since both cycle edges at the deleted wall vertex disappear and no new contact is made. This contradicts contact-minimality in the triangle-free minimizer class. Hence $z\ge K$. The argument counts all interior labels, including isolates, and uses no stress or core-only motion theorem.

For the residual estimate, the reference polygon has perimeter $2L$, $2L$ vertices, and area $mn\sin\phi$. If its vertices move by at most $\eta$, the shoelace formula gives

\[
|A_W-mn\sin\phi|\le2L\eta+(2L)\eta^2/2=2L\eta+L\eta^2.
\]

Using $z\ge mn-L+1$ in $r_W=A_W/a_0-L+1-z$ gives the exact displayed bound. Convexity is assumed only for this residual statement; the population theorem itself allows nonconvex simple cycles.

## Triangular pinned-motion regression

At $\phi=\pi/3$, put $w=u-v$, which is also a unit vector. For a feasible alternative write $\xi_{ij}=p'_{ij}-p_{ij}$ on the interior labels and $\rho=\max|\xi_{ij}|$. Every original unit edge with direction $e\in\{u,v,w\}$ gives

\[
e\cdot(\xi_b-\xi_a)\ge-\tfrac12|\xi_b-\xi_a|^2\ge-2\rho^2.
\]

Summing along a horizontal chain in row $j\ge1$, whose two boundary endpoints remain pinned, bounds

\[
|u\cdot\xi_{ij}|\le2m\rho^2.
\]

Every $w$-chain through an interior vertex has constant coordinate sum $i+j\ge2$. Its boundary endpoints remain pinned because the deleted pin $p_{1,0}$ has coordinate sum one. The chain length is at most $\min(m,n)$, giving

\[
|w\cdot\xi_{ij}|\le2\min(m,n)\rho^2.
\]

The dual basis to the unit vectors $u,w$ has both lengths $1/a_0$. Hence

\[
\rho\le\frac{2(m+\min(m,n))}{a_0}\rho^2\le\frac{2L}{a_0}\rho^2.
\]

Thus either $\rho=0$ or $\rho\ge a_0/(2L)$. A continuous feasible path starting at zero displacement cannot cross this positive gap. This is a local pinned regression only; it does not assert that the triangular chart is globally isolated.

## Hostile scope checks and verifier boundary

- The auxiliary reference points are not identified with old source points; the source proof deletes the interior population and explicitly reassigns its labels.
- The actual wall is a simple cycle, not assumed convex for the population theorem. Convexity is required only for the residual quantity.
- The crossing argument uses actual unit sides and actual source separation, including contact-isolated exterior points. The removed wall vertex is used only as a geometric separator endpoint.
- No selected stress core, contact-only population, or deleted-isolate count substitutes for the full source.
- No near-oblique wall is extracted from arbitrary canonical sources; no frame disjointness or aggregate residual payment is asserted.
- The triangular result rules out an angle-independent local radius, not the explicitly vanishing $\delta$-dependent oblique motion. The optional positive pinned-stress construction in the source report was not needed for any promoted statement and is not promoted here.
- The frozen verifier was inspected and rerun with exact arithmetic in $\mathbb Q(\sqrt3)$. It checks 1,042 two-stage pair constraints and 11,774 complete guarded source pairs, including 82 removed contacts, 32 interior labels, and perturbed-wall fixtures; it also checks four finite triangular stress fixtures. It corroborates those finite instances only. It does not prove the universal motion bounds, actual-wall source theorem, crossing lemma, or global optimality. The analytic arguments above carry those claims; no verifier is registered as a theorem certificate.

## Verdict and frontier effect

The four promoted theorem claims and the scoped regression are valid at their stated scopes. The theorem excludes only a contact-minimal triangle-free global minimizer that actually contains the specified near-oblique rectangular unit wall. It gives no extraction of that wall, no count for nonframed chambers, and no uniform asymptotic coverage. The local residual formula removes the former linear boundary allowance for this wall family but does not charge the canonical global residual. Therefore the active C-II obligation remains a full-source finite move or discrete replacement that checks every lower bound and every actual-diameter upper bound; C-II and Level I remain open.
