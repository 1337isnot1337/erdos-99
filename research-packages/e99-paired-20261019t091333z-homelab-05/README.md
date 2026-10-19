# Independent audit: near triangular one pin capacity plateau

**Investigation:** audit-target-c-near-triangular-one-pin-capacity-plateau-pr947-paired-20261019

**Candidate:** TARGET-C-NEAR-TRIANGULAR-ONE-PIN-CAPACITY-PLATEAU-PR947

**Audit result: PASS for the exact fixed frame claim.** This is a proof audit and finite reproduction, not a theorem state transaction. The destination candidate remains **unreviewed** in the registry; no claim was promoted.

## Exact question and scope

Fix integers \(m,n\ge3\), let \(u=(1,0)\), \(v=(\cos\phi,\sin\phi)\), and let
\[
P_{m,n}(\phi)=\{su+tv:0\le s\le m,\ 0\le t\le n\},\qquad p_{ij}=iu+jv.
\]
Delete the boundary label \(p_{1,0}\), retain every other boundary label at its grid location, and count only additional points in the open parallelogram. Weak capacity requires all additional points to be pairwise at distance at least one and at distance at least one from retained boundary labels. Strict capacity replaces both inequalities by strict inequalities.

The audited claim is that for each **fixed** \((m,n)\), a nonexplicit \(\epsilon_{m,n}>0\) exists such that both capacities equal
\[
K=(m-1)(n-1)
\]
for \(\pi/3<\phi<\pi/3+\epsilon_{m,n}\). The interval may depend on the frame. The result says nothing about a uniform interval as \(m,n\) grow, exterior sites, moved walls, source-wall extraction, or global minimizers.

**Downstream quantity:** the weak and strict fixed-wall interior capacities. If the capacity upper bound had failed, it could reopen a fixed-wall refill route in this near-triangular range. Its validity rules out that route under these exact fixed-frame hypotheses; moved-wall or outside-capacity payment remains possible.

**Falsification test:** find a weak packing with \(K+1\) interior points arbitrarily close to the triangular angle, invalidate the restored-pin displacement gap, or find a failed target pair in the strict refill construction. The exact finite controls below check the last possibility in sample frames. The stopping condition was a complete proof reconstruction of both bounds, the restored-pin contradiction, and the strict lower-bound dependency, or an exact counterexample to one of them.

## Reconstruction of the weak upper bound

The \(K\) interior grid sites give weak capacity at least \(K\). Suppose instead that weak capacity exceeds \(K\) arbitrarily close to \(\pi/3\). Choose \(\phi_j\downarrow\pi/3\) and \(K+1\) feasible interior points for each \(j\). Along with the retained boundary sites this gives
\[
N=2(m+n)-1+(K+1)=(m+1)(n+1)
\]
unit separated centers in the closed parallelogram. The four retained corners force their convex hull to be the whole parallelogram.

For a subsequence, compactness gives a limiting unit separated set of \(N\) centers in the triangular parallelogram at \(\phi=\pi/3\). Its area is \(mn\sqrt3/2\), and its perimeter is \(2(m+n)\). The Thue–Groemer packing bound for unit separated centers is
\[
N\le \frac{2}{\sqrt3}\operatorname{area}(P)+\frac12\operatorname{perimeter}(P)+1.
\]
At the limit, the right side is \(mn+m+n+1=N\), so equality holds. The hull is two dimensional, excluding the segment equality case. The equality description gives a triangulation by regular unit triangles. Its face-adjacency graph is connected; across each shared edge, the adjacent face lies on the other side, so its third vertex is forced. Propagating from one face puts every center in one triangular lattice. The fixed corner and the two side directions fix its translation and orientation, so the lattice sites in this parallelogram are exactly \(p_{ij}\), \(0\le i\le m\), \(0\le j\le n\).

There are exactly \(N\) such sites. The retained pins occupy all boundary sites except \(p_{1,0}\), so after a finite relabeling subsequence the \(K+1\) inserted points converge to the \(K\) interior sites and \(p_{1,0}\). Place one inserted label at the role of the restored pin and the others at the interior-label roles. Their displacements from the reference grid at angle \(\phi_j\) tend to zero. The restored-pin gap holds at each of these same angles and has uniform lower bound \(\sqrt3/[4(m+n+1)]\), so sufficiently late placements must have zero displacement. This contradicts an inserted point lying in the open parallelogram at the role of the deleted boundary site.

## Restored-pin displacement gap

For any \(\pi/3\le\phi\le\pi/2\), restore \(p_{1,0}\) as a movable label with all interior labels; keep all other boundary labels fixed, require unit separation, and constrain all movable labels to the closed parallelogram. Write \(\xi_{ij}\) for displacement and \(\rho=\max|\xi_{ij}|\). For every old unit edge with direction \(e\), feasibility implies
\[
e\cdot(\xi_b-\xi_a)\ge-\tfrac12|\xi_b-\xi_a|^2\ge-2\rho^2.
\]
Summing along each horizontal interior row from its two fixed endpoints gives \(|u\cdot\xi_{ij}|\le2m\rho^2\). At the restored pin, its two fixed horizontal neighbors give the sharper \(|u\cdot\xi_{1,0}|\le\rho^2/2\). Because that pin lies on the lower side of the closed parallelogram, \((\xi_{1,0})_y\ge0\), hence \(v\cdot\xi_{1,0}\ge-\rho^2/4\).

Summing vertical-edge inequalities up column one from the restored pin and down from its fixed top endpoint gives
\[
-(2n+1)\rho^2\le v\cdot\xi_{1j}\le2n\rho^2.
\]
Every other interior column has fixed top and bottom endpoints, giving \(|v\cdot\xi_{ij}|\le2n\rho^2\). The dual vectors to \(u,v\) each have norm \(1/a\), where \(a=\sin\phi\ge\sqrt3/2\). Thus
\[
\rho\le\frac{2m+2n+1}{a}\rho^2\le\frac{2(m+n+1)}{a}\rho^2.
\]
Therefore \(\rho=0\) or \(\rho\ge a/[2(m+n+1)]\). The convergent placements have \(\rho\to0\); for large \(j\), the gap forces \(\rho=0\), placing the assigned \(p_{1,0}\) point on the boundary even though each inserted point was in the open parallelogram. Contradiction. This proves weak capacity at most \(K\) on some frame-dependent interval.

## Strict lower bound and dependency audit

The lower bound is supplied by canonical claim C-OBLIQUE-ONE-PIN-STRICT-REFILL, whose manifest scope is fixed \(m,n\ge3\), \(\pi/3<\phi\le\pi/2\), with \(p_{1,0}\) deleted and all other boundary labels fixed. It explicitly moves all \(K\) interior labels into the open parallelogram and ends with squared separation at least \(1+g\) for each pair involving a moved label, where
\[
g=\frac{(1-2\cos\phi)^4}{25\,000\,000\,000\,000(m+n)^{20}}>0.
\]
Thus it supplies strict capacity at least \(K\) for every strict angle in the range. Strict capacity is bounded above by weak capacity, so after shrinking the weak upper-bound interval if needed, both capacities equal \(K\).

This is sharp compatibility with Audit.187: the canonical one-pin oblique refill supplies exactly K strictly separated targets, while the plateau prevents upgrading that fixed-wall result to K+1 near the triangular angle. The distinct triangular two-pin capacity regression has only its listed frame scopes and is not used to infer the one-pin oblique bound. No actual wall is extracted from a canonical source.

I reconstructed the load-bearing endpoint separation as follows. Put \(\delta=1-2c>0\), \(L=m+n\), \(s=\delta/(100L^2)\), \(h=s^2/(100L^3)\), \(\beta=1/(10L^3)\), and \(r=(1,-c/a)\). Move column one by \(-s(n-j)(0,1)\), then columns \(2\le i<m\) by \(-h(m-i)f_jr\), where \(f_j=j(n-j)(1+\beta j)\). During stage one, the horizontal contacts touching column one have squared lengths \(1+s^2(n-j)^2\), and its vertical contacts have \(1+2as+s^2\). The only bottom vertical contact the downward motion could shorten is incident to the deleted \(p_{1,0}\), so that constraint is absent. The first-stage column-one points have \((u,v)\)-coordinates \((1+cs(n-j)/a,\ j-s(n-j)/a)\); these stay in the open frame since \(sn/a<1\) and \(m\ge3\). For a second-stage point, put \(H=h(m-i)f_j\); the vector \(r=(1,-c/a)\) has \((u,v)\)-coordinates \((1/a^2,-c/a^2)\), so the point coordinates become \((i-H/a^2,\ j+Hc/a^2)\). Since \(f_j\le n^2/2\), \(H<hL^3=s^2/100\); with \(a^2\ge3/4\), both coordinates remain strictly inside their frame ranges throughout stage two. The source constants give total point displacement below \(sn+3hL^3<\delta/(50L)\). Since \(u\cdot r=1\) and \(v\cdot r=0\), the block horizontal contacts lengthen by at least \(2h\) in squared distance and vertical block contacts gain
\[
\frac{h^2(m-i)^2(f_j-f_{j-1})^2}{a^2}\ge4\beta^2h^2=g.
\]
The difference is \(f_j-f_{j-1}=n-2j+1+\beta(2nj-n-3j^2+3j-1)\). The correction has magnitude below \(1/2\) for \(j\le n\le L\), \(L\ge6\). If the integer part is nonzero its absolute value is at least one, so the difference has absolute value above \(1/2\ge2\beta\). If it vanishes, then \(n=2j-1\) and the correction is \(\beta j(j-1)\ge2\beta\). At the end indices \(f_1,f_{n-1}\ge2\). Thus \(|f_j-f_{j-1}|\ge2\beta\) for all \(1\le j\le n\). The column-one/column-two interface starts with squared excess at least \(s^2\); the later motion changes its length by less than \(s^2/2\). These are the only unit-contact types that can lose slack. For every nonbasis grid difference, squared length is at least \(1+\delta\). A pairwise displacement change is below \(\delta/(25L)\), and a grid difference has length at most \(L\); using \(\lvert x+y\rvert^2\ge|x|^2-2|x||y|\), its squared length loses less than \(2\delta/25\), leaving more than \(1+23\delta/25\ge1+g\). This checks target-target pairs as well as target-boundary pairs; deleting \(p_{1,0}\) is essential.

For the cited packing equality case I checked the primary paper by Böröczky and Ruzsa, which states the Thue–Groemer inequality and Groemer's equality description. Their unit-disc center separation is two; scaling all lengths by one half gives the unit-separated point normalization used here. See [Note on an Inequality of Wegner](https://www.renyi.hu/~carlos/wegner.pdf), pp. 1–2.

## Reproduction and finite controls

- The pinned Audit.187 verifier's SHA-256 is ed32673b81d8764905003f6486a5228fc8d4caa516c9b2bf4818bff1b261e9b0; its rerun passed 1,042 two-stage pair constraints, 11,774 guarded source pairs, 82 removed contacts, 32 interior labels, and its listed perturbed-wall controls.
- verify.py uses exact rational coordinates at a rational angle strictly above \(\pi/3\) for seven small frames. It checks the reconstructed endpoint against every boundary pin and target pair, open-interior membership, the explicit displacement and margin bounds, the exact Oler population identity, and the control that restoring the deleted pin creates a subunit pair. Its run passed 1,261 target-bearing pair checks. These finite cases corroborate the construction; they do not prove the compactness or equality argument.

The destination candidate was imported from source e-99 PR #947 at head 1afb7e64d47c5619d872d32759b0e01f1526fd5a (tree 48b678c0d2695002595dc8aa9eaa6d1ac909e31b). The original source report hash was 91c0dc1b86aaf7b2941943dce132e258a3364709f6b00a67575d465bbe8189c4 (source Git blob 0325be2261b6eb1c1e9528feeb7883f8401ce0f8). Source Audit cycle 253 recorded PASS/promote and proposed state .236 there. That source disposition is historical evidence only: the destination candidate registry records this claim as unreviewed, and destination main does not adopt the source theorem-state transition. The referee ledger entry is pinned as an input below.

The offline overlap output exposed a short excerpt from the existing destination audit before I began this reconstruction. I disclose that exposure; this is not a blind review. The complete independent derivation above is recorded against destination main 7d0a450fe66991036541023f95c44c064a04b6a8, with the candidate artifact SHA-256 ce709b3988db6bae2b1deb5aacc0d5ed755e86bf7781e77e167e6203b0702f7c. Its destination lifecycle remains unreviewed in the registry. The destination theorem state stays 2026-10-15.publication.2, priority public-frontier.3, catalogue public-frontier.9. Level I, A, B and C-II remain open; C-I remains closed.

## Open next question

- **Downstream claim/decision:** a global Target C-II vacancy/refill route based on an actual near-triangular wall.
- **Exact quantity:** the number of mutually and boundary-separated points available in the wall interior after deletion of one boundary pin.
- **Changed hypothesis:** permit the wall to move or count outside points; this fixed-wall theorem applies only for one fixed \((m,n)\) and an interval depending on that frame.
- **What either outcome enables:** a counterexample to the plateau could reopen a fixed-wall local refill at those angles; confirming the plateau directs the route to moved-wall or outside-capacity payment.
- **First step:** formulate a moved-wall displacement or capacity bound that includes every retained source label.
- **Blocker:** the candidate does not extract such a wall from all canonical C-II sources or constrain exterior points.

## Attribution

First-party project reports and code were consulted at the pinned destination base. External theorem attribution is to H. Groemer's equality characterization and the cited Böröczky–Ruzsa paper. OpenAI Codex (GPT-6 Luna, xhigh) reconstructed and audited the proof, wrote the finite verifier and this report, and ran the listed checks. No canonical lifecycle or claim file was modified.
