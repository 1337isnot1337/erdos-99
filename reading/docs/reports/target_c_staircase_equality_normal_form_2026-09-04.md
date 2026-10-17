> Generated reading edition · [exact source](../../../docs/reports/target_c_staircase_equality_normal_form_2026-09-04.md) · source SHA-256 `709cf4cf64e9ca93cc5476696daaa65b7f51a718a8737db85632633675c31b3e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2DE0B4CD3331","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C audit: C88 already contains the staircase equality normal form

**Date:** 2026-09-04  
**Repository base:** `89c17412`  
**Run type:** duplication audit + small exact corollary  
**Target:** Target C C-II, pure-rhombic C80 chain-face branch  
**LEVEL I STATUS:** STILL OPEN

## 1. Audit result

The initial version of this report incorrectly presented the exact C87 staircase
block form as new. It is not new.

`docs/reports/target_c_staircase_separator_budget_2026-09-01.md` (C88), Section 1,
already extracts equality in the C87 edge-count proof and proves:

- the distinct left endpoints are `a_i=i-1`;
- `M_1=D` and `m_s=s`;
- `m_i=M_(i+1)`;
- every row is complete;
- with `t_0=D`, `t_i=m_i`, the tree is exactly
  `E(G_P)={(i-1,b): t_i<=b<=t_(i-1)}`.

Thus the proposed “C97 staircase equality theorem” was a rediscovery of C88 and must
not be promoted as a new theorem.

The duplicate was caught before any route-map or canonical promotion.

## 2. Small corollary not stated explicitly in C88

C88's equality form has `a_1=0` and `M_1=D`. Since row 1 is complete, the simple
prefix edge

`{0,D}`

is present.

By C87.4, every simple prefix edge occurs in both physical hull-arc orientations.
Therefore there are at least two actual **non-chain** active diameter pairs with
C83 interval

`I=P=(0,D]`,

one with `eta>0` and one with `eta<0`.

They are distinct from the exact chain diameter `h_0=za`, because C83 has
`eta_(h_0)=0` while every non-chain active diameter meeting `P` has `eta!=0`.

Hence the complete C65 diameter graph contains the chain diameter together with a
paired transverse full-span bundle.

This is an immediate corollary of C83+C87+C88, not a new structural theorem.

## 3. Full-span curvature localization

Let

`W_P={v in R^P: sum_(tau in P) v_tau=0}`.

For a non-chain full-span bar `h`, C83 gives

`g_h|P=eta_h 1_P`,

so `g_h dot v=0` for every `v in W_P`.

C83.7 then gives

`H_h[v,v]=-c_h ||v||^2`.

C87.8 proves, interval by interval, that for every normalized KKT stress

`R_I=sum_(h:I_h=I) beta_h c_h >=0`.

For `I=P`,

`sum_(h:I_h=P) beta_h H_h[v,v] = -R_P ||v||^2 <=0`.

The chain diameter contributes

`beta_(h_0) H_(h_0)[v,v] = -beta_(h_0) D ||v||^2 <0`

under the C65 relative-interior stress. Therefore the chain diameter plus all
full-span non-chain bars make a strictly negative KKT diameter-curvature contribution
on every nonzero `v in W_P`.

### Audited corollary — full-span rows are not the chain-bending blockers

The forced full-span diameter bundle contributes no first-order rank on `W_P` and no
positive KKT quadratic curvature there. Any first-order locking of `W_P`, and any
positive diameter curvature capable of opposing the chain bar, must come from proper
C88 staircase intervals.

This corollary is exact but does not create a nonzero critical velocity: the proper
intervals can still have full rank on `W_P`.

## 4. Rejected shortcut

A tempting model treats the two physical orientations over every prefix edge as a
literal two-sheeted lift of `G_P`. That is not justified. C83's prefix value `k(v)` is
a separator level, not a unique source vertex, and several physical source vertices
can occupy the same level on the same hull arc. Any contradiction based on identifying
one physical `L_k` and one physical `U_k` per level is therefore invalid without a new
multiplicity theorem.

## 5. Exact next obligation

The working frontier is unchanged by the duplicate. The useful narrowed question is:

> Can the proper C88 staircase intervals realize full first-order rank on `W_P` while
> satisfying the physical diameter-thrackle geometry, C18 shared-endpoint angular
> gap, and C87 opposite-orientation KKT pairing?

A proof that they cannot would produce a chain-bending direction for which the forced
full-span bundle helps rather than blocks the second-order decrease.
