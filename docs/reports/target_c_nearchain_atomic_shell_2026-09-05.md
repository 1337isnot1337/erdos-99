<!-- migration-source: path=docs/reports/target_c_nearchain_atomic_shell_2026-09-05.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a1aed5e75ec52664001100df06e77ed218d81391; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C101: near-chain separator stack creates a limiting train atom

**Date:** 2026-09-05  
**Run type:** asymptotic shell transfer  
**Target:** C71-B one-leaf near-chain phase  
**Depends on:** C98, C100, Target B Section 39, C82 weighted-Mantel argument  
**LEVEL I STATUS:** STILL OPEN

C82's sharpened shell constants were originally stated under the exact C80 chain face because that face supplies `D` train tracks in one literal direction. C100 shows that exact equality is unnecessary for the asymptotic weighted-Mantel step.

Let `h_D=z_Da_D` be the C98 dominant diameter edge and `P_D` its separator trains. Put

`b_D=beta_(h_D)->1`,

`k_D=|P_D|`,

`T_D=total number of trains`,

and let `u_D` be the diameter direction.

C100 gives

`k_D/D->1`

and

`max_(tau in P_D) angle(a_tau,u_D)->0`.

After rotating each configuration so that `u_D` is fixed, every empirical train-direction weak limit therefore has an atom of mass at least

`liminf k_D/T_D=1/x`

when `T_D/D->x`.

This is exactly the C80 input used by the weighted-Mantel part of C82.

## 1. Uniform cone collapse creates an atom

Let

`mu_D=(1/T_D) sum_tau delta_[u_tau]`

be the empirical projective train-direction measure.

C100 gives, for every `tau in P_D`,

`angle([u_tau],[u_D])<=arcsin rho_D`,

where

`rho_D=(1-b_D)/b_D->0`.

Rotate so `[u_D]` is a fixed projective direction `[u]`. Every neighborhood of `[u]` contains all of `P_D` for sufficiently large `D`. Thus

`mu_D(N)>=k_D/T_D`.

Passing to a weakly convergent subsequence gives a limiting atom at `[u]` of mass at least `1/x`.

C100 also gives

`k_D/D=1+O((1-b_D)^2)`,

so no leading-order mass is lost.

## 2. Insert Target-B atomic crossing theory

Target B Section 39 gives, for every pure-rhombic asymptotic survivor:

- positive-density rhombus crossings are carried by atoms of the limiting train-direction measure;
- the limiting crossing graph on those atoms is triangle-free;
- if `s` is total atomic mass and `y=q/T`, then `s<=1-y/2`;
- with `x=T/D` and `c=2sqrt(3)/pi`, the limiting crossing density is `1/(c x^2)`.

C101 supplies one distinguished atom of mass at least `1/x`. Therefore the prescribed-heavy-atom weighted-Mantel proof of C82 applies unchanged.

## 3. C101 shell inequality

Put

`Delta_2=pi/(2sqrt(3))`,

`A=1+Delta_2`.

For every pure-rhombic C71-B near-zero sequence to which C98/C100 apply,

### Theorem C101

`T/D >= A/(1-y/2)+o(1)`,

where `y=q/T`.

Consequently

`liminf T/D >= (4/3)(1+Delta_2)=2.5425329094...`,

`limsup q/T <= pi/(1+Delta_2+pi/2)=0.9033545903...`,

and

`liminf (T-q)/D >= 1+Delta_2-pi/2=0.3361033553...`.

## 4. Robust chain-side stack

C98-C101 now give

`D epsilon->0` in C71-B

`=> one beta edge has weight 1-o(1)`  (C98)

`=> its separator trains are uniformly near-parallel, nested, and k=D+o(D)`  (C99-C100)

`=> those trains form a limiting atom of mass at least 1/x`  (C101)

`=> the C82 sharpened shell and neutral-space constants hold without an exact C80 face.`

Thus the near-zero branch cannot evade the exact-chain shell footprint merely by splitting the chain direction through vanishing angles.

## 5. Remaining gap

Weighted Mantel is still nearly sharp. The live finite defect is explicit: the dominant separator stack is an atom only in the limit. Its finite angular spread is `O(1-b_D)`, and the C87 prefix circulation fails by the corresponding train-by-train gradient errors.

A closure must charge that angular spread, or the residual topology needed to support it, at a scale strong enough to contradict the global response/shell budget.
