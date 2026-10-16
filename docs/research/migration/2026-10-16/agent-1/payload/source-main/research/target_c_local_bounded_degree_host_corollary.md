# Target C — low-density detour branch forces bounded-degree local defect hosts

**Date:** 2026-09-12  
**Status:** proof-only corollary of `target_c_local_area_slack_detour_face_dichotomy.md`; C-II remains open.

Retain the repaired Section-118 frontier/common-cap notation

\[
t_D={q-k\over D},
\qquad
\kappa_D={k\over D},
\]

and the constant

\[
A_{DF}=12.19736577709914\ldots .
\]

The parent theorem proves

\[
{F_{loc}\over D}
\ge
\left[{A_{DF}-6t_D-2\kappa_D\over4}-o(1)\right]_+,
\tag{BD.1}
\]

where `F_loc` counts distinct actual bounded nonquadrilateral faces arising inside harmonic cells.

For an integer `K>=5`, let `F_{loc,<=K}` count those local faces of degree at most `K`.

## Theorem

Every survivor in the stated profile satisfies

\[
\boxed{
{F_{loc,\le K}\over D}
\ge
\left[
{A_{DF}-6t_D-2\kappa_D\over4}
-{t_D-\kappa_D\over K-3}
-o(1)
\right]_+.
}
\tag{BD.2}
\]

### Proof

Let `Q` be the full bounded-face degree excess. The loaded-hull ledger is

\[
q-x_B=Q+2k,
\qquad x_B\ge0.
\]

Therefore

\[
\boxed{{Q\over D}\le t_D-\kappa_D.}
\tag{BD.3}
\]

Every local exceptional face of degree greater than `K` contributes at least

\[
(K+1)-4=K-3
\]

to the same global `Q`. Local bounded-face fidelity is injective across harmonic cells, so no face is charged twice. Hence

\[
F_{loc,>K}
\le {Q\over K-3}.
\tag{BD.4}
\]

Subtract (BD.4) from (BD.1) and use (BD.3). This proves (BD.2). `square`

## Explicit degree-22 branch

For `K=22`,

\[
\boxed{
{F_{loc,\le22}\over D}
\ge
\left[
{A_{DF}\over4}
-\left({3\over2}+{1\over19}\right)t_D
-\left({1\over2}-{1\over19}\right)\kappa_D
-o(1)
\right]_+.
}
\tag{BD.5}
\]

Thus the concrete subbranch

\[
t_D\le1.90+o(1),
\qquad
\kappa_D\le0.05+o(1)
\]

forces

\[
\boxed{
F_{loc,\le22}
\ge(0.0769730\ldots-o(1))D.
}
\tag{BD.6}
\]

This is much stronger, on that low-density subbranch, than the universal §143 bounded-degree face floor because the faces are additionally localized inside the harmonic-cell decomposition.

## Frontier effect

A giant exceptional face cannot by itself absorb the detour obligation in the low-density profile. Either the loaded/topology density rises, or linearly many actual harmonic-cell defect hosts have uniformly bounded degree. The next unresolved step is to combine this bounded-degree *local* host population with §151 face-closure rank and the ordered macroscopic train grid.

No source point is removed; contact isolates remain outside the core rigidity matrix. The theorem is profile-specific and does not close Type II or the inactive-container branch.
