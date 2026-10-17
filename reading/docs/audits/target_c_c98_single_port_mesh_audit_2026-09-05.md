> Generated reading edition · [exact source](../../../docs/audits/target_c_c98_single_port_mesh_audit_2026-09-05.md) · source SHA-256 `1e40de41ae59fe0e9e6b121b04b78529aec34457b094980ec7c3ed3a14f99230`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-97B6DB4DA5FD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C C98 single-port mesh defect

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_c_single_port_mesh_defect_2026-09-05.md`  
**Verdict:** PASS.  
**LEVEL I status:** STILL OPEN.

## 1. Single-port Kron decomposition

Let `R` be a component of `C-z` attached to `z` by one contact `zx` of conductance `A`. With `{x} union B_R` held as boundary, eliminate the other interior vertices of `R`. The resulting response is a Laplacian with nonnegative conductances `d_xt,d_st`.

After adjoining `zx` and eliminating `x`, the one-vertex Schur complement gives

`c_zt=A d_xt/(A+d_x)`

and

`c_st=d_st+d_xs d_xt/(A+d_x)`.

Other contact components add response Laplacians and cannot lower these conductances. Hence globally

`c_st>=c_zs c_zt/A`.

PASS.

## 2. Port stress bound

Summing KKT equilibrium over `R` cancels all internal contact and diameter forces. The only crossing contact force has magnitude `A`; crossing diameter forces have total beta mass at most one, hence total resultant norm at most `D`. Therefore

`A<=D`,

and

`c_st>=c_zs c_zt/D`.

PASS.

## 3. Uniform leaf-pair diameter deficit

For two distinct diameter partners `a,b` of `z`, C18 gives

`angle azb<Theta_D<pi/3`

in the large-`D` regime. Hence

`1-|a-b|^2/D^2 > Gamma_D:=1-4 sin^2(Theta_D/2)>0`,

with `liminf Gamma_D>0`.

C41 gives exactly

`epsilon=sum_(s<t)c_st(1-|s-t|^2/D^2)`.

Restricting to leaf pairs and inserting the mesh inequality yields

`D epsilon >= (Gamma_D/2)[C_R^2-sum_a c_za^2]`.

PASS.

## 4. PSD transfer

C64 gives `M=Lambda-L_H` PSD and `tr M=2epsilon`. On diameter edge `za`,

`M_za=beta_za-c_za`.

A `2x2` principal minor gives

`|beta_za-c_za|<=sqrt(M_zz M_aa)<=epsilon`.

The planar diameter-edge bound is `O(D)`, so aggregate discrepancy over any star subset is `O(D epsilon)` and is `o(1)` when `D epsilon->0`.

PASS.

## 5. Herfindahl implication

In C71-B the beta star mass in the single-port component tends to one, so the corresponding response mass `C_R` tends to one. The aggregate inequality gives

`sum_a(c_za/C_R)^2->1`.

For nonnegative `p_a` summing to one,

`sum p_a^2<=max p_a`.

Thus one response edge has weight `1-o(1)`, and the PSD transfer makes the corresponding actual diameter beta weight `1-o(1)`.

PASS.

## 6. Scope

C98 applies only to C71-B. It does not address C71-A multi-port return components and does not itself turn near-one beta into an exact C76 chain.

Audited conclusion:

> In every C71-B sequence with `D epsilon->0`, one actual diameter edge carries `1-o(1)` of normalized KKT diameter mass. C81's source-to-leaf flow then uses `D^2-o(D^2)` total contact-capacity mass.
