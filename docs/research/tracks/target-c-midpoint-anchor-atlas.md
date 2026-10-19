# Target C midpoint, anchor, and atlas track

**Status:** The results summarized here come from source PR #947 and remain
unreviewed in the destination. The source PR proposed several theorem-state
promotions; none was adopted. The destination theorem-state is authoritative.
Exact source commits, blobs, destination mappings, and treatments are in the
[PR file ledger](../migration/2026-10-16/ledger/source-pr-files.jsonl).

## Full-source midpoint localization

[Audit.246](../../audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md)
claims the following for a noncollinear global minimum-diameter unit-separated
source with (D\ge216). Choose one actual diameter partner independently for
each actual diameter endpoint, let (m_p) be its midpoint, and let (o) be a
circumcenter of the full-source hull. Uniformly over partner choices, the
number of midpoints at distance at least (s) obeys

\[
\#\{p:|m_p-o|\ge s\}\le C D^2/s^2
\quad(s\ge4\,3^{1/4}\sqrt D),
\]

with first and second absolute moments (O(D^{3/2})) and (O(D^2\log D)).
The proof scope retains all source points, including contact isolates. It
asserts no stress-weighted midpoint control, no count of almost-diameter
pairs, and no source motion.

For a canonical C-II source, the same report transfers the tail and moments to
the actual edges of the full diameter graph by injecting those edges into
distinct endpoints through the stated Woodall topology. This transfer adds no
pair multiplicity bound.

The same audit claims a separate localization for any source pair (p,x) with

\[
|p-x|\ge D-s,\qquad \nu=(p-x)/|p-x|,\qquad
\eta=3^{1/4}\sqrt D,\qquad m=(p+x)/2:
\]

\[
|(p-o)\cdot J\nu|,\ |(x-o)\cdot J\nu|
\le 13D^{2/3}+2sD^{1/3},\qquad
|(m-o)\cdot\nu|\le2\eta+s/2.
\]

Bounded-deficit pairs therefore have midpoint distance (O_s(D^{2/3})), but
the report explicitly leaves their number uncontrolled. The
[midpoint-tail second-referee note](../../audits/target_c_midpoint_mean_tail_second_referee_2026-10-10.md)
records the source proof clarification for its dyadic angular band width.

The destination [near-diameter localization audit](../../audits/target_c_near_diameter_pair_midpoint_destination_audit_2026-10-19.md)
independently reconstructs this near-pair component from `C-FS-GEOM` and
`C-FS-DIAMETER-MIDPOINT-D2-3`. It verifies the endpoint tangent and midpoint
normal bounds for all `s>=0`, uniformly on `0<=s<=2`, including both boundary
values. The audit is limited to this component; the destination candidate stays
unreviewed pending an explicit lifecycle transaction. It does not audit the
endpoint-tail/moment claims used separately by PR #113 or establish a pair
count, atlas, or source motion.

## Positive-leaf anchor strengthening

[Audit.247](../../audits/target_c_positive_leaf_anchor_sharpening_independent_audit_2026-10-10.md)
proposes strengthening the destination's canonical positive-leaf bound from
\(O(D^{-1/2})\) to \(O(D^{-2/3})\). The source hypotheses require a
noncollinear global minimum-diameter source, an actual diameter endpoint with
exactly one actual unit neighbor, positive coefficient for that contact in a
normalized full-source KKT stress, and retention of every source point in
\(K_D\), the intersection of source-centered disks of radius \(D-1\). The
proof uses the near-diameter localization above, the narrow cone of positive
KKT normals, and a full-source inner-ball contraction. It gives boundary
localization only: no vacancy, packet, source motion, or capacity payment.

The [positive-leaf second-referee note](../../audits/target_c_positive_leaf_anchor_second_referee_2026-10-10.md)
records a source reconstruction. It does not count as the destination's
required independent AI-agent audit of an exact destination commit.

## Supplied slow-chart coverage

[Audit.254](../../audits/target_c_slow_chart_contact_port_cover_independent_audit_2026-10-10.md)
claims that, on an unbounded canonical post-ZF triangle-free C-II sequence,
at most (O_{J,K}(D^{4/5})) loaded endpoints lie in the union of two specified
classes covered by a supplied family of at most (J) unit-rhombic charts with
fixed (K/D) displacement error:

1. Positive-stress contact leaves whose sole actual unit neighbor is in a
   supplied chart.
2. Actual diameter endpoints with two distinct actual unit neighbors in one
   supplied chart.

Since the source has at least (D) loaded endpoints under the stated
canonical hypotheses, at least (D-O_{J,K}(D^{4/5})) remain outside those
classes. The supplied atlas is an assumption. The report gives no extraction,
bound for all uncovered endpoint types, or finite competitor.

The corrected inverse-phase argument in
[Audit.236](../../audits/target_c_global_inverse_phase_face_tail_second_referee_2026-10-10.md)
claims only (q=o(D)) from its original global phase and face-tail premises.
The fixed-cutoff proof's additive tail term does not give a global
\(K'/D\)-Lipschitz chart or (q=O(D^{4/5})). Those historical inferences
remain withdrawn in [Audit.202](../../audits/target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md)
and in the [current frontier](../../targets/target-c/CURRENT.md). Audit.236
does not supply the atlas assumed by Audit.254.

## One-pin fixed-wall obstruction

[Audit.253](../../audits/target_c_one_pin_restoration_gap_capacity_plateau_independent_audit_2026-10-10.md)
records two separate finite statements. For each fixed (m,n\ge3), after
deleting (p_{1,0}) and fixing every other boundary pin, both weak and strict
capacity inside the open reference parallelogram are exactly
\((m-1)(n-1)\) for all angles in a frame-dependent interval immediately above
\(\pi/3\). The interval is not uniform as the frame grows and the result
counts no exterior sites.

The same report proves a displacement gap in the restored-pin model: if the
deleted boundary pin and all interior labels may move inside the old closed
wall while all other boundary labels stay fixed and all pair distances remain
at least one, then the maximum displacement is zero or at least
\(\sqrt3/(4(m+n+1))\). This blocks continuous local restoration in that
fixed-wall model; distant alternatives and changed walls remain open. The
existing Audit.187 verifier does not encode these universal analytic claims.

## Audit screens and next obligations

The exact duplicate
[fused-sign and residual-tail screen](../../audits/target_c_fused_sign_classes_and_residual_tail_screening_2026-10-10.md)
records that selected quarter-fold signs/charge and a PR #722 Type-II owner
bound are already subsumed by named canonical claims. Audit cycles 255 and 256
also record scoped canonical duplicate screens for shell-fold, finite
radial-stress, and Oler-separator statements. These screens leave source
extraction, a feasible finite move, and macroscopic-container closure open.
The source wording and its promotion history are retained under an explicit
warning in the
[referee-run ledger](../../audits/target_c_referee_run_ledger_2026-10-10.md)
and [integration audit ledger](../../audits/target_c_integration_audit_ledger_2026-10-06.md).

The next useful proof obligations are:

- Extract the midpoint and leaf hypotheses from every relevant canonical
  source while retaining all labels and full-source stress conditions.
- Either prove the bounded (K/D)-chart atlas from a source-wide argument or
  use the linearly many uncovered endpoints in a strict, full-source finite
  competitor.
- For one-pin routes, pay for the missing label through changed guards,
  outside capacity, or a nonlocal replacement that passes every lower and
  upper pair constraint.
- Keep the source's withdrawn global chart and (D^{4/5}) inference out of
  every downstream proof dependency.

Machine-readable claims, proposed source statuses, dependencies, current
destination statuses, source hashes, and exact next obligations are in the
[Target C candidate registry](../../targets/target-c/candidate-registry.json).


For the separate train-return and rigidity-forced attachment/grid linkage route, see the [source PR #950 track](target-c-train-returns-rigidity-grid.md); its two endpoint families may be disjoint and it supplies no finite competitor.
