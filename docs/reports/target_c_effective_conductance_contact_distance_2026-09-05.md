<!-- theorem-state: {"artifact_id":"ART-EA7745BB8E36","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C effective-conductance / contact-distance bound

**Date:** 2026-09-05  
**Run type:** exact PSD / metric-energy theorem  
**Target:** extend C98 near-chain geometry beyond the pure-rhombic train model  
**Depends on:** C53 full selected-support PSD; C11 virial identity  
**LEVEL I STATUS:** STILL OPEN

## Theorem

Work in the fully force-visible C65/C53 branch with relative-interior normalized stress `(alpha,beta)`. Let `za` be any active diameter pair, let

`b=beta_za`,

and let

`k=d_C(z,a)`

be its unweighted distance in the positive unit-contact graph.

Then

`b <= D^2/k^2`.

Equivalently,

`k <= D/sqrt(b)`.

Since every contact path consists of unit edges joining points at Euclidean distance `D`, always `k>=D`.

Thus if `b=1-eta`,

`0<=k-D <= D(1/sqrt(1-eta)-1)`

`= (eta/2+O(eta^2))D`.

In particular, C98's `b=1-o(1)` conclusion forces

`d_C(z,a)=D+o(D)`

without any pure-rhombic hypothesis.

## 1. PSD domination lower-bounds effective conductance

C53 gives the full scalar quadratic-form domination

`L_C(alpha)-L_H(beta) >= 0`.

Therefore for every real vertex function `f`,

`E_C(f):=sum_(ij in C)alpha_ij(f_i-f_j)^2`

`>= sum_(hk in H)beta_hk(f_h-f_k)^2`.

Restrict to functions satisfying

`f_z=0`, `f_a=1`.

The diameter edge `za` alone contributes `b` on the right, and all other terms are nonnegative. Hence

`E_C(f)>=b`

for every such function.

The minimum of `E_C(f)` over `f_z=0,f_a=1` is the effective conductance between `z,a` in the contact network. Denote it by `C_eff(z,a)`. Thus

`C_eff(z,a)>=b`.                                      (1.1)

## 2. Graph distance upper-bounds effective conductance

Let

`d(v)=d_C(z,v)`.

Define the truncated distance potential

`f(v)=min{d(v),k}/k`.

Then

`f(z)=0`, `f(a)=1`.

Across every contact edge `ij`, graph distance changes by at most one, so

`|f_i-f_j|<=1/k`.

Therefore

`E_C(f)<= (1/k^2) sum_(ij in C)alpha_ij`.

The normalized virial identity gives

`sum_C alpha_ij=D^2`.

Hence

`C_eff(z,a)<=E_C(f)<=D^2/k^2`.                     (2.1)

Combine (1.1) and (2.1):

`b<=D^2/k^2`.

## 3. Near-geodesic path consequence

Choose a shortest contact path

`P:z=x_0,x_1,...,x_k=a`.

Orient its unit edge vectors as

`e_j=p_(x_j)-p_(x_(j-1))`.

With

`u=(p_a-p_z)/D`,

one has

`sum_j e_j=D u`.

Therefore the exact path identity is

`sum_(j=1)^k |e_j-u|^2=2(k-D)`.

Using `k<=D/sqrt(b)` gives

`sum_j |e_j-u|^2`

`<=2D(1/sqrt(b)-1)`.                                (3.1)

Thus `b=1-o(1)` gives a simple `z-a` contact path with

- `D+o(D)` edges;
- total squared directional defect `o(D)`;
- only `o(D)` edges outside any fixed angular cone around the diameter direction.

This recovers the path-level conclusion of the C99 train theorem at linear rather than quadratic defect scale, but it applies to arbitrary fully force-visible contact topology.

## 4. Comparison with C99-C100

In the pure-rhombic branch:

- C99 gives `k<=D/(2b-1)`;
- this theorem improves that to `k<=D/sqrt(b)` near `b=1`;
- C100 is much stronger there, giving `k-D=O(D(1-b)^2)` through coordinatewise train-angle stationarity.

The value of the present theorem is topology robustness: it does not require trains, rhombi, pseudolines, or simple connectivity.

## 5. Exact endpoint

If `b=1`, the theorem gives `k<=D`; Euclidean length gives `k>=D`, so `k=D`. Therefore a β-one full-support diameter edge forces an exact straight contact geodesic. The separate contact-direction energy theorem then shows all full-support positive contacts are parallel to that diameter and recovers the C19 contradiction.

## Handoff

```text
For every active diameter edge za of beta weight b in the C53 full-support branch:

  beta_za <= C_eff^contact(z,a) <= D^2/d_C(z,a)^2.

Hence

  d_C(z,a) <= D/sqrt(beta_za).

C98 beta=1-o(1) therefore gives a D+o(D) contact geodesic to the dominant leaf even outside the pure-rhombic train model.

Next target:
Use C35 degree constraints, C42 near-quadrangulation, or the C97 terminal-twist geometry to show that a fully force-visible triangle-free minimizer cannot contain such a near-geodesic diameter path with vanishing directional defect unless it pays a quantitative response/shell cost.
```