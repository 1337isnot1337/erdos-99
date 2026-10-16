<!-- theorem-state: {"artifact_id":"ART-99E538416F60","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — DCJC endpoint excluded by one-gap moment rigidity

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after the DCJC `0.634057...` floor  
**Run type:** equality-case closure / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC/DC  
**External web search:** not used  
**Computation:** displayed decimals only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The DCJC endpoint

\[
\lambda_{DCJC}=0.6340575990818539559\ldots
\]

is not asymptotically attainable. Hence there is an absolute, presently nonexplicit
constant `eta_DC>0` such that every sufficiently large audited post-ZF survivor obeys

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DCJC}+\eta_{DC}.
}
\tag{OG.1}
\]

The contradiction is much stronger than the earlier paired-pocket exclusion. DCJC
equality forces MA perimeter equality, hence exactly one missing projective circle
interval. Therefore only two force-hull sides have macroscopic normalized chord length;
they are antipodal and both have length

\[
cD+o(D),
\qquad c=\cos(y_D/2).
\]

All other force-hull sides have `o(D)` length. Since the total chain--chord detour is
only `uD+o(D)`, the DD cubic moment is then at most

\[
(c+u)^3+c^3
\]

after normalization, not the much larger abstract diameter-capped value used in DCJC.
This leaves far too little outer-pocket area to carry the required attachment-cell gap.

---

## 1. DCJC endpoint data

Assume for contradiction that an unbounded audited survivor sequence satisfies

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{DCJC}.
\tag{1.1}
\]

DCJC endpoint localization gives

\[
\boxed{
\frac hD\to y_D,
\qquad
\frac{Q+2s_Z}{D}\to0,
\qquad
\frac{P_F}{D}\to p_0(y_D),
}
\tag{1.2}
\]

and

\[
\boxed{
\frac{e_{BB}}D\to\lambda_{DCJC},
\qquad
\frac{s_C}{D}\to0.
}
\tag{1.3}
\]

Here

\[
p_0(y)=y+2\cos(y/2),
\qquad
u(y)=y-2\cos(y/2),
\]

and

\[
y_D=1.5852324139288403018\ldots .
\]

Put

\[
c:=\cos(y_D/2),
\qquad
u_*:=\nu(y_D)=y_D-2c.
\tag{1.4}
\]

Numerically

\[
c=0.7019844778468146049\ldots,
\qquad
\nu_*=0.1812634582352110920\ldots .
\]

ZE and (1.2) give the exact total normalized outer-pocket detour limit

\[
\boxed{
\frac{b-P_F}{D}\to
2y_D-p_0(y_D)=\nu_*.
}
\tag{1.5}
\]

---

## 2. MA equality gives exactly one projective gap

Let `K_D=D^{-1}(F-o)` and pass to a Hausdorff limit `K_infty`. FS/MA imply that
`K_infty` is centrally symmetric, lies in the radius-`1/2` disk, and is the convex
hull of a closed subset of the boundary circle.

Let its missing projective-circle intervals have lengths `alpha_i`, with total

\[
X=\sum_i\alpha_i\le M:=\pi-y_D.
\tag{2.1}
\]

The exact cyclic perimeter formula is

\[
\operatorname{per}K_\infty
=
\pi-X+2\sum_i\sin(\alpha_i/2).
\tag{2.2}
\]

For fixed total `X`, merging two positive gaps strictly decreases the sine sum, so

\[
\sum_i\sin(\alpha_i/2)\ge\sin(X/2),
\tag{2.3}
\]

with equality only when at most one gap has positive length. Also

\[
f(X):=\pi-X+2\sin(X/2)
\]

is strictly decreasing on `(0,pi)`. Thus

\[
\operatorname{per}K_\infty
\ge f(X)\ge f(M)=p_0(y_D).
\tag{2.4}
\]

DCJC has perimeter equality in (1.2), so equality holds throughout (2.4). Hence

\[
\boxed{
X=M=\pi-y_D,
\qquad
\text{there is exactly one positive projective gap.}
}
\tag{2.5}

The ordinary-circle lift consists of two antipodal missing arcs, each of angle `M`.
Their two chord sides in `K_infty` both have length

\[
\sin(M/2)=\cos(y_D/2)=c.
\tag{2.6}
\]

Every other boundary point of `K_infty` lies on one of the two retained circular arcs.

---

## 3. Only two finite force-hull sides can remain macroscopically long

For every fixed `epsilon>0`, (2.5) implies that for all sufficiently large `D`, all
but two force-hull sides have length at most `epsilon D`, while the two exceptional
sides have lengths

\[
s_1=cD+o(D),
\qquad
s_2=cD+o(D).
\tag{3.1}
\]

Proof: if a third sequence of sides had normalized length bounded below by a positive
constant, pass to its endpoint directions. FS radial localization places both endpoint
limits on the radius-`1/2` circle. Their positive chord length leaves a positive open
circle interval between them containing no force-hull extreme point, producing a third
ordinary-circle missing arc and therefore another positive projective gap, contrary to
(2.5). The same argument shows the two exceptional sides converge to the two chords in
(2.6).

Since `cD->infinity`, both exceptional sides are noncontact hull sides and determine
two distinct OP outer pockets.

---

## 4. One-gap cubic moment theorem

For each outer pocket `P`, write

\[
\ell_P=s_P+d_P,
\qquad d_P\ge0,
\]

where `s_P` is its force-hull chord and `d_P` its chain--chord detour. OD gives

\[
\sum_Pd_P=b-P_F.
\tag{4.1}
\]

Let `P_1,P_2` be the two exceptional macroscopic-chord pockets from (3.1). Put

\[
d_i/D\to\delta_i
\qquad(i=1,2)
\]

after passing further, and let

\[
\delta_0:=\nu_*-\delta_1-\delta_2\ge0
\tag{4.2}
\]

be the remaining normalized detour.

We claim

\[
\boxed{
\limsup\frac{1}{D^3}
\sum_P\ell_P^3
\le
(c+\delta_1)^3+(c+\delta_2)^3+\delta_0^3.
}
\tag{4.3}
\]

To prove it, fix `epsilon>0` and let `S_epsilon` be the other pockets, whose chords
satisfy `s_P<=epsilon D` for large `D`. Minkowski's inequality in `l^3` gives

\[
\left(\sum_{P\in S_\epsilon}\ell_P^3\right)^{1/3}
\le
\left(\sum_{P\in S_\epsilon}s_P^3\right)^{1/3}
+
\left(\sum_{P\in S_\epsilon}d_P^3\right)^{1/3}.
\tag{4.4}
\]

The total force-hull perimeter is `O(D)`, so

\[
\sum_{P\in S_\epsilon}s_P^3
\le
(\epsilon D)^2\sum_Ps_P
=O(\epsilon^2D^3).
\tag{4.5}
\]

Also convexity gives

\[
\sum_{P\in S_\epsilon}d_P^3
\le
\left(\sum_{P\in S_\epsilon}d_P\right)^3.
\tag{4.6}
\]

Divide (4.4) by `D`, let `D->infinity`, then `epsilon->0`. Equations (4.1)--(4.2)
give

\[
\limsup\frac1{D^3}
\sum_{P\in S_\epsilon}\ell_P^3
\le\delta_0^3.
\]

Together with `ell_i/D->c+delta_i`, this proves (4.3).

The right side of (4.3) is a convex function on the simplex

\[
\delta_0+\delta_1+\delta_2=\nu_*,
\qquad\delta_i\ge0.
\]

A convex function achieves its maximum on this compact simplex at a vertex. Allocating
all detour to one of the two `c`-based chains gives

\[
(c+\nu_*)^3+c^3,
\]

while allocating all detour to the zero-chord class gives

\[
2c^3+\nu_*^3.
\]

Their difference is

\[
(c+\nu_*)^3-c^3-\nu_*^3
=3c\nu_*(c+\nu_*)>0.
\]

Therefore

\[
\boxed{
\limsup\frac1{D^3}
\sum_P\ell_P^3
\le
M_{1g}:=(c+\nu_*)^3+c^3.
}
\tag{4.7}
\]

---

## 5. The one-gap moment is strictly below the DC moment

DCJC used the abstract diameter-capped moment

\[
M_D
=(1+\nu_*)^3+1+[p_0(y_D)-2]^3.
\tag{5.1}
\]

All three displayed terms are positive. Since `c<1`,

\[
(c+\nu_*)^3<(1+\nu_*)^3
\]

and

\[
c^3<1.
\]

Hence already

\[
\boxed{M_{1g}<M_D.}
\tag{5.2}
\]

Numerically,

\[
M_{1g}=1.0345708774\ldots,
\qquad
M_D=3.6162680516\ldots .
\]

The loss is macroscopic and does not depend on a delicate rounding margin.

---

## 6. Contradiction with the DCJC crossover

DD before its scalar moment relaxation gives

\[
H_{out}
\le
\frac1{\sqrt6}
\left(\sum_P\ell_P^3\right)^{1/2}
(b-P_F)^{1/2}.
\tag{6.1}
\]

Using (1.5) and (4.7),

\[
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}\sqrt{M_{1g}\nu_*}.
\tag{6.2}
\]

Since `Q/D->0`, CC gives

\[
A_{exc}=o(D^2).
\tag{6.3}
\]

On the other hand DCJC defines its crossover by

\[
\boxed{
\Phi(y_D)-\frac\pi4\lambda_{DCJC}^2
=
\frac1{\sqrt6}\sqrt{M_D\nu_*}.
}
\tag{6.4}
\]

MA/GU therefore give

\[
\liminf\frac GD^2
\ge
\frac1{\sqrt6}\sqrt{M_D\nu_*}.
\tag{6.5}
\]

But ZG/GU, (6.2), and (6.3) give

\[
\limsup\frac GD^2
\le
\frac1{\sqrt6}\sqrt{M_{1g}\nu_*}
<
\frac1{\sqrt6}\sqrt{M_D\nu_*},
\tag{6.6}
\]

contradicting (6.5). Therefore the DCJC endpoint is impossible. `square`

As before, if no positive `eta_DC` in (OG.1) existed, a diagonal sequence of survivors
with diameters tending to infinity and normalized currency tending down to
`lambda_DCJC` would contradict the endpoint exclusion. This proves OG.1. `square`

---

## 7. Regression audit

- **Regular odd shell:** has no macroscopic missing projective gap in the disk limit;
  Section 3 does not force only two macroscopic sides there.
- **Many tiny force-hull gaps:** they cannot survive DCJC perimeter equality with a
  positive total projective missing angle; gap splitting strictly raises perimeter.
- **Many tiny outer pockets along the retained arcs:** allowed. Their total chord
  perimeter may be linear in `D`, but (4.5) makes their normalized cubic chord moment
  vanish because every individual chord is `o(D)`.
- **One large zero-chord detour chain:** included through the `delta_0^3` term; convex
  optimization still favors spending detour on one of the two `c`-based chains.
- **Dense isolated fillings:** FS/MA equality is used only after the full post-ZF source
  has been selected; no arbitrary annular filling is promoted to a minimizer.
- **Response trace and matching regressions:** unused.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| MA perimeter equality gives one projective gap | proved | strict gap merging + total-angle monotonicity |
| only two macroscopic finite hull sides | proved asymptotically | any third positive chord creates another limit circle gap |
| small-side cubic chord moment vanishes | proved | max-side-squared times total perimeter |
| one-gap moment bound (4.7) | proved | Minkowski + detour simplex convexity |
| strict `M_1g<M_D` | proved | `c<1` and positive third DC term |
| DCJC endpoint exclusion | proved relative to report-level chain | gap lower exceeds cavity upper |
| uniform nonexplicit gap above `0.634057...` | proved | diagonal compactness argument |
| Level I | still open | a quantitative near-one-gap version is still needed for a stronger explicit floor or full closure |

---

## 9. Exact next obligation

The qualitative endpoint proof is now robust enough to expose the next quantitative
object. Let the normalized cyclic force hull have projective missing gaps `alpha_i`.
The exact DD cubic moment can be bounded in terms of the **cubic chord mass**

\[
\sum_i 2\sin^3(\alpha_i/2)
\]

and the total detour. The MA perimeter formula already fixes the first chord moment
`sum 2sin(alpha_i/2)` in terms of `(X,p)`.

A sharp or certified moment comparison between the first and third chord moments,
combined with the detour allocation, would replace the endpoint-only `M_1g` by a
uniform force-hull-aware DD capacity. That is the direct route to another explicit
threshold and potentially to a contradiction with the remaining post-ZF topological
budget.