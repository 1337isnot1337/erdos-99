> Generated reading edition · [exact source](../../../docs/audits/target_c_near_port_conditional_promotion_audit_2026-10-08.md) · source SHA-256 `2e7efbb61ac640b1d998f0ee2d3d09318398aaaf3ffa68c1ee6605511c2d1cd4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E6BF70C5B602","canonical":true,"claim_ids":["C-NEAR-PORT-DEFECT-TAIL-ALTERNATIVE","C-TYPEII-NEAR-PORT-GRID-EXTRACTION"],"claim_statuses":{"C-NEAR-PORT-DEFECT-TAIL-ALTERNATIVE":"canonical","C-TYPEII-NEAR-PORT-GRID-EXTRACTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.175 — near-port grid and face-tail theorem integration

Date: 2026-10-08  
Audit base: origin/main=1f792c3a3e3973c09e84314dbe0f4050f5bbd9f7, state 2026-10-08.audit.170  
Frozen source: origin/research/sol-c2-deep-port-route-20261004 at a2ccd6161519c7d27482a7c6e751cd44e595e1b6, open PR #668  
Source report: docs/reports/target_c_deep_port_local_grid_defect_routes_2026-10-04.md  
Source report SHA-256: bf0ae00a71c86ac895059c6c5b9edff9fb2b27ccab4d6a62bd18efbce191b018  
Exact verifier SHA-256: 21367e572ced2b7967731ed817763717d21f7472778dd8f3f04709d217d861cc

## Audit boundary

This audit rechecks [Audit.136](target_c_typeii_near_port_grid_independent_audit_2026-10-08.md)’s cap-local grid implication and defect-tail alternative against the exact frozen PR #668 snapshot, then integrates the newer canonical Audit.173 local-grid theorem. It does not audit the extraction of a macroscopic cap from an arbitrary canonical source, the validity of a uniform vanishing tail premise, or any finite source move.

The canonical main state and all source refs were refreshed before this audit. Main remained at 1f792c3a3e3973c09e84314dbe0f4050f5bbd9f7, the deep-port branch remained at the frozen source SHA above, and the open Target C PRs were #737 and #668. No discovery-worker branch was modified.

The explicit canonical inputs are the [Audit.134 fixed-port route theorem](target_c_fixed_port_route_bound_independent_audit_2026-10-08.md), the [Audit.173 attachment-local grid theorem](target_c_uniform_harmonic_cells_global_diameter_access_independent_audit_2026-10-08.md), its [face-tail and cap supplement](target_c_typeii_face_tail_port_multiplicity_independent_audit_2026-10-08.md), and the canonical attachment-cell and coherent-grain modules named by the state dependencies below.

## Exact conditional claims

### Cap-local positive-height grid

Take an unbounded canonical post-ZF C-II sequence in the Type-II branch of C-FULLCORE-NEAR-DISK, with D tending to infinity and all source points retained. Fix epsilon in (0, pi/6). Assume one harmonic cell P=conv(A) with unloaded positive-contact component I, a convex host cap C_cap above a supporting chord, and a finite union G_cap of strict source-rhombus faces in I such that, for one fixed alpha>0 along the sequence:

- G_cap has area at least alpha D^2 and lies in int(C_cap) intersect P;
- a in A is an actual loaded attachment on the same designated host arc and has signed height eta(a)>=alpha D above the chord;
- eta>=0 on C_cap, and the cap package lies inside the full source force hull.

Then for every fixed rho in (0,min(1,alpha/2)), all sufficiently large members of the sequence contain, in I, an epsilon-coherent complete train grid with both shores of size at least c_(alpha,rho,epsilon)D. Every grid point lies in closed_ball(a,rho D) intersect int(P) intersect conv({a} union C_cap), and has height greater than alpha D/2 above the host chord.

The cap package remains an explicit antecedent. Audit.173’s canonical grid theorem gives a grid near every attachment without this package, but does not put that grid in the cap wedge or above this designated host chord. This conditional statement therefore retains distinct geometric content.

### Global face-tail alternative at every Type-II attachment

In the same canonical Type-II sequence, fix epsilon in (0,pi/6). For each attachment a in each unloaded positive-contact component I and each fixed rho in (0,1), use a complete grid supplied by canonical C-TYPEII-LOCAL-COHERENT-GRID-ACCESS. Its vertices lie within rho D of a. For each fixed integer M>=5, let T_M be the one global sum of (d(f)-4) over bounded faces of degree greater than M in all augmented harmonic cells.

1. If lim_(M->infinity) limsup_(D->infinity) T_M/D=0, then for every fixed lambda>0 there are fixed M and rho>0 such that, for all sufficiently large D, every actual attachment reaches every vertex of its selected local grid by an actual contact path in its own component of length less than lambda D. The grid shores remain linear in D, with constants depending on epsilon, rho, and lambda.
2. Conversely, suppose some fixed lambda>0 has this property: for every sufficiently small fixed rho>0 and all sufficiently large D, some actual attachment a in some component I has a vertex z in a grid supplied at radius rho with contact distance in I at least lambda D. The attachment, component, and grid may depend on D and rho. Then, for every fixed M>=5, liminf_(D->infinity) T_M/D>=lambda/10.

This alternative requires no macroscopic cap. It does not bound route multiplicity or positive KKT mass.

## Independent reconstruction

For the cap-local claim, put K=conv(G_cap) and K_rho=a+rho(K-a). The premise places G_cap in P but does not assume it lies in int(P). Strict containment follows from harmonic trapping: for any supporting functional of P, if an unloaded vertex of I attained its maximum, its positive equilibrium would force every contact neighbor to attain the same maximum. Connectivity of I propagates that equality to each actual loaded attachment in A, contradicting the noncollinear extreme attachment set. Thus every vertex of I lies in int(P); the rhombi in G_cap and their compact convex hull K lie there as well. Since K is also in C_cap and C_cap and P are convex, K_rho lies in int(P) intersect conv({a} union C_cap). Every point of K is a convex combination of source points and is at distance at most D from the source point a, so K_rho lies in the closed rho-D ball around a. Its area is at least alpha rho^2 D^2. The signed height is 1-Lipschitz, hence eta(x)>=eta(a)-rho D>alpha D/2 throughout K_rho.

The canonical Type-II coherent-rhombus deficit is o(D^2) globally, so it also bounds the deficit in this source-dependent K_rho. Rhombi meeting its boundary lie in a width-two boundary tube of area O(D), since K_rho is convex with perimeter O(D); deleting them costs O(D) faces. The remaining coherent rhombi have quadratic area and total physical interface perimeter O_epsilon(D). If their connected components have areas A_j and perimeters P_j, planar isoperimetry gives sum sqrt(A_j)<=sum P_j/(2 sqrt(pi))=O_epsilon(D). Since sum A_j>=cD^2, one component has area Omega(D^2). It is a subcomplex of one coherent grain with perimeter O_epsilon(D), so the canonical pseudogrid extraction yields linear-by-linear shores. All selected rhombi are inside int(P), have no loaded vertices, and lie in one unloaded contact component. If that component differed from I, its harmonic cell would have positive-area interior overlap with P, contradicting canonical cell interior-disjointness. This proves the same-cell conclusion without dropping contact-isolated source points.

For the tail statement, the Audit.173 local-grid theorem places every grid vertex z in (1-rho)a+rho P_I, hence |a-z|<=rho D. The canonical bounded-face route theorem gives an actual route in I with

    length <= K_M |a-z| + B_M + 5 T_M,

where K_M=C+200(M+1/2)/pi and B_M=C_0+100(M+1/2)^2, with C=4/sqrt(3)+30pi and C_0=90pi+30. The constants are fixed once M is fixed.

If the normalized global tails vanish, choose fixed M so that eventually 5T_M/D<lambda/4, then fixed rho so K_M rho<lambda/4. The route length is then below lambda D for all grid vertices once D is large enough; B_M/D tends to zero. The grid theorem keeps both shores linear for this fixed rho.

For the converse, fix M and choose fixed rho<lambda/(2K_M). The assumed obstruction supplies a z with route distance at least lambda D, while the route estimate gives lambda D<=K_M rho D+B_M+5T_M. Taking liminf after division by D gives liminf T_M/D >= (lambda-K_M rho)/5 >=lambda/10. This argument is uniform over the attachment and component chosen by the obstruction because T_M is global.

## Scope and hostile checks

- The route graph uses actual contacts in the specified unloaded component and the actual loaded attachment; the conclusion does not use arbitrary pins or scaffold vertices.
- Contact isolates remain in the full source. They are not assigned route-graph coordinates, deleted, or moved.
- The fixed-rho order is essential. No uniform linear grid shore is asserted when rho tends to zero with D.
- The tail is counted once globally. No route-disjointness, independent payment, stress-weight estimate, contact-opening motion, finite replacement, or strict sub-D competitor follows.
- The cap-local grid implication does not extract its cap package. The generalized tail implication does not establish either tail vanishing or a persistent route obstruction.
- The original exact verifier uses Fraction arithmetic. I reran it at the frozen source snapshot; it passed 14 exact harmonic-fixture augmented faces, 111 rational rhombi / 13,320 boundary pairs, 17,736 lattice source-pair checks, 3,164 thin-face source-pair checks, and three exact regressions. Inspection confirms that it checks finite fixtures and arithmetic only. It does not encode the Type-II density theorem, moving-cap localization, pseudogrid extraction, or the universal route implications.

## Verdict and disposition

- PASS — promote the exact cap-conditioned implication C-TYPEII-NEAR-PORT-GRID-EXTRACTION. Audit.173 subsumes only its bare near-port grid existence; the cap-wedge and positive-height conclusions remain additional conditional content.
- PASS — promote the strengthened implication C-NEAR-PORT-DEFECT-TAIL-ALTERNATIVE using the canonical local grid at every Type-II attachment. The cap package has been removed; the tail-vanishing antecedent and persistent-obstruction antecedent remain explicit hypotheses.
- No C-II frontier change. Neither theorem yields a source move, route multiplicity bound, strict sub-D competitor, exact triangle, or Level I conclusion. The current finite-move/payment obligation remains unchanged.

Both exact implications are recorded as canonical theorems with their unresolved hypotheses explicit in the statement. No canonical entry asserts that the cap package, tail-vanishing condition, or persistent route obstruction holds for an arbitrary canonical sequence.
