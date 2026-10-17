> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_heavy_chain_harmonic_capture_2026-09-09.md) · source SHA-256 `04bc64dbc3f646a8464031f650b6e2c9ce32d80cf5a270a31cb732b59efe191d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3A2435B82015","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHH: one harmonic cell captures a macroscopic bridge chain

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** closing-proof continuation / heavy-chain response localization  
**Target:** Target C, Gate C-II / Level I  
**Depends on:** PR #108 ZBL/ZBC, C35, C41, C64/C66  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

PR #108 proves that bridge dominance produces linearly many macroscopic bridges, and that their antichain width is bounded. In the near-zero response phase, the resulting nested heavy chain is crossed by a diameter edge incident to the C66 stress-star center.

This report strengthens that statement quantitatively. The deepest heavy cut itself carries a fixed positive amount of star-centered diameter KKT mass. After discarding the `o(1)` nonstar and tiny-response tails, C35's degree-three cap forces a fixed fraction of that mass and its exact contact response into one unloaded harmonic component. Every assigned star edge crosses the deepest heavy cut and therefore the entire ancestor chain, so the whole macroscopic bridge chain lies in the closure of the same harmonic cell.

The cell therefore contains `Omega(D)` bridges of stress `Omega(D)` each: an `Omega(D^2)` macroscopic bridge-stress package localized inside one response cell.

---

## 1. Heavy bridge chain from PR #108

Assume

$$
S_{br}\ge\eta D^2,
\qquad 0<\eta\le1.
\tag{1.1}
$$

ZBL defines the heavy threshold

$$
a_D:=\frac{\eta}{4\pi}D
\tag{1.2}
$$

and proves that at least `eta D/2` physical contact bridges satisfy

$$
\alpha_e\ge a_D.
\tag{1.3}
$$

C20's antichain stress budget makes the heavy-bridge poset have width at most `8pi/eta`. ZBC therefore gives a nested heavy chain

$$
e_1\prec e_2\prec\cdots\prec e_L
\tag{1.4}
$$

of length

$$
\boxed{
L\ge\frac{\eta^2}{16\pi}D.
}
\tag{ZHH1}
$$

Root the contact bridge tree at the block containing the C66 star center `z`, and orient the chain away from `z`, so `e_L` is deepest.

For every heavy bridge, C23 gives

$$
\alpha_e\le Dw_e,
\tag{1.5}
$$

where `w_e` is the total beta mass of actual diameter edges crossing its cut. Hence

$$
\boxed{w_e\ge\frac{\eta}{4\pi}.}
\tag{1.6}
$$

---

## 2. The deepest heavy cut carries fixed star beta mass

Let

$$
\tau_z:=\sum_{g\not\ni z}\beta_g.
\tag{2.1}
$$

C66 gives

$$
\tau_z\le C_0D\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0}.
\tag{2.2}
$$

At the deepest heavy bridge `e_L`, the total crossing beta mass is at least `eta/(4pi)`. All crossing nonstar edges together contribute at most `tau_z`. Therefore the beta mass of crossing star edges incident to `z` is at least

$$
\boxed{
B_{star}(e_L)
\ge
\frac{\eta}{4\pi}-C_0D\varepsilon.
}
\tag{ZHH2}
$$

Assume now the near-zero phase

$$
D\varepsilon\to0.
\tag{2.3}
$$

For all sufficiently large members,

$$
B_{star}(e_L)\ge\frac{\eta}{8\pi}.
\tag{2.4}
$$

Every star edge crossing `e_L` also crosses every ancestor `e_1,...,e_{L-1}`.

---

## 3. Almost all of the fixed star mass is response-visible

For every diameter edge `g`, PSD of `M=Lambda-L_H` gives the pointwise estimate

$$
|c_g-\beta_g|\le\varepsilon.
\tag{3.1}
$$

Discard star edges crossing `e_L` with `beta_g<=2epsilon`. There are at most `|H|<=pi D` diameter edges in total, so the discarded beta mass is at most

$$
2\pi D\varepsilon=o(1).
\tag{3.2}
$$

Let `mathcal S_L` be the remaining star edges crossing `e_L`. Then

$$
\boxed{
\sum_{g\in\mathcal S_L}\beta_g
\ge
\frac{\eta}{4\pi}-(C_0+2\pi)D\varepsilon.
}
\tag{ZHH3}
$$

and each such edge satisfies

$$
c_g>\beta_g/2>0.
\tag{3.3}
$$

---

## 4. One of at most three star-attached harmonic cells captures fixed mass

Take `g=zy in mathcal S_L`. Since `|z-y|=D>1`, its positive response is not a direct loaded-loaded contact term. C41 therefore gives at least one unloaded harmonic component with

$$
z,y\in A_r,
\qquad c_{zy}^{(r)}>0.
\tag{4.1}
$$

The terminal `z` belongs to at most three harmonic attachment sets because C35.1 gives `deg_C(z)<=3`. Choose for each `g` a common component `r(g)` maximizing its component response. Then

$$
c_g^{(r(g))}
\ge c_g/3
>\beta_g/6.
\tag{4.2}
$$

Pigeonhole over at most three possible components. There is one cell `I_*` and a subfamily `mathcal D_* subset mathcal S_L` assigned to it with

$$
\boxed{
\sum_{g\in\mathcal D_*}\beta_g
\ge
\frac13
\left[
\frac{\eta}{4\pi}-(C_0+2\pi)D\varepsilon
\right].
}
\tag{ZHH4}
$$

and

$$
\boxed{
\sum_{g\in\mathcal D_*}c_g^{(*)}
>
\frac1{18}
\left[
\frac{\eta}{4\pi}-(C_0+2\pi)D\varepsilon
\right].
}
\tag{ZHH5}
$$

Consequently, along `D epsilon->0`, the cell captures asymptotically at least

$$
\frac{\eta}{12\pi}
\tag{4.3}
$$

of beta mass and

$$
\frac{\eta}{72\pi}
\tag{4.4}
$$

of exact-diameter component-response mass.

---

## 5. The entire heavy chain lies in the same cell closure

Choose any `g=zy in mathcal D_*`. Its endpoints both lie in `A_*`, so there is a contact path from `z` to `y` through the connected interior component `I_*` using only `E_*`.

The edge `g` crosses the deepest heavy bridge `e_L`, hence, by nestedness, every heavy bridge `e_1,...,e_L` lies on the global bridge-tree route between `z` and `y`.

Each `e_j` is a global contact bridge separating `z` from `y`. Every contact path from `z` to `y` must use it, including the path through `I_*`. Therefore

$$
\boxed{
\{e_1,\ldots,e_L\}\subset E_*.
}
\tag{ZHH6}
$$

So one unloaded harmonic cell contains the complete nested macroscopic chain.

---

## 6. Quadratic bridge stress is localized inside that one cell

Each chain bridge satisfies `alpha_e>=eta D/(4pi)` and there are at least `eta^2 D/(16pi)` of them. Hence

$$
\boxed{
\sum_{j=1}^L\alpha_{e_j}
\ge
\frac{\eta^3}{64\pi^2}D^2.
}
\tag{ZHH7}
$$

This is already a fixed positive fraction of the complete contact-stress normalization `D^2`, localized entirely on physical bridge edges of one harmonic cell.

Independently, the component coordinate-energy identity and ZHH5 give

$$
\boxed{
\sum_{e\in E_*}\alpha_e
>
\frac1{18}
\left[
\frac{\eta}{4\pi}-(C_0+2\pi)D\varepsilon
\right]D^2,
}
\tag{ZHH8}
$$

so asymptotically the whole cell carries at least `eta/(72pi)` of the full contact stress. For small `eta`, ZHH8 is stronger than the direct chain-sum constant ZHH7; ZHH7 is stronger structurally because it locates quadratic stress **on the bridges themselves**.

---

## 7. One response-visible diameter pair crosses the whole macroscopic chain

The assigned family has at most all diameter edges, hence at most `pi D` members. From ZHH5, some `g_*=zy in mathcal D_*` satisfies, eventually,

$$
\boxed{
 c_{zy}^{(*)}
\ge
\frac{\eta}{144\pi^2D}.
}
\tag{ZHH9}
$$

after taking the bracket in ZHH5 at least `eta/(8pi)` for large members.

Since `c_{zy}>=c_{zy}^{(*)}` and `|c_{zy}-beta_{zy}|<=epsilon`, the same phase eventually gives

$$
\boxed{
\beta_{zy}
\ge
\frac{\eta}{288\pi^2D}.
}
\tag{ZHH10}
$$

This same actual diameter pair crosses every bridge in the heavy chain.

Thus one cell has a response-visible diameter pair of weight `Omega_eta(1/D)` whose route contains `Omega_eta(D)` bridge edges of stress `Omega_eta(D)` each.

---

## 8. Geometric localization inherited from ZBL

ZBL proves that at the C66 star center `z`, every `eta`-heavy bridge line satisfies

$$
\frac{\operatorname{dist}(z,\operatorname{line}(e))}{D}\to0
\tag{8.1}
$$

when `D epsilon->0`.

It also proves that for every fixed `xi>0`, all but `o(D)` of the heavy bridges satisfy

$$
\bigl||u-z|-|v-z|\bigr|>1-\xi.
\tag{8.2}
$$

Since the ZHH chain has `Omega_eta(D)` members, all but an `o(1)` fraction of its bridges are asymptotically radial unit contacts whose supporting lines pass `o(D)` from the same star center.

Therefore the localized cell contains a linear **macroscopic near-radial articulation chain**, not merely an arbitrary set of high-stress cut edges.

---

## 9. Attachment consequence

Apply the ZHA argument to `G_*`, the induced actual contact graph on `I_* union A_*`. Its graph diameter is at least the number `L` of separating heavy bridges. C33 gives at least `2|I_*|+1` component rows, while Eppstein gives the connected triangle-free penny-graph upper bound. Therefore

$$
\boxed{
|A_*|\ge\frac{L+3}{2}
\ge
\frac{\eta^2}{32\pi}D+\frac32.
}
\tag{ZHH11}
$$

C43 then gives a uniformly-short positive component-response matching on all but at most two of these attachments, of size at least

$$
\boxed{
\frac{\eta^2}{64\pi}D-O(1).
}
\tag{ZHH12}
$$

In the near-zero phase its total response conductance is `o(1/D)` by the same defect argument as ZHA.

---

## 10. Exact target implication

The bridge-dominant near-zero branch is now forced into one cell with all of:

```text
Omega_eta(D^2) total cell contact stress,
Omega_eta(D^2) stress carried specifically by physical contact bridges,
Omega_eta(D) nested macroscopic bridges alpha_e=Omega_eta(D),
one actual z--y diameter pair crossing the whole chain with
    c_zy^(*)=Omega_eta(1/D), beta_zy=Omega_eta(1/D),
all chain bridge lines o(D) from z and almost all bridge edges near-radial,
Omega_eta(D) distinct loaded attachments,
an almost-perfect Omega_eta(D) matching of uniformly-short positive response pairs
    with total conductance o(1/D).
```

This is materially narrower than the old macroscopic-bridge-cut target. A closing theorem no longer has to exclude an arbitrary isolated heavy bridge. It is enough to exclude this one-cell macroscopic bridge-chain geometry.

The most concrete next statement is:

> **ZHH radial-chain exclusion.** A triangle-free global minimizer cannot contain one unloaded harmonic cell carrying a nested `Omega(D)` chain of `Omega(D)`-stress unit bridges that is asymptotically radial about a common diameter endpoint while the same cell has the ZHH response/attachment data.

A valid substitute is `epsilon=Omega(1/D)`, a strict sub-`D` competitor, or the global face inequality.

---

## 11. Regressions and limits

- A convex reciprocal polygon can contain many long nested diagonals; ZHH does not claim otherwise.
- The heavy bridges need not be consecutive contact edges; two-edge-connected blocks may lie between them.
- Radialization is asymptotic and does not make the whole cell one-dimensional.
- The uniformly-short response matching still has no conductance floor.
- Fully inactive rattlers remain outside the force-visible core.

---

## 12. Dependencies

- PR #108 ZBL and ZBC;
- C20/C23 bridge cut and antichain identities;
- C35.1 loaded contact degree at most three;
- C41 component response decomposition and coordinate-energy identity;
- C64 PSD transfer;
- C66 mechanical stress-star concentration;
- ZHA attachment argument for Section 9.

No new external literature is imported.

---

## 13. Promotion recommendation

**Hold as report.** It is downstream of report-level ZR/ZF and stacked PR #108/#111.

---

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHH:
Assume S_bridge>=eta D^2 and D epsilon->0. PR #108 gives a nested heavy bridge chain
of length >=eta^2 D/(16pi), each alpha_e>=eta D/(4pi). For the deepest cut,
    w_e>=eta/(4pi).
C66 leaves only o(1) nonstar beta mass, so fixed beta mass >=eta/(8pi) is carried by
z-star diameter edges crossing the deepest cut. Removing beta<=2epsilon edges costs
o(1). Since deg_C(z)<=3, one harmonic cell captures fixed beta and exact-diameter
response mass from these star edges.

Every assigned star edge crosses the deepest cut and all ancestor heavy cuts; its
contact path through the assigned cell must therefore contain the entire heavy chain.
Thus one cell contains
    L>=eta^2 D/(16pi) bridges,
    alpha_e>=eta D/(4pi) on each,
so chain bridge stress >=eta^3 D^2/(64pi^2).
The same cell has exact-diameter response mass >=eta/(72pi)-o(1), and one actual
z--y diameter pair crossing the whole chain with c_zy^(*)=Omega_eta(1/D).
ZBL makes all chain lines o(D) from z and almost all chain edges near-radial.

ZHA then gives |A_*|>=eta^2 D/(32pi)+O(1) and a linear uniformly-short response
matching in the same cell.

Remaining bridge target:
exclude this one-cell macroscopic near-radial bridge chain, or derive a quantitative
defect / strict sub-D competitor / exact face inequality.
```
