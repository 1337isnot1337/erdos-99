<!-- theorem-state: {"artifact_id":"ART-B12EF8503121","canonical":true,"claim_ids":["C-SEPARATED-PACKET-RELEASE-OBSTRUCTION"],"claim_statuses":{"C-SEPARATED-PACKET-RELEASE-OBSTRUCTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.112 — separated packet contact release

**Date:** 2026-10-07
**Audit base:** `468d06ae695ea012de73a5a8919e034c424ecd9e`, tree `c2d77ee2a78bcaaf1412dbc0d767ce5eaba46b4d`
**Starting state:** `2026-10-07.audit.111`; C-I closed, C-II open, Level I open
**Source branch:** `research/sol/target-c-exterior-cap-closure-20261006`
**Frozen source commit:** `f4a362727779f6afc0f01738015112c04fdb73d5`
**Source artifact:** `docs/reports/target_c_exterior_packet_release_and_unloaded_core_cut_2026-10-06.md`, SHA-256 `6b8722e95d92cfc1c32f7bcc6d4ba5cd71f6138df657d73ce5be982d8299fa08`
**Verdict:** PASS — promote the separated packet obstruction below.
**Classification:** proved candidate, independently audited; the exact claim below is canonicalized by this audit. No computational certificate is claimed.

## Exact statement audited

Let `A` be a triangle-free, unit-separated `n`-point global minimizer of diameter `D=D(n)>1`, chosen with the fewest unit-distance pairs among all triangle-free global minimizers of cardinality `n`. Let `R` be a subset of `A`, let `T` be `A` with `R` deleted, and let `Y` be a finite set of `|R|` distinct points, disjoint from `T`, such that `T union Y` is unit-separated. Assume every pair in `T union Y` involving `Y` has distance strictly less than `D`.

Partition `Y` into nonempty sets `Y_1,...,Y_r`. For each `i`, assume there are a unit vector `u_i` and a real number `c_i` such that

`u_i dot a <= c_i < u_i dot y` for every `a in T` and `y in Y_i`.

Also assume every pair from distinct packets `Y_i,Y_j` has distance strictly greater than one.

Then no such replacement exists if either:

1. `R` is incident to at least one unit-distance pair of `A`; or
2. `R` meets every actual diameter pair of `A`.

The second alternative follows from diameter minimality alone. The first uses only contact-minimality among triangle-free global minimizers; it needs no secondary minimum on the number of diameter pairs.

## Independent reconstruction

For each packet `Y_i`, translate its points to `y+epsilon*u_i`. For every retained `a in T`, strict separation gives `u_i dot (y-a)>0`, so

`|y+epsilon*u_i-a|^2 - |y-a|^2 = 2*epsilon*u_i dot (y-a) + epsilon^2 > 0`.

Thus all packet-to-retained distances, initially at least one, become strictly greater than one. Distances within one packet are unchanged. Distances between distinct packets begin strictly greater than one. Since there are finitely many pairs and every pair involving `Y` begins strictly below `D`, choose one positive `epsilon` small enough to preserve every cross-packet lower bound and every involving upper bound.

Now dilate each translated `Y_i` by a factor `1+eta` about any fixed center for that packet. Every within-packet distance is multiplied by `1+eta`, so all within-packet unit contacts open. All already strict cross-packet and packet-to-retained lower bounds, and all strict upper bounds, persist for a sufficiently small common positive `eta`, again by finiteness. Call the resulting packet `Y'`. Every pair involving `Y'` is now strictly between one and `D`.

The source `T union Y'` has cardinality `n`, is unit-separated, and has no new unit contacts. It is triangle-free because its remaining unit-contact graph is the induced old graph on `T`. If its diameter is below `D`, global optimality is contradicted. If `R` removes an old contact and the diameter remains `D`, it is a triangle-free global minimizer with fewer contacts. If `R` meets every old diameter pair, no pair within `T` has distance `D`, and every pair involving `Y'` is strictly below `D`; therefore the new diameter is strictly below `D`.

This is a finite endpoint argument. It does not infer a usable move from first-order data, and it does not require the initial packet to be triangle-free.

## Hostile scope checks

- Internal unit contacts, including those in a packet containing an equilateral triangle, are opened by dilation after the packet-to-retained distances have been made strict.
- Contacts between separate packets are not opened by the dilation argument; the theorem explicitly requires their initial distances to be greater than one.
- Strict upper slack is required for every pair involving the packet. If a new pair may lie at `D`, the finite perturbation need not preserve the diameter bound.
- The complete retained source `T`, including any contact-isolated labels, stays fixed and remains in the pair checks. No source labels are dropped from the bookkeeping.
- If `R` removes a contact but not all diameter pairs, the contact-minimality branch handles the case where the diameter stays `D`. If `R` covers every diameter pair, the diameter strictly drops regardless of contact loss.
- The final replacement is triangle-free even though the initial `T union Y` need not be: every new pair is opened above one.

## Dependencies and relation to existing theorems

The proof has no nontrivial theorem dependencies. It uses the definition of the global minimum `D(n)`, the stated contact-minimal choice, and the finite strict-margin argument. It does not assume `C=C_*`, `H=H_*`, positive-contact-core geometry, a loaded hull, an actual cap, stress, or an interior/exterior placement of `Y`.

This is complementary to canonical `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`: the latter allows arbitrary new-contact counts but assumes the stronger contact-then-diameter-pair normalization and explicit contact-budget inequalities. Here the separators open all new contacts, so the deletion of an old contact contradicts contact-minimality without the secondary diameter-pair choice. It is also distinct from `C-EXTERIOR-STATIC-PACKET-BARRIER`, which covers packets outside the loaded core hull under the stronger canonical stress normalization and permits a broader class of contact-release mechanisms.

## Disposition and frontier effect

Promote as `C-SEPARATED-PACKET-RELEASE-OBSTRUCTION`. The result excludes only finite replacements satisfying the stated packet partition, strict separator, cross-packet, and upper-distance hypotheses. It constructs no packet, proves no cap population bound, and supplies no equal-cardinality competitor from canonical source data. It therefore does not reduce the live full-source packet-existence obligation; C-II and Level I remain open.

No discovery-worker source branch or worktree was modified; this is an independent audit artifact.
