# Target C-II — aggregate-detour endpoint floor

**Date:** 2026-09-13
**Status:** proof-only composition; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note combines three audited-working ingredients at their stated scopes on the
Section-118 endpoint/common-cap profile:

1. the exact harmonic-cell face-incidence identity;
2. the Type-II `c_B=0` localization and the `o(D)` full-core rhombus localization;
3. the orbit-level stopped-train feasibility inequality.

The result is a new endpoint-profile lower floor for the normalized quantity
`t=(q-k)/D`. It removes the low-`t` region on that profile without assuming a
near-geodesic outer walk. It is still not a C-II closure.

The implication chain is

```text
full-core rhombus localization + exact face ledger
  -> upper bound on aggregate two-arc detour
  -> upper bound on outer detour delta for fixed t
  -> audited orbit-capacity feasibility excludes t <= 1.8585.
```

## 1. Normalized variables and dependencies

Use the canonical Type-II notation:

- `q` is the loaded force-hull vertex count;
- `k=d_H+s_Z`;
- `b` is the occurrence-counted outer contact-walk length;
- `Q` is the bounded-face degree excess;
- `f` is the bounded nonquadrilateral-face count;
- `d_r=diam(P_r)` and `d_Σ=Σ_r d_r`;
- `E_Σ=Σ_r(L_r+P_exc,r-2d_r)`; and
- `Δ_R=R_4-Σ_rR_r` is the full-core/local harmonic rhombus loss.

Pass to a convergent Type-II subsequence and write

\[
 t=\lim {q-k\over D},\qquad
 \delta=\lim {b\over D}-\pi\ge0.
\tag{AD.1}
\]

The nonnegativity of `δ` follows from `b≥per(F)` and the canonical Type-II limit
`per(F)/D→π`. The canonical outer ledger is exact:

\[
 b+Q=2(q-k).
\tag{AD.2}
\]

On the Section-118 endpoint/common-cap profile, the audited endpoint moment floor gives

\[
 \liminf {d_\Sigma\over D}\ge S_*:=2.798596312209462\ldots .
\tag{AD.3}
\]

The audited full-core localization gives `Δ_R=O(D^{2/3})=o(D)` in Type II. The
exact face-incidence identity is

\[
 E_\Sigma
 =4\Delta_R+4f+2(q-k-e_{BB}+C_{\rm att})-2d_\Sigma,
\tag{AD.4}
\]

where `C_att` is the occurrence-counted number of loaded-loaded contacts used by
the local harmonic graphs. Since `c_B=0`, every loaded-loaded contact is a force-hull
side, and the cell-disjointness argument gives `C_att≤e_BB`. Consequently

\[
 E_\Sigma\le4\Delta_R+4f+2(q-k)-2d_\Sigma.
\tag{AD.5}
\]

Every exceptional face contributes at least one degree unit, so `f≤Q`. Using (AD.2),
`b/D→π+δ`, and (AD.3), (AD.5) becomes

\[
 \limsup {E_\Sigma\over D}
 \le 10t-4\pi-4\delta-2S_*.
\tag{AD.6}
\]

Canonical Section 122 supplies the opposite inequality

\[
 \liminf {E_\Sigma\over D}
 \ge c_0,
 \qquad c_0:={\pi\over2}(2-\sqrt3).
\tag{AD.7}
\]

Therefore every endpoint/common-cap Type-II limit satisfies the new necessary detour
constraint

\[
\boxed{
 4\delta\le 10t-4\pi-2S_*-c_0.
 }
\tag{AD.8}
\]

In particular, the right side must be nonnegative. This alone gives

\[
 t\ge {4\pi+2S_*+c_0\over10}
 =1.8584456846\ldots .
\tag{AD.9}
\]

The point of (AD.8), rather than only (AD.9), is that it can be composed with the
independent orbit-capacity obstruction, which becomes stronger when `δ` is small.

## 2. Composition with the audited orbit feasibility inequality

The audited-working orbit theorem (§171) gives, for the same normalized variables,

\[
 F_t(\delta):=
 10t-5\pi-5\delta
 +\bigl(81(\pi+\delta)^2\delta\bigr)^{1/3}
 -{8\Delta_2\over {9t\over2}-2\pi-2\delta}
 \ge0,
\tag{AD.10}
\]

where `Δ_2=π/(2√3)`. Its feasibility domain also has

\[
 {9t\over2}-2\pi-2\delta
 \ge 2\sqrt{\Delta_2}+0.0004.
\tag{AD.11}
\]

The derivative in `t` is strictly positive on this domain:

\[
 \partial_tF_t(\delta)
 =10+{36\Delta_2\over({9t\over2}-2\pi-2\delta)^2}>0.
\tag{AD.12}
\]

For `δ>0`,

\[
 \partial_\delta F_t(\delta)
 =-5+{81^{1/3}\over3}(\pi+3\delta)(\pi+\delta)^{-1/3}\delta^{-2/3}
 -{16\Delta_2\over({9t\over2}-2\pi-2\delta)^2}.
\tag{AD.13}
\]

Fix `t_0=1.8585` and define

\[
 A(t):={10t-4\pi-2S_*-c_0\over4},
 \qquad A_0:=A(t_0).
\tag{AD.14}
\]

Outward-safe evaluation gives

\[
 0<A_0<0.00014,
\tag{AD.15}
\]

and, throughout `0<δ≤A_0`, (AD.11)--(AD.13) give

\[
 \partial_\delta F_{t_0}(\delta)>1160.
\tag{AD.16}
\]

The value at the upper endpoint is also outward-safe:

\[
 \boxed{F_{t_0}(A_0)<-0.13.}
\tag{AD.17}
\]

The continuous value at `δ=0` is smaller, so `F_{t_0}` is strictly increasing on
`[0,A_0]` and remains negative there.

Suppose now that an endpoint/common-cap Type-II limit had `t≤t_0`. If `A(t)<0`, (AD.8) is already
impossible. Otherwise (AD.8) gives `0≤δ≤A(t)≤A_0`. Monotonicity in `t` and `δ` then
gives

\[
 F_t(\delta)\le F_{t_0}(A_0)<0,
\]

contradicting (AD.10). Hence

\[
\boxed{
 \liminf_{D\to\infty}{q-k\over D}>1.8585.
 }
\tag{AD.18}
\]

The exact numerical intersection of the two relaxed envelopes is approximately
`1.8585605048`; only the safe threshold `1.8585` is claimed.

## 3. What this does and does not close

This is a source-level strengthening of the endpoint/common-cap Type-II ledger. It
uses the aggregate detour lower bound and the actual full-core/local rhombus incidence
rather than a new carrier decimal. It rules out all endpoint/common-cap subsequences
with normalized `q-k≤1.8585`, including those with positive outer detour.

It does not rule out the remaining region `q-k>1.8585` on that profile, any other
Type-II profile, or the Type-I macroscopic inactive-container branch. No strict
diameter-decreasing competitor, exact unit triangle, or Level-I conclusion is
produced.

**Classification:** proved candidate awaiting independent audit; proof-only and scoped
to the Section-118 endpoint/common-cap profile. Theorem state remains
`2026-09-12.audit.46`; C-II remains open.
