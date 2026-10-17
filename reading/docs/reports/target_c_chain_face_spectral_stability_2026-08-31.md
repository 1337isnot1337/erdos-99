> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_face_spectral_stability_2026-08-31.md) · source SHA-256 `9e048fbdf21d507124e2c7b30cab73afd4e7a92a48782567e4826bcd18cc7cf5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6C2BE4C3BC29","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C81: one-edge chain spectral stability

**Date:** 2026-08-31  
**Repository base:** `e0a0b7cf` (main after C80 / PR #85)  
**Run type:** exact matrix perturbation theorem  
**Target:** Target C / Target B cross-route interface  
**Depends on:** C80 exact chain-face train atom; Target B Section 41 train-angle Hessians  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C80 identifies the exact C76 chain bar as a rank-`D-1` negative variance operator on
its `D` parallel train tracks. C81 proves that this macroscopic negative spectrum is
stable whenever one diameter edge retains almost all beta mass.

Let a pure simply connected rhombic source contain the exact C80 chain geometry for a
diameter edge `h_0=za`, with chain-track set `P`, `|P|=D`. Consider any normalized KKT
stress on the same configuration, not necessarily the chain-face stress, and suppose

$$
\beta_{h_0}\ge1-\delta.
$$

Let

$$
Q_s:=\sum_{h\in H}\beta_h H_h
$$

be Target B's stress-projected train-angle Hessian. If `T` is the total number of
trains, then on the `D-1` dimensional zero-sum chain-bending space

$$
W_P:=\left\{v:\operatorname{supp}v\subseteq P,
\ \sum_{\tau\in P}v_\tau=0\right\}
$$

one has

$$
\boxed{
Q_s[v,v]
\le-
\bigl[D-\delta(2D+T)\bigr]\|v\|^2.
}
$$

Consequently, whenever

$$
\delta<\frac{D}{2D+T},
$$

`Q_s` has at least `D-1` negative eigenvalues. In the pure-rhombic asymptotic regime
`T=O(D)`, any `delta=o(1)` gives a spectral gap `(1-o(1))D` on all `D-1` chain-bending
modes.

This is the robust version of C80. It shows that if Target C can strengthen C66 from
**star-center concentration** to **one-edge concentration**, then the ordinary KKT
train Hessian acquires a macroscopic negative index that cannot be erased by the
vanishing residual beta mass.

---

## 1. Uniform operator bound for one diameter Hessian

Use Target B Section 41 train coordinates. For a diameter bar `h`, write

$$
d_{h\tau}\in\{-1,0,1\},
\qquad
a_{h\tau}=d_{h\tau}u_\tau,
\qquad
\lambda_{h\tau}=r_h\cdot a_{h\tau},
$$

where `|r_h|=D` and `|u_tau|=1`.

The train-angle Hessian entries are

$$
(H_h)_{\tau\tau}=d_{h\tau}^2-\lambda_{h\tau},
\qquad
(H_h)_{\tau\sigma}=a_{h\tau}\cdot a_{h\sigma}
\quad(\tau\ne\sigma).
\tag{C81.1}
$$

Since

$$
|\lambda_{h\tau}|\le D,
\qquad
|a_{h\tau}\cdot a_{h\sigma}|\le1,
$$

every diagonal entry has absolute value at most `D+1`, and every off-diagonal entry
has absolute value at most one. A row with `d_{h tau}=0` is identically zero. Every
nonzero row has at most `T-1` off-diagonal entries. Therefore the absolute row-sum
norm obeys

$$
\boxed{
\|H_h\|_{op}\le\|H_h\|_\infty\le D+T.
}
\tag{C81.2}
$$

This crude bound is sufficient and is uniform over all active diameter bars.

---

## 2. Exact chain curvature on W_P

C80 gives, for the chain bar `h_0`,

$$
H_{h_0}[v,v]
=-D\sum_{\tau\in P}(v_\tau-\bar v_P)^2.
\tag{C81.3}
$$

If `v in W_P`, then `bar v_P=0`, so

$$
\boxed{
H_{h_0}[v,v]=-D\|v\|^2.
}
\tag{C81.4}
$$

Thus `H_{h_0}` is exactly `-D I` on the chain-bending subspace `W_P`.

---

## 3. Perturb by the residual diameter mass

Write

$$
b:=\beta_{h_0},
\qquad
\delta':=1-b\le\delta.
$$

Then

$$
Q_s=bH_{h_0}+R,
\qquad
R:=\sum_{h\ne h_0}\beta_hH_h.
\tag{C81.5}
$$

Using C81.2 and `sum_{h ne h0} beta_h=delta'`,

$$
\boxed{
\|R\|_{op}
\le\delta'(D+T)
\le\delta(D+T).
}
\tag{C81.6}
$$

For `v in W_P`, C81.4-C81.6 give

$$
\begin{aligned}
Q_s[v,v]
&\le-bD\|v\|^2+\|R\|_{op}\|v\|^2\\
&\le-\left[(1-\delta)D-\delta(D+T)\right]\|v\|^2\\
&=-\left[D-\delta(2D+T)\right]\|v\|^2.
\end{aligned}
\tag{C81.7}
$$

This proves the quantitative bound.

### Theorem C81 — stable macroscopic negative train curvature

If

$$
\mu:=D-\delta(2D+T)>0,
$$

then `Q_s` is negative definite on `W_P` with spectral gap at least `mu`. In
particular

$$
\boxed{
\nu_-(Q_s)\ge D-1.
}
\tag{C81.8}
$$

The conclusion follows from the min-max principle because `dim W_P=D-1`.

---

## 4. Pure-rhombic asymptotic form

Target B's pure-rhombic shell theory gives

$$
T=\Theta(D).
$$

Suppose along a sequence there is a fixed chain edge `h_0` with

$$
\beta_{h_0}=1-o(1).
$$

Then

$$
\delta(2D+T)=o(D),
$$

so C81.7 becomes

$$
\boxed{
Q_s[v,v]\le-(1-o(1))D\|v\|^2
\qquad(v\in W_P).
}
\tag{C81.9}
$$

Thus the KKT-weighted train Hessian has `D-1` eigenvalues at most
`-(1-o(1))D`.

This is much stronger than the earlier Target B trace estimate

$$
\operatorname{tr}Q_s=-\Theta(D^2),
$$

which by itself does not control the negative index.

---

## 5. Consequence for higher-order blocking

Target B Sections 42--43 show that local survival does not require one fixed KKT
multiplier to have favorable second-order sign; the direction-dependent second-order
stress may change with the train velocity. C81 therefore is not by itself a
contradiction.

It does sharpen the required blocker burden.

If `beta_{h_0}=1-o(1)`, the ordinary stress projects `D-1` independent chain-bending
directions to curvature of order `-D`. The total beta mass on every other diameter bar
is `o(1)`. Hence the actual local-minimality mechanism must obtain all compensating
quadratic/equality/tangent behavior from diameter bars that are asymptotically
invisible in this ordinary multiplier.

This is exactly the mismatch that the Target B higher-order shell-rank theorem did not
previously quantify.

A full contradiction still needs a theorem linking the **available higher-order
blocker rank** to beta mass, or a minimax statement converting direction-dependent
secondary stresses into one stress whose residual mass cannot be `o(1)`.

---

## 6. The missing leaf-selection lemma is now explicit

C66 gives only

$$
S_z:=\sum_{zk\in H}\beta_{zk}=1-o(1)
$$

in the small-response phase. It does **not** imply that one star edge has
`beta=1-o(1)`; the mass may be spread over many leaves.

C79 also does not close this gap: a winner-take-all contact carrier can peel many tiny
diameter loads without a macroscopic forward split.

Therefore C81 isolates the precise next stress-side theorem:

> **One-leaf concentration / multi-leaf defect lemma.** Either some `z`-star diameter
> edge has beta weight `1-o(1)`, or a star with beta mass spread over multiple leaves
> forces a response/radial/reciprocal defect bounded below strongly enough to exclude
> `D epsilon->0`.

A theorem of that form would immediately place the C66 phase in C81's macroscopic
negative-spectrum regime.

---

## 7. Regression audit

- The operator bound `D+T` is intentionally coarse but exact.
- C81 assumes the configuration contains the exact C80 chain geometry for `h_0`; it
  does not prove that a near-star configuration has a nearby literal chain.
- C66 center concentration alone is insufficient for C81.
- Direction-dependent secondary KKT stresses remain a real loophole; no fixed-stress
  second-order necessary condition is assumed.
- The theorem is pure-rhombic because it uses Target B train coordinates.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C81:
Assume a pure-rhombic source contains the exact C80 chain bar h0 with D-track atom P.
For every diameter bar h,
  ||H_h||_op <= D+T.
For a normalized stress with beta_h0 >=1-delta,
  Q_s=sum_h beta_h H_h.
On W_P={v supported on P, sum_P v=0},
  H_h0=-D I.
Therefore
  Q_s[v,v] <= -[D-delta(2D+T)] ||v||^2.
If delta<D/(2D+T), then
  nu_-(Q_s)>=D-1.
If T=O(D) and delta=o(1), the negative gap is (1-o(1))D.

Missing lemma:
upgrade C66 star-center concentration to one-edge concentration, or prove multi-leaf
star mass forces nonvanishing defect.
```
