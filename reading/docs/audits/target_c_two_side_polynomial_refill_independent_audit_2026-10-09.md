> Generated reading edition · [exact source](../../../docs/audits/target_c_two_side_polynomial_refill_independent_audit_2026-10-09.md) · source SHA-256 `ee9a73f573d9b75904838e0607fc113981e77c4e8bb4bd68f8f859877e27fcf5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5FF0E3FB7A3C","canonical":true,"claim_ids":["C-OBLIQUE-TWO-SIDE-POLYNOMIAL-STRICT-REFILL","C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-OLER-RESIDUAL","C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-POPULATION"],"claim_statuses":{"C-OBLIQUE-TWO-SIDE-POLYNOMIAL-STRICT-REFILL":"canonical","C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-OLER-RESIDUAL":"canonical","C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-POPULATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: polynomial-margin two-side oblique refill

**Date:** 2026-10-09
**Audit base:** `origin/main=1c1abea8e51f0c6af53783e24835563b86efa47e`, state `2026-10-09.audit.188`
**Frozen source:** `origin/research/sol/target-c-level1-gpt61-2026-10-04` at `9875cd6a77939bb6347353fc798ab8f9ab03ec3e`
**Classification:** independent reconstruction; **PASS — promote three exact, scoped claims**.
**Target effect:** the result adds a uniform growing-frame constraint for actual near-oblique walls. It does not extract such a wall from an arbitrary source or change the C-II finite-move/payment obligation.

## Candidate snapshot and certificate

The candidate is `docs/reports/target_c_two_side_polynomial_collective_refill_2026-10-05.md`, SHA-256 `f6b75c01c629bbb4aa33a825f50ff991061f0b20622743af45a8174f03c81b25`. Its verifier is `research/verify_target_c_two_side_polynomial_refill_2026_10_05.py`, SHA-256 `741eab5d14f3d147e4a5a6ad517422311d5fb37b471f7cb43a38c87f833396ec`. It imports exact arithmetic helpers from `verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05.py` (SHA-256 `959129b75bca577c6820ec00e96af8e28ac239c1ef6e4c3a07c450c6bc6eff4c`), vector helpers from `verify_target_c_one_vacancy_collective_strictification_2026_10_05.py` (SHA-256 `a7dde4b19c70f31266d3e17c781d2523238e25d4e1abc04b251d8d5c7ec1249a`), and the full-source replacement fixture from `verify_target_c_vacancy_funded_unit_wall_activation_2026_10_05.py` (SHA-256 `53660a5a8d61c512065d1b188a3e6259a03cc4cf59f3510090c2c3d10b282746`).

I inspected and reran the verifier at the frozen source tip. It passes 3,694 exact local pair checks, 30,440 complete guarded source-pair checks, records 259 lost contacts, and moves all 119 interior labels across six fixtures. Its arithmetic is exact in rational and Q(sqrt(3)) coordinates. The fixtures include the triangular endpoint, strict oblique and square frames, and nearby actual walls. They verify only those finite packets; the analytic inequalities below carry the universal claims. The script is not registered as a theorem certificate.

## Exact claims

Let integers m,n be at least four, L=m+n, u=(1,0), v=(cos(phi),sin(phi)), and pi/3 <= phi <= pi/2. Write q_(i,j)=i*u+j*v for 0<=i<=m and 0<=j<=n, with K=(m-1)(n-1) interior labels. Delete the bottom labels (i,0) for 0<=i<m and the left labels (0,j) for 1<=j<n. This deletes J=L-1 boundary labels and leaves every other boundary label fixed.

Set epsilon=1/(10 L^4), t=1/(100 L^3), I=m-i, and Q=n-j. Move each interior label along

    q_(i,j)(s) = i*u+j*v - s*t*I*Q*(1+epsilon*I)*(u+v),  0<=s<=1.

**C-OBLIQUE-TWO-SIDE-POLYNOMIAL-STRICT-REFILL.** This simultaneous segment is unit-separated throughout; each interior point stays in the reference parallelogram and moves less than 1/100. At the endpoint, every pair involving at least one moved label has squared distance at least 1+g_L, where g_L=3/(250000 L^14). Boundary-to-boundary pairs need not become strict.

Now let A be a triangle-free global minimum-diameter configuration selected contact-minimal within the triangle-free global-minimizer class. Suppose it contains an actual simple unit-contact cycle W with 2L distinct vertices in the ordered boundary correspondence above, each within eta_L=g_L/(4(L+1)) of its reference vertex after one Euclidean isometry. Let z count every source point in int(W), including contact isolates.

**C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-POPULATION.** No convexity is assumed for W, and

    z >= K-J+1 = mn-2m-2n+3.

All exterior source points, including isolates, remain at their original coordinates in the replacement argument. If W is convex with area A_W and r_W=A_W/(sqrt(3)/2)-L+1-z, then the following exact corollary also holds:

**C-OBLIQUE-TWO-SIDE-POLYNOMIAL-WALL-OLER-RESIDUAL.**

    r_W <= mn*(sin(phi)/(sqrt(3)/2)-1) + L-2
           + (2L*eta_L+L*eta_L^2)/(sqrt(3)/2).

## Independent reconstruction of the motion

The nonzero lattice differences of length below sqrt(2), apart from basis contacts, can only be the short diagonal u-v. For a horizontal or vertical unit step with at least one interior endpoint, lambda=I*Q*(1+epsilon*I) strictly decreases as the corresponding index increases. The difference vector therefore acquires a positive component along u or v; its squared-length excess is at least 2s*t along the path and at least 2t at the endpoint. Retained wall-to-wall edges have lambda=0 at both ends and remain fixed.

For a short diagonal, the change in lambda between (I,Q) and (I-1,Q+1) has integer part I-Q-1 and an epsilon correction of magnitude at most 2 epsilon L^3 < 1/2. If the integer part is nonzero, the difference has magnitude at least 1/2. If it is zero, I=Q+1 and the correction has magnitude epsilon*I*Q >= 2 epsilon. Thus every such diagonal involving an interior label has |Delta lambda|>=2 epsilon. With c=cos(phi), d=s*t*Delta lambda, and |d|<1, direct expansion gives

    |(u-v)-d*(u+v)|^2 - 1
      = (1-2c)*(1-d^2) + 3*d^2 >= 3*d^2.

This holds for every s in [0,1], including c=1/2 where the diagonal begins at contact. At s=1 its excess is at least 12*t^2*epsilon^2=g_L. A basis endpoint excess is at least 2t>g_L. Other noncontact lattice pairs start at distance at least sqrt(2); the relative displacement is at most sqrt(3)/(25L), so for L>=8 their distance remains greater than 1.4 throughout, giving squared excess greater than 0.96>g_L. Since lambda<=2L^2, both oblique coordinates decrease by at most 1/(50L), keeping every interior label inside. These checks establish the asserted path and endpoint margins, including the triangular limiting angle.

## Actual-wall replacement and population bound

Every reference endpoint target is at distance at most L+1 from each reference wall vertex. Perturbing a retained wall vertex by at most eta_L lowers its squared target distance by at most 2(L+1)eta_L=g_L/2. Hence all target-to-retained-wall distances remain strictly greater than one. The targets and their reference starting sites remain inside the actual simple cycle: their reference depth is at least sqrt(3)/2-1/100, while the ordered boundary homotopy stays within eta_L of the reference boundary.

For any old exterior source point y, every actual wall vertex is at distance at least one from y. Each reference interior site q is at distance at least 1-eta_L>=19/20 from every actual wall vertex. The segment [q,y] crosses an actual unit side; if it passes through a wall vertex, perturb y within the open exterior by less than 1/20, so its distances to all wall vertices remain at least 19/20, use a side-interior crossing, and take a limit. The canonical `C-UNIT-SIDE-CROSSING-SEPARATION` bound gives |q-y|>=sqrt(261)/10. The target moves less than 1/100, so every target remains farther than 3/2 from y. This handles all exterior labels, including contact isolates, without requiring targets to clear deleted wall coordinates.

If z+J<=K, delete all z interior source points and the J designated wall points, and assign those z+J labels to distinct strict targets. All new lower constraints are strict, old retained pairs are unchanged, and each target lies in int(conv(A)) because it lies strictly inside the nondegenerate simple cycle whose vertices belong to A. Every pair involving a target is consequently strictly shorter than the old diameter D: if such a pair attained D with an interior target, moving that target a small distance away from its partner while remaining in conv(A) would create a pair longer than D. If the new diameter were below D, global optimality would fail. If it equals D, the competitor is still triangle-free and has fewer unit contacts: the deleted cycle vertices remove old contacts, while every target has strict distance from every retained point and other target. This contradicts contact-minimality in the triangle-free global-minimizer class. Therefore z+J>K, giving the stated integer bound.

For convex W, the shoelace formula gives |A_W-mn sin(phi)|<=2L eta_L+L eta_L^2: the linear variation is at most L eta_L per vertex and there are 2L vertices, while the quadratic terms sum to at most L eta_L^2. Substitution of z>=mn-2L+3 into the definition of r_W gives the displayed residual bound.

## Comparison, regressions, and scope

- The canonical one-pin oblique result has the stronger population conclusion z>=K for phi>pi/3, but its angular margin and wall tolerance depend on 1-2cos(phi). The present theorem supplies an explicit tolerance independent of phi, at the cost of an L-1 boundary bank and a weaker population bound.
- At phi=pi/3, Audit.192 gives z>=K-1 in a fixed-frame neighborhood, stronger than this theorem's z>=K-L+2. Audit.192's tolerance depends on the fixed frame and is not uniform for growing frames. The new theorem does not supersede it.
- The source report's phrase that the residual estimate “recovers the original triangular residual threshold” is not adopted. At phi=pi/3 the displayed estimate gives r_W<=L-2 plus the explicit area error. Audit.192's stronger fixed-frame population bound instead yields r_W<=1 plus its own frame-dependent area error.
- The report does not extract a near-frame wall or the required population deficit from an arbitrary canonical source. The finite verifier's guarded configurations are not certified global minimizers. No C-II closure, Level I conclusion, frame-overlap payment, or general macroscopic-container capacity follows.

## Verdict and promotion

The simultaneous strictification, actual-wall population implication, and convex-wall residual corollary all pass at the exact scopes above. The actual-wall theorem depends only on the new refill and canonical `C-UNIT-SIDE-CROSSING-SEPARATION`; the finite motion has no theorem dependency. The three claims are entered as canonical at state `2026-10-09.audit.189`. C-II and Level I remain open, and the exact global finite-move/payment obligation is unchanged.
