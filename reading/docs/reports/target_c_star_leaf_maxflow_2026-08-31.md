> Generated reading edition · [exact source](../../../docs/reports/target_c_star_leaf_maxflow_2026-08-31.md) · source SHA-256 `0d8b45f74a966c6885904d5d1a799510c1c34f786d872b876c20bb891381f237`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2816E2CDB8F9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C81: arbitrary-cut star transport and max-flow saturation

**Date:** 2026-08-31  
**Repository base:** `e0a0b7cf` (main after C80 / PR #85)  
**Run type:** exact cut theorem / capacitated-flow reduction  
**Target:** Target C Gate C-II, C66 near-star phase  
**Depends on:** C11 equilibrium and `sum_C alpha=D^2`, C14/C18 diameter-star reaction cone, C66 stress-star concentration  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C72 proves a lower bound on the special contact cuts given by graph-distance balls around the C66 center. C81 upgrades this to **every** contact cut separating that center from all of its mechanically loaded diameter leaves. The improvement matters: internal nonstar diameter reactions cancel exactly when equilibrium is summed over an arbitrary vertex set, so the error is `D delta_z`, not `2D delta_z`.

Fix a diameter vertex `z` in the C65 full-support normalized stress. Write

```math
L_z:=\{k:zk\in H\},
\qquad
S_z:=\sum_{k\in L_z}\beta_{zk},
\qquad
\delta_z:=1-S_z,
```

and let

```math
g_z:=\sum_{k\in L_z}\beta_{zk}(p_z-p_k)
```

be its complete diameter reaction.

For every vertex set `U` in the positive contact core satisfying

```math
z\in U,
\qquad
U\cap L_z=\varnothing,
```

let

```math
\operatorname{cap}_\alpha(U)
:=
\sum_{\substack{ij\in C\\i\in U,\ j\notin U}}\alpha_{ij}.
```

### Theorem C81.1 — arbitrary star-separating cut bound

```math
\boxed{
\operatorname{cap}_\alpha(U)
\ge
|g_z|-D\delta_z.
}
\tag{C81.1}
```

Thus, with the contact stresses `alpha_e` used as edge capacities, the minimum cut separating `z` from the leaf set `L_z` has capacity at least

```math
F_z:=\bigl[|g_z|-D\delta_z\bigr]_+.
\tag{C81.2}
```

By max-flow/min-cut there is an undirected contact flow of value at least `F_z` from `z` to `L_z`.

Every contact path from `z` to a leaf has at least `D` unit edges. After cycle removal and path decomposition, any such flow therefore uses at least `DF_z` total edge-flow mass. Since each edge flow is bounded by `alpha_e` and C11 gives

```math
\sum_{e\in C}\alpha_e=D^2,
```

we obtain:

### Theorem C81.2 — diameter-length stress-flow saturation

There exists a `z`-to-`L_z` contact flow `f` satisfying

```math
\boxed{
\sum_{e\in C}|f_e|
\ge
D\,[|g_z|-D\delta_z]_+,
}
\tag{C81.3}
```

and hence

```math
\boxed{
\frac1{D^2}\sum_e|f_e|
\ge
\left[\frac{|g_z|}{D}-\delta_z\right]_+.
}
\tag{C81.4}
```

C14/C18 give

```math
|g_z|\ge c_DDS_z,
\qquad
c_D\longrightarrow c_\infty=0.90348\ldots .
```

Therefore

```math
\boxed{
\frac1{D^2}\sum_e|f_e|
\ge
\bigl[c_D-(1+c_D)\delta_z\bigr]_+.
}
\tag{C81.5}
```

At the C66 center,

```math
\delta_z\le C_0D\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0},
```

so the near-zero response phase `D epsilon->0` admits a diameter-leaf flow consuming asymptotically at least

```math
\boxed{c_\infty=0.90348\ldots}
```

of the entire normalized contact-stress budget in edge-flow mass.

The exact remaining scalar is the weighted cancellation of the star reaction. If

```math
\chi_z:=S_z-\frac{|g_z|}{D},
```

then C81.4 becomes

```math
\frac1{D^2}\sum_e|f_e|
\ge 1-2\delta_z-\chi_z.
\tag{C81.6}
```

Thus a near-chain certificate has only two ways not to saturate essentially all of `D^2`: nonstar diameter mass `delta_z`, already controlled by C66, or genuine angular cancellation `chi_z` among the star spokes.

---

## 1. Sum equilibrium over an arbitrary vertex set

For every contact-core vertex `v`, KKT equilibrium is

```math
\sum_{vw\in C}\alpha_{vw}(p_v-p_w)
=
\sum_{vh\in H}\beta_{vh}(p_v-p_h).
\tag{C81.7}
```

Fix `U` with `z in U` and `U cap L_z=emptyset`. Sum C81.7 over `v in U`.

Every contact edge internal to `U` cancels, as does every diameter edge with both endpoints in `U`. Therefore

```math
\sum_{\substack{ij\in C\\i\in U,j\notin U}}
\alpha_{ij}(p_i-p_j)
=
\sum_{\substack{ij\in H\\i\in U,j\notin U}}
\beta_{ij}(p_i-p_j),
\tag{C81.8}
```

where each crossing edge is oriented from `U` to its complement.

Every star edge `zk`, `k in L_z`, crosses this cut, and their vector sum is exactly `g_z`. All remaining crossing diameter edges are nonstar edges. Their total beta weight is at most `delta_z`, and each has Euclidean length `D`. Hence

```math
\left|
\sum_{\substack{ij\in H\\i\in U,j\notin U}}
\beta_{ij}(p_i-p_j)-g_z
\right|
\le D\delta_z.
\tag{C81.9}
```

Taking norms in C81.8 and then using the triangle inequality on the contact side gives

```math
\operatorname{cap}_\alpha(U)
\ge
\left|
\sum_{\substack{ij\in C\\i\in U,j\notin U}}
\alpha_{ij}(p_i-p_j)
\right|
\ge |g_z|-D\delta_z.
```

This proves C81.1.

### Comparison with C72

C72 bounded the error on graph-distance balls by `2D delta_z` because it bounded the sum of individual nonstar endpoint reactions. C81 instead sums the equilibrium equations first. Every nonstar diameter edge internal to `U` cancels exactly, and a crossing nonstar edge appears only once. The sharp bookkeeping error is therefore `D delta_z`.

---

## 2. Max-flow/min-cut on the positive contact graph

Give every undirected positive contact edge `e` capacity `alpha_e`. Add a formal sink `t` and connect every leaf `k in L_z` to `t` with infinite capacity.

A finite `z`-`t` cut is exactly a vertex set `U` with

```math
z\in U,
\qquad
U\cap L_z=\varnothing.
```

By C81.1 every such cut has capacity at least `F_z`. The finite real-capacity max-flow/min-cut theorem therefore supplies a flow of value at least `F_z` from `z` to the star leaf set.

Choose one of value exactly `F_z` if the maximum is larger. Replace any antiparallel use of one undirected edge by its net direction and remove flow cycles. The resulting flow decomposes into finitely many simple `z`-to-leaf paths `P` with nonnegative path weights `x_P` such that

```math
\sum_P x_P=F_z.
\tag{C81.10}
```

If `m(P)` is the number of contact edges in `P`, then all edges have Euclidean length one while the path endpoint is a diameter partner of `z`. Hence

```math
D
=|p_z-p_k|
\le m(P).
\tag{C81.11}
```

Therefore the total absolute edge-flow mass is

```math
\begin{aligned}
\sum_e|f_e|
&=\sum_P x_Pm(P)\\
&\ge D\sum_Px_P\\
&=DF_z.
\end{aligned}
```

This proves C81.3.

Because `|f_e|<=alpha_e`, C11 also gives the consistency bound

```math
DF_z
\le\sum_e|f_e|
\le\sum_e\alpha_e
=D^2.
\tag{C81.12}
```

---

## 3. Reaction cancellation is the only constant-fraction loss

Normalize the center reaction by

```math
j_z:=\frac{|g_z|}{D}.
```

Then C81.4 says the transport fraction is at least `j_z-delta_z`.

Since the star coefficients have total mass `S_z=1-delta_z`, define

```math
\chi_z:=S_z-j_z\ge0.
\tag{C81.13}
```

The nonnegativity is just the triangle inequality applied to the weighted unit spoke directions. Substitution gives

```math
j_z-\delta_z
=S_z-\chi_z-\delta_z
=1-2\delta_z-\chi_z,
```

which proves C81.6.

Thus:

- `delta_z` measures mechanical beta mass outside the C66 star;
- `chi_z` measures vector cancellation inside the star itself;
- once both are small, almost the **entire** `D^2` contact-stress budget must be usable as a diameter-length source-to-leaf flow.

C18 gives the unconditional cancellation bound

```math
j_z\ge c_DS_z,
```

hence

```math
\chi_z\le(1-c_D)S_z.
\tag{C81.14}
```

This yields C81.5 and the asymptotic `0.90348...` fraction without assuming single-spoke concentration.

---

## 4. Equality and near-equality meaning

If `delta_z=0` and `chi_z=0`, then `F_z=D`. C81.12 forces equality everywhere:

```math
\sum_e|f_e|=\sum_e\alpha_e=D^2.
```

Every positive-flow path has exactly `D` unit edges and therefore is a straight Euclidean geodesic from `z` to its leaf. There can be no unused positive contact capacity in the selected stress. C76-C80 identify the resulting exact face as the single straight chain and its `D`-track train atom.

C81 supplies a stable version of the capacity half of that picture. Define the flow-capacity slack

```math
\mathcal S_f:=
D^2-\sum_e|f_e|.
```

Then there exists a star-leaf flow with

```math
\boxed{
\mathcal S_f
\le
D^2(2\delta_z+\chi_z).
}
\tag{C81.15}
```

This does not yet imply geometric closeness to one chain when `chi_z` is a fixed constant. It isolates `chi_z` as the only constant-order obstruction after C66.

---

## 5. Pure-rhombic train interpretation

In a pure simply connected rhombic disk, every contact edge has one train label. For the C81 flow put

```math
f_\tau:=
\sum_{e\text{ of train }\tau}|f_e|,
\qquad
A_\tau:=
\sum_{e\text{ of train }\tau}\alpha_e.
```

Then

```math
0\le f_\tau\le A_\tau
```

and

```math
\boxed{
\sum_\tau f_\tau
=
\sum_e|f_e|
\ge
D^2(1-2\delta_z-\chi_z).
}
\tag{C81.16}
```

The Target B virtual-work identity gives

```math
A_\tau
=
\sum_{h\in H}\beta_h\lambda_{h\tau}.
\tag{C81.17}
```

Therefore C81 produces a concrete capacitated transport measure on the same train set on which Sections 40--43 analyze first- and higher-order diameter blocking.

At the exact C80 chain face, `delta_z=chi_z=0`, and C81.16 is saturated by the `D` parallel chain tracks. In a near-face sequence, the missing theorem can now be stated as a stability problem for the pair `(f_tau,A_tau)`, not merely for abstract train directions.

---

## 6. What C81 does not prove

The unconditional reaction-cone bound only gives

```math
1-2\delta_z-\chi_z
\ge
c_D-(1+c_D)\delta_z,
```

whose limiting constant is `c_infty=0.90348...`, not one. Roughly `9.65%` of the total stress budget can still remain outside the guaranteed flow even when `delta_z->0`.

That constant slack is enough to support a mechanically light but geometrically macroscopic transverse rhombic medium. Therefore C81 alone does not close C-II.

The next exact split is now clear:

1. **small cancellation:** `chi_z=o(1)`. Then C81 gives almost complete stress-flow saturation, and C80 suggests a uniform spectral/geodesic stability theorem toward the `D`-track chain atom;
2. **macroscopic cancellation:** `chi_z>=eta>0`. Then a nonvanishing fraction of beta mass is angularly spread among star spokes. One must convert that weighted spoke spread into either C68 angular contact cost, a C66 response defect, or a Target B train-angle blocker.

This is sharper than treating every near-star stress by the same argument.

## Compact handoff

For every contact cut `U` containing the C66 center `z` and excluding all of its diameter leaves,

`cap_alpha(U) >= |g_z|-D(1-S_z)`.

Hence there is a contact max flow from `z` to the star leaf set of value at least that quantity. Every source-to-leaf path has at least `D` unit edges, so some such flow has total edge-flow mass at least

`D[|g_z|-D(1-S_z)]`.

Writing

`delta_z=1-S_z`,
`chi_z=S_z-|g_z|/D`,

there is a flow consuming at least

`(1-2delta_z-chi_z)D^2`

of contact-capacity mass. C18 gives the unconditional near-zero lower fraction `c_infty=0.90348...`.

**Status:** open. The remaining constant-fraction obstruction is exactly weighted star-reaction cancellation `chi_z`; when `chi_z=o(1)`, C81 is a stable capacity precursor to C80's exact chain/train atom.
