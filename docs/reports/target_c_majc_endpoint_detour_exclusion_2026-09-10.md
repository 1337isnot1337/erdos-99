<!-- migration-source: path=docs/reports/target_c_majc_endpoint_detour_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=f32254176f3bf2237ec52a353cd8d69d4a6632fb; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — MAJC endpoint excluded by detour/face collapse

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after MAJC  
**Run type:** equality-case closure / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/MAJC/OD  
**External web search:** not used  
**Computation:** displayed decimals only; proof is exact

## LEVEL I STATUS

`STILL OPEN`

The explicit MAJC lower endpoint

\[
\lambda_{MAJC}=0.5937285472681860970\ldots
\]

cannot be approached by an audited post-ZF survivor sequence.

More precisely, there is an absolute nonexplicit constant `eta_MA>0` such that every
sufficiently large audited survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{MAJC}+\eta_{MA}.
}
\tag{ME.1}
\]

The endpoint localization from MAJC forces simultaneous equality in DB:

\[
\frac hD\to2\rho,
\qquad
\frac{\operatorname{per}F}{D}\to4\rho,
\qquad
\frac{e_{BB}}D\to\lambda_{MAJC},
\qquad
\frac{s_C}{D}\to0.
\]

DB then makes the face/mixed defect `Q+2s_Z` sublinear and the outer contact-walk
length asymptotic to the true force-hull perimeter. OD therefore collapses all outer
pocket area to `o(D^2)`, while `Q=o(D)` collapses all bounded exceptional-face area to
`o(D^2)`. This contradicts the positive quadratic attachment-cell gap required by
MA/GU.

---

## 1. Endpoint assumptions

Assume for contradiction that an unbounded audited survivor sequence satisfies

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{MAJC}.
\tag{1.1}
\]

MAJC endpoint localization gives

\[
\boxed{
\frac hD\to y_0:=2\rho,
\qquad
\frac{P_F}{D}\to p_0:=4\rho,
}
\tag{1.2}
\]

where `P_F=per(F)`, and

\[
\boxed{
\frac{e_{BB}}D\to\lambda_{MAJC},
\qquad
\frac{s_C}{D}\to0.
}
\tag{1.3}
\]

The Dottie identity `rho=cos rho` gives

\[
p_0=2y_0.
\tag{1.4}
\]

---

## 2. DB forces the topology defect to vanish linearly

Put

\[
z:=Q+2s_Z\ge0.
\tag{2.1}
\]

DB's exact finite defect inequality is

\[
z
\le
h+1-2D\cos\left((h-1)\arcsin\frac1{2D}\right).
\tag{2.2}
\]

Divide by `D` and use (1.2). Since

\[
(h-1)\arcsin\frac1{2D}\to\rho
\]

and `rho=cos rho`,

\[
0\le\limsup\frac zD
\le
2\rho-2\cos\rho
=0.
\]

Hence

\[
\boxed{
Q=o(D),
\qquad
s_Z=o(D).
}
\tag{2.3}
\]

ZE gives

\[
b=2h-Q-2s_Z=2h-z.
\tag{2.4}
\]

Therefore (1.2)--(2.3) imply

\[
\boxed{
\frac{b-P_F}{D}\to0.
}
\tag{2.5}
\]

---

## 3. Outer-pocket area collapses

OD proves the exact finite estimate

\[
H_{out}
\le
\frac{\pi}{4\sqrt2}
(x_B+a)^{3/2}\sqrt{b-P_F}.
\tag{3.1}
\]

Here `x_B+a=O(D)` for every post-ZF survivor. Indeed OD gives

\[
x_B+a
=2h-Q-2s_Z-e_{BB}+c_B
\le2h=O(D),
\tag{3.2}
\]

using `c_B<=e_BB` and nonnegativity. Combining (2.5), (3.1), and (3.2),

\[
\boxed{H_{out}=o(D^2).}
\tag{3.3}
\]

This is exactly OD's near-perimeter stability regime.

---

## 4. Exceptional-face area also collapses

Let the bounded nonquadrilateral contact faces have degrees `k_1,...,k_f>=5`.
Recall

\[
Q=\sum_{j=1}^f(k_j-4)=f+g_F.
\tag{4.1}
\]

Thus `f<=Q` and their total unit-edge perimeter is

\[
L_{exc}:=\sum_jk_j
=4f+Q
\le5Q.
\tag{4.2}
\]

By the planar isoperimetric inequality applied face by face,

\[
A_{exc}
:=\sum_j\operatorname{area}(F_j)
\le
\frac1{4\pi}\sum_jk_j^2
\le
\frac{L_{exc}^2}{4\pi}
\le
\frac{25Q^2}{4\pi}.
\tag{4.3}
\]

Using (2.3),

\[
\boxed{A_{exc}=o(D^2).}
\tag{4.4}
\]

No bound on the number of isolated source points is used.

---

## 5. The required gap remains quadratically positive

Let

\[
G
=
\operatorname{area}F-
\sum_r\operatorname{area}(P_r)
\tag{5.1}
\]

be the attachment-cell gap.

At the endpoint, MA gives the force-hull area floor

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(2\rho)
=
\frac{2\rho+\sin2\rho}{4}.
\tag{5.2}
\]

GU and (1.1) give

\[
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le
\frac\pi4\lambda_{MAJC}^2.
\tag{5.3}
\]

Hence

\[
\liminf\frac GD^2
\ge
\Phi(2\rho)-\frac\pi4\lambda_{MAJC}^2.
\tag{5.4}
\]

The defining equation for `lambda_MAJC`,

\[
(\pi^2+1)\lambda^2
+4\rho\lambda+4\rho^2
-\pi(2\rho+\sin2\rho)=0,
\]

is equivalent to

\[
\boxed{
\Phi(2\rho)-\frac\pi4\lambda_{MAJC}^2
=
\frac{(\lambda_{MAJC}+2\rho)^2}{4\pi}>0.
}
\tag{5.5}
\]

Numerically the positive coefficient is

\[
0.3416073603065\ldots .
\]

Thus

\[
\boxed{G=\Omega(D^2).}
\tag{5.6}
\]

---

## 6. Contradiction

The JC/PC cavity decomposition gives

\[
G\le H_{out}+A_{exc}+O(D).
\tag{6.1}
\]

Equations (3.3) and (4.4) make the right side `o(D^2)`, contradicting (5.6).
Therefore no endpoint sequence (1.1) exists. `square`

If no positive `eta_MA` in (ME.1) existed, choose for each integer `m` a survivor with
`D>=m` and

\[
\frac{e_{BB}+2s_C}{D}
<\lambda_{MAJC}+\frac1m.
\]

MAJC's universal liminf bound would force the selected sequence to converge to
`lambda_MAJC`, contradicting the endpoint exclusion. This proves ME.1. `square`

---

## 7. Additional endpoint currencies

Although the endpoint is impossible, its forced algebra is useful for quantitative
stability.

From (2.3), DB/NB place essentially all diameter branching into outer-walk excess:

\[
2h-q=x_B+o(D).
\tag{7.1}
\]

At `h/D->2rho`, NB's defect-dependent bound gives

\[
\liminf\frac{x_B}{D}\ge\rho.
\tag{7.2}
\]

PC/ZK are sharper for the unloaded-core side. Their exact component ledger gives

\[
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C.
\tag{7.3}
\]

Thus at the endpoint

\[
3\frac{d_H}{D}
\le\lambda_{MAJC}+o(1),
\tag{7.4}
\]

and ZU gives

\[
\frac{c_I}{D}
=
2\rho+2\frac{d_H}{D}-\lambda_{MAJC}+o(1).
\tag{7.5}
\]

In particular

\[
\liminf\frac{c_I}{D}
\ge2\rho-\lambda_{MAJC}
=0.8844417191621\ldots .
\tag{7.6}
\]

Since every nonsingleton unloaded component has graph diameter at least one, (7.3)
and (7.5) imply that the number `N_1` of singleton unloaded components satisfies

\[
\liminf\frac{N_1}{D}
\ge
2\rho-2\lambda_{MAJC}
=0.2907131718939\ldots .
\tag{7.7}
\]

Because `s_C=o(D)`, all but `o(D)` of these singletons have contact degree exactly
three. Thus the impossible endpoint also carries a linear family of exact harmonic
tripods. This is not needed for the detour contradiction.

---

## 8. Regression audit

- **Regular odd shell:** has `h/D->pi`, so DB defect does not collapse and it lies far
  from the MAJC endpoint.
- **Dense isolated fillings:** FS/MA may still apply geometrically, but they do not
  satisfy the globally sourced post-ZF/DB/PC chain as a certified minimizer.
- **One giant exceptional face:** cannot survive endpoint DB equality; its boundary
  degree would make `Q=Theta(D)`, contradicting `Q=o(D)`.
- **Many thin outer pockets:** allowed, but their total area is `o(D^2)` once total
  chain--chord detour is `o(D)`.
- **Response trace and matching regressions:** unused.

The decisive global-source information is the FS/MA force-hull geometry combined with
DB's exact source topology and the PC/OD cavity decomposition.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| MAJC endpoint localization | proved in preceding report | strict optimization |
| `Q+2s_Z=o(D)` | proved | equality in exact DB defect bound at `y=2rho` |
| `b-P_F=o(D)` | proved | ZE plus endpoint `P_F/D=4rho` |
| `H_out=o(D^2)` | proved | OD detour theorem |
| `A_exc=o(D^2)` | proved | total exceptional perimeter `<=5Q=o(D)` |
| positive quadratic gap | proved | MA/GU plus exact MAJC root equation |
| endpoint exclusion / nonexplicit strict gap | proved relative to report-level chain | contradiction with JC cavity decomposition |
| Level I | still open | larger pinned/contact currency remains feasible |

---

## 10. Promotion recommendation and next run

**Hold as report pending joint dependency promotion.** ME is proof-complete relative to
DB/FS/MA/GU/PC/OD/JC.

The next useful step is quantitative, not another equality-only restatement. Keep

\[
z=\frac{Q+2s_Z}{D},
\qquad
u=\frac{b-P_F}{D}
=2y-z-p
\]

inside the cavity estimate. OD gives outer-pocket area proportional to `sqrt(nu)`, and
exceptional faces contribute at most `25z^2/(4pi)`. Combining those two explicit terms
with MA/GU should yield a stronger **numerical feasible-region floor** above
`lambda_MAJC`, rather than only the nonexplicit `eta_MA`.
