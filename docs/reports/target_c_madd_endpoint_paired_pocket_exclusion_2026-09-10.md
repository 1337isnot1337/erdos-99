<!-- theorem-state: {"artifact_id":"ART-FD19EF43CE1C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_madd_endpoint_paired_pocket_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6ad172faef837097f34afc137332d543867bdf17; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — MADD endpoint excluded by paired macroscopic outer pockets

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after the MADD `0.599785...` floor  
**Run type:** equality-case closure / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC  
**External web search:** not used  
**Computation:** displayed decimals only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The MADD endpoint

\[
\lambda_{MADD}=0.5997852332423223371\ldots
\]

is not asymptotically attainable. Therefore there is an absolute, presently
nonexplicit constant `eta_pair>0` such that every sufficiently large audited post-ZF
survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{MADD}+\eta_{pair}.
}
\tag{PP.1}
\]

The new mechanism is geometric. Equality in MA's perimeter lower bound forces the
normalized force hull to have exactly one missing projective circle interval. Its lift
to the ordinary circle consists of two antipodal missing arcs, so the force hull has
two macroscopic straight sides. Each is a noncontact hull side and therefore belongs
to a distinct OP outer pocket. Hence the DD chain-length cubic moment cannot
concentrate in a single pocket. This gives a fixed strict loss in the only cavity term
capable of carrying the MADD attachment-cell gap.

---

## 1. MADD equality data

Assume for contradiction that an unbounded audited survivor sequence satisfies

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{MADD}.
\tag{1.1}
\]

The MADD strict minimization gives

\[
\boxed{
\frac hD\to y_*,
\qquad
\frac{Q+2s_Z}{D}\to0,
\qquad
\frac{P_F}{D}\to p_0(y_*),
}
\tag{1.2}
\]

where

\[
p_0(y)=y+2\cos(y/2),
\qquad
u(y):=2y-p_0(y)=y-2\cos(y/2),
\tag{1.3}
\]

and

\[
y_*=1.4937010344306311087\ldots .
\]

Also

\[
\frac{e_{BB}}D\to\lambda_{MADD},
\qquad
\frac{s_C}{D}\to0.
\tag{1.4}
\]

Put

\[
M:=\pi-y_*\in(0,\pi),
\qquad
c:=\sin(M/2)=\cos(y_*/2)>0.
\tag{1.5}
\]

Numerically `c=0.7338320459683585...`, but only positivity is needed.

---

## 2. Equality in the MA perimeter bound gives one projective gap

Let `K_infty` be a normalized Hausdorff limit of the force hull about the FS
circumcenter. FS/MA make `K_infty` a centrally symmetric convex hull of a closed subset
of the radius-`1/2` circle.

Let the complementary open intervals on the projective circle have lengths

\[
\alpha_1,\alpha_2,\ldots,
\qquad
X:=\sum_i\alpha_i\le M.
\tag{2.1}
\]

MA gives the exact perimeter formula

\[
\operatorname{per}K_\infty
=
\pi-X+2\sum_i\sin(\alpha_i/2).
\tag{2.2}
\]

For positive `a,b` with `a+b<pi`,

\[
\sin(a/2)+\sin(b/2)-\sin((a+b)/2)>0.
\tag{2.3}
\]

Therefore repeated merging of positive gaps strictly decreases the sine sum. Hence

\[
\sum_i\sin(\alpha_i/2)
\ge\sin(X/2),
\tag{2.4}
\]

with equality only when at most one projective gap has positive length.

Define

\[
f(X)=\pi-X+2\sin(X/2).
\]

For `X>0`,

\[
f'(X)=-1+\cos(X/2)<0.
\tag{2.5}
\]

Since `X<=M`, (2.2)--(2.5) give

\[
\operatorname{per}K_\infty
\ge f(X)\ge f(M)=p_0(y_*).
\tag{2.6}
\]

But (1.2) says the perimeter is exactly `p_0(y_*)`. Thus both inequalities in
(2.6) are equalities. Consequently

\[
\boxed{
X=M,
\qquad
\text{there is exactly one projective missing interval of length }M.
}
\tag{2.7}

Its ordinary-circle lift consists of two antipodal missing arcs, each of angular length
`M`. The boundary of `K_infty` therefore contains two antipodal straight chord sides,
each of length

\[
\boxed{c=\sin(M/2)=\cos(y_*/2).}
\tag{2.8}
\]

---

## 3. The two limit chords produce two macroscopic OP pockets

Every force-hull vertex of the normalized finite configurations lies `o(1)` from the
radius-`1/2` circle by FS.1/FS.4. In the interior of either missing limit arc, the
corresponding limit chord lies a fixed positive radial distance inside that circle.
Therefore finite force-hull vertices cannot persist in the interior of either limit
chord.

More explicitly, fix a small angular neighborhood of the two endpoints of one missing
arc. For sufficiently large `D`, every force-hull vertex whose direction meets that
support sector lies in one of those two endpoint neighborhoods; otherwise a subsequence
would converge to a radius-`1/2` circle point in the missing arc. Cyclic adjacency of
the polygon then supplies a force-hull side joining the two endpoint clusters. Its
normalized length tends to the chord length `c`.

Doing this for the antipodal missing arc gives two distinct force-hull sides
`s_1,s_2` with

\[
\boxed{
\frac{s_1}{D}\to c,
\qquad
\frac{s_2}{D}\to c.
}
\tag{3.1}
\]

Since `cD->infinity`, neither side is a unit contact for large `D`. OP therefore assigns
each side to a distinct outer pocket. Let the old-contact chain lengths of those two
pockets be `ell_1,ell_2`. The triangle inequality gives

\[
\boxed{
\frac{\ell_1}{D}\ge c-o(1),
\qquad
\frac{\ell_2}{D}\ge c-o(1).
}
\tag{3.2}
\]

This is the extra information absent from the scalar DD bound.

---

## 4. Paired-pocket cubic-moment loss

Let all outer-pocket chain lengths be

\[
\ell_1,\ell_2,\ell_3,\ldots
\]

and put

\[
L:=\sum_j\ell_j.
\]

MADD has

\[
\frac{Q+2s_Z}{D}\to0.
\]

The PC/DD chain identity used in MADD therefore gives

\[
\boxed{
\limsup\frac LD\le2y_*.
}
\tag{4.1}
\]

For nonnegative numbers with total at most `L`, two specified entries at least `cD-o(D)`,
and `L/D<=2y_*+o(1)`, convexity of `x^3` gives

\[
\boxed{
\limsup\frac{\sum_j\ell_j^3}{D^3}
\le
(2y_*-c)^3+c^3.
}
\tag{4.2}
\]

Indeed, after fixing one required entry at its minimum `c`, transferring every
remaining amount into a single other entry can only increase the sum of cubes. The
maximal limiting vector is therefore `(2y_*-c,c,0,...)` up to permutation.

The inequality is strictly stronger than the scalar DD relaxation because

\[
(2y_*)^3-igl[(2y_*-c)^3+c^3\bigr]
=6y_*c(2y_*-c)>0.
\tag{4.3}
\]

---

## 5. Refined DD capacity at the endpoint

DD's pocketwise estimate is

\[
\operatorname{area}(P_j)
\le
\frac1{\sqrt6}\ell_j^{3/2}\sqrt{u_j},
\qquad
u_j:=\ell_j-s_j\ge0.
\tag{5.1}
\]

Cauchy--Schwarz gives the pre-relaxation global form

\[
H_{out}
\le
\frac1{\sqrt6}
\left(\sum_j\ell_j^3\right)^{1/2}
\left(\sum_j\nu_j\right)^{1/2}.
\tag{5.2}
\]

OD gives

\[
\sum_j\nu_j=b-P_F.
\]

From ZE and (1.2),

\[
\frac{b-P_F}{D}
\to
2y_*-p_0(y_*)
=\nu_*:=\nu(y_*)>0.
\tag{5.3}
\]

Combining (4.2), (5.2), and (5.3),

\[
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
H_{pair}:=
\frac1{\sqrt6}
\sqrt{(2y_*-c)^3+c^3}
\sqrt{\nu_*}.
}
\tag{5.4}
\]

By (4.3),

\[
\boxed{
H_{pair}
<
\frac1{\sqrt6}(2y_*)^{3/2}\sqrt{\nu_*}
=:H_{scalar}.
}
\tag{5.5}
\]

The right side is exactly the scalar DD capacity used to define the MADD crossover.

Also `Q=o(D)` at the endpoint, so CC gives

\[
\boxed{A_{exc}=o(D^2).}
\tag{5.6}
\]

---

## 6. Contradiction with the MADD crossover

MADD defines `lambda_MADD` by simultaneous equality of the MA/JC threshold and the
scalar DD threshold. Therefore

\[
\boxed{
\Phi(y_*)-rac\pi4\lambda_{MADD}^2
=H_{scalar}.
}
\tag{6.1}
\]

GU gives the left side as a lower bound for `G/D^2`. Thus

\[
\liminf\frac G{D^2}
\ge H_{scalar}.
\tag{6.2}
\]

On the other hand ZG/GU gives

\[
G\le H_{out}+A_{exc}+O(D).
\]

Using (5.4) and (5.6),

\[
\limsup\frac G{D^2}
\le H_{pair}
<H_{scalar},
\tag{6.3}
\]

contradicting (6.2). Hence no MADD endpoint sequence exists. `square`

For scale only,

\[
H_{scalar}=0.3401417038662788\ldots,
\]

while

\[
H_{pair}=0.2266716299622857\ldots .
\]

The normalized cavity loss is about `0.11347`, so the contradiction is not a fragile
decimal effect.

As in the earlier endpoint exclusions, failure of a uniform positive gap in (PP.1)
would produce a diagonal sequence converging to `lambda_MADD`, contradicting the theorem.
This proves (PP.1). `square`

---

## 7. Regression audit

- **Regular odd shell:** its force hull tends to the full disk, so there is no
  macroscopic missing projective interval and PP's paired-side hypothesis is not
  triggered.
- **Dense isolated fillings:** may reproduce disk-like FS geometry but are not globally
  certified post-ZF sources; PP uses MA/MADD endpoint localization from the full source.
- **One giant outer pocket:** this is precisely the configuration DD allowed to maximize
  its cubic moment. PP proves MADD equality forces a second macroscopic pocket, so the
  one-pocket concentration is unavailable.
- **Many tiny outer pockets:** they can only decrease the cubic moment once the two
  mandatory macroscopic chains are retained.
- **Giant exceptional face:** excluded at the endpoint by `Q=o(D)`.
- **Response trace and matching regressions:** unused.

The decisive use of global source information is FS/MA's common cyclic force-hull limit
combined with the post-ZF diameter-direction measure and OP's actual outer-pocket
interpretation of missing force-hull sides.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| MA perimeter equality implies one projective gap | proved | strict gap-merging and strict monotonicity in total missing angle |
| one projective gap gives two macroscopic finite hull sides | proved asymptotically | FS radial vertex localization + polygon cyclic adjacency |
| each side gives a distinct macroscopic OP chain | proved | side length `Theta(D)` is not a unit contact; OP one-pocket-per-missing-side |
| paired cubic-moment bound (4.2) | proved | convex concentration with two positive lower bounds |
| strict DD capacity loss | proved | exact positive algebraic difference (4.3) |
| MADD endpoint exclusion | proved relative to report-level chain | lower gap exceeds paired cavity capacity |
| uniform nonexplicit gap above `0.599785...` | proved | diagonal compactness argument |
| Level I | still open | larger pinned/contact currency remains feasible |

---

## 9. Next theorem

The paired-pocket loss should be made quantitative away from exact equality. The
natural variables are the projective missing gaps `alpha_i` of the normalized cyclic
force hull. Every gap produces two actual outer-pocket chains whose limiting lengths
are at least `sin(alpha_i/2)`. Before the scalar DD relaxation one therefore has a
cubic-moment capacity problem with **paired lower bounds**.

A sharp theorem of the form

\[
\sum_P\ell_P^3
\le
\mathcal M(L;\alpha_1,\alpha_2,\ldots)
< L^3
\]

combined with the exact circle formulas for perimeter and area would turn PP's
nonexplicit gap into a substantially stronger explicit feasible-region bound. The
one-gap case already suggests a threshold above `0.60`.
