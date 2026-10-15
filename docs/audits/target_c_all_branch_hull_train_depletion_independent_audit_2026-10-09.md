<!-- theorem-state: {"artifact_id":"ART-1F513BE69946","canonical":true,"claim_ids":["C-ALL-BRANCH-HULL-TRAIN-DEPLETION"],"claim_statuses":{"C-ALL-BRANCH-HULL-TRAIN-DEPLETION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of all-branch hull-train depletion

Date: 2026-10-09  
Audit base: origin/main `baa7a450757f39a28a0e44770bc2ffe4d2896f3e`, state `2026-10-09.audit.197`  
Frozen source: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`  
Source artifact: Section 9 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.

## Exact claim and verdict

Consider any unbounded canonical post-ZF Target C-II sequence, in either exhaustive global branch, with D tending to infinity and all source points retained. Let B be the cyclic loaded-hull vertex set, q its size, m_H the number of nonunit sides of conv(B), and g=q-m_H the number of unit loaded-hull sides. Let T=q-k+2f be the full stopped-train population, including singleton contact trains, where k=d_H+s_Z and f is the number of bounded nonquadrilateral contact faces. Let H_L be the trains with at least one terminal occurrence on a unit loaded-hull side; let N_0=T-|H_L|. Let R_4 count bounded quadrilateral contact faces and R_H count those whose train-crossing edge is incident to H_L.

The candidate proves, in both branches,

    R_H=o(D^2),
    N_0 >= 2 sqrt(R_4) - o(D).

Its two exact all-branch consequences are

    5(q-k)+x_B+m_H+2 >= 3 P_F + 2 sqrt(R_4) - o(D),

    4 mu_D D >= 2 P_F + 2 sqrt(R_4) + k + 3 m_H - o(D),

where P_F=per(conv(B)), x_B=b-q, and mu_D D=e_BB+2s_C-3k. The second consequence uses the canonical sufficiently-large-D equality e_BB=q-m_H and the canonical component estimate c_I=O(sqrt(D)).

**Verdict: PASS — promote `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`.** The statement is asymptotic; it does not assert a finite zero-error Mantel bound. It creates no packet, motion, payment, strict sub-D competitor, C-II closure, or Level I result. It strictly extends the hull-train incidence depletion conclusion to both branches without requiring the Type-II near-disk hypothesis. Its scalar corollaries are recorded in the same theorem entry because they follow from this bound and exact canonical ledgers.

## Independent proof reconstruction

### Normal-window count

For each selected actual diameter endpoint p choose an actual partner p' at distance D. Put m_p=(p+p')/2 and n_p=(p-p')/D. For every other source point x, the diameter upper bound gives

    n_p dot (x-p) <= -|x-p|^2/(2D) < 0.

Thus p is a strict exposed vertex of the full-source hull, even when contact-isolated source points are present. If all actual diameter midpoints lie within L_D=o(D) of one center, the projection argument in the frozen Section 8.1 gives, for any oriented normal window of half-width t<pi/2,

    count <= 1 + (D sin(t)+2L_D)/cos(t).

For t<=1/4 this is at most 1+2Dt+4L_D. The argument orders the selected exposed endpoints on the full-source convex boundary; intervening source vertices do not invalidate the projection interval or the unit-separation chord lower bound. Canonical C-FS-GEOM supplies L_D=sqrt(D eta_D+eta_D^2)=o(D), with eta_D=3^(1/4)sqrt(D).

### Trains in one phase bin

Fix epsilon in (0,pi/6). C-PUNCTURED-PHASE gives E_4=O(D) and an exact real phase potential after O(D) crossing deletions. The fixed-width coarea argument in C-COHERENT-GRAINS deletes a further O_epsilon(D) crossing relations so each retained relation has both train potentials in one epsilon-wide bin. This holds in both post-ZF alternatives and does not remove any source point, contact, or rhombus from the source; only auxiliary crossing-graph edges are deleted.

Each train in H_L is assigned one of its unit loaded-hull terminal sides. The assignment is injective: each side is one contact edge and belongs to one stopped train, and distinct cyclic sides have distinct starting endpoints. In a fixed phase bin, the side direction is in one of three projective intervals of width epsilon. Its starting endpoint's strict full-source diameter normal is within (4+8L_D)/D of one of the two normals to that side, by the two endpoint support inequalities and the unit-chord midpoint identity. Hence the chosen normals lie in six oriented windows of half-width

    t = epsilon/2 + (4+8L_D)/D.

For large D, t<=1/4. Applying the normal-window count separately to the six windows bounds the number h_j of H_L trains in bin j by

    h_j <= 6(1+2Dt+4L_D)
         = 6 epsilon D + 120 L_D + 54.

The bound is independent of the phase shift and bin location. No concentric annulus for the loaded force hull is used.

### Crossing depletion and Mantel

Let T_j be the total train population in bin j. The canonical actual train-crossing graph is simple; therefore retained crossing edges incident to H_L are at most sum_j h_j T_j. The full train count obeys T=q-k+2f<=3q<=3 pi D: indeed Q=2(q-k)-b<=q from b>=q and k>=0, f<=Q, and q<=per(conv(B))<=pi D. The O_epsilon(D) deleted relations contribute at most O_epsilon(D) further incident rhombi. Consequently

    R_H <= (6 epsilon D + 120 L_D + 54) 3 pi D + O_epsilon(D).

For each fixed epsilon, divide by D^2 and let D tend to infinity. Since L_D=o(D), the limsup is at most 18 pi epsilon. Then let epsilon decrease to zero. This proves R_H=o(D^2).

After removing only the H_L vertices from the auxiliary simple triangle-free train-crossing graph, N_0 vertices and R_4-R_H edges remain. Mantel gives N_0>=2 sqrt(R_4-R_H). Since sqrt(R_4-R_H)>=sqrt(R_4)-sqrt(R_H) and sqrt(R_H)=o(D), the claimed N_0 bound follows. This deletion is solely in the auxiliary graph.

### Exact ledger corollaries

The number of good loaded-hull terminal occurrences is g=q-m_H. Section 61 gives at most two trains with both terminal occurrences good; it does not bound the number of trains with at least one good end. Thus |H_L|>=g-2. Therefore

    N_0 <= T-g+2 = 2f-k+m_H+2 <= 2Q-k+m_H+2.

Using Q=2(q-k)-b, b=q+x_B, f<=Q, and b>=P_F gives

    5(q-k)+x_B+m_H+2 >= 3P_F+2 sqrt(R_4)-o(D).

For the second corollary, the sufficiently-large-D endpoint incidence theorem says every loaded-loaded unit contact is a full-source hull side, hence a loaded-hull side. Conversely every unit loaded-hull side is an actual contact. So e_BB=q-m_H. Substituting in the exact C-LOADED-HULL slack identity yields

    mu_D D = e_BB+2s_C-3k = q+m_H-k-2c_I-4.

Combining the same N_0 upper/lower bounds with b>=P_F gives

    4q-5k+m_H >= 2P_F+2 sqrt(R_4)-2-o(D).

Multiplication of the exact mu identity by four then yields the stated inequality with error O(c_I+1)+o(D). Current canonical C-HARMONIC-COMPONENT-SQRT-COUNT gives c_I=O(sqrt(D)), which is o(D); no older O(D^(2/3)) estimate is needed.

## Hostile checks and scope

- All source points, including contact isolates, remain in the full-source diameter support inequality. Strict exposure is from an actual diameter partner, not from selected stressed edges.
- H_L consists of all trains with one or more actual unit loaded-hull terminal sides. The only “at most two” fact is about trains with two good terminal sides, proved from alternating boundary endpoints, embedded train arcs, and triangle-freeness. Audit.125's five-ended pentagonal flower refutes the broader but different claim that a local face can meet at most two hull-ended trains; it does not contradict this global count.
- The square/additive-two train regression rules out finite claims that omit the two-double-ended-train correction. The promoted conclusion retains the asymptotic o(D) error and makes no finite zero-error assertion.
- The crossing graph uses all actual rhombi and all stopped trains, including singleton trains. No selected-stress graph, local-to-global optimality inference, source/scaffold identification, or simultaneous-motion inference occurs.
- C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND is not a duplicate: it assumes a concentric near-disk annulus of the loaded hull and gives a finite angular estimate. This theorem uses full-source midpoint localization and the canonical phase budget in either global branch.
- The promoted claim is an all-branch refinement. In the Type-II branch its qualitative scalar conclusion does not replace the stronger canonical `C-FULLCORE-HULL-DEPLETION-FLOOR`; it adds the train-incidence o(D^2) statement and the explicit R_4, P_F, and m_H tradeoffs.

## Dependencies, verifier, and disposition

Dependencies: `C-FS-GEOM`, `C-LINEAR-NONMATCH`, `C-LOADED-HULL`, `C-RHOMBUS-POP`, `C-PUNCTURED-PHASE`, `C-COHERENT-GRAINS`, `C-TRAIN-INTERFACE-CURRENCY`, `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, and `C-HARMONIC-COMPONENT-SQRT-COUNT`.

No finite verifier certifies the analytic support-normal window count or the asymptotic two-limit argument, and none is claimed. The exact finite identities and the decisive deductions above were independently reconstructed from canonical inputs. The finite pentagon and square cases are scope regressions, not counterexamples to the asymptotic statement.

The frontier remains unchanged: C-II and Level I are open. Section 10 and later in the frozen source report were not audited in this cycle.

### Audit.202 dependency provenance correction

The existing Audit.202 entry incorrectly attributed endpoint inclusion to `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE`. That theorem only supplies generic isolate perturbation and anchor avoidance. Endpoint inclusion instead follows from `C-RHOMBUS-POP`, which gives F=conv(B)=conv(V), together with the strict full-source support inequality above: each actual diameter endpoint in B is an exposed point of F, and therefore belongs to V. Contact isolates stay in the full-source geometry. This corrects the dependency in the Audit.202 state entry, audit artifact, and ledger; it does not change that theorem's scope or conclusion.

### Promotion transaction

The theorem-bearing PR #904 head `5da1235da540f749cbad482adcecfa125d332e06` merged as `41dabc2a89bf2f750cd70a60f2b644e01fcc3036`. Protected `state-consistency` run `37964218065` passed in 6m36s, including all 94 registered certificates and patch-whitespace validation.

Discovery-worker protection: this audit used only the frozen source commit. No discovery branch or worktree was modified.
