<!-- theorem-state: {"artifact_id":"ART-69C775B68E70","canonical":false,"claim_ids":["C-TERMINAL-LONG-POCKET-ANCHOR-REGRESSION"],"claim_statuses":{"C-TERMINAL-LONG-POCKET-ANCHOR-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit — three-edge pocket anchor regression

**Date:** 2026-10-08
**Audit base:** `a55064e5c2a96eea4aeb1e480072e0d468eee76a`, state `2026-10-08.audit.127`
**Target:** C-II; C-II and Level I remain open.
**Frozen source:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2` (PR #737).
**Source files:** `docs/reports/target_c_terminal_oo_depletion_and_short_pocket_clauses_2026-10-06.md` (SHA-256 `5c560eafe95149b7e0694fa0f54e595cef2d4ee5be92e019a0621a949034b0ee`) and `research/verify_target_c_terminal_oo_geometry_2026_10_06.py` (SHA-256 `9033b26a60214e55c4325e74dcbf595889babcf686bc702fe13ac737b333f9dd`). Both files are unchanged from the Audit.63 source snapshot `51853ce9752c065663fd407289c6d46adc767f69`.
**Verdict:** REGRESSION VALID, at the finite local scope below.

## Exact statement

There is a strictly convex four-point unit-separated set whose unit-contact graph is a three-edge path along the convex hull, but whose first contact edge has squared normalized determinant `1/65` with the outward unit normal to the closing hull side. In particular, the short-pocket estimate `|det(v,n)| >= 1/2` cannot be extended to a three-edge pocket using only convexity, unit separation, and the local contact-path geometry.

The statement is local. The closing hull side is not asserted to be an actual diameter pair, and the set is not asserted to satisfy KKT equilibrium, canonical full-core hypotheses, or global minimum-diameter optimality.

## Independent exact reconstruction

Take

`A=(0,0), B=(0,-1), C=(1,-1), D=(8/5,-1/5)`.

The three path edges have squared length one. The other pairwise squared distances are `|AC|^2=2`, `|BD|^2=16/5`, and `|AD|^2=13/5`, so these are the only unit contacts. The successive oriented turns of `A-B-C-D-A` have determinants `1`, `4/5`, `7/5`, and `8/5`; hence this is a strictly convex hull cycle, with `DA` the closing side.

The outward normal to the oriented side `D-A` is proportional to `(1,8)`. Its squared norm is `65`. The first contact vector `B-A=(0,-1)` has determinant of magnitude `1/sqrt(65)` with the unit normal. Therefore

`|det(B-A,n)|^2 = 1/65 < 1/4`.

This exact counterexample rules out the claimed `1/2` determinant lower bound for a three-edge pocket under these local hypotheses. It does not show that the determinant can approach zero over all longer pockets, nor does it refute a theorem with additional actual-load or canonical-source hypotheses.

## Relation to the canonical terminal results

The larger frozen report also states `N_OO=o(D)` for canonical full-core Type-II sequences with `q/D -> pi` and `u_B=o(D)`, and the narrow-window binary witness bound `N_BB_binary <= u_B`. Those exact claims are already canonical as `C-OO-TERMINAL-TRAIN-POPULATION` and `C-BINARY-LOADED-WITNESS-POCKET-BUDGET` from Audit.63. I compared the report and verifier at `bf288c82` with their immutable Audit.63 source snapshot and found no changes, so those theorems are not promoted again here.

The finite regression explains why the terminal shore argument treats only good unit-hull or at-most-two-edge pocket ends as uniformly anchored and separately charges long pockets through `u_B`. It adds a proof-scope guardrail; it supplies no train population, motion, packet capacity, or Level I consequence.

## Certificate review

I inspected and reran `research/verify_target_c_terminal_oo_geometry_2026_10_06.py` at the frozen source snapshot. Its `long_pocket_regression` uses rational arithmetic to check every pair distance, the exact contact list, the positive turns, and the determinant ratio `1/65`. The full script also passed its 1,154 anchor checks, 32 short-pocket binary checks, 47,314 positive-cone checks, and 36,138 finite ledger checks. These finite checks do not prove the asymptotic train theorem or realize this four-point set as a canonical source.

## Canonical disposition

Promote the exact finite result as regression `C-TERMINAL-LONG-POCKET-ANCHOR-REGRESSION`. It refutes only the extension of the short-pocket determinant threshold from pockets of at most two edges to three-edge pockets under the stated local hypotheses. The Audit.63 terminal asymptotic and binary pocket theorems retain their exact scopes. The Target C frontier does not change: C-I is closed, C-II is open, and Level I is open.
