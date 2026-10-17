> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_cut_load_profile_2026-09-05.md) · source SHA-256 `9c70e8b8827d6ff39b2af31814335831f141c57e03add9507c02f2c4840f3cfe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-620D59D53026","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C chain-cut load profile

**Date:** 2026-09-05  
**Repository state:** `89c17412` (`main`)  
**Run type:** exact finite structural theorem  
**Target:** Target C / C96 near-spanning caterpillar  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used for the proof  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

C87-C88 put the canonical pure-rhombic chain-face survivor into an exact staircase normal form. C96 uses the common chain train to obtain one caterpillar cut with at least `2D+1` crossing diameter edges and hence `q>=2D+2` diameter endpoints.

The missing geometric step is to classify the near-spanning common-cut caterpillar. Before doing that, it is useful to remove an ambiguity left in C87/C96: the common train is not merely existential. C88 determines it uniquely and determines the selected diameter load on every chain train.

```text
C88 staircase -> exact load profile on all D chain cuts -> unique C96 cut and exact deficit profile -> sharper equality/near-equality data for the caterpillar classification
```

## 2. Strongest genuinely new audited theorem

### Theorem — exact chain-cut load profile

Use the C88 staircase notation

`D=t_0>=t_1>=...>=t_s=s`

and

`E(G_P)={(i-1,b): t_i<=b<=t_(i-1), 1<=i<=s}`.

For `1<=j<=D`, let `N_j` be the number of simple prefix intervals containing the chain train `tau_j`:

`N_j=#{(a,b) in E(G_P): a<j<=b}`.

Then

`N_j=D-t_j+j` for `1<=j<=s`,

and

`N_j=D-j+1+#{i in {1,...,s-1}: t_i>=j}` for `s<=j<=D`.

In particular:

1. `N_s=D`;
2. `N_j<=D-1` for every `j!=s`;
3. the unique chain train contained in every simple staircase interval is `tau_s`;
4. `N_1<...<N_s>N_(s+1)>...>N_D`, with exact increments
   `N_(j+1)-N_j=t_j-t_(j+1)+1` for `j<s`, and
   `N_(j+1)-N_j=-1-#{i: t_i=j}` for `j>=s`;
5. after selecting one active diameter pair of each C87 physical orientation above every simple interval and adjoining the chain diameter `za`, the selected crossing subgraph at `tau_j` has exactly `2N_j+1` edges. Since it is a forest, it uses at least `2N_j+2` distinct diameter endpoints. Hence

   `q>=2N_j+2`

   for every chain cut, with the unique strongest member `q>=2D+2` occurring at `j=s`.

Equivalently, the selected-edge deficit from the C96 cut is exact:

`D-N_j=t_j-j` for `j<=s`,

and

`D-N_j=j-1-#{i in {1,...,s-1}:t_i>=j}` for `j>=s`.

### Scope

This is an exact finite theorem inside the canonical pure simply-connected C80-C88 chain-face branch. It does not assert that every Target C survivor is already in that branch, and it does not by itself settle Level I.

### Proof

A C88 row `i` consists of the intervals

`(i-1,b]`, `t_i<=b<=t_(i-1)`.

Such an interval contains `tau_j` exactly when

`i<=j<=b`.

Assume first `j<=s`. Only rows `1,...,j` can contribute. Since the staircase sequence ends at `t_s=s`, monotonicity gives `t_i>=s>=j` for every `i<=j`. Thus every edge in each of the first `j` rows contains `tau_j`, and

`N_j=sum_(i=1)^j (t_(i-1)-t_i+1)=D-t_j+j`.

At `j=s`, `t_s=s`, so `N_s=D`.

Now assume `j>=s`. Every row index `i<=s` satisfies `i<=j`, so the only condition is `b>=j`. The integer row intervals

`[t_i,t_(i-1)]`, `1<=i<=s`,

cover every integer column `b` from `s` through `D` once, with one additional occurrence for each internal junction value `t_i=b`, `1<=i<=s-1`. Therefore the number of row-edge pairs with `b>=j` is

`N_j=(D-j+1)+#{i in {1,...,s-1}:t_i>=j}`.

For `j<s`, the first formula gives

`D-N_j=t_j-j>=s-j>=1`.

For `j>s`, the second formula gives

`D-N_j=j-1-#{i:t_i>=j}>=j-1-(s-1)=j-s>=1`.

Hence `N_s=D` and every other `N_j` is at most `D-1`. This also proves that `tau_s` is the unique common train. (Directly, C88 includes the singleton interval `(s-1,s]`, so any common train must be `tau_s`.)

The difference formulas follow by subtraction. For `j<s`,

`N_(j+1)-N_j=t_j-t_(j+1)+1>=1`.

For `j>=s`, the count `#{i:t_i>=j}` drops by exactly `#{i:t_i=j}` when `j` is replaced by `j+1`, so

`N_(j+1)-N_j=-1-#{i:t_i=j}<=-1`.

Finally C87 supplies at least one active diameter pair in each physical hull-arc orientation above every simple interval. Select exactly one of each orientation. A selected diameter crosses `tau_j` exactly when its C83 interval contains `j`, so exactly `2N_j` selected non-chain diameter edges cross that train. The chain diameter `za` crosses every chain train, giving `2N_j+1` selected crossing edges total.

C90 applies to the complete crossing diameter graph at every train cut; therefore its selected subgraph is also a forest. A nonempty forest with `m` edges has at least `m+1` incident vertices. Consequently the selected cut at `tau_j` uses at least `2N_j+2` distinct source diameter endpoints, proving `q>=2N_j+2`.

### Dependencies

- `docs/reports/target_c_positive_prefix_thrackle_collapse_2026-09-01.md` (C87 paired staircase/common-cut theorem)
- `docs/reports/target_c_staircase_separator_budget_2026-09-01.md` (C88 exact staircase normal form)
- `docs/reports/target_c_secondary_train_caterpillar_2026-09-01.md` (C90 train-cut forest/caterpillar theorem)
- `docs/reports/target_c_common_chain_caterpillar_2026-09-01.md` (C96 endpoint floor and current endpoint)

### Why it is new

C88 records only the total span `sum_e |I_e|=D(D+1)/2`. C87/C96 record existence of a common train, and C96 uses its load `D`. The current canonical files do not identify that train as `tau_s`, prove uniqueness, or give the exact finite load `N_j` and edge deficit at every chain cut.

## 3. Exact target implication

C96's existential common-cut object is now canonically located at the staircase pivot `s`, and its equality/near-equality analysis can use exact neighboring-cut deficits rather than only the global span average.

This does not improve the endpoint floor beyond `q>=2D+2`: the theorem proves that the C96 cut is already the unique maximally loaded selected chain cut. Any stronger endpoint inequality must therefore use geometry or compatibility between multiple cuts, not a better choice of one chain cut.

That is also a no-go result for a tempting route: single-cut re-averaging of the C88 staircase cannot beat C96.

## 4. Exact remaining lemma

A useful next theorem must exploit simultaneous geometry, not another load count. One sharp form is:

> **Near-spanning multi-cut compatibility lemma.** There is an absolute `epsilon>0` such that no triangle-free globally minimal canonical chain-face survivor with `q<=(2+epsilon)D` realizes the C88 paired staircase together with the exact chain-cut load profile above.

Even a proof in the exact endpoint case `q=2D+2` would materially advance C96, because then the `tau_s` crossing graph is one spanning caterpillar tree with no crossing-edge slack.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Exact formulas for `N_j` | proved | direct count from C88 staircase rows |
| `tau_s` is the unique common chain train | proved | `N_s=D`, all other loads `<D`; also singleton interval `(s-1,s]` |
| Exact selected crossing count `2N_j+1` | proved | C87 gives two selected orientations per interval; `za` crosses every chain train |
| `q>=2N_j+2` for each `j` | proved | C90 crossing graph is a forest |
| A different single chain cut can improve C96 | rejected | `N_s` is the unique maximum `D` |
| Near-spanning multi-cut geometry yields a contradiction | conjectural | this is the remaining lemma, not proved here |

## 6. Regression tests

The formulas include both extremal staircase shapes.

- If `s=1`, then `t_1=1` and the tree is the single row `(0,b)`, `1<=b<=D`; the profile is `N_j=D-j+1`, with unique maximum at `j=1`.
- If `s=D`, then all `t_i=D` and the tree is the single-column star `(i-1,D)`, `1<=i<=D`; the profile is `N_j=j`, with unique maximum at `j=D`.

Thus no hidden balance or symmetry assumption on the staircase was used.

## 7. Failed routes and no-go results

The load profile itself cannot strengthen `q>=2D+2`. Its maximum is exactly `D`, attained only at the already-used C96 cut. Any claimed improvement obtained solely by choosing another chain train contradicts the exact profile.

## 10. Canonical promotion recommendation

**Hold as report** until the multi-cut compatibility consequence is developed or independently audited. The statement is exact and proved, but it sharpens bookkeeping rather than yet changing Level I status.

## 11. Next run

Attack the exact endpoint `q=2D+2`. Combine:

1. C96: `H_(tau_s)` is one spanning caterpillar tree with `2D+1` edges;
2. the load profile: every neighboring chain cut is obtained by deleting an explicitly counted family of paired staircase diameter edges;
3. the diameter-thrackle order on both sides of each cut.

The first target is to classify how the caterpillar spine can change when crossing from `tau_j` to `tau_(j+1)`. A forced extra diameter edge, extra component, or forbidden even cycle at any step would create endpoint slack and push beyond the C96 minimum.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
The C88 staircase has an exact strictly unimodal chain-cut load profile N_j. Its unique common/maximally loaded train is tau_s, with N_s=D; every selected cut contains exactly 2N_j+1 diameter edges including za and forces q>=2N_j+2.

Exact endpoint now:
C96 is already the optimal single-chain-cut endpoint. Further progress must use simultaneous geometry between cuts. At q=2D+2, H_(tau_s) is one spanning caterpillar tree with zero crossing-edge/component slack.

Binding no-go:
No re-averaging or alternative single chain cut can improve q>=2D+2, because N_s=D is the unique maximum.

Highest-value next lemma:
Classify the q=2D+2 spanning caterpillar under the adjacent-cut deletion profile; force an extra edge/component, an even diameter cycle, or a geometric unit-separation violation.

Authoritative inputs:
docs/reports/target_c_positive_prefix_thrackle_collapse_2026-09-01.md
docs/reports/target_c_staircase_separator_budget_2026-09-01.md
docs/reports/target_c_secondary_train_caterpillar_2026-09-01.md
docs/reports/target_c_common_chain_caterpillar_2026-09-01.md
```
