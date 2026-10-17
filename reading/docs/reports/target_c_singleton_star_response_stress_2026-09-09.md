> Generated reading edition · [exact source](../../../docs/reports/target_c_singleton_star_response_stress_2026-09-09.md) · source SHA-256 `8c3d355d9042466b3e05148c86c60e423c5c797e3c44835b539e5c06c2eb351d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1C6FEAC6C58E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — SSR: singleton harmonic stars convert mechanical stress into uniformly short response

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact local response theorem / ESN structural consequence  
**Target:** Target C C-II, especially the ESN near-equality shell  
**Depends on:** C11/C41 harmonic response decomposition and normalized contact stress; C26 unloaded equilibrium  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

ESN shows that a sequence attempting to approach the ENS pinned/contact threshold has

```math
(1.03693311957\ldots)D+o(D)
```

singleton unloaded contact components, all but `o(D)` of them incident to exactly three loaded contacts. Cardinality alone does not control response: a priori all those stars could carry arbitrarily small conductances.

The local equilibrium of a singleton gives an exact quantitative bridge from mechanical contact stress to response mass.

Let `x` be any unloaded singleton component. Let its loaded neighbors be

```math
b_1,\ldots,b_m\in B_+,
```

with positive contact stresses

```math
\alpha_1,\ldots,\alpha_m>0,
\qquad |b_i-x|=1.
```

Put

```math
S_x:=\sum_i\alpha_i.
```

Eliminating `x` from this star produces pair response conductances

```math
c^{(x)}_{ij}=\frac{\alpha_i\alpha_j}{S_x}.
```

Then

```math
\boxed{
\sum_{i<j}c^{(x)}_{ij}\ge\frac{S_x}{4}.
}
\tag{SSR.1}
```

Every pair of loaded neighbors satisfies

```math
|b_i-b_j|\le2.
```

Consequently the C41 diameter-defect trace pays

```math
\boxed{
E_x
:=\sum_{i<j}c^{(x)}_{ij}\bigl(D^2-|b_i-b_j|^2\bigr)
\ge
\frac{D^2-4}{4}S_x.
}
\tag{SSR.2}
```

If `S_sing` is the total contact-stress mass on all unloaded singleton components, then

```math
\boxed{
\operatorname{tr}(\Lambda-L_H)
\ge
\frac12\left(1-\frac4{D^2}\right)S_{sing}.
}
\tag{SSR.3}
```

Equivalently, with the C41 response defect

```math
\varepsilon:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H),
```

one has

```math
\boxed{
S_{sing}
\le
\frac{4\varepsilon}{1-4/D^2}
\qquad(D>2).
}
\tag{SSR.4}
```

Thus the linear singleton population exposed by ESN cannot hide mechanically significant stress in the small-response-defect phase. If `D epsilon ->0`, then

```math
\boxed{S_{sing}=o(1/D).}
\tag{SSR.5}
```

The remaining `D^2-o(1/D)` contact stress must then lie on the non-singleton part of the contact core. Combined with ESN, where only one unloaded component has macroscopic graph diameter, this sharply localizes the mechanical branch that remains to be excluded.

---

## 1. Positive equilibrium bounds each star arm by half the total stress

At the unloaded singleton `x`, KKT equilibrium has no diameter reaction and reads

```math
\sum_i\alpha_i(x-b_i)=0.
\tag{1.1}
```

For each fixed `i`, rearrange:

```math
\alpha_i(x-b_i)
=-\sum_{j\ne i}\alpha_j(x-b_j).
```

Every vector `x-b_j` has norm one. Taking norms and using the triangle inequality gives

```math
\alpha_i
\le
\sum_{j\ne i}\alpha_j
=S_x-\alpha_i.
```

Hence

```math
\boxed{
\alpha_i\le\frac{S_x}{2}
\quad\text{for every }i.
}
\tag{SSR.6}
```

This uses only positive unloaded equilibrium and unit contact lengths. It does not assume `m=3`.

---

## 2. Exact star Kron reduction

The grounded Laplacian block of the singleton is the scalar `S_x`. Schur complementation therefore gives, for distinct loaded neighbors,

```math
\boxed{
c^{(x)}_{ij}=\frac{\alpha_i\alpha_j}{S_x}.}
\tag{SSR.7}
```

The total pair conductance is

```math
\begin{aligned}
C_x
&:=\sum_{i<j}c^{(x)}_{ij}\\
&=\frac1{S_x}\sum_{i<j}\alpha_i\alpha_j\\
&=\frac{S_x^2-\sum_i\alpha_i^2}{2S_x}.
\end{aligned}
\tag{2.1}
```

Normalize `p_i=alpha_i/S_x`. Then `p_i>=0`, `sum p_i=1`, and SSR.6 gives `p_i<=1/2`. Under these constraints,

```math
\sum_i p_i^2\le\frac12.
\tag{2.2}
```

One proof is simply `p_i^2 <= p_i/2` termwise and summation. Thus

```math
C_x
\ge
\frac{S_x}{2}\left(1-\frac12\right)
=\frac{S_x}{4},
```

which proves SSR.1.

There is an independent energy check. The coordinate functions are harmonic at `x` by (1.1), so the star Dirichlet energy satisfies

```math
\sum_{i<j}c^{(x)}_{ij}|b_i-b_j|^2
=\sum_i\alpha_i|x-b_i|^2
=S_x.
\tag{2.3}
```

Since `|b_i-b_j|<=2`, (2.3) also gives `C_x>=S_x/4` immediately.

---

## 3. Every singleton response channel is uniformly short

All loaded neighbors of `x` lie on the unit circle centered at `x`. Therefore

```math
\boxed{|b_i-b_j|\le2.}
\tag{3.1}
```

For every sufficiently large Target C survivor, `D>2`, so these are strict non-diameter response pairs.

The C41 component defect of the singleton is

```math
E_x
=\sum_{i<j}c^{(x)}_{ij}
\bigl(D^2-|b_i-b_j|^2\bigr).
```

By (3.1) and SSR.1,

```math
E_x
\ge(D^2-4)C_x
\ge\frac{D^2-4}{4}S_x.
```

This proves SSR.2.

---

## 4. Sum over singleton components

Different unloaded components have disjoint contact-edge sets. Let `X_sing` be the set of singleton unloaded components and define

```math
S_{sing}:=
\sum_{x\in X_{sing}}S_x.
\tag{4.1}
```

C41 decomposes the full response defect into nonnegative direct loaded-loaded and component contributions:

```math
\frac{D^2}{2}\operatorname{tr}(\Lambda-L_H)
=(D^2-1)\sum_{bb'\in C[B_+]}\alpha_{bb'}
+\sum_r E_r.
\tag{4.2}
```

Discard every term except the singleton contributions and apply SSR.2:

```math
\frac{D^2}{2}\operatorname{tr}(\Lambda-L_H)
\ge
\frac{D^2-4}{4}S_{sing}.
```

Divide by `D^2/2` to obtain SSR.3.

Since C41/C64 gives

```math
\operatorname{tr}(\Lambda-L_H)=2\varepsilon,
```

SSR.4 follows. If `D epsilon ->0`, then `epsilon=o(1/D)` and SSR.4 gives SSR.5.

---

## 5. ESN consequence

At the forbidden ENS endpoint, ESN proves:

- `c_I/D -> c_E=1.03693311957...`;
- one component `I_*` has graph diameter `(lambda_E+o(1))D`;
- the total graph diameter of all other components is `o(D)`;
- hence all but `o(D)` of the other components are singletons;
- all but `o(D)` singleton components have exactly three loaded contacts.

SSR adds an orthogonal, weighted statement.

### Corollary SSR.1 — small response defect evacuates stress from the singleton sea

Along any ESN-type sequence with

```math
D\varepsilon\to0,
```

```math
\boxed{S_{sing}=o(1/D).}
\tag{SSR.8}
```

Because normalized total contact stress is

```math
\sum_{e\in C}\alpha_e=D^2,
```

the singleton sea carries a vanishingly negligible fraction of mechanical stress despite containing `Theta(D)` components.

This does **not** by itself prove that the unique giant component carries `D^2-o(D^2)` stress: ESN permits `o(D)` non-singleton components with submacroscopic graph diameters, and such components could in principle carry substantial stress. The next step must either control their aggregate stress or combine SSR with the existing ZR/ZHH stress-localization machinery.

---

## 6. Relation to E43 and C44/C66

E43 is not needed for SSR itself. It improves the broader response split by making the C43 short-distance constant explicit. SSR is stronger on singleton components because their response distances are at most the absolute constant `2`, rather than merely `(24/25)D`.

In the C66 near-zero phase, where `D epsilon ->0`, SSR.8 gives an especially strong weighted collapse: all singleton contact stress is `o(1/D)`. This can be combined with C66's explicit nonstar diameter-weight bound from E43R,

```math
\sum_{h\not\ni z}\beta_h
\le\frac{723\pi}{49}D\varepsilon,
```

to put both contact stress and diameter reaction into highly concentrated residual structures.

---

## 7. Regression audit

- A balanced three-arm star has `alpha_1=alpha_2=alpha_3`; then `C_x=S_x/3`, comfortably above `S_x/4`.
- The constant `1/4` is sharp in the closure: weights approaching `(S/2,S/2,0)` give total Kron conductance approaching `S/4`. Strict positivity prevents exact equality for a genuine three-arm star but no uniform improvement follows without angular control.
- The theorem applies to singleton components of degree 3, 4, or 5; ESN's degree-three conclusion is not needed for the local inequality.
- Large response trace is allowed. SSR is a conversion theorem, not an upper bound on `tr M`.
- No stress is inferred from singleton count alone.

## 8. Next target

Use SSR to close the small-response-defect half of the ESN shell.

A sufficient next theorem is:

> if all but one unloaded components have total graph diameter `o(D)`, then their total contact stress is `o(D^2)` whenever their total response defect is `o(1)`.

For singleton components SSR proves this with much more room. The unresolved part is the `o(D)` family of non-singleton components. A componentwise extension that lower-bounds response defect in terms of contact stress and graph diameter would force essentially all `D^2` stress into the unique giant component, where ZR/ZHH/bridge-hinge machinery becomes applicable.

## 9. Compact handoff

```text
SSR exact singleton-star theorem.

For an unloaded singleton x with unit contact stresses alpha_i to loaded neighbors b_i,
let S_x=sum alpha_i. Equilibrium gives alpha_i<=S_x/2 for every i.
Kron reduction of the star gives
    c_ij=alpha_i alpha_j/S_x.
Therefore
    sum_{i<j} c_ij >= S_x/4.
Every neighbor pair has distance <=2, so its C41 defect obeys
    E_x >= (D^2-4)S_x/4.
Summing all singleton components:
    tr(Lambda-L_H) >= (1/2)(1-4/D^2) S_sing.
If epsilon=sum c-1=trM/2, then
    S_sing <=4 epsilon/(1-4/D^2).
Thus D epsilon->0 implies S_sing=o(1/D), even if there are Theta(D) singleton stars.

ESN has ~1.0369D singleton components near its forbidden endpoint. SSR says their
mechanical stress is nevertheless negligible in the C66 near-zero response phase.
Next: extend stress-to-response control to the remaining o(D) non-singleton components,
then force D^2 stress into the unique giant component and invoke ZR/ZHH/hinge structure.
```
