> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cap_local_stress_transversal_independent_audit_2026-10-08.md) · source SHA-256 `8da03fef40db87ab64b61280b4d14a87b29e79021763c1f396e0399ae2cfc32f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-43D6F1B1DB6F","canonical":true,"claim_ids":["C-EXTERIOR-CAP-LOCAL-STRESS-TRANSVERSALS"],"claim_statuses":{"C-EXTERIOR-CAP-LOCAL-STRESS-TRANSVERSALS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent Audit.150: localized stress transversals along an exterior-cap separator

**Date:** 2026-10-08  
**Audit base:** `origin/main=2010296d3c00903423b67d96d70ae369d56b9e26`, state `2026-10-08.audit.147`  
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`  
**Source report:** `docs/reports/target_c_exterior_cap_separator_motion_and_interior_refill_2026-10-06.md`, SHA-256 `0192a54ab219b0a6bdfd4ea012138d82c59a219e59b13ad4b6a395a3081abfce`  
**Audited unit:** Section 3, Theorem S.3-L only. The earlier Audit.139 did not audit this claim.

## Verdict

**PASS — promote `C-EXTERIOR-CAP-LOCAL-STRESS-TRANSVERSALS` at the exact cut scope below.** For every eligible parallel cut, the contact stress crossing that cut has a weighted projection sum at least `2g`, and a set of at most `s_Z+1` negative-side core vertices meets the positive contact support of every normalized KKT stress. Cuts spaced at least two units apart give disjoint transversals; when `g>=gamma D` for fixed `gamma>0`, there are `Omega(D)` such cuts.

The strict-motion consequence is the already canonical `C-UNLOADED-KKT-STRESS-TRANSVERSAL`: deleting any unloaded set that kills all normalized stresses admits a strict reduced-source motion, with contact-isolated points retained. This result gives many separate reduced-source descents. It does not give simultaneous motions, a same-cardinality refill, a strict competitor at the original cardinality, or C-II/Level I closure.

## Exact statement audited

Let `A` be a canonical contact-minimal then actual-diameter-pair-minimal C-II source, with `D>=9`, full source retained, nonisolated positive-contact core `V`, actual diameter-endpoint set `B`, unit-contact set `C`, actual diameter-pair set `H`, and normalized KKT stress polytope

```math
\mathcal P=\{(\alpha,\beta)\ge0:R^T(\alpha,-\beta)=0,\ \sum_{h\in H}\beta_h=1\}.
```

Write `s_Z=dim_aff(P)`, as in canonical Section 64.1. Assume the canonical actual exterior-cap separator supplies a unit vector `w` and `g>1` such that every `b in B` has `|w dot b|>=g`, and every actual diameter pair has one endpoint with `w dot b<=-g` and the other with `w dot b>=g`.

For each `t` in `(-g+1,g-1)`, use shores `V_-={p in V:w dot p<=t}` and `V_+={p in V:w dot p>t}`. Let `C_t` be the actual unit contacts crossing these shores, orient each crossing edge `e=p_e q_e` from the negative to positive shore, and set

```math
d_e=w\cdot(q_e-p_e)>0,\qquad
R_t=\{p_e:e\in C_t\}.
```

Then:

1. `R_t` is a nonempty subset of the unloaded core `V\\B`, and every `p in R_t` lies in the strip `t-1 < w dot p <= t`.
2. For every normalized stress `(alpha,beta) in P`,

   
   ```math
   \sum_{e\in C_t}\alpha_e d_e
   =\sum_{h\in H}\beta_h d_h\ge2g.
   ```


   Hence `sum_{e in C_t} alpha_e >=2g`, since each unit-contact projection `d_e` is at most one.
3. There is a nonempty `U_t subset R_t` with `|U_t|<=s_Z+1` such that every normalized stress has positive contact coefficient on at least one contact incident to `U_t`. Thus deleting `U_t` removes every normalized KKT stress and, by the canonical unloaded-transversal theorem, permits a strict reduced-source motion.
4. If two cut levels differ by at least two, their strips and transversals are disjoint. If `g>=gamma D` along a source sequence for fixed `gamma>0`, one can choose `Omega(D)` pairwise disjoint transversals.

The cap-area hypothesis is needed only for the last asymptotic count: Audit.139 supplies `g>=gamma_alpha D` when an actual exterior cap has area at least fixed `alpha D^2`. The finite cut statement itself needs the displayed separator hypotheses.

## Independent proof reconstruction

For a cut level `t`, a crossing unit contact has a unique orientation from `x_p<=t` to `x_q>t`. Its projected length is

```math
d_e=x_q-x_p\in(0,1],
```

so `t-1<x_p<=t`. Since `t>-g+1` and `t<g-1`, the strip `(t-1,t]` lies strictly between `-g` and `g`. It contains no loaded endpoint. Every point in `R_t` is a contact vertex, hence is in `V`, and is unloaded.

For any velocity field on the core, KKT stationarity gives the virtual-work identity

```math
\sum_{e\in C}\alpha_e\,\dot\ell_e
 =\sum_{h\in H}\beta_h\,\dot\ell_h,
```

where `dot ell` is the derivative of half the squared pair distance. Give every core vertex on the negative shore velocity `+w` and every core vertex on the positive shore velocity `-w`. Contacts internal to either shore have zero derivative. A crossing contact has `dot ell_e=-2d_e`. Each actual diameter pair also crosses the cut, has projected span `d_h>=2g`, and has `dot ell_h=-2d_h`. Substitution and cancellation of `-2` prove the equality. Since `sum beta_h=1` and every `d_h>=2g`, the right side is at least `2g`. This proves the strict positivity of the crossing contact load for every normalized stress.

For each `u in R_t`, define the nonnegative affine functional

```math
f_u(\alpha,\beta)=\sum_{e\ni u}\alpha_e,
\qquad F_u=\{s\in\mathcal P:f_u(s)=0\}.
```

The force inequality implies `intersection_{u in R_t} F_u` is empty: every stress has positive coefficient on some crossing edge, whose negative endpoint belongs to `R_t`. Choose an inclusion-minimal subfamily `U_t` with empty intersection. For each `u in U_t`, minimality supplies a stress `s_u` in all `F_v` for `v in U_t\\{u}` and outside `F_u`. Thus `f_u(s_u)>0` and `f_v(s_u)=0` for every other selected `v`.

If `sum_u lambda_u s_u=0` and `sum_u lambda_u=0` is an affine dependence, applying each `f_v` gives `lambda_v f_v(s_v)=0`; hence every `lambda_v=0`. The witnesses are affinely independent in `P`, so `|U_t|<=dim_aff(P)+1=s_Z+1`. They are nonempty because the intersection over all `R_t` is empty. Any normalized stress on the reduced source extends by setting all removed incident contact coefficients to zero; it would belong to every selected `F_u`, a contradiction. The canonical `C-UNLOADED-KKT-STRESS-TRANSVERSAL` then gives the stated strict reduced-source motion. Its full-source margin argument retains every contact isolate.

If `t_2-t_1>=2`, the strips `(t_1-1,t_1]` and `(t_2-1,t_2]` are disjoint, so `U_{t_1}` and `U_{t_2}` are disjoint. The admissible interval has length `2g-2`; taking levels two units apart gives a number proportional to `g` once `g` grows. Audit.139's fixed-area cap conclusion `g>=gamma_alpha D` gives the `Omega(D)` count.

## Dependencies and hostile scope checks

- `C-EXTERIOR-CAP-DIAMETER-SEPARATOR` (canonical Audit.139) supplies the cap-specific loaded-endpoint gap and opposite-side property. No selected-stress-only diameter graph is substituted for the full actual graph.
- `C-DIAMETER-LEAF-CONTACT-INCIDENCE` places canonical loaded endpoints in `V`; the cut motion used for virtual work is defined on every core vertex. Contact isolates are not given stress coordinates and remain in the full source.
- `C-UNLOADED-KKT-STRESS-TRANSVERSAL` supplies the reduced-source strict-motion consequence once the selected set kills every normalized stress. No new finite-motion theorem is claimed.
- Section 64.1 identifies `dim_aff(P)=s_Z`; the independent face proof above uses only this dimension identity.
- The canonical `C-UNLOADED-TRANSVERSAL-RESTORATION-REGRESSION` remains binding: the newly deleted contacts need not open along the same reduced-source descent. A transversal is not a refill.
- Distinct cut transversals are disjoint as vertex sets, but their associated reduced motions are not asserted compatible or simultaneous. The force lower bound is aggregate; it does not bound any individual KKT multiplier from below.
- No verifier checks Theorem S.3-L. I inspected `research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py` at the frozen source: it constructs explicit spoke/isolate packets and checks finite source/endpoint pair distances. It has no stress variables, cut levels, or transversal test, so its finite checks are not evidence for this theorem and were not used.

## Canonical disposition and frontier effect

Promote `C-EXTERIOR-CAP-LOCAL-STRESS-TRANSVERSALS` with dependencies on `C-EXTERIOR-CAP-DIAMETER-SEPARATOR`, `C-DIAMETER-LEAF-CONTACT-INCIDENCE`, and `C-UNLOADED-KKT-STRESS-TRANSVERSAL`. Add it to the Target C canonical theorem graph, but leave the current endpoint unchanged: an actual macroscopic cap still yields only reduced-cardinality descents, with the same full-source refill/capacity obligation open. The active continuation prompt needs only its state-version stamp updated; its mission and next obligation are unchanged. C-II and Level I remain open.
