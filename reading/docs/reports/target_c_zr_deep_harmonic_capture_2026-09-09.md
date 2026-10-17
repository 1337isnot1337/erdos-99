> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_deep_harmonic_capture_2026-09-09.md) · source SHA-256 `b9a08a3140e087a0646bb71e79f1d879e299e1482606d4be7ce078a94044937d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E469CE6C1692","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHC: deep bridge mass collapses into one star-attached harmonic cell

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Base:** stacked on PR #108  
**Run type:** closing-proof continuation / bridge-response synthesis  
**Target:** Target C, Gate C-II / Level I  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

This report combines ZBD's exact diameter-pair bridge-depth identity with C41 component response, C66 mechanical stress-star concentration, C35's unconditional loaded-degree bound, and C64 PSD transfer.

The first draft used the C44 constant-number macroscopic-component lemma. The post-ZF ZM/ZS reconciliation on current `main` correctly warns that the C44 near-minimal response branch is not a valid post-ZF fallback. The proof below removes C44 completely.

The replacement is stronger. In the phase `D epsilon -> 0`, C66 puts all but `o(1)` of the diameter KKT mass on one star center `z`. C35.1, which follows directly from convexity and triangle-free unit-angle separation and does not require `sigma_B=o(D)`, gives `deg_C(z)<=3`. Hence `z` can attach to at most three unloaded harmonic components. A fixed amount of linearly deep, response-visible diameter mass must therefore enter one of only three cells.

The resulting single cell carries a fixed fraction of the full `D^2` contact stress and contains an actual diameter pair with both response and KKT weight `Omega(1/D)` whose bridge-tree route has length `Omega(D)`.

---

## 1. Setup

Work in a sufficiently large lexicographically normalized triangle-free C-II survivor satisfying the audited ZR/ZF inputs and PR #108. Let

- `C` be the full positive contact graph on the nonisolated core;
- `H` be the full actual diameter graph on loaded terminal set `B`;
- `alpha_e>0` and `beta_g>0` be a relative-interior normalized KKT stress;
- `sum_C alpha_e=D^2` and `sum_H beta_g=1`;
- `Lambda` be the positive contact-network response on `B`;
- `c_{uv}=-Lambda_{uv}` for `u!=v`;
- `M=Lambda-L_H(beta) succeq0`;
- `epsilon=(1/2) tr M`.

C65 makes `H` the full actual diameter graph. Hopf--Pannwitz and the force-hull perimeter bound give

$$
|H|\le |B|\le\pi D.
\tag{1.1}
$$

Let `T` be the contact bridge-block tree. For `g=ab in H`, write

$$
\ell(g)=d_T(\tau(a),\tau(b)),
\tag{1.2}
$$

the number of physical contact bridges on its route.

ZBD rewrites C23's rooted layer-cake identity as

$$
\sum_{e\text{ bridge}}w_e
=
\sum_{g\in H}\beta_g\ell(g),
\tag{1.3}
$$

and C23 gives `alpha_e<=D w_e`. Therefore

$$
\boxed{
S_{br}:=\sum_{e\text{ bridge}}\alpha_e
\le
D\sum_{g\in H}\beta_g\ell(g).
}
\tag{1.4}
$$

C27 gives at most `2|B|-3<=2pi D-3` contact bridges, so

$$
0\le\ell(g)<2\pi D.
\tag{1.5}
$$

For component response, let `I_r` be the connected components of `C[V\setminus B]`, with attachment sets `A_r subset B`. C41 gives

$$
c_{uv}=c_{uv}^{dir}+\sum_r c_{uv}^{(r)},
\tag{1.6}
$$

where `c_{uv}^{(r)}>0` exactly when `u,v in A_r`, and a direct term occurs only for a loaded-loaded unit contact.

C35.1 is unconditional in fully force-visible C-II: every loaded extreme terminal has

$$
\boxed{1\le\deg_C(b)\le3.}
\tag{1.7}
$$

Thus any loaded terminal belongs to at most three harmonic attachment sets, because distinct components touching it consume distinct contact edges.

Finally C66 defines

$$
\kappa_0=\frac{2\gamma_0}{1+2\gamma_0},
\qquad
C_0=\frac{2\pi}{\kappa_0},
\tag{1.8}
$$

and supplies a diameter vertex `z` with

$$
\boxed{
\sum_{g\ni z}\beta_g\ge1-C_0D\varepsilon.
}
\tag{1.9}
$$

---

## 2. Bridge dominance forces a fixed beta mass onto linearly deep diameter routes

Assume

$$
S_{br}\ge\eta D^2,
\qquad 0<\eta\le1.
\tag{2.1}
$$

Equation (1.4) gives

$$
\sum_{g\in H}\beta_g\ell(g)\ge\eta D.
\tag{2.2}
$$

Put

$$
H_{deep}=\{g\in H:\ell(g)\ge\eta D/2\},
\qquad
p=\sum_{g\in H_{deep}}\beta_g.
\tag{2.3}
$$

Using (1.5),

$$
\sum_g\beta_g\ell(g)
\le
2\pi D\,p+\frac{\eta D}{2}(1-p).
\tag{2.4}
$$

Combining with (2.2) gives

$$
\boxed{
p\ge p_\eta:=\frac{\eta}{4\pi-\eta}>0.}
\tag{ZHC1}
$$

So bridge dominance forces a fixed fraction of the complete normalized diameter KKT measure onto actual diameter pairs whose contact bridge-tree routes have length `Omega(D)`.

---

## 3. Small defect makes almost all of that deep mass response-visible

For a diameter edge `g=uv`,

$$
M_{uv}=\beta_g-c_g.
\tag{3.1}
$$

PSD gives

$$
|M_{uv}|
\le\sqrt{M_{uu}M_{vv}}
\le\frac{M_{uu}+M_{vv}}2
\le\frac{\operatorname{tr}M}{2}
=\varepsilon.
\tag{3.2}
$$

Hence

$$
\boxed{|c_g-\beta_g|\le\varepsilon\qquad(g\in H).}
\tag{3.3}
$$

Define

$$
H_{resp}=\{g\in H_{deep}:\beta_g>2\varepsilon\}.
\tag{3.4}
$$

The omitted deep edges carry at most

$$
2\varepsilon |H|\le2\pi D\varepsilon
\tag{3.5}
$$

of beta mass. Therefore

$$
\sum_{g\in H_{resp}}\beta_g
\ge p_\eta-2\pi D\varepsilon,
\tag{3.6}
$$

and every `g in H_resp` satisfies

$$
c_g\ge\beta_g-\varepsilon>\beta_g/2>0.
\tag{3.7}
$$

---

## 4. C66 turns the fixed deep mass into a star family

Let `z` be the C66 center from (1.9). The total beta mass on diameter edges not incident to `z` is at most

$$
C_0D\varepsilon.
\tag{4.1}
$$

Let

$$
\mathcal S=
\{g\in H_{resp}:z\in g\}.
\tag{4.2}
$$

Subtracting the two exceptional masses from ZHC1 gives

$$
\boxed{
\sum_{g\in\mathcal S}\beta_g
\ge
R_\eta(D):=
p_\eta-(2\pi+C_0)D\varepsilon.
}
\tag{ZHC2}
$$

Along any hypothetical sequence with

$$
D\varepsilon\to0,
\tag{4.3}
$$

we have `R_eta(D)->p_eta>0`.

Thus a fixed fraction of all beta mass is simultaneously:

- incident to one actual diameter vertex `z`;
- supported on diameter pairs of bridge depth at least `eta D/2`; and
- carried by pairs with strictly positive contact-network response.

---

## 5. At most three harmonic cells can receive this star-centered mass

Take `g=zy in mathcal S`. Since `|z-y|=D>1`, there is no direct loaded-loaded contact term in (1.6). Since `c_{zy}>0`, at least one harmonic component satisfies

$$
z,y\in A_r,
\qquad
c_{zy}^{(r)}>0.
\tag{5.1}
$$

Every such component consumes a distinct contact edge incident to `z`. By C35.1, `deg_C(z)<=3`. Therefore the complete family `mathcal S` can use at most three harmonic components in total.

For each `g=zy in mathcal S`, choose a common component `r(g)` maximizing `c_g^(r)`. Since at most three component terms occur,

$$
c_g^{(r(g))}
\ge\frac{c_g}{3}
>\frac{\beta_g}{6}.
\tag{5.2}
$$

Pigeonhole the beta masses over the at most three possible assigned components. There is one unloaded component `I_*` and a subfamily

$$
\mathcal D_*=
\{g\in\mathcal S:r(g)=*\}
\tag{5.3}
$$

such that

$$
\boxed{
\sum_{g\in\mathcal D_*}\beta_g
\ge\frac{R_\eta(D)}3.
}
\tag{ZHC3}
$$

Summing (5.2),

$$
\boxed{
\sum_{g\in\mathcal D_*}c_g^{(*)}
>
\frac{R_\eta(D)}{18}.
}
\tag{ZHC4}
$$

Every `g in mathcal D_*` is an actual diameter edge incident to the same center `z`, has bridge depth at least `eta D/2`, and has both endpoints in the same attachment set `A_*`.

Because `mathcal D_*` is nonempty for large members of a `D epsilon->0` sequence, `A_*` contains a diameter pair and therefore

$$
\operatorname{diam}A_*=D.
\tag{5.4}
$$

No C44 near-minimal hypothesis or macroscopic-component count is used.

---

## 6. The same cell carries a fixed fraction of the full contact stress

Let `E_*` consist of all contact edges internal to `I_*` together with its attachment contacts to `B`. C41's componentwise coordinate-energy identity gives

$$
\sum_{e\in E_*}\alpha_e
=
\sum_{s<t\in A_*}c_{st}^{(*)}|s-t|^2.
\tag{6.1}
$$

Every edge in `mathcal D_*` has length exactly `D`. Restricting the right-hand side,

$$
\boxed{
\sum_{e\in E_*}\alpha_e
>
\frac{R_\eta(D)}{18}D^2.
}
\tag{ZHC5}
$$

Hence if `D epsilon->0`, this one unloaded harmonic cell carries asymptotically at least

$$
\frac{p_\eta}{18}D^2
\tag{6.2}
$$

of the complete `D^2` contact-stress normalization.

---

## 7. One concrete diameter pair has response and beta weight of order 1/D

The family `mathcal D_*` has at most all diameter edges, so by (1.1)

$$
|\mathcal D_*|\le\pi D.
\tag{7.1}
$$

By ZHC4, some `g_*=ab in mathcal D_*` satisfies

$$
\boxed{
 c_{ab}^{(*)}
>
\frac{R_\eta(D)}{18\pi D}.
}
\tag{7.2}
$$

In a sequence with `D epsilon->0`, eventually `R_eta(D)>=p_eta/2`, and therefore

$$
\boxed{
 c_{ab}^{(*)}
\ge
\frac{p_\eta}{36\pi D}.
}
\tag{ZHC6}
$$

Since `c_ab>=c_ab^(*)` and `|c_ab-beta_ab|<=epsilon`, the same asymptotic regime eventually gives

$$
\boxed{
\beta_{ab}
\ge
\frac{p_\eta}{72\pi D}.
}
\tag{ZHC7}
$$

By construction,

$$
\boxed{
\ell(ab)\ge\frac{\eta D}{2}.
}
\tag{ZHC8}
$$

Thus one actual Euclidean-diameter pair in one unloaded harmonic cell simultaneously has

```text
component response conductance >= p_eta/(36 pi D),
KKT diameter weight            >= p_eta/(72 pi D),
contact bridge-tree depth      >= eta D/2.
```

---

## 8. Every bridge on that deep route lies inside the same cell closure

Because `a,b in A_*`, there is a contact path from `a` to `b` consisting only of attachment contacts and edges/vertices of the connected component `I_*`.

A physical contact bridge on the bridge-block-tree route between `a` and `b` separates them in the complete contact graph. Therefore every contact path from `a` to `b` uses that bridge, including the path through `I_*`.

Hence every route bridge belongs to `E_*`, and ZHC8 gives

$$
\boxed{
E_*\text{ contains at least }\eta D/2
\text{ distinct physical contact bridges on one }a\!\text{--}\!b\text{ route}.}
\tag{ZHC9}
$$

This is the route-local structural endpoint: a single unloaded harmonic cell carries quadratic contact stress and contains a response-visible actual diameter pair whose transport path crosses linearly many global articulation edges.

---

## 9. Exact target implication

For every fixed `eta>0`, the conjunction

$$
S_{br}\ge\eta D^2,
\qquad
D\varepsilon\to0
\tag{9.1}
$$

forces one unloaded component `I_*` with all of the following:

1. `diam A_*=D`;
2. `sum_{E_*}alpha_e >= (p_eta/18-o(1))D^2`;
3. assigned exact-diameter component-response mass at least `p_eta/18-o(1)`;
4. assigned deep star-centered beta mass at least `p_eta/3-o(1)`;
5. one actual diameter pair `ab` with `c_ab^(*)>=p_eta/(36pi D)`, `beta_ab>=p_eta/(72pi D)`, and `ell(ab)>=eta D/2`;
6. every one of those `ell(ab)` physical contact bridges belongs to the same harmonic cell closure.

This eliminates the diffuse-component loophole without any C44 assumption. The surviving bridge obstruction is localized inside one actual unloaded harmonic cell attached to the C66 star center.

A sufficient next theorem is:

> **ZHC-cell exclusion.** Exclude an unloaded harmonic cell carrying `Omega_eta(D^2)` contact stress and a response-visible actual diameter pair of conductance `Omega_eta(1/D)` whose route inside the cell contains `Omega_eta(D)` physical contact bridges.

An alternative sufficient conclusion is `epsilon=Omega(1/D)`, a strict sub-`D` competitor, or the exact global face inequality.

---

## 10. Audit and regressions

### Post-ZF C44 reconciliation

The proof does **not** use the C44 Branch A/B dichotomy, its near-minimal premise, or its `K_0` count. The only component-count input is the unconditional C35.1 loaded degree bound at the single C66 center `z`.

### Tiny deep beta weights

ZHC1 prevents bridge-depth expectation from being carried by a vanishing total beta measure: at least `p_eta` beta mass is linearly deep.

### Deep rows with tiny or zero response

Under `D epsilon->0`, rows with `beta<=2epsilon` carry at most `2pi D epsilon=o(1)` total beta mass. Every remaining deep row has `c>beta/2`.

### Nonstar deep rows

C66 bounds their total beta mass by `C_0D epsilon=o(1)`.

### Multiple component realizations of one response pair

A pair incident to `z` can use at most three harmonic components because each common component consumes a distinct contact edge at `z` and `deg_C(z)<=3`. Choosing the largest term loses at most a factor three.

### Direct response

An actual diameter pair cannot be a direct loaded-loaded unit contact because `D>1`.

### Contact-isolated source points

Untouched. The theorem concerns only the fully force-visible nonisolated core; fully inactive rattlers remain outside it.

### Deep bridge-tree route versus narrow contact path

ZHC9 does not make the route a narrow embedded path. Two-edge-connected blocks between consecutive bridges may remain genuinely two-dimensional.

---

## 11. Dependencies

- PR #108 / ZBD: exact diameter-pair bridge-depth identity.
- C23: Helly hub and bridge flow.
- C27: `O(D)` bridge count.
- C35.1: unconditional loaded contact degree at most three.
- C41: component response decomposition and coordinate-energy identity.
- C64: `M succeq0`.
- C65: full diameter visibility.
- C66: mechanical stress-star concentration.
- Hopf--Pannwitz and force-hull perimeter: `|H|<=|B|<=pi D`.

No new external literature is imported.

---

## 12. Promotion recommendation

**Hold as report.** ZHC is downstream of report-level ZR/ZF and stacked PR #108. Do not alter the canonical route map solely from this report.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Assume S_bridge>=eta D^2. ZBD plus the O(D) bridge-tree diameter gives fixed deep mass:
    sum_{ell(h)>=eta D/2} beta_h >= p_eta=eta/(4pi-eta).

If D epsilon->0, pointwise PSD transfer removes only o(1) beta mass from tiny-response
rows, and C66 removes only o(1) from nonstar rows. Hence at the C66 center z,
    deep + responsive + z-star beta mass >= p_eta-o(1).

C35.1 gives deg_C(z)<=3, so z touches at most three unloaded harmonic components.
Assign each deep responsive star edge to a common component carrying the largest share
of its response. One cell I_* captures
    deep star beta >= p_eta/3-o(1),
    exact diameter component response >= p_eta/18-o(1),
    contact stress >= (p_eta/18-o(1))D^2.

One actual diameter pair ab in I_* satisfies
    c_ab^(*) >= p_eta/(36pi D),
    beta_ab >= p_eta/(72pi D),
    ell(ab) >= eta D/2.
Every physical contact bridge on the a--b bridge-tree route lies in the closure of I_*.

No C44 near-minimal assumption is used.
```
