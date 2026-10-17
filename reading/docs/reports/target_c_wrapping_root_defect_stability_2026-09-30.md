> Generated reading edition · [exact source](../../../docs/reports/target_c_wrapping_root_defect_stability_2026-09-30.md) · source SHA-256 `2ce7656dd62ee019e5a1de395b17824d252fd92b1626ad54e90cee005d418ebb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-781BC1AB3F16","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- rooted-detour defect stability at the 0.989134 threshold

**Date:** 2026-09-30  
**Base main:** `43c1bd4eb6983578bdd6e7b9633df8fba8eea789`  
**Status:** proof-only current-main theorem; theorem-state authority unchanged  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Result

Work in the canonical full-core Type-II branch and suppose a positive-area
center-wrapping harmonic-cell sequence `P_w` has

$$
{d_w\over D}\to\lambda\in[\lambda_1,1),
$$

where current main defines `lambda_1` by

$$
A(\lambda_1)={\pi\over2},\qquad
A(\lambda):=\lambda+4\lambda\sqrt{1-\lambda^2},
$$

so

$$
\lambda_1=0.9891345915624005\ldots .
$$

Put

$$
\Delta(\lambda):={\pi\over2}-A(\lambda)\ge0.
$$

For the harmonic attachment cells write

$$
S_D:=\sum_r d_r,\qquad
X_D:=q-k-S_D,
$$

$$
p_r:=\operatorname{per}(P_r),\qquad
Z_D:=\sum_r(L_r-p_r)\ge0,
$$

and let

$$
Q_D:=\sum_rQ_r.
$$

Use the current-main completion notation `d_tile`, `e_BB`, and
`C_A=sum_r c_r`, and define the completion slack

$$
Y_D:=2d_{\rm tile}-(e_{BB}-C_A)\ge0.
$$

Finally set

$$
M_D:=S_D-[\lambda+A(\lambda)]D.
$$

The current complement-gap diameter moment gives

$$
M_D\ge-o(D).
$$

Then the rooted detour theorem and the exact global outer-walk identity imply

$$
\boxed{
(\pi D-P_F)+(P_F-q)+k
+{Z_D\over2}+{Q_D\over2}+Y_D+M_D
\le \Delta(\lambda)D+o(D).
}
\tag{1.1}
$$

Here `P_F=per(F)` is the loaded force-hull perimeter. All terms except `M_D`
are nonnegative exactly, and the negative part of `M_D` is `o(D)`. Therefore

$$
\boxed{
\begin{aligned}
\pi D-P_F&\le\Delta D+o(D),\\
P_F-q&\le\Delta D+o(D),\\
k&\le\Delta D+o(D),\\
Z_D&\le2\Delta D+o(D),\\
Q_D&\le2\Delta D+o(D),\\
Y_D&\le\Delta D+o(D),\\
M_D&\le\Delta D+o(D).
\end{aligned}
}
\tag{1.2}
$$

At the exact current threshold `lambda=lambda_1`, `Delta=0`, so every one of
these defect currencies is sublinear. In particular,

$$
\boxed{
Z_D=o(D),\qquad Q_D=o(D),\qquad k=o(D),\qquad Y_D=o(D).
}
\tag{1.3}
$$

Moreover

$$
\boxed{
S_D=(\lambda_1+\pi/2)D+o(D),
\qquad
q-k=\pi D+o(D),
}
\tag{1.4}
$$

and hence

$$
\boxed{
X_D=(\pi/2-\lambda_1)D+o(D).
}
\tag{1.5}
$$

The same equality chain fixes the aggregate harmonic outer detour:

$$
\boxed{
\sum_r(L_r-2d_r)=(\pi-2\lambda_1)D+o(D),
}
\tag{1.6}
$$

while `Z_D=o(D)` gives the identical first-order value for the pure cell-shape
detour

$$
\boxed{
\sum_r(p_r-2d_r)=(\pi-2\lambda_1)D+o(D).
}
\tag{1.7}
$$

Thus equality in the new rooted carrier bound is not merely a scalar endpoint.
It forces simultaneous first-order saturation of the loaded hull, the harmonic
route geometry, the local nonquadrilateral defect, and the completion-triangle
payment.

No numerical computation is load-bearing. The decimal value of `lambda_1` is
copied from the current-main rooted-detour report; the proof uses the exact root
equation.

## 2. Retain route excess and completion slack in the exact upper ledger

Current main proves the exact finite identity

$$
S_{\rm out}
:=\sum_r(L_r-2d_r)
=
2X_D+4c_I-4-Q_D
+2(e_{BB}-C_A-2d_{\rm tile}).
\tag{2.1}
$$

The completion-triangle lemma gives

$$
e_{BB}-C_A\le2d_{\rm tile},
$$

so with `Y_D` as above,

$$
\boxed{
S_{\rm out}=2X_D+4c_I-4-Q_D-2Y_D.
}
\tag{2.2}
$$

Canonical component deatomization gives `c_I=o(D)`.

The current rooted chord-dissection theorem gives, for the same wrapping carrier,

$$
\sum_r(p_r-2d_r)
\ge(\pi-2\lambda-o(1))D.
\tag{2.3}
$$

Since

$$
S_{\rm out}
=Z_D+\sum_r(p_r-2d_r),
$$

we retain the nonnegative route excess instead of discarding it:

$$
\boxed{
S_{\rm out}
\ge Z_D+(\pi-2\lambda-o(1))D.
}
\tag{2.4}
$$

Combine (2.2) and (2.4). Because `c_I=o(D)`, this yields

$$
\boxed{
X_D
\ge
(\pi/2-\lambda)D
+{Z_D\over2}+{Q_D\over2}+Y_D-o(D).
}
\tag{2.5}
$$

Equation (2.5) is the first new inequality. The previous rooted-detour report
used only the first term on its right-hand side.

## 3. Add the complement-gap diameter moment

Current main also proves for a wrapping carrier of normalized diameter `lambda`
that

$$
S_D
\ge
[2\lambda+4\lambda\sqrt{1-\lambda^2}-o(1)]D.
\tag{3.1}
$$

With `A(lambda)` as in Section 1, the bracket is `lambda+A(lambda)`, so by
construction

$$
S_D=[\lambda+A(\lambda)]D+M_D,
\qquad M_D\ge-o(D).
\tag{3.2}
$$

Since `q-k=S_D+X_D`, equations (2.5) and (3.2) give

$$
\boxed{
q-k
\ge
[\pi/2+A(\lambda)]D
+M_D+{Z_D\over2}+{Q_D\over2}+Y_D-o(D).
}
\tag{3.3}
$$

This is stronger than the scalar inequality used to define `lambda_1`: it keeps
all first-order defect currencies instead of dropping them.

## 4. Compare with the force-hull perimeter ceiling

Every loaded force-hull side has length at least one, hence

$$
q\le P_F.
\tag{4.1}
$$

Every planar convex body of diameter `D` has perimeter at most `pi D`, hence

$$
P_F\le\pi D.
\tag{4.2}
$$

The identity

$$
\pi D-(q-k)
=(\pi D-P_F)+(P_F-q)+k
\tag{4.3}
$$

is exact. Subtract (3.3) from `pi D` and use (4.3):

$$
(\pi D-P_F)+(P_F-q)+k
+M_D+{Z_D\over2}+{Q_D\over2}+Y_D
\le
[\pi/2-A(\lambda)]D+o(D).
$$

This is (1.1).

Current main already proves that `A(lambda)` is strictly decreasing on the live
interval and that `A(lambda_1)=pi/2`. Hence `Delta(lambda)>=0` for
`lambda>=lambda_1`.

Because every displayed currency except `M_D` is nonnegative and
`M_D^-:=max(-M_D,0)=o(D)`, each individual estimate in (1.2) follows.

## 5. Endpoint rigidity

Set `lambda=lambda_1`. Then `Delta=0`. Equation (1.1) and
`M_D^- = o(D)` imply

$$
\pi D-P_F=o(D),\quad P_F-q=o(D),\quad k=o(D),
$$

$$
Z_D=o(D),\quad Q_D=o(D),\quad Y_D=o(D),\quad M_D=o(D).
\tag{5.1}
$$

Equation (3.2) now gives

$$
S_D=(\lambda_1+\pi/2)D+o(D),
$$

while (4.3) gives

$$
q-k=\pi D+o(D).
$$

Subtracting yields (1.5).

Finally (2.2), together with `c_I=o(D)`, `Q_D=o(D)`, `Y_D=o(D)`, and (1.5),
gives

$$
S_{\rm out}
=2X_D+o(D)
=(\pi-2\lambda_1)D+o(D),
$$

which is (1.6). Since `Z_D=o(D)`, equation

$$
S_{\rm out}=Z_D+\sum_r(p_r-2d_r)
$$

gives (1.7).

## 6. What this narrows

A hypothetical wrapping survivor at the exact `0.989134...` endpoint must now
satisfy all of the following simultaneously:

1. the loaded hull has asymptotically maximal perimeter and asymptotically unit
   average side length;
2. the loaded/topological deficit `k` is sublinear;
3. the total bounded nonquadrilateral face defect is sublinear;
4. the completion-triangle inequality is saturated to first order;
5. the total occurrence-counted harmonic route excess above the convex cell
   perimeters is sublinear;
6. the complement-gap diameter-moment lower bound is saturated to first order.

The fifth item is the useful new bridge toward the existing inverse-phase train
geometry: any closing continuation may work with `Z_D=o(D)` rather than only the
coarser scalar endpoint equation.

This report does not prove that the endpoint is impossible. It also does not
address the two-half-disk alternative or the macroscopic inactive-container
branch.

## 7. Scope audit

- The proof uses only current-main results: the rooted chord-dissection lower
  bound, the exact global outer-detour identity, the completion-triangle lemma,
  the uncapped complement-gap diameter moment, component deatomization, and the
  convex perimeter ceiling.
- The wrapping cell is assumed to have positive limiting area and normalized
  diameter `lambda`; no rate of convergence is assumed.
- Repeated outer-walk occurrences are retained in `L_r` and therefore in
  `Z_D`.
- Contact-isolated source points are untouched.
- No rejected Euler-path, Reuleaux-cap, FB4, full-source ZR/ZF, or withdrawn
  Section-121 scaling inference is used.
- No numerical verifier or unexecuted code is part of the proof.
- The theorem-state manifest is unchanged.

**Disposition:** proof-only current-main stability theorem. C-II and Level I remain open.
