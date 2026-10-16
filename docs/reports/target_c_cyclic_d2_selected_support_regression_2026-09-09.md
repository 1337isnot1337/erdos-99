<!-- theorem-state: {"artifact_id":"ART-9326ADF9D299","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: selected-support stress signs cannot close the phase

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact regression / route elimination  
**Target:** D2R four-transition stress-incompatibility proposal  
**Depends on:** RSP regular odd-shell stress polygon, US/CG selected-stress rank package, D2R/IB  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

D2R reduces a true cyclic `d_H=2` survivor to two statically determinate `D,D,1` triangle-chain bodies joined by four transition unit bars and carrying one positive mixed self-stress. It is tempting to try to contradict KKT positivity using only this selected support.

That route is false.

### Proposition SSR — exact selected-support regression

For every odd `q>=5`, the regular unit `q`-gon at the exact Reinhardt diameter

\[
D_q=\frac1{2\sin(\pi/(2q))}
\]

has a normalized KKT stress whose positive support consists of

- all `q` unit shell contacts;
- exactly `q-2` of its `q` actual diameter edges;
- a diameter support graph
  \[
  \boxed{K_2\sqcup P_{q-2};}
  \]
- strictly positive contact coefficients on every shell side;
- strictly positive diameter coefficients on every selected diameter edge;
- a maximal-rank PSD scalar stress matrix with affine kernel only.

Thus the positive selected mixed framework has precisely the row count and two-tree/four-transition form of a cyclic `d_H=2` circuit, even though the **full actual** diameter graph of the source is still the `q`-edge odd cycle.

Consequently no theorem depending only on

1. the selected support graph;
2. the selected bar geometry;
3. positivity of all selected KKT coefficients;
4. the unique selected equilibrium dependence; or
5. maximal-rank PSD of the selected scalar stress

can exclude the true `d_H=2` phase.

The indispensable distinction is the status of the two omitted diameter rows:

- in SSR they are actual length-`D` chords with coefficient zero;
- in a true `d_H=2` source they are **not** actual diameter pairs. In the canonical difference-body completion their absence is represented by the two units of `d_H=r_parallel+a_short`.

Therefore the next valid attack must use the strict metric defect of those two completion states, not selected-support statics alone.

---

## 1. Exact construction from RSP

RSP classifies the complete normalized KKT stress polygon of the regular odd shell. At every vertex of that polygon exactly two diameter coefficients vanish:

\[
\beta_j=\beta_{j+1}=0
\]

in the RSP vertex indexing, while every other diameter coefficient is strictly positive.

RSP also proves that every contact coefficient remains strictly positive throughout the entire beta-nonnegative stress polygon. Hence at such a polytope vertex the positive support contains all `q` shell contacts and exactly `q-2` diameter edges.

RSP converts the zero pattern to graph/projective diameter order: the two omitted diameter edges are separated by exactly one surviving diameter edge around the full odd diameter cycle. Removing them therefore leaves

\[
H_s=K_2\sqcup P_{q-2}.
\]

This proves the selected-support statement.

---

## 2. The selected stress remains maximal-rank PSD

CG proves in the cyclic endpoint that scalar stress rank does not drop anywhere on the normalized KKT-polytope boundary. In the exact regular shell this is also directly visible from the RSP Fourier description and US interior stress.

Thus at the RSP polygon vertex

\[
\Omega_s\succeq0,
\qquad
\ker\Omega_s=\operatorname{span}\{1,P_x,P_y\},
\qquad
\operatorname{rank}\Omega_s=q-3.
\]

The selected signed equilibrium dependence is one-dimensional at the polytope vertex, so the `2q-2` supported rows form the same rigidity-circuit count as the true `d_H=2` singleton-stress phase.

Hence neither maximal scalar rank nor uniqueness of the selected stress separates the two cases.

---

## 3. D2R/IB geometry is present in the regression

The regular shell has exact shared-endpoint diameter gap at every full-diameter transition. After deleting the two RSP zero edges, all selected within-component consecutive diameter transitions retain the exact `D,D,1` mixed triangle geometry used by D2S/D2R.

The selected `K_2` component and long path component occupy the four alternating boundary blocks supplied by the same convex-thrackle order. Adding all shell contacts gives two isostatic selected bodies joined by four transition shell bars, exactly as in IB.

Therefore a method-of-joints computation on the two selected bodies cannot produce a sign contradiction: SSR itself supplies the positive solution.

This is a binding regression for the proposed D2R four-transition stress-incompatibility theorem.

---

## 4. What differs in a true `d_H=2` source

The full regular SSR source still has

\[
h=q,
\qquad d_H=0.
\]

The two zero-beta rows are omitted only from the **selected stress support**. Geometrically they remain exact diameter chords of length `D`.

A true D2 source instead has

\[
h=q-2,
\qquad d_H=2,
\]

so those two completion states are absent from the actual diameter set.

AD decomposes the missing difference-body states exactly as

\[
d_H=r_{parallel}+a_{short}=2.
\]

The three metric branches are

```text
P2: two parallel-side merges, no short antipodal state;
PS: one parallel merge and one short antipodal state;
S2: two short antipodal states.
```

DP/RP show that their total deviation from the Reinhardt equality scale is extremely small, but it is **strictly nonzero**. That strict metric defect is the only feature not reproduced by SSR.

---

## 5. Consequence for future proof design

The following proposed implication is invalid:

```text
two d_H=2 isostatic D,D,1 bodies
+ four unit transition bars
+ positive unique KKT stress
+ maximal-rank PSD
=> contradiction.
```

SSR is an exact counterexample to the selected-support implication.

Any valid D2 closing theorem must contain at least one hypothesis that detects the two missing **actual** diameter states. Suitable currencies include:

1. the strict short-state deficits in AD's S branches;
2. the exact parallel-side merges in AD's P branches;
3. the two strict cross-tree projective gap defects from D2S/DGE;
4. an envelope/second-order KKT term measuring movement away from the `d_H=0` Reinhardt stress-polygon boundary.

This also explains why purely sign-based WM/WT calculations are likely to saturate: at zero metric defect they must admit the SSR solution.

---

## 6. A sharpened perturbative target

The right local problem is now a **two-defect transversality theorem**.

Let `epsilon_1,epsilon_2` measure the two AD completion defects, chosen as either

- short-chord deficits `D-|h_i^*|` in an S cell; or
- the corresponding support-angle/parallel merge parameter in a P cell.

At `(epsilon_1,epsilon_2)=(0,0)` the SSR/Reinhardt boundary stress exists. A true D2 source has a positive defect vector.

The target is to prove that along every geometry preserving

- all `q` unit shell contacts;
- the `q-2` selected actual diameter equalities;
- KKT positivity on their unique stress;

one has a one-sided obstruction

\[
\Phi(\epsilon_1,\epsilon_2)>0
\]

for every nonzero admissible defect vector, where `Phi` can be any exact-attainment quantity: a selected diameter becoming longer than `D`, a shell side ceasing to be unit/convex, or failure of C56-G/PSD.

Because the base stress has zero multipliers on exactly the two missing rows, a first-order scalar KKT argument may vanish identically. Second-order or exact finite geometry is likely necessary.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| regular d0 shell has a stress with exactly q-2 positive diameter rows | proved | RSP vertex classification |
| selected H is `K2 sqcup P_(q-2)` | proved | RSP projective reindexing |
| all selected alpha/beta signs are KKT-positive | proved | RSP beta polygon + strict contact positivity |
| selected scalar stress remains maximal-rank PSD | proved downstream of CG / direct regular symmetry |
| selected framework has d2 row/circuit count | proved | q contacts + q-2 diameters, one extreme dependence |
| sign-only D2R incompatibility route | refuted | exact SSR regression |
| true d2 source excluded | open | missing actual-diameter metric defect not yet exploited |

---

## 8. Next target

Work directly with AD's P2/PS/S2 two-defect coordinates and the D2R triangle-chain geometry. Linearize the unique selected KKT stress and the two omitted completion chord lengths at the SSR/Reinhardt boundary point.

The desired result is a second-order sign or envelope obstruction showing that the d0 polytope vertex is one-sided: the selected positive circuit cannot persist after both omitted diameter constraints become genuinely inactive while the shell remains an exact unit cycle at the same diameter.
