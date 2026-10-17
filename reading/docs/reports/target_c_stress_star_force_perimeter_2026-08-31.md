> Generated reading edition · [exact source](../../../docs/reports/target_c_stress_star_force_perimeter_2026-08-31.md) · source SHA-256 `6af9b871c6605c2f5feb1dc6bd4055c5a757b61b68f3f1a0fcc847174f0b9c68`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-F76CF5996A82","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C69: stress-star mass forces a reciprocal-perimeter gap

**Date:** 2026-08-31  
**Repository base:** `015707e5` (main after C68 / PR #72)  
**Run type:** exact weighted diameter-reaction estimate  
**Target:** Target C Gate C-II  
**Depends on:** C10 reciprocal force polygon, C14 sixty-degree diameter cone, C66 stress-star concentration  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C66 says that a near-zero C-II response defect forces almost all normalized diameter weight onto one star. C69 records the corresponding exact effect on the reciprocal force polygon.

For a diameter vertex `z`, let

```math
S_z:=\sum_{zk\in H}\beta_{zk}.
```

Then

```math
\boxed{
P_*:=\operatorname{per}(F^*)
\ge D\left(1+\frac{\sqrt3}{2}S_z\right).
}
\tag{C69.1}
```

Consequently the C66 star center satisfies

```math
\boxed{
P_*
\ge
D\left(1+\frac{\sqrt3}{2}\right)
-
\frac{\sqrt3\pi}{\kappa_0}D^2\varepsilon.
}
\tag{C69.2}
```

Thus any hypothetical phase with `D epsilon ->0` obeys

```math
\boxed{
\liminf \frac{P_*}{D}
\ge
1+\frac{\sqrt3}{2}
=1.8660254037\ldots .
}
\tag{C69.3}
```

This separates the surviving C66 phase by a fixed amount from the lower reciprocal-perimeter endpoint `sqrt(3)D`. It is not a contradiction because C10 allows `P_*` up to `2D`.

---

## 1. Reaction notation

For each diameter endpoint `b`, write

```math
s_b:=\sum_{bk\in H}\beta_{bk}
```

and

```math
g_b:=\sum_{bk\in H}\beta_{bk}(b-k).
```

C10 gives

```math
P_*=\sum_b|g_b|.
\tag{C69.4}
```

Put

```math
c:=\cos(\pi/6)=\frac{\sqrt3}{2}.
```

C14 proves the generic local bound

```math
|g_b|\ge cDs_b.
\tag{C69.5}
```

Fix a diameter vertex `z` and put

```math
S:=S_z,
\qquad
\delta:=1-S.
\tag{C69.6}
```

Let `L` be the set of diameter neighbors of `z`. For `k in L`, define

```math
w_k:=\beta_{zk},
\qquad
t_k:=s_k-w_k.
\tag{C69.7}
```

Thus

```math
\sum_{k\in L}w_k=S.
\tag{C69.8}
```

Let

```math
T:=\sum_{k\in L}t_k.
\tag{C69.9}
```

Every edge not incident to `z` has total weight `delta` and contributes to `T` at at most two endpoints, so

```math
0\le T\le2\delta.
\tag{C69.10}
```

---

## 2. Star leaves have a stronger local reaction bound

Fix `k in L` and project `g_k` onto

```math
u_k:=\frac{k-z}{D}.
```

The star edge contributes exactly `Dw_k` in that direction. Every other diameter vector `k-l` makes angle at most `pi/3` with `k-z`, by the same diameter-cone lemma C14.1. Therefore its projection onto `u_k` is at least half its length.

Hence

```math
\begin{aligned}
|g_k|
&\ge g_k\cdot u_k\\
&\ge D\left(w_k+\frac12t_k\right).
\end{aligned}
```

So:

### Lemma C69.1 — loaded star-neighbor reaction

```math
\boxed{
|g_k|
\ge
D\left(w_k+\frac12t_k\right)
\qquad(k\in L).
}
\tag{C69.11}
```

At the center itself, C14 gives

```math
\boxed{|g_z|\ge cDS.}
\tag{C69.12}
```

---

## 3. Sum all reactions

The total diameter-incidence mass is

```math
\sum_b s_b=2.
```

The incidence mass on vertices outside `{z} union L` is therefore

```math
2-S-(S+T)=2\delta-T.
\tag{C69.13}
```

Use C69.12 at `z`, C69.11 on `L`, and the generic C69.5 on all remaining vertices:

```math
\begin{aligned}
\frac{P_*}{D}
&\ge
cS
+
\sum_{k\in L}\left(w_k+\frac12t_k\right)
+
c(2\delta-T)\\
&=
cS+S+\frac12T+2c\delta-cT\\
&=(1+c)S+2c\delta+(1/2-c)T.
\end{aligned}
\tag{C69.14}
```

Since `1/2-c<0`, C69.10 gives the weakest lower bound at `T=2delta`. Therefore

```math
\frac{P_*}{D}
\ge
(1+c)S+\delta.
```

Using `delta=1-S`,

```math
\boxed{
\frac{P_*}{D}
\ge
1+cS.
}
\tag{C69.15}
```

This proves C69.1.

The estimate is strongest when a large fraction of diameter weight shares one endpoint. It complements C14.16, which instead detects weight on diameter-graph leaves.

---

## 4. Insert C66

C66 gives a diameter vertex `z` with

```math
S_z
\ge
1-C_0D\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0}.
\tag{C69.16}
```

Substitute this into C69.1:

```math
\begin{aligned}
P_*
&\ge
D\left(1+c-cC_0D\varepsilon\right)\\
&=
D\left(1+\frac{\sqrt3}{2}\right)
-
\frac{\sqrt3\pi}{\kappa_0}D^2\varepsilon.
\end{aligned}
```

This is C69.2.

If `D epsilon ->0`, divide by `D` to obtain C69.3.

---

## 5. Interpretation and limitation

The exact lower endpoint from C14 is

```math
P_*=\sqrt3D
```

and occurs only for an equal-weight equilateral diameter triangle. C69 shows that the C66 stress-star phase cannot approach that endpoint. Its limiting lower ratio is instead at least

```math
1+\frac{\sqrt3}{2}
=1.8660254\ldots,
```

leaving only the interval

```math
1.8660254\ldots\le P_*/D\le2
```

in the `D epsilon ->0` phase.

This still leaves a real interval. A diameter star whose spoke weights are concentrated near one direction can have reciprocal perimeter close to `2D`, while a two-direction star with comparable weights at the full sixty-degree spread approaches the C69 lower constant. Neither configuration is excluded by convex geometry alone.

C69 therefore supplies a clean scalar diagnostic for the remaining phase, but the closing theorem still has to use the unit-contact carrier, as in C68.

## Compact handoff

For every diameter vertex `z`,

`P_*/D >= 1 + (sqrt(3)/2) S_z`.

At the C66 star center,

`P_* >= (1+sqrt(3)/2)D - (sqrt(3)pi/kappa_0)D^2 epsilon`.

Hence `D epsilon ->0` forces

`liminf P_*/D >= 1+sqrt(3)/2`.

This rules out the low-perimeter/equilateral reaction regime but does not yet contradict the universal upper bound `P_*<=2D`.
