> Generated reading edition · [exact source](../../../docs/reports/target_c_single_port_mesh_defect_2026-09-05.md) · source SHA-256 `56dd84aa897f7c0a38640620719c230b8a43459597701caa2c0e72a6234a65c6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-72F84527FA8A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C98: single-port mesh defect forces one-leaf concentration

**Date:** 2026-09-05  
**Run type:** exact Schur-complement / KKT cut theorem  
**Target:** C71-B near-zero single-port phase  
**Depends on:** C41 response-defect identity; C64 PSD domination; C18 shared-endpoint diameter-angle gap; C65 full visibility; C71 single-port decomposition  
**Audit:** `docs/audits/target_c_c98_single_port_mesh_audit_2026-09-05.md`  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

Let

`epsilon = sum_(b<k) c_bk - 1 = tr(Lambda-L_H)/2 >0`

be the C41/C64 response defect. Fix a diameter vertex `z`, delete `z` from the positive contact graph, and let `R` be a connected component attached back to `z` by exactly one contact edge

`e=zx`

of contact stress `A=alpha_zx>0`. Let `B_R` be the loaded diameter endpoints in `R`.

If `x` is itself a loaded boundary terminal, C41.14 gives

`epsilon >= A(1-1/D^2)`.

In the C71-B phase `A=Omega(D)`, so this is incompatible with `D epsilon->0`. Hence the near-zero survivor has `x notin B_+`.

## 2. Single-port Schur complement

Hold `{x} union B_R` as Dirichlet boundary in the subnetwork `R`, eliminate the other vertices, and write its response conductances as `d_xt` and `d_st`. Put

`d_x=sum_(t in B_R)d_xt`.

Attach the physical edge `zx` of conductance `A` and eliminate `x`. The one-vertex Schur complement gives

`c_zt=A d_xt/(A+d_x)`

and, for distinct `s,t in B_R`,

`c_st=d_st+d_xs d_xt/(A+d_x)`.

Therefore

`c_st >= d_xs d_xt/(A+d_x) >= c_zs c_zt/A`.

### Theorem C98.1 — single-port mesh inequality

For distinct loaded terminals `s,t` in a single-port component,

`c_st >= c_zs c_zt/A`.

## 3. Port stress bound

Sum KKT equilibrium over all vertices of `R`. Internal contact and diameter forces cancel. The unique crossing contact force has magnitude `A`; all crossing diameter reactions have total norm at most

`D sum_H beta_h=D`.

Hence

`A<=D`,

so

`c_st>=c_zs c_zt/D`.

## 4. Uniform leaf-pair deficit

Let

`L_R={a in R: za in H}`.

For distinct `a,b in L_R`, C18 gives

`angle azb<Theta_D<pi/3`

for large `D`. Define

`Gamma_D=1-4 sin^2(Theta_D/2)>0`.

Then

`1-|a-b|^2/D^2>Gamma_D`,

with `liminf Gamma_D>0`.

C41 gives exactly

`epsilon=sum_(s<t)c_st(1-|s-t|^2/D^2)`.

Restricting to star-leaf pairs and using the mesh inequality gives

`epsilon >= (Gamma_D/D) sum_(a<b in L_R)c_za c_zb`.

Put

`C_R=sum_(a in L_R)c_za`.

Since

`sum_(a<b)c_za c_zb=(C_R^2-sum_a c_za^2)/2`,

we obtain:

### Theorem C98.2 — single-port Herfindahl defect

`D epsilon >= (Gamma_D/2)[C_R^2-sum_(a in L_R)c_za^2]`.

Equivalently, for `p_a=c_za/C_R`,

`1-sum_a p_a^2 <= 2D epsilon/(Gamma_D C_R^2)`.

## 5. Response-to-beta transfer

C64 gives

`M=Lambda-L_H >=0`, `tr M=2epsilon`.

On a diameter edge `za`,

`M_za=beta_za-c_za`.

A `2x2` PSD principal minor gives

`|beta_za-c_za|<=sqrt(M_zz M_aa)<=epsilon`.

Since the complete planar diameter graph has `O(D)` edges, aggregate beta and response mass on any star subset differ by `O(D epsilon)`.

## 6. C71-B collapses to one leaf

In C71-B, one single-port component `R` carries beta star mass

`w_R=sum_(a in L_R)beta_za ->1`.

Under `D epsilon->0`, Section 5 gives `C_R->1`. C98.2 then gives

`sum_a(c_za/C_R)^2->1`.

For nonnegative `p_a` summing to one,

`sum p_a^2<=max p_a`,

so one leaf `a_*` has

`c_(za_*)->1`.

The per-edge PSD transfer gives

`beta_(za_*)->1`.

### Theorem C98 — one-leaf concentration

Along every C71-B sequence with

`D epsilon->0`,

one actual diameter edge carries

`beta_(za_*)=1-o(1)`.

Equivalently the C81 star-cancellation scalar tends to zero, and the source-to-leaf contact flow uses `D^2-o(D^2)` total contact-capacity mass.

## 7. Finite quantitative form

From

`sum_a c_za^2 <= (max_a c_za)C_R`,

C98.2 yields

`max_a c_za >= C_R - 2D epsilon/(Gamma_D C_R)`.

Thus

`max_a beta_za >= C_R - 2D epsilon/(Gamma_D C_R) - epsilon`.

## 8. Scope

C98 eliminates diffuse/multi-leaf mass only in C71-B, where the dominant component has one physical port to `z`. It does not exclude the C71-A multi-port return phase, and it does not turn `beta_za=1-o(1)` into the exact C76 chain on a finite source.

Combined with C97, the live near-zero split is:

1. a multi-port return component carries nonvanishing star mass; or
2. one actual diameter edge has beta `1-o(1)` and approaches the exact chain geometry that C97 forbids at equality.
