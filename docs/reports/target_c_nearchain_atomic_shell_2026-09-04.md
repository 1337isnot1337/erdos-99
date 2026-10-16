<!-- theorem-state: {"artifact_id":"ART-04ADDCA32F32","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearchain_atomic_shell_2026-09-04.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=1273c77a52cc53ef4160169d3be7bce026448c34; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C101: the near-chain separator stack is a limiting train-direction atom

**Date:** 2026-09-04
**Repository base:** branch after audited C99/C100 (`e62e9a6`)
**Run type:** asymptotic shell transfer
**Target:** C71-B one-leaf near-chain phase
**Depends on:** C98, C100, Target-B Section 39, C82 weighted-Mantel argument
**Status:** proved working result
**LEVEL I STATUS:** STILL OPEN

C82's improved shell constants were originally stated under the exact C80 chain face because that face supplies `D` train tracks in one literal direction. C100 shows that exact equality is unnecessary for the asymptotic weighted-Mantel step.

In the C98/C100 one-leaf phase, let `h_D=z_Da_D` be the dominant diameter edge and `P_D` its separator trains. Write

`b_D=beta_(h_D)->1`,

`k_D=|P_D|`,

`T_D=total number of trains`,

and let `u_D` be the diameter direction.

C100 gives

`k_D/D ->1`

and

`max_(tau in P_D) angle(a_tau,u_D)->0`.

After rotating each configuration so that `u_D` is a fixed projective direction, every empirical train-direction weak limit therefore has an atom of mass at least

`liminf k_D/T_D = 1/x`

when `T_D/D->x`.

That is exactly the only C80 input used by the weighted-Mantel portion of C82. Hence all C82 shell inequalities survive in the near-chain phase.

---

## 1. Uniform cone collapse creates an atom

Let

`mu_D=(1/T_D) sum_(tau) delta_[u_tau]`

be the empirical projective train-direction measure.

By C100, for every `tau in P_D`,

`angle([u_tau],[u_D]) <= arcsin rho_D`,

where

`rho_D=(1-b_D)/b_D ->0`.

Choose rotations so `[u_D]` is a fixed projective direction `[u]`. For every open neighborhood `N` of `[u]`, all of `P_D` lies in `N` for sufficiently large `D`. Therefore

`mu_D(N) >= k_D/T_D`.

Pass to any weakly convergent subsequence `mu_D => mu` with `T_D/D->x`. The Portmanteau theorem, followed by shrinking `N`, gives

`mu({[u]}) >= limsup k_D/T_D` along a further subsequence; in particular the limiting atom mass `a` satisfies

`a>=1/x`.

Using C100.4,

`k_D/D=1+O((1-b_D)^2)`,

so no mass is lost at leading order.

## 2. Target-B atomic crossing theory applies unchanged

Target-B Section 39 proves for every pure-rhombic asymptotic survivor:

1. positive-density rhombus crossings are carried by atoms of the limiting train-direction measure;
2. the limiting crossing graph on those atoms is triangle-free;
3. if `s` is total atomic mass and `y=q/T`, then

   `s<=1-y/2`;

4. with `x=T/D` and `c=2sqrt(3)/pi`, the limiting crossing density is

   `R/T^2 -> 1/(c x^2)`.

These statements do not require the heavy atom to be exactly atomic at each finite `D`; weak-limit atomicity is precisely their setting.

C101.1 supplies a distinguished limiting atom of mass

`a>=1/x`.

Thus the weighted-Mantel proof of C82 applies verbatim.

## 3. C101 shell inequality

Put

`Delta_2=pi/(2sqrt(3))`,

`A=1+Delta_2`.

For every pure-rhombic C71-B near-zero sequence to which C98/C100 apply,

### Theorem C101

`T/D >= A/(1-y/2)+o(1)`,

where `y=q/T`.

Consequently

`liminf T/D >= (4/3)(1+Delta_2)
                  =2.5425329094...`,

`limsup q/T <= pi/(1+Delta_2+pi/2)
             =0.9033545903...`,

and

`liminf (T-q)/D
 >=1+Delta_2-pi/2
 =0.3361033553...`.

These are exactly the C82 constants, now obtained without an exact C76/C80 chain face.

## 4. Interpretation

C98-C101 now give the following robust chain-side stack:

`D epsilon->0` in C71-B

`=> one beta edge has weight 1-o(1)`  (C98)

`=> its separating trains are uniformly near-parallel, nested, and k=D+o(D)`  (C99-C100)

`=> those trains form a limiting atom of mass at least 1/x`  (C101)

`=> the sharpened C82 shell/neutral-space constants hold`.

Thus the near-zero branch cannot evade the exact-chain shell footprint merely by letting the chain train directions split by vanishing angles.

## 5. Remaining gap

The weighted-Mantel inequality is still close to sharp: an almost balanced bipartite limiting crossing graph can accommodate an atom of mass `1/x`. C101 therefore does not by itself force an Oler surplus.

The live finite defect is now explicit. The dominant separator stack is an atom in the limit but not an exact finite atom; its angular spread is `O(1-b_D)`, and the C87 prefix circulation fails by exactly those finite angular errors. A closure must charge that angular spread, or the residual train topology needed to support it, at order at least `1/D` in the global response/shell budget.
