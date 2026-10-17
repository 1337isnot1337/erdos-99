> Generated reading edition · [exact source](../../../docs/audits/target_c_unloaded_sink_outer_occurrence_independent_audit_2026-10-09.md) · source SHA-256 `ae67647438244849e18d741a288327686932a8ea54e5d17fdb0df3c4b6f9a800`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A29630046B60","canonical":true,"claim_ids":["C-BINARY-SINK-OUTER-EXCESS-TRADEOFF","C-BINARY-SINK-UNLOADED-WITNESS-OUTER-CAP"],"claim_statuses":{"C-BINARY-SINK-OUTER-EXCESS-TRADEOFF":"canonical","C-BINARY-SINK-UNLOADED-WITNESS-OUTER-CAP":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: unloaded sink witnesses and outer-walk excess

**Date:** 2026-10-09
**Audit base:** `origin/main=43d220b80a76d80585bc34dc292910a97b220c5b`, state `2026-10-09.audit.178`.
**Target:** C-II. C-I is closed; C-II and Level I remain open.
**Frozen source branch:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`.
**Source artifact:** `research/target_c_unloaded_sink_outer_occurrence_payment_2026-10-05.md`, SHA-256 `917f0764ddbc79f62971a3d9c72af4ea77a23a09833ff977fd2285a8376a202e`.
**Run type:** independent audit and promotion. No discovery branch was modified.

## Exact statement and scope

Use the finite canonical O--O owner system of `C-OO-LOWER-BLOCKER-LOCALIZATION`, after its compatible bounded-face isolate reassignment. The positive contact core is connected, every old unit contact is preserved under each binary owner state, the owner translations are nonzero and pairwise acute, and their cloud has diameter

$$
s<\gamma_D:=D-\sqrt{D^2-1}.
$$

Let `B` be the actual loaded diameter-endpoint set, `q=|B|`, and `b` the occurrence-counted outer contact-face boundary-walk length. Let `Z_out` be the number of contact-isolated source points in that outer contact face. All source points, including contact isolates, remain in the source and in the owner system. The lower formula is the post-dispatch intergroup binary formula; unary strict-rhombus blockers are kept separate.

For pairwise disjoint internally incompatible binary sink SCCs `S_a`, choose the Audit.184 covering packet of `|S_a|+1` distinct physical lower-witness pairs. Let `u(S_a)` count packet pairs with at least one endpoint outside `B`, and let `R(S_a)` be the sum of cyclic loaded-hull owner-run counts. Then:

1. For `D>=6`,
   $$
   \sum_a u(S_a)\le 6(b-q+Z_{out}).
   $$
2. For `D>=7`, the canonical Audit.184 payment also gives
   $$
   t\le 6(b-q+Z_{out})+\sum_a(R(S_a)-|S_a|),
   $$
   where `t` is the number of counted sinks. In particular, the number of these sinks with `R(S_a)=|S_a|` is at most `6(b-q+Z_out)`.

These are finite conditional owner-system bounds. They do not establish satisfiability, nonzero-move feasibility, an upper-diameter test, or an asymptotic bound on `b-q+Z_out`.

## Independent proof

### Near-unit witnesses have at most six neighbors at any source point

An old lower-witness pair is a noncontact pair that violates the lower bound in some binary state. Its relative displacement changes by less than `s`, so its old length `ell` satisfies

$$
1<\ell<1+s<1+\gamma_D.
$$

Since `\gamma_D=1/(D+\sqrt{D^2-1})<1/(2D-1)`, for `D>=6` we have `ell<12/11`. Also

$$
\frac{1}{2\sin(\pi/7)}>\frac{49}{44}>\frac{12}{11},
$$

using `sin(\pi/7)<\pi/7<22/49`. Thus all such witnesses belong to the canonical near-unit graph `N_\tau` with `\tau=1+s<1/(2 sin(pi/7))`.

The canonical `C-NEAR-UNIT-CONFLICT-GEOMETRY` result gives degree at most six in this range. Its angular argument is exact: for neighbor radii `a,b in [1,\tau]`, unit separation implies

$$
\cos\theta\le \frac{a^2+b^2-1}{2ab}.
$$

When `\tau^2<2`, the right side increases in both radii on `[1,\tau]`, so it is at most `(2\tau^2-1)/(2\tau^2)`. Hence

$$
\theta\ge 2\arcsin(1/(2\tau))>2\pi/7.
$$

Seven distinct neighbor directions cannot fit around a point with every cyclic angular gap greater than `2pi/7`. The report's strict cutoff is necessary: at `\tau=1/(2 sin(pi/7))`, a regular unit-edge heptagon with its center has seven neighbors at distance `\tau` from the center and unit pairwise separation around the ring.

### Outer-face endpoint capacity is `b-q+Z_out`

Write `U_out` for the distinct unloaded, nonisolated source vertices incident with the outer contact face. The canonical loaded-hull occurrence theorem supplies one distinguished outer-walk occurrence for each of the `q` loaded vertices. Select also one occurrence for each vertex in `U_out`. These are distinct positions in the length-`b` outer walk because their source labels are distinct and `U_out` is disjoint from `B`. Therefore

$$
|U_{out}|+q\le b,
\qquad |U_{out}|\le b-q.
$$

This count allows bridge and articulation repetitions: those add walk positions. Outer-face contact isolates are not boundary-walk vertices and are counted separately by `Z_out`.

By canonical `C-OO-LOWER-BLOCKER-LOCALIZATION`, every intergroup full-source lower clause in the post-dispatch system lies in the outer contact face, except unary strict-rhombus diagonals. Each packet witness is a binary intergroup clause, so any unloaded endpoint is either in `U_out` or is one of the `Z_out` outer-face contact isolates. The bounded-face isolate reassignment is needed here; it is a stated part of that canonical reduction and preserves every source label.

Assign each distinct selected witness pair with an unloaded endpoint to one such endpoint. A source endpoint is incident with at most six witness pairs by the near-unit degree bound. Audit.184's `C-ACUTE-BINARY-SINK-WITNESS-DEBT` ensures that packet witnesses are distinct physical pairs, both within and across the disjoint sink SCCs. Thus

$$
\sum_a u(S_a)\le 6(|U_{out}|+Z_{out})\le 6(b-q+Z_{out}),
$$

proving item 1. The factor six is a vertex-degree charge, not an assumption that different witnesses have different unloaded endpoints.

For `D>=7`, sum Audit.184's exact sink payment

$$
u(S_a)+R(S_a)-|S_a|\ge1
$$

over the `t` sink components and substitute item 1. This gives item 2. If `R(S_a)=|S_a|`, the same payment forces `u(S_a)>=1`; distinct selected packets then give the stated cap on single-run sinks.

## Hostile scope checks

- The strict `D>=6` and cloud-size hypotheses ensure all lower witnesses lie below the degree-six threshold. At equality, the center of the unit-edge regular heptagon has degree seven in the near-unit graph.
- The cap applies to the reduced post-dispatch binary formula. Unary rhombus clauses are not counted as sink witnesses; sinks without an internal binary incompatibility are outside the statement.
- `Z_out` is essential in the endpoint budget: contact isolates are retained but do not contribute ordinary outer-walk edge occurrences.
- The proof uses the actual loaded endpoints `B`, the actual contact-face walk, and physical source pairs. It does not replace source geometry by an owner scaffold.
- The result only controls the unloaded-witness term. The repeated-run term can still be linear; no asymptotic claim follows unless a separate theorem bounds `b-q+Z_out` and the run excess.
- No verifier is supplied or needed for this analytic finite count. No computation is treated as evidence for the geometry or for an infinite-family conclusion.

## Canonical dependencies and frontier effect

| ID | Exact result | Dependencies |
|---|---|---|
| `C-BINARY-SINK-UNLOADED-WITNESS-OUTER-CAP` | `sum_a u(S_a)<=6(b-q+Z_out)` for distinct internally incompatible binary sink packets in the post-dispatch acute O--O owner system, `D>=6`. | `C-NEAR-UNIT-CONFLICT-GEOMETRY`; `C-OO-LOWER-BLOCKER-LOCALIZATION`; `C-LOADED-HULL`; `C-ACUTE-BINARY-SINK-WITNESS-DEBT`. |
| `C-BINARY-SINK-OUTER-EXCESS-TRADEOFF` | For `D>=7`, `t<=6(b-q+Z_out)+sum_a(R(S_a)-|S_a|)`; single-run sinks are at most `6(b-q+Z_out)`. | `C-BINARY-SINK-UNLOADED-WITNESS-OUTER-CAP`; `C-BINARY-SINK-OWNER-RUN-TRADEOFF`. |

The source claim survives in the exact post-dispatch, acute, small-cloud scope. It does not establish that `b-q+Z_out=o(D)`, does not pay repeated loaded-owner runs, and does not create a finite move. Target C's source-realized face-coupled finite-move endpoint and C-II/Level I statuses are unchanged.

**Verdict:** PASS — promote both exact bounds at the scopes above. The strict degree-six threshold is supplied by the canonical near-unit conflict theorem and checked independently here; Audit.184 supplies the distinct sink packets and the run payment.
