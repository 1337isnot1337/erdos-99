> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_macroscopic_train_alignment_2026-09-09.md) · source SHA-256 `36434bf652f836935644239aa11421c49a50e5f02d6730264d76af7cc6009b8c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 8 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-EFF890A78FAE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZMA: macroscopic global train cuts align with the stress-star cone

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111 / ZGS  
**Run type:** mechanical alignment of exact global train shears  
**Target:** bridge-dominant near-zero / global outer-train branch  
**Depends on:** ZGS, C18, C66  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZGS shows that every stopped train whose two endpoints lie on the actual global outer face is an exact contact cut. If its total contact KKT stress is

```math
A_\tau:=\sum_{e\in\tau}\alpha_e,
```

then summing KKT equilibrium over one train shore gives

```math
A_\tau u_\tau
=
\sum_{h\pitchfork\tau}\beta_h r_h,
```

where `u_tau` is the common unit cut-edge direction and the crossing diameter vectors `r_h` are consistently shore-oriented.

In the C66 near-zero phase, all but `o(1)` of the normalized diameter `beta` mass is incident to one stress-star center `z`. C18 puts every diameter partner direction at `z` inside one projective cone of asymptotic width

```math
\theta_\infty
:=\frac{5\pi}{6}-\sqrt3
=0.8859430704\ldots
=50.7607988\ldots^\circ
<\frac\pi3.
```

Therefore any outer train cut with `A_tau>=cD` for fixed `c>0` has direction within `o_c(1)` of that same star cone. Two such macroscopic train directions differ projectively by less than `pi/3` for large `D`, while two crossing trains require projective separation strictly greater than `pi/3`.

Hence:

```math
\boxed{
\text{for every fixed }c>0,
\text{ all global outer trains with }A_\tau\ge cD
\text{ are pairwise noncrossing for large }D.
}
```

This is the first direct interaction between the ZGS exact train-shear family and the C66 stress-star phase.

---

## 1. Stress-star notation

Work along a hypothetical C-II sequence with

```math
D\varepsilon\to0,
\qquad
\varepsilon=\frac12\operatorname{tr}(\Lambda-L_H).
\tag{1.1}
```

C66 supplies a diameter vertex `z` for which the total normalized diameter stress outside the star at `z` satisfies

```math
\boxed{
\tau_z
:=
\sum_{h\not\ni z}\beta_h
=o(1).
}
\tag{ZMA1}
```

The full normalized diameter mass is

```math
\sum_{h\in H}\beta_h=1.
```

C18 supplies a finite-width bound `Theta(D)` on partner directions at any diameter vertex, with

```math
\boxed{
\Theta(D)\longrightarrow
\theta_\infty
=\frac{5\pi}{6}-\sqrt3
<\frac\pi3.
}
\tag{ZMA2}
```

Thus all unit vectors

```math
\frac{k-z}{D}
\qquad(zk\in H)
```

lie in one oriented angular interval of width at most `Theta(D)`. Reversing all of them gives the antipodal interval; projectively this is the same cone.

---

## 2. Exact train-cut resultant

Let `tau` be a global outer-to-outer stopped train. Use ZGS notation and orient its shores so every train contact crossing from `T_tau` to `S_tau` has vector

```math
u_\tau.
```

Put

```math
A_\tau:=\sum_{e\in\tau}\alpha_e>0.
```

For every active diameter edge crossing the same shore cut, orient

```math
r_h=p_s-p_t,
\qquad s\in S_\tau,\ t\in T_\tau.
```

ZGS gives the exact vector equation

```math
\boxed{
A_\tau u_\tau
=
\sum_{h\pitchfork\tau}\beta_h r_h.
}
\tag{ZMA3}
```

Divide by `D` and write

```math
a_\tau:=\frac{A_\tau}{D}.
```

Then

```math
a_\tau u_\tau
=
V_{\star}+V_{\rm off},
\tag{2.1}
```

where

```math
V_{\star}
:=
\sum_{\substack{h\pitchfork\tau\\h\ni z}}
\beta_h\frac{r_h}{D},
\qquad
V_{\rm off}
:=
\sum_{\substack{h\pitchfork\tau\\h\not\ni z}}
\beta_h\frac{r_h}{D}.
\tag{2.2}
```

Because every diameter vector has length `D`,

```math
\boxed{
|V_{\rm off}|
\le
\sum_{h\not\ni z}\beta_h
=\tau_z.
}
\tag{ZMA4}
```

---

## 3. All crossing star vectors use one oriented star cone

The center `z` lies on exactly one shore of the train cut.

If `z in T_tau`, every crossing star edge is `zk` with `k in S_tau`, and the shore-oriented vector is

```math
r_{zk}=k-z.
```

If `z in S_tau`, every crossing star edge has partner `k in T_tau` and shore-oriented vector

```math
r_{zk}=z-k=-(k-z).
```

Thus **all** crossing star vectors use the same orientation sign. Their normalized directions lie in one angular cone `K_z(tau)` of width at most `Theta(D)`, equal either to the C18 partner cone or to its antipode.

Because all coefficients `beta_h` are nonnegative,

```math
\boxed{V_{\star}\in K_z(\tau)}
\tag{ZMA5}
```

where `K_z(tau)` denotes the closed convex cone generated by those oriented unit star directions, including the origin.

Projectively every `K_z(tau)` is the same C18 star cone.

---

## 4. A macroscopic train direction is close to the star cone

Fix `c>0` and suppose

```math
A_\tau\ge cD,
\qquad
a_\tau\ge c.
\tag{4.1}
```

Equation (2.1) and ZMA4 give

```math
\operatorname{dist}(a_\tau u_\tau,K_z(\tau))
\le\tau_z.
\tag{4.2}
```

Let `phi_tau` be the angular distance from the ray `R_+u_tau` to the cone `K_z(tau)`. Once `tau_z<c`, (4.2) implies `phi_tau<pi/2`; otherwise the distance from `a_tau u_tau` to the cone would be at least `a_tau>=c`.

For `phi_tau<pi/2`, the Euclidean distance from `a_tau u_tau` to the nearest ray in the cone is

```math
a_\tau\sin\phi_\tau.
```

Hence

```math
a_\tau\sin\phi_\tau
\le\tau_z.
```

Therefore

```math
\boxed{
\phi_\tau
\le
\arcsin\frac{\tau_z}{a_\tau}
\le
\arcsin\frac{\tau_z}{c}
=o_c(1).
}
\tag{ZMA6}
```

Thus every fixed-scale macroscopic global train direction is asymptotically trapped in the same projective C18 star cone.

---

## 5. Macroscopic global trains cannot cross

Let `tau_1,tau_2` be two global outer-to-outer trains satisfying

```math
A_{\tau_i}\ge cD.
```

By ZMA6 their projective directions lie within `o_c(1)` of the same projective cone of width at most `Theta(D)`.

Hence their projective angular separation satisfies

```math
\operatorname{dist}_{\mathbb{RP}^1}(u_{\tau_1},u_{\tau_2})
\le
\Theta(D)+2o_c(1).
\tag{5.1}
```

By ZMA2, for sufficiently large `D`,

```math
\Theta(D)+2o_c(1)<\frac\pi3.
```

But DT proves that if two trains cross in a strict unit rhombus, the acute projective angle between their contact-edge directions is strictly greater than `pi/3`.

Contradiction.

Thus:

### Theorem ZMA.1 — macroscopic outer trains are pairwise noncrossing

For every fixed `c>0`, all sufficiently large C66 survivors satisfy

```math
\boxed{
A_{\tau_1},A_{\tau_2}\ge cD
\quad\Longrightarrow\quad
\tau_1,\tau_2\text{ do not cross.}
}
\tag{ZMA7}
```

Equivalently, every rhombus crossing of two global outer-to-outer trains has

```math
\boxed{
\min(A_{\tau_1},A_{\tau_2})<cD
}
\tag{ZMA8}
```

for every fixed `c>0` and all sufficiently large `D`.

Since `c` is arbitrary, along any sequence of train crossings in the near-zero phase, at least one of the two train total stresses is `o(D)` after subsequence diagonalization.

---

## 6. Laminarity and ordered slabs

Two disjoint outer-to-outer train midpoint curves are proper simple arcs of the force-hull disk with endpoints on the outer face. If they do not cross, their Jordan closures through the outer face can be chosen as a laminar family of cuts.

Therefore, for fixed `c>0`, the macroscopic train cuts form an ordered noncrossing family. Their shores partition the contact core into slabs.

An active diameter edge crosses a consecutive interval of those ordered cuts. This interval structure is the exact multi-shear geometry left after ZMA7.

It is stronger than the arbitrary circular-split matrix in ZGS but still admits a two-sided diameter cusp across a nested cut family.

---

## 7. Stress dichotomy for any linear train family

Let `mathcal T_D` be any family of pairwise distinct global outer trains with

```math
|\mathcal T_D|\ge\kappa D
```

for fixed `kappa>0`.

For fixed `c>0`, split

```math
\mathcal T_D
=
\mathcal T_D^{\rm mac}(c)
\sqcup
\mathcal T_D^{\rm light}(c),
```

where `A_tau>=cD` on the first set.

ZMA1 makes `mathcal T_D^{mac}(c)` pairwise noncrossing. Every train in the light set satisfies

```math
A_\tau<cD.
```

Since distinct trains partition the contact-edge set,

```math
\sum_{\tau\in\mathcal T_D^{\rm light}(c)}A_\tau
<cD\,|\mathcal T_D^{\rm light}(c)|.
\tag{7.1}
```

No lower bound on the total stress carried by `mathcal T_D` is asserted. Thus ZMA does not force a linear macroscopic subfamily by counting alone.

The exact surviving split is:

```text
macroscopic train cuts:
    asymptotically star-aligned,
    pairwise noncrossing,
    laminar ordered slabs;

remaining train crossings:
    at least one crossing train has total contact stress o(D)
    along a suitable diagonal scale.
```

---

## 8. Interaction with ZWT/ZEA

The ZWT/ZEA branch contains `Omega_eta(D)` weak-rich trains with macroscopic endpoint-anchored nonradial strips.

If a positive fraction of those trains are global outer-to-outer and macroscopic at some fixed scale `cD`, ZMA makes that subfamily pairwise noncrossing and star-aligned.

If not, then either

- many weak-rich trains end on bounded holes/exceptional faces, entering the ZPL-B boundary-charge branch; or
- many global weak-rich trains have total train stress `o(D)` at progressively smaller fixed scales.

The latter is the mechanically light train-angle branch on which an unclamped deformation theorem is now the natural target.

---

## 9. Binding regression

An oblique rhombic grid with one strongly loaded direction family and one weak transverse direction family satisfies ZMA qualitatively:

- the loaded family is parallel/noncrossing;
- every crossing uses one weak train.

Therefore ZMA does not by itself exclude the grid regression. It proves that the actual near-zero survivor is asymptotically forced **into** that regression at train scale.

The remaining source-specific ingredients are ZSP/ZHA loaded attachments, exact global diameter shears ZGS, and current-main PI/PC/HB boundary geometry.

---

## 10. Exact next target

The next high-value theorem is a **light-train shear theorem**:

> If `Omega(D)` global outer-to-outer train cuts have total train stress `o(D)` individually and each contains an `Omega(D)` weak transverse strip, then some nontrivial linear combination of their exact ZGS shears is diameter-nonincreasing to first order and strictly decreases a diameter pair or the second-order max, contradicting the lexicographic global minimum.

The multi-shear derivative matrix has interval support after ordering any noncrossing macroscopic subfamily, and satisfies `A^T beta=0`, `beta>0`. The two-edge cusp regression must remain explicit.

---

## 11. Classification

**Status:** proved report-level mechanical alignment theorem.  
**Level I:** still open.  
**External literature:** none newly imported.  
**Computation:** none.
