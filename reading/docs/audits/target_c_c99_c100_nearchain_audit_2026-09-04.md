> Generated reading edition · [exact source](../../../docs/audits/target_c_c99_c100_nearchain_audit_2026-09-04.md) · source SHA-256 `c3fa9086e56d01c2c7620519243d197f708710d271746177fee4a35f267009f0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4A5FD50B3F28","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C C99/C100 dominant-leaf near-chain stability

**Date:** 2026-09-04
**Branch:** `research/target-c-c97-staircase-equality-2026-09-04`
**Candidates:**
- `docs/reports/target_c_dominant_leaf_partial_cube_stability_2026-09-04.md`
- `docs/reports/target_c_dominant_leaf_uniform_train_alignment_2026-09-04.md`

**Verdict:** PASS in the pure simply connected strict-rhombic train-coordinate regime.
**LEVEL I status:** STILL OPEN.

## C99.1 — partial-cube identification

C77 draws each train as a proper simple curve through rhombus centers and contact-edge midpoints; two train curves cross at most once. The complementary chambers are exactly the vertex neighborhoods of the rhombic complex, and crossing one chamber wall traverses one contact edge carrying that train label.

The chamber sign vector records the side of every train. Adjacent contact vertices differ in exactly one sign. The standard tope-graph theorem for pseudoline arrangements / complexes of oriented matroids says this sign embedding is isometric; equivalently the region graph is a partial cube. Therefore

`d_C(x,y)=# separating trains`.

This external combinatorial fact applies to proper disk pseudoline arrangements, including noncrossing train pairs; it is not restricted to arrangements in which every pair crosses.

PASS.

## C99.2 — dominant-edge cut flow

For any `z`-`a` cut, summed KKT equilibrium contains the crossing force of the diameter edge `za` with magnitude `D b`, where `b=beta_za`. All other crossing diameter reactions have total beta mass at most `1-b`, hence resultant norm at most `D(1-b)`. The contact cut capacity is at least the resultant norm. Thus

`cap>=D(2b-1)`

for `b>1/2`.

Max-flow/min-cut and the partial-cube path lower bound give

`k D(2b-1)<=D^2`,

so

`k<=D/(2b-1)`.

PASS.

## C99.3 — direction-defect identity

Train coordinates give the exact displacement

`D u=sum_(tau in P)a_tau`

with every `|a_tau|=1`. Dotting with `u` and summing

`|a_tau-u|^2=2(1-u dot a_tau)`

gives

`sum |a_tau-u|^2=2(k-D)`.

PASS.

## C100.1 — coordinatewise angular stationarity

A single train-angle variation preserves all contact lengths to first order, so KKT stationarity gives

`sum_h beta_h r_h dot J a_(h tau)=0`.

For a separator of the dominant edge, the dominant contribution is `bD u dot J a_tau`; every residual diameter contributes at most `D beta_h` in absolute value. Hence

`|u dot J a_tau|<=(1-b)/b`.

PASS.

## C100.2 — forward orientation from train stress

The Target-B virtual-work identity is

`A_tau=sum_e(in tau) alpha_e=sum_h beta_h r_h dot a_(h tau)>=0`.

Residual beta mass again contributes at most `(1-b)D`. Therefore

`u dot a_tau>=-(1-b)/b`.

For `rho=(1-b)/b<1/sqrt(2)`, the unit-circle equations plus `|sin|<=rho` exclude the negative-cosine branch and give

`u dot a_tau>=sqrt(1-rho^2)`.

PASS.

## C100.3 — noncrossing threshold

If `b>2/3`, then `rho<1/2` and every separator direction is within `pi/6` of `u`. Hence the acute angle between any two separator train lines is below `pi/3`.

At a crossing of two train tracks, their edge directions are adjacent side directions of a strict unit rhombus. Triangle-freeness requires both rhombus diagonals to exceed one, equivalent to the side angle lying strictly in `(pi/3,2pi/3)`. Thus the acute line angle is strictly greater than `pi/3`. The two conditions are incompatible.

Therefore all dominant-edge separators are pairwise noncrossing once `b>2/3`.

PASS.

## C100.4 — stronger separator count

Since every separator has forward projection at least `sqrt(1-rho^2)`,

`D=sum u dot a_tau>=k sqrt(1-rho^2)`.

Thus

`k<=D/sqrt(1-rho^2)`

and `k-D=O(D(1-b)^2)` as `b->1`.

PASS.

## Scope and remaining defect

C99/C100 do not recover the C87 prefix circulation. The nested separator stack gives exact prefix supports for other bars, but their train-angle gradient entries are

`r_h dot J a_tau`,

which vary with `tau`; C87 needs a common scalar on each interval. Replacing these rows by constant rows would silently discard an error of order up to `D(1-b)` per coordinate and is not justified at the current response-defect scale.

Audited conclusion:

> In the pure-rhombic C71-B near-zero phase, C98's dominant diameter eventually has a pairwise noncrossing ordered separator family, uniformly angularly close to the diameter direction, with only `O(D(1-beta)^2)` excess train count and exact contact distance equal to that train count.
