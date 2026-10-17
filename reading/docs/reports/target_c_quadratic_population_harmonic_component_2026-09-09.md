> Generated reading edition · [exact source](../../../docs/reports/target_c_quadratic_population_harmonic_component_2026-09-09.md) · source SHA-256 `bbf43d673a8b7427ab56c150c453537a0fa115a3eb34f8534c08a9831c22ff3d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9B8B140E5E19","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — positive-density core forces a quadratic-population harmonic component

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** finite packing / component concentration theorem  
**Target:** UF near-circle harmonic-component branch  
**Depends on:** C36/C44 attachment cells, Oler, NBd near-circle total-diameter budget  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

MC/CH/LC force one harmonic component with graph diameter `Omega(D)`. A separate concentration argument shows that some harmonic component must also contain `Theta(D^2)` unloaded vertices whenever the force-visible core has positive quadratic density.

Let

$$
\Delta:=\frac\pi{2\sqrt3}.
$$

Along a PR #119 near-circle subsequence suppose

$$
\frac v{D^2}\to r>0.
$$

Then

$$
\boxed{
\liminf
\max_r\frac{n_r}{D^2}
\ge
\frac{r^2}{4\pi^2\Delta}.
}
\tag{QP.1}

$$

In the UF notation `r=Delta-zeta`, this is

$$
\boxed{
\liminf
\max_r\frac{n_r}{D^2}
\ge
\frac{(\Delta-\zeta)^2}{4\pi^2\Delta}.
}
\tag{QP.2}

$$

At the UF worst crossover `zeta_*=0.5572837714...`, the certified component density is

$$
\boxed{0.0034139990\ldots D^2.}
\tag{QP.3}

$$

At the asymptotically full-core endpoint it is at least

$$
\boxed{
\frac{\Delta}{4\pi^2}D^2
=0.0229720373\ldots D^2.
}
\tag{QP.4}

$$

The constants are conservative. The point is qualitative but strong: the live harmonic obstruction contains an actual positive-density two-dimensional contact component, not only a long sparse spine.

---

## 1. One component has capacity `Delta delta_r^2+O(delta_r)`

For an unloaded component `I_r`, write

$$
n_r=|I_r|,
\qquad
P_r=\operatorname{conv}A_r,
\qquad
\delta_r=\operatorname{diam}_{C[I_r]}I_r.
$$

C36 gives

$$
I_r\subseteq P_r.
$$

C44 gives

$$
\operatorname{diam}(P_r)
\le\delta_r+2.
\tag{1.1}
$$

The `n_r` points of `I_r` are unit-separated. Apply Oler to those points in the convex container `P_r`:

$$
a_0(n_r-1)
\le
\operatorname{area}(P_r)
+\frac{a_0}{2}\operatorname{per}(P_r),
\qquad
a_0=\frac{\sqrt3}{2}.
\tag{1.2}
$$

The isodiametric and perimeter-diameter inequalities give

$$
\operatorname{area}(P_r)
\le
\frac\pi4(\delta_r+2)^2,
$$

and

$$
\operatorname{per}(P_r)
\le
\pi(\delta_r+2).
$$

Therefore

$$
\boxed{
 n_r
\le
1+\Delta(\delta_r+2)^2
+\frac\pi2(\delta_r+2),
}
\tag{QP.5}
$$

because

$$
\frac{\pi}{4a_0}=\Delta.
$$

In particular

$$
 n_r\le\Delta\delta_r^2+O(\delta_r+1)
\tag{1.3}
$$

with absolute implied constants.

---

## 2. Small-diameter components cannot carry quadratic population

Put

$$
S:=\sum_r\delta_r.
$$

NBd gives in the near-circle branch

$$
S\le q+2x_B=(\pi+o(1))D.
\tag{2.1}
$$

Fix `epsilon>0` and split the components into

$$
\mathcal S_\epsilon:=\{r:\delta_r<\epsilon D\}
$$

and

$$
\mathcal L_\epsilon:=\{r:\delta_r\ge\epsilon D\}.
$$

For the small components, use

$$
\sum_{\mathcal S_\epsilon}\delta_r^2
\le
\epsilon D\sum_r\delta_r
\le
(\pi\epsilon+o(1))D^2.
$$

Summing QP.5 and using `c_I=O(D)` gives

$$
\boxed{
\sum_{\mathcal S_\epsilon}n_r
\le
(\Delta\pi\epsilon+o(1))D^2.
}
\tag{2.2}
$$

The number of large components satisfies

$$
|\mathcal L_\epsilon|\epsilon D
\le S,
$$

so

$$
\boxed{
|\mathcal L_\epsilon|
\le\frac\pi\epsilon+o(1).
}
\tag{2.3}
$$

Thus only `O_epsilon(1)` large components remain.

---

## 3. Pigeonhole the positive-density population

Since

$$
v=q+\sum_r n_r,
$$

and `q=O(D)`, the unloaded population satisfies

$$
\sum_r n_r=(r+o(1))D^2.
\tag{3.1}
$$

Equations (2.2)--(2.3) show that the large components carry at least

$$
\left(r-\Delta\pi\epsilon-o(1)\right)D^2
$$

vertices and there are at most `pi/epsilon+o(1)` of them. Therefore one component satisfies

$$
\max_r n_r
\ge
\left[
\frac{\epsilon}{\pi}
\left(r-\Delta\pi\epsilon\right)
-o(1)
\right]D^2.
\tag{3.2}
$$

The bracket is a concave quadratic in `epsilon`. It is maximized at

$$
\epsilon_*
=\frac{r}{2\Delta\pi},
$$

which lies in `(0,1)` because `0<r<=Delta` and `2pi>1`. Substitution gives

$$
\boxed{
\max_r n_r
\ge
\left(
\frac{r^2}{4\pi^2\Delta}-o(1)
\right)D^2.
}
$$

This proves QP.1.

---

## 4. Relation to the macroscopic-diameter component

QP does not by itself prove that the component maximizing `n_r` is the same component maximizing `delta_r`. That distinction matters.

However QP combines with LC/TD to reduce the harmonic obstruction to finitely many macroscopic components:

- the total normalized graph-diameter budget is `O(1)`;
- components below any fixed diameter fraction carry only the controlled fraction (2.2) of the population;
- a fixed finite family of macroscopic components therefore carries all but an arbitrarily small chosen fraction of the positive-density core population.

In the TD cap-minimal full-core endpoint, the optimizer has only two diameter-one maximal cap groups. The small-cap estimate then forces all but `o(D^2)` unloaded vertices into those two groups. If, additionally, the total diameter cost satisfies `S/D->2`, the two defining diameter-scale components are the only macroscopic-diameter components; any separate quadratic-population component would itself require another positive diameter cost. Thus the equality regime reduces to two positive-density half-disk carriers.

Away from the cap minimum, QP deliberately makes no identification between the largest-population and largest-diameter components.

---

## 5. Why this matters for the next proof step

The main regressions against C66/C72 allowed a long high-stress spine with arbitrarily light transverse geometry. QP shows that the live near-circle harmonic obstruction cannot be only such a sparse carrier. Somewhere in the harmonic decomposition there is a connected triangle-free unit-contact component containing `Theta(D^2)` vertices.

This opens local use of:

1. Eppstein's edge/diameter theorem on the component itself;
2. stopped-rhombic-train and squaregraph arguments inside one attachment cell;
3. finite-packing boundary corrections such as Wegner on one macroscopic component;
4. interface stability in the TD two-cap equality regime.

The remaining difficulty is to couple this positive-density component to the diameter-scale component when they are not the same member of the decomposition.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| component capacity QP.5 | proved | Oler + C44 + isodiametric/perimeter bounds |
| small components carry at most `Delta pi epsilon D^2` | proved | `sum delta^2<=epsilon D S` + NBd `S<=pi D+o(D)` |
| only `O(1/epsilon)` large components | proved | total diameter budget |
| QP.1 quadratic-population component | proved | optimized pigeonhole |
| largest-population component equals LC largest-diameter component | not proved generally | separate components may carry the two extrema |
| full-core cap-minimal regime reduces to two positive-density cap groups | proved at leading equality | TD optimizer + small-cap population bound |
| Level I | still open | local dense-component theorem still needed |

---

## 7. Next target

The highest-value next target is now a **dense harmonic component boundary theorem**.

For one connected component with

$$
n_r\ge cD^2,
\qquad
\operatorname{diam}(P_r)\le\delta_r+2=O(D),
$$

use its pinned-positive equilibrium and the fact that every extreme vertex of `conv(I_r)` must be directly loaded to compare

- its internal penny-graph outer-face length,
- its attachment-contact count `t_r`, and
- the perimeter/shape of its circular cap.

A coefficient improvement over the bare C40 bound `t_r>=delta_r+3` on this positive-density subclass would feed directly into NBd and could close part of the UF population range.
