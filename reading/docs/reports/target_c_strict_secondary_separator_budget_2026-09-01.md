> Generated reading edition · [exact source](../../../docs/reports/target_c_strict_secondary_separator_budget_2026-09-01.md) · source SHA-256 `38e55750379903b56dd7af23fc2171986f9074e2acf706b0416f9fd74f730dc2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F936F038CC8C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C93: strict secondary-train separator budget

**Date:** 2026-09-01  
**Repository base:** `ebe68c04` (main after C92 / PR #97)  
**Status:** LEVEL I STILL OPEN

C88 proves a quadratic incidence between the C87 paired staircase diameters and trains
outside the exact D-track chain atom P. C93 sharpens the integer separator count for
every non-chain diameter and improves the exact budget from `D(D-1)` to `D(D+1)`.

Let h be an active non-chain diameter pair with nonempty C83 chain interval `I_h` of
length

`ell_h=|I_h|`.

In exact train coordinates,

`r_h=sum_tau d_(h,tau) u_tau`,

where every nonzero summand is a unit vector. Let

`k_h=sum_tau d_(h,tau)^2`

be the number of trains separating the endpoints. Since `|r_h|=D`, triangle
inequality gives `k_h>=D`.

### Lemma C93.1 — strict total separator count

For every such non-chain diameter,

`k_h>=D+1`.

Proof. If `k_h=D`, equality holds in the triangle inequality

`|sum d_(h,tau)u_tau| <= sum |d_(h,tau)u_tau|=D`.

Therefore every nonzero oriented separator vector `d_(h,tau)u_tau` is parallel and
points in the same direction as `r_h`. Since `I_h` is nonempty, at least one of those
vectors is `+-u`, where u is the exact C80 chain direction. Thus `r_h` is parallel to
u. A diameter-D point set contains at most one diameter segment in a prescribed
unoriented direction; that segment is the chain diameter `za`. Hence h would equal the
chain diameter, contradicting that h is non-chain. `square`

Exactly `ell_h` of the separating trains lie in P. Consequently

`# {tau notin P : tau separates h} >= D+1-ell_h`.

C87 supplies at least two actual active diameter pairs, one in each hull-arc
orientation, over every one of its D simple staircase edges. Select one of each
orientation. C88 proves the exact staircase identity

`sum_e ell_e=D(D+1)/2`.

Summing the strict separator bound over the 2D selected diameters gives

`sum_(selected h) # {tau notin P : tau separates h}`

`>= 2 sum_e(D+1-ell_e)`

`= D(D+1)`.

### Theorem C93 — strict staircase separator budget

Every canonical pure-rhombic C80-C87 chain-face survivor has at least

`D(D+1)`

incidences between the selected paired staircase diameters and train tracks outside P
that separate their endpoints.

This improves C88 by exactly `2D` incidences. The leading asymptotic coefficient is
unchanged, but the bound is exact and has no hidden O(D) loss.

If `T` is the total number of trains, some non-chain train separates at least

`D(D+1)/(T-D)`

of the selected active diameter pairs. C90 then classifies that train-cut subgraph as
a caterpillar forest.

The exact next target remains a capacity theorem for the simultaneous C87 staircase
and C90 caterpillar orders; C93 removes the last integer equality loophole in the
secondary-separator count.