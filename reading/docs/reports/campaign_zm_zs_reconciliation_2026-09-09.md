> Generated reading edition · [exact source](../../../docs/reports/campaign_zm_zs_reconciliation_2026-09-09.md) · source SHA-256 `b8f1376b91ae323f6e574f5f9e81270db78e5867309ec41a64f73e08e71e2980`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b88f368fb5ea6de46e7fc5501041f30dfb7d0a00", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/campaign_zm_zs_reconciliation_2026-09-09.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2fe94bc98736952b5abc87b8c255344938df2ca112d221a543cd303943344712"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — ZM/ZS post-ZF reconciliation

**Date:** 2026-09-09  
**Repository state:** `2c476b38ee07218bb17a594b397717866c58b971` plus PR #109 research branch  
**Run type:** audit / synthesis  
**Target:** Target C Gate C-II / Level I  
**Active prompt:** user-supplied 2026-09-09 Target C-Z settlement prompt  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Two report-level results landed independently on September 9:

- ZS, in `target_c_zf_boundary_surplus_collapse_2026-09-09.md`, proves after ZF that
  
  ```math
  q\ge h\ge\delta\ge\lceil D\rceil
  ```

  and therefore
  
  ```math
  \sigma_B=2q-\delta-2\ge\lceil D\rceil-2.
  ```

- ZM, in `campaign_boundary_defect_matching_2026-09-09.md`, proves that the non-diameter response graph contains a terminal-disjoint matching `J` with
  
  ```math
  |J|\ge q/16.
  ```


The ZM report still states only the older C33 consequence `|J|>=(ceil(D)+2)/32` and proposes C44 Branch B as one possible next route. Both statements need reconciliation with ZS.

---

## 1. Starting endpoint

The live response-side endpoint after ZM is quantitative, not combinatorial:

```math
0<\sum_{ij\in J}c_{ij}
\le\frac12\operatorname{tr}(\Lambda-L_H),
\qquad
|J|\ge q/16.
```

ZM supplies linearly many terminal-disjoint positive non-diameter response channels but no lower bound on their aggregate conductance.

The direct Level I endpoint remains

```math
\boxed{
b+\sum_F(\deg F-4)>2h,}
```

which would contradict ZF.

---

## 2. Corollary ZMS — doubled diameter-scale response matching and removal of the C44 fallback

Assume the common audited post-ZF hypotheses of ZS and ZM for a sufficiently large lexicographically normalized triangle-free C-II global minimizer. Then

```math
\boxed{
|J|\ge\frac q{16}\ge\frac{\lceil D\rceil}{16}.
}
\tag{ZMS.1}
```

Moreover

```math
\boxed{
\sigma_B=o(D)
\quad\text{is impossible post-ZF}.
}
\tag{ZMS.2}
```

Consequently C44 Branch A/B is not a valid post-ZF fallback for proving a ZM aggregate-conductance lower bound. Any ZM mass theorem must be proved in the actual linear-boundary-surplus regime or by a theorem whose hypotheses do not include `sigma_B=o(D)`.

### Proof

ZM proves `|J|>=q/16`. ZS proves

```math
q\ge h\ge\delta\ge\lceil D\rceil.
```

Substitution gives ZMS.1.

ZS also proves

```math
\sigma_B\ge\lceil D\rceil-2.
```

Thus along every unbounded-cardinality sequence, `liminf sigma_B/D>=1`; in particular `sigma_B=o(D)` is impossible. This proves ZMS.2.

The C35-C45 near-minimal response module explicitly assumes `sigma_B=o(D)`, including C44. Therefore C44 Branch A/B cannot be applied to the same post-ZF source. `square`

### Dependencies

- `docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md` — ZS;
- `docs/reports/campaign_boundary_defect_matching_2026-09-09.md` — ZM;
- `docs/targets/target-c/04-near-minimal-response-frontier.md` — explicit `sigma_B=o(D)` premise.

### Why this reconciliation matters

The current ZM report retains the pre-ZS conversion `q>=(ceil(D)+2)/2` and explicitly lists C44 Branch B as a next-run option. ZS was committed separately and was not propagated into those statements. ZMS is the exact cross-route correction.

---

## 3. Exact target implication

The recorded diameter-scale matching improves from

```text
|J| >= (ceil(D)+2)/32
```

to

```text
|J| >= ceil(D)/16.
```

More importantly, post-ZF response work cannot use C44's near-minimal-boundary phase. The live mass problem must be attacked directly in the ZS linear-boundary-surplus class.

PR #109 supplies one exact description of that class through

```math
q=x_B+f+g_F+2d_H+2s_Z
```

and

```math
c_I+e_{BB}+s_C=q-2+d_H+s_Z.
```

Thus future response work can split by actual finite currencies rather than by the now-empty `sigma_B=o(D)` phase.

---

## 4. Exact remaining lemma

### ZM-mass lemma

Find an explicit `mu(D)>0`, strong enough to feed the C41/C64 quantitative bridge, such that every sufficiently large post-ZF survivor admits a ZM matching `J` with

```math
\boxed{
\sum_{ij\in J}c_{ij}\ge\mu(D).
}
```

A first meaningful target is `mu(D)>=c/D` for an absolute `c>0`; a constant lower bound would be stronger. Positivity edge by edge is already contained in ZM and is insufficient.

This mass lemma is not by itself Level I closure. A resulting trace defect still must be converted, using the actual unit embedding and global minimum, into the exact face inequality or a strict sub-`D` competitor.

The shortest direct Level I lemma remains

```math
\boxed{
b+\sum_F(\deg F-4)>2h.}
```

---

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| ZM exact rank `rank(\Lambda-L_H)=q-3` | proved at report level | Unchanged. |
| ZM matching `|J|>=q/16` | proved at report level | Unchanged. |
| ZM diameter conversion `|J|>=(ceil(D)+2)/32` | correct but superseded | ZS gives `q>=ceil(D)`. |
| ZMS `|J|>=ceil(D)/16` | proved and new cross-route corollary | Direct ZM + ZS substitution. |
| C44 Branch B as post-ZF ZM route | rejected under current hypotheses | C44 requires `sigma_B=o(D)`; ZS rules it out. |
| C44 theorem itself | correct under its stated premise | Only its use after ZF is removed. |

---

## 6. Regression tests

- ZM regular-hexagon affine projector: unchanged; ZMS changes only geometric scaling and phase bookkeeping.
- Unit square: below the sufficiently-large ZC/ZS regime.
- Crossing diameter matching: allowed; no uncrossing or star replacement is introduced.
- Strict pentagon response/face regression: allowed; no conductance floor or local Oler charge is asserted.

---

## 7. Failed routes

### ZM matching count -> quantitative mass

A linear number of positive response channels can carry arbitrarily small total mass absent a source-specific quantitative theorem. The stronger `D/16` support count does not change this.

### ZM + C44 Branch B after ZF

This route is dead under the present hypotheses. C44 requires `sigma_B=o(D)`, while ZS gives `sigma_B>=ceil(D)-2` for the same post-ZF source.

---

## 8. Literature and computation

No literature theorem or computation is imported by ZMS. It is an exact dependency reconciliation.

---

## 9. Canonical promotion recommendation

**Hold as report.**

ZS and ZM remain report-level. If their dependency stacks are later promoted, then update the near-minimal response module, Target C route map, active continuation prompt, and campaign ledger together. Do not promote this reconciliation independently.

---

## 10. Next run

Attack the ZM mass lemma directly in the linear-boundary-surplus class. Two live routes are:

1. combine ZM's `D/16` terminal-disjoint matching with the exact PR #109 ledgers and C35-C38 attachment incidence, splitting according to which of `c_I`, `e_BB`, or `s_C` is linear;
2. use ZM with C64.17 and the circular-planar split/dual representation to prove that vanishing aggregate non-diameter response mass forces the additive/zero-transfer structure already excluded by ZC, without invoking C44.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

ZM gives |J|>=q/16.
ZS gives q>=h>=delta>=ceil(D).
Therefore
    |J|>=ceil(D)/16.

ZS also gives sigma_B>=ceil(D)-2, so the C35-C45 phase sigma_B=o(D) is impossible after ZF. C44 Branch A/B is therefore not a post-ZF fallback.

Response endpoint:
    prove aggregate conductance mass for a ZM matching directly in the linear-boundary-surplus class.

Direct Level I endpoint:
    b+sum_F(deg F-4)>2h.

Authoritative report-level files:
    docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md
    docs/reports/campaign_boundary_defect_matching_2026-09-09.md
    docs/reports/target_c_zf_exact_defect_budget_addendum_2026-09-09.md
    docs/reports/campaign_zm_zs_reconciliation_2026-09-09.md
```
