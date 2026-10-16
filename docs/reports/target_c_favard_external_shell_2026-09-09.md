<!-- theorem-state: {"artifact_id":"ART-2EE0ACCCF6A5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Favard lens sharpening of the external force-hull phase

**Date:** 2026-09-09  
**Repository state:** current main through `58420d2f13ba3f75ea943d8b60e90b2984287081`, combined with PR #112  
**Run type:** literature import plus exact source-population consequence  
**Target:** Target C C-II / external completion shell  
**External literature:** Favard's planar perimeter-area-diameter extremal theorem, via Stefano Campi, *Three-dimensional Bonnesen type inequalities*, Le Matematiche 60 (2005), 425–431, Theorem 2.2 discussion; see also Campi–Gronchi, *A Favard-type problem for 3d convex bodies*, Bull. Lond. Math. Soc. 40 (2008), 604–612  
**Computation:** numerical constants only; proof analytic once Favard is imported

## LEVEL I STATUS

`STILL OPEN`

The companion ZX report bounds the force-hull area by the ordinary isoperimetric inequality and obtains a quadratic external-population floor whenever `h/D<pi/2`. That bound wastes the fact that the force hull itself contains a diameter-`D` pair.

Favard's classical extremal theorem identifies the sharp body for fixed perimeter and diameter: the symmetric lens. Importing that theorem strengthens the external-population coefficient while preserving the same exact threshold `h/D=pi/2`.

## 1. External theorem and applicability

Campi's formulation of Favard's theorem is as follows. For positive `L_0,A_0`, among planar convex bodies with perimeter at most `L_0` and area at least `A_0`, the symmetric lens is the unique body of maximum circumradius. Campi then notes explicitly that, because a symmetric lens has circumradius equal to half its diameter, the same lens is the unique body of maximum diameter in that class.

Reference:

- Stefano Campi, *Three-dimensional Bonnesen type inequalities*, Le Matematiche 60 (2005), 425–431, Section 2, Favard theorem.
- Modern provenance: Stefano Campi and Paolo Gronchi, *A Favard-type problem for 3d convex bodies*, Bull. Lond. Math. Soc. 40 (2008), 604–612, DOI `10.1112/blms/bdn039`.

The consequence needed here is the inverse extremal statement:

> among planar convex bodies of diameter exactly `D` and perimeter at most `P`, with `2D<=P<=pi D`, the maximum area is attained by the symmetric lens of diameter `D` and perimeter `P`.

This inversion is legitimate because, within the one-parameter symmetric-lens family of fixed perimeter, area increases strictly as diameter decreases from `P/2` to `P/pi`. If a diameter-`D` body of perimeter at most `P` had more area than the diameter-`D` lens, Favard applied with that larger area and perimeter allowance `P` would give a lens of diameter strictly below `D` as the maximum-diameter member of a class that already contains the proposed body, a contradiction.

No property specific to electrical networks or KKT stresses enters this imported convex-geometric step.

## 2. Exact symmetric-lens formula

Let `0<alpha<=pi/2`. A symmetric lens of diameter `D` is bounded by two equal circular arcs, each subtending central angle `2alpha`. Its circle radius is

\[
R=\frac{D}{2\sin\alpha}.
\]

Each boundary arc has length

\[
2\alpha R
= D\frac{\alpha}{\sin\alpha},
\]

so the total perimeter is

\[
\boxed{
P=2D\frac{\alpha}{\sin\alpha}.
}
\tag{FL.1}
\]

The two equal circular segments have total area

\[
\boxed{
A_{\rm lens}
=\frac{D^2}{2\sin^2\alpha}
\left(\alpha-\sin\alpha\cos\alpha\right).
}
\tag{FL.2}
\]

The map `alpha/sin(alpha)` increases from `1` to `pi/2` on `[0,pi/2]`. Thus for every normalized half-perimeter

\[
x:=\frac{P}{2D}\in[1,\pi/2]
\]

there is a unique `alpha=alpha(x)` satisfying

\[
\boxed{
\frac{\alpha}{\sin\alpha}=x.
}
\tag{FL.3}
\]

Define

\[
\mathcal L(x)
:=
\frac{\alpha(x)-\sin\alpha(x)\cos\alpha(x)}
{2\sin^2\alpha(x)}.
\tag{FL.4}
\]

Favard then gives the sharp area bound

\[
\boxed{
\operatorname{area}(K)\le D^2\mathcal L(P/(2D))
}
\tag{FL.5}
\]

for every convex diameter-`D` body with perimeter at most `P<=pi D`.

At `x=pi/2`, `alpha=pi/2` and `mathcal L=pi/4`, recovering the disk. For every `x<pi/2`, the inequality is strictly sharper than the ordinary isoperimetric estimate `P^2/(4pi)` for a body known to have diameter `D`.

## 3. Apply Favard to the force hull

In the post-ZF C65 source, the force hull `F` contains actual diameter endpoints and therefore has diameter exactly `D`. The survivor inequality and the outer-walk perimeter bound give

\[
\operatorname{per}(F)\le b\le b+Q\le2h.
\tag{3.1}
\]

Assume `h<=pi D/2`. Put

\[
x=\frac hD.
\]

Favard with `P=2h` yields

\[
\boxed{
\operatorname{area}(F)
\le D^2\mathcal L(x).
}
\tag{FL.6}
\]

Current-main OP gives

\[
 v+Z_{def}+Z_{in}
\le
\frac2{\sqrt3}\operatorname{area}(F)
+\frac12\operatorname{per}(F)+1.
\]

Since `per(F)<=2h`, subtract from `n`.

### Theorem FL.1 — sharp external-shell floor from Favard

For `h<=pi D/2`,

\[
\boxed{
Z_{ext}
\ge
n-
\frac{2D^2}{\sqrt3}\mathcal L(h/D)
-h-1.
}
\tag{FL.7}
\]

This improves ZX.1, which used the weaker area bound `h^2/pi`.

## 4. Asymptotic coefficient

Let

\[
\Delta=\frac\pi{2\sqrt3}
\]

and pass to a subsequence with

\[
\frac hD\to x\in[1,\pi/2].
\]

The global packing asymptotic `n/D^2->Delta` gives

\[
\boxed{
\liminf\frac{Z_{ext}}{D^2}
\ge
\Delta-rac2{\sqrt3}\mathcal L(x).
}
\tag{FL.8}
\]

The right side is positive for every `x<pi/2` and vanishes at `x=pi/2`. Thus the phase threshold remains sharp:

\[
\boxed{
h/D<\pi/2
\quad\Longrightarrow\quad
Z_{ext}=\Omega(D^2).
}
\tag{FL.9}
\]

At the current general post-ZF endpoint

\[
\tau_*=1.4781702664\ldots,
\]

the unique solution of

\[
\alpha/\sin\alpha=\tau_*
\]

is

\[
\alpha=1.4707837101\ldots,
\]

and

\[
\mathcal L(\tau_*)=0.6926232518\ldots .
\]

Therefore

\[
\boxed{
\liminf\frac{Z_{ext}}{D^2}
\ge
0.1071272403\ldots
}
\tag{FL.10}
\]

at that endpoint. The ordinary-isoperimetric ZX coefficient was `0.1038019123...`.

## 5. Why the threshold cannot move past pi/2 from perimeter alone

At `h/D=pi/2`, the survivor upper bound `per(F)<=2h` becomes the universal Rosenthal–Szasz upper bound `per(F)<=pi D`. The Favard extremizer becomes the diameter-`D` disk itself. Hence no argument that uses only

- `diam(F)=D`, and
- `per(F)<=2h`

can force a positive area deficit, or a positive external-population density, at or above `h/D=pi/2`.

This is an exact no-go statement for the current perimeter-capacity route. To push the external-shell phase beyond `pi/2`, one must use additional structure: the discrete diameter graph, contact-face defect, KKT/response data, or source-hull interface geometry.

## 6. Relation to shell regressions

The threshold has a natural shell interpretation. Large regular even polygons have opposite-pair diameter matchings with

\[
h/D\to\pi/2
\]

and convex hulls tending to the disk. They are not post-ZF global survivors—the clean-train theorem excludes their matching row count—but they show why the convex perimeter/diameter extremal itself loses all quantitative area deficit at `pi/2`.

Thus Favard both sharpens ZX and confirms that its phase boundary is geometrically real rather than an artifact of the ordinary isoperimetric inequality.

## 7. Promotion recommendation

**Hold as report pending literature/dependency review.**

If retained, add Favard to the literature baseline and replace the ordinary-isoperimetric coefficient in the external-shell continuation with FL.7–FL.10. Do not change the Level I status.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Favard (1929; modern statement in Campi 2005):
among convex plane bodies with given perimeter allowance and area floor,
the symmetric lens uniquely maximizes diameter. Inverted, the symmetric lens
maximizes area at fixed diameter D and perimeter P.

For P=2Dx, define alpha in [0,pi/2] by
    alpha/sin(alpha)=x.
Then
    A_lens/D^2 = L(x)
      = [alpha-sin(alpha)cos(alpha)]/[2 sin^2(alpha)].

Post-ZF has per(F)<=2h. For x=h/D<=pi/2:
    area(F)<=D^2 L(x).
OP therefore gives
    Z_ext >= n - (2/sqrt3)D^2 L(x) - h - 1.

If h/D->x:
    liminf Z_ext/D^2 >= Delta-(2/sqrt3)L(x).
Positive exactly for x<pi/2.
At tau_*=1.4781702664...:
    coefficient = 0.1071272403...
(up from 0.1038019123 under ordinary isoperimetry).

No perimeter/diameter-only argument can push the phase threshold beyond pi/2,
because the Favard extremizer becomes the disk there.
```
