> Generated reading edition · [exact source](../../../docs/audits/target_c_midpoint_mean_tail_second_referee_2026-10-10.md) · source SHA-256 `1a9ab31c0fa492cc56b4c625b279654a69005ad2d531a02da553b707da2a3d52`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-443896D300E0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent second referee — midpoint-tail counting bridge

Date: 2026-10-10\
Audit base: `origin/main=ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`\
Frozen source: `origin/research/level-i-fused-review-20261009=6132201c1d3056ca68a222217094acb819f5b4d7`\
Candidate: Sections 17.1–17.3 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`\
Reviewed proof: `docs/audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md`, proposed Audit.246.

## Verdict

**PASS — corroborate the midpoint-tail and near-diameter bounds.** I found no scope error or counterexample in the support-energy argument, the actual-edge endpoint injection, or the almost-diameter-pair localization. I made one proof clarification in the Audit.246 artifact: the derivative-band count uses windows of width `a/(2D)`, not arbitrary fixed-width windows.

## Independent reconstruction of the delicate band count

Let `E=int(h')^2<=C_E D`, with `h''>=-D`. For a dyadic band `a<=h'(n)<2a`, the normal lies in a component of `{h'>a/2}`. The energy bounds give total component length `Λ<=4E/a^2` and component count `N_c<=8DE/a^3`: every component has length-energy at least `a^3/(8D)` by the semiconvex ramp.

For any selected actual diameter endpoints whose chosen midpoint norms are at most `L`, strict support orders their normals along the hull arc. In a normal window of width `w<=1/2`, the chord directions advance by at least `cos(w/2)` in the central tangent direction. Writing each endpoint as `p=m_p+(D/2)n_p`, the tangent projection range is at most `D sin(w/2)+2L`. Unit separation then gives the bound `O(1+Dw+L)` in that window; the proof counts the selected endpoints directly and allows uncounted hull vertices between them.

For the band, (17.3) gives `L<=3a`. The derivative bound `|h'|<6D^(2/3)<=D` for `D>=216` makes every nonempty band satisfy `a<D`. Choose window width `w_a=a/(2D)<=1/2`. Each window holds `O(a+1)` counted endpoints, while all component arcs require `O(DΛ/a+N_c)` windows. Hence

`N_band = O((a+1)(DΛ/a+N_c)) = O(DE/a^2+(a+1)DE/a^3) = O(D^2/a^2)`

because `E=O(D)` and `a>=eta=3^(1/4)*sqrt(D)>1`. The negative band uses the backward ramp. Dyadic summation proves the derivative tail; `|m_p·n_p|<=eta` converts it to the midpoint-radius tail. Integrating the tail with `|B|<=P<=pi D` and the canonical worst-case radius `7D^(2/3)` gives the first and second moments as stated.

For every actual C-II diameter edge, Woodall's graph topology supplies a distinct endpoint assignment: root each tree and use its child endpoint; on the unique odd cycle assign each cycle edge to its head, and assign pendant edges to their leaves. These endpoints define admissible partner choices in the uniform endpoint theorem, so the edge tail and both edge-moment sums are bounded by the endpoint sums. No selected edge graph is substituted.

For a pair `p,x` with `d>=D-s`, the support deficits are nonnegative and sum to `h(nu)+h(-nu)-d<=s`. Tilting the support direction by `epsilon=D^(-1/3)` bounds each endpoint's tangent coordinate by `13D^(2/3)+2sD^(1/3)` using `|h'|<6D^(2/3)`, `1-cos(epsilon)<=epsilon^2/2`, and `sin(epsilon)>=epsilon/2`. The support interval gives `|h(nu)-h(-nu)|<=3eta`; combining it with the deficit sum yields the stated midpoint-normal bound `2eta+s/2`. This gives no pair-count estimate.

## Scope and disposition

Full-source support is retained throughout, including contact-isolated source points. The tail is unweighted and uniform over partner choices; it does not bound KKT stress mass. The near-diameter result counts no pairs. The actual-edge result depends on canonical `C-WOODALL` for the full diameter graph. No finite verifier encodes these analytic statements.

The window-width clarification repairs the exposition only; theorem statements, dependencies, state version, and Target C frontier are unchanged. C-II and Level I remain open. No discovery branch or worktree was modified.
