> Generated reading edition · [exact source](../../../docs/audits/target_c_c98_single_port_mesh_audit_2026-09-04.md) · source SHA-256 `bc64b91846d2462de7d4043911999cddcda8f83e722b440bdaeeb4d82606442f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-030C67B213DC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C C98 single-port mesh defect

**Date:** 2026-09-04
**Branch:** `research/target-c-c97-staircase-equality-2026-09-04`
**Candidate:** `docs/reports/target_c_single_port_mesh_defect_2026-09-04.md`
**Verdict:** PASS.
**LEVEL I status:** STILL OPEN.

## 1. Single-port Kron decomposition

Let `R` be a component of `C-z` attached to `z` by one contact `zx` of conductance `A`. With `{x} union B_R` held as boundary, eliminate the other interior vertices of `R`. The resulting response is a Laplacian with nonnegative conductances `d_xt,d_st`.

After adjoining the edge `zx` and eliminating `x`, the one-vertex Schur complement gives

`c_zt=A d_xt/(A+d_x)`

and

`c_st=d_st+d_xs d_xt/(A+d_x)`.

No other contact component can alter these terms downward: Kron responses of the components of `C-B_+` and direct boundary contacts add as Laplacians. Therefore the global response satisfies

`c_st >= c_zs c_zt/A`.

PASS.

## 2. Port stress bound

Summing KKT equilibrium over `R` cancels all internal contact and diameter forces. The only crossing contact force has magnitude `A`. Every crossing diameter force has magnitude `D beta_h`, and the total crossing beta weight is at most `sum_H beta_h=1`. Hence

`A<=D`.

Therefore

`c_st>=c_zs c_zt/D`.

PASS.

## 3. Uniform leaf-pair diameter deficit

For two distinct diameter partners `a,b` of `z`, C18 gives

`angle azb<Theta_D<pi/3`

for the large-D regime. Hence

`1-|a-b|^2/D^2 > Gamma_D:=1-4 sin^2(Theta_D/2)>0`,

with `liminf Gamma_D>0`.

C41 gives exactly

`epsilon=sum_(s<t)c_st(1-|s-t|^2/D^2)`.

Restricting this nonnegative sum to leaf pairs and inserting the mesh inequality yields

`D epsilon >= (Gamma_D/2)[C_R^2-sum_a c_za^2]`,

where `C_R=sum_a c_za`.

PASS.

## 4. PSD transfer and aggregate error

C64 gives `M=Lambda-L_H` positive semidefinite and `tr M=2epsilon`. On a diameter edge `za`,

`M_za=beta_za-c_za`.

A `2x2` PSD principal minor gives

`|beta_za-c_za|<=sqrt(M_zz M_aa)<=epsilon`.

The Hopf-Pannwitz / hull bound gives `|H|<=pi D`. Thus the aggregate discrepancy over any star subset is at most `pi D epsilon`, which is `o(1)` in the phase `D epsilon->0`.

PASS.

## 5. Herfindahl implication

In C71-B the beta star mass in the single-port component satisfies `w_R->1`. Section 4 gives `C_R->1`. Therefore C98's aggregate inequality implies

`sum_a(c_za/C_R)^2->1`.

For nonnegative `p_a` with sum one,

`sum p_a^2 <= max p_a`.

Hence one response edge has weight `1-o(1)`, and the per-edge PSD transfer gives one actual diameter edge with `beta=1-o(1)`.

This fixes the invalid inference in the first C98 draft, where only the second-largest leaf was controlled. The current aggregate version also excludes diffuse mass over `Theta(D)` individually small leaves.

PASS.

## 6. Scope

C98 applies only to C71-B, where the dominant star mass lies in a component attached to `z` by exactly one physical contact. It does not address C71-A multi-port return components. It also does not turn `beta_za=1-o(1)` into an exact C76 chain on a finite source.

Audited conclusion:

> In every C71-B sequence with `D epsilon->0`, one actual diameter edge carries `1-o(1)` of the normalized KKT diameter mass; equivalently the star-cancellation scalar `chi_z` tends to zero and C81's source-to-leaf flow uses `D^2-o(D^2)` total contact-capacity mass.
