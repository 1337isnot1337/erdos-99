# Target C-II — exact route-surplus / stopped-train identity

**Date:** 2026-09-13  
**Status:** proof-only composition; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note isolates an exact finite identity linking the global route currency to the
complete stopped-train count. It uses the Type-II loaded-contact normalization
`c_B=0`, so every loaded-loaded unit contact is a loaded force-hull side.

The implication chain is

```text
Type-II hull/train ledgers
  -> route surplus + exceptional perimeter = 2T - per(F)
  -> audited train-gap and diameter-endpoint floors
  -> a large necessary global route currency.
```

This is a source-level lower bound. It supplies no upper bound on the same currency
and therefore does not close C-II.

## 1. Exact finite identity

Use the standard Type-II notation:

- `q=|B|` for loaded force-hull vertices;
- `m` for nonunit sides of the loaded force hull;
- `k=d_H+s_Z`;
- `u_B` for extra outer-walk occurrences;
- `Q` for global bounded-face degree excess;
- `f` for bounded nonquadrilateral faces;
- `b` for the occurrence-counted outer contact walk; and
- `T` for the complete stopped-train count.

The audited loaded-hull and train identities are

\[
e_{BB}=q-m=Q+2k+u_B,
\qquad
b=q+m+u_B,
\qquad
T=q+2f-k.
\tag{RT.1}
\]

The exceptional-face perimeter is

\[
P_{\rm exc}=4f+Q.
\tag{RT.2}
\]

Subtracting the first identity in (RT.1) from `q` gives `m=q-Q-2k-u_B`. Hence,
without any asymptotic estimate,

\[
\begin{aligned}
b+P_{\rm exc}
 &=q+m+u_B+Q+4f\\
 &=2q-2k+4f\\
 &=2(q+2f-k)=2T.
\end{aligned}
\tag{RT.3}
\]

Therefore

\[
\boxed{
\frac{b-\operatorname{per}(F)+P_{\rm exc}}{D}
 =2\frac{T}{D}-\frac{\operatorname{per}(F)}{D}.
}
\tag{RT.4}
\]

The left side is exactly the route-surplus currency used by the recent atomic and
two-phase reports. No occurrence is identified with another occurrence in (RT.3).

## 2. Composition with the audited train and endpoint floors

Let

\[
s_2:=\sqrt{\frac{\pi}{2\sqrt3}}.
\]

The audited all-regime atomic-gap theorem in the Section-142 scope gives an absolute
`eta_grid>0` with

\[
\liminf\frac{T-q/2}{D}\ge2s_2+\eta_{\rm grid}.
\tag{RT.5}
\]

The same audited Type-II stack gives

\[
\liminf\frac{h}{D}\ge C_{146},
\qquad
C_{146}=1.8195135379794445\ldots,
\tag{RT.6}
\]

and the diameter pseudoforest has `h<=q`. Thus

\[
\liminf\frac{T}{D}
\ge \frac12C_{146}+2s_2+\eta_{\rm grid}.
\tag{RT.7}
\]

Type-II near-disk convergence gives `per(F)/D -> pi`. Combining (RT.4) and (RT.7)
proves

\[
\boxed{
\liminf\frac{b-\operatorname{per}(F)+P_{\rm exc}}{D}
\ge C_{146}+4s_2-\pi+2\eta_{\rm grid}.
}
\tag{RT.8}
\]

Using only the conservative enclosures `C_{146}>1.8195`,
`4s_2>3.8092`, and `pi<3.1416`, the non-gap part of the right side is

\[
C_{146}+4s_2-\pi>2.4871.
\tag{RT.9}
\]

In a near-geodesic subbranch with `b-per(F)=o(D)`, (RT.8) becomes the direct
exceptional-perimeter demand

\[
\boxed{
\liminf\frac{P_{\rm exc}}{D}
\ge C_{146}+4s_2-\pi+2\eta_{\rm grid}>2.4871.
}
\tag{RT.10}
\]

The same conclusion applies in any two-phase branch whose selected outer walk has
`b<=pi D+o(D)`, because Type-II near-disk convergence also gives
`per(F)=pi D+o(D)` and the outer walk dominates the loaded-hull perimeter.

## 3. Closure boundary and limits

The identity (RT.4) does not identify the global route currency with the aggregate
cell detour in canonical Section 122. In particular, it gives no upper bound on
`T`, `P_exc`, or `b-per(F)`. The scalar region remains feasible by increasing the
exceptional-face population; (RT.10) therefore does not contradict Section 123's
payment, which is only an upper payment by `e_{BB}-k`.

This result is consequently classified as a **proved candidate awaiting promotion at
proof-only scope**, not as a C-II closure. A closing bridge still has to convert the
large route currency into a forbidden upper bound, a strict diameter descent, or an
exact unit equilateral triangle.
