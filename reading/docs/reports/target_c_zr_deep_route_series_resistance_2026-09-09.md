> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_deep_route_series_resistance_2026-09-09.md) · source SHA-256 `937aeb2132dab9d97f3cf85304923e0b23a44a65838bdeebbd4917700441a0d9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9A8E336F6F79","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZSR: deep harmonic route has bounded series resistance

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Base:** stacked on PR #108; continues ZHC in PR #111  
**Run type:** closing-proof continuation / exact electrical reduction  
**Target:** Target C, Gate C-II / Level I  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHC produces, in the bridge-dominant small-defect phase, one actual diameter pair `a,b` in one unloaded harmonic cell whose component response conductance is `Omega(1/D)` and whose bridge-block-tree route contains `Omega(D)` physical contact bridges. This report proves that those bridges cannot all have tiny KKT contact stress.

The decisive observation is an exact effective-resistance comparison. Kron reduction preserves the effective resistance between retained terminals. Every physical contact bridge separating `a` and `b` is traversed by unit current in the unit `a`-to-`b` Thomson problem, so the sum of its electrical resistances `1/alpha_e` is a lower bound for the full effective resistance. In the reduced terminal network there is a direct conductance edge of weight `c_ab`, so the same effective resistance is at most `1/c_ab`. Therefore

$$
\boxed{
\sum_{e\in P_{ab}}\frac1{\alpha_e}
\le R_{\rm eff}(a,b)
\le\frac1{c_{ab}}
\le\frac1{c_{ab}^{(*)}}.
}
$$

For the ZHC pair this is `O(D)`. Since the route has `Omega(D)` bridges, a linear number of them have an absolute positive stress floor independent of `D`.

---

## 1. Setup and imported ZHC pair

Fix `eta in (0,1]`. Work along a hypothetical sequence of sufficiently large lexicographically normalized triangle-free C-II survivors satisfying

$$
S_{br}\ge\eta D^2,
\qquad
D\varepsilon\to0,
\tag{1.1}
$$

where

$$
\varepsilon=\frac12\operatorname{tr}(\Lambda-L_H).
$$

Define

$$
p_\eta:=\frac{\eta}{4\pi-\eta}.
\tag{1.2}
$$

ZHC gives, for all sufficiently large members of the sequence, one unloaded harmonic component `I_*`, attachment set `A_*`, and one actual diameter pair

$$
g_*=ab\in H,
\qquad a,b\in A_*,
\qquad |a-b|=D,
\tag{1.3}
$$

such that

$$
c_{ab}^{(*)}\ge\frac{p_\eta}{36\pi D},
\tag{1.4}
$$

$$
\beta_{ab}\ge\frac{p_\eta}{72\pi D},
\tag{1.5}
$$

and its contact bridge-block-tree route contains

$$
L:=|P_{ab}|=\ell(ab)\ge\frac{\eta D}{2}
\tag{1.6}
$$

physical contact bridges. ZHC also proves that every one of these bridges lies in the closure `E_*` of the same harmonic cell.

Here `c_ab^(*)` is the contribution of `I_*` to the full terminal response conductance. Hence

$$
c_{ab}\ge c_{ab}^{(*)}>0.
\tag{1.7}
$$

---

## 2. Exact series-resistance lemma

### Lemma ZSR.1

Let `G` be any finite connected positive-conductance network and let `a,b` be two vertices. Suppose `P` is a collection of physical bridge edges of `G`, each of which separates `a` from `b`. If the conductance of bridge `e` is `alpha_e`, then

$$
\boxed{
\sum_{e\in P}\frac1{\alpha_e}
\le R_{\rm eff}^G(a,b).
}
\tag{ZSR.1}
$$

#### Proof

Use Thomson's principle with one unit of current injected at `a` and removed at `b`, and no external injection at any other vertex.

If `e` is a physical bridge separating `a` from `b`, deleting `e` gives two components, one containing `a` and the other containing `b`. Conservation of current on the `a`-side forces the net current through the unique cut edge `e` to be exactly one. Therefore the Dirichlet/Thomson energy spent on `e` is exactly

$$
\frac{1^2}{\alpha_e}=\frac1{\alpha_e}.
$$

The bridge edges in `P` are distinct. The total energy of the unit current is therefore at least the sum of these bridge energies. Minimizing over unit flows gives (ZSR.1). `square`

### Lemma ZSR.2

Let `Lambda` be the Kron response of the same network on any retained terminal set containing `a,b`, and write `c_ab=-Lambda_ab`. Then

$$
\boxed{
R_{\rm eff}^G(a,b)
=R_{\rm eff}^{\Lambda}(a,b)
\le\frac1{c_{ab}}.
}
\tag{ZSR.2}
$$

#### Proof

Schur/Kron reduction preserves effective resistance between retained vertices. The reduced response network is the complete weighted graph with edge conductances `c_st=-Lambda_st>=0` (zero weights allowed).

In that reduced network, the single direct edge `ab` of conductance `c_ab` is one admissible `a`-to-`b` route. Deleting all other reduced edges can only increase effective resistance by Rayleigh monotonicity, and the one-edge network has resistance `1/c_ab`. Hence

$$
R_{\rm eff}^{\Lambda}(a,b)\le1/c_{ab}.
$$

This proves ZSR.2. `square`

Combining the two lemmas gives the exact bridge-route inequality

$$
\boxed{
\sum_{e\in P_{ab}}\frac1{\alpha_e}
\le R_{\rm eff}(a,b)
\le\frac1{c_{ab}}
\le\frac1{c_{ab}^{(*)}}.
}
\tag{ZSR.3}
$$

No small-defect assumption is used in ZSR.1--ZSR.3; the small-defect phase enters only to supply the quantitative ZHC pair.

---

## 3. Quantitative consequence for the ZHC route

Insert ZHC's bound (1.4) into ZSR.3:

$$
\boxed{
\sum_{e\in P_{ab}}\frac1{\alpha_e}
\le\frac{36\pi}{p_\eta}D.
}
\tag{ZSR.4}
$$

Thus the `L>=eta D/2` bridge stresses have harmonic mean at least

$$
\frac{L}{\sum_{e\in P_{ab}}1/\alpha_e}
\ge
\frac{p_\eta L}{36\pi D}
\ge
\boxed{\frac{p_\eta\eta}{72\pi}}.
\tag{ZSR.5}
$$

This already rules out a deep route whose bridge stresses all tend to zero.

A stronger counting form is convenient. Put

$$
\tau_\eta:=\frac{p_\eta\eta}{144\pi}.
\tag{1.8}
$$

Let

$$
N_{\rm low}
=|\{e\in P_{ab}:\alpha_e<\tau_\eta\}|.
$$

Each low-stress bridge contributes more than `1/tau_eta` to the left side of ZSR.4. Hence

$$
\frac{N_{\rm low}}{\tau_\eta}
<\frac{36\pi}{p_\eta}D,
$$

so

$$
N_{\rm low}<\frac{\eta D}{4}.
\tag{ZSR.6}
$$

Since `L>=eta D/2`, at least

$$
\boxed{
N_{\rm abs}
:=|\{e\in P_{ab}:\alpha_e\ge\tau_\eta\}|
\ge\frac{\eta D}{4}
}
\tag{ZSR.7}
$$

route bridges have the absolute stress floor

$$
\boxed{
\alpha_e\ge
\tau_\eta
=\frac{p_\eta\eta}{144\pi}
=\frac{\eta^2}{144\pi(4\pi-\eta)}.
}
\tag{ZSR.8}
$$

All of these bridges lie in the closure of the same unloaded harmonic cell `I_*`, and because they lie on one bridge-tree route they form one nested chain of cuts separating the same diameter pair `a,b`.

Consequently the same route carries at least linear total contact stress:

$$
\boxed{
\sum_{e\in P_{ab}}\alpha_e
\ge
N_{\rm abs}\tau_\eta
\ge
\frac{p_\eta\eta^2}{576\pi}D.
}
\tag{ZSR.9}
$$

The stronger fact is not the `Omega(D)` total, which is small compared with the global `D^2` normalization; it is the existence of `Omega(D)` individually nonvanishing bridge stresses on one concrete diameter route.

---

## 4. Exact target implication

The bridge-dominant small-defect survivor is now forced into the following single-cell normal form.

There is one unloaded harmonic component `I_*` and one actual diameter pair `a,b in A_*` such that

1. `|a-b|=D`;
2. `c_ab^(*)>=p_eta/(36 pi D)`;
3. `beta_ab>=p_eta/(72 pi D)`;
4. the route from `a` to `b` contains at least `eta D/2` physical contact bridges, all in `E_*`;
5. the route series resistance satisfies `sum 1/alpha_e <= (36 pi/p_eta)D`;
6. at least `eta D/4` of those bridges satisfy the absolute floor `alpha_e>=tau_eta>0`.

Thus two earlier degeneracies are simultaneously excluded on this route:

- the deep route cannot be supported by a vanishing `beta_ab` smaller than order `1/D`;
- the route cannot be made of linearly many bridge contacts whose `alpha` stresses all vanish.

What remains possible is a nested chain of `Theta(D)` articulation cuts with order-one bridge stresses, separated by two-edge-connected contact blocks whose internal geometry may still be two-dimensional.

---

## 5. What this does not prove

ZSR does **not** give `alpha_e=Omega(D)` on the route. Therefore the C68 radialization estimate that is effective for ZBL's macroscopic bridges does not automatically make the ZSR absolute-stress chain radial under only `D epsilon->0`.

It also does not make the physical bridge edges consecutive in the embedded contact graph. Intervening two-edge-connected blocks may contain nontrivial internal paths, so Theorem P cannot yet be applied directly.

Finally, ZSR is a theorem about the force-visible contact core. It does not control fully inactive rattlers outside that core.

---

## 6. Regression checks

### Long series chain

A literal unit path with identical conductance `alpha` has resistance `L/alpha`. If its endpoint response conductance is of order `1/D` and `L=Theta(D)`, the theorem correctly requires `alpha=Omega(1)`. Thus the scaling in ZSR.8 is the correct series scaling.

### Large parallel blocks between bridges

Arbitrary parallel conductance inside the intervening two-edge-connected blocks can reduce their own resistance but cannot bypass a physical bridge. Every unit `a`-to-`b` flow still sends current exactly one through every route bridge, so ZSR.1 remains exact.

### Extra response attachments

The full response may have many other terminals and many other positive conductances. They only decrease the reduced-network effective resistance relative to deleting them, so `R_eff<=1/c_ab` remains valid.

### Nonuniform bridge stresses

Fully allowed. The theorem does not assert every bridge has a constant floor; it proves a linear-size subchain does.

---

## 7. Shortest next lemma

The electrical weakness of the deep route is now removed. The remaining route-local obstruction is geometric.

A sufficient next statement is:

> **ZSR block-transport lemma.** In a sufficiently large triangle-free global minimizer, one unloaded harmonic cell cannot contain a Euclidean-diameter attachment pair whose bridge-tree route has `Omega(D)` physical bridges, with `Omega(D)` of those bridges carrying an absolute positive KKT stress floor, while the component itself carries `Omega(D^2)` total contact stress.

The proof must control the intervening two-edge-connected blocks. Promising exact currencies are C39/C40's total block-diameter budget, C42's `m-O(D)` strict-rhombic bulk, or the reciprocal-polygon diagonals associated with the nested bridge cuts.

A response-side alternative is to use the same cell's `Omega(1/D)` diameter response together with its strict C41 subdiameter response clique to prove `epsilon=Omega(1/D)`.

---

## 8. Classification

**Status:** proved report-level theorem conditional on ZHC and the same report-level ZR/ZF dependencies.  
**Level I:** still open.  
**External literature:** none newly imported.  
**Computation:** none.
