> Generated reading edition · [exact source](../../../docs/audits/target_c_one_deficit_root_packet_independent_audit_2026-10-07.md) · source SHA-256 `e26781caad680b1e1ea0b4e300761ae01f6e2d15e29235fecdf59a2673a78a6d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7DE7725C1A9C","canonical":true,"claim_ids":["C-M4-ONE-DEFICIT-ALL-SMALL-PACKET","C-M4-ONE-DEFICIT-ALL-SMALL-SOURCE-EXCLUSION","C-ONE-DEFICIT-EXACT-CURVATURE-PACKETS","C-ONE-DEFICIT-EXACT-CURVATURE-SOURCE-EXCLUSION"],"claim_statuses":{"C-M4-ONE-DEFICIT-ALL-SMALL-PACKET":"superseded","C-M4-ONE-DEFICIT-ALL-SMALL-SOURCE-EXCLUSION":"superseded","C-ONE-DEFICIT-EXACT-CURVATURE-PACKETS":"canonical","C-ONE-DEFICIT-EXACT-CURVATURE-SOURCE-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: one-deficit root packets

Date: 2026-10-07. Audit base: `baadff26b3fae1107f8ed2d9d18f03f78cd4a23b`, state `2026-10-07.audit.75`. Source branch: `research/sol/target-c-overnight-closure-20261007`, frozen at `4bb549bd0ae37e1c7015d80b650dabc224b695d6`. At refresh the branch was `5e7c3ee22263765aa2de4fd78ded5f1484228a14`; both source reports, both verifiers, and their data files audited here were unchanged. Later branch additions updating the audit ledger and state are not used.

Source artifacts:

- `docs/reports/target_c_one_deficit_all_small_curvature_M4_2026-10-07.md`, Sections 1--4;
- `docs/reports/target_c_one_deficit_certified_strict_root_packets_2026-10-07.md`, Sections 1--4.

The broad arbitrary-M continuation, arbitrary-wall extraction, and remaining C-II / Level I claims in those reports are not promoted.

## Exact claims and endpoint chain

The audit treats two conclusions separately.

**Claim A — `C-M4-ONE-DEFICIT-ALL-SMALL-PACKET`.** Let (t=\tan(\theta/2)>0). Use the specified six-sector sorting wall with (M=4), rates (3,1,-1,-3), and let (N=37). There is a (\theta_0>0) such that for every (0<\theta<\theta_0), after omitting the target chart site (h=(1,2)) and the actual wall vertex (v_0=(1,3)), there is a set of (N) points strictly inside the wall which are pairwise at distance strictly greater than one and strictly farther than one from every retained wall vertex. The packet consists of the 36 opened interior chart sites and one root point near (v_0). The root need not be clear of the deleted vertex (v_0).

**Claim B — `C-M4-ONE-DEFICIT-ALL-SMALL-SOURCE-EXCLUSION`.** For the same wall family and every (0<\theta<\theta_0), no contact-minimal, then diameter-pair-minimal, triangle-free global minimizer in canonical normal form can contain the full wall and (z\le36=N-1) actual source points in its strict interior.

**Claim C — `C-ONE-DEFICIT-EXACT-CURVATURE-PACKETS`.** Strict (N=3M^2-3M+1) packets exist for the five exact cases
$$
(M,t)\in\{(4,1/50),(5,1/50),(6,1/50),(8,1/50),(4,1/10000)\}.
$$
Each packet omits target site ((1,M-2)), omits one actual wall vertex ((1,M-1)), and is strictly inside the wall, pairwise unit-separated with strict slack, and strictly clear of all retained wall vertices.

**Claim D — `C-ONE-DEFICIT-EXACT-CURVATURE-SOURCE-EXCLUSION`.** In each of those five specified wall geometries, a contact-minimal, then diameter-pair-minimal, triangle-free global minimizer containing the full wall cannot have (z\le N-1) strict-interior source points.

The exact implication is

`strict N-site packet -> delete z old interior labels and one actual wall vertex -> insert z+1 packet sites -> preserve every exterior source point and all old-old pairs, create no contacts, lose at least two wall contacts, and keep every new distance strictly below D -> contradict canonical contact minimality or global minimality`.

It applies to an arbitrary old interior cloud: no lattice, sorting, vacancy, or source-contact pattern is assumed. All source points outside the wall, including contact isolates, remain in place.

## Independent construction and analytic audit

Write (u=(1,0)), (v=(1/2,\sqrt3/2)), (w=v-u), and
$$
\rho(t)=\frac{1-t^2+2it}{1+t^2}=e^{i\theta}.
$$
For (M=4), the descending-rate chart uses ((3,1,-1,-3)) and the finite sums stated in the source report. Consecutive outer-wall edge directions on a side are (\rho^{2j-3}w), (j=0,1,2,3); each has length one. Consecutive edges turn by (2\theta) within a side and by (\pi/3-6\theta) at a corner. For sufficiently small positive (\theta) these turns all lie in ((0,\pi)) and sum to (2\pi), so the closed wall is a strictly convex polygon. The 36 unpunctured interior chart sites limit to (P_3\setminus\{(1,2)\}\), strictly inside (H_4); since there are finitely many sites and wall supports, all remain strictly inside the curved wall for sufficiently small (\theta).

The exact symbolic verifier was inspected and rerun. It represents the 60-point wall-plus-chart set by rational functions in (t) with coefficients in (\mathbb Q(\sqrt3)). It identifies all 92 unit rows with a moving endpoint and certifies positive leading coefficients for every other pair's squared-distance gap. The 73-by-73 basis system has 72 moving coordinates and one common opening variable; its 73 pivots have known nonzero leading terms (70 of order zero and 3 of order one). All 92 resulting row margins have positive leading coefficients, of orders 0 through 6, with certified remainder order at least 9. These are exact Laurent-series sign certificates, not floating feasibility tolerances. The tracked truncation rules for addition, multiplication, division, and pivot inversion preserve a remainder (O(t^p)); every accepted leading coefficient occurs below that remainder order. Each pivot is therefore nonzero for all sufficiently small (t>0), and each row margin is eventually positive.

For each fixed small (\theta>0), choose a sufficiently small positive amplitude (\varepsilon) along the certified opening field. The 92 interior-involving exact contacts then become strict; every noncontact chart pair has a positive gap and remains so for small enough (\varepsilon). The wall's own unit sides remain as old contacts. This finite choice is made separately at each (\theta); no uniform amplitude or bound on the velocity field is needed.

For the added root, let (\xi=(1,3)) be the deleted wall vertex and put
$$
r_\theta=\xi+3\sin\theta\,J(\rho^2w).
$$
Its two adjacent wall-edge distances satisfy ( |r_\theta-q|^2=1+3\sin^2\theta>1). At (\theta=0), the only remaining interior unit neighbor of (\xi) after deleting (h=(1,2)) is (a=(0,3)). Direct differentiation gives
$$
(\xi-a)\cdot(r'_0-a'_0)=\frac{3\sqrt3}{2}>0,
$$
so this last root-to-chart lower constraint opens for small positive (\theta); all other root-to-chart and root-to-wall distances have strict limiting margin. For the collinear limiting side, write its four directed edges as (E_j(\theta)), (j=0,1,2,3), with initial endpoints (W_j(\theta)). At zero, (E_j=w) and (\xi-W_j=(3-j)w); differentiation gives (E'_j=(2j-3)Jw), (W'_j=-j(4-j)Jw), and (r'_0=0). Thus the inward signed cross-product derivative is
$$
\operatorname{cross}(E'_j,\xi-W_j)+\operatorname{cross}(w,r'_0-W'_j)
=-(3-j)(2j-3)+j(4-j)=(3-j)^2-(3-j)+3>0.
$$
All other wall supports have positive margin already at (\theta=0). Hence (r_\theta) lies strictly inside the curved wall. Its strict clearances from the opened chart sites persist after choosing (\varepsilon) small enough. This proves Claim A without inferring a finite motion from first-order feasibility alone.

## Full-source exchange check

For a source with this wall, every source point on its boundary is a wall vertex: a nonvertex point on a unit edge is within (1/2) of an endpoint and violates unit separation. Thus all other points in the closed wall are counted by (z) and deleted. Claim A supplies (z+1\) packet points whenever (z\le36\).

All inserted points lie strictly inside the convex wall and are strictly farther than one from every wall vertex except the deleted (v_0). The canonical `C-ONE-VERTEX-CONVEX-WALL-SHIELD` therefore gives strict lower clearance from every retained exterior source point, including isolates. For any retained old point (y), the function (x\mapsto|x-y|^2) is strictly convex on the wall polygon; its maximum is attained at wall vertices, and an interior (x) cannot attain that maximum. Every wall vertex belongs to the old source, so the maximum is at most the old diameter (D), and every new-to-retained distance is strictly below (D). For an interior packet point (y), its distance from every wall vertex is strictly below the wall diameter: moving (y) a short step away from that vertex stays inside the wall and increases the distance. The maximum of (x\mapsto|x-y|^2) on the wall is attained at a wall vertex, hence every new-to-new distance is strictly below the wall diameter and therefore below (D). The finite certificates check this directly for their exact cases. Retained old-old pairs are unchanged.

No inserted-involving pair is a unit contact, so the replacement creates no new contact or unit triangle. Removing (v_0) removes its two unit wall contacts, so (j=0<t). The canonical `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` excludes the replacement: if the diameter drops global minimality fails; if it stays (D), contact minimality fails. This proves Claims B and D while retaining all exterior points and isolates.

## Finite exact cases and computational certificate audit

The source finite verifier and all inputs were inspected and rerun at the frozen snapshot; its generated JSON exactly matches the saved certificate. The audit copy in this promotion inlines the exact chart construction rather than importing the source branch's newer optional-parameter change to the canonical sorted-rate helper; this avoids changing that canonical helper, and the adapted verifier reproduces the same saved JSON. It uses rational (t,\varepsilon) and exact (\mathbb Q(\sqrt3)) arithmetic. For (t=1/50), it verifies 830 opening rows, 34,535 strict new lower pairs, the same number of strict upper pairs, and 14,106 wall-containment tests across (M=4,5,6,8). The separate (M=4,t=1/10000) case checks 92 opening rows, 1,517 strict lower and upper pairs, and 888 containment tests. Every old exact unit pair with a moving endpoint has a positive directional margin. The code uses a floating key only to select a candidate wall-diameter pair, then checks exactly that the selected squared distance is at least every wall-pair squared distance; no floating comparison enters the certificate. The final packet inequalities, wall contacts, containment, and population counts are exact.

These finite checks do not prove an all-small-curvature result for (M=5,6,8), or an arbitrary-(M) construction. The universal M4 statement comes from the Laurent certificate and the analytic root/support argument, not extrapolation from the finite samples.

## Hostile scope and frontier effect

- Audit.70's affine full-grid regression does not contradict these packets: the auxiliary chart has a deleted interior site, the actual wall vertex is deleted from the source, and the contact-opening field is not an affine motion preserving all six guards.
- Audit.71's nested-ring energy demand remains valid for its complete chart and guard hypotheses; this packet opens a punctured chart and removes one actual wall vertex.
- Audit.72's general one-corner packet excludes (z\le N-2) under its stated area condition. These new results add the (z=N-1) exclusion only for the specified M4 all-small-curvature family and the listed exact geometries.
- Audit.74 still leaves the (z=N) population. For the M4 wall as (\theta\downarrow0), the only unexcluded population after this audit is (z=N=37), which audit.74 localizes asymptotically to (P_3) but does not classify or exclude.
- No arbitrary curved-wall extraction from a canonical source, arbitrary-M small-curvature exclusion, macroscopic-container transfer, C-II closure, or Level I result follows.

**Verdict: PASS — promote Claims A--D at the exact scopes above.** The strict-root finite certificates and the M4 all-small Laurent theorem are independent modules; broader source-report assertions remain unreviewed.

## Audit.242 clarification — interior isolate accounting

The source-exchange prose above that says the move retains “all exterior points and isolates” is too broad if read to include contact-isolated labels strictly inside the wall. The exchange deletes every strict-interior label, including any interior contact isolates, and one wall vertex, then inserts `z+1` packet points. Those isolates are included in the population `z` and are not lost from the cardinality count; their label identities are not retained. Every old source point outside the wall, including exterior contact isolates, is retained. The canonical source-exclusion conclusion is unchanged.
