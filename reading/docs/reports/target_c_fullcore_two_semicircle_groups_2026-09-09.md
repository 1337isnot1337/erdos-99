> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_two_semicircle_groups_2026-09-09.md) · source SHA-256 `77ccdaf686952cfd31f9ff8955d6baa226ad7d9fa4ba62f65de6e21bac43a831`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-86FE74A88880","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_two_semicircle_groups_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=1f1d8442d5d2e35923ec5f625bc19f3bd3756202; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — every full-core near-circle survivor splits into two half-density semicircle groups

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** asymptotic equality classification without cap-minimality  
**Target:** full-core `x_B=o(D)` near-circle branch  
**Depends on:** repaired LC/TR maximal-cap decomposition, AR groupwise Oler capacity, DC disk convergence, C49 disjoint attachment cells  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

TD/TS identified two complementary semicircle carriers under the additional cap-cost equality `S/D->2`. The **geometric two-half-disk decomposition itself does not require that equality**.

Assume only the full-core near-circle hypotheses

$$
x_B=o(D),
\qquad
\frac{n-v}{D^2}\to0.
$$

Then the repaired maximal-cap decomposition contains two inclusion-maximal attachment arcs whose normalized angular lengths tend to `pi`, while every other maximal cap has total normalized area tending to zero.

Grouping every harmonic component under the inclusion-maximal cap containing its attachment arc, there are two dominant groups `G_1,G_2` such that

$$
\boxed{
\sum_{r\in G_i}\frac{n_r}{D^2}
\to\frac\Delta2,
\qquad i=1,2,
}
\tag{HG.1}

$$

where

$$
\Delta=\frac\pi{2\sqrt3}.
$$

Each group lies asymptotically in one semicircular cap, and the two caps are complementary. Every remaining maximal-cap group contains only `o(D^2)` unloaded vertices.

The component defining each dominant maximal arc has attachment diameter `(1-o(1))D` and hence graph diameter `(1-o(1))D` by C44. Thus **every** full-core near-circle survivor contains two diameter-scale harmonic components, although those two components need not themselves contain the full half-density populations unless `S/D->2`.

---

## 1. Full-core Oler saturation of the attachment cells

Let `P_r=conv(A_r)` be the C49 attachment cells. AR gives

$$
\sum_r\operatorname{area}(P_r)
\ge
 a_0(v-q)-O(S+c_I),
\qquad a_0=\frac{\sqrt3}{2}.
\tag{1.1}
$$

In the near-circle branch, NBd gives `S=O(D)` and HBd gives `c_I=o(D)`, while `q=O(D)`. Full core gives

$$
\frac v{D^2}\to\Delta.
$$

Since

$$
a_0\Delta=\frac\pi4,
$$

we obtain

$$
\liminf\frac1{D^2}\sum_r\operatorname{area}(P_r)
\ge\frac\pi4.
\tag{1.2}
$$

But the cell interiors are pairwise disjoint and lie in the force hull, while DC gives

$$
\operatorname{area}(F)/D^2\to\pi/4.
$$

Therefore

$$
\boxed{
\frac1{D^2}\sum_r\operatorname{area}(P_r)
\to\frac\pi4.
}
\tag{HG.2}

$$

Thus the harmonic attachment cells asymptotically fill the entire force-hull disk in area.

---

## 2. Maximal cap union must fill the disk

Use the repaired LC/TR construction. Let

$$
J_{1,D},\ldots,J_{m_D,D}
$$

be the inclusion-maximal supporting intervals of the attachment cells along the loaded convex boundary. Their relative interiors are disjoint. Let `theta_{j,D}` be their normalized disk-centered angular lengths.

Every attachment cell in the group below `J_j` lies inside the corresponding circular cap in the disk limit. Hence the total cell area is at most the total maximal-cap area plus `o(D^2)`.

For macroscopic limiting arcs with angles

$$
0\le\theta_j\le\pi,
\qquad
\sum_j\theta_j\le2\pi,
$$

the radius-`1/2` cap areas sum to

$$
\sum_j\frac18(\theta_j-\sin\theta_j)
=
\frac18\sum_j\theta_j-rac18\sum_j\sin\theta_j.
\tag{2.1}
$$

HG.2 forces this sum to approach `pi/4`. Since

$$
\frac18\sum_j\theta_j\le\frac\pi4
$$

and every `sin(theta_j)>=0`, equality at leading order requires simultaneously

$$
\sum_j\theta_j\to2\pi
\tag{2.2}
$$

and

$$
\sum_j\sin\theta_j\to0.
\tag{2.3}
$$

On `[0,pi]`, `sin theta` vanishes only at `0` and `pi`. Therefore every macroscopic maximal arc has limiting angle `pi`; all other maximal arcs have angle tending to zero.

Because the total limiting angular mass is `2pi`, there are exactly two macroscopic maximal arcs, each tending to `pi`.

### Theorem HG.1 — two dominant maximal caps

After relabeling, there are two maximal groups `G_1,G_2` whose containing caps converge to complementary semicircles. Every other maximal group has total normalized cap area tending to zero.

The complementarity follows from disjointness of maximal arc interiors and total angular length `2pi+o(1)`.

---

## 3. Each dominant group contains half the core population

Let

$$
N_i:=\sum_{r\in G_i}n_r.
$$

The cells in one dominant group are interior-disjoint and lie in one semicircular cap of normalized area `pi/8+o(1)`.

Apply the AR/Oler lower bound componentwise but sum only over the group:

$$
a_0N_i
\le
\sum_{r\in G_i}\operatorname{area}(P_r)
+O\left(\sum_{r\in G_i}\delta_r+c_{I,i}+D\right).
\tag{3.1}
$$

The group diameter sum is at most global `S=O(D)` and `c_{I,i}<=c_I=o(D)`, so the error is `o(D^2)`. Therefore

$$
\limsup\frac{N_i}{D^2}
\le
\frac{\pi/8}{a_0}
=rac\Delta2.
\tag{3.2}
$$

The remaining maximal groups have total cap area `o(D^2)`. The same groupwise Oler estimate shows their total unloaded population is `o(D^2)`.

Full core gives

$$
\sum_rn_r=(\Delta+o(1))D^2.
$$

Thus

$$
N_1+N_2=(\Delta+o(1))D^2,
$$

and the two separate upper bounds (3.2) force

$$
\boxed{
N_1=N_2=(\Delta/2+o(1))D^2.
}
$$

This proves HG.1.

The same squeeze shows the total attachment-cell area in each dominant group tends to `pi D^2/8`; both half-disk groups are Oler-saturated at leading order.

---

## 4. Each dominant group has a diameter-scale defining component

Let `I_i^*` be the harmonic component whose attachment interval is the inclusion-maximal interval defining group `G_i`.

The two extreme attachment terminals of `I_i^*` converge to the endpoints of a semicircle, so their Euclidean distance is

$$
(1-o(1))D.
$$

C44 gives

$$
\operatorname{diam}(A_i^*)\le\delta_i^*+2.
$$

Hence

$$
\boxed{
\delta_i^*/D\to1,
\qquad i=1,2.
}
\tag{4.1}

$$

Thus two diameter-scale harmonic components exist without assuming `S/D->2`.

What cap-minimality adds in TS is population concentration: if the two defining components already spend the minimum possible total diameter `2D+o(D)`, all nested components have total diameter `o(D)` and hence only `o(D^2)` population, forcing the defining components themselves to carry `Delta/2` each.

Without cap-minimality, a dominant semicircle group may contain nested mesoscopic/macroscopic components sharing its half-density population.

---

## 5. Groupwise Eppstein cost

Eppstein's triangle-free penny-graph edge theorem gives, for every component,

$$
\delta_r+r_r
\ge
c_E\sqrt{n_r}-O(1),
\qquad
c_E:=\frac12\sqrt{2\pi\sqrt3}.
\tag{5.1}
$$

Sum over one dominant group. HBd gives `c_I=o(D)`, so the accumulated `O(1)` error is `o(D)`. Since

$$
\sum_{r\in G_i}\sqrt{n_r}
\ge
\sqrt{\sum_{r\in G_i}n_r},
$$

HG.1 gives

$$
\sum_{r\in G_i}(\delta_r+r_r)
\ge
c_E\sqrt{\Delta/2}\,D-o(D).
$$

The coefficient simplifies to

$$
c_E\sqrt{\Delta/2}
=rac\pi{2\sqrt2}.
$$

Therefore

$$
\boxed{
\sum_{r\in G_i}(\delta_r+r_r)
\ge
\left(\frac\pi{2\sqrt2}-o(1)\right)D,
}
\tag{HG.3}

$$

and globally

$$
\boxed{
S+R_I
\ge
\left(\frac\pi{\sqrt2}-o(1)\right)D
= (2.2214414690\ldots-o(1))D.
}
\tag{HG.4}

$$

This bound is weaker than SI/TS in the cap-minimal equality branch but holds throughout the full-core near-circle branch.

---

## 6. Consequence for the remaining stress/degree budget

NC and HBd simplify NBd to

$$
S+R_I+s_B+s_C=(\pi+o(1))D.
$$

Insert HG.4:

$$
\boxed{
 s_B+s_C
\le
\left(\pi-\frac\pi{\sqrt2}+o(1)\right)D
= (0.9201511845\ldots+o(1))D.
}
\tag{6.1}

$$

HBd also gives

$$
Q+2s_C=(\pi+o(1))D.
$$

Discarding `s_B>=0` therefore gives the independent full-core floor

$$
\boxed{
Q
\ge
\left(\frac{2\pi}{\sqrt2}-\pi-o(1)\right)D
=
(1.3012902846\ldots-o(1))D.
}
\tag{6.2}

$$

UF's exposed-train bound `1.390168...D` is stronger numerically, but HG.4 is structurally different: it comes entirely from the two half-density harmonic groups and the penny-graph edge deficit.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| total attachment-cell area -> disk area | proved | AR Oler lower + C49 disjointness + DC force-hull area |
| maximal cap union must be two semicircles | proved | cap-area equality forces total angle `2pi` and `sum sin theta->0` |
| each dominant cap group has `Delta/2 D^2` population | proved | groupwise Oler upper + total population |
| each group has a diameter-scale defining component | proved | semicircle endpoint chord + C44 |
| groupwise `S+R` cost `pi/(2sqrt2)D` | proved | Eppstein + Cauchy on square roots |
| defining component itself has half-density population | not proved without `S/D->2` | nested components may share population |
| Level I | still open | two nested half-disk groups remain feasible |

---

## 8. Next target

HG removes the cap-minimality assumption from the two-half-disk geometry. The full-core near-circle obstruction is now always:

```text
two complementary semicircle groups,
each with (Delta/2+o(1))D^2 unloaded vertices,
each containing a diameter-scale defining harmonic component,
c_I=o(D),
S+R_I >= (pi/sqrt2-o(1))D.
```

The next target is a **group-level stopped-train theorem**. Instead of applying DT separately to individual nested components, glue the train systems of all components in one semicircle group across their common loaded attachment boundary and quantify the train loss caused by nesting. If nesting has sublinear cost, the squaregraph `2sqrt(n)` boundary deficiency should apply at the group population `Delta/2 D^2`, potentially strengthening HG.3 from `pi/(2sqrt2)D` toward the exact squaregraph coefficient `sqrt(pi/sqrt3)D` per group.