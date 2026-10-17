> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_leaf_partial_cube_stability_2026-09-05.md) · source SHA-256 `bee6c738d3b607ea524a86df829f1ad972e6a0125750a8a60c5bade04bf82f3f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-29051C8ADAAD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C99: dominant-leaf partial-cube stability

**Date:** 2026-09-05  
**Run type:** exact train-combinatorics + max-flow theorem  
**Target:** C98 one-leaf near-chain phase  
**Depends on:** C11 total contact stress; C65 full visibility; C77 train pseudolines; C81 cut-flow method; C98 one-leaf concentration  
**External input:** region/tope graphs of weak pseudoline arrangements are partial cubes; see D. Eppstein, *Algorithms for drawing media* (GD 2004), arXiv:cs/0406020, and the standard tope-graph theory of oriented matroids/COMs.  
**Audit:** `docs/audits/target_c_c99_c100_nearchain_audit_2026-09-05.md`  
**LEVEL I STATUS:** STILL OPEN

C98 gives one actual diameter edge `h_*=za` with beta weight approaching one in C71-B. C99 turns that stress statement into exact train geometry without assuming the C76/C80 equality face.

Let `P(za)` be the trains separating `z,a` in a pure simply connected strict-rhombic disk, and put

`k=k_(za)=|P(za)|`.

For every normalized KKT stress with

`b=beta_(za)>1/2`,

C99 proves

`D <= k <= D/(2b-1)`.

If `b=1-eta`,

`0<=k-D<=2D eta/(1-2eta)`.

Moreover, orient every separator train vector from the `z` side toward the `a` side and write it as `a_tau`, with `|a_tau|=1`. For

`u=(p_a-p_z)/D`,

train coordinates give

`D u=sum_(tau in P)a_tau`,

and therefore the exact direction defect is

`sum_(tau in P)|a_tau-u|^2=2(k-D)`.

## 1. Train separation equals contact distance

C77's train curves are proper pseudolines in the rhombic disk: each runs through rhombus centers and contact-edge midpoints, two trains cross at most once, and each contact edge has one train label.

The complementary chambers correspond to contact vertices. Recording on which side of each train a chamber lies gives a sign vector; crossing one contact edge flips exactly its train coordinate. The region graph of a weak pseudoline arrangement is a partial cube, so this sign-vector embedding is isometric.

### Lemma C99.1

For any two contact vertices `x,y`,

`d_C(x,y)=#{tau: tau separates x and y}`.

Thus

`d_C(z,a)=k`,

and a shortest `z`-`a` contact path crosses every train in `P(za)` exactly once and no other train.

## 2. Dominant diameter gives direct contact max flow

Fix the actual diameter edge `za` with KKT weight `b>1/2`.

For any vertex cut `U` with `z in U`, `a notin U`, sum KKT equilibrium over `U`. The crossing diameter-force sum contains the `za` force of magnitude `Db`; every other crossing diameter reaction has total beta mass at most `1-b`, hence resultant norm at most `D(1-b)`.

Therefore the crossing contact-force resultant has norm at least

`D(2b-1)`.

Contact cut capacity is at least that norm. Max-flow/min-cut gives a contact flow from `z` to `a` of value

`F>=D(2b-1)`.

## 3. Capacity plus partial-cube distance bounds separator count

Remove cycles and decompose the flow into simple `z`-`a` paths. Every path has at least `k` contact edges by Lemma C99.1. Therefore

`sum_e |f_e|>=kF`.

But `|f_e|<=alpha_e` and C11 gives

`sum_e alpha_e=D^2`.

Hence

`kD(2b-1)<=D^2`.

### Theorem C99.2 — dominant-leaf separator count

`k_(za)<=D/(2b-1)`.

Unit contact paths between points at Euclidean distance `D` have at least `D` edges, so `k>=D`.

Writing `b=1-eta`,

`0<=k-D<=2D eta/(1-2eta)`.

## 4. Exact direction-defect identity

Because

`D u=sum_(tau in P)a_tau`,

one has

`sum_(tau in P)u dot a_tau=D`.

Since `|a_tau|=|u|=1`,

`|a_tau-u|^2=2(1-u dot a_tau)`.

Summing yields:

### Theorem C99.3

`sum_(tau in P)|a_tau-u|^2=2(k-D)`.

Thus

`sum_(tau in P)|a_tau-u|^2<=4D eta/(1-2eta)`.

Consequently, when `eta=o(1)`:

- `k=D+o(D)`;
- the mean-square angular defect tends to zero;
- for every fixed `rho>0`, only `o(D)` separator trains satisfy `|a_tau-u|>=rho`;
- a shortest contact path is a `D+o(D)`-edge near-geodesic crossing those trains once each.

## 5. C98 consequence

In C71-B with `D epsilon->0`, C98 gives one diameter edge with

`beta_(za)=1-o(1)`.

Therefore

`k_(za)=D+o(D)`

and

`sum_(tau in P(za))|a_tau-u|^2=o(D)`.

This is a weight-free near-chain train atom: only a sublinear number of separator tracks exceed the Euclidean minimum, and almost all are directionally close to the dominant diameter.

## 6. Limitation

C99 alone does not make `k=D`, because the available defect rate need not force `1-beta=o(1/D)`. Nor does average alignment reproduce C97's exact terminal-prefix contradiction. C100 supplies the stronger pointwise alignment and nesting theorem.
