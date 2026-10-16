<!-- theorem-state: {"artifact_id":"ART-61B268FA715E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZWT: weighted star flow forces an almost-eta-D macroscopic bridge trunk

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / weighted bridge-tree theorem  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** ZBD, C18, C27, C66  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

The earlier ZHH/ZHT route extracted a macroscopic bridge chain by first thresholding bridge stresses and then applying an antichain-width argument. That loses a factor of `eta`: it produced length `eta^2 D/(16pi)`.

The normalized diameter stress itself gives a much stronger route. In the phase `D epsilon->0`, C66 puts all but `o(1)` beta mass on one diameter star centered at `z`. Bridge dominance says the beta-weighted total bridge-tree path length is at least `eta D`. Nonstar diameter edges can contribute only `o(D)` to this weighted length. Therefore the z-star endpoint measure alone has first bridge-depth moment `(eta-o(1))D`.

Threshold the **star subtree masses**, not the bridge stresses. Low-mass bridge cuts can account for at most `2pi a D` of that first moment. The high-mass bridge cuts form a rooted subtree, and each depth level carries total mass at most one. Hence this high-mass subtree must contain a root-to-leaf chain of length `(eta-2pi a-o(1))D` for every fixed `a<eta/(2pi)`.

C18 gives a common sub-60-degree cone for all z-star diameter directions. The exact bridge cut-force law then makes every bridge on the high-mass chain carry `Omega_a(D)` contact stress.

Taking `a=eta/(4pi)` yields a **consecutive macroscopic bridge trunk of length `(eta/2-o(1))D`**, a large improvement over ZHT.

---

## 1. Weighted bridge depth

Assume

\[
S_{br}\ge\eta D^2,
\qquad 0<\eta\le1,
\tag{1.1}
\]

and the near-zero response phase

\[
D\varepsilon\to0.
\tag{1.2}
\]

ZBD gives the exact bridge-depth identity

\[
\sum_{e\text{ bridge}}w_e
=
\sum_{g\in H}\beta_g\ell(g),
\tag{1.3}
\]

while C23 gives `alpha_e<=D w_e`. Therefore

\[
\boxed{
\sum_{g\in H}\beta_g\ell(g)
\ge\eta D.
}
\tag{1.4}
\]

C66 supplies a diameter vertex `z` with nonstar beta mass

\[
\tau_z:=\sum_{g\not\ni z}\beta_g
\le C_0D\varepsilon=o(1).
\tag{1.5}
\]

Every diameter tree path has length at most the total number of contact bridges, and C27 gives

\[
\ell(g)\le2q-3\le2\pi D.
\tag{1.6}
\]

Hence the complete nonstar contribution to (1.4) is at most

\[
\sum_{g\not\ni z}\beta_g\ell(g)
\le2\pi D\tau_z=o(D).
\tag{1.7}
\]

Thus the z-star diameter edges alone satisfy

\[
\boxed{
\sum_{zy\in H}\beta_{zy}\ell(zy)
\ge
(\eta-2\pi\tau_z)D.
}
\tag{ZWT1}
\]

---

## 2. Rooted star-mass flow

Root the complete contact bridge-block tree at the block containing `z`.

For every rooted bridge edge `e`, define its **star subtree mass**

\[
\boxed{
 m_e^z
 :=
 \sum_{\substack{zy\in H\\y\text{ lies below }e}}
 \beta_{zy}.
}
\tag{2.1}
\]

A star edge `zy` contributes `beta_zy` to `m_e^z` for exactly the bridge edges on its tree path from `z` to `y`. Therefore

\[
\boxed{
\sum_e m_e^z
=
\sum_{zy\in H}\beta_{zy}\ell(zy).
}
\tag{2.2}
\]

Combining with ZWT1,

\[
\boxed{
\sum_e m_e^z
\ge
(\eta-2\pi\tau_z)D.
}
\tag{ZWT2}
\]

The masses are monotone down the rooted tree: if `f` is a descendant of `e`, then

\[
m_f^z\le m_e^z.
\tag{2.3}
\]

At any fixed tree depth, the descendant subtrees of the bridge edges at that depth are disjoint, so

\[
\boxed{
\sum_{e\text{ at depth }j}m_e^z
\le
\sum_{zy\in H}\beta_{zy}
\le1.
}
\tag{2.4}
\]

---

## 3. Parametric high-mass trunk theorem

Fix a constant

\[
0<a<\frac{\eta}{2\pi}.
\tag{3.1}
\]

Call a rooted bridge **a-heavy in star mass** if

\[
m_e^z\ge a.
\tag{3.2}
\]

Let `E_<a` be the remaining bridge edges. Since the complete contact graph has at most `2pi D` bridges,

\[
\sum_{e\in E_{<a}}m_e^z
< a|E(T)|
\le2\pi aD.
\tag{3.3}
\]

Therefore ZWT2 gives

\[
\boxed{
\sum_{e:m_e^z\ge a}m_e^z
\ge
(\eta-2\pi a-2\pi\tau_z)D.
}
\tag{3.4}
\]

Because star subtree mass is monotone under ancestry, the set

\[
T_a:=\{e:m_e^z\ge a\}
\tag{3.5}
\]

is a rooted subtree with no gaps from the root.

Let `H_a` be its maximum edge depth. By (2.4), the total star mass over all edges of `T_a` is at most one per depth level:

\[
\sum_{e\in T_a}m_e^z
\le H_a.
\tag{3.6}
\]

Combine with (3.4).

### Theorem ZWT.1 — weighted star trunk

For every fixed `a in (0,eta/(2pi))`, the rooted bridge tree contains a **consecutive** root-to-leaf bridge chain of length

\[
\boxed{
H_a
\ge
(\eta-2\pi a-2\pi\tau_z)D.
}
\tag{ZWT3}
\]

Every bridge on this chain has star crossing beta mass at least `a`.

In the phase `D epsilon->0`, `tau_z=o(1)`, so

\[
\boxed{
\liminf\frac{H_a}{D}
\ge
\eta-2\pi a.
}
\tag{ZWT4}
\]

This is a weighted tree theorem; no Dilworth/antichain extraction is used.

---

## 4. C18 converts star mass into macroscopic bridge force

Choose any one actual z-star diameter edge and let `u_0` be its unit direction from `z` to its partner. C18 gives, for all sufficiently large sources,

\[
\angle(u_0,u_{zy})<\Theta(D)<\pi/3
\tag{4.1}
\]

for every z-star diameter direction `u_zy`. Hence

\[
u_0\cdot u_{zy}>1/2.
\tag{4.2}
\]

Take a bridge `e` on the ZWT chain and orient it away from `z`. Every z-star edge counted by `m_e^z` crosses this bridge from `z` to its descendant partner. C23's exact vector cut law gives

\[
\frac{\alpha_e}{D}u_e
=
\sum_{g\pitchfork e}\beta_g u_g
\tag{4.3}
\]

with consistent orientation.

Project onto `u_0`. The z-star contribution is more than `m_e^z/2>=a/2`. The complete nonstar contribution has norm at most `tau_z`, so

\[
\frac{\alpha_e}{D}
\ge
u_0\cdot\frac{\alpha_e}{D}u_e
>
\frac a2-\tau_z.
\tag{4.4}
\]

Thus:

### Theorem ZWT.2 — every weighted-trunk bridge is macroscopic

For every fixed `a>0`, along `D epsilon->0`, all bridges in the ZWT chain satisfy

\[
\boxed{
\alpha_e
\ge
\left(\frac a2-o(1)\right)D.
}
\tag{ZWT5}
\]

In particular, eventually

\[
\boxed{
\alpha_e\ge\frac a4D.
}
\tag{ZWT6}
\]

The same projection shows that all oriented trunk directions remain in the common z-star cone up to `o(1)` angular error.

---

## 5. Concrete choice `a=eta/(4pi)`

Set

\[
 a=\frac{\eta}{4\pi}.
\tag{5.1}
\]

Then ZWT3 becomes

\[
\boxed{
H_a
\ge
\left(\frac\eta2-2\pi\tau_z\right)D
=
\left(\frac\eta2-o(1)\right)D.
}
\tag{ZWT7}
\]

Every trunk bridge eventually satisfies

\[
\boxed{
\alpha_e\ge\frac{\eta}{16\pi}D.
}
\tag{ZWT8}
\]

Thus the earlier ZHT bound

\[
H\ge\frac{\eta^2}{16\pi}D
\]

is superseded, in the near-zero phase, by

\[
\boxed{
H\ge(\eta/2-o(1))D.
}
\tag{5.2}
\]

The improvement is by a factor asymptotic to `8pi/eta` in trunk length.

The stress carried by this complete trunk obeys, for sufficiently large members,

\[
\boxed{
\sum_{e\in\text{trunk}}\alpha_e
\ge
\left(\frac{\eta^2}{32\pi}-o(1)\right)D^2.
}
\tag{ZWT9}
\]

using the sharper asymptotic `alpha_e/D>=a/2-o(1)`; with the finite safe bound ZWT8 one gets `eta^2D^2/(32pi)-o(D^2)` after combining `H=(eta/2-o(1))D`.

---

## 6. One harmonic cell captures the whole weighted trunk

Consider the deepest bridge `e_*` of the ZWT chain. Its star crossing beta mass is at least `a`.

Discard z-star edges crossing `e_*` with `beta<=2epsilon`; their total beta mass is at most

\[
2\varepsilon\deg_H(z)
\le2\pi D\varepsilon=o(1).
\tag{6.1}
\]

Every remaining star edge has `c_g>beta_g/2>0` by the PSD pointwise transfer estimate. Since `z` has contact degree at most three, it belongs to at most three unloaded harmonic attachment sets. Assign each remaining star edge to a common component carrying maximal component response, exactly as in revised ZHC/ZHH.

One unloaded component `I_*` captures a fixed beta mass at least

\[
\boxed{
a/3-o(1)}
\tag{6.2}
\]

and exact-diameter component response at least

\[
\boxed{
a/18-o(1).}
\tag{6.3}
\]

Every assigned star edge crosses the deepest bridge and therefore every ancestor bridge of the ZWT chain. Its contact path through `I_*` must cross all those global contact bridges. Hence

\[
\boxed{
\text{the complete ZWT trunk lies in the closure of one unloaded harmonic cell }I_*.
}
\tag{ZWT10}

The cell contact stress satisfies

\[
\boxed{
\sum_{e\in E_*}\alpha_e
\ge
\left(\frac a{18}-o(1)\right)D^2.
}
\tag{ZWT11}

For `a=eta/(4pi)`, this is

\[
\sum_{E_*}\alpha_e
\ge
\left(\frac{\eta}{72\pi}-o(1)\right)D^2.
\tag{6.4}
\]

---

## 7. Stronger attachment, matching, and post-ZF surplus consequences

ZHA applies to the complete ZWT trunk. If its length is `H_a`, then

\[
\boxed{|A_*|\ge H_a+1,}
\tag{7.1}
\]

and the uniformly-short component-response graph on `A_*` has a matching of size at least

\[
\boxed{(H_a-1)/2.}
\tag{7.2}
\]

For `a=eta/(4pi)`,

\[
\boxed{
|A_*|
\ge
(\eta/2-o(1))D,
}
\tag{ZWT12}
\]

\[
\boxed{
|J_*|
\ge
(\eta/4-o(1))D.
}
\tag{ZWT13}
\]

The ZHA defect estimate still gives

\[
\sum_{st\in J_*}c_{st}^{(*)}=o(1/D),
\tag{7.3}
\]

so the average component conductance on this now much larger matching is `o(1/D^2)`.

ZHL also improves immediately. The internal graph diameter of the captured component is at least `H_a-2`, so the current-main exact component ledger yields

\[
\boxed{
 e_{BB}+2s_C
\ge
H_a-8+3(d_H+s_Z).
}
\tag{7.4}
\]

Therefore for `a=eta/(4pi)`,

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge
\frac\eta2.
}
\tag{ZWT14}

This replaces ZHL's older `eta^2/(16pi)` coefficient.

---

## 8. Limit as the threshold decreases

The parametric form is useful. For every fixed `a>0` with `2pi a<eta`,

\[
\liminf H_a/D\ge\eta-2\pi a,
\]

while every bridge has asymptotic stress at least `(a/2)D`.

Thus one may make the trunk length coefficient arbitrarily close to `eta` at the cost of making the fixed macroscopic stress coefficient small but still positive.

Formally, for every fixed `theta in (0,eta)`, choose

\[
a=\frac{\eta-\theta}{2\pi}.
\]

Then there is a consecutive trunk of length at least

\[
(\theta-o(1))D
\]

whose every bridge has

\[
\alpha_e
\ge
\left(\frac{\eta-\theta}{4\pi}-o(1)\right)D.
\]

This weighted tradeoff is the strongest bridge-tree route obtained so far.

---

## 9. Exact target implication

The bridge-dominant `D epsilon->0` branch is no longer a short heavy-chain phenomenon. For any fixed `theta<eta`, one single harmonic cell contains a **consecutive** contact-bridge trunk of length `(theta-o(1))D`, every bridge carrying a fixed `Theta_{eta,theta}(D)` stress and lying in the acute C18 star cone.

For the convenient midpoint choice `theta=eta/2`, the same cell has:

```text
trunk length >= (eta/2-o(1))D,
every bridge alpha >= eta D/(16pi),
trunk bridge stress >= (eta^2/(32pi)-o(1))D^2,
cell response mass on exact diameter pairs >= eta/(72pi)-o(1),
|A_*| >= (eta/2-o(1))D,
uniformly-short positive response matching >= (eta/4-o(1))D,
e_BB+2s_C >= (eta/2-o(1))D.
```

The remaining obstruction is correspondingly narrower: a macroscopic fraction of a source-scale radial force chain is embedded inside one unloaded harmonic cell, while the cell's short boundary response channels vanish quantitatively.

---

## 10. Regressions and limits

- The result requires the near-zero phase `D epsilon->0`; without C66 star concentration the weighted bridge depth can be distributed among many diameter directions.
- The trunk is a bridge-tree trunk, not literally a contact path: two-edge-connected blocks remain between consecutive bridges.
- As `a` is made smaller to lengthen the trunk, the guaranteed per-bridge stress coefficient also becomes smaller; `a` must remain fixed independently of `D` for the macroscopic conclusion.
- Low-stress braces inside the intervening blocks remain a binding local regression.
- Contact-isolated source points remain outside the force-visible core.

---

## 11. Dependencies

- ZBD exact diameter-pair bridge-depth identity;
- C18 shared-endpoint star-angle bound;
- C27 total contact-bridge count;
- C35/C41 for harmonic-cell capture;
- C64 pointwise response transfer;
- C66 stress-star concentration;
- ZHA/ZHL for downstream consequences.

No new external literature is imported.

---

## 12. Promotion recommendation

**Hold as report.** This theorem is downstream of report-level ZR/ZF and stacked PR #108/#111. It supersedes the earlier ZHH/ZHT trunk-length constants in the near-zero phase.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZWT weighted star-flow theorem:
Bridge dominance gives sum_h beta_h ell(h)>=eta D. Under D epsilon->0, C66 leaves
nonstar beta mass tau_z=o(1), whose weighted path contribution is <=2piD tau_z. Thus
z-star edges alone satisfy
    sum_{zy} beta_zy ell(zy) >= (eta-2pi tau_z)D.

Root the bridge tree at z. Let m_e^z be beta mass of z-star partners below bridge e.
Then sum_e m_e^z is the displayed first moment. Fix a<eta/(2pi). Low-mass bridges
m_e^z<a contribute at most 2pi aD. High-mass bridges form a rooted subtree, and each
depth level has total star mass <=1. Therefore the high-mass subtree contains a
consecutive chain of length
    H_a >= (eta-2pi a-2pi tau_z)D.

C18 puts all z-star directions in one <60-degree cone. Projecting the exact cut-force
law onto one star direction gives on every chain bridge
    alpha_e/D >= a/2-o(1).

With a=eta/(4pi):
    H >= (eta/2-o(1))D,
    alpha_e >= eta D/(16pi) eventually,
and the complete trunk is captured by one unloaded harmonic cell. Consequently
    |A_*| >= (eta/2-o(1))D,
    |J_short| >= (eta/4-o(1))D,
    (e_BB+2s_C)/D >= eta/2-o(1).

More generally, for every fixed theta<eta one can obtain length (theta-o(1))D with
per-bridge stress ((eta-theta)/(4pi)-o(1))D.
```
