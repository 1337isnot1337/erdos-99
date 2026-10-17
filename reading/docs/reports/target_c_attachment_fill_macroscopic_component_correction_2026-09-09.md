> Generated reading edition · [exact source](../../../docs/reports/target_c_attachment_fill_macroscopic_component_correction_2026-09-09.md) · source SHA-256 `36481d775ef5cf4d304a9ab4eb8aca4605887b5084c5b060e4ef71ce39d0542c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-81923D1E427B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — correction to AR: positive-density core forces a macroscopic harmonic component

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** correction / strengthening of AR  
**Target:** Target C harmonic attachment cells after ZF  
**Depends on:** AR cell lower bound, C49 disjoint attachment cells, C44/ZG diameter control; C40/HB for the near-circle numerical form  
**Computation:** only displayed decimal evaluation

## LEVEL I STATUS

`STILL OPEN`

The original AR report contains an overly weak caveat: it says the theorem does not force one unloaded component to have graph diameter `Omega(D)`. That statement is false once AR's lower cell-area bound is combined with the **unsummed** isodiametric cell upper bound.

The corrected theorem is stronger:

> whenever the positive contact core has positive quadratic density, at least one harmonic unloaded component has graph diameter linear in `D`.

In the UF near-circle phase, if

```math
\frac{v}{D^2}\to\Delta-\zeta,
\qquad
\Delta=\frac\pi{2\sqrt3},
```

then

```math
\boxed{
\liminf\frac{\delta_{\max}}D
\ge
\frac{1-\zeta/\Delta}{\pi},
}
```

where `delta_max=max_r delta_r`.

At UF's worst crossover `zeta_*=0.5572837714...`, this still forces

```math
\delta_{\max}\ge(0.1227105962...-o(1))D.
```

In the asymptotically full-core subbranch `zeta=0`,

```math
\delta_{\max}\ge(1/\pi-o(1))D.
```

This supersedes the contrary caveat in AR Sections 8--9.

---

## 1. Recall the cell lower bound

Use the AR notation. For unloaded components `I_r`, write

```math
\delta_r=\operatorname{diam}_{C[I_r]} I_r,
\qquad
S:=\sum_r\delta_r,
\qquad
\delta_{\max}:=\max_r\delta_r.
```

Let

```math
P_r=\operatorname{conv}A_r
```

be the C49 harmonic attachment cells. AR proves

```math
\boxed{
\sum_r\operatorname{area}(P_r)
\ge
a_0(v-q)
-\frac{a_0\pi}{2}S
-a_0(\pi-2)c_I,
}
\tag{MC.1}
```

where

```math
a_0=\frac{\sqrt3}{2}.
```

The terms after `a_0(v-q)` are only boundary-order because post-ZF gives

```math
q,S,c_I=O(D).
```

---

## 2. Keep the maximum component diameter instead of replacing every square by `S^2`

C44/ZG gives

```math
\operatorname{diam}(P_r)\le\delta_r+2.
```

Hence the planar isodiametric inequality gives cellwise

```math
\operatorname{area}(P_r)
\le\frac\pi4(\delta_r+2)^2.
```

Sum and use

```math
\sum_r\delta_r^2
\le
\delta_{\max}\sum_r\delta_r
=\delta_{\max}S.
```

Therefore

```math
\boxed{
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4
\left(
\delta_{\max}S+4S+4c_I
\right).
}
\tag{MC.2}
```

This is the step lost in the first AR writeup. Replacing `sum delta_r^2` by `S^2` proves a total-diameter floor but discards the concentration information needed to force a macroscopic component.

---

## 3. Finite macroscopic-component inequality

Compare MC.1 and MC.2.

### Theorem MC.1

Every finite post-ZF survivor satisfies

```math
\boxed{
 a_0(v-q)
\le
\frac\pi4\delta_{\max}S
+\pi\left(1+\frac{a_0}{2}\right)S
+\bigl[\pi+a_0(\pi-2)\bigr]c_I.
}
\tag{MC.3}
```

This is exact and contains no KKT coefficient lower bound.

---

## 4. Any positive-density core has a linear-diameter component

Take an unbounded subsequence with

```math
\frac v{D^2}\to r>0.
```

Post-ZF gives `S=O(D)`. Pass to a further subsequence on which

```math
\frac SD\to s,
\qquad
\frac{\delta_{\max}}D\to\mu
```

with finite limits after taking limsup/liminf subsequences as needed.

Divide MC.3 by `D^2`. All linear terms vanish, leaving

```math
a_0r
\le
\frac\pi4\mu s.
```

Since

```math
\frac{4a_0}{\pi}=\frac1\Delta,
\qquad
\Delta=\frac\pi{2\sqrt3},
```

we obtain

### Theorem MC.2

```math
\boxed{
\mu s\ge\frac r\Delta.
}
\tag{MC.4}
```

In particular, because `s` is finite and `r>0`,

```math
\boxed{
\delta_{\max}=\Omega(D).
}
\tag{MC.5}
```

Thus a positive-density force-visible core cannot be carried by a linear number of bounded-diameter harmonic cells. One macroscopic harmonic component is mandatory.

A safe liminf/limsup form is

```math
\boxed{
\left(\liminf\frac{\delta_{\max}}D\right)
\left(\limsup\frac SD\right)
\ge\frac r\Delta
}
\tag{MC.6}
```

along every subsequence on which `v/D^2->r` and after the usual compact subsequence extraction.

---

## 5. Stronger upper bound for `S` in the UF near-circle phase

C40 gives for every component

```math
t_r\ge\delta_r+3,
```

where `t_r` is the number of physical contact edges from `I_r` to the loaded terminal set. Therefore

```math
S+3c_I\le e_{BI}.
\tag{5.1}
```

The loaded degree-three cap gives

```math
e_{BI}+2e_{BB}\le3q.
\tag{5.2}
```

HB gives the exact outer-walk coupling

```math
e_{BB}\ge q-x_B.
\tag{5.3}
```

Hence

```math
\boxed{
S+3c_I
\le e_{BI}
\le q+2x_B.
}
\tag{5.4}
```

In particular, in the PR #119 near-circle phase

```math
x_B=o(D),
\qquad
q/D\to\pi,
```

so

```math
\boxed{
\limsup\frac SD\le\pi.
}
\tag{5.5}
```

---

## 6. UF population-dependent macroscopic component

In UF notation

```math
\frac{v}{D^2}\to r=\Delta-\zeta.
```

Combine MC.6 with (5.5):

```math
\boxed{
\liminf\frac{\delta_{\max}}D
\ge
\frac{r/\Delta}{\pi}
=
\frac{1-\zeta/\Delta}{\pi}.
}
\tag{MC.7}
```

At the UF crossover

```math
\zeta_*=0.5572837714\ldots,
```

this gives

```math
\boxed{
\liminf\frac{\delta_{\max}}D
\ge0.1227105962\ldots .
}
\tag{MC.8}
```

At the asymptotically full-core endpoint `zeta=0`,

```math
\boxed{
\liminf\frac{\delta_{\max}}D
\ge\frac1\pi
=0.3183098861\ldots .
}
\tag{MC.9}
```

These constants are conservative because (5.5) discards `3c_I` and all other post-ZF slack.

---

## 7. Why this is a meaningful route reduction

The old harmonic-component frontier had to handle two qualitatively different possibilities:

1. many graph-small attachment components collectively carrying the positive-density core;
2. at least one component whose internal graph diameter is comparable with the source diameter.

MC eliminates the first possibility whenever `v=Theta(D^2)`.

The live positive-density branch may now focus on one component `I_*` with

```math
\delta_*\ge cD
```

for an explicit `c>0` depending on the core population fraction. C40 further gives

```math
t_*\ge\delta_*+3=\Omega(D),
```

so the component also consumes a linear number of physical loaded-contact incidences.

In the near-circle phase, almost all loaded terminals already spend two contact incidences on the unit hull cycle. Therefore the macroscopic component must attach through a linear interval/family of the remaining single contact slots. This is a substantially narrower geometric object than an arbitrary cloud of harmonic cells.

---

## 8. Correction notice for AR

The following sentences in the first AR report are superseded by MC:

- “The theorem does not yet imply that one component has linear diameter; the total `S` may be distributed over many components.”
- “it does not force one component to have diameter `Omega(D)`.”
- the suggestion that a linear number of bounded-size cells remains an unconstrained escape.

The correct statement is MC.5: positive quadratic core population forces at least one linear-diameter harmonic component.

WG and TC on the same branch remain compatible with this correction; they give additional boundary-order packing and terminal-support information about the surviving macroscopic-component branch.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| finite MC.3 | proved | AR lower cell area + cellwise isodiametric upper bound + `sum delta^2<=delta_max S` |
| positive-density core -> `delta_max=Omega(D)` | proved | divide MC.3 by `D^2` and use `S=O(D)` |
| near-circle `S/D<=pi` | proved | C40 + loaded degree cap + HB + `x_B=o(D)` |
| UF bound MC.7 | proved conditional on UF | substitute `r=Delta-zeta` |
| one macroscopic physical attachment component | proved | `delta_max=Omega(D)` identifies such `I_r` |
| Level I | still open | macroscopic component itself is not yet excluded |

---

## 10. Next target

The surviving positive-density near-circle branch contains a specific macroscopic harmonic component `I_*` satisfying

```math
\delta_* = \Omega(D),
\qquad
t_*\ge\delta_*+3=\Omega(D).
```

The next theorem should exploit the simultaneous facts that

1. `I_*` is contained in the convex hull of its loaded attachment set `A_*`;
2. almost all loaded hull vertices have only one contact slot left after the direct unit hull cycle;
3. `A_*` therefore occupies a linear family of convex-boundary terminals;
4. the terminal defect support is 3-connected (TC);
5. UF already forces `Q=Omega(D)` exceptional-face defect.

A geometric restriction on a single linear-diameter harmonic cell is now enough to advance the live near-circle branch; there is no need to control an arbitrary number of tiny cells first.
