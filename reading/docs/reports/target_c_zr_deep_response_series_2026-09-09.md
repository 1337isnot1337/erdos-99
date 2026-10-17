> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_deep_response_series_2026-09-09.md) · source SHA-256 `ce9b3ab18a0cc3136e812b62f95961c01d0dec8db9eed6dac7d346cbdc5ccb1f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C5D7A1E6F156","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHS: deep harmonic response forces a non-tiny bridge series

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / electrical series estimate  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** revised ZHC and positive contact-network response  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The revised ZHC theorem produces, in the bridge-dominant near-zero phase, one unloaded harmonic component `I_*` and an actual diameter pair `a,b in A_*` with

$$
\ell(a b)\ge\eta D/2,
\qquad
c_{ab}^{(*)}\ge\frac{p_\eta}{36\pi D},
\tag{1.1}
$$

where

$$
p_\eta=\frac{\eta}{4\pi-\eta}.
\tag{1.2}
$$

Every physical contact bridge on the global `a--b` bridge-tree route lies in the closure of `I_*`.

This report proves that the route cannot consist mostly of arbitrarily small positive bridge stresses. The transfer conductance `c_ab^(*)` bounds the sum of reciprocal bridge stresses in exact electrical series.

The proof below uses nested bridge cuts and the maximum principle. It does **not** assume that voltage is monotone along an arbitrary graph path.

---

## 1. Component Dirichlet problem

Let `N_*` be the weighted contact subnetwork consisting of `I_*`, its attachment set `A_*`, and every contact edge internal to or incident with `I_*`. Edge conductances are the KKT contact stresses `alpha_e>0`.

Prescribe boundary values

$$
V_b=1,
\qquad
V_s=0\quad(s\in A_*\setminus\{b\}),
\tag{1.3}
$$

and let `V` be the harmonic extension to `I_*`.

The maximum principle gives

$$
0\le V_x\le1
\qquad(x\in V(N_*)).
\tag{1.4}
$$

The current absorbed at attachment `a` has magnitude exactly

$$
c_{ab}^{(*)},
\tag{1.5}
$$

because

$$
(\Lambda^{(*)}V)_a
=
\Lambda^{(*)}_{ab}
=-c_{ab}^{(*)}.
$$

---

## 2. Every separating bridge carries at least the transfer current to `a`

Let `e=uv` be a physical contact bridge on the global bridge-tree route from `b` to `a`, oriented from the `b` side toward the `a` side. Revised ZHC proves `e in E_*`, so `e` is an edge of `N_*`.

Delete `e` from the complete contact graph. Let `S_e` be the side containing `a`; it does not contain `b`. Since `e` is a global contact bridge, every contact path from `b` to `a`, in particular every path inside `N_*`, crosses `e`.

Sum Kirchhoff current balance over all interior vertices of `N_* cap S_e`. Internal currents cancel. The current through `e` equals the total current absorbed at the zero-voltage attachments lying on the `a` side. For each such attachment `s`,

$$
-(\Lambda^{(*)}V)_s
=c_{sb}^{(*)}\ge0.
\tag{2.1}
$$

Since `a` is one of them,

$$
\boxed{
I_e
=\sum_{s\in A_*\cap S_e}c_{sb}^{(*)}
\ge c_{ab}^{(*)}.
}
\tag{2.2}
$$

Ohm's law gives the oriented bridge drop

$$
V_u-V_v
=\frac{I_e}{\alpha_e}
\ge\frac{c_{ab}^{(*)}}{\alpha_e}>0.
\tag{2.3}
$$

---

## 3. Successive bridge drops are genuinely in series

Order the physical bridges on the `b--a` bridge-tree route as

$$
e_1=u_1v_1,\ldots,e_L=u_Lv_L,
\tag{3.1}
$$

from `b` toward `a`, each oriented so `u_j` lies on the `b` side and `v_j` on the `a` side.

The bridge sides are nested. After deleting `e_j`, the side containing `a` also contains every later bridge `e_{j+1},...,e_L` and contains no boundary attachment with prescribed voltage one: the unique such terminal is `b`, on the opposite side.

Restrict the harmonic solution to this `a`-side subnetwork and treat `v_j` as an additional boundary vertex with value `V_{v_j}`. Every original attachment boundary value inside is zero. The maximum principle therefore gives

$$
V_x\le V_{v_j}
\qquad
\text{for every vertex }x\text{ on the }a\text{ side of }e_j.
\tag{3.2}
$$

In particular,

$$
V_{u_{j+1}}\le V_{v_j}.
\tag{3.3}
$$

Together with the positive bridge drops (2.3),

$$
1=V_b
\ge V_{u_1}>V_{v_1}
\ge V_{u_2}>V_{v_2}
\ge\cdots\ge
V_{u_L}>V_{v_L}\ge V_a=0.
\tag{3.4}
$$

Hence the bridge drops themselves telescope below the full boundary drop:

$$
\sum_{j=1}^L(V_{u_j}-V_{v_j})\le1.
\tag{3.5}
$$

Using (2.3) termwise proves the exact series theorem.

### Theorem ZHS — bridge-series transfer bound

For every positive harmonic-component response pair `a,b`,

$$
\boxed{
 c_{ab}^{(*)}
 \sum_{e\in P_{br}(a,b)}\frac1{\alpha_e}
 \le1.
}
\tag{ZHS1}
$$

Equivalently,

$$
\boxed{
\sum_{e\in P_{br}(a,b)}\frac1{\alpha_e}
\le\frac1{c_{ab}^{(*)}}.
}
\tag{ZHS2}
$$

No two-terminal reduction is substituted for the multi-terminal response coefficient. All other attachment terminals remain grounded throughout the proof.

---

## 4. Apply ZHS to the revised ZHC pair

Define

$$
C_\eta:=\frac{p_\eta}{36\pi}>0.
\tag{4.1}
$$

For the ZHC pair, eventually along a sequence with `D epsilon->0`,

$$
L:=|P_{br}(a,b)|=\ell(ab)\ge\eta D/2,
\qquad
c_{ab}^{(*)}\ge C_\eta/D.
\tag{4.2}
$$

ZHS2 gives

$$
\boxed{
\sum_{e\in P_{br}(a,b)}\frac1{\alpha_e}
\le\frac{D}{C_\eta}.
}
\tag{ZHS3}
$$

### 4.1 Linear route-stress lower bound

Cauchy--Schwarz gives

$$
\left(\sum_{e\in P}\alpha_e\right)
\left(\sum_{e\in P}\frac1{\alpha_e}\right)
\ge L^2.
\tag{4.3}
$$

Therefore

$$
\boxed{
\sum_{e\in P_{br}(a,b)}\alpha_e
\ge
c_{ab}^{(*)}L^2
\ge
\frac{C_\eta\eta^2}{4}D.
}
\tag{ZHS4}
$$

Thus the selected deep route itself carries `Omega_eta(D)` bridge stress.

### 4.2 A linear subfamily has an absolute stress floor

Set

$$
a_\eta:=\frac{C_\eta\eta}{4}>0.
\tag{4.4}
$$

Let `N_small` count route bridges with `alpha_e<a_eta`. Every such edge contributes more than `1/a_eta` to ZHS3, so

$$
\frac{N_{small}}{a_\eta}
<\frac{D}{C_\eta},
$$

hence

$$
N_{small}
<\frac{a_\eta}{C_\eta}D
=\frac{\eta D}{4}.
\tag{4.5}
$$

Since `L>=eta D/2`, at least `eta D/4` route bridges obey `alpha_e>=a_eta`:

$$
\boxed{
\#\{e\in P_{br}(a,b):\alpha_e\ge a_\eta\}
\ge\frac{\eta D}{4},
\qquad
 a_\eta=\frac{p_\eta\eta}{144\pi}.
}
\tag{ZHS5}
$$

This eliminates another real loophole: the linearly deep harmonic-cell route cannot consist almost entirely of bridge stresses tending to zero. A fixed linear subfamily has a fixed absolute positive stress floor.

---

## 5. Exact target implication

Under

$$
S_{br}\ge\eta D^2,
\qquad
D\varepsilon\to0,
\tag{5.1}
$$

the revised ZHC/ZHS cell contains one actual diameter route with simultaneously:

- at least `eta D/2` physical contact bridges;
- endpoint component-response conductance at least `p_eta/(36pi D)`;
- KKT diameter weight at least `p_eta/(72pi D)` on the same actual diameter pair;
- reciprocal bridge-stress sum at most `36pi D/p_eta`;
- route bridge stress at least `[p_eta eta^2/(144pi)]D`;
- at least `eta D/4` bridge edges with
  $$
  \alpha_e\ge\frac{p_\eta\eta}{144\pi}>0;
  $$
- the whole harmonic cell carrying `(p_eta/18-o(1))D^2` contact stress.

Therefore, unless a macroscopic amount of the cell's quadratic stress lies on much heavier bridge edges, almost all of its stress must lie in the intervening two-edge-connected blocks. The bridge-dominant near-zero problem has become a route-local block-stress problem inside one unloaded harmonic cell.

The next sufficient theorem is:

> **ZHS block exclusion.** Exclude a single unloaded harmonic cell carrying `Omega(D^2)` contact stress and containing an `Omega(D)`-bridge response-visible diameter route for which a linear subfamily of bridges has an absolute stress floor.

A valid substitute is `epsilon=Omega(1/D)`, a strict sub-`D` competitor, or the exact global face inequality.

---

## 6. Regressions and limits

### Current leakage to grounded terminals

Allowed. Downstream leakage only makes the current through an upstream separating bridge larger than the transfer current reaching `a`. Equation (2.2) uses this monotonicity in the correct direction.

### Arbitrary-path voltage monotonicity

Not assumed. The proof orders nested global bridge cuts and applies the maximum principle separately to each downstream subnetwork, establishing (3.3).

### Two-terminal effective resistance

Not substituted. `c_ab^(*)` remains the off-diagonal multi-terminal Dirichlet-to-Neumann coefficient with all other attachments grounded.

### Tiny bridge stresses

Some may survive. ZHS5 proves only that fewer than half of the guaranteed `eta D/2` route bridges can fall below the fixed threshold `a_eta`.

### Macroscopic bridge threshold

Not reached. `a_eta` is `Theta_eta(1)`, whereas ZBL's macroscopic bridge threshold is `Theta_eta(D)`.

### Intervening two-edge-connected blocks

Still the binding geometry. ZHS does not control their diameter, face defect, train structure, or stress anisotropy.

### Fully inactive rattlers

Untouched.

---

## 7. Dependencies

- revised ZHC: the deep response-visible pair in one star-attached unloaded harmonic cell;
- C41: component response interpretation;
- positivity of all selected contact conductances;
- elementary Kirchhoff current balance and the maximum principle for a finite positive network.

No new external literature is required.

---

## 8. Promotion recommendation

**Hold as report.** ZHS is downstream of the report-level ZR/ZF and stacked PR #108/#111 chain.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHS exact series theorem:
For a positive harmonic-component response pair a,b, orient every physical contact
bridge on its bridge-tree route from b to a. Under V_b=1 and all other attachments
zero, each separating bridge carries at least the transfer current c_ab^(*). Nested
bridge sides plus the maximum principle make successive bridge voltage drops genuinely
series-ordered. Hence
    c_ab^(*) sum_{e in P_br(a,b)} 1/alpha_e <= 1.

For the revised ZHC pair,
    |P_br| >= eta D/2,
    c_ab^(*) >= p_eta/(36pi D),
so
    sum_P 1/alpha_e <= 36pi D/p_eta,
    sum_P alpha_e >= [p_eta eta^2/(144pi)]D.
At least eta D/4 route bridges satisfy
    alpha_e >= p_eta eta/(144pi) > 0.

The remaining quadratic cell stress is forced into the intervening two-edge-connected
blocks unless substantially heavier bridge edges occur.
```
