# Independent audit of PR #114 cut-stress model

**Classification:** unreviewed audit evidence. **Target C-II and Level I remain open.**

## Exact question and scope

This audit checks PR #114, head `cd33f4c76fd48722f06c03ddc86a05fd5e8f9e51`, at its published row data. Assignment: `audit-pr114-cut-stress-boundary-work-macbook-20261019`. Scope key: `355d30c9a0373f160287b299040e70c16963faff5c7b2269b5c8e323c8a2a3`.

Candidate question: under the submitted finite incidence supports, unit row vectors, positive diameter multipliers, edgewise A-packet balance, and full B-support of the internal packet, do the exact B-cut equations allow a nonexact B phase and equal, opposite internal and boundary work?

The controlled quantity is the two-cut shear direction
\[
\lambda_1Q_1+\lambda_2Q_2,
\qquad (\lambda_1,\lambda_2)=(1/5,-1/5),
\]
and its work split between the internal `(1,2)` packet and the A-boundary `(0,2)` rows. If this identity failed, the cut-equations-only boundary-payment example would fail. The falsification controls remove one boundary row, shorten one internal B support, and independently change a positive multiplier. The stopping condition is reached once the finite equations and these controls are exact: this task supplies no planar realization or global-minimizer bridge.

## Finding

The submitted arithmetic is correct for its stated abstract row model. Recomputing every cut from the row table gives A resultants `(23,0)`, `(309/13,0)`, `(18,0)` and B resultants
\[
Q_1=(-11/5,276/65),\qquad Q_2=(14/5,276/65).
\]
Thus `det(Q1,Q2)=-276/13`, so the B cut directions are nonparallel. The internal B load, derived directly from its two rows, is `P_int=(0,24/13)`. The chosen shear satisfies `lambda_1 Q_1 + lambda_2 Q_2=(-1,0)`. Under `J(x,y)=(-y,x)`, the internal packet work is `-48/13` and the boundary-row work is `+48/13`; the reference row contributes zero. The total first variation is zero.

The boundary payment is therefore a valid identity in this finite cut-incidence model. The checker does not establish that the model is an embedded source. It gives no point coordinates, hull order, assignment of row endpoints to shared source labels, individual contact rows or vertex equilibrium, complete all-pairs distance ledger, or global-minimality certificate. The aggregate vectors `Q_j` can be normalized to positive masses and directions, but that does not construct the omitted contact system. This result shows that the cut equations and listed row conditions alone do not force exact B phase or rule out boundary payment. It does not refute a source-geometric or global-minimizer statement.

## Source inventory and reading order

1. **Authority first:** `AGENTS.md`, `autoresearch.md`, `CONTRIBUTING.md`, `docs/STATE.md`, `docs/state/theorem-state.yaml`, `docs/problem/statement.md`, `docs/research/bottleneck-brief.md`, `docs/research/agent-procedure.md`, `docs/research/research-family-status.md`, `docs/research/run-reconciliation-2026-10-17.md`, `docs/REVIEW_POLICY.md`, and `docs/ci/README.md`. The matched status text keeps Level I/A/B/C-II open and C-I closed; the global quantifiers remain outside this finite audit.
2. **Route and exact objective:** `docs/targets/target-c/CURRENT.md`, `docs/research/priority-state.json`, `docs/research/tracks/target-c-exact-phase-packet-fork.md`, and `tasks/target-c-threshold-packet-cross-shore.md`. `rg` hits identify the boundary/layer correction, no uniform packet-resultant floor, limited two-cut family, and separate double-exact-phase branch. The task-card `existing_checks` list is empty; PR #114 itself includes a checker.
3. **Proof prerequisites:** `target_c_exact_phase_threshold_paired_staircase_2026-10-01.md`, `target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md`, `target_c_exact_phase_threshold_edgewise_kkt_balance_2026-10-02.md`, `target_c_exact_phase_threshold_edgewise_flux_packets_2026-10-02.md`, `target_c_exact_phase_threshold_cross_shore_packet_resultants_2026-10-02.md`, `target_c_exact_phase_threshold_strict_packet_resultants_2026-10-02.md`, `target_c_exact_phase_threshold_cross_shore_escape_2026-10-02.md`, and `target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md`. Their exact statements support the abstract incidence hypotheses, but leave source realization and endpoint closure open.
4. **Pinned audited source:** PR #114, head `cd33f4c76fd48722f06c03ddc86a05fd5e8f9e51`, branch `research/e99-pass-20261018-local-06`.

| Original source file | SHA-256 |
| --- | --- |
| `README.md` | `831a37b1ef9788af1bb8e78c750dd99408c763f40b5053c2c6b8e6c17fc7719d` |
| `SOURCES.json` | `54282bb14a6df7b38a41e84f2f01a259277c38d54e02509c2819fdb284b6f434` |
| `TASK.json` | `d7a04a72bf69baa3669e5521bdca95af03d0fd38729991ebf25ae9f786959ea3` |
| `VERIFY.json` | `e5599b03a9a257fe109f34e3313a6b8bad646a7254d055c74b5cf725e235a167` |
| `verify.py` | `fa9ad7dc2e00a7d0d006de101e23cab5ca9628a4e57b0586987fa75f08637d27` |

The exact pin file and PR head both match these hashes. There is no `candidate.json`; the source package marks itself `unreviewed` and records source realization as unresolved. Original source bytes are not copied or changed by this audit.
5. **Coordination and live delta:** the offline overlap cache matched PR #114 and the distinct PR #127 open-cell flux audit; all four cached and live comments in Discussion #83 are handoffs for other tasks. Live `gh` confirms PR #114 remains open at the pinned head and PR #127 is a separate candidate audit. The previous local handoff is the PR #114 producer result; the prior homelab handoff #127 audits a different candidate in this route.

**Independence exposure:** the required offline overlap output displayed part of PR #114's producer-body summary before the row-by-row reconstruction. The pinned source verifier also contains the claimed totals and a constant `P_int`. I treated both as claims, recomputed the sums and work from the row supports and vectors, and only then read the complete producer README and previous handoff. The independent verifier derives `P_int` from the rows rather than reusing the constant.

## Row model and support convention

An interval `(a,b]` crosses integer cut `k` exactly when `a < k <= b`. Every listed `beta` is positive. For a B-supported row, its oriented B vector is `b_sign * a_vec`.

| Row | A edge | `beta` | A vector | A support | B support | B sign |
| --- | --- | ---: | --- | --- | --- | ---: |
| `h0` | none | `1` | `(1,0)` | `(0,3]` | `(0,2]` | `+1` |
| `e02+` | `(0,2)` | `3` | `(3/5,4/5)` | `(0,2]` | `(1,2]` | `+1` |
| `e02-` | `(0,2)` | `4` | `(4/5,-3/5)` | `(0,2]` | `(0,1]` | `-1` |
| `e03+` | `(0,3)` | `8` | `(8/17,15/17)` | `(0,3]` | none | none |
| `e03-` | `(0,3)` | `15` | `(15/17,-8/17)` | `(0,3]` | none | none |
| `e12+` | `(1,2)` | `1` | `(5/13,12/13)` | `(1,2]` | `(0,2]` | `+1` |
| `e12-` | `(1,2)` | `1` | `(5/13,-12/13)` | `(1,2]` | `(0,2]` | `-1` |

The support tree is `T={(0,2),(0,3),(1,2)}`, a path on vertices `0,1,2,3` with edge lengths `1,2,3`; every edge crosses A cut 2. The row vectors have unit norm and are pairwise nonparallel. For each A edge, the stress-weighted transverse components cancel and the longitudinal resultants are positive:

| A edge | transverse sum | longitudinal resultant |
| --- | ---: | ---: |
| `(0,2)` | `3(4/5)+4(-3/5)=0` | `3(3/5)+4(4/5)=5` |
| `(0,3)` | `8(15/17)+15(-8/17)=0` | `8(8/17)+15(15/17)=17` |
| `(1,2)` | `12/13-12/13=0` | `5/13+5/13=10/13` |

## Reconstructed cut sums

For A cut 1, the row vectors sum to
\[
(1,0)+(9/5,12/5)+(16/5,-12/5)+(64/17,120/17)+(225/17,-120/17)=(23,0).
\]
For A cut 2, the same rows cross, together with `e12+` and `e12-`, whose weighted sum is `(10/13,0)`. Hence the result is `(23+10/13,0)=(309/13,0)`. For A cut 3, only `h0`, `e03+`, and `e03-` cross; their sum is `(1+(64+225)/17,0)=(18,0)`.

For B cut 1, the contributions are `h0=(1,0)`, `e02-=(-16/5,12/5)`, and the two internal rows, totaling `(0,24/13)`. Thus
\[
Q_1=(1,0)+(-16/5,12/5)+(0,24/13)=(-11/5,276/65).
\]
For B cut 2, the contributions are `h0=(1,0)`, `e02+=(9/5,12/5)`, and the same full-support internal load, giving `Q_2=(14/5,276/65)`.

The determinant and shear checks are
\[
\det(Q_1,Q_2)=-276/13\ne0,
\qquad
Q_1/5-Q_2/5=(-1,0).
\]

Let `R_1=(-16/5,12/5)` and `R_2=(9/5,12/5)` be the two B-boundary row resultants. Then
\[
R_1\cdot JQ_1=108/13,\qquad R_2\cdot JQ_2=-12/13.
\]
Their shear work is
\[
2\left((1/5)(108/13)+(-1/5)(-12/13)\right)=48/13.
\]
Both internal rows cross both B cuts. Since their combined shear vector is `(-1,0)`, its quarter turn is `(0,-1)`, so their work is
\[
2\left((5/13,12/13)+(-5/13,12/13)\right)\cdot(0,-1)=-48/13.
\]
The reference row `h0` crosses both B cuts and has equal work factors `h0 dot JQ_1=h0 dot JQ_2=-276/65`; its opposite shear coefficients cancel. The `e03` rows have no B support. The total is exactly zero.

## Adversarial controls

`verify.py` recomputes the row contributions instead of trusting the source checker's stored cut totals or internal-load constant.

1. **Remove `e02-`.** The `(0,2)` A-packet transverse sum becomes `12/5`, not zero. The B cut resultants become `Q_1'=(1,24/13)` and `Q_2'=(14/5,276/65)`, so the same shear coefficients give `(-9/25,-12/25)`, not `(-1,0)`.
2. **Weaken `e12-` B support from `(0,2]` to `(0,1]`.** The internal row is absent from B cut 2. Then `Q_1` is unchanged and `Q_2'=(207/65,216/65)`, giving shear vector `(-14/13,12/65)`, not `(-1,0)`.
3. **Independent positive-multiplier corruption:** change `beta(e02+)` from `3` to `4`. The `(0,2)` A-packet transverse sum becomes `4/5`; B cut 2 changes to `(17/5,328/65)`, and the shear vector becomes `(-28/25,-4/25)`. Positivity alone does not preserve the claimed boundary-payment ledger.

All three controls fail the submitted exact identity for distinct reasons: row inventory and packet balance, support incidence, and edgewise stress balance.

## Scope and next lemma

This is an exact finite audit of one abstract row system. It is not a new uniform result and does not test the other, double-exact-phase complete-grid branch. It neither moves points nor claims that every pair of source labels satisfies lower- and upper-distance constraints.

The next missing lemma is geometric: either exclude this support/sign/payment arrangement under the full threshold-source hypotheses, including contact endpoints and all source-pair constraints, or construct a source-realized configuration satisfying those hypotheses. Until then, the PR #114 conclusion is valid only at cut-incidence scope. The accepted theorem state and claim lifecycle do not change.

## Source and attribution

The audited row model and original checker are from PR #114, exact head `cd33f4c76fd48722f06c03ddc86a05fd5e8f9e51`; the original bytes remain unchanged. The independent reconstruction is first-party audit material, offered under Apache-2.0. OpenAI Codex GPT-6 Luna xhigh produced this audit and verifier. No human review or canonical promotion is claimed.

## Open next question

**Downstream decision:** whether the nonexact-B threshold branch can be closed using cut equations alone. **Affected quantity:** the aggregate boundary work `W_boundary` relative to `P_int` and the two-cut shear vector. **Changed hypothesis:** add the planar four-host source realization, vertex-level contact equilibrium, and complete source-pair constraints omitted by this model. If those hypotheses exclude the identity, the next proof can use a source-specific restriction; if they admit it, the cut equations need an additional global argument. First action: translate this exact support table into shared point-pair endpoints and solve the resulting all-pairs and vertex-equilibrium constraints. Blocker: the present audit has no such embedding or solver certificate.
