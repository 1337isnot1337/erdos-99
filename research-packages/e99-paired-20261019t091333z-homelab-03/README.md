# Support-aware two-cut flux and escape fork

**Classification:** unreviewed conditional proof note with exact finite algebra controls. It changes no accepted claim. Target C-II and Level I remain open.

- Base: 7d0a450fe66991036541023f95c44c064a04b6a8
- Theorem state: 2026-10-15.publication.2
- Priority: public-frontier.3
- Catalogue: public-frontier.9
- Assigned investigation: c-zero-weight-stress-cut-paired-20261019
- Scope key: 1baaf151547e115f3aecc2b1
- Contributor/originating AI: OpenAI Codex, GPT-6 Luna xhigh. AI assistance produced the proof note and checker; no human mathematical review is claimed.
- License: offered under Apache-2.0. This note reproduces no third-party text.

## Question and result

The open-cell phase-flux identity is exact for nonnegative KKT multipliers, but its original full-graph sign classification assumes every moving actual diameter has positive multiplier. Can a zero multiplier on a moving actual diameter be handled without changing the source or dropping that pair?

A support-aware fork is available, but nonnegative stress alone does not imply a full-graph sign. Work with a triangle-free C-II representative at fixed cardinality, chosen contact-minimal and then diameter-pair-minimal, and retain H as its complete actual diameter graph. Let K be the nonempty set of normalized nonnegative KKT stresses,
\[
K=\{(\alpha,\beta)\geq0:\ R_C^{T}\alpha-R_H^{T}\beta=0,\quad
\sum_{h\in H}\beta_h=1\}.
\]
Define the stress-reachable support
\[
H_{\rm supp}=\{h\in H:\text{some }(\alpha,\beta)\in K\text{ has }\beta_h>0\}.
\]
Assume K contains a stress with both boundary cut masses A_p,A_q positive. There is then one stress in K that retains both positive cut masses and is positive on every edge of H_supp simultaneously: include the positive-boundary stress and, for each of the finitely many h in H_supp, a witnessing stress with beta_h > 0, then average this finite list. Nonnegativity preserves the two boundary masses and makes every edge outside H_supp zero in every feasible stress. This removes accidental zeros in a particular stress while retaining the structural zero set.

Also fix the source block-transposition hypotheses: a fixed-star complete O--O rectangle, two distinct train phases in a common open diameter-direction cell, a feasible normalized KKT stress with positive boundary contact masses A_p,A_q, the exact contact-preserving slab translation Δ = u_q-u_p = -s w, and the non-grazing bound |n_h·w| > Ds/2 for every moving actual diameter h. Here n_h is oriented from the fixed exterior into the translated slab. The source labels are all retained.

For the stress chosen above, restrict the exact phase-flux identity to the crossing edges in H_supp. Write t = sin((theta_q-theta_p)/2), and let F_out+ and F_in+ be the positive stress flows leaving and entering the slab. Then
\[
F_{\rm out}^{+}-F_{\rm in}^{+}=(A_p+A_q)t.
\]
The same positive-support sign table follows:

| Phase sign | Positive-support condition | Consequence on positive-support moving rows |
| --- | --- | --- |
| t > 0 | F_in+ > 0 | Both signs occur: an incoming lengthening row and an outgoing shortening row |
| t > 0 | F_in+ = 0 | Every such row is outgoing and strictly shortens |
| t < 0 | F_out+ > 0 | Both signs occur |
| t < 0 | F_out+ = 0 | Every such row is incoming and strictly shortens |

The zero-support moving rows are not in this flux equation. In either one-sign support case, inspect them in the full actual diameter graph:

- If at least one zero-support row has the opposite, lengthening sign, the full geometric graph has both signs. The stress identity does not turn this into a feasible escape.
- If every zero-support moving row has the shortening sign, then every moving actual diameter strictly shortens. This includes the case where some zero-support rows are present; full positive stress on the moving set is unnecessary.
- There is no third sign case under the non-grazing hypothesis.

This is the support-aware replacement for the unqualified full-graph equivalence. It preserves every active upper row in the sign ledger. It does not infer the sign of any structurally zero row from KKT.

## Conditional endpoint arm and pair ledger

Assume every moving actual diameter shortens. The exact finite motion changes each moving old diameter by
\[
|r_h+\Delta|^2-D^2=-2s(n_h\cdot w)+s^2<0
\]
for a shortening row, using |n_h·w| > Ds/2 and D>1. At least one positive-support moving row shortens because the flux is nonzero. Nonswitching actual diameter pairs are unchanged, and the two boundary contact families and all other old contacts are preserved exactly by the slab motion.

Now check every source pair, including contact-isolated labels. If no previously strict pair reaches either constraint, the endpoint remains unit-separated with the same contact graph, so it remains triangle-free. It either has diameter below D or has diameter D with strictly fewer actual diameter pairs. Both contradict the contact-minimal, then diameter-pair-minimal representative. Therefore some previously strict source pair xy reaches or crosses a boundary during the full displacement:
\[
1<|xy|\leq 1+s
\quad\text{or}\quad
D-s\leq |xy|<D.
\]
With the Section-90 shore window s <= 4K/D, this is the inverse-D inactive-pair fork. This is a near-activity witness, not a claim that the full displacement is infeasible or an admissible C-II endpoint. A lower-bound hit may add a contact (and may create a unit triangle); an upper-bound hit may replace an old diameter pair. Either outcome still requires the full triangle-free and lexicographic endpoint check. Every old lower pair and every actual or inactive upper pair remains in the check; no label is deleted or restored.

The exact quantity affected downstream is the actual diameter-pair count |H| at diameter D. A same-cardinality, contact-preserving endpoint with fewer actual diameter pairs is forbidden for the canonical representative. The result does not produce such an endpoint: it says either a zero-support row prevents the all-shortening arm, or a previously strict pair is forced into the displayed near-boundary range.

## Proof reconstruction and finite checks

The support-selection claim follows by a finite average. Start with a feasible normalized KKT stress whose two boundary cut masses are positive. For each h in H_supp, append one feasible normalized stress with beta_h > 0, then average the finite list. Feasibility and normalization are convex; both cut masses stay positive, and the average is positive at every h in H_supp. For h outside H_supp, the definition makes beta_h zero in every feasible stress.

For the flux table, the exact two-cut identity has nonzero right-hand side with the sign of t. If t > 0, F_out+ > F_in+. Thus F_in+ > 0 gives both a positive incoming flow and positive outgoing flow; F_in+ = 0 leaves only outgoing positive-support edges. The t < 0 case is symmetric. The predecessor non-grazing estimate converts those row signs into strict finite length-change signs. No sign estimate is obtained for H minus H_supp; the explicit zero-support check is required.

The exact rational checker verifies finite support averaging, both orientations of the sign table, a structural-zero adverse-row control, and the finite squared-distance sign formula. Its test vectors are abstract stress/row data, not a planar source realization. It certifies no vertex-level contact equilibrium, hull order, global optimality, or complete Euclidean pair ledger.

Run from the repository root:

    flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research-packages/e99-paired-20261019t091333z-homelab-03/verify.py

The pinned PR #127 artifact docs/audits/target_c_open_cell_phase_flux_independent_audit_2026-10-18.md at https://github.com/1337isnot1337/erdos-99/pull/127 is at head 6c2b6d7be91c6d6cd5b9e2133c8add94c506bf1f and SHA-256 ea3731cafd66ec6c53bcda70f3bc780c1ff277598ede3459d6ee0658ba16c4b8. I read that audit before writing this successor; the derivation above was reconstructed from the base phase-flux note and block-transposition proof, and this is not a second audit of PR #127. PR #114 research-packages/e99-pass-20261018-local-06/README.md (head cd33f4c76fd48722f06c03ddc86a05fd5e8f9e51, SHA-256 831a37b1ef9788af1bb8e78c750dd99408c763f40b5053c2c6b8e6c17fc7719d) and its PR #136 audit research-packages/e99-macbook-20261019T054318Z-10/README.md (head 7cf4b8517c0f846058a9befda03bf3aa4343e688, SHA-256 91b86e43039b23bbcd84978931c418e820f50e98d859febc9c44d15214b2e174) concern abstract cut-incidence models without a source realization; neither is reused as one.

## Limits and next question

This proof-only extension does not extract a source stress, show that H_supp contains every moving diameter, or force the zero-support rows to shorten. It proves no asymptotic statement and no universal claim over sufficiently large cardinalities or every global minimizer. The canonical state remains C-I closed, C-II open, and Level I open.

**Open next question.** Downstream decision: whether the open-cell one-sign arm can yield the C-II diameter-pair contradiction. Exact affected quantity: |H| after the two-cut displacement. Changed hypothesis: replace full positive multiplier support by the support-completed stress plus a source-derived sign theorem for every edge in H minus H_supp. If such a theorem makes all zero-support moving rows shorten, the pair-minimal endpoint arm applies; if one can realize an adverse zero-support row under the full canonical hypotheses, the full-graph one-sign inference is false. First action: on a canonical full-source candidate, enumerate every feasible KKT support face and every moving actual diameter, then evaluate n_h·w and all lower/upper pair constraints. Stop if the face computation cannot be tied to source-realized phases and a complete pair ledger; report that missing geometric lemma rather than screening more cut-only fixtures.

## Predecessor credit

The exact phase-flux identity and its conditional sign argument are from the unreviewed phase-flux candidate at base SHA 7d0a450fe66991036541023f95c44c064a04b6a8; its original note SHA-256 is 82bcf72417a4e622cc72a2b52f7d4ae30b169a8970343d2a8ed7a9713f21ad1a. The full-support finite transposition and inactive-pair endpoint ledger are from docs/reports/target_c_open_cell_block_transposition_2026-10-01.md at the same base. This contribution adds only the simultaneous stress-support selection and zero-support trichotomy.
