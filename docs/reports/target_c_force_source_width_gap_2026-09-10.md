<!-- migration-source: path=docs/reports/target_c_force_source_width_gap_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=81355e579c72d04914560022a19ba4b6ff98607b; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — source/force perimeter loss forces a macroscopic diameter-direction gap

**Date:** 2026-09-10  
**Repository state:** PR #178 after PI commit `e8defbe79924b2932ef512dba4ad7c5d29056ad5`  
**Run type:** exact geometric transport / diameter-support reduction  
**Target:** Target C, C-II after ZF  
**Depends on:** C65 full actual diameter support on the force-visible core; CP full-source perimeter defect; PI explicit force-perimeter envelope  
**External web search:** Woodall straight-thrackle classification was checked as a possible continuation, but is not needed for the theorem proved here  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let

\[
F=\operatorname{conv}B_+\subseteq K=\operatorname{conv}A
\]

be the force hull and the full source hull of the lexicographically normalized C-II
source.  Both have diameter `D`.  Let

\[
\Theta_H\subset\mathbb R/\pi\mathbb Z
\]

be the set of unoriented directions of the **actual** diameter edges.  C65 identifies
their endpoints with force-visible loaded vertices, so every `theta in Theta_H` is a
width-`D` direction of both `F` and `K`.

Order the `h=|H|` distinct directions cyclically on the projective circle and let

\[
\gamma_1,\ldots,\gamma_h>0,
\qquad
\sum_i\gamma_i=\pi
\tag{WG.1}
\]

be the projective angular gaps.

The new exact inequality is

\[
\boxed{
\operatorname{per}K-\operatorname{per}F
\le
\frac D2\sum_{i=1}^h\gamma_i^2.
}
\tag{WG.2}
\]

Consequently

\[
\boxed{
\sum_i\gamma_i^2
\ge
\frac{2(\operatorname{per}K-\operatorname{per}F)}D,
}
\tag{WG.3}
\]

and, with `Gamma_H=max_i gamma_i`,

\[
\boxed{
\Gamma_H
\ge
\frac{2(\operatorname{per}K-\operatorname{per}F)}{\pi D}.
}
\tag{WG.4}
\]

Combining CP and PI, every fixed pinned/contact regime

\[
\limsup\frac{e_{BB}+2s_C}{D}\le\lambda_0<\lambda_{\rm disk}
\]

therefore has a **macroscopic hole in its actual diameter-direction support**:

\[
\boxed{
\liminf\Gamma_H
\ge
\frac{2}{\pi}\bigl(\pi-p_+(\lambda_0)\bigr)>0.
}
\tag{WG.5}
\]

This is qualitatively different from the previous scalar-surplus conclusions: low
surplus now removes an open interval of projective directions from the full actual
diameter graph.

---

## 1. Distinctness of diameter directions

No two distinct actual diameter edges have the same unoriented direction.

Indeed, two disjoint diameter edges belong to a straight-line diameter thrackle, so
they must cross and therefore cannot be parallel.  If two distinct diameter edges
share an endpoint and are parallel, their other endpoints lie either on the same ray
or opposite rays at distance `D` from the common endpoint.  The same-ray case gives
the same other endpoint; the opposite-ray case makes the two other endpoints distance
`2D`, impossible in a diameter-`D` set.  Thus the projective directions are distinct
and WG.1 is well-defined.

---

## 2. Width functions vanish together at every actual diameter direction

For a compact convex body `C`, write

\[
w_C(\theta)
\]

for its width in projective direction `theta`.

If `xy` is an actual diameter edge of direction `theta`, C65 puts `x,y in B_+`, hence
`x,y in F subseteq K`.  Their projection difference in direction `theta` is exactly
`D`.  Since both bodies have diameter at most `D`,

\[
\boxed{
w_F(\theta)=w_K(\theta)=D.}
\tag{WG.6}
\]

Therefore the nonnegative width difference

\[
g(\theta):=w_K(\theta)-w_F(\theta)
\tag{WG.7}
\]

satisfies

\[
\boxed{g(\theta)=0\quad(\theta\in\Theta_H).}
\tag{WG.8}
\]

This is the decisive source/force coupling.  It uses the **actual** diameter support;
a selected stress with missing actual diameter edges would not suffice.

---

## 3. Exact Lipschitz bound

For every diameter-`D` convex body `C`,

\[
\boxed{|w_C(\theta)-w_C(\phi)|\le D\,d_\pi(\theta,\phi),}
\tag{WG.9}
\]

where `d_pi` is projective angular distance.

### Proof

The width is the support function of the difference body:

\[
w_C(u)=h_{C-C}(u).
\]

Every vector of `C-C` has Euclidean norm at most `D`.  Hence for unit vectors `u,v`,

\[
|h_{C-C}(u)-h_{C-C}(v)|
\le D|u-v|
\le D\,\angle(u,v).
\]

Passing to unoriented directions gives WG.9. `square`

Applying WG.9 to both `K` and `F`,

\[
\boxed{|g(\theta)-g(\phi)|\le2D\,d_\pi(\theta,\phi).}
\tag{WG.10}
\]

---

## 4. Proof of the gap-energy inequality

Fix one projective gap of length `gamma`, parameterized by `0<=t<=gamma`, with actual
diameter directions at both endpoints.  By WG.8 and WG.10,

\[
g(t)
\le2D\min\{t,\gamma-t\}.
\tag{WG.11}
\]

Therefore

\[
\int_0^\gamma g(t)\,dt
\le
2D\int_0^\gamma\min\{t,\gamma-t\}\,dt
=\frac D2\gamma^2.
\tag{WG.12}
\]

Sum over all projective gaps.  Cauchy's width formula gives

\[
\int_0^\pi g(\theta)\,d\theta
=\operatorname{per}K-\operatorname{per}F.
\tag{WG.13}
\]

Equations WG.12--WG.13 prove WG.2 and WG.3.

Finally

\[
\sum_i\gamma_i^2
\le
\Gamma_H\sum_i\gamma_i
=\pi\Gamma_H,
\]

so WG.4 follows. `square`

---

## 5. Low-surplus consequence

CP proves for every global source

\[
\operatorname{per}K
>\pi D-\frac{\pi\sqrt3}{2}.
\tag{WG.14}
\]

PI proves that for every fixed `lambda_0<lambda_disk`, any unbounded post-ZF sequence
with

\[
\limsup\lambda_D
:=
\limsup\frac{e_{BB}+2s_C}{D}
\le\lambda_0
\]

satisfies

\[
\limsup\frac{\operatorname{per}F}{D}
\le p_+(\lambda_0)<\pi.
\tag{WG.15}
\]

Thus

\[
\liminf\frac{\operatorname{per}K-\operatorname{per}F}{D}
\ge\pi-p_+(\lambda_0).
\tag{WG.16}
\]

Insert this into WG.3--WG.4 to obtain

\[
\boxed{
\liminf\sum_i\gamma_i^2
\ge2\bigl(\pi-p_+(\lambda_0)\bigr),
}
\tag{WG.17}
\]

and WG.5.

For orientation only, at `lambda_0=0.60`, PI gives
`p_+(lambda_0)=3.029400052854...`, so the actual diameter directions omit an interval
of asymptotic projective length at least

\[
0.07142\ldots\text{ radians}\approx4.09^\circ.
\]

No decimal is used in the proof.

---

## 6. Exact effect on the C-II endpoint

The low-surplus AS/PI branch now has all of the following simultaneously:

1. `K` has perimeter `pi D-O(1)`;
2. `F` loses a fixed linear amount of perimeter;
3. a positive fraction of all source points are contact-isolated outside `F`;
4. those external points saturate the annular area to triangular density up to `O(D)`;
5. the actual diameter graph has a projective angular gap of fixed positive size.

The fifth item is new.  It separates the low-surplus branch from regular odd shells,
whose diameter directions become uniformly dense around the projective circle.

It also identifies where a closing diameter-thrackle theorem would enter: one no
longer needs to exclude arbitrary large thrackles, only the Woodall
caterpillar/spiked-odd-cycle possibilities whose unit-separated diameter realization
has a fixed missing interval of projective directions while the full source hull has
only `O(1)` integrated width defect.

---

## 7. Regressions and limits

- **Unit square:** compatible.  Its two diameter directions have gaps `pi/2`; WG is a
  finite geometric inequality and makes no large-source claim.
- **Regular odd shell:** compatible and excluded from the low-surplus consequence;
  `P_K=P_F`, so WG.2 carries no gap energy.
- **Dense isolated odd-shell filling:** same.  Its force/source perimeter difference is
  zero, so no false directional-gap conclusion is produced.
- **Star-like diameter supports:** not excluded.  A large directional gap is compatible
  with a diameter star; ZS independently proves that a large post-ZF support has
  linearly many edges outside every single star, but not a quantitative direction
  distribution.
- **Near-diameter directions:** WG concerns only exact actual diameter edges.  A dense
  family of chords of length `D-o(D)` may still cross the omitted direction interval.

Thus WG is a genuine structural reduction but not yet a contradiction.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| actual diameter directions are distinct | proved | straight-thrackle intersection plus diameter bound |
| width equality WG.6 | proved | C65 full actual support on `B_+` |
| width Lipschitz WG.9 | proved | difference body lies in radius-`D` disk |
| gap-energy WG.2--WG.4 | proved | exact integration between zeros |
| low-surplus macroscopic direction hole WG.5 | proved | CP + PI + WG |
| fixed direction hole contradicts C-II | not proved | star/caterpillar diameter regressions remain |
| Level I | still open | need a geometric thrackle or finite-capacity closure |

---

## 9. Next obligation

The strongest continuation is now a geometric diameter-thrackle statement, not another
area bound:

> **WGT.**  In the lexicographically normalized post-ZF source, combine the Woodall
> straight-thrackle structure of `H`, ZS (`q>=h>=D` and linear off-star support), the
> C18 shared-endpoint angle bound, and the full-source `O(1)` integrated width defect to
> show that the fixed projective gap in WG.5 either forces a strict sub-`D` competitor
> or forces enough contact/face surplus to violate `b+Q<=2h`.

Woodall's classification was checked externally: a finite straight-line thrackle is
either a disjoint union of caterpillars or has an odd cycle with every vertex adjacent
to that cycle.  It should be imported only with exact primary-source provenance if WGT
uses it in a proof.
