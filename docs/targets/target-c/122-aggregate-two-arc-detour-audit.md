# Target C — aggregate two-arc detour over the harmonic-cell tiling

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical from theorem-state `2026-09-12.audit.46`.

This module canonicalizes the concurrent research artifact originally numbered Section 120 as **Section 122** to avoid collision with canonical `C-ANISOTROPIC-TWO-ARC-RETURN`.

The theorem aggregates the canonical Section-116 zero-host two-arc inequality over every actual harmonic cell without selecting one carrier.

## 122.1 Local theorem

For each unloaded positive-contact component `I_r`, let

\[
P_r=\operatorname{conv}(A_r),
\qquad d_r=\operatorname{diam}(P_r),
\]

and let `H_r` be the induced positive-contact graph on `I_r\cup A_r`, including loaded-loaded contacts with both endpoints in `A_r`. Write

- `L_r` for its occurrence-counted outer-face walk length;
- `P_{{\rm exc},r}` for the total degree of its bounded nonquadrilateral faces;
- `A_{4,r}` for its total bounded strict-rhombus area.

Canonical `C-ZERO-HOST-SIGNED-RETURN` gives

\[
\boxed{
d_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge(4-2\sqrt3)A_{4,r}.
}
\tag{122.1}
\]

Put

\[
E_r:=L_r+P_{{\rm exc},r}-2d_r\ge0.
\tag{122.2}
\]

## 122.2 Injective area summation

Call a strict rhombus **unloaded-only** when all four vertices are unloaded. Every such rhombus belongs to one and only one unloaded component, because its four contact edges form a connected cycle of unloaded vertices.

Let `A_{4,r}^0` be the unloaded-only strict-rhombus area assigned to `I_r`, and let `A_4^0` be their total global area. Then

\[
0\le A_{4,r}^0\le A_{4,r},
\qquad
\boxed{\sum_rA_{4,r}^0=A_4^0.}
\tag{122.3}
\]

Apply (122.1) and discard loaded-touching rhombi:

\[
E_r
\ge(4-2\sqrt3){A_{4,r}^0\over d_r}.
\]

Therefore

\[
\boxed{
\sum_rE_r
\ge(4-2\sqrt3)
\sum_r{A_{4,r}^0\over d_r}.
}
\tag{122.4}
\]

Since every `P_r\subset F\subset\operatorname{conv}(A)` has `d_r\le D`,

\[
\boxed{
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge {4-2\sqrt3\over D}A_4^0.
}
\tag{122.5}
\]

No boundary-occurrence injectivity between different induced graphs is assumed; (122.4) is only a sum of valid scalar inequalities. Area injectivity is supplied by (122.3).

## 122.3 Type-II consequence

In the canonical full-core Type-II branch,

\[
{A_4\over D^2}\to{\pi\over4}.
\tag{122.6}
\]

Only `O(D)` strict rhombi touch loaded vertices: a loaded vertex has positive-contact degree at most three, and the loaded set has `O(D)` vertices. Unit rhombi have area at most one. Hence

\[
A_4-A_4^0=O(D),
\qquad
{A_4^0\over D^2}\to{\pi\over4}.
\tag{122.7}
\]

Divide (122.5) by `D`:

\[
\boxed{
\liminf_{D\to\infty}{1\over D}
\sum_r\bigl(L_r+P_{{\rm exc},r}-2d_r\bigr)
\ge {\pi\over4}(4-2\sqrt3)
={\pi\over2}(2-\sqrt3).
}
\tag{122.8}
\]

The right side is approximately `0.42089`.

This is an all-regime source-level detour floor. It does not by itself contradict the global incidence budgets.

## 122.4 Audit points

- **No rhombus double counting:** only unloaded-only rhombi are summed.
- **No occurrence double counting premise:** local boundary walks may reuse physical loaded edges in different induced graphs; the proof never interprets their sum as an injective global boundary set.
- **Diameter comparison:** only `d_r<=D` is used.
- **Source retention:** contact-isolated source points remain globally present.
- **No KKT coefficient floor or full-source ZR/ZF extension is used.**

**Theorem state:** canonical as `C-AGGREGATE-TWO-ARC-DETOUR` from `2026-09-12.audit.46`. C-II remains open.
