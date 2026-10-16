<!-- theorem-state: {"artifact_id":"ART-09654A9C1D2F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — RCC: response defect forces component-diameter / pinned-contact currency

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact cross-route inequality  
**Target:** Target C C-II, especially the C66 near-zero response phase  
**Depends on:** C41 coordinate-energy identity, ZK component-diameter ledger, C40 attachment diameter bound  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

Let

\[
\varepsilon
:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H)\ge0
\]

be the C41 response-conductance defect. Let

\[
L:=e_{BB}+2s_C,
\qquad
k:=d_H+s_Z.
\]

ZK defines

\[
L_2:=6-3k+L
\]

and proves

\[
\sum_r\delta_r\le L_2.
\]

C40 gives every harmonic attachment set

\[
\operatorname{diam}(A_r)\le\delta_r+2.
\]

The full response is the sum of direct loaded-loaded contacts and the Kron responses of the unloaded components. Therefore every positive response conductance is supported on a loaded pair of Euclidean distance at most

\[
L_2+2.
\]

C41's exact coordinate-energy identity is

\[
\sum_{b<k}c_{bk}|b-k|^2=D^2.
\]

Hence

\[
D^2
\le
(L_2+2)^2\sum_{b<k}c_{bk}
=(L_2+2)^2(1+\varepsilon).
\]

This gives the exact finite inequality

\[
\boxed{
L_2+2
\ge
\frac{D}{\sqrt{1+\varepsilon}}.
}
\tag{RCC.1}
\]

Substituting `L_2=6-3k+e_BB+2s_C` yields:

### Theorem RCC — response/currency coupling

\[
\boxed{
e_{BB}+2s_C
\ge
\frac{D}{\sqrt{1+\varepsilon}}
-8
+3(d_H+s_Z).
}
\tag{RCC.2}
\]

In particular,

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\frac1{\sqrt{1+\varepsilon}}-rac8D.
}
\tag{RCC.3}
\]

Thus any sequence with `epsilon ->0` already satisfies

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}\ge1.
}
\tag{RCC.4}
\]

The C66 near-zero phase assumes the stronger

\[
D\varepsilon\to0,
\]

so it lies entirely in the asymptotic high pinned/contact-surplus region

\[
\boxed{
e_{BB}+2s_C\ge D-o(D).}
\tag{RCC.5}
\]

This is more than twice the currently explicit unconditional ENS floor `0.48072358047D` on that response phase.

---

## 1. Response support diameter

C41 decomposes the contact Dirichlet response as

\[
\Lambda
=L_{BB}^{dir}+\sum_r\Lambda^{(r)}.
\tag{1.1}
\]

A direct loaded-loaded contact contributes response only on its two endpoints, which are unit distance apart.

For a component contribution `Lambda^(r)`, C41 says the off-diagonal conductance support is the complete graph on its attachment set `A_r`. C40 proves

\[
\operatorname{diam}(A_r)\le\delta_r+2.
\tag{1.2}
\]

Since every `delta_r>=0`,

\[
\delta_r+2
\le
2+\sum_s\delta_s
\le
L_2+2.
\tag{1.3}
\]

Also a direct loaded-loaded contact has length `1<=L_2+2` because `L_2>=0`.

Consequently

\[
\boxed{
c_{bk}>0\Longrightarrow |b-k|\le L_2+2.}
\tag{RCC.6}
\]

This is a global response-support diameter bound extracted from the component ledger.

---

## 2. Coordinate energy gives RCC

C41 proves exactly

\[
\sum_{b<k}c_{bk}|b-k|^2=D^2.
\tag{2.1}
\]

Use RCC.6:

\[
\begin{aligned}
D^2
&=\sum_{b<k}c_{bk}|b-k|^2\\
&\le(L_2+2)^2\sum_{b<k}c_{bk}\\
&=(L_2+2)^2(1+\varepsilon).
\end{aligned}
\]

All factors are nonnegative, so

\[
L_2+2\ge D/\sqrt{1+\varepsilon},
\]

which is RCC.1.

Now

\[
L_2+2
=8-3(d_H+s_Z)+e_{BB}+2s_C.
\]

Rearrange to obtain RCC.2.

---

## 3. Phase consequences

### Small absolute response defect

If

\[
\varepsilon=o(1),
\]

then

\[
\frac1{\sqrt{1+\varepsilon}}=1-o(1),
\]

so RCC.3 gives

\[
e_{BB}+2s_C\ge D-o(D).
\]

Thus no post-ZF sequence can simultaneously have

\[
\varepsilon=o(1)
\]

and

\[
\limsup\frac{e_{BB}+2s_C}{D}<1.
\]

### C66 near-zero phase

C66's difficult branch has

\[
D\varepsilon\to0.
\]

RCC forces that branch into

\[
\liminf\frac{e_{BB}+2s_C}{D}\ge1.
\]

So all scalar/cavity configurations near the ENS threshold are automatically disjoint from the C66 near-zero-response regime. The two frontiers should no longer be attacked as though they could occur simultaneously.

### Positive topology defect

RCC.2 retains the exact positive correction

\[
3(d_H+s_Z).
\]

Any linear density of diameter-tree components or extra mixed dependencies pushes the required pinned/contact currency strictly above the response-only value.

---

## 4. Relation to HSR

HSR proves the componentwise refinement

\[
S_r
\le
\frac{L_r^2}{D^2-L_r^2}E_r,
\]

where `S_r` is component contact-stress mass and `E_r` its C41 response defect.

RCC is the global support-radius consequence obtained without tracking the stress distribution. It can also be viewed directly from the energy identity: if total response conductance is almost one, then some response pair must live at distance almost `D`; C40/ZK say producing such a pair requires total component graph-diameter currency almost `D`.

This interpretation is useful:

\[
\boxed{
\varepsilon\to0
\quad\Longrightarrow\quad
\text{some harmonic attachment geometry spans }D-o(D)
}
\]

unless direct loaded-loaded response itself is large, in which case `epsilon` cannot be small because those pairs have length one.

---

## 5. Comparison with the scalar frontier

ENS proves unconditionally

\[
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.48072358047.
\]

RCC proves the stronger conditional floor

\[
\liminf\frac{e_{BB}+2s_C}{D}
\ge1
\]

whenever `epsilon->0`.

Therefore the remaining Target C parameter space now has a clean response split:

1. `epsilon` bounded away from zero: a fixed response defect is available and C64/E43 should be exploited directly;
2. `epsilon->0`: pinned/contact currency is at least `D-o(D)` by RCC, and C66 further radializes the diameter reaction if `D epsilon->0`.

This is a qualitative improvement over treating the response and cavity branches independently.

---

## 6. Regression audit

- RCC does not assume one giant component.
- It does not use ESN or the scalar near-equality classification.
- Direct loaded-loaded contacts are included honestly: their response distance is one.
- The bound `diam(A_r)<=delta_r+2` is an upper bound on every response pair generated by component `r`; no inference from graph support cardinality is used.
- `L_2>=0` is guaranteed by ZK because it bounds the nonnegative sum `sum delta_r`.
- Large `epsilon` makes RCC weak, as expected.
- RCC is not Level I: `e_BB+2s_C` can in principle be at least `D`.

## 7. Next target

RCC moves the C66 near-zero phase into the high-surplus regime. The next useful question is whether the exact identities ZU/ZK/ZT permit

\[
e_{BB}+2s_C\ge D-o(D)
\]

together with C66's near-star diameter reaction and `D epsilon->0`.

A promising split is:

- if `e_BB` carries a fixed fraction of `D`, C41.14 makes its **stress** expensive in response defect, so those direct contacts must have vanishing aggregate stress despite linear support;
- if `s_C` carries the currency, many extra pinned self-stress dimensions coexist with an almost rank-minimal boundary response, suggesting a stress-space / mixed-rigidity incompatibility.

The bridge-hinge rank theorem in PR #126 may attack the latter if the extra pinned stress is carried on deep bridge structure.

## 8. Compact handoff

```text
RCC exact response/currency coupling.
Let epsilon=sum c_bk-1=tr(Lambda-L_H)/2 and
L_2=6-3(d_H+s_Z)+e_BB+2s_C.
ZK: sum delta_r<=L_2.
C40: diam(A_r)<=delta_r+2.
Hence every positive response pair has length <=L_2+2.
C41 coordinate energy gives
    D^2=sum c_bk |b-k|^2
       <=(L_2+2)^2(1+epsilon).
Therefore
    L_2+2 >= D/sqrt(1+epsilon),
and exactly
    e_BB+2s_C
      >= D/sqrt(1+epsilon)-8+3(d_H+s_Z).
In particular epsilon->0 forces
    (e_BB+2s_C)/D >=1-o(1).
Thus the C66 D epsilon->0 branch lies wholly above slope 1, not near the
0.48072358 ENS scalar frontier.
```