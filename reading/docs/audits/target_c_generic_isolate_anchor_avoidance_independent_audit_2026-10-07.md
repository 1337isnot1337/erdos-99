> Generated reading edition · [exact source](../../../docs/audits/target_c_generic_isolate_anchor_avoidance_independent_audit_2026-10-07.md) · source SHA-256 `866ae69ddc13d9da6a90822f0a9ec16e7b1b42601876eeda28212cd84ad82481`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-65B00B3DF4D9","canonical":true,"claim_ids":["C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE","C-LOADED-UNIT-ANCHOR-STRICT-OBTUSE","C-SHORT-WALL-WEAK-CLEARANCE-CLASSIFICATION","C-STATIC-SINGLETON-UNLOADED-ANCHOR"],"claim_statuses":{"C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE":"canonical","C-LOADED-UNIT-ANCHOR-STRICT-OBTUSE":"canonical","C-SHORT-WALL-WEAK-CLEARANCE-CLASSIFICATION":"canonical","C-STATIC-SINGLETON-UNLOADED-ANCHOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: independent audit of generic isolate anchors and static singleton constraints

Date: 2026-10-07. Audit base: `origin/main=4753030e5fcd17997a06872a93ae3da3d1679155`, state `2026-10-07.audit.99`.

## Frozen source and audit boundary

Source: PR #722 branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`; report `docs/reports/target_c_generic_isolate_anchor_localization_2026-10-05.md`, SHA-256 `2efbbfcc67e50f12cf218ea00d17ba9a1bc4a20b2cd40e9dd22edaab23936ca3`. I audited §§2--3, §5, and the loaded-anchor argument in §6 as four separable claims. Section 4's fan reflection and the report's other broader static-route conclusions are not promoted here.

The proof-only report is not treated as authority. The results below are reconstructed from the stated geometry and the current canonical inputs. No numerical verifier is claimed or needed.

## Claim 1 — generic isolate perturbation and anchor avoidance

Take a canonical C-II source in the contact-first, diameter-pair-second normal form `C=C_*`, `H=H_*`. Let `V` be its nonisolated positive-contact core and `Z` its contact isolates, retained in the full source. In this normal form every actual diameter pair is strong and has positive coefficient in a relative-interior stress. A contact isolate cannot be incident to a positive diameter pair: if `z` were such an endpoint, its contact forces vanish. For any two diameter partners `a,b` of `z`, `|a-b|<=D=|z-a|=|z-b|`, so the unit directions from `z` to its diameter partners have pairwise dot product at least `1/2`. Their positively weighted sum therefore has positive dot product with any one of those directions, contradicting equilibrium at `z`. Thus every pair containing a contact isolate has strict distance in `(1,D)`.

Fix the core and vary all isolate coordinates in a sufficiently small open product neighborhood; every old isolate-involving pair remains in `(1,D)`. For any old triple containing an isolate, define

`F(a,b,c)=|a-b|^2|b-c|^2|c-a|^2-4 det(b-a,c-a)^2`.

For noncollinear triples, `F=0` exactly when the circumradius is one. Collinear distinct triples have `F>0`. This is a nonzero polynomial in the free isolate coordinates: freeze the other two labels at their distinct original positions and send one isolate coordinate to infinity. The product term then has a positive degree-four leading term with coefficient equal to the squared distance between the frozen pair; the determinant square has degree at most two. Likewise `G(a,b)=|a-b|^2-4` for an isolate-containing pair is a nonzero polynomial. There are finitely many such conditions. Their zero sets have empty interior, so every feasible isolate neighborhood contains perturbations avoiding all of them.

Consequently one may perturb isolates arbitrarily little while keeping the core fixed, preserving every contact and diameter pair and the canonical minimizing status, and ensuring that (i) no old triple containing an isolate has unit circumradius and (ii) no isolate-containing pair has length two. This is source-dependent genericity; it supplies no uniform slack or a bound on isolate population.

If a locally pinned singleton replacement has at least three retained unit neighbors strictly surrounding its new point, no such neighbor can be an isolate. Otherwise any triple consisting of that isolate and two other distinct unit neighbors is an old-source triple on the new point's unit circle, contradicting (i). The neighbors are distinct and noncollinear because a line meets a circle in at most two points.

## Claim 2 — weak-clearance classification for walls with at most six edges

Let a simple cyclic polygon have `n<=6` edges, each of length at most one. Let `x` be strictly inside and suppose `|x-v_i|>=1` for every cyclic vertex. Write `r_i=|x-v_i|` and let `theta_i` be the principal signed angle between consecutive radius vectors. The cosine law gives

`cos(theta_i) >= (r_i^2+r_(i+1)^2-1)/(2 r_i r_(i+1)) >= 1/2`,

because

`r_i^2+r_(i+1)^2-r_i r_(i+1)-1 = (r_i-r_(i+1))^2+r_i r_(i+1)-1 >= 0`.

No wall edge can pass through `x`, since that would make its length at least two. The interior winding is therefore `+/-2pi`, while `|theta_i|<=pi/3`. Thus

`2pi <= sum_i |theta_i| <= n*pi/3 <= 2pi`.

Every inequality is equality. Hence `n=6`, each radius is one, and all six turns have the same sign and magnitude `pi/3`: the wall is a regular unit hexagon centered at `x`. Conversely that center is weakly clear. Inserting it creates a unit equilateral triangle with each adjacent wall edge. Therefore a triangle-free replacement cannot use a weak-clearance site inside an intact wall of at most six edges. This classifies only that local geometry; it does not rule out a strict-diameter competitor that is allowed to contain a triangle or a move that deletes a wall guard.

This sharpens the canonical strict-clearance result `C-SHORT-WALL-ZERO-CAPACITY`: the only weakly clear exception is the regular hexagon center, and it forces a triangle after insertion.

## Claim 3 — three loaded unit anchors form an obtuse triangle at large diameter

Assume a canonical full-source minimizer with diameter `D>=10000`. Let three distinct actual loaded diameter endpoints `v_1,v_2,v_3` lie on one unit circle with center `x`. Choose an actual diameter partner `a_i` for each and set

`m_i=(v_i+a_i)/2`, `n_i=(v_i-a_i)/D`.

By canonical `C-FS-GEOM`, all diameter-pair midpoints lie within

`L_D=sqrt(D*eta+eta^2)`

of one source circumcenter, where `eta=3^(1/4)*sqrt(D)`. For `D>=10000`, `L_D<D/8`: using `3^(1/4)<4/3`,

`L_D^2/D^2 < 4/(3*sqrt(D))+16/(9*D) <= 4/300+16/90000 < 1/64`.

Since `|v_i-v_j|<=2`,

`D|n_i-n_j|=|2(v_i-v_j)-2(m_i-m_j)| <=4+4L_D`.

Thus the smaller angle between any two `n_i,n_j` is at most `2 asin(1/4+2/D)`, which is less than `pi/2`. Relative to `n_1`, lift the other two directions into this short interval. Their difference is below `pi`, so their pairwise angular bound implies that all three directions lie in one ordinary interval of width less than `pi/2`.

Each `n_i` is a strict supporting normal at `v_i`: for every other source point `w`, the diameter bound `|w-a_i|<=D` expands to

`n_i dot (w-v_i) <= -|w-v_i|^2/(2D) < 0`.

Order the three vertices by their normal angles. The directed edge `v_2-v_1` lies strictly between the quarter-turns of `n_1,n_2`; likewise `v_3-v_2` lies between the quarter-turns of `n_2,n_3`. Their directions differ by less than `pi/2`, so the triangle's interior angle at `v_2` is strictly greater than `pi/2`. Its circumcenter `x` is outside the closed triangle. In particular, no triple of loaded vertices on a unit circle can contain its center in its convex hull.

## Claim 4 — a pinned singleton needs an unloaded core anchor

Under the hypotheses of `C-ONE-SITE-CONTACT-SURROUND`, a locally pinned one-site replacement strictly inside the old hull has its unit-neighbor vectors surrounding the new point. If all those neighbors were loaded, triangulate their convex hull. The new point lies in a closed triangle whose three vertices are loaded and lie on the same unit circle centered at it. Claim 3 says that center lies outside every such triangle, a contradiction. Therefore at least one unit neighbor is an unloaded source point. Claim 1 excludes contact isolates from all these anchors, so this is an unloaded positive-contact-core neighbor.

This is a necessary anchor condition, not an existence theorem. It gives no interior site, packet capacity, simultaneous compatibility, diameter improvement, or C-II closure. The report's Section 4 fan-reflection claim and any inference from this anchor condition to a population/capacity bound remain unaudited.

## Verdict and canonical disposition

**PASS WITH NARROWED SCOPE.** Promote the four separately stated claims as `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE`, `C-SHORT-WALL-WEAK-CLEARANCE-CLASSIFICATION`, `C-LOADED-UNIT-ANCHOR-STRICT-OBTUSE`, and `C-STATIC-SINGLETON-UNLOADED-ANCHOR`. The last is conditional on the canonical one-site pinning hypotheses and `D>=10000`. No claim about the existence of the new anchor/site or any packet is promoted. The exact static anchor frontier is now: any pinned singleton replacement in scope must use at least one unloaded core unit neighbor; its population and full-source clearance remain unproved.
