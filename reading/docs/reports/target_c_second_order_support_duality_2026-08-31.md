> Generated reading edition · [exact source](../../../docs/reports/target_c_second_order_support_duality_2026-08-31.md) · source SHA-256 `2a40475c15bd650f6c9f203f2a2298c7f83e9fd84036ed046fb0650841f30213`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1B21202463A8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: second-order support duality

**Date:** 2026-08-31  
**Repository base:** `ee50a9db` (main after C61 / PR #63)  
**Run type:** exact second-order Farkas duality  
**Target:** Target C Gate C-I  
**Depends on:** C6 first-order support duality, C13.3 direction-dependent second-order stress, C53-C54 universal PSD, C57-C61 null-body integration

## LEVEL I STATUS

**STILL OPEN.**

The remaining C-I issue after C61 was phrased as support saturation of the exposed face annihilating the entire strong-flex space. That formulation is stronger than necessary and is not valid as a purely convex-PSD principle.

For the actual contact-minimal contradiction, fix one relative-interior weak-release velocity `v`. Its **zero-energy KKT face** is the correct object. Universal PSD gives an exact second-order analogue of C6:

- the fixed-diameter second-order acceleration inequalities are feasible;
- a strong row is forced to second-order equality for every feasible acceleration if and only if it appears with positive multiplier in some zero-energy KKT stress for `v`;
- every other strong row can be made strictly feasible simultaneously at second order.

Thus the support union of the zero-energy face is not something that must be artificially enlarged to all strong rows. It is exactly the true second-order frozen support. The residual strong rows already have strict quadratic slack in one common acceleration certificate.

Moreover all of C57-C61 applies to this larger velocity-specific zero face, not only to C54's smaller face annihilating every flex. Hence the only remaining C-I issue is a precise jet-stitching problem: combine the exact common-hinge finite motion on the second-order frozen support with the strict second-order acceleration on its complement.

## 1. Signed second-order acceleration system

Fix

```math
v\in\operatorname{ri}\mathcal K_D(A).
\tag{C62.1}
```

By C6, every strong row has zero first variation and every weak row has strict first variation. Weak rows therefore need no second-order condition for sufficiently small positive time.

Let `R_*` be the signed rigidity matrix on the strong active set `E_*=C_* union H_*`, with rows

```math
R_e a=(p_i-p_j)\cdot(a_i-a_j)
\qquad(e=ij\in C_*),
\tag{C62.2}
```

and

```math
R_h a=-(p_i-p_j)\cdot(a_i-a_j)
\qquad(h=ij\in H_*).
\tag{C62.3}
```

For the quadratic jet

```math
p_i(t)=p_i+t v_i+\frac{t^2}{2}a_i,
\tag{C62.4}
```

the coefficient of `t^2` in the squared-distance constraint is feasible exactly when

```math
R_ea\ge -|v_i-v_j|^2
\qquad(e=ij\in C_*),
\tag{C62.5}
```

and

```math
R_ha\ge |v_i-v_j|^2
\qquad(h=ij\in H_*).
\tag{C62.6}
```

Define the right-hand side vector `b(v)` by

```math
b_e=-|v_i-v_j|^2\quad(e\in C_*),
\qquad
b_h=|v_i-v_j|^2\quad(h\in H_*),
\tag{C62.7}
```

and the second-order acceleration polyhedron

```math
\boxed{
\mathcal A_2(v)=\{a:R_*a\ge b(v)\}.
}
\tag{C62.8}
```

For `a in A_2(v)` put

```math
\rho_e(a)=R_ea-b_e(v)\ge0.
\tag{C62.9}
```

These are the signed second-order slacks.

## 2. Universal PSD makes the acceleration system feasible

Let `lambda=(alpha,beta)>=0` satisfy

```math
R_*^{\mathsf T}\lambda=0.
\tag{C62.10}
```

Exactly as in C6, a nonzero such dependence must have positive total diameter coefficient: a nonzero nonnegative equilibrium dependence supported only on free contact forces is impossible by the generic extreme-vertex argument. Normalize

```math
\sum_H\beta_h=1.
```

Then `lambda` is a normalized KKT stress. Its pairing with the second-order right-hand side is

```math
\begin{aligned}
\lambda^{\mathsf T}b(v)
&=\sum_H\beta_h|v_i-v_j|^2
 -\sum_C\alpha_e|v_i-v_j|^2\\
&=-q_\lambda(v),
\end{aligned}
\tag{C62.11}
```

where

```math
q_\lambda(v)=\operatorname{tr}(V^{\mathsf T}\Omega_\lambda V).
```

C53-C54 give

```math
\Omega_\lambda\succeq0
```

for every normalized KKT stress, so

```math
\lambda^{\mathsf T}b(v)\le0.
\tag{C62.12}
```

Farkas' alternative for `R_*a>=b(v)` says infeasibility would produce a nonzero `lambda>=0` with

```math
R_*^{\mathsf T}\lambda=0,
\qquad
\lambda^{\mathsf T}b(v)>0,
```

contradicting (C62.12).

### Theorem C62.1 (second-order acceleration feasibility)

For every relative-interior fixed-diameter critical velocity,

```math
\boxed{\mathcal A_2(v)\ne\varnothing.}
\tag{C62.13}
```

This is stronger than C13.3 in a different direction. C13.3 supplies one zero-energy dual stress; C62.1 says the entire fixed-diameter second-order primal inequality system is feasible because **all** normalized stresses have the PSD sign.

## 3. The velocity-specific zero-energy face

Define

```math
\mathcal Z(v)
=\{s\in\mathcal S:q_s(v)=0\},
\tag{C62.14}
```

where `S` is the normalized KKT polytope. Universal PSD makes `q_s(v)>=0` on all of `S`, while C13.3 gives at least one stress with `q_s(v)<=0`. Therefore

```math
\boxed{\mathcal Z(v)\text{ is a nonempty exposed face of }\mathcal S.}
\tag{C62.15}
```

Let

```math
E_2(v)=\bigcup_{s\in\mathcal Z(v)}\operatorname{supp}s.
\tag{C62.16}
```

A relative-interior point of `Z(v)` has support exactly `E_2(v)`.

Because every `Omega_s` is PSD,

```math
q_s(v)=0
\iff
\Omega_sV_x=\Omega_sV_y=0.
\tag{C62.17}
```

Thus every extreme point of `Z(v)` satisfies the C57 kernel hypothesis for this fixed velocity. All of the extreme-body, zero-transfer, shunt-collapse, and common-hinge integration results C57-C61 therefore apply verbatim with `Z(v)` in place of the smaller C54 face `F_0`.

## 4. Zero-energy support implies universal second-order equality

Take `s=(alpha,beta) in Z(v)` and any `a in A_2(v)`. Since `lambda^T R_*=0`,

```math
\begin{aligned}
\sum_{e\in E_*}\lambda_e\rho_e(a)
&=\lambda^{\mathsf T}(R_*a-b(v))\\
&=-\lambda^{\mathsf T}b(v)\\
&=q_s(v)=0.
\end{aligned}
\tag{C62.18}
```

Every term is nonnegative. Hence

```math
\lambda_e>0
\Longrightarrow
\rho_e(a)=0
\quad\text{for every }a\in\mathcal A_2(v).
\tag{C62.19}
```

Therefore every row in `E_2(v)` is second-order frozen.

## 5. Universal equality implies zero-energy support

The converse is the important half.

Assume a strong row `e` satisfies

```math
\rho_e(a)=0
\qquad\text{for every }a\in\mathcal A_2(v).
\tag{C62.20}
```

The inequality

```math
-R_ea\ge-b_e(v)
\tag{C62.21}
```

is therefore valid on the nonempty polyhedron `R_*a>=b(v)`. By the valid-inequality form of Farkas' lemma, there is `mu>=0` such that

```math
\mu^{\mathsf T}R_*=-R_e,
\qquad
\mu^{\mathsf T}b(v)\ge-b_e(v).
\tag{C62.22}
```

Put

```math
\lambda=\mu+\mathbf e_e.
\tag{C62.23}
```

Then

```math
\lambda\ge0,
\qquad
R_*^{\mathsf T}\lambda=0,
\qquad
\lambda_e\ge1,
\qquad
\lambda^{\mathsf T}b(v)\ge0.
\tag{C62.24}
```

The nonzero dependence `lambda` has positive total diameter coefficient and can be normalized to a KKT stress. Universal PSD gives the reverse inequality

```math
\lambda^{\mathsf T}b(v)\le0.
```

Hence equality holds:

```math
\lambda^{\mathsf T}b(v)=0,
\qquad
q_\lambda(v)=0.
\tag{C62.25}
```

After normalization, `lambda in Z(v)` and has positive `e` coordinate. Thus

```math
e\in E_2(v).
```

Combining both directions gives the exact theorem.

### Theorem C62 (second-order support / acceleration duality)

For every strong active row `e`,

```math
\boxed{
e\in E_2(v)
\iff
\rho_e(a)=0\text{ for every }a\in\mathcal A_2(v).}
\tag{C62.26}
```

Equivalently, the support union of the velocity-specific zero-energy KKT face is exactly the set of active rows that are **unavoidably second-order tight** for the fixed release velocity.

This is the precise second-order counterpart of C6.6.

## 6. Simultaneous strict quadratic release outside the zero face

If `f notin E_2(v)`, Theorem C62 gives some feasible acceleration `a^(f)` with

```math
\rho_f(a^{(f)})>0.
```

There are finitely many such rows. Average the corresponding accelerations. Convexity of `A_2(v)` keeps the average feasible, and for each outside row one summand contributes positive slack while every other summand contributes nonnegative slack.

### Corollary C62.2 (simultaneous second-order strict release)

There exists one acceleration `a^circ in A_2(v)` such that

```math
\boxed{
\rho_e(a^\circ)=0\quad(e\in E_2(v)),
\qquad
\rho_e(a^\circ)>0\quad(e\in E_*\setminus E_2(v)).
}
\tag{C62.27}
```

Together with `v in ri K_D(A)`, the active hierarchy is now exact:

- weak rows: strict at first order;
- strong rows outside `E_2(v)`: zero at first order but strict at second order;
- rows in `E_2(v)`: zero at first and second order for every feasible acceleration.

## 7. Effect on the C57-C61 body machinery

Replace C54's global null face by `Z(v)`.

Every extreme point of `Z(v)` is an extreme normalized KKT stress and annihilates `v`. C57 makes its positive contact component a rigid body for this velocity. Convex mixtures stay in `Z(v)`, so C56-C61 apply unchanged:

1. different-motion extreme bodies have zero-transfer mixtures;
2. their zero-transfer diameter support is a bounded articulated star forest;
3. two-body hinges integrate;
4. three distinct hinges are impossible by C61's shunt-saturation argument;
5. all distinct motion classes share one source hinge and the whole **covered** `Z(v)` bouquet has an exact finite rotation path.

Thus the rows that genuinely require exact nonlinear treatment are exactly `E_2(v)`, and those rows already possess the common-hinge rigid-body description.

## 8. Exact remaining C-I lemma

C62 removes the need to prove that the zero face contains all strong support. Rows outside it are not frozen: they admit one common strict second-order acceleration.

The remaining issue is now a jet-stitching statement, not support saturation:

> **C63 jet stitching.** Combine the exact common-hinge finite rotation on the `E_2(v)` body bouquet with an acceleration having the strict slacks (C62.27), so that every row outside `E_2(v)` keeps its positive quadratic margin while every row in `E_2(v)` is preserved exactly.

A proof would produce a same-diameter finite path releasing all weak contacts and close Gate C-I.

The difficulty is precise. The acceleration `a^circ` from C62.2 need not equal the second derivative of the explicit rigid-body bouquet path on the covered vertices. A naive substitution can change an outside row's `t^2` coefficient. This mismatch must be repaired, not ignored.

## 9. Why the older support-saturation target was too strong

For a convex family of PSD matrices, an exposed zero-kernel face can omit coordinates that are positive elsewhere; abstract convexity alone does not force support saturation. The repository should therefore not promote a claim that `F_0` or `Z(v)` has maximal KKT support without additional geometry.

C62 gives the correct replacement: omitted rows are precisely the rows with genuine second-order slack available in the primal acceleration system.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C62.1:** universal PSD implies the complete fixed-diameter second-order acceleration system `R_*a>=b(v)` is feasible for every relative-interior release velocity.

**C62:** the union of supports of the zero-energy face `Z(v)` is exactly the set of rows forced to equality in every feasible acceleration.

**C62.2:** one acceleration makes every other strong row strict simultaneously at second order.

**Body effect:** C57-C61 apply to `Z(v)` itself, so all genuinely second-order-frozen rows lie in an exact common-hinge rigid-body bouquet.

**Only remaining C-I lemma:** stitch that exact bouquet path to the strict second-order acceleration without losing its quadratic margins.
