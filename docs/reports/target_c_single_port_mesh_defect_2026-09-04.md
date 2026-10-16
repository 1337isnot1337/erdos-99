<!-- theorem-state: {"artifact_id":"ART-91AA5C6604B1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C98 candidate: single-port mesh defect forces one-leaf concentration

**Date:** 2026-09-04
**Repository base:** branch after C97 (`0e5ab9ca`)
**Run type:** exact Schur-complement / KKT cut theorem
**Target:** C71-B near-zero single-port phase
**Depends on:** C41 response-defect identity; C64 PSD domination; C18 shared-endpoint diameter-angle gap; C65 full visibility; C71 single-port decomposition
**Status:** proved working result; audit pending
**LEVEL I STATUS:** STILL OPEN

C71 leaves a near-zero branch in which one component `R` of `C-z` carries almost all of the `z`-star KKT mass through one physical contact edge `e=zx`. C98 shows that this component cannot carry diffuse star mass when `D epsilon ->0`: one `z`-star diameter edge must carry `1-o(1)` of the normalized beta mass.

The mechanism is an exact Schur-complement inequality. Eliminating the unique physical port creates unavoidable leaf-leaf Kron conductance proportional to every product `c_za c_zb`. KKT cut equilibrium bounds the port stress by `D`, while C18 makes every pair of distinct `z`-diameter leaves uniformly subdiametral. Summing C41 over all leaf pairs gives a Herfindahl concentration inequality.

---

## 1. Setup

Work in the C65 lexicographically normalized triangle-free C-II source. Let

`epsilon = sum_(b<k) c_bk - 1 = tr(Lambda-L_H)/2 >0`

be the C41/C64 response defect, where `c_bk=-Lambda_bk` are boundary response conductances and `sum_H beta_h=1`.

Fix a diameter vertex `z`. Delete `z` from the contact graph. Let `R` be a connected component attached back to `z` by exactly one contact edge

`e=zx`,

of KKT contact stress

`A=alpha_zx>0`.

Let `B_R` be the loaded diameter endpoints lying in `R`.

If `x` itself is a loaded boundary terminal, then `zx` is a direct loaded-loaded unit contact. C41.14 gives

`epsilon >= A(1-1/D^2)`.

In the C71-B phase `A=Omega(D)`, this already contradicts `D epsilon ->0`. Hence the near-zero survivor has `x notin B_+`; the nontrivial argument below assumes this case.

## 2. Exact single-port Schur complement

Consider the electrical contact subnetwork on `R union {z}`. Temporarily treat

`{x} union B_R`

as Dirichlet boundary and eliminate all other unpinned vertices of `R`. Write its response conductances as

`d_xt >=0` for `t in B_R`,

and `d_st>=0` for distinct `s,t in B_R`. Put

`d_x = sum_(t in B_R) d_xt`.

Now attach the physical edge `zx` of conductance `A` and eliminate `x`. Since `R` has no other contact edge to the rest of the contact graph, this is exactly the contribution of `R` to the global response on `{z} union B_R`.

The one-vertex Schur complement gives

`c_zt = A d_xt/(A+d_x)`

and, for distinct `s,t in B_R`,

`c_st = d_st + d_xs d_xt/(A+d_x)`.

Therefore

`c_st >= d_xs d_xt/(A+d_x)`.

Using the formulas for `c_zs,c_zt`,

`d_xs d_xt/(A+d_x)
 = c_zs c_zt (A+d_x)/A^2
 >= c_zs c_zt/A`.

### Theorem C98.1 — single-port mesh inequality

For any two distinct loaded terminals `s,t` in a single-port component `R`,

`c_st >= c_zs c_zt/A`.

No planarity or asymptotics are used here; this is an exact Kron-reduction identity plus positivity.

## 3. The physical port stress is at most `D`

Sum the KKT equilibrium equations over all source vertices in `R`. Every internal contact force cancels. The only contact force crossing the cut is the port force of magnitude `A`.

Every diameter reaction crossing the cut has Euclidean magnitude `D beta_h`. The total beta weight of all crossing diameter edges is at most the globally normalized mass `1`. Hence

`A <= D`.

Combining with C98.1 gives

### Corollary C98.2

`c_st >= c_zs c_zt/D`.

## 4. Star leaves are uniformly subdiametral

Let

`L_R={a in R: za in H}`

be the `z`-star leaves in `R`. For distinct `a,b in L_R`, C18 gives

`angle azb < Theta_D < pi/3`

for `D>=20`. Thus

`|a-b|/D < 2 sin(Theta_D/2)`.

Define

`Gamma_D = 1 - 4 sin^2(Theta_D/2) >0`.

Then

`1-|a-b|^2/D^2 > Gamma_D`.

Moreover

`Gamma_D -> Gamma_infty
 = 1-4 sin^2((5pi/6-sqrt(3))/2) >0`.

C41.17 gives

`epsilon = sum_(s<t) c_st (1-|s-t|^2/D^2)`.

Restrict to unordered pairs of leaves in `L_R`, then use C98.2:

`epsilon
 >= Gamma_D sum_(a<b in L_R) c_ab
 >= (Gamma_D/D) sum_(a<b in L_R) c_za c_zb`.

Put

`C_R = sum_(a in L_R) c_za`.

Since

`sum_(a<b) c_za c_zb
 = (C_R^2-sum_a c_za^2)/2`,

we obtain the aggregate form.

### Theorem C98.3 — single-port Herfindahl defect

`D epsilon
 >= (Gamma_D/2)
    [ C_R^2 - sum_(a in L_R) c_za^2 ].`

Equivalently, if `p_a=c_za/C_R` when `C_R>0`, then

`1-sum_a p_a^2
 <= 2D epsilon/(Gamma_D C_R^2)`.

Thus a near-zero single-port response star has Herfindahl index tending to one whenever `C_R` stays bounded away from zero.

## 5. Response conductance is close to beta on each diameter edge

C64 gives

`M=Lambda-L_H >=0`

in PSD order, with

`tr M=2 epsilon`.

On a diameter edge `za`,

`M_za = beta_za-c_za`.

PSD of the `z,a` principal minor gives

`|beta_za-c_za|
 <= sqrt(M_zz M_aa)
 <= (M_zz+M_aa)/2
 <= epsilon`.

Hence every star edge satisfies

`|beta_za-c_za|<=epsilon`.

The planar diameter-edge bound gives

`|H|<=pi D`.

Therefore for any set of star leaves,

`| sum beta_za - sum c_za |
 <= pi D epsilon`.

In particular, under `D epsilon->0`, aggregate response star mass and aggregate beta star mass agree up to `o(1)`.

## 6. C71-B collapses to one leaf

In C71-B there is one single-port component `R` with beta star mass

`w_R=sum_(a in L_R) beta_za ->1`.

By Section 5,

`C_R ->1`.

C98.3 and `D epsilon->0` then give

`sum_(a in L_R) (c_za/C_R)^2 ->1`.

For nonnegative numbers summing to one, `sum p_a^2->1` implies `max p_a->1`: indeed

`sum p_a^2 <= (max p_a) sum p_a = max p_a`.

Hence there is one leaf `a_*` such that

`c_(z a_*) ->1`.

Section 5 then gives

`beta_(z a_*) ->1`.

### Theorem C98.4 — one-leaf concentration in C71-B

Along every C71-B sequence with

`D epsilon ->0`,

one actual diameter edge `z a_*` carries

`beta_(z a_*)=1-o(1)`.

Thus the single-port near-zero branch is asymptotically a one-leaf diameter stress, not merely a star stress.

The C81 cancellation scalar

`chi_z = S_z-|g_z|/D`

therefore satisfies

`chi_z->0`.

Consequently C81.15 sharpens to an almost fully saturated source-to-leaf contact flow:

`sum_e |f_e| = D^2-o(D^2)`

for a flow ending overwhelmingly at the single leaf `a_*`.

## 7. Finite quantitative form

C98.3 also gives a direct largest-response-edge estimate. Since

`sum_a c_za^2 <= (max_a c_za) C_R`,

we have

`D epsilon
 >= (Gamma_D/2) C_R(C_R-max_a c_za)`.

Therefore

`max_(a in L_R) c_za
 >= C_R - 2D epsilon/(Gamma_D C_R)`

whenever `C_R>0`.

After the per-edge PSD transfer,

`max_(a in L_R) beta_za
 >= C_R - 2D epsilon/(Gamma_D C_R) - epsilon`.

This is the explicit stability statement needed for later rate bookkeeping.

## 8. What remains

C98 closes the diffuse/multi-leaf escape inside C71-B.

The live near-zero phases become:

1. **C71-A return/multi-port phase:** one component attached to `z` by at least two contact edges carries nonvanishing star mass. C98 does not apply because there is no unique physical port to eliminate.
2. **one-leaf single-port phase:** one diameter edge has `beta=1-o(1)` and C81 supplies an almost fully saturated depth-`D` contact flow. The exact endpoint of this degeneration is C76's straight-chain face, which C97 excludes in the pure rhombic train regime. The missing theorem is quantitative stability from near-saturated one-leaf flow to a forbidden near-chain geometry.

The important improvement is that genuine angular cancellation or diffuse mass among many tiny star leaves is no longer an obstruction in C71-B.
