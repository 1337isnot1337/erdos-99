<!-- theorem-state: {"artifact_id":"ART-8A846FDD3455","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Centered-fan blocker source reconciliation

**Source:** `research/target-c-fan-blocker-closure-20261005` at
`ba8197f5c4ade5dbb55f3c5f138597e47a30191a`.
**Source blob:** `683e523a8aad8da73c04f75791521ccc566f1504`;
SHA-256 `b4d3106a7ae373d05e48e10cbe02f2228f70fbbd2559e1e6c3d09c46b8288d31`.
**Comparison main:** `eebbc6b691b96689f937b295eae1851a0089c009`.
**Authority:** `2026-10-10.audit.234`; Level I/C-II remain open.
**Classification:** preservation and AI source audit; no canonical change.

## Full history and canonical successor

The complete 713-line source and all five unique commits were reviewed.
The initial isolate-only closure proof is strengthened in the final commit to
include shrinking old contacts in the arrow relation. An intermediate correction
proves that translated cap points remain in the carrier disk before using its
cap diameter. The first face-localization addition wrongly assumes all fan
contacts are hull sides and bounds every path edge; the next commit separates
bridge-adjacent fan leaves. Its remaining whole-path overstatement survives at
the tip and needs the prefix correction below. No code or other source path is
introduced by these five commits. Exact patches remain in private recovery.

[Canonical Audit 152](target_c_centered_fan_blocker_closure_independent_audit_2026-10-08.md)
freezes this exact tip, blob and hash. Its independently reconstructed theorem
`C-CENTERED-FAN-BLOCKER-DEPTH-PATH` covers the complete valid Sections 1–6:
full-source closure to depth `D/10`, at least `D/11` arrows, edge lengths in
`[1,1+1/D]`, strictly increasing depth, the first strict blocker's depth bound,
and the bounded total gap excess. It explicitly withholds source Section 7.
The source text was missing from main despite that exact provenance reference;
it is now [restored at its original path](../../research/target_c_centered_fan_blocker_closure_2026-10-05.md),
with current scope and historical corrections stated visibly.

## Proof reconstruction

The two fan-neighbor separation inequalities and the old/new blocker distances
give `|v| <= (1+s delta-delta^2)/(2 tau)`. Substitution into the strict old
distance yields the stated quadratic and its positive root. The displayed
lower bound follows because `delta^2(1-delta^2)(5-delta^2)>=0`.

For an arrow, the strict/weak conventions differ correctly between old unit
contacts and old noncontacts: an old contact is absorbed only if it shrinks
below one, while a new contact from a strict pair must also be absorbed.
The squared-distance identity gives a depth increase greater than `delta/2`.
The graph is acyclic, and summing gives the accumulated gap bound. The source's
version drops a nonnegative initial depth, so is valid also for a path whose
initial vertex has positive depth.

For a shallow moved-to-fixed pair whose distance increases, both endpoints lie
in the support cap of height `D/10+1/D`, and the translated point is still in
the actual radius-D carrier disk. The cap bound is
`D^2(8q-3q^2) <= (8437/10000)D^2 < D^2` for `q<=11/100`.
Unchanged and nonincreasing pairs retain their bounds. An arrow-closed shallow
set therefore gives a same-cardinality unit-separated endpoint with no new
contacts or diameters, while `pa` strictly shortens. The global/contact/diameter
lexicographic minimality fork is valid even when some old contacts open.
The parent path to the first depth crossing gives `m>=D/11` and the total gap
bound. All contact isolates remain source labels. No disjointness between paths
for different fan leaves follows.

## Face extension: repaired prefix, conditional payments

Audit 152 correctly observes that reaching a nonisolated boundary vertex permits
later arrows to leave through that shared vertex without crossing a contact edge.
The restored Lemma 7.1 therefore speaks only about the initial path segment up to
the first nonisolated vertex or the first depth crossing. Its crosscut alternative
likewise uses that segment, rather than the entire path of Theorem 5.1.
This is the exact limitation established by the planar argument.

The cited `target_c_degree2_fan_exceptional_face_payment_2026-10-02.md` is an
unpromoted dependency, absent from the current main tree. No proof or status for
it is manufactured here. The face identification, bridge count, face-excess
accounting and proposed return-currency application remain conditional, as
Audit 152 requires. The original unconditional upgrade is not accepted by this
preservation. The geometric prefix argument is retained under an explicitly
supplied bounded face with the required interior sector; deriving that face and
its population payments remains separate. The updated handoff is subject to
those same assumptions. It supplies no new triangle conclusion or competitor.

## Validation and disposition

The existing registered centered-fan reflection checker was rerun as a finite
geometry control. It does not certify the new global path theorem, whose complete
analytic proof is already canonical in Audit 152. No new certificate is registered.
Artifact regeneration, state/transaction, prelaunch links and whitespace checks
accompany this preservation. Current theorem state, routes, theory, prompts and
problem definitions remain unchanged.

This accounts for every valid source claim, the withdrawn scope upgrades, and the
unique conditional tail without deleting its history. Ref cleanup still requires
landed preservation, an exact recoverable identity and fresh open-PR/worktree/
activity guards. Private receipts record whether deletion actually executes.
Prepared with Codex (GPT-6); this AI source audit is not independent human review.
