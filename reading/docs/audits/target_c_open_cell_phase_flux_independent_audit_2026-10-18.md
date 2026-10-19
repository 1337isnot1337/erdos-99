> Generated reading edition · [exact source](../../../docs/audits/target_c_open_cell_phase_flux_independent_audit_2026-10-18.md) · source SHA-256 `ea3731cafd66ec6c53bcda70f3bc780c1ff277598ede3459d6ee0658ba16c4b8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A4A2978EC0A3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit: exact open-cell phase flux

**Review status:** independent proof reconstruction completed; the identity is
correct under its cut-balance hypotheses. The sign and endpoint corollaries are
conditional on inherited hypotheses that the reviewed note does not restate.
This audit does not promote a theorem or change the canonical state.

## Exact object audited

- Repository head: `7d0a450fe66991036541023f95c44c064a04b6a8`
- Theorem state: `2026-10-15.publication.2`
- Priority: `public-frontier.3`
- Catalogue: `public-frontier.9`
- Candidate: `TARGET-C-OPEN-CELL-PHASE-FLUX-20261016`
- Reviewed bytes: `research/target_c_open_cell_phase_flux_2026-10-03.md`
- SHA-256: `82bcf72417a4e622cc72a2b52f7d4ae30b169a8970343d2a8ed7a9713f21ad1a`
- Git blob: `82411a0aad446f1f59461b4d45e061a5e9f87404`

The candidate registry says `unreviewed`, and the assignment card's
`existing_checks` array is empty; its lifecycle records no destination audit.
The offline overlap result had no exact match.
Discussion #83's current comments concern other tasks. The only open PR at the
live check was #102, a Target A Hall-overlap result; it is unrelated and is not
repeated here.

Related review evidence is narrower or explicitly unreviewed. The October 2
[subset-reflection hostile audit](../reports/target_c_subset_reflection_independent_hostile_audit_2026-10-02.md)
reviewed PR #614 at its own exact source head and passed finite statements only
under its nonempty-cutset, narrow-span, and empty-cell conditions; it left the
source application conditional. The October 15
[finite staircase-preservation note](../reports/open_cell_staircase_finite_preservation_2026-10-15.md)
explicitly retains this analytic phase-flux note as unreviewed, and its finite
census does not audit the analytic identity. The October 3
[antitone-interval report](../reports/target_c_antitone_interval_scc_release_2026-10-03.md)
assumes the block-transposition theorem and remains a proof-only candidate.
None is a completed destination audit of this exact phase-flux artifact.

## Question, hypotheses, and affected quantity

**Question.** For two distinct train phases in one retained open-cell shore, does
the two-cut slab's weighted diameter-flow divergence equal
`(A_p+A_q) sin((theta_q-theta_p)/2)`, and do the claimed sign and interval-ideal
consequences follow?

**Hypotheses needed for the full claimed fork.** The identity needs the finite
cut-balance identity and coherent phase lifts. The old-diameter classification
also needs positive KKT weight on every moving actual diameter and the
non-grazing finite-change estimate. The inverse-`D` endpoint alternative
additionally needs the fixed-star complete O--O slab motion, the Section-90
phase-window bound `|u_q-u_p| <= 4K/D`, and the contact-minimal then
diameter-pair-minimal representative used by the endpoint argument. The pinned
note invokes these as existing prerequisites but does not list their complete
hypotheses or define `K` in its own setup. This positivity is not automatic
from generic KKT language: the canonical force-hull module starts with
nonnegative multipliers and distinguishes the actual diameter set `H` from
the positive-support union `H_*`. The predecessor's stronger positive
full-support hypothesis must therefore be carried explicitly.

The quantity controlled is the signed weighted divergence across the two-cut
slab. Under the full hypotheses it decides whether the transposition has
diameter rows of both signs or all moving old diameters shorten, in which case
an inactive pair must lie within `4K/D` of a distance boundary. This affects a
conditional C-II endpoint fork; it does not establish a source-wide endpoint.

**Falsification controls.** First, drop strict positivity of the multipliers.
With `t>0`, one outgoing crossing row of positive weight and an incoming row of
zero weight give `F_out>F_in=0`, while the zero-weight incoming old diameter
still has the opposite finite length-change sign. Thus the equivalence
`ONE-SIGN iff F_in=0` is false for the full geometric diameter graph without
the positive-support hypothesis. This is a signed-row control, not a claimed
geometric source counterexample. Second, take a phase gap `theta_q-theta_p`
equal to `pi/3`; then `|u_q-u_p|=1`, not `O(1/D)`. This shows why the Section-90
window is required for an inverse-`D` conclusion; it is not a source
realizability claim.

**Stop condition.** Stop if the cut identity, sign table, and conditional
endpoint argument reconstruct under the exact parent hypotheses, or if one
fails there. No search for a global endpoint is part of this audit.

## Independent reconstruction

Let `P_i={0,...,i-1}` be the prefix of gap vertices. For a cut `i`, the
prerequisite KKT identity is

```math
A_i u(\theta_i)=\sum_{a_h<i\le b_h}\beta_h r_h,
```

where `r_h` is oriented from its lower layer to its higher layer. Put
`v=J u(mu)`. Since the open cell contains no actual diameter direction, every
crossing row has `r_h dot v != 0`. Direct each row according to that sign and
give it flow `f_h=beta_h |r_h dot v|`. Taking the dot product of cut balance
with `v` gives

```math
\Phi(P_i;\mu):=F_{out}(P_i)-F_{in}(P_i)
=A_i\sin(\theta_i-\mu).
```

For `S=P_q` minus `P_p`, divergence is the difference of the two prefix
divergences:

```math
\Phi(S;\mu)=A_q\sin(\theta_q-\mu)-A_p\sin(\theta_p-\mu).
```

At `mu=(theta_p+theta_q)/2`, writing
`t=sin((theta_q-theta_p)/2)`, the right side is `(A_p+A_q)t`. Hence

```math
F_{out}(S)-F_{in}(S)=(A_p+A_q)t,
```

with no asymptotic term. Equivalently, the slab layer potential is `2t` on
`S` and zero outside. Its weighted work is
`2t(F_in-F_out)=-2(A_p+A_q)t^2`, matching the two-cut KKT work identity.
The sign is valid for either sign of `t`; only `t=0` is excluded.

For `t>0`, the net divergence is positive. Each incoming row contributes
`+2t f_h` to the work and each outgoing row contributes `-2t f_h`. If every
moving actual diameter has `beta_h>0`, then `F_in>0` is exactly the presence of
an incoming geometric row. Thus `F_in>0` gives both work signs, while
`F_in=0` gives only the shortening sign. For `t<0`, the roles reverse:
`F_out>0` gives both signs and `F_out=0` gives only shortening rows. The
predecessor block-transposition proof supplies the needed full-support
positivity and strict non-grazing bound for its moving actual diameters.

For a source ideal `S`, no geometric diameter edge enters. If `t>0`, the flux
identity then supplies outgoing shortening rows and no opposite-sign row. The
predecessor endpoint theorem makes that one-sign move impossible when its
inactive near-pair witness is excluded, so a source ideal must have
`theta_p >= theta_q`. The sink case is symmetric and gives
`theta_p <= theta_q`. For adjacent cuts, a strict ascent therefore forces an
incoming row at that gap and a strict descent an outgoing row; distinct heads
and tails yield at least `max(|U|,|Dn|) >= (|U|+|Dn|)/2` distinct rows.

The endpoint part uses more than the flux equation. The predecessor theorem
assumes a fixed-star complete O--O rectangle, exact contact preservation of
the slab move, a full-support positive KKT stress on moving old diameters,
the common open witness cell, and the Section-90 shore window. Its exact
non-grazing estimate and endpoint ledger imply that if all moving old
diameters shorten, a previously strict pair must satisfy
`1 < |xy| <= 1+s` or `D-s <= |xy| < D`, where
`s=|u_q-u_p| <= 4K/D`. The diameter-pair-minimal normalization rules out an
endpoint at the same diameter with fewer old diameter pairs. Under those
hypotheses, the inverse-`D` fork reconstructs. If the other endpoint
prerequisites hold but the shore-window bound is dropped, the endpoint
argument yields only the `s`-scale statement, not the inverse-`D` bound.

## Scope and disposition

The algebraic identity and the conditional sign argument reconstruct. I found
no contradiction to them under the predecessor's positive full-support and
non-grazing hypotheses. The note's stated setup and the candidate registry do
not explicitly bind the old-diameter classification to positive multipliers on
all moving actual diameter rows, or bind the inverse-`D` endpoint alternative
to the Section-90 window and diameter-pair-minimal normalization. Those
conditions are available in the earlier block-transposition result, so this is
a scope and dependency statement rather than a counterexample to that result.
The proof-only candidate should be read with those explicit inherited
hypotheses; its broad wording alone does not establish them.

Comparison with predecessors: the October 1
[block-transposition report](../reports/target_c_open_cell_block_transposition_2026-10-01.md)
supplies the finite contact-preserving motion, full-support sign argument,
non-grazing estimate, and endpoint ledger. The October 3
[cut-divergence note](../../research/target_c_open_cell_cut_divergence_condensation_2026-10-03.md)
gives the prefix formula from which this pairwise midpoint identity follows.
This audit reconstructs the exact pairwise identity and checks the extra
dependencies; it does not repeat their broader geometric claims.

The exact five-point one-sign regression in the
[subset-reflection gap report](../reports/target_c_subset_reflection_gap_obstruction_2026-10-02.md)
is consistent with the endpoint fork: it has positive diameter coefficients,
but no actual contacts, vertex KKT, or global/secondary minimality. The
thirteen-point [interleaved-SCC regression](../reports/target_c_interleaved_scc_actual_diameter_regression_2026-10-03.md)
also lacks actual contact cutsets, vertex KKT, and global minimality; it shows
that diameter geometry and narrow phases alone do not force interval terminal
SCCs. Neither is a counterexample under the full predecessor hypotheses.
The October 2 hostile subset-reflection audit also checks a distinct exact
actual-contact regression, but its audit target is PR #614's subset-reflection
packet, not this two-cut phase-flux identity; I reuse only its stated boundary
and scope, not its audit verdict.

The two prior exact regression checkers were independently replayed under the
shared single-process compute lock:

```text
flock -x /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock python research/verify_target_c_interleaved_scc_source_2026_10_03.py
PASS: all 78 source pairs; exactly 9 actual diameters; all disjoint chords cross;
common-star open cell; noninterval source/sink SCCs; all 6 positive cut resultants;
strict inactive-pair margins; exact divergence; homothetic phase bound; derivative rank 4.
REGRESSION ONLY: no actual unit contacts, vertex KKT stress, or global optimality.

flock -x /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock python research/verify_target_c_subset_reflections_2026_10_02.py
PASS: exact-rational regression packet; m=2..8 exhaustive subsets plus m=12,16 controls;
five-point contrast has one strictly shortened and three unchanged actual diameters,
zero inactive blockers; no source KKT or global optimality.
```

These checks corroborate the stated regression boundaries; neither is a verifier
for the analytic phase-flux identity. No state, priority, manifest, or candidate
lifecycle entry was changed. **C-I remains closed; C-II, A, B, and Level I
remain open.** The remaining global question is to charge the
interleaved/noninterval SCC branch against the full opposite shore/four-host
geometry or produce a same-cardinality source-wide endpoint retaining every
label and every lower/upper pair constraint.

**AI role:** OpenAI Codex, GPT-6 Luna xhigh, independently reconstructed the
proof and adversarially checked the scope for this audit. No human mathematical
review is claimed. The contribution is offered under Apache-2.0; it quotes no
external publication.
